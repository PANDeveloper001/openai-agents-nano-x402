# Distribution funnel — 2026-09-18 02:30 UTC

## This run (Sep 18, ~02:20-02:35)

### AgentMRR re-registered
- Product removed again between runs (periodic cleanup)
- Re-registered successfully: agent ID a0128e14, product ID 8ff6fa22-befe-40bd-b019-f3167db697a0
- Homepage shows 57 products (down from 67 — broader cleanup)
- Our product not yet on homepage top rankings (normal for new registration)
- Already logged as listing_submitted (duplicate blocked by tool)

### Directory re-check
All 9-10 pending directories still NOT live:
- agents.net/directory: 47 agents listed, ours absent (submitted Sep 15, 3 days)
- bestaiagents.org: absent (submitted Sep 15)
- theagentrank.com: absent (submitted Sep 15)
- x402info.com/ecosystem: 14-featured unchanged, ours absent (submitted Sep 16, 2 days)
- aiagentcensus.com: landing only, no directory view (submitted Sep 17, 1 day)
- aiagentslist.io: in 48h editorial window (submitted Sep 17)
- swarmbazaar.ai: still pending (submitted Sep 17)
- AiAgents.Directory: absent (submitted Sep 12, 6 days)
- MeshKore: 000/unreachable (submitted Sep 17)

Key finding: 5-7 day review cycles are the norm. No directory went live yet.

### New surfaces evaluated (all not autonomously submittable)
- agentic.ai -> email-gated (mailto:hello@agentic.ai), needs account or email
- aiagenttools.dev -> form has no name attributes, likely broken; email fallback
- agentbets.ai -> keyless API but prediction-market/betting only, off-topic
- agentindexed.com/submit -> still mailto fallback (verified browser-side: "Your email client opened...")
- FallMarket -> auto-imports from specific GitHub org, not our account

### No new keyless/autonomous surfaces found
All remaining directory options require email-send or account creation.

### PR branches: 19/20 clean (unchanged)
All waiting on req2 (GH public_repo token scope)

### Traffic (14-day, no change since last check)
- Views: 76 total, 29 uniques
- Clones: 812 total, 260 uniques
- Referrers: t.co 58, github.com 3 (all own traffic, no organic)

### Blockers (unchanged)
1. req1 (PyPI): customer one-page publisher registration — still open
2. req2 (GH PR scope): customer approval for public_repo token — still open
3. Directory curation time: earliest Sep 15 submissions at 72h+

### Next actions
- Sep 20-22: bulk directory re-check (some dirs will be 5-7d+)
- Sep 22: weekly X post slot (link to GitHub Pages status page)
- When req1 arrives: publish to PyPI
- When req2 arrives: open 19 PRs across all MERGES targets