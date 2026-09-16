# x402 seller discovery (CDP Bazaar) — study + what it means for Rai

Owner request 2026-09-16: read https://docs.cdp.coinbase.com/x402/seller/get-discovered and decide
what it means for Nano adoption. Method: read the doc, then **measure the live index** rather than
reason about it, then test the published validator against Nano endpoints.

## What the doc says (read 2026-09-16, source: the page itself)

- Discovery is per **paid route**: a route must answer `402` with an `accepts[]` list, carry an
  `extensions.bazaar` declaration, and be indexed after **a successful settled payment through the
  CDP Facilitator**. There is no registration form and no separate API call.
- Indexed endpoints reach agents through CDP APIs, the **Bazaar MCP server**, Amazon Bedrock
  AgentCore, and people browsing agentic.market. The Bazaar lists 23,000+ resources (doc claim).
- Metadata rules: description ≤ 500 chars (longer descriptions make the facilitator *reject* verify
  and settle), complete input/output schemas + examples, per-call pricing, documented errors.
- Ranking uses real economic usage over a rolling 30-day window; **resources with no settlement for
  30 days are removed** from the catalog and search.
- Curation (featured tier) requires live **mainnet** payments, ≥99% measured availability, passing
  health probes and validation; listing stays editorial.
- `POST https://api.cdp.coinbase.com/platform/v2/x402/validate` with `{resource, method}` needs **no
  API key** and returns `valid` + `preflight[]` + `simulation.outcome`.
- The x402.org facilitator keeps its **own separate** catalog — not the CDP Bazaar.

## What I measured (keyless, reproducible)

Index reader: `GET https://api.cdp.coinbase.com/platform/v2/x402/discovery/resources?limit=1000&offset=N`
(paginate; `pagination.total` = 15779). Full scan script output saved in the ledger tmp dir.

| measurement | value |
|---|---|
| resources in the public Bazaar index | 15,779 |
| `accepts[]` entries total | 44,240 |
| accepts with `network: "nano:mainnet"`, `asset: "XNO"` | **55 (0.124% of accepts)** |
| distinct hosts offering Nano | **1** (`pyfile-agent.taile3ff35.ts.net`) |
| resources that accept XNO at all | 55 of 15,779 (**0.35%**) |
| top networks by accepts | Base 17,412 · Solana 5,512 · Polygon 3,231 · Arbitrum 3,034 · XRPL 2,523 |
| top asset | USDC on Base (`0x8335…2913`), 17,428 |

**The decisive fact: the CDP Bazaar already indexes Nano.** `nano:mainnet` + `asset: "XNO"` +
`scheme: "exact"` entries are live in the same index as the USDC ones, and that seller's endpoints
really do answer 402 (`pyfile-agent.taile3ff35.ts.net/data/ip` → HTTP 402 with a `payment-required`
header). Nano is absent from x402 discovery **by omission, not by exclusion** — no protocol change is
needed for a Nano endpoint to be discoverable.

Validator tests (`POST /platform/v2/x402/validate`, no API key):

| resource | result |
|---|---|
| `https://example.com/` | reachable 200 → fails only `returns_402` |
| `https://pyfile-agent.taile3ff35.ts.net/` (live Nano seller) | `endpoint_reachable: false`, all later checks skipped |
| `https://x402nano.com/weather` (Nano-scheme x402) | `endpoint_reachable: false` |
| `https://nanoroute.com/` | reachable 200 → fails only `returns_402` |

So the preflight reachability check runs from **the validator's own egress**, and at least one living
Nano host is unreachable from it while being reachable from other networks. Consequence for the goal:
XNO sellers can be silently downgraded by health probes even when their service is up.

## Decision (honest, no new project)

- **We cannot list the payer SDK in the Bazaar, and we should not try.** The Bazaar indexes *paid
  resources*, not client libraries; our adapter sells nothing. This is recorded as not-a-fit once.
- **A Nano XNO seller endpoint would be Bazaar-eligible today** — the network string is accepted by
  the index. But that requires deploying a public paid service and completing settled calls through
  the CDP Facilitator, which is building a new thing, and this run is distribution-only. It is the
  strongest *future* distribution lever found so far and is recorded in the backlog, not built here.
- **The actionable step that fits the current run** is precedent evidence: the strongest argument for
  listing a Nano payer in x402 SDK lists is not opinion, it is the Bazaar's own index. That evidence
  is now in the prepared `xpaysh/awesome-x402` PR branch (`add-openai-agents-nano-v2` @ b9e9b5f),
  which names 543 USDC entries and zero XNO while the live Bazaar indexes XNO.
- **Outreach**: the one verified live XNO x402 seller (`pyfile-toolkit`, an agent-operated service,
  contact `pyfile-toolkit@mail.ru`) received a factual report — validator reachability finding, the
  adapter as a second independent client, and an offer to make a real paid XNO call. Filed through
  the fork-issue route (`PANDeveloper001/nano-llm-api` issue 1) because upstream issue creation and
  fork→upstream PRs are both 403 on the current token.

## Raw data

- `/root/work/openai-agents-nano-x402/.ledger/tmp/bazaar_scan2.json` — full scan: counts, networks,
  every Nano accept entry (resource, asset, scheme, amount, payTo).
- validator responses are reproducible with the curl in the table above.
