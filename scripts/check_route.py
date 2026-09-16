#!/usr/bin/env python3
"""Check an x402 route keylessly, with a Nano (XNO) focus.

Why this exists: an agent that wants to pay a route in Nano has two questions the
owner's docs answer only in prose -- "does this route really answer 402 with a
nano:mainnet accepts entry?" and "would Coinbase's own indexer accept it?".
Both are answerable without an API key. This script answers them in one command.

It never pays, never signs and never needs a key.

Usage:
  python3 scripts/check_route.py https://host/path [--method GET] [--json]

Exit code 0 when both checks pass, 1 otherwise. Output is JSON with --json.
"""
from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request

VALIDATE_URL = "https://api.cdp.coinbase.com/platform/v2/x402/validate"


def fetch_402(url: str, method: str, timeout: int = 30):
    """Return (status, parsed_body_or_None, headers). Follows no redirects' bodies."""
    req = urllib.request.Request(url, method=method, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, _try_json(r.read()), dict(r.headers)
    except urllib.error.HTTPError as e:
        return e.code, _try_json(e.read()), dict(e.headers or {})


def _try_json(raw: bytes):
    try:
        return json.loads(raw.decode("utf-8", "replace"))
    except Exception:
        return None


def nano_accepts(accepts):
    out = []
    for a in accepts or []:
        net = str(a.get("network", "")).lower()
        asset = str(a.get("asset", ""))
        if "nano" in net or asset.upper() == "XNO":
            out.append(
                {
                    "network": a.get("network"),
                    "asset": asset,
                    "scheme": a.get("scheme"),
                    "amount": a.get("amount"),
                    "payTo": a.get("payTo"),
                    "maxTimeoutSeconds": a.get("maxTimeoutSeconds"),
                }
            )
    return out


def validate(url: str, method: str, timeout: int = 60):
    body = json.dumps({"resource": url, "method": method}).encode()
    req = urllib.request.Request(
        VALIDATE_URL, data=body, headers={"Content-Type": "application/json"}, method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            d = _try_json(r.read()) or {}
    except Exception as e:  # network or 4xx/5xx; report, never raise
        return {"error": f"{type(e).__name__}: {e}"}
    failed = [
        c.get("check")
        for c in d.get("preflight", [])
        if c.get("severity") == "required" and not c.get("passed")
    ]
    return {
        "valid": d.get("valid"),
        "outcome": (d.get("simulation") or {}).get("outcome"),
        "failed_required": failed,
        "has_bazaar_extension": any(
            c.get("check") == "has_bazaar_extension" and c.get("passed")
            for c in d.get("preflight", [])
        ),
    }


def check(url: str, method: str = "GET") -> dict:
    status, body, headers = fetch_402(url, method)
    accepts = (body or {}).get("accepts") if isinstance(body, dict) else None
    if accepts is None and isinstance(body, dict):
        accepts = (body.get("paymentRequirements") or {}).get("accepts")
    nano = nano_accepts(accepts)
    return {
        "resource": url,
        "method": method,
        "status": status,
        "returns_402": status == 402,
        "payment_required_header": "PAYMENT-REQUIRED" in {k.upper() for k in headers},
        "accepts_count": len(accepts or []),
        "nano_accepts": nano,
        "payable_in_nano": bool(nano),
        "cdp_facilitator_validation": validate(url, method),
        "note": "No key, no payment, no signature. Nano counts as payable only if a "
        "nano:mainnet / asset XNO entry is present in accepts[].",
    }


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Keyless x402 route check with a Nano focus")
    p.add_argument("url")
    p.add_argument("--method", default="GET")
    p.add_argument("--json", action="store_true")
    args = p.parse_args(argv)

    r = check(args.url, args.method)
    if args.json:
        print(json.dumps(r, indent=2))
    else:
        print(f"{r['resource']}  {r['method']}")
        print(f"  HTTP {r['status']} (402 expected)  PAYMENT-REQUIRED header: {r['payment_required_header']}")
        print(f"  accepts[] entries: {r['accepts_count']}  payable in Nano: {r['payable_in_nano']}")
        for a in r["nano_accepts"]:
            print(f"    nano: {a['amount']} raw XNO -> {a['payTo']} (timeout {a['maxTimeoutSeconds']}s, work {a['scheme']})")
        v = r["cdp_facilitator_validation"]
        if "error" in v:
            print(f"  CDP validate: unreachable ({v['error']})")
        else:
            print(
                f"  CDP validate: valid={v['valid']} outcome={v['outcome']} "
                f"bazaar={v['has_bazaar_extension']} failed_required={v['failed_required']}"
            )
    ok = r["returns_402"] and r["payable_in_nano"] and r["cdp_facilitator_validation"].get("valid") is True
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())