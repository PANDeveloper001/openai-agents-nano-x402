#!/usr/bin/env python3
"""Regenerate the CURRENT HEAD SNAPSHOT section of .ledger/on-key-arrival.md from the fork-derived scan.

Why this exists (corrective action 2026-09-16 16:34 UTC): the prepared-PR snapshot in the runbook was
hand-written and went stale silently - it named an older x402 docs branch and omitted the spec branch,
so a "clean" report under-reported the two artifacts that carry this repo's adoption argument. The
scanner stops going stale; this script makes the DOC stop going stale too, by rewriting its data rows
from the scanner's own JSON instead of a human retyping branches.

Usage:  python3 scripts/pr_drift_doc.py [--json .ledger/tmp/drift_all.json] [--write] [--doc PATH]

Without --write it prints the section it would write (a diff-free preview). Exit 0 always: reporting
tool, never a gate.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys

BEGIN = "## CURRENT HEAD SNAPSHOT"
END = "### Superseded branch names (history — do not open from these)"

# The two artifacts that carry the adoption argument get their own table, plus any branch the scan
# missed entirely: an artifact that disappears from the scan must still appear in the doc as a hole,
# not silently vanish (that is exactly how the spec branch was dropped, 2026-09-16 16:34).
KEY_TARGETS = ["x402-foundation/x402"]
# (upstream, branch) that must be named in the key table; reported as MISSING when the scan lacks it.
KEY_EXPECTED = [("x402-foundation/x402", "docs/list-openai-agents-nano-v6"),
                ("x402-foundation/x402", "specs/exact-nano-mainnet")]


def rows_from(report: list[dict]) -> tuple[list[dict], list[dict]]:
    key, rest = [], []
    for r in report:
        (key if r.get("upstream") in KEY_TARGETS else rest).append(r)
    key.sort(key=lambda r: r.get("branch", ""))
    rest.sort(key=lambda r: (r.get("upstream", ""), r.get("branch", "")))
    return key, rest


def fmt(r: dict) -> str:
    st = f"{r.get('status')} ahead {r.get('ahead_by')} / behind {r.get('behind_by')}"
    return f"{r.get('upstream')} `{r.get('branch')}` {st}"


def section(report: list[dict], when: str) -> str:
    key, rest = rows_from(report)
    clean = [r for r in report if r.get("status") == "ahead" and r.get("behind_by") == 0]
    found = {(r.get("upstream"), r.get("branch")) for r in report}
    out = [BEGIN, ""]
    out.append(f"**Generated {when} from the fork-derived scan - do not hand-edit this section.**")
    out.append("")
    out.append("```bash")
    out.append("# 1. scan every fork (fails loudly if a fork's branch list looks truncated)")
    out.append("python3 scripts/prepared_pr_drift_all.py --json .ledger/tmp/drift_all.json")
    out.append("# 2. rewrite this section from that scan (never hand-edit it)")
    out.append("python3 scripts/pr_drift_doc.py --json .ledger/tmp/drift_all.json --write")
    out.append("```")
    out.append("")
    out.append(f"It asks the forks which branches exist, keeps the newest `-vN` per target, filters to branches whose")
    out.append(f"newest commit is authored by Rai, and pages the branch lists until a short page (the `x402` fork has 783).")
    out.append(f"Result on {when}: **{len(report)} prepared branches, {len(clean)} clean (ahead / behind 0)**, "
               f"{len(report) - len(clean)} being superseded history.")
    out.append("")
    out.append("### Branches on `x402-foundation/x402` (the adoption argument)")
    out.append("")
    out.append("| target | branch | head | state |")
    out.append("|---|---|---|---|")
    for r in key:
        st = f"{r.get('status')} ahead {r.get('ahead_by')} / behind {r.get('behind_by')} |"
        head = f"`{r.get('head')}`" if r.get("head") else "?"
        out.append(f"| `{r.get('upstream')}` | `{r.get('branch')}` | {head} | {st}")
    for up, br in KEY_EXPECTED:
        if (up, br) not in found:
            out.append(f"| `{up}` | `{br}` | ? | **MISSING from the scan** - check the fork before opening |")
    out.append("")
    out.append("Re-check every row against upstream `main` immediately before opening - those repos move daily.")
    out.append("")
    out.append("### The rest")
    out.append("")
    for r in rest:
        note = "" if (r.get("status") == "ahead" and r.get("behind_by") == 0) else "  ← NOT CLEAN"
        out.append(f"- {fmt(r)}{note}")
    out.append("")
    out.append("### Superseded branch names (history — do not open from these)")
    out.append("")
    return "\n".join(out)


def upstream_rows(report: list[dict], upstream: str) -> list[dict]:
    """Fresh rows for one upstream, newest-name-first, clean rows before superseded ones."""
    rows = [r for r in report if r.get("upstream") == upstream]
    rows.sort(key=lambda r: (not (r.get("status") == "ahead" and r.get("behind_by") == 0),
                             r.get("branch", "")))
    return rows


def docs_table(report: list[dict], when: str) -> str:
    """The `docs/upstream-x402-nano-registration.md` artifact table, generated from the same scan.

    That file carried a hand-typed `@ cbef150a` for the spec branch and a hand-typed state for the docs
    row - the same failure mode as .ledger/on-key-arrival.md, in a document meant for upstream reviewers.
    """
    out = ["## What is already prepared and verified", "",
           f"*Table generated {when} from the fork-derived scan (`scripts/pr_drift_doc.py --doc docs/...`) - do not hand-edit.*",
           "",
           "| artifact | branch | head | state vs upstream `main` |", "|---|---|---|---|"]
    ARTIFACT = {
        "specs/exact-nano-mainnet":
            "missing per-network scheme spec + offline checker",
        "docs/list-openai-agents-nano-v6":
            "docs row: `openai-agents-nano` in `docs/dev-tools/third-party-sdks.md`",
    }
    for r in upstream_rows(report, "x402-foundation/x402"):
        clean = r.get("status") == "ahead" and r.get("behind_by") == 0
        art = ARTIFACT.get(r.get("branch"), "_(superseded name)_")
        state = (f"ahead {r.get('ahead_by')} / behind {r.get('behind_by')} vs current `main`"
                 + (" — compare page 200 signed out" if clean else " — do not open this one"))
        out.append(f"| {art} | `{r.get('branch')}` | `{r.get('head') or '?'}` | {state} |")
    out.append("| the two-validator measurement | this repo, `docs/x402-discovery-study.md` + "
               "`scripts/two_validator_probe.py` | — | published on `main` |")
    out.append("")
    out.append("Re-check every row against upstream `main` immediately before opening "
               "(`scripts/prepared_pr_drift_all.py`); `x402-foundation/x402` moves several commits a day.")
    out.append("")
    out.append("<!-- RA_DOCS_TABLE_END -->")
    out.append("")
    return "\n".join(out)


def rewrite_docs_table(doc: str, new: str) -> str:
    marker = "<!-- RA_DOCS_TABLE_END -->"
    i = doc.find("## What is already prepared and verified")
    if i < 0:
        raise SystemExit("docs file is missing the artifact-table heading")
    if marker in doc:
        k = doc.find(marker) + len(marker)
    else:
        j = doc.find("\n## Deliberately not done", i)
        if j < 0:
            raise SystemExit("docs file has neither the end marker nor the next heading")
        k = j + 1
    # Normalise the separator so a second run is a no-op: exactly one blank line before what follows.
    while k < len(doc) and doc[k] == "\n":
        k += 1
    return doc[:i] + new.rstrip("\n") + "\n\n" + doc[k:]


def rewrite(doc: str, new: str) -> str:
    i = doc.find(BEGIN)
    j = doc.find(END)
    if i < 0 or j < 0 or j < i:
        raise SystemExit("runbook is missing the snapshot markers; refusing to guess where they go")
    k = j + len(END) + 1  # keep the marker itself, and skip the newline after it
    return doc[:i] + new + doc[k:]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", default=".ledger/tmp/drift_all.json")
    ap.add_argument("--doc", default=".ledger/on-key-arrival.md")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()

    report = json.load(open(a.json))
    if not isinstance(report, list) or not report:
        raise SystemExit("empty scan report: run prepared_pr_drift_all.py first")
    when = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    # Which section a file owns is mapped by NAME, never guessed from a glob: guessing rewrites the
    # wrong document (the failure this whole script exists to prevent, one level up).
    DOC_KINDS = {
        ".ledger/on-key-arrival.md": (section, rewrite),
        "docs/upstream-x402-nano-registration.md": (docs_table, rewrite_docs_table),
    }
    key = a.doc.replace("./", "")
    if key in DOC_KINDS:
        build, rewrite_fn = DOC_KINDS[key]
    elif "--new-doc" in sys.argv:
        build, rewrite_fn = docs_table, rewrite_docs_table
    else:
        raise SystemExit(f"{a.doc}: unknown document; known: {', '.join(DOC_KINDS)}")
    new = build(report, when)
    doc = open(a.doc).read()
    out = rewrite_fn(doc, new)
    if a.write:
        open(a.doc, "w").write(out)
        print(f"rewrote {a.doc}: {len(report)} rows, section {len(new)} chars")
    else:
        print(new)
    return 0


if __name__ == "__main__":
    sys.exit(main())
