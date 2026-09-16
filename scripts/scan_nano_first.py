#!/usr/bin/env python3
"""2026-09-16 run: find live Nano-first x402 sellers and test the keyless validator.

Two questions, both keyless:
  1. CDP Bazaar: how many resources declare any nano:mainnet accept, and how many are
     NANO-FIRST (accepts[0].network == nano:mainnet)? The second is the one that matters:
     the earlier measurement proved a Nano-only accepts[] is REJECTED by the validator,
     so a Nano-first route that still validates would be a genuine gap in that finding.
  2. Agent402.Tools cross-seller index: same question against 4 aggregated facilitators.
Output: JSON on stdout / to .ledger/tmp/.
"""
import json, sys, time, urllib.request

UA = {"User-Agent": "rai-agent/1.0 (autonomous AI agent; Nano x402 measurement)"}


def get(url, tries=3):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=45) as r:
                return json.loads(r.read())
        except Exception as e:
            if i == tries - 1:
                raise
            time.sleep(2 + 2 * i)


def scan_bazaar():
    total = None
    offset = 0
    nano_resources = []
    nano_first = []
    limit_seen = None
    while True:
        d = get(f"https://api.cdp.coinbase.com/platform/v2/x402/discovery/resources?limit=1000&offset={offset}")
        p = d.get("pagination", {})
        total = p.get("total")
        limit_seen = p.get("limit")
        items = d.get("items") or d.get("resources") or []
        for it in items:
            acc = it.get("accepts") or []
            nets = [a.get("network") for a in acc]
            if any(n == "nano:mainnet" for n in nets):
                nano_resources.append({
                    "resource": it.get("resource"),
                    "accepts0": nets[0] if nets else None,
                    "n_nano": sum(1 for n in nets if n == "nano:mainnet"),
                    "payTo": [a.get("payTo") for a in acc if a.get("network") == "nano:mainnet"],
                    "amount": [a.get("amount") for a in acc if a.get("network") == "nano:mainnet"],
                })
                if nets and nets[0] == "nano:mainnet":
                    nano_first.append(it.get("resource"))
        offset += len(items)
        if not items or offset >= (total or 0):
            break
    return {"total": total, "limit": limit_seen, "nano_resources": nano_resources,
            "nano_first": nano_first}


def scan_agent402():
    d0 = get("https://agent402.tools/api/index?perPage=100&page=1")
    total = d0.get("sellerCount") or d0.get("total")
    pages = d0.get("pages") or 1
    nano = []
    for page in range(1, pages + 1):
        d = get(f"https://agent402.tools/api/index?perPage=100&page={page}")
        blob = json.dumps(d).lower()
        sellers = d.get("sellers") or d.get("items") or []
        for s in sellers:
            nets = json.dumps(s.get("networks", [])).lower()
            if "nano" in nets:
                nano.append({"name": s.get("displayName"), "origin": s.get("origin"),
                             "networks": s.get("networks"),
                             "routable": s.get("routable"),
                             "dispatch": s.get("routerDispatchByChain") or s.get("routerDispatchEligible"),
                             "payToByNetwork": s.get("payToByNetwork")})
    return {"sellerCount": total, "pages": pages, "nano_sellers": nano}


if __name__ == "__main__":
    out = {"at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    try:
        out["bazaar"] = scan_bazaar()
    except Exception as e:
        out["bazaar_error"] = repr(e)
    try:
        out["agent402"] = scan_agent402()
    except Exception as e:
        out["agent402_error"] = repr(e)
    print(json.dumps(out, indent=1)[:12000])
    with open(".ledger/tmp/nano_first_scan.json", "w") as f:
        json.dump(out, f, indent=1)
