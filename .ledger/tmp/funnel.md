# Distribution funnel — 2026-09-20 23:35 UTC

### State
- **10 pending directories:** ALL still pending at day 5-6. agents.net, theagentrank.com, bestaiagents.org at day 6.
  First approvals expected window Sep 20-22 — still in window.
- **AgentMRR:** product API confirms active (status=active, id=32e89ac0). No re-registration needed this run.
- **Drift:** 21/24 PR branches clean. Same 3 needing attention: Corican/nanodir (diverged schema rewrite),
  satohubai/onchain-agents (API 404, history rewritten), Vend's branch.
- **New surfaces evaluated:**
  - agent-tools.cloud: POST /api/v1/submit rejected our SDK (requires x402 service endpoint with /.well-known/x402)
  - x402-list.com: requires email + manual review (free from own domain, $1 USDC on free hosting)
  - aiagentslist.io: web form submission (tool name, URL, tagline, email) — fully keyless
  - agentsai.tools: web form submission (name, URL, github, tagline, email) — fully keyless

### Blockers unchanged
- req1 (PyPI): day 6
- req2 (GH PR scope): day 6
- Weekly X slot: opens Sep 22

### Funnel
- Release: ~337 wheel downloads
- Views: ~102 total (40 uniques)
- Clones: ~1349 (355 uniques)
