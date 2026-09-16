#!/usr/bin/env python3
"""Prove the published paid-endpoint offer is real, not aspirational.

The offer at docs/offer/paid-endpoint.json claims an x402 route priced in Nano with a
specific payTo and a specific CDP-validator result. This script fetches the live 402
body and fails if any of those claims is untrue.

Offline test for the parsing logic lives in tests/test_offer.py; this is the live check.

Usage: python3 scripts/verify_offer.py [--offer docs/offer/paid-endpoint.json]
Exit 0 = every claim in the file matches the live route.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_route import check  # noqa: E402


def main(argv=None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--offer", default="docs/offer/paid-endpoint.json")
    args = p.parse_args(argv)

    offer = json.loads(Path(args.offer).read_text())
    target = offer["resource"]
    url, method = target["url"], target.get("method", "GET")
    declared = offer["accepts"][0]

    live = check(url, method)
    problems = []

    if not live["returns_402"]:
        problems.append(f"route does not return 402 (HTTP {live['status']})")
    match = None
    for a in live["nano_accepts"]:
        if a["asset"] == declared["asset"] and a["scheme"] == declared["scheme"]:
            match = a
    if match is None:
        problems.append("no live nano:mainnet/XNO accept matches the declared asset+scheme")
    else:
        for field in ("network", "amount", "payTo", "maxTimeoutSeconds"):
            if str(match[field]) != str(declared[field]):
                problems.append(f"{field} differs: live {match[field]!r} != declared {declared[field]!r}")

    v = live["cdp_facilitator_validation"]
    if v.get("valid") is not True or v.get("outcome") != "accepted":
        problems.append(f"CDP validator does not accept the route: {v}")

    # The offer states its own indexing status honestly; verify the claim is present
    # and that the payTo it publishes is a well-formed Nano account.
    payto = declared["payTo"]
    if not (payto.startswith("nano_") and len(payto) in (64, 65)):
        problems.append(f"published payTo is not a well-formed nano_ account: {payto!r}")
    if offer.get("indexing", {}).get("status") not in {"not indexed yet", "indexed"}:
        problems.append("indexing.status missing or not honest")

    print(json.dumps({"offer": args.offer, "resource": url, "problems": problems}, indent=2))
    if problems:
        print("OFFER VERIFICATION FAILED", file=sys.stderr)
        return 1
    print("OFFER VERIFIED: every declared field matches the live route and the CDP validator accepts it.")
    return 0


if __name__ == "__main__":
    sys.exit(main())