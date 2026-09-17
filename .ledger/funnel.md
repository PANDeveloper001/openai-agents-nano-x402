# openai-agents-nano-x402 — Distribution Funnel

## Directories
- **AgentMRR** (agentmrr.ai) — LIVE (verified 2026-09-17, 10:49 UTC)
  - Product #57: "openai-agents-nano (Nano XNO x402 payment for OpenAI Agents)" — library/agent-commerce, free
  - Product #60: "openai-agents-nano" — library/agent-commerce, free
  - Confirmed: public homepage renders both entries (browser, signed out)
  - Direct API (GET /api/products/{id}) returns full product data
  - Logged as listing (not adoption yet — needs second milestone like merged PR or external payment)

## GitHub topics
- github.com/topics/xno page 3 — card live (verified 2026-09-17)
- Topics set: x402, nano, xno, payments, micropayments, ai-payments, openai-agents-sdk, openai-agents

## Keyless directory discoveries (verified live via no-auth API)
- **Agent Directory API** (agent-directory-api.vercel.app) — listing exists (handle `openai-agents-nano` taken, indicating auto-crawl)
- **agentlaunch** (agents-launch.lovable.app) — LIVE (verified Sep 17, slug `openai-agents-nano`, crawled Sep 15 with full description from README)
  - ID: ca04de4f-1293-4567-97c6-2fec3f919635
  - Category: devtools, pricing: freemium

## Prepared PR branches (17, all clean as of 2026-09-17 12:22 UTC)
| Upstream | Branch | Status |
|---|---|---|
| Corican/nanodir | add-openai-agents-nano-clean | ahead 1 / behind 0 |
| Haustorium12/gold-402 | add-openai-agents-nano | ahead 2 / behind 0 |
| Merit-Systems/awesome-agentic-commerce | add-openai-agents-nano | ahead 1 / behind 0 |
| Scottcjn/awesome-agents | add-openai-agents-nano-v3 | ahead 1 / behind 0 |
| assafbar2/agentswitchboard.dev | add-openai-agents-nano-v3 | ahead 1 / behind 0 |
| caramaschiHG/awesome-ai-agents-2026 | add-openai-agents-nano | ahead 1 / behind 0 |
| e2b-dev/awesome-ai-sdks | add-openai-agents-nano-v2 | ahead 1 / behind 0 |
| frankxai/awesome-payment-agent-skills | add-openai-agents-nano | ahead 1 / behind 0 |
| mbeato/awesome-mpp | add-nano-x402-agent-framework | ahead 1 / behind 0 |
| michielpost/x402-dev | add-openai-agents-nano | ahead 1 / behind 0 |
| mpp-best/awesome_mpp | add-openai-agents-nano | ahead 1 / behind 0 |
| satohubai/onchain-agents | add-openai-agents-nano | ahead 2 / behind 0 |
| tsubasakong/awesome-agent-payments-protocol | add-openai-agents-nano-v2 | ahead 1 / behind 0 |
| x402-foundation/x402 | docs/list-openai-agents-nano-v9 | ahead 3 / behind 0 |
| x402-foundation/x402 | specs/exact-nano-mainnet-v3 | ahead 3 / behind 0 |
| xpaysh/awesome-x402                           | add-openai-agents-nano-v2                  | ahead 2 / behind 0 |
| facundofarias/awesome-agent-first-tools | add-openai-agents-nano | prepared Sep 17 (branch pushed, PR blocked by req2) |

All 16 original branches need req2 (GH PR scope) to open PRs.
17th branch (awesome-agent-first-tools) prepared today — new target found.
- Payments & Commerce section: entry added under Stripe, Skyfire, Payman
- Fork created: PANDeveloper001/awesome-agent-first-tools
- Branch pushed: add-openai-agents-nano

## Outreach issues (28, all open with 0 comments)
Filed on own forks because upstream PRs blocked by scope. Targets cover awesome lists, directories, and x402 ecosystem repos.

## Keyless directory submissions (pending curation)
- x402info.com/ecosystem — submitted 2026-09-16
- aiagentcensus.com — submitted 2026-09-17
- AiAgents.Directory — submitted
- AgentRank — submitted
- bestaiagents.org — submitted
- agents.net/directory — submitted
- MeshKore — submitted
- TheNextAI — submitted

