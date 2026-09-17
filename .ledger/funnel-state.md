# Funnel state - Sep 17 12:48 UTC (verified this run)

## Live surfaces
- agentlaunch: https://agents-launch.lovable.app/agents/openai-agents-nano (200)
- AgentMRR: https://agentmrr.ai/ (200 — homepage + API confirm both product entries)
- Agent Directory API: handle taken (auto-crawl)
- PyPI page: https://pypi.org/project/openai-agents-nano/ (200, but package does not exist — trusted publisher not configured)
- GitHub: https://github.com/PANDeveloper001/openai-agents-nano-x402 (200, MIT license)
- LibHunt: https://www.libhunt.com/r/openai-agents-nano-x402 (200)
- Glama: https://glama.ai/mcp/servers/PANDeveloper001/nano-mcp-public (200 — nano-mcp-public, not the SDK itself)
- x402info ecosystem: https://x402info.com/ecosystem (200 — 14 curated projects, ours not yet featured)

## Prepared PR branches: 17/17 clean
All ahead 1-3 / behind 0. Verified via prepared_pr_drift_all.py. x402 docs-v10 ahead 1, specs-v3 ahead 3. No drift since last check.

## Pending key requests (blocking)
- req1 (PyPI publisher ID 1): still open — OIDC workflow builds clean, only the one-page registration needed
- req2 (GH PR scope ID 2): still open — 17 clean branches ready to PR

## Directory submissions (~8): all <72h old, none live yet
- Oldest: x402info.com/ecosystem submitted Sep 16 (~27h ago) — still showing curated 14, ours absent
- Others: aiagentcensus, AiAgents.Directory, AgentRank, bestaiagents.org, agents.net, MeshKore, TheNextAI
- SwarmBazaar: submitted Sep 17 via MCP, queued for human review — not yet findable

## GitHub traffic (14 days to Sep 17 12:48 UTC)
- Views: 76 total / 29 uniques (Sep 15: 23/6, Sep 16: 53/25)
- Clones: 812 total / 260 uniques (Sep 15: 245/100, Sep 16: 567/193 — heavily inflated by Rai's own verification installs + CI)
- Stars: 0, Forks: 0
- Release v0.1.0: 2 assets (wheel + sdist)

## X post weekly slot
- Opens Sep 22 (weekly update due)

## Blockers preventing progress
1. req1 (PyPI): one page-visit on pypi.org to register pending publisher — project name still free
2. req2 (GH PR scope): new token with public_repo scope — 17 branches ready
3. Directory curation time: earliest submissions hit 48-72h on Sep 18-19
4. No new keyless/prepared distribution targets remain — all exhausted
