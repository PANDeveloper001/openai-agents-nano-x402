"""Offline proof for L11 (block 3): a redeem result is never headed PAID
unless the ledger confirmed settlement.

Driven through the real tool redeem path (preview mint, token reject gate,
then the receipt formatter), with the module-level request_with_payment
monkeypatched to hand back a chosen receipt:
  - settled True        -> receipt headed PAID, block shown;
  - settled False       -> NOT headed PAID, names the failure, block shown;
  - settled indeterminate -> NOT headed PAID, warns to check the hash.

No real Nano network and no wallet spend happen here.

Prints RECEIPT_HONESTY_OK on success; any broken assertion raises first.
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

ORIGINAL_REQUEST = tool.request_with_payment


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


def redeem_out(receipt_settled) -> str:
    """Run one full preview-then-redeem through the tool, monkeypatching
    request_with_payment to return a receipt with the wanted settled verdict."""

    def fake_request_with_payment(method, url, wallet, rpc, max_raw, headers=None, dry_run=False, **kw):
        if dry_run:
            resp = _quote_response()
            from nano_pay.x402 import parse_quote
            return resp, parse_quote(resp)
        rec = {"amount_xno": "0.02", "pay_to": "nano_testpay",
               "block": "ABB100", "settled": receipt_settled}
        if receipt_settled is True:
            rec["ledger"] = "confirmed"
            rec["note"] = "payment is on the ledger"
        elif receipt_settled is False:
            rec["ledger"] = "present"
            rec["note"] = "merchant refused and the ledger does not hold the block; nothing was paid"
        else:
            rec["ledger"] = "unconfirmed"
            rec["note"] = "no confirmation from merchant or ledger; check this hash before paying again"
        return _quote_response(), rec

    tool.request_with_payment = fake_request_with_payment
    try:
        with tempfile.TemporaryDirectory() as td:
            walletp = os.path.join(td, "wallet.json")
            tt = tool.make_nano_x402_tool(wallet_path=walletp, rpc=OfflineRPC(), default_max_xno="0.05")

            async def run():
                from agents.tool_context import ToolContext
                ctx = ToolContext(context={"nano": True}, tool_name=tt.name,
                                  tool_arguments="{}", tool_call_id="call_l11_1")
                out = await tt.on_invoke_tool(ctx, json.dumps(
                    {"url": "http://127.0.0.1/x", "dry_run": True}))
                assert out.startswith("QUOTE"), out
                m = re.search(r"quote_token: (\S+)", out)
                assert m, f"no quote_token in output: {out!r}"
                return await tt.on_invoke_tool(ctx, json.dumps({
                    "url": "http://127.0.0.1/x", "dry_run": False, "quote_token": m.group(1)}))

            return asyncio.run(run())
    finally:
        tool.request_with_payment = ORIGINAL_REQUEST


def main():
    # settled True -> PAID is truthful, block shown.
    out = redeem_out(True)
    assert out.startswith("PAID (Nano x402):"), f"settled True must be headed PAID: {out!r}"
    assert "ABB100" in out, "a settled receipt must show the block hash"

    # settled False -> never headed PAID.
    out = redeem_out(False)
    assert not out.startswith("PAID"), f"settled False must never start 'PAID: {out!r}"
    assert "NOT PAID" in out, f"settled False must name the failure: {out!r}"
    assert "ABB100" in out, "the block hash must still be shown"

    # settled indeterminate -> never headed PAID, warns to check the hash.
    out = redeem_out("indeterminate")
    assert not out.startswith("PAID"), f"indeterminate must never start 'PAID: {out!r}"
    assert "UNCONFIRMED" in out or "UNCERTAIN" in out, out
    assert "ABB100" in out, "the block hash must still be shown"

    print("RECEIPT_HONESTY_OK")


if __name__ == "__main__":
    main()