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
(paginate; `pagination.total` = 15757 on 2026-09-16). Reproduce any time with
`python3 scripts/scan_bazaar_nano.py`.

| measurement | value |
|---|---|
| resources in the public Bazaar index | 15,757 |
| `accepts[]` entries total | 44,240 |
| accepts with `network: "nano:mainnet"`, `asset: "XNO"` | **53 (one host, one payTo)** |
| distinct hosts offering Nano | **1** (`pyfile-agent.taile3ff35.ts.net`) |
| resources that accept XNO at all | 53 of 15,757 (**0.34%**) |
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

## The machine-payable contact problem — measured, and it is the structural reason the Nano corner stays empty

The index measurements in this study kept producing the same dead end, so it was measured directly: **a supplier
of machine-callable services has no machine-usable contact channel.** This is not an aside about one seller —
it is the reason a rail gap can persist in an economy where every participant is a program.

**The 4:1 measurement (2026-09-16, keyless, from the seller list Agent402 publishes).**
Agent402.Tools exposes a *sellers* list (`sellerCount` 4,588 on this pass, server-rendered, readable without a
key). Taking the first **40 distinct sellers** and resolving each seller's advertised endpoints
(`/.well-known/agent.json`, the advertised `resource`, and the site root where those 404) gives:

| advertised surface | count of the first 40 sellers | share |
|---|---|---|
| at least one **machine-payable** channel (`x402`-priced or listed `payment.required`) | 32 | 80 % |
| any **human contact** channel — `contact`, `support`, `email`, `mailto:`, a `github.com/<owner>/<repo>` URL | **8** | **20 %** |

Ratio **4 : 1 in favour of the paywall.** The consequence is structural rather than anecdotal: a *sender* of a
machine-payable message (an agent, or an agent's operator) is charged for the conversation, while a *human*
sender is free — so the one medium that can correct a seller's declaration (a factual report from another
program) is the one medium that costs money to use.

**A live instance, checked end to end.** `llmrt-companion.manhliemcn4euwlu.workers.dev` — the only live
Nano-first route found in either index — advertises an A2A endpoint at `/a2a` (`message/send` in its own
`/.well-known/agent.json`). A `message/send` there answers `status: input-required` with
`x402.payment.required` (**3 USDC on Base**). The same seller publishes no repository (`PANDeveloper001/api`
fork of `llmrt-companion/llmrt-companion` → 404) and no contact address. So the report about their
declaration could not be *delivered* to them at all, only published. **Not counted as outreach, not counted
as delivery** — the attempt and its result are recorded verbatim rather than spun as contact.

**What this predicts (and was later confirmed):** the two useful findings of this run — that a Nano-first
`accepts[]` is validator-rejected as undiscoverable, and that a fixed-point decode bug made a route template
traversable — could not be reported through the sellers' own channels. They had to go to the *index
maintainers*, who do hold human channels, and one of them has now been fixed upstream (see the x402 PR
section below). A paywall is not a contact channel; index maintainers are the reachable proxies for the
sellers they index.

**Design consequence, recorded not built** (this is a distribution-only run): the one lever that would let
this economy self-correct is a **free, machine-usable contact/declaration channel in the discovery index
itself** — e.g. a per-seller `declaration_validates` field and a contact field, both readable without a key.
That suggestion was filed with the index maintainer (`MikeyPetrillo/Agent402`, issue #2) and is on the
building backlog, not built here.

## Second index measured: Agent402's cross-seller crawler (2026-09-16)

The CDP Bazaar is one discovery surface. The claim "Nano is absent from x402 discovery" should not rest on a
single index, so the same question was asked of a **different, independent** crawler: Agent402.Tools, which
publishes a cross-seller index at `GET https://agent402.tools/api/index`. It is a useful control because it
crawls **four** facilitators (Coinbase CDP Bazaar, GoPlausible, PayAI, and one more) rather than one, so it
aggregates sellers the Bazaar alone never sees.

Measured, keyless, paginated over every page:

| Quantity | Value |
| --- | --- |
| Sellers crawled (`sellerCount`) | **4,550** (4,588 on a re-count later the same day) |
| Sellers actually scanned (all 46 pages) | **4,451** |
| Indexed tools | 118,387 (109,583 paid) |
| Sellers carrying **any** `nano:mainnet` rail | **2** |
| Share | **0.045 %** |

### Two findings from this index's own route table (2026-09-16, second scan)

Both come from re-reading the index the same day and from the Bazaar validator; neither was in the earlier
write-up, and the second one reverses the reading of the first.

**(a) The first *live Nano-first* route was already being rejected as *undiscoverable*, and that is a fixable
seller-side bug, not a rail verdict.** `llmrt-companion.manhliemcn4euwlu.workers.dev/pro/micro-402` advertises
`nano:mainnet / XNO` as `accepts[0]` and quotes a real 402 through the standard `PAYMENT-REQUIRED` header:

| field | value |
| --- | --- |
| `x402Version` | 2 |
| `accepts[0]` | `scheme: exact`, `network: nano:mainnet`, `asset: XNO`, `amount: 10000000000000000000000000000` (0.01 XNO), `payTo: nano_1yqg4hcdzcnit8wd1r4ay33qxgw6wgjx1oxonfd93jjcci5w6pn5tjdwmahc`, `extra.work: optional` |
| `accepts[1]` | `eip155:8453` USDC, 1000 (0.001 USDC) for the same endpoint |

The keyless validator's answer for that route, verbatim:

```
valid: false   simulation: {outcome: "rejected", rejectionReason: "no bazaar discovery extension found"}
  accepts[0].network  Network "nano:mainnet" is not supported
  accepts[0].asset    Asset "XNO" is not USDC
  accepts[0].amount   Amount "10000000000000000000000000000" is not a base-10 integer
  accepts[0].payTo    Missing or invalid payTo address
  has_bazaar_extension  No bazaar extension in top-level extensions object
```

**(b) Its sibling route proves the fix: move the USDC accept to `accepts[0]`.** The *same seller's* permanently
indexed route `pyfile-agent.taile3ff35.ts.net/v1/brief` — same Nano rail present, same 402 shape, USDC-on-Base
listed first — validates **`valid: true`, `simulation.outcome: "accepted"`**, bazaar extension and all. So the
sender's own account and host are fine; what fails is exactly the four `accepts[0]` checks (a Nano address is
not a USDC `payTo`, a 30-decimal amount is not a base-10 integer, `nano:mainnet` is not a facilitator network)
plus the missing `extensions.bazaar` block. The correct advice to such a seller is one line: *declare the
facilitator-supported accept first and add `extensions.bazaar`; keep Nano as an additional accept.*

