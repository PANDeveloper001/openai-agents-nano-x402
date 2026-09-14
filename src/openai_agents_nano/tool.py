"""Thin OpenAI Agents SDK adapter that reuses feeless402's Nano client.

`make_nano_x402_tool(...)` returns an OpenAI Agents SDK `FunctionTool` named
`nano_x402_fetch`. It binds a self-custodied Nano `Wallet` and an `RPC` once at
construction — the model never sees a wallet path, seed or RPC URL. Every spend
goes through feeless402's `request_with_payment`, so no Nano payment logic is
rebuilt here.

Tool behaviour
--------------
- `dry_run=True` is spendless: it runs `request_with_payment(dry_run=True)`,
  which stops after the server's 402 quote, and returns agent-readable quote
  text (price, pay_to, cap) without signing or broadcasting anything.
- `dry_run=False` first reads the spendless quote, and refuses with a plain
  refusal string (not an exception the model can loop around) if the price is
  above the applied cap. Only then does it call `request_with_payment(...)`,
  which signs locally, retries with the payment header, and verifies on the
  ledger. The applied cap is `min(max_xno, default_max_xno)`.
- Payments that share one wallet are serialised with an `asyncio.Lock`
  (Nano blocks are stateful and non-replayable: parallel sends from one wallet
  would race on the frontier/nonce), exactly as the design requires.
- The return value is agent-readable text: on success a receipt with status,
  body, amount_xno, pay_to, block, settled, ledger, note; on a cap refusal a
  short refusal.
"""
from __future__ import annotations

import asyncio
import os
from decimal import Decimal
from pathlib import Path
from typing import Optional

try:  # the Agents SDK is imported lazily so the core adapter is importable alone
    from agents import FunctionTool, function_tool
except Exception:  # pragma: no cover - optional dependency
    FunctionTool = None
    function_tool = None

from nano_pay.rpc import RPC
from nano_pay.wallet import Wallet
from nano_pay.x402 import request_with_payment
from nano_pay import xno_to_raw, raw_to_xno

DEFAULT_WALLET_ENV = "X402_WALLET_PATH"
DEFAULT_WALLET_PATH = "~/.nano-pay/wallet.json"
DEFAULT_MAX_XNO = os.environ.get("X402_MAX_XNO", "0.01")  # hard default cap


class NanoX402ToolError(Exception):
    """Raised only for conditions the tool cannot represent as text."""


def _wallet_path(wallet_path: Optional[str]) -> str:
    if wallet_path is not None:
        return wallet_path
    return os.environ.get(DEFAULT_WALLET_ENV, DEFAULT_WALLET_PATH)


def _apply_cap(requested: Optional[str], default: str) -> Decimal:
    """The applied cap is min(requested, default); a bad requested value is refused."""
    cap = Decimal(str(default))
    if requested is not None and str(requested).strip() != "":
        try:
            req = Decimal(str(requested))
        except Exception:
            raise ValueError(f"max_xno is not a number: {requested!r}")
        if req < 0:
            raise ValueError(f"max_xno must be >= 0: {requested!r}")
        cap = min(cap, req)
    return cap


def _format_quote(quote: dict, cap_xno: str) -> str:
    return (
        "QUOTE (dry run, nothing spent):\n"
        f"  price:  {quote.get('amount_xno')} XNO\n"
        f"  pay_to: {quote.get('pay_to')}\n"
        f"  cap:    {cap_xno} XNO (refusing to pay more than this)\n"
        "Call again with dry_run=false to pay this amount."
    )


def _format_refusal(price_xno: str, cap_xno: str) -> str:
    return (
        "REFUSED: the endpoint's price is above your cap.\n"
        f"  price: {price_xno} XNO\n"
        f"  cap:   {cap_xno} XNO\n"
        "Nothing was paid. Raise max_xno (or the tool's default cap) if you "
        "intend to pay this endpoint."
    )


