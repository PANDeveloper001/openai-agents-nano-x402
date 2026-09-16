# Block 11 — oracle-verified only (judge stage unreachable, honestly recorded)

Law L24 (block 11): "The probe reports a route as caller-dependent only when User-Agents disagree on the status."
Oracle: `python3 tests/tunnel_ua_probe_offline.py` expecting `7/7 checks passed`.

**What actually ran, with real output:**

```
$ python3 tests/tunnel_ua_probe_offline.py
  PASS  probe exits 0 on a caller-dependent route -- rc=0
  PASS  probe reports caller_dependent true
  PASS  browser UA sees 200 -- {'curl/8.5.0': 402, 'python-urllib/3.12': 402, 'Mozilla/5.0': 200, 'x402-Doctor/1.0': 402, 'agent-payer/1.0': 402}
  PASS  library UAs see 402
  PASS  M1 hard-wired verdict is caught -- 0/1 checks passed
  PASS  M2 missing browser UA is caught -- 1/4 checks passed
  PASS  M3 None-status counts as caller-dependence elsewhere -- 2/4 checks passed

7/7 checks passed      (exit 0)

$ uv run python -m pytest -q
9 passed in 4.96s

$ python3 scripts/tunnel_ua_probe.py https://dzxoe-2602-fa59-2-c5c7--1.free.pinggy.net
    402  curl/8.5.0
    402  python-urllib/3.12
    200  Mozilla/5.0
    402  x402-Doctor/1.0
    402  agent-payer/1.0
caller-dependent (a UA decides the status): True      (exit 0)
```

**What did NOT run:** the ledger judge. `ledger verify --block 11` and `ledger unwind --block 11` both abort with
`RuntimeError: LLM call to https://openrouter.ai/api/v1 failed: HTTP Error 402: Payment Required` before any verdict is
written. The only configured alternative judge provider is the routed fallback, which my own recorded rule forbids
feeding into a project ledger. Consequence, stated plainly: block 11 is **oracle-verified only, not judge-verified**,
appears in `blocks not passed`, and nothing here may be reported as "verified".
