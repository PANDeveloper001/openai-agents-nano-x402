"""Offline fail-closed proof for L1.

Runs a local HTTP 402 server (no real network, no real wallet spend) and proves:
  1. dry_run=True spends nothing: returns a QUOTE, never signs or broadcasts.
  2. a price above the cap returns a REFUSAL string and never signs.

Prints FAIL_CLOSED_OK on success (the ledger oracle's expected output) and exits 0.
"""
import asyncio
import base64
import json
import os
import sys
import tempfile
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

# Make the package importable from src/
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from agents.tool_context import ToolContext
from openai_agents_nano.tool import make_nano_x402_tool

# A payment-required envelope with a single x402nano exact offer.
PAY_TO = "nano_1x9k4qmqwc6f9amcq8gdgyb1gm7b3s5w1kzn9aafoza3tr4tbrmq1j4xyg4z"


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


LOW_RAW = "100000000000000000000000000000"  # 0.1 XNO
HIGH_RAW = "1000000000000000000000000000000"  # 1.0 XNO
CAP = "0.05"  # tool default cap below the low price


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(402)
        raw = HIGH_RAW if self.path.startswith("/high") else LOW_RAW
        self.send_header("payment-required", make_quote(raw).decode())
        self.send_header("Content-Length", "0")
        self.end_headers()

    def log_message(self, format, *args):  # noqa: A002
        pass


async def invoke(tool, json_args: str) -> str:
    ctx = ToolContext(
    context={"nano": True},
    tool_name=tool.name,
    tool_arguments=json_args,
    tool_call_id="call_test_01",
)
    return await tool.on_invoke_tool(ctx, json_args)


def main():
    srv = HTTPServer(("127.0.0.1", 0), Handler)
    port = srv.server_address[1]
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{port}"

    with tempfile.TemporaryDirectory() as td:
        walletp = str(Path(td) / "wallet.json")
        tool = make_nano_x402_tool(wallet_path=walletp, default_max_xno=CAP)

        def frontier():
            """Return the wallet's recorded frontier, or None if never opened."""
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

        # 1) dry_run spends nothing -> QUOTE text, and the wallet gained no
        #    frontier/balance (no block was ever signed or broadcast).
        out = asyncio.run(
            invoke(tool, json.dumps({"url": f"{base}/low", "dry_run": True}))
        )
        assert out.startswith("QUOTE"), out
        assert "0.1 XNO" in out, out
        assert frontier() is None, "dry_run must not create a frontier (no spend)"

        # 2) price above cap with dry_run=False -> REFUSED, no spend. The
        #    two-phase gate (block 2) requires a quote token minted by a prior
        #    dry-run of the SAME offer; mint it on /high, then the over-cap
        #    offer must still be refused without signing even though the token
        #    is valid.
        import re as _re

        _preview = asyncio.run(
            invoke(tool, json.dumps({"url": f"{base}/high", "dry_run": True}))
        )
        assert _preview.startswith("QUOTE"), _preview
        _m = _re.search(r"quote_token: (\S+)", _preview)
        assert _m, f"no quote_token in dry-run output: {_preview!r}"
        cap_ok_token = _m.group(1)
        out2 = asyncio.run(
            invoke(tool, json.dumps({
                "url": f"{base}/high", "dry_run": False,
                "quote_token": cap_ok_token,
            }))
        )
        assert out2.startswith("REFUSED"), out2
        assert "1 XNO" in out2 and "0.05 XNO" in out2, out2
        assert frontier() is None, "cap refusal must not create a frontier (no spend)"

        print("FAIL_CLOSED_OK")


if __name__ == "__main__":
    main()