#!/usr/bin/env python3
"""Measure how the Agent402 index treats the Nano (XNO) sellers it indexes.

Why: a report to keep "delivery is not action" honest. The index maintains the same seller records we
read, so a measurement that cross-cuts the index itself reaches a maintainer who cannot see his own
cross-industry blind spot. The specific question a Nano payer needs answered: is a Nano-first seller
in the index *dispatchable*, or only *routable*? The two claims differ (routable = the router can
reach it; routerDispatchByChain = the router will settle on that chain).

Read-only, keyless, paginates the API's own `pages`, writes a JSON snapshot + a human summary.

Usage: python3 scripts/measure_agent402_nano.py [--json OUT] [--per-page 100]
"""
from __future__ import annotations

import argparse
import json
import sys
import urllib.request

API = "https://agent402.tools/api/index"


def fetch(page: int, per_page: int) -> dict:
    url = f"{API}?perPage={per_page}&page={page}"
    req = urllib.request.Request(url, headers={"User-Agent": "rai-agent/1.0 (+nano adoption)"})
    with urllib.request.urlopen(req, timeout=45) as r:
        return json.loads(r.read())


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", default=".ledger/tmp/agent402_nano_measure.json")
    ap.add_argument("--per-page", type=int, default=100)
    a = ap.parse_args()

    first = fetch(1, a.per_page)
    pages, per_page = first["pages"], first.get("perPage", a.per_page)
    sellers = list(first["sellers"])
    for p in range(2, pages + 1):
        sellers += fetch(p, per_page)["sellers"]

    total = len(sellers)
    with_nano = [s for s in sellers if "nano:mainnet" in (s.get("networks") or [])]
    # a seller whose *first/primary* network is Nano: the ordering is the seller's own declaration
    nano_first = [s for s in with_nano if (s.get("networks") or [None])[0] == "nano:mainnet"]
    dispatch = []
    for s in with_nano:
        by_chain = s.get("routerDispatchByChain") or {}
        dispatch.append({
            "origin": s.get("origin"),
            "name": s.get("displayName") or s.get("origin"),
            "networks": s.get("networks"),
            "routable": s.get("routable"),
            "routerDispatchEligible": s.get("routerDispatchEligible"),
            "routerDispatchReason": s.get("routerDispatchReason"),
            "routerDispatchByChain": by_chain,
        })

    out = {"sellers_total": total, "pages": pages, "nano_sellers": len(with_nano),
           "nano_first_sellers": len(nano_first), "detail": dispatch}
    json.dump(out, open(a.json, "w"), indent=1)

    print(f"Agent402 index: {total} sellers over {pages} pages (API perPage honoured: {per_page})")
    print(f"  sellers declaring nano:mainnet : {len(with_nano)}")
    print(f"  of those, Nano as networks[0]  : {len(nano_first)}")
    for d in dispatch:
        print(f"\n  {d['name']}  {d['origin']}")
        print(f"    networks            : {d['networks']}")
        print(f"    routable            : {d['routable']}")
        print(f"    routerDispatchEligible: {d['routerDispatchEligible']}  reason: {d['routerDispatchReason']}")
        print(f"    routerDispatchByChain : {json.dumps(d['routerDispatchByChain'])}")
    print(f"\nwritten: {a.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
