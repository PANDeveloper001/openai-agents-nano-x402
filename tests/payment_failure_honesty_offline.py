"""Offline proof for L12 (block 3): a redeem whose merchant never replied
reports the signed block and the ledger verdict, so the agent never re-pays
blind.

feeless402 raises PaidRequestFailed when a signed payment block was handed to
the merchant and no HTTP reply came back. The adapter must surface that
receipt (block hash, settled, note) instead of a generic ERROR, and must tell
the agent to re-present the SAME block rather than pay again. No real Nano
network and no wallet spend happen here: the module-level request_with_payment
is monkeypatched to a fake that raises PaidRequestFailed.

Prints PAYMENT_FAILURE_HONESTY_OK on success; a broken assertion raises first.
"""
import asyncio
import base64
import json
import os
import re
import sys
import tempfile
import types

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

os.environ.setdefault("X402_MAX_XNO", "0.05")

import openai_agents_nano.tool as tool
from nano_pay.x402 import PaidRequestFailed


class OfflineRPC:
    def __getattr__(self, name):
        def _fail(*a, **k):
            raise RuntimeError("offline rpc")

        return _fail


def _quote_response() -> types.SimpleNamespace:
    envelope = {
        "x402Version": 1,
        "accepts": [{
            "scheme": "exact", "protocolScheme": "exact",
            "network": "nano:mainnet", "asset": "XNO",
            "amount": "20000000000000000000000000000",  # 0.02 XNO, under the cap
            "payTo": "nano_testpay",
        }],
    }
    hdr = base64.b64encode(json.dumps(envelope).encode()).decode()
    return types.SimpleNamespace(status_code=402, text="", headers={"payment-required": hdr})


def fake_request_with_payment(method, url, wallet, rpc, max_raw, headers=None, dry_run=False, **kw):
    """Quote path succeeds; the redeem path loses the reply after signing."""
    if dry_run:
        resp = _quote_response()
        from nano_pay.x402 import parse_quote
        return resp, parse_quote(resp)
    rec = {
        "amount_xno": "0.02",
        "pay_to": "nano_testpay",
        "block": "AABBCCDD",
        "settled": "indeterminate",
        "ledger": "unconfirmed",
        "note": "no confirmation from merchant or ledger; check this hash before paying again",
    }
    raise PaidRequestFailed("no reply from merchant", rec)


async def invoke(tool_obj, json_args: str) -> str:
    from agents.tool_context import ToolContext
    ctx = ToolContext(context={"nano": True}, tool_name=tool_obj.name,
                      tool_arguments=json_args, tool_call_id="call_l12_1")
    return await tool_obj.on_invoke_tool(ctx, json_args)


def token_from(text: str) -> str:
    m = re.search(r"quote_token: (\S+)", text)
    assert m, f"no quote_token in output: {text!r}"
    return m.group(1)


def main():
    real = tool.request_with_payment
    tool.request_with_payment = fake_request_with_payment
    try:
        with tempfile.TemporaryDirectory() as td:
            walletp = os.path.join(td, "wallet.json")
            t = tool.make_nano_x402_tool(wallet_path=walletp, rpc=OfflineRPC(), default_max_xno="0.05")
            out = asyncio.run(invoke(t, json.dumps({"url": "http://127.0.0.1/x", "dry_run": True})))
            assert out.startswith("QUOTE"), out
            tok = token_from(out)
            out = asyncio.run(invoke(t, json.dumps({
                "url": "http://127.0.0.1/x", "dry_run": False, "quote_token": tok})))
            assert out, "redeem must produce some output"
            assert "AABBCCDD" in out, f"must surface the signed block hash: {out!r}"
            assert "indeterminate" in out or "unconfirmed" in out, f"must surface the ledger verdict: {out!r}"
            assert not out.startswith("ERROR: payment or request failed"), out
            lowered = out.lower()
            assert "re-present" in lowered or "same block" in lowered or "do not re-pay" in lowered, \
                f"must warn against paying again: {out!r}"
    finally:
        tool.request_with_payment = real

    print("PAYMENT_FAILURE_HONESTY_OK")


if __name__ == "__main__":
    main()