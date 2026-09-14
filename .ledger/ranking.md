# Ranking: adapter Tool shape for OpenAI Agents SDK + Nano

Ideas from ../tmp/ideas.json (8, engine + deepseek-v4.1-flash). All admissible except #5.

## Excluded challenges (before ranking)
- prompt-injected endpoint / malicious pay_to (server-controlled x402 quote, Nano sends irreversible)
- agent cannot exfiltrate the wallet path/seed (key theft)
- overspend: price must never exceed the cap, and no exception the model can retry around
- stateful-wallet concurrency: one Wallet, parallel calls → nonce collisions / failed settlement
- accidental spending during a quote (must be spendless)

## Ranked
| Rank | Idea (n) | Why | Verdict |
|---|---|---|---|
| 1 | Single `nano_x402_fetch(url, max_xno, dry_run)` via a tool factory that binds `Wallet(path)` + `RPC` once; cap enforced in code before signing; spendless quote when `dry_run=True`; agent-readable text receipt (status, amount_xno, pay_to, block, settled, ledger, note) (0,2,5:3,7) | Attacks every challenge: wallet never a model arg, cap deterministic, dry_run never signs, receipt text the model can reason over. Framework-native single tool lowers tool-choice errors. | **Adopt (composite)** |
| 2 | Two-phase quote-redeem with single-use HMAC token (7,5:2) | Strongest against prompt injection + spoof, but adds state/TTL the agent must hold across calls; more surface for a thin adapter. Keep HMAC token as an internal detail if cheap. | Adopt as block-2 refinement, not block 1 |
| 3 | Strict JSON receipts + 15s timeout, structured for parsing (1,6,4) | JSON clashes with "model reads text"; a hard timeout is good and folded into the adapter (fail fast, never hang the loop). | Fold the timeout in; return text |
| 4 | asyncio.Lock serialization of the shared wallet (6) | Real, necessary: Nano blocks are stateful/non-replayable, parallel calls race. | **Adopt — in block 1** |
| 5 | cap via `max_raw=0` for simulation (4) | Hidden flag, obscure. `dry_run` is clearer. | Reject |
| 6 | Separate balance / pay / quote tools (AsterPay mirror) (0 baseline) | More tool surface, more model error. | Reject — one tool |

## Chosen invention (block 1)
`NanoX402Tool` delivered by `make_nano_x402_tool(wallet_path=None, rpc=None, default_max_xno=...)`:
- one OpenAI Agents SDK tool `nano_x402_fetch(url, method="GET", json_body="", max_xno=None, dry_run=False)`;
- wallet + RPC bound at construction (env `X402_WALLET_PATH` or param), never a tool arg;
- `dry_run=True` → spendless quote text (price, pay_to, cap), via `request_with_payment(dry_run=True)`;
- `dry_run=False` → cap checked inside before signing (price ≤ min(max_xno, default cap)), then `request_with_payment(dry_run=False)`; refusal string (not exception) when over cap;
- an `asyncio.Lock` serializes payments behind one wallet so stateful Nano blocks never race;
- returns agent-readable text: status, body, amount_xno, pay_to, block, settled, ledger, note.
- Reuses feeless402's `request_with_payment`, `Wallet`, `RPC` verbatim — zero Nano payment logic rebuilt.
Prompt injection is contained: wallet path/cap live in deterministic code; url is LLM-chosen but pay_to/price come from the server's signed 402 quote and are capped.