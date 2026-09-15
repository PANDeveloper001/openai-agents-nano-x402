"""Offline two-phase gate proof for L2 (block 2).

Runs a local HTTP 402 server (no real network, no real wallet spend) and proves
the two-phase quote-redeem gate:
  1. dry_run=True mints a single-use quote_token bound to the exact offer.
  2. redeem without a token                -> REFUSED (missing)
  3. redeem with a bogus token             -> REFUSED (invalid or already used)
  4. redeem with the matching token        -> token gate OPENS (payment then
     fails only on an injected offline RPC, i.e. the refusal path was passed;
     nothing on a real ledger was touched).
  5. redeeming the SAME token again        -> REFUSED (single-use)
  6. redeem where the endpoint's offer changed since the preview
                                           -> REFUSED (offer changed)

Prints TWO_PHASE_OK on success and exits 0 (the ledger oracle's expected
output); any broken assertion raises before that marker prints.
"""
import asyncio
import base64
import json
import os
import re
import sys
import tempfile
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

# Make the package importable from src/
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from agents.tool_context import ToolContext
from openai_agents_nano.tool import make_nano_x402_tool

PAY_TO = "nano_1x9k4qmqwc6f9amcq8gdgyb1gm7b3s5w1kzn9aafoza3tr4tbrmq1j4xyg4z"
LOW_RAW = "100000000000000000000000000000"  # 0.1 XNO
SMALL_RAW = "20000000000000000000000000000"  # 0.02 XNO (under the 0.05 cap)
HIGH_RAW = "1000000000000000000000000000000"  # 1.0 XNO
CAP = "0.05"


def make_quote(raw_amount: str) -> bytes:
    envelope = {
        "x402Version": 1,
        "accepts": [
            {
                "scheme": "exact",
                "protocolScheme": "exact",
                "network": "nano:mainnet",
                "asset": "XNO",
                "amount": raw_amount,
                "payTo": PAY_TO,
            }
        ],
    }
    return base64.b64encode(json.dumps(envelope).encode())


class Handler(BaseHTTPRequestHandler):
    """/stable always serves the LOW offer. /flip serves LOW once then HIGH."""

    flip_calls = 0

    def do_GET(self):
        # /small: always an under-cap offer (gate may open, then payment must
        # fail only on the offline RPC). /stable: always LOW (over-cap).
        # /flip: LOW once then HIGH (offer change between preview and redeem).
        if self.path.startswith("/small"):
            raw = SMALL_RAW
        elif self.path.startswith("/flip"):
            Handler.flip_calls += 1
            raw = HIGH_RAW if Handler.flip_calls > 1 else LOW_RAW
        else:
            raw = LOW_RAW
        self.send_response(402)
        self.send_header("payment-required", make_quote(raw).decode())
        self.send_header("Content-Length", "0")
        self.end_headers()

    def log_message(self, format, *args):  # noqa: A002
        pass


class OfflineRPC:
    """Any RPC call raises immediately: payment can never touch a real node."""

    def __getattr__(self, name):
        def _fail(*a, **k):
            raise RuntimeError("offline rpc")

        return _fail


async def invoke(tool, json_args: str) -> str:
    ctx = ToolContext(
        context={"nano": True},
        tool_name=tool.name,
        tool_arguments=json_args,
        tool_call_id="call_test_01",
    )
    return await tool.on_invoke_tool(ctx, json_args)


def token_from(text: str) -> str:
    m = re.search(r"quote_token: (\S+)", text)
    assert m, f"no quote_token in output: {text!r}"
    return m.group(1)


def main():
    srv = HTTPServer(("127.0.0.1", 0), Handler)
    port = srv.server_address[1]
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{port}"

    with tempfile.TemporaryDirectory() as td:
        walletp = str(Path(td) / "wallet.json")
        tool = make_nano_x402_tool(
            wallet_path=walletp, rpc=OfflineRPC(), default_max_xno=CAP
        )

        def frontier():
            if not os.path.exists(walletp):
                return None
            try:
                import json as _j

                d = _j.load(open(walletp))
                for k in ("frontier", "new_frontier"):
                    if d.get(k):
                        return d[k]
                return d.get("block") or None
            except Exception:
                return None

        # 1) dry_run mints a single-use token and spends nothing.
        out = asyncio.run(invoke(tool, json.dumps({"url": f"{base}/stable", "dry_run": True})))
        assert out.startswith("QUOTE"), out
        t1 = token_from(out)
        assert frontier() is None, "dry_run must not create a frontier (no spend)"

        # 2) redeem without a token -> REFUSED (missing).
        out = asyncio.run(invoke(tool, json.dumps({"url": f"{base}/stable", "dry_run": False})))
        assert out.startswith("REFUSED") and "no quote token" in out, out

        # 3) redeem with a bogus token -> REFUSED (invalid).
        out = asyncio.run(invoke(tool, json.dumps({
            "url": f"{base}/stable", "dry_run": False, "quote_token": "forged-token"})))
        assert out.startswith("REFUSED") and "invalid or already used" in out, out

        # 4) redeem /small (under-cap) with the matching token -> gate opens,
        #    payment proceeds and fails only on the offline RPC (the refusal
        #    path was NOT taken; nothing on a real ledger was touched).
        out = asyncio.run(invoke(tool, json.dumps({"url": f"{base}/small", "dry_run": True})))
        assert out.startswith("QUOTE"), out
        ts = token_from(out)
        out = asyncio.run(invoke(tool, json.dumps({
            "url": f"{base}/small", "dry_run": False, "quote_token": ts})))
        assert not out.startswith("REFUSED"), f"token gate must open: {out}"
        assert out.startswith("ERROR: payment or request failed"), out

        # 5) single-use: the same token is spent after (4).
        out = asyncio.run(invoke(tool, json.dumps({
            "url": f"{base}/small", "dry_run": False, "quote_token": ts})))
        assert out.startswith("REFUSED") and "invalid or already used" in out, out

        # 6) offer changed between preview and redeem -> REFUSED (offer-changed).
        out = asyncio.run(invoke(tool, json.dumps({"url": f"{base}/flip", "dry_run": True})))
        assert out.startswith("QUOTE"), out
        tf = token_from(out)
        out = asyncio.run(invoke(tool, json.dumps({
            "url": f"{base}/flip", "dry_run": False, "quote_token": tf})))
        assert out.startswith("REFUSED") and "changed its price or pay_to" in out, out

        assert frontier() is None, "no real block may ever be signed in this proof"
        print("TWO_PHASE_OK")


if __name__ == "__main__":
    main()