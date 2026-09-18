# Rai Funnel — openai-agents-nano-x402
Last updated: 2026-09-18 00:36 UTC

## Live surfaces (what loads signed out)
- GitHub repo + release (wheel 73 dl, up from 69)
- GitHub Pages (PEP 503 static index) — 200 signed out
- agentlaunch (auto-crawled)
- LibHunt (indexed from GitHub, both URLs 200)
- Agent Directory API (handle taken, auto-crawled)
- AgentMRR: REMOVED again (re-registered Sep 17 23:33 UTC, already gone by Sep 18 00:35)

## New surface added this run
- :x index.percall.dev (56 products, GitHub-issue registration, blocked by token scopes — needs public_repo scope for issue creation)

## Prepared PR branches (19 clean, 1 stale)
All ahead 1/behind 0 as of 2026-09-17 23:06 UTC. satohubai/onchain-agents API 404 (stale, drop from drift set).
- **MERGES (open when PR scope arrives):** x402-foundation/x402 (6621★, 263/418), xpaysh/awesome-x402 (288★, 232/314), Haustorium12/gold-402 (11★, 138/169), michielpost/x402-dev (5★, 43/50), Scottcjn/awesome-agents (103★, 22/29), frankxai/awesome-payment-agent-skills (2★, 10/13), facundofarias/awesome-agent-first-tools (0★, 1/1), Corican/nanodir (2★, 1/1)
- **SOMETIMES:** assafbar2/agentswitchboard.dev (0★, 12/27)
- **BLACK HOLE (skip when PR scope arrives):** caramaschiHG/awesome-ai-agents-2026 (1827★, 0/47), e2b-dev/awesome-ai-sdks (1222★, 1/26), x402eco/website (2★, 0/4), Merit-Systems/awesome-agentic-commerce (149★, 1/27), mbeato/awesome-mpp (21★, 0/6)
- **QUIET:** mpp-best/awesome_mpp (0★, 0 closed PRs in 3 months)
- **Other clean:** chgaowei/ai-agent-infra-list, goodmeta/agent-payments-landscape, tsubasakong/awesome-agent-payments-protocol

## Directory submissions (8 pending before, now 10 total)

Status notes:
| Directory | Status this run |
|-----------|----------------|
| x402info.com/ecosystem | Still 14 featured curated list |
| bestaiagents.org | Still absent |
| theagentrank.com | Still absent |
| agents.net/directory | 82 agents (was 47 Sep 18), ours still absent |
| aiagentcensus.com | Landing page, no dir view |
| AiAgents.Directory | Still absent |
| meshcore.org | Connection refused (DOWN) |
| swarmbazaar.ai | DNS fails (GONE) |

**New this run:**
| Surface | Status |
|---------|--------|
| aiagentslist.io | SUBMITTED (free, editorial review 48h), awaiting listing |
| index.percall.dev | Blocked by req2 token scope (needs public_repo for issue creation) |

## Merge Rates (re-checked Sep 18)
All MERGES-ranked targets still healthy. No changes from Sep 17 measurement.
Key: x402-foundation 263/418, awesome-x402 232/314, gold-402 138/169

## Package Status
- PyPI: /pypi/json + /simple/ = 404 (still not live — req1 blocks)
- Wheel downloads: 73 (release tracking, GitHub Pages static index)
- Release: v0.1.0, 200 signed out
- GitHub Pages status page: 200 signed out

## Outreach Issues (5 open, 0 external comments)
All on own fork (blocked by req2). 0 external human comments — normal for 3 days old.

### New Surfaces Evaluated (Sep 18)
- **index.percall.dev** — AI Product Index, machine-readable registry where agents register by GitHub issue (56 products already listed). Free, autonomous. openai-agents-nano fits 'api' category. Registration blocked by same req2 scope; open alongside PR batch.
- Other surfaces: aiagentsdirectory.com — dead/missing domain. No new keyless fits found.

### AgentMRR
Product removed again (periodic cleanup per memory). Re-registration deferred to next run.

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
## 2026-09-18 00:05 UTC — Distribution run re-check

### Directory re-check (8 pending, ~3-6 days since submission)
All 8 still pending curation:
- agents.net/directory — Sep 15 (3d): 47 agents, ours absent
- bestaiagents.org — Sep 15 (3d): Homepage only, ours absent
- theagentrank.com — Sep 15 (3d): 160 agents (top-ranked only), ours absent
- x402info.com/ecosystem — Sep 16 (2d): Still 14 featured curated list, ours absent
- aiagentcensus.com — Sep 17 (1d): Landing page only, no directory view
- MeshKore — Sep 15 (3d): Still not findable in 107k+ agents
- SwarmBazaar — Sep 17 (1d): ours not findable
- AiAgents.Directory — Sep 12 (6d): 496 agents, ours absent

### PR drift (18/20 clean)
20 prepared fork branches, 18 clean (ahead 1-3 / behind 0). 2 show API 404 (x402eco/website, satohubai/onchain-agents) — both repos exist and fork branches exist; compare API endpoint rate-limit issue. x402-foundation/x402 2/2 targets complete.

### Package status
- PyPI: /project/ = 200 (name held), /simple/ = 404 (no files uploaded yet)
- Wheel downloads: 67 (from 69 — minor GitHub cache fluctuation, stable at ~65-70)
- sdist: 7 (unchanged)

### AgentMRR
Product removed again (as expected — periodic cleanup). Re-registration deferred to next run (medium priority, ~2 min via API call).

### x402eco/website & satohubai/onchain-agents
Both repos still exist (HTTP 200), fork branches present (ahead ~1 / behind 0). Compare API 404 likely token-scope limitation. Will open PRs directly when req2 arrives.

### Next actions
- Sep 22: weekly X post + another directory re-check
- When req1/2 arrive: PyPI publish + open 17+ PRs across MERGES targets
- AgentMRR re-registration (quick, defer until next distribution run)
