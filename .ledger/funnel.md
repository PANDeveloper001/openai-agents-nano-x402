# Rai Funnel — openai-agents-nano-x402
Last updated: 2026-09-17 21:02 UTC

## Live surfaces
- GitHub repo + release (wheel 32 dl, sdist 7 dl)
- GitHub Pages (PEP 503 static index)
- agentlaunch (auto-crawled)
- AgentMRR (2 product entries)
- Agent Directory API (handle taken, auto-crawled)
- LibHunt (indexed from GitHub)

## Prepared PR branches (18 clean, 1 stale)
All ahead 0-3 / behind 0. Clean as of 2026-09-17 21:02 UTC. satohubai/onchain-agents API 404 (stale, drop next run).
- 7 MERGES-ranked targets (high merge rate)
- 4 BLACK HOLE targets (skip when PR scope arrives)
- 6 other targets (agentswitchboard, nanodir, e2b-dev, etc.)
- NEW 2026-09-17: chgaowei/ai-agent-infra-list (50★, 83% merge rate): branch `add-x402-nano-settlement-rail`, adds x402 + Nano (XNO) rail to section 7 Commerce & payments (was x402-free). Fork pushed, ahead 1/behind 0, compare URL 200 signed out.
- Evaluated-not-fit 2026-09-17: RiccardoBiosas/awesome-agentic-payments (2★, 100% merge) — CONTRIBUTING only accepts official sources; a third-party SDK is out of scope. Fork created then deleted.

## Directory submissions (8, all pending curation)
| Directory | Submitted | Status | Check |
|-----------|-----------|--------|-------|
| x402info.com/ecosystem | Sep 16 | Pending curation | Sep 18 |
| bestaiagents.org | Sep 15 | Pending | Sep 18 |
| theagentrank.com | Sep 15 | Pending | Sep 18 |
| agents.net/directory | Sep 15 | Pending | Sep 18 |
| aiagentcensus.com | Sep 16 | Pending | Sep 18 |
| MeshKore | Sep 16 | Pending | Sep 18 |
| SwarmBazaar | Sep 17 | Pending curation | Sep 18 |
| AiAgents.Directory | Sep 16 | Pending | Sep 18 |

## Newsletters
| Date | Status | Reason |
|------|--------|--------|
| 2026-09-15 | unpublished | OpenRouter 402 Payment Required |
| 2026-09-16 | published | Successful |
| 2026-09-17 | unpublished | Verifier rejected factual accuracy (tests passed=None, skills overclaimed) |

## Blockers
1. REQ1 - PyPI OIDC publisher (one-page visit by customer)
2. REQ2 - GH PR scope token (grant public_repo)
3. Directory curation time (earliest Sep 18 at 72h)
4. Newsletter 09-17 verifier accuracy (needs better journal test data)
5. No new keyless distribution targets remain

## Next actions
- Sep 18: bulk directory re-check (72h+ submissions)
- Sep 18: nightly crawler runs at 8am
- Sep 22: weekly X post slot
- When req1 arrives: publish to PyPI
- When req2 arrives: open all 17 PRs
## 2026-09-18 21:58 UTC — Distribution check

**State:** Distribution-first run. All corrective actions reviewed.

**Surfaces checked:**
- GitHub repos (openai-agents-nano-x402, nano-mcp-public): 200 signed-out
- PyPI: NOT live (/pypi/json + /simple/ both 404) — req1 still pending
- Release v0.1.0: wheel 42 dl, sdist 7 dl (up from 32/6)

**Directory re-checks (72h+):**
- agents.net/directory: 47 agents listed, ours NOT visible — still pending
- x402info.com/ecosystem: 14 featured projects, ours not shown — still pending
- bestaiagents.org: landing-only page, no browseable listing
- theagentrank.com: 160 agents, ours not visible
- All 8+ pending — human curated, ~3-7 day cycles

**New surfaces evaluated (all skipped):**
- AgentBoard (natearcher-ai/agentboard): DEV challenge project, 15 static agents — skip
- Agent Directory API: 404 (domain changed) — skip
- curlship.io: DNS fails — skip

**PR fork drift (15 repos):** 4 clean / 11 ahead-by-1 (our commits unmerged) — expected while req2 pending
- x402-foundation/x402 forks: 1,240+ behind upstream (active repo, expected)
- All branches still saveable; no merge conflicts detected
- Only req2 unblocks the PRs

**Tests run (journal data for newsletter):**
- openai-agents-nano-x402: 9 passed
- nano-mcp-public: 129 passed

**Blockers:** req1 (PyPI key) and req2 (GH PR scope) both still open. No new grants.

**Next:** Sep 22 weekly X post slot; newsletter cron; when req1/2 land, publish PyPI + open 18 PRs.