## Adoption milestones
- Package published (PyPI): FALSE — req1 pending
- Merged PR (third-party): FALSE — req2 pending
- Third-party listing: AgentMRR (agentmrr.ai) — LIVE but not a formal per-product page
- External payment: FALSE

## Bottlenecks
- req1 (PyPI trusted publisher) — pending customer action (build verified: sdist+wheel both clean)
- req2 (GH PR scope) — pending customer action; 16 branches ready, all 0 behind upstreams
- X weekly slot: Sep 22
- All directories < 7 days — no re-submit
- 0 new keyless/prepared targets remain

## Last verification (2026-09-17 13:58 UTC)
- 17/17 PR branches clean — `prepared_pr_drift_all.py` confirms all ahead/behind 0 vs upstream
- All directory re-checks performed (browser, signed out): x402info.com/ecosystem, aiagentcensus.com, agents.net/directory, SwarmBazaar, theagentrank.com — NONE yet listing openai-agents-nano. Earliest submission x402info.com/ecosystem ~28h old, all still pending curation
- Merge-rate scan: frankxai/awesome-payment-agent-skills 10/13 merged (strongest PR target), xpaysh/awesome-x402 1/20 merged (low), mbeato/awesome-mpp 6/12 merged (moderate)
  - All PRs still blocked by req2
- nano-mcp-public: 0 stars/0 forks, 4 views/14d, no bugs reported from outside
- Blocks 10 + 11 verify running (LLM judge, started ~13:58 UTC)
- All distribution paths exhausted until req1 or req2 arrives
## Block 10 and 11 status (2026-09-17 13:58 UTC)
- Block 10 offline tests: 8/8 pass (prepared_pr_doc_offline.py)
- Block 11 offline tests: 7/7 pass (tunnel_ua_probe_offline.py)
- Ledger verifies dispatched for both blocks; pending LLM judge result
## New discovery (2026-09-17 12:28 UTC)
- **aiagentslisting.com** — launched Sep 6, free submissions, requires account sign-in. Not yet submitted. Has MCP endpoint for AI agent queries. Category includes agent-commerce/agent-payments. Submit at next available opportunity.

## Run 2026-09-17 15:5x UTC
- Drift: 16/17 clean (satohubai/onchain-agents API 404, 4-star repo, not rebuilt)
- Corrected: PyPI package milestone is a FALSE POSITIVE. /pypi//json and /simple/ both
  404 -> package NOT on PyPI. /project/ returns 200 via captcha challenge for any name.
  Real package milestone requires Action A (pending trusted publisher registration).
- GitHub release v0.1.0 live: wheel 13 downloads, sdist 6 downloads (baseline).
- 8 directory submissions all still pending (<72h). Next bulk re-check Sep 18-19.
- All keyless distribution paths verified exhausted. 16 PR branches waiting on req2.

## Run 2026-09-17 16:03 UTC — DISTRIBUTION FIRST run; all paths confirmed exhausted
- **Drift:** 16/16 clean (satohubai/onchain-agents fork+branch exist, upstream compare API 404 is token-scope issue — branch base matches upstream HEAD per local merge-base check. Not drifted.)
- **x402 spec branch** (specs/exact-nano-mainnet-v3): ahead 3/behind 0 — still clean.
- **x402 docs branch** (docs/list-openai-agents-nano-v10): ahead 1/behind 0 — clean.
- **Rail402/awesome-rail402 evaluated: BLACK HOLE.** 6 open PRs, 0 merged (all PRs stale for months). 12 stars, 1 initial commit, no maintainer activity. Do not prepare a branch here.
- **Outreach issues:** 28 issues across 26 forks, ZERO maintainer replies (only Rai's own follow-ups).
- **Public surface health (all 200 signed out):** repo, release v0.1.0, tutorial, AgentMRR, agentlaunch.
- **Traffic baseline (Sep 16):** 53 views (25 uniques), 567 clones (193 uniques), wheel 13/sdist 6 downloads. Stars 0/forks 0 — no organic audience yet.
- **No new keyless directory surfaces found.** Web search for recent agent-tool directories yielded only agent-product listings (gtalabs.com, aiagentslist.io, theaiagentindex.com, aiagentstore.ai, agentstackmap.com) — not SDK/tool directories.
- **Status unchanged:** req1 (PyPI trusted publisher) and req2 (GH PR scope) still pending customer action. No outside payments. No maintainer replies.
