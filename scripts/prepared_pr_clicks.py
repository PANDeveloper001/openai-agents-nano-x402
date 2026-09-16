#!/usr/bin/env python3
"""Regenerate the one-click compare-URL block: the keyless handoff for every prepared branch.

`POST /repos/<third-party>/pulls` answers 403 on the stored fine-grained token, so the last step of each
prepared PR is one signed-in click by a human who owns the account. This script produces that click as a
list of prefilled compare URLs (the target's OWN /compare/<base>...<you>:<branch>?expand=1 page), verifies
each answers 200 **signed out**, and writes a paste-free handoff document.

Deriving it here, rather than typing it, is deliberate: a typed list of branches went stale twice on
2026-09-16 and both times the stale version looked authoritative.

Usage: python3 scripts/prepared_pr_clicks.py [--json .ledger/tmp/drift_all.json] [--out .ledger/handoff.md]
Exit code 0 always (a report, and a URL that 404s is reported, not fatal).
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
import urllib.error
import urllib.request

UA = {"User-Agent": "Mozilla/5.0 (compatible; rai-agent; signed-out check)"}


def status_of(url: str) -> int:
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=45) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception:
        return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", default=".ledger/tmp/drift_all.json")
    ap.add_argument("--out", default=".ledger/handoff.md")
    a = ap.parse_args()

    rows = json.load(open(a.json))
    clean = [r for r in rows if r.get("status") == "ahead" and r.get("behind_by") == 0]

    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    out = ["# Handoff - open these prepared pull requests (one click each)", "",
           f"Generated {now} from `.ledger/tmp/drift_all.json`. Regenerate, never hand-edit:",
           "",
           "```bash",
           "python3 scripts/prepared_pr_drift_all.py --json .ledger/tmp/drift_all.json",
           "python3 scripts/prepared_pr_clicks.py",
           "```",
           "",
           "`POST /repos/<third-party>/pulls` is 403 on the stored token, so each row below is the target's own",
           "compare page with `?expand=1`: it opens the full pull-request form prefilled from the fork branch.",
           "Every URL is checked signed out; the HTTP status is the one measured at generation time.", "",
           "| # | target | branch | compare URL (signed-out status) |", "|---|---|---|---|"]
    bad = 0
    for n, r in enumerate(sorted(clean, key=lambda r: r["upstream"]), 1):
        up, br = r["upstream"], r["branch"]
        url = f"https://github.com/{up}/compare/HEAD...PANDeveloper001:{br}?expand=1"
        st = status_of(url)
        if st != 200:
            bad += 1
        out.append(f"| {n} | `{up}` | `{br}` | [{st}]({url}) |")
    out += ["",
            f"{len(clean)} clean branches, {bad} whose compare page did not answer 200 at generation time.",
            "",
            "Each row still needs the drift re-check immediately before the click "
            "(`scripts/prepared_pr_drift_all.py`); `x402-foundation/x402` moves several commits a day.",
            ""]
    open(a.out, "w").write("\n".join(out))
    print(f"{len(clean)} clean branches, {bad} non-200 compare pages -> {a.out}")
    for line in out[9:12 + len(clean)]:
        print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())