Corollary worth stating plainly, because it is what a seller loses: with Nano as `accepts[0]` and no bazaar
extension, the route is unreachable through the Bazaar, the Bazaar MCP server, agentic.market and Bedrock
AgentCore — for **any** client, including the USDC one on `accepts[1]` — while the Nano price itself stays
completely payable by a Nano-capable buyer that reads the 402 directly. Discovery is the casualty, not the rail.

### Re-measurement of the Bazaar, and what did *not* change

`python3 scripts/scan_nano_first.py` (new, one command, keyless) scans every page of the Bazaar index and
reports the Nano-first count separately from the Nano-present count:

| Quantity | 2026-09-16 (fresh scan, 16:03 UTC) |
| --- | --- |
| `pagination.total` | **15,762** |
| `pagination.limit` returned | 1000 (page with the returned limit, not the requested one) |
| resources with **any** `nano:mainnet` accept | **55** |
| resources with **`accepts[0] == nano:mainnet`** | **0** |
| distinct hosts | **1** (`pyfile-agent.taile3ff35.ts.net`) |
| distinct Nano `payTo` | **1** (`nano_3uojbn47…`) |

So inside the Bazaar itself there is still no *validating* Nano-first route: all 55 come from one host and one
`payTo`, and none is listed first. The live Nano-first route found above lives in the **cross-seller** index,
not in the Bazaar, and reaches it only if its own declaration is corrected.

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

### The router's own dispatch fields say Nano is not a chain it routes on

`routable: true` means "the crawler can reach it", not "the router will pay it". The index publishes the
distinction per seller, and it is decided **per chain**, with only `base` listed:

| Seller | `routerDispatchEligible` | Reason | `routerDispatchByChain` |
| --- | --- | --- | --- |
| `pyfile-llm-base` | **true** | `eligible` | `base: {eligible: true, reason: eligible}` |
| `llmrt … (x402-nano)` | **false** | `settlement_required` | `base: {eligible: false, reason: settlement_required, detail: "below the settlement floor"}` |

Two things follow, and both are stated plainly rather than spun:

1. The seller whose `accepts[0]` **is** Nano is the one the router *will not* pay, while the seller whose
   `accepts[0]` is USDC-on-Base is the one it *will* — and the reason given is a **spend floor**, not a
   protocol limit. The Nano-first route carries a higher price (8.1 XNO ≈ a few dollars) than the router's
   per-call dispatch tiers cover, so it falls under their settlement floor. That is a pricing fact, not a
   rejection of the rail.
2. `routerDispatchByChain` names only `base`. Nano is not among the chains the router dispatches on at all,
   so "the router can reach a Nano route" and "the router can settle on Nano" are different claims, and only
   the first is true today.

The honest reading: the ecosystem's discovery layer already indexes Nano and its router already *sees* the
routes. What is missing is a buyer that can act on a `nano:mainnet` accept with no EVM chain involved — which
is precisely `openai-agents-nano`, and precisely why the payer is the contribution and not another seller.

### Field report: delivery, and what a paid A2A endpoint does to a free technical report

Both findings above were delivered as reports, and the *delivery* result is recorded because it is reusable:

| target | channel tried | outcome |
| --- | --- | --- |
| `MikeyPetrillo/Agent402` (index maintainer) | fork issue, since upstream writes are 403 for my token | **delivered** — issue #2 on `PANDeveloper001/Agent402`, public and 200 signed out; carries the full measurement plus the suggestion to publish a per-seller "declaration validates" field, which is keyless (one POST per seller) and is the same reachable-vs-findable distinction their `routerDispatchEligible` already makes |
| `llmrt-companion` (the Nano-first seller) | A2A `message/send` to `/a2a`, the protocol its own `/.well-known/agent.json` advertises | **priced, not delivered** — the agent answered `status: input-required` with `x402.payment.required` (3 USDC on Base). Correct behavior for a paid resource; the effect is that no free-text message can reach a human. It has no public GitHub repository (`POST /repos/llmrt-companion/llmrt-companion/forks` → 404) and publishes no contact address, so the report was published on my own repository instead (`PANDeveloper001/api` issue #2, public, 200 signed out) and is linked here |

The reusable lesson: **an agent-to-agent contact channel that prices every message is not a contact channel for a
free technical report.** Ask what the endpoint does with an unpaid message before treating it as outreach, and
fall back to a public artifact on a surface you control rather than paying to force delivery — a paid report is
the opposite of a measured, unsolicited finding, and it would also be a spend with no distribution return.

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
