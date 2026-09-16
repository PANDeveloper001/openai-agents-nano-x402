#!/usr/bin/env python3
"""Dedupe the prepared-PR runbook down to the NEWEST branch per upstream target.

Why this exists
---------------
The runbook (`.ledger/on-key-arrival.md`) accumulates a new line every time an upstream
drifts and a branch is rebuilt (`add-...` -> `-v2` -> `-v3` ...). The authoritative entry is
the LAST one in file order, but the file also carries older entries that are explicitly
marked "USE THIS" - so a line-order-agnostic or "grab the USE THIS" reader picks a stale
branch, which is exactly the mistake the runbook itself warns against.

This script prints the newest entry per target, and flags a target whose newest entry is NOT
the one marked "USE THIS" (a stale marker), because that is the case that bites.

Usage: python3 scripts/prepared_pr_latest.py [path-to-runbook]
"""
import re
import sys
import pathlib

DEFAULT = "/root/work/openai-agents-nano-x402/.ledger/on-key-arrival.md"

# Shapes seen in the file (the target may be bolded, quoted, or spaced out with colons):
#   - x402-foundation/x402 (v5, USE THIS): branch `docs/list-openai-agents-nano-v5` @ da1bcd2 ...
#   - Corican/nanodir:        fork PAN branch `add-openai-agents-nano-clean` @ def0d34
#   - mbeato/awesome-mpp (v1, prepared): branch add-nano-x402-agent-framework - ahead 1 ...
#   - **Haustorium12/gold-402** (14th target, prepared ...): fork `PANDeveloper001/gold-402`,
TARGET = re.compile(r"([A-Za-z0-9._-]+/[A-Za-z0-9._-]+)")
BRANCH = re.compile(r"branch\s+`?([A-Za-z0-9._/-]+)`?")
SHA = re.compile(r"@\s*([0-9a-f]{7,40})")
MARKER = re.compile(r"\((?:[^)]*?\bUSE THIS\b[^)]*?)\)", re.I)


def parse(path):
    latest = {}
    for line in pathlib.Path(path).read_text().splitlines():
        s = line.strip()
        if not s.startswith(("-", "*")):
            continue
        m = TARGET.search(s)
        if not m:
            continue
        target = m.group(1)
        if target.startswith(("http", "refs/")):
            continue
        b = BRANCH.search(s)
        sha = SHA.search(s)
        # the last occurrence wins: the runbook appends newer entries below older ones
        latest[target] = {
            "branch": b.group(1) if b else "?",
            "sha": sha.group(1) if sha else "",
            "use_this": bool(MARKER.search(s)),
            "line": s[:150],
        }
    return latest


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT
    latest = parse(path)
    stale = [t for t, r in latest.items() if not r["use_this"] and
             any(r2["use_this"] for t2, r2 in latest.items() if t2 == t)]
    print(f"{len(latest)} prepared targets in {path}\n")
    for target, r in sorted(latest.items()):
        flag = "  USE THIS" if r["use_this"] else ""
        print(f"{target:52s} {r['branch']:44s} {r['sha']:9s}{flag}")
    print()
    print("targets whose NEWEST entry is not the one marked USE THIS:", stale or "none")


if __name__ == "__main__":
    main()
