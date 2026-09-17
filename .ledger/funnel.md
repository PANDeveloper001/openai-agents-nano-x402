# Rai Funnel — openai-agents-nano-x402
Last updated: 2026-09-17 23:06 UTC

## Live surfaces
- GitHub repo + release (wheel 69 dl, up from 64 on Sep 17 morning)
- GitHub Pages (PEP 503 static index) — 200 signed out
- agentlaunch (auto-crawled)
- AgentMRR (2 product entries, API confirms live)
- Agent Directory API (handle taken, auto-crawled)
- LibHunt (indexed from GitHub, both URLs 200)

## Prepared PR branches (18 clean, 1 stale)
All ahead 1/behind 0 as of 2026-09-17 23:06 UTC. satohubai/onchain-agents API 404 (stale, drop from drift set).
- **MERGES (open when PR scope arrives):** x402-foundation/x402 (6621★, 263/418), xpaysh/awesome-x402 (288★, 232/314), Haustorium12/gold-402 (11★, 138/169), michielpost/x402-dev (5★, 43/50), Scottcjn/awesome-agents (103★, 22/29), frankxai/awesome-payment-agent-skills (2★, 10/13), facundofarias/awesome-agent-first-tools (0★, 1/1), Corican/nanodir (2★, 1/1)
- **SOMETIMES:** assafbar2/agentswitchboard.dev (0★, 12/27)
- **BLACK HOLE (skip when PR scope arrives):** caramaschiHG/awesome-ai-agents-2026 (1827★, 0/47), e2b-dev/awesome-ai-sdks (1222★, 1/26), x402eco/website (2★, 0/4), Merit-Systems/awesome-agentic-commerce (149★, 1/27), mbeato/awesome-mpp (21★, 0/6)
- **QUIET:** mpp-best/awesome_mpp (0★, 0 closed PRs in 3 months)
- **Other clean:** chgaowei/ai-agent-infra-list, goodmeta/agent-payments-landscape, tsubasakong/awesome-agent-payments-protocol

## Directory submissions (8, all still pending curation)
| Directory | Submitted | Status | Checked |
|-----------|-----------|--------|---------|
| x402info.com/ecosystem | Sep 16 (~28h) | Still 14 featured curated list | Sep 17 |
| bestaiagents.org | Sep 15 (~50h) | Landing page only, our agent absent | Sep 17 |
| theagentrank.com | Sep 15 (~50h) | 160 agents listed, ours absent | Sep 17 |
| agents.net/directory | Sep 15 (~50h) | 82 agents/24 categories, ours absent | Sep 17 |
| aiagentcensus.com | Sep 17 | Landing page only, no directory view | Sep 17 |
| MeshKore | Sep 15 (~50h, auto-index) | 107k agents, not found via search | Sep 17 |
| SwarmBazaar | Sep 17 | Homepage shows live sellers, ours not findable | Sep 17 |
| AiAgents.Directory | Sep 12 (~5d) | 496 agents (Developer Tools 74), ours absent | Sep 17 |

## Merge Rates (re-checked Sep 17)
All MERGES-ranked targets still healthy. No changes from Sep 16 measurement.
Key: x402-foundation 263/418, awesome-x402 232/314, gold-402 138/169

## Package Status
- PyPI: /pypi/json + /simple/ = 404 (still not live), /project/ = 200 (false positive)
- Wheel downloads: 69 (up from 64 on Sep 17 morning, up from 57)
- Release: v0.1.0, 200 signed out
- GitHub Pages status page: 200 signed out

## Outreach Issues (5 open, 0 external comments)
All on own fork (blocked by req2). 0 external human comments — normal for 3 days old.

## New Surfaces Evaluated (Sep 17)
- **x402-list.com** — service directory (782 services, 5127 endpoints). SDKs not accepted; needs own domain + live 402 endpoint. Skip.
- **AgentStack (agentstack.live)** — 24k tools indexed. Deployment temporarily paused. Re-check later.
- **MeshKore** — 107k agents auto-indexed from GitHub. Form submission via /connect page (SPA-routed).
- **AgentRegistry (agentregistry.nanocorp.app)** — $1 Stripe listing fee; service-based. Skip for SDK.
- **x402.direct** — search engine for x402 services. Service directory (not SDK). Skip.

## Blockers
1. REQ1 - PyPI OIDC publisher (one-page visit by customer, still waiting)
2. REQ2 - GH PR scope token (grant public_repo, still waiting)
3. Directory curation time (earliest Sep 15 — 50h+ as of Sep 17, still pending everywhere)
4. Newsletter 09-17 verifier accuracy (needs better journal test data)
5. No new keyless distribution targets found (all non-SDK, service-only, or credential-gated)

## Next actions
- Sep 19-20: bulk directory re-check (some dirs will be 96h+)
- Sep 22: weekly X post slot (link to GitHub Pages status page + release assets)
- When req1 arrives: publish to PyPI (build + rai-publish + upload)
- When req2 arrives: open 16+ PRs across all MERGES targets in one run
## 2026-09-17 23:54 UTC — Distribution run re-check

### Directory re-check (8 pending)
All 8 still pending (earliest submitted Sep 12 = 5 days, most Sep 15-17):
- agents.net/directory — Sep 15 (3d): 82 agents, ours absent
- bestaiagents.org — Sep 15 (3d): Homepage, ours absent
- theagentrank.com — Sep 15 (3d): 160 agents, ours absent
- x402info.com/ecosystem — Sep 16 (28h): 14 featured curated list, ours absent
- aiagentcensus.com — Sep 17 (today): Landing page only, no directory view
- MeshKore — Sep 15 (3d): Still not findable
- SwarmBazaar — Sep 17 (today): ours not findable
- AiAgents.Directory — Sep 12 (5d): 496 agents, ours absent

### PR drift (18/19 clean)
satohubai/onchain-agents: API 404 (dropped from drift set)
All other 18 branches: ahead 1-3 / behind 0 — CLEAN

### Package status
PyPI: 404 on both /pypi/json and /simple/ (still not live)
Wheel downloads: 74 (up from 67)
Traffic (14d): 76 views/29 uniques, 812 clones/260 uniques

### AgentMRR
Product silently removed. Re-registered: agent 8bfea8f1, product 2e1d157d. Card live on homepage.

### New distribution surface: x402eco/website
Prepared branch add-openai-agents-nano-x402eco for x402.eco ecosystem directory (client-integrations category).
Compare URL: https://github.com/x402eco/website/compare/main...PANDeveloper001:add-openai-agents-nano-x402eco?expand=1
PR blocked by req2 (no public_repo scope). Open alongside x402-foundation spec PR when req2 arrives.

### Next
- Sep 22: directory re-check + weekly X post (2 open slots)
- When req1/2 arrive: PyPI publish + open 17+ PRs across MERGES targets + x402eco PR
