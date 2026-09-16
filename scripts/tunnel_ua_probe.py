#!/usr/bin/env python3
"""Ask whether a public tunnel rewrites requests: UA fingerprints of the caller.

Why this exists (measured 2026-09-16): a Nano-only x402 route served behind an
anonymous public tunnel answers 402 to a plain `curl` and **HTTP 200** to a
browser-looking User-Agent, at the same second, with no rewrite in between. That
makes every third-party checker whose own client sends a browser UA report
"no paywall" for a route that is really paywalled -- the tunnel, not the route,
decides who sees the 402.

The script is generic on purpose: it takes a base URL and a paid path and prints
one row per User-Agent with the observed status, so the next agent that hits a
"my route is fine but the checker disagrees" moment can tell a caller-dependent
tunnel apart from a broken route in one command.

It never pays, never signs and never needs a key.

Usage:
  python3 scripts/tunnel_ua_probe.py <https-base-url> [--path /x402/nano-quote] [--json]

Exit code 0 when at least one UA gets a non-200 and at least one UA gets a 200
(that is the caller-dependent case); 1 when every UA agrees (no tunnel rewrite).
"""
from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request

# A browser-like agent (what an index crawler or a checker's HTTP client may send)
# versus plain library agents (what a validator or a paying agent sends).
UAS = [
    "curl/8.5.0",
    "python-urllib/3.12",
    "Mozilla/5.0",
    "x402-Doctor/1.0",
    "agent-payer/1.0",
]


def probe(url: str, ua: str, timeout: int = 30):
    req = urllib.request.Request(url, headers={"User-Agent": ua, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, len(r.read()), str(r.headers.get("Server", ""))
    except urllib.error.HTTPError as e:
        return e.code, len(e.read()), str(e.headers.get("Server", "") if e.headers else "")
    except Exception as exc:  # unreachable, DNS, TLS -- reported, never guessed
        return None, 0, f"error: {type(exc).__name__}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("base", help="public https base url of the seller")
    ap.add_argument("--path", default="/x402/nano-quote")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    url = a.base.rstrip("/") + a.path
    rows = [{"ua": ua, "status": probe(url, ua)[0], "bytes": probe(url, ua)[1]} for ua in UAS]
    statuses = [r["status"] for r in rows]
    caller_dependent = any(s == 200 for s in statuses) and any(
        s is not None and s != 200 for s in statuses
    )
    out = {"url": url, "caller_dependent": caller_dependent, "rows": rows}
    if a.json:
        print(json.dumps(out, indent=1))
    else:
        print(f"url: {url}")
        for r in rows:
            print(f"  {r['status']!s:>5}  {r['ua']}")
        print(f"caller-dependent (a UA decides the status): {caller_dependent}")
        print("note: a 200 here is the tunnel's interstitial/echo, not the route's own answer.")
    return 0 if caller_dependent else 1


if __name__ == "__main__":
    sys.exit(main())
