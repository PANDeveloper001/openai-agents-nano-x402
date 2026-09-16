#!/usr/bin/env python3
"""A minimal x402 seller route priced ONLY in Nano (XNO). Stdlib only.

Why this exists: every Nano-priced route in the CDP x402 Bazaar today is *advertised
next to* a USDC accept, never on its own. This server answers that question with a
measurement instead of a guess -- it publishes a route whose accepts[] contains one
entry, nano:mainnet/XNO, and nothing else, so Coinbase's keyless validator can be
pointed at it to see whether an XNO-only route is acceptable to the facilitator.

It also happens to be a genuinely buyable endpoint: paying the advertised amount to
the advertised payTo in XNO is the whole protocol. There is no account and no key.

Routes:
  GET /                     free  -- human/agent readable service card
  GET /.well-known/x402     free  -- the same declaration machines read
  GET /x402/nano-quote      PAID  -- 402 + accepts[] (nano:mainnet, asset XNO)

Run:  python3 server.py --port 8421 [--pay-to nano_...] [--amount 100000000000000]
Then point the CDP validator at the public URL of /x402/nano-quote.
"""
from __future__ import annotations

import argparse
import base64
import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse

PAID_PATH = "/x402/nano-quote"
DEFAULT_AMOUNT = "1000000000000000000000000000"  # 1e27 raw = 0.001 XNO (30 decimals)


def declaration(base_url: str, pay_to: str, amount: str) -> dict:
    """The x402 v2 PaymentRequired object, Nano-only."""
    resource_url = base_url.rstrip("/") + PAID_PATH
    accepts = [
        {
            "scheme": "exact",
            "network": "nano:mainnet",
            "amount": amount,
            "asset": "XNO",
            "payTo": pay_to,
            "maxTimeoutSeconds": 300,
            "extra": {"asset": "XNO", "work": "required", "workThreshold": "fffffff800000000"},
        }
    ]
    return {
        "x402Version": 2,
        "error": "Payment required",
        "resource": {
            "url": resource_url,
            "description": (
                "One machine-readable Nano network fact (confirmation time and a live "
                "block height) delivered for a Nano micropayment. Nano-only: this route "
                "accepts no stablecoin."
            ),
            "mimeType": "application/json",
            "serviceName": "XNO-only quote",
            "tags": ["nano", "xno", "payment", "x402", "feeless"],
        },
        "accepts": accepts,
        "extensions": {
            "bazaar": {
                "info": {
                    "input": {
                        "type": "http",
                        "method": "GET",
                        "queryParams": {"node": "rpc.nano.to"},
                    },
                    "output": {
                        "type": "json",
                        "example": {
                            "asset": "XNO",
                            "network": "nano:mainnet",
                            "confirmation_time_s": 0.4,
                            "feelss": 0,
                        },
                    },
                },
                "schema": {
                    "$schema": "https://json-schema.org/draft/2020-12/schema",
                    "type": "object",
                    "properties": {
                        "input": {
                            "type": "object",
                            "properties": {
                                "type": {"type": "string", "const": "http"},
                                "method": {"type": "string", "enum": ["GET"]},
                                "queryParams": {
                                    "type": "object",
                                    "properties": {"node": {"type": "string"}},
                                },
                            },
                            "required": ["type", "method"],
                        }
                    },
                    "required": ["input"],
                },
            },
            "xno-rail": {
                "info": {
                    "only_rail": "nano:mainnet",
                    "why": "A Nano transfer costs the sender nothing and settles in under a "
                    "second, so the price of a call is the amount transferred.",
                },
                "schema": {"type": "object", "properties": {"info": {"type": "object"}}, "required": ["info"]},
            },
        },
    }


class Handler(BaseHTTPRequestHandler):
    server_version = "xno-only-seller/1.0"
    protocol_version = "HTTP/1.1"
    pay_to = ""
    amount = DEFAULT_AMOUNT

    def log_message(self, fmt, *args):  # keep stderr quiet
        pass

    def _send(self, code: int, payload: dict, extra_headers=None):
        body = json.dumps(payload, indent=2).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        for k, v in (extra_headers or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(body)

    def _base_url(self) -> str:
        host = self.headers.get("X-Forwarded-Host") or self.headers.get("Host") or "localhost"
        proto = self.headers.get("X-Forwarded-Proto") or "http"
        return f"{proto}://{host}"

    def do_GET(self):
        path = urlparse(self.path).path

        if path in ("/", "/index"):
            self._send(
                200,
                {
                    "service": "XNO-only x402 route",
                    "paid_route": self._base_url() + PAID_PATH,
                    "accepts": ["nano:mainnet / XNO"],
                    "what_it_proves": "an x402 route can ask for Nano and nothing else",
                    "discovery": self._base_url() + "/.well-known/x402",
                    "operator": "Rai, an autonomous AI agent",
                },
            )
            return

        if path == "/.well-known/x402":
            self._send(200, declaration(self._base_url(), self.pay_to, self.amount))
            return

        if path == PAID_PATH:
            d = declaration(self._base_url(), self.pay_to, self.amount)
            hdr = base64.b64encode(json.dumps(d).encode()).decode()
            self._send(402, d, {"PAYMENT-REQUIRED": hdr})
            return

        self._send(404, {"error": "not found", "paid_route": self._base_url() + PAID_PATH})

    def do_HEAD(self):
        self.do_GET()


def main(argv=None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--port", type=int, default=8421)
    p.add_argument("--pay-to", default=os.environ.get("XNO_PAY_TO", ""))
    p.add_argument("--amount", default=DEFAULT_AMOUNT)
    a = p.parse_args(argv)
    if not a.pay_to.startswith("nano_"):
        print("refusing to start: --pay-to must be a nano_ address (never a seed or private key)")
        return 2
    Handler.pay_to = a.pay_to
    Handler.amount = a.amount
    srv = ThreadingHTTPServer(("127.0.0.1", a.port), Handler)
    print(f"listening on 127.0.0.1:{a.port}  paid route {PAID_PATH}  payTo {a.pay_to[:14]}...")
    srv.serve_forever()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
