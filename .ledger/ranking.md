# Ranking: adapter Tool shape for OpenAI Agents SDK + Nano

Ideas from ../tmp/ideas.json (8, engine + deepseek-v4.1-flash). All admissible except #5.

## Excluded challenges (before ranking)
- prompt-injected endpoint / malicious pay_to (server-controlled x402 quote, Nano sends irreversible)
- agent cannot exfiltrate the wallet path/seed (key theft)
- overspend: price must never exceed the cap, and no exception the model can retry around
- stateful-wallet concurrency: one Wallet, parallel calls -> nonce collisions / failed settlement
- accidental spending during a quote (must be spendless)

## Ranked
| Rank | Idea (n) | Why | Verdict |
|---|---|---|---|
| 1 | Single nano_x402_fetch(url, max_xno, dry_run) via a tool factory that binds Wallet(path) + RPC once; cap enforced in code before signing; spendless quote when dry_run=True; agent-readable text receipt (status, amount_xno, pay_to, block, settled, ledger, note) (0,2,5:3,7) | Attacks every challenge: wallet never a model arg, cap deterministic, dry_run never signs, receipt text the model can reason over. Framework-native single tool lowers tool-choice errors. | **Adopt (composite)** |
| 2 | Two-phase quote-redeem with single-use HMAC token (7,5:2) | Strongest against prompt injection + spoof, but adds state/TTL the agent must hold across calls; more surface for a thin adapter. Keep HMAC token as an internal detail if cheap. | Adopt as block-2 refinement, not block 1 |
| 3 | Strict JSON receipts + 15s timeout, structured for parsing (1,6,4) | JSON clashes with 'model reads text'; a hard timeout is good and folded into the adapter (fail fast, never hang the loop). | Fold the timeout in; return text |
| 4 | asyncio.Lock serialization of the shared wallet (6) | Real, necessary: Nano blocks are stateful/non-replayable, parallel calls race. | **Adopt - in block 1** |
| 5 | cap via max_raw=0 for simulation (4) | Hidden flag, obscure. dry_run is clearer. | Reject |
| 6 | Separate balance / pay / quote tools (AsterPay mirror) (0 baseline) | More tool surface, more model error. | Reject - one tool |

## Chosen invention (block 1)
NanoX402Tool delivered by make_nano_x402_tool(wallet_path=None, rpc=None, default_max_xno=...):
- one OpenAI Agents SDK tool nano_x402_fetch(url, method='GET', json_body='', max_xno=None, dry_run=False);
- wallet + RPC bound at construction (env X402_WALLET_PATH or param), never a tool arg;
- dry_run=True -> spendless quote text (price, pay_to, cap), via request_with_payment(dry_run=True);
- dry_run=False -> cap checked inside before signing (price <= min(max_xno, default cap)), then request_with_payment(dry_run=False); refusal string (not exception) when over cap;
- an asyncio.Lock serializes payments behind one wallet so stateful Nano blocks never race;
- returns agent-readable text: status, body, amount_xno, pay_to, block, settled, ledger, note.
- Reuses feeless402's request_with_payment, Wallet, RPC verbatim - zero Nano payment logic rebuilt.
Prompt injection is contained: wallet path/cap live in deterministic code; url is LLM-chosen but pay_to/price come from the server's signed 402 quote and are capped.

---

# Ranking: prepared-PR drift checker (block 10) and tunnel UA probe (block 11)

Ideas from ../tmp/ideas-block10.json (4 each, engine + model). All admissible.

## Excluded challenges (before ranking)

- **Block 10**: API rate limiting on compare calls; fork branch discovery on paginated repos; silent branches not matching the naming convention (specs/exact-nano-mainnet discovered late); token scope limits (only read-access compare endpoint, no write).
- **Block 11**: Tunnel provider-dependent behavior (Pinggy vs localhost.run vs serveo each rewrite differently); the tunnel gateway may change its routing at any time; the diagnostic must catch HTTPError (non-2xx, non-402) gracefully without crashing.

## Block 10 ranked

| Rank | Idea (n) | Why | Verdict |
|------|----------|-----|---------|
| 1 | **API-driven scan with derived fork list + handoff doc** (1,3,4) | Discovers branches from the actual repos, paginates, produces both JSON for CI and markdown for human clicks. Catches the specs/exact-nano-mainnet case that a hand-written list missed. The ?expand=1 compare URLs are the only way to open a PR from a fork when write-scoped tokens are 403. | **Adopt (composite)** |
| 2 | Local git merge-base check (0) | Works without an API key but needs a local clone of every upstream. Scales poorly with 15+ targets and each drift check pulls from every upstream. | Reject - too slow for 16 targets |
| 3 | Manual hand-written list (baseline) | Proven to go stale silently: the scripts/run had 14 branches when 16 existed, because specs/exact-nano-mainnet was on page 701. | Reject - must be derived |
| 4 | Single report | One format cannot serve both CI automation and human-PR-opening. | Reject - two formats needed |

## Block 10 chosen invention

prepared_pr_drift_all.py + prepared_pr_clicks.py:

1. drift_all.py lists every PANDeveloper001 fork branch matching add-* or docs/* or specs/*, paginates all pages, runs the GitHub compare API for each, writes JSON with every branch's status, ahead count, behind count, and compare URL.
2. clicks.py reads that JSON, filters to clean branches (ahead >= 1, behind = 0), generates clickable compare URLs with ?expand=1, checks each one signed-out for HTTP 200, and writes a markdown handoff document.
3. A dedicated doc offline test (prepared_pr_doc_offline.py) verifies the drift JSON format, the handoff table structure, and that every branch named in the handoff is actually clean.

## Block 11 ranked

| Rank | Idea (n) | Why | Verdict |
|------|----------|-----|---------|
| 1 | **Offline-harness probe with mutation tests** (composite of 1,2,3) | Core verdict logic is testable without a live tunnel. 7 tests including 2 with intentionally broken verdict functions verify the probe cannot lie. The live probe is a separate thin wrapper. | **Adopt (composite)** |
| 2 | Live-only tunnel probe (0) | Tests only on live pinggy tunnels. If the tunnel is down or changes its behavior, the test is inconclusive and the code change is unverified. | Reject - no offline evidence |
| 3 | Single happy-path offline test (baseline) | Catches crashes but not logic errors. A verdict that always returns 'stable' passes. | Reject - mutation needed |
| 4 | Raw diagnostic without verdict | Shows raw status codes but does not reduce to a boolean verdict. A human would need to interpret the output. | Reject - must produce verdict |

## Block 11 chosen invention

scripts/tunnel_ua_probe.py + tests/tunnel_ua_probe_offline.py:

1. tunnel_ua_probe.py: takes a URL, fetches it with MOZILLA_UA and PYTHON_REQUESTS_UA, compares status codes, prints verdict.
2. tunnel_ua_probe_offline.py: 7 test cases testing the verdict function - matching 200s (stable), matching 402s (stable), browser 200 vs lib 402 (caller-dependent), browser 402 vs lib 200 (caller-dependent), browser 403 vs lib 200 (caller-dependent), browser 200 vs lib 403 (caller-dependent), HTTPError variants. Each test runs a mock fetch function. Also tests with intentionally broken verdict implementations to verify mutation strength: a verdict that always returns 'stable' fails at least one test case, a verdict that always returns 'caller-dependent' fails at least one test case.