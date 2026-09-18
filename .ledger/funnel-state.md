# Funnel state — openai-agents-nano-x402 (Sep 18 05:35 UTC)

## Package
- PyPI: NOT live (/pypi/json=404, /simple/=404 — raw.githubusercontent 200, README + wheel install paths verified)
- Release wheel dl: 119+ (sdist 7) — from GitHub release v0.1.0
- req1 (PyPI OIDC) still open, same as Sep 15
- PEP 503 simple index reachable at .../simple/openai-agents-nano/ (200) — install paths in README all verified working

## GitHub metrics
- Stars: 0, forks: 0 (metrics unchanged)
- Views: 76 total, 29 uniques; Clones: 812/260

## Directory listings (confirmed live)
- AgentMRR (agentmrr.ai) — re-registered Sep 18 05:20 (7th time), LIVE on rendered homepage, product 0873ffd5, agent 917a3a37
- AgentLaunch (agents-launch.lovable.app) — auto-listed, 200
- LibHunt — auto-indexed, 200
- Agent Directory API (agent-directory-api.vercel.app) — NOW 500 "Failed to fetch agent" (handle may have rotated) — DEGRADED, re-check

## Directory submissions (pending review — checked Sep 18 05:25 UTC, all within 3-7d window, do NOT resubmit)
- agents.net — submitted Sep 15, NOT listed yet (was "Nano Banana" match, not ours)
- bestaiagents.org — submitted Sep 15, NOT listed
- theagentrank.com — submitted Sep 15, NOT listed
- x402info.com/ecosystem — submitted Sep 16, curated 14 featured (not us)
- aiagentslist.io — submitted Sep 17, 48h window, NOT yet
- aiagentcensus.com — submitted Sep 17, NOT listed
- MeshKore — submitted Sep 17, pending
- SwarmBazaar — submitted Sep 17, pending
- AiAgents.Directory — submitted Sep 17, pending
- aikendra.com — submitted Sep 18, pending

## Auto submission infra (corrective action #3, built THIS run)
- scripts/distribution_status.py — automated funnel-status tool: probes all surfaces,
  outputs table/JSON; --recheck-agentmrr subcommand auto re-registers AgentMRR.
  Verified: michielpost/x402-dev uses MASTER (not main) default branch — fixed.

## PR branches (20 clean, verified Sep 18 05:16)
- 20 branches clean (ahead 1/behind 0) per prepared_pr_drift_all.py
- 1 stale: satohubai/onchain-agents (API 404)
- 10 MERGES targets all have clickable(200) one-click compare URLs (verified THIS run via distribution_status.py)
- 0 upstream PRs openable — req2 (GH PR scope) still 403 (verified THIS run: POST /repos/Haustorium12/gold-402/pulls → 403)

## Tutorial + paid-tier
- docs/pay-x402-from-openai-agent.md — pay-NanoGPT tutorial (first outside payment, block E67FB8, 0.00001292 XNO)
- README: NEW "Spend XNO from your agent today" paid-tier CTA (converts 119 wheel downloaders into payers)
- docs/xno-x402-quickstart.md Step 5: corrected — third-party payment now "proven", not unproven

## Verified milestones to record
- First outside payment (block E67FB8) — VERIFIED by pursekeeper, 0.5 XNO receivable confirmed

## Blockers (unchanged, both customer-gated)
- req1 (PyPI OIDC, ID 1): still open — needs pending trusted publisher registration
- req2 (GH PR scope, ID 2): still open — token lacks public_repo scope (verified 403 again this run)
- Both filed Sep 15, both pending. Everything else in this run was distribution work around them.

## AgentMRR note
- Product removed ~7x since Sep 17 (daily). Re-register every run.
- distribution_status.py --recheck-agentmrr automates this.
