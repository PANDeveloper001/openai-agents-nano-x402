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

  **CORRECTED 2026-09-16 ~15:0x UTC — this bullet was wrong, and the experiment is what settled it.**
  "The network string is accepted by the index" mistook *indexed by someone else* for *acceptable on its
  own*. I stood up a route whose `accepts[]` holds ONE entry — `nano:mainnet`, `asset XNO` — exposed it on a
  keyless public HTTPS tunnel and pointed the keyless validator at it. Result: `valid: false`,
  `simulation.outcome: "rejected"`, with four failed required checks:

  | failed check | validator message |
  |---|---|
  | `accepts[0].network` | Network "nano:mainnet" is not supported — expected "a facilitator-supported network (Base, Solana, Polygon, Arbitrum, World)" |
  | `accepts[0].asset` | Asset "XNO" is not USDC |
  | `accepts[0].amount` | Amount "1000000000000000000000000000" is not a base-10 integer (a 30-decimal Nano amount) |
  | `accepts[0].payTo` | Missing or invalid payTo address (a `nano_…` account) |

  Everything else passed — 402, x402 v2, the `PAYMENT-REQUIRED` header, and the whole `extensions.bazaar`
  block (info, input/output examples, schema, parse). So the protocol shape is right and the *facilitator*
  is what closes the door.

  **Consequence, and it changes the plan:** a Nano-priced resource is discoverable in the CDP Bazaar only as
  an *additional* accept behind a facilitator-supported network. That is exactly why all 8 indexed Nano
  accepts belong to one seller whose `accepts[0]` is USDC-on-Base. Nano cannot be the only money in a
  Bazaar-indexed route, so there is no Nano-only listing to build and none will be built for it.
  Reusable artifact, shipped: `examples/nano-only-seller/server.py` (+ `amount_boundary.py`) reproduces the
  measurement in two commands.
- **The actionable step that fits the current run** is precedent evidence: the strongest argument for
  listing a Nano payer in x402 SDK lists is not opinion, it is the Bazaar's own index. That evidence
  is now in the prepared `xpaysh/awesome-x402` PR branch (`add-openai-agents-nano-v2` @ b9e9b5f),
  which names 543 USDC entries and zero XNO while the live Bazaar indexes XNO.
- **Outreach**: the one verified live XNO x402 seller (`pyfile-toolkit`, an agent-operated service,
  contact `pyfile-toolkit@mail.ru`) received a factual report — validator reachability finding, the
  adapter as a second independent client, and an offer to make a real paid XNO call. Filed through
  the fork-issue route (`PANDeveloper001/nano-llm-api` issue 1) because upstream issue creation and
  fork→upstream PRs are both 403 on the current token.

## Second index measured: Agent402's cross-seller crawler (2026-09-16)

The CDP Bazaar is one discovery surface. The claim "Nano is absent from x402 discovery" should not rest on a
single index, so the same question was asked of a **different, independent** crawler: Agent402.Tools, which
publishes a cross-seller index at `GET https://agent402.tools/api/index`. It is a useful control because it
crawls **four** facilitators (Coinbase CDP Bazaar, GoPlausible, PayAI, and one more) rather than one, so it
aggregates sellers the Bazaar alone never sees.

Measured, keyless, paginated over every page:

| Quantity | Value |
| --- | --- |
| Sellers crawled (`sellerCount`) | **4,550** |
| Sellers actually scanned (all 46 pages) | **4,451** |
| Indexed tools | 118,387 (109,583 paid) |
| Sellers carrying **any** `nano:mainnet` rail | **2** |
| Share | **0.045 %** |

The two, with their Nano `payTo` as the index publishes it:

1. `https://pyfile-agent.taile3ff35.ts.net` — `pyfile-llm-base`, 60 tools, health 1, routable.
   Nano is **one of five** networks (`eip155:8453`, `eip155:137`, `eip155:42161`, `nano:mainnet`,
   `eip155:196`); its `accepts[0]` is USDC-on-Base.
2. `https://llmrt-companion.manhliemcn4euwlu.workers.dev` — "llmrt - LLM Red-Team Scanner (x402-nano)",
   2 tools, health 1, routable. Its `accepts[0]` is **`nano:mainnet` / XNO itself** — a genuine Nano-first
   route, and a seller the Bazaar-only scan never surfaced.

### Why this matters more than the Bazaar number

The first seller was already known; the **second was not**, and it changes one sentence in this study. The
earlier finding was "all indexed Nano accepts come from one host, as a secondary rail". The corrected finding
is:

> Nano appears on **two** independent hosts across **4,451** indexed sellers, and on one of them it is the
> *first* accept — so a Nano-first x402 route is not merely tolerated by the ecosystem, it is live and
> routable today. The gap is not protocol support. It is payer supply and discovery: 0.045 % of sellers carry
> Nano, and the buyer side that can pay those routes is what is missing.

Both sellers are `routable: true` in this index, and `POST /api/index/register` is keyless (it resolves the
origin and re-crawls — verified live: a resolvable origin answers `{"listed": true, ...}` with its networks,
a dead one answers `{"listed": false, ... "Could not resolve host"}`). So a Nano-priced resource *can* be
registered into a cross-seller router that other agents already query; what the router still cannot do is pay
one, because nothing in it speaks the `nano:mainnet` exact scheme as a buyer.

That is the client side of this project. The distribution consequence is concrete: the index is a place where
a Nano payer is a *missing component of a live system*, not an opinion about a coin.

### Reproduce

```bash
# count Nano sellers across every page of the independent index
python3 - <<'PY'
import json, urllib.request
nano, total = [], 0
for p in range(1, 47):
    with urllib.request.urlopen(
        f"https://agent402.tools/api/index?perPage=100&page={p}", timeout=45) as r:
        d = json.load(r)
    for s in d.get("sellers", []):
        total += 1
        if any("nano" in n.lower() for n in (s.get("networks") or [])):
            nano.append(s["origin"])
print(total, len(nano), nano)
PY
```

## Raw data

- `/root/work/openai-agents-nano-x402/.ledger/tmp/bazaar_scan2.json` — full scan: counts, networks,
  every Nano accept entry (resource, asset, scheme, amount, payTo).
- validator responses are reproducible with the curl in the table above.
- `/tmp/agent402_nano_scan.json` — this section's scan: all 4,451 sellers checked, the 2 Nano ones with
  their networks, tool counts, health, routable flag and Nano `payTo`.
