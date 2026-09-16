#!/usr/bin/env python3
"""Run a live Nano-only x402 route through TWO independent validators.

Usage: python3 doctor_rail_probe.py <https-base-url> [--tunnel-cmd CMD]

Prints a JSON report with raw outputs from:
  1. the CDP Bazaar validator  (POST api.cdp.coinbase.com/platform/v2/x402/validate)
  2. the third-party x402 Doctor (GET api.stelardigital.com/doctor?url=...)
The point is the contrast: the third-party checker passes every protocol rule and names
`nano` as a CAIP-2 namespace, while the CDP facilitator rejects the four rail-value checks.
"""
import argparse, json, subprocess, sys, time, urllib.parse, urllib.request

CDP = "https://api.cdp.coinbase.com/platform/v2/x402/validate"
DOCTOR = "https://api.stelardigital.com/doctor?url="


def http_json(url, data=None, timeout=90):
    req = urllib.request.Request(url, data=data, headers={"User-Agent": "rai-agent", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, json.loads(r.read())
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read())


def cdp(route):
    st, d = http_json(CDP, json.dumps({"resource": route, "method": "GET"}).encode())
    failed = [{"check": c.get("name"), "detail": c.get("detail") or c.get("reason") or c.get("error")}
              for c in d.get("preflight", []) if not c.get("passed")]
    return {"http": st, "valid": d.get("valid"), "simulation": d.get("simulation"),
            "checks_total": len(d.get("preflight", [])), "failed": failed}


def doctor(route):
    st, d = http_json(DOCTOR + urllib.parse.quote(route, safe=""))
    return {"http": st, "score": d.get("score"), "grade": d.get("grade"), "recommendation": d.get("recommendation"),
            "checks": [{"id": c["id"], "status": c["status"], "message": c["message"]} for c in d.get("checks", [])]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("base", help="public https base url of the seller")
    ap.add_argument("--path", default="/x402/nano-quote")
    a = ap.parse_args()
    route = a.base.rstrip("/") + a.path
    out = {"route": route, "ts": int(time.time()), "cdp": cdp(route), "doctor": doctor(route)}
    print(json.dumps(out, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
