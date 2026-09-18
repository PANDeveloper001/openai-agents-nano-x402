# openai-agents-nano-x402 funnel (2026-09-18 23:08 UTC)

## Package
- GitHub release downloads: **337 total** (wheel 330 +12 from 318, sdist 7 — flat, Sep 19 22:30 check)
- PyPI: /pypi/openai-agents-nano/json -> 404 (NOT live — req1 still open on day 5)
- pip install path: git+https://github.com/PANDeveloper001/openai-agents-nano-x402@v0.1.0
- Wheel + sdist built and ready in dist/ (last build Sep 18)

## Live surfaces (verified Sep 19 22:30)
- [LIVE] **nanodirectory.info** — directory.json still carries us (2 mentions in restructured schema, verified Sep 19 22:30 via browser). UI rebuild in progress; card will reappear when their front-end catches up.
- [LIVE] **AgentMRR (agentmrr.ai)** — RE-REGISTERED Sep 19 22:27 (product had expired from carousel; API mentions dropped to 0). New product id 32e89ac0-6ead-41cc-896d-95596af50608 confirmed live via GET /api/products/{id}. Homepage rendered 48 mentions of openai-agents-nano (carousel rotation).
- [LIVE] **agents-launch.lovable.app** — auto-indexed
- [LIVE] **libhunt.com** — auto-indexed
- [LIVE] **GitHub topics** — 12 topics set, repo appears on /topics/xno (page 3)
- **3 ready PR branches still not open** (x402-foundation/x402 docs + mpp-best/awesome_mpp + ai-agent-marketplace) — req2-gated

## Directories (re-checked Sep 19 22:30, all 10 still pending)
All 10 pending directories still NOT listing us (browser-verified JS-rendered content):
- agents.net (submitted Sep 15, day 5): NOT listed (95 agents/26 categories, no openai-agents-nano)
- theagentrank.com (submitted Sep 15, day 5): NOT listed (160 agents, verified reviews)
- bestaiagents.org (submitted Sep 15, day 5): NOT listed (homepage cards, SEObot etc)
- x402info.com/ecosystem (submitted Sep 16, day 4): NOT listed (14 featured, not our entry)
- aiagentcensus.com (submitted Sep 17, day 3): NOT listed
- AiAgents.Directory (submitted Sep 18, day 2): NOT listed (browse 404s for us)
- MeshKore (submitted Sep 18, day 2): NOT listed (100k+ indexed, not curated yet)
- SwarmBazaar (submitted Sep 17): NOT listed
- AIKendra (submitted): NOT listed (1933 tools, no mention)
- 4agent.dev (submitted 5x): NOT listed (172 tools)

Expected: human-curated dirs take 5-7 days. Sep 15 submissions hit day 5-6 now; first approvals expected Sep 20-22.

## PR Branch drift (Sep 19 22:30, prepared_pr_drift_all.py)
20 clean, 4 needing attention:
- Corican/nanodir add-openai-agents-nano-clean: diverged (behind 4, upstream schema rewrite) — leave until schema stabilizes
- assafbar2/agentswitchboard.dev add-openai-agents-nano-v3: diverged (behind 4) — needs rebuild on current upstream
- Haustorium12/gold-402 add-vend-api-merchant: diverged (behind 1) — VEND's branch, not ours, leave
- satohubai/onchain-agents add-openai-agents-nano: API 404 (history rewritten by maintainer) — known

## GitHub traffic (14-day, as of Sep 19)
- Views: 102 total, 40 unique (flat; no new organic referrers)
- Clones: 1,349 total, 355 unique (inflated by CI + our verification installs)
- Release: 337 downloads (wheel 330, sdist 7) — organic crawl/UX growth ~+12/day

## New surface evaluation (Sep 19)
- s-a-m-a-i/awesome-x402: 0★, 0 closed PRs, QUIET/DEAD — skip
- michielhdoteth/awesome-ai-agent-tools: 23★ but zero x402/payment/nano mentions; general agent components directory, no payments section — NOT a fit for a payments SDK
- submitaitools/Free-AI-Directories: mining list, no new keyless agent-tool dirs that accept SDKs and aren't already submitted

## Blockers (unchanged)
- req1 (PyPI token, filed Sep 15): still open — customer action needed (day 5)
- req2 (GH PR scope, filed Sep 15): still open — customer action needed (day 5)
- Weekly X post slot: opens Sep 22 (last technical update Sep 15)
- mpp.best web form: requires Google OAuth (not keyless) — PR route only, req2-gated

## Next actions
- Sep 20-22: re-check 5-6 day directories (agents.net, theagentrank.com, bestaiagents.org first approvals expected)
- Sep 20+: drift re-check; rebuild agentswitchboard branch on current upstream
- Sep 22: weekly X post when slot opens
- When req2 arrives: x402-foundation/x402 docs PR first (strongest MERGES target), then mpp-best/awesome_mpp, then ai-agent-marketplace
- When req1 arrives: publish to PyPI (uv build + publish + verify)
- Per-run: AgentMRR re-registration check (expires), drift check, directory re-checks
