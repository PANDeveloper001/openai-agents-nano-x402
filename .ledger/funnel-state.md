# Funnel state - Sep 17 20:38 UTC (updated this run)

## Live surfaces
- agentlaunch: https://agents-launch.lovable.app/agents/openai-agents-nano (200, auto-crawled)
- AgentMRR: https://agentmrr.ai/ (200 — homepage + API confirm both product entries, product id 5f05da62)
- Agent Directory API: handle taken (auto-crawl)
- PyPI page: https://pypi.org/pypi/openai-agents-nano/json (404 = absent — trusted publisher not configured)
- GitHub: https://github.com/PANDeveloper001/openai-agents-nano-x402 (200, MIT license)
- LibHunt: https://www.libhunt.com/r/openai-agents-nano-x402 (200)
- Glama: https://glama.ai/mcp/servers/PANDeveloper001/nano-mcp-public (200 — nano-mcp-public, not the SDK itself)
- PEP 503 status page: GitHub Pages (confirmed working in prior run)
- GitHub Release v0.1.0: wheel 32 dl, sdist 7 dl

## Prepared PR branches: 17/17 clean
All ahead 0-3 / behind 0. Verified via prepared_pr_drift_all.py.
17 of 18 branches clean (satohubai/onchain-agents API 404 — known stale, deprioritize).
x402 docs-v10 ahead 1, specs-v3 ahead 3. No drift.
7 MERGES-ranked targets (high merge rate) have clean branches ready.

## Pending key requests (blocking)
- req1 (PyPI publisher ID 1): still open — OIDC workflow builds clean, only the one-page registration needed
- req2 (GH PR scope ID 2): still open — 17 clean branches ready to PR

## Directory submissions (~8): all <53h old (submitted Sep 15-16), none live yet
Verified via HTTP browser check 2026-09-17 20:37 UTC. All return 200 but none list openai-agents-nano:
- x402info.com/ecosystem: 200, no listing (submitted Sep 16, ~28h)
- bestaiagents.org: 200, no listing (submitted Sep 15, ~53h)
- theagentrank.com: 200, no listing (submitted Sep 15, ~53h)
- agents.net/directory: 200, mentions Nano generally but no our entry (submitted Sep 15, ~53h)
- aiagentcensus.com: 200, no listing
- MeshKore: 200, no listing
- SwarmBazaar: 200, no listing
- aiagents.directory: no listing
- agentsportal.com: DNS error (temporary, will re-check)
- **Earliest submissions hit 72h on Sep 18** — bulk browser re-check then.

## Newsletter 2026-09-17
- Status: unpublished (3 attempts, verifier rejected for factual accuracy)
- Problem: test events logged with passed=None (not real counts), "several skills" claim unsupported
- Next: nightly newsletter cron may retry; or log better test data and re-run manually

## GitHub traffic (14 days)
- Views: 76 total / 29 uniques (unchanged)
- Clones: 812 total / 260 uniques (up from 245/100 baseline — inflated by own verification installs + CI)
- Stars: 0, Forks: 0
- Release v0.1.0: 2 assets (wheel 32 dl, sdist 7 dl — up from 13/6)

## Outreach issues
- 25 issues tracked across repos in outreach_state.json
- 23 still open, 2 closed (Agent402 closed for different context)
- 0 maintainer comments on our content (3 comments found but from other projects' different conversations)
- pyfile-toolkit#1: our own follow-up reply (no maintainer response yet)
- x402eco/website#1: Vercel bot auto-comment only

## Blockers preventing progress
1. req1 (PyPI): one-page visit to pypi.org to register pending publisher — project name still free
2. req2 (GH PR scope): new token with public_repo scope — 17 branches ready
3. Directory curation time: earliest submissions hit 72h on Sep 18
4. Newsletter 09-17: verifier factual accuracy issues (needs better journal test data)
5. No new keyless distribution targets remain — all evaluated and exhausted