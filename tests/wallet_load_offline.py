"""Offline proof for L13 (block 4): an existing wallet is loaded, not
re-created, before a redeem signs.

The tool must work with a PRE-EXISTING, already-funded wallet file (one a
user imported or topped up). A bug that only `create()`s when the file is
absent, and never `load()`s an existing one, leaves `wallet.data` as None
so any later signing crashes with "'NoneType' object is not subscriptable".

This proof runs the full preview-then-redeem path against a wallet FILE that
already exists (a seed on disk, exactly as ~/.nano-pay/wallet.json looks),
monkeypatching the module-level request_with_payment so the redeem hands the
signing wallet back to us. We assert:
  - the pre-existing wallet's seed was loaded (wallet.data is a dict with a
    seed) at redeem time, i.e. the tool called load(), not create() with a
    brand-new random seed;
  - the redeem completes with a settled receipt (the loaded wallet signed).

No real Nano network and no wallet spend happen here.

Prints WALLET_LOAD_OK on success; any broken assertion raises first.
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

# A stable seed we write into the pre-existing wallet file. We must be able
# to tell it apart from any freshly random seed the tool might create().
EXISTING_SEED = "a2cf" + "0" * 60  # 64 hex chars, clearly not random


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
            "amount": "20000000000000000000000000000",  # 0.02 XNO, under cap
            "payTo": "nano_testpay",
        }],
    }
    hdr = base64.b64encode(json.dumps(envelope).encode()).decode()
    return types.SimpleNamespace(status_code=402, text="", headers={"payment-required": hdr})


wallets_seen = []  # the wallet objects handed to request_with_payment for redeem


def fake_request_with_payment(method, url, wallet, rpc, max_raw, headers=None, dry_run=False, **kw):
    if dry_run:
        resp = _quote_response()
        from nano_pay.x402 import parse_quote
        return resp, parse_quote(resp)
    wallets_seen.append(wallet)  # capture the wallet the tool intends to sign with
    rec = {"amount_xno": "0.02", "pay_to": "nano_testpay",
           "block": "BLOADED", "settled": True, "ledger": "confirmed"}
    return _quote_response(), rec


def main():
    tool.request_with_payment = fake_request_with_payment
    try:
        with tempfile.TemporaryDirectory() as td:
            # A wallet file that ALREADY exists when the tool starts, holding
            # a known seed (mirrors an imported / topped-up ~/.nano-pay/wallet.json).
            walletp = os.path.join(td, "wallet.json")
            with open(walletp, "w") as f:
                json.dump({"seed": EXISTING_SEED, "index": 0,
                           "representative": "nano_rep",
                           "work_cache": {}}, f)

            tt = tool.make_nano_x402_tool(wallet_path=walletp, rpc=OfflineRPC(), default_max_xno="0.05")
            from agents.tool_context import ToolContext
            ctx = ToolContext(context={"nano": True}, tool_name=tt.name,
                              tool_arguments="{}", tool_call_id="call_l13_1")

            async def run():
                out = await tt.on_invoke_tool(ctx, json.dumps(
                    {"url": "http://127.0.0.1/x", "dry_run": True}))
                assert out.startswith("QUOTE"), out
                m = re.search(r"quote_token: (\S+)", out)
                assert m, f"no quote_token in output: {out!r}"
                return await tt.on_invoke_tool(ctx, json.dumps({
                    "url": "http://127.0.0.1/x", "dry_run": False, "quote_token": m.group(1)}))

            out = asyncio.run(run())

        assert out.startswith("PAID"), f"redeem must settle with a loaded wallet: {out!r}"
        assert wallets_seen, "the redeem never handed a wallet to request_with_payment"
        w = wallets_seen[0]
        # The wallet loaded must be the PRE-EXISTING one (our known seed),
        # not a freshly created random one.
        assert isinstance(w.data, dict) and w.data.get("seed") == EXISTING_SEED, (
            "existing wallet was NOT loaded — tool re-created it with a new seed; "
            f"wallet.data.seed={w.data.get('seed') if isinstance(w.data, dict) else None!r}")
    finally:
        tool.request_with_payment = ORIGINAL_REQUEST

    print("WALLET_LOAD_OK")


if __name__ == "__main__":
    main()
