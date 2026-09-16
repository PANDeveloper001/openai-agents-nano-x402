#!/usr/bin/env python3
"""Isolate the CDP validator's accepts[0].amount rule for a Nano-priced route.

The validator rejected a 28-digit Nano amount with "is not a base-10 integer".
That wording is ambiguous: is the rule a magnitude limit (int64) or a format limit?
This runs the same route at three amounts, changing nothing else, and prints the
verdict of the accepts[0].amount check for each.

Usage: python3 amount_boundary.py <public_base_url>
"""
import json
import subprocess
import sys
import time
import urllib.request

VALIDATE = "https://api.cdp.coinbase.com/platform/v2/x402/validate"
PAY_TO = "nano_1yo6c1t64ahfjdw1dxizmbbnpdmbrckwhw9phbg5pdkeubrizga4qhnjmnx7"
CASES = [
    ("9223372036854775807", "int64 max"),
    ("9223372036854775808", "int64 max + 1"),
    ("1", "1 raw (1e-30 XNO)"),
]


def validate(url):
    body = json.dumps({"resource": url, "method": "GET"}).encode()
    req = urllib.request.Request(VALIDATE, data=body, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def main():
    base = sys.argv[1].rstrip("/")
    for amount, label in CASES:
        p = subprocess.Popen(
            [sys.executable, "server.py", "--port", "8421", "--pay-to", PAY_TO, "--amount", amount],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        time.sleep(1.3)
        try:
            d = validate(f"{base}/x402/nano-quote")
            amt = [c for c in d.get("preflight", []) if c["check"] == "accepts[0].amount"]
            v = amt[0] if amt else {}
            net = [c for c in d.get("preflight", []) if c["check"] == "accepts[0].network"]
            print(
                f"amount={amount:<20} ({label:<20}) digits={len(amount):<3} "
                f"amount_passed={v.get('passed')}  network_passed={net[0]['passed'] if net else None}"
            )
            if v and v.get("detail"):
                print(f"    detail: {v['detail']}")
        finally:
            p.terminate()
            p.wait(timeout=10)
            time.sleep(0.5)


if __name__ == "__main__":
    main()