def _format_receipt(resp, receipt: dict, cap_xno: str) -> str:
    lines = [
        "PAID (Nano x402):",
        f"  status:    {resp.status_code}",
        f"  amount:    {receipt.get('amount_xno')} XNO  (cap {cap_xno})",
        f"  pay_to:    {receipt.get('pay_to')}",
        f"  block:     {receipt.get('block')}",
        f"  settled:   {receipt.get('settled')}",
        f"  ledger:    {receipt.get('ledger')}",
    ]
    note = receipt.get("note")
    if note:
        lines.append(f"  note:      {note}")
    lines.append("  body:")
    try:
        body = resp.text
    except Exception:
        body = ""
    body = (body or "").strip()
    lines.append(body[:4000] if body else "  (empty response body)")
    return "\n".join(lines)


def make_nano_x402_tool(
    wallet_path: Optional[str] = None,
    rpc: Optional[RPC] = None,
    default_max_xno: Optional[str] = None,
) -> FunctionTool:
    """Return an OpenAI Agents SDK FunctionTool named ``nano_x402_fetch``.

    wallet_path: path to the self-custodied Nano wallet. Default: the
      ``X402_WALLET_PATH`` env var, else ``~/.nano-pay/wallet.json``.
    rpc: a feeless402 ``RPC``. Default: a fresh ``RPC()`` against public nodes.
    default_max_xno: the hard cap when the model does not pass one. Default:
      the ``X402_MAX_XNO`` env var, else 0.01 XNO.
    """
    if function_tool is None:  # pragma: no cover - optional dependency
        raise ImportError(
            "openai-agents is not installed; install with `pip install "
            "openai-agents-nano[x402]` or `pip install openai-agents`."
        )
    wallet = Wallet(Path(_wallet_path(wallet_path)).expanduser())
    rpc = rpc or RPC()
    default_cap = str(default_max_xno or DEFAULT_MAX_XNO)
    lock = asyncio.Lock()

    @function_tool(
        name_override="nano_x402_fetch",
        description_override=(
            "Fetch an HTTP resource that requires an x402 payment, paying in "
            "self-custodied Nano (XNO). Use dry_run=true first to see the price "
            "and the cap (nothing is spent). If the price is below the cap and "
            "you intend to pay, call with dry_run=false: it pays from the "
            "configured wallet and returns the resource body plus the on-ledger "
            "receipt. Never pay more than necessary; keep max_xno small."
        ),
    )
    async def _nano_x402_fetch(
        url: str,
        method: str = "GET",
        json_body: str = "",
        max_xno: Optional[str] = None,
        dry_run: bool = False,
    ) -> str:
        if not wallet.exists():
            wallet.create()
        try:
            cap_xno = str(_apply_cap(max_xno, default_cap))
        except ValueError as e:
            return f"REFUSED: {e}"
        cap_raw = xno_to_raw(cap_xno)

        req_kwargs = {}
        if json_body:
            import json as _json

            try:
                req_kwargs["json"] = _json.loads(json_body)
            except Exception:
                req_kwargs["data"] = json_body

        async with lock:  # one wallet, stateful non-replayable Nano blocks
            try:
                # Spendless quote first: never sign or broadcast on dry_run.
                _resp, quote = await asyncio.to_thread(
                    request_with_payment,
                    method, url, wallet, rpc, cap_raw,
                    headers={"x-x402": "true"},
                    dry_run=True,
                    **req_kwargs,
                )
            except Exception as e:
                return f"ERROR: could not read the x402 quote: {e}"
            if dry_run:
                if quote is None:
                    return f"NOTE: {url} returned {_resp.status_code}, not a 402 x402 quote; nothing spent."
                return _format_quote(quote, cap_xno)

            # Not dry_run: confirm the price is within the applied cap before signing.
            price_raw = int(quote.get("amount_raw") or 0)
            if quote is None or price_raw > cap_raw:
                return _format_refusal(
                    raw_to_xno(price_raw) if quote else "?",
                    cap_xno,
                )

            try:
                resp, receipt = await asyncio.to_thread(
                    request_with_payment,
                    method, url, wallet, rpc, cap_raw,
                    headers={"x-x402": "true"},
                    dry_run=False,
                    **req_kwargs,
                )
            except Exception as e:
                return f"ERROR: payment or request failed: {e}"
            receipt = receipt or {}
            return _format_receipt(resp, receipt, cap_xno)

    return _nano_x402_fetch


__all__ = ["make_nano_x402_tool", "NanoX402ToolError"]