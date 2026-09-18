## 2026-09-18 08:04 UTC — Distribution run: Sep 18 (morning check)

### Current status
- Date: 2026-09-18 ~08:04 UTC
- Run: distribution-only (DISTRIBUTION FIRST)
- Last funnel update: Sep 18 07:55 UTC
- This run: directory re-check, traffic measurement, new surface scan

### AgentMRR
- Re-checked homepage rendered text (via curl + browser): FOUND
  - Product card "openai-agents-nano (Nano XNO x402 payment for OpenAI Agents)" is live
  - API /products list does NOT show it (score 1.0, vote-ranked, normal)
  - 92 products total (up from 57?) - broader catalog growth
- No re-registration needed this run

### Directory re-check (browser-verified, 0/9 live)
| Directory | Submitted | Days | Status |
|---|---|---|---|
| AiAgents.Directory | Sep 12 | 6 | NOT listed (browser verified) |
| agents.net/directory | Sep 15 | 3 | NOT listed (browser verified: 82 agents, ours absent) |
| theagentrank.com | Sep 15 | 3 | NOT listed (browser verified: "160 agents listed" page) |
| bestaiagents.org | Sep 15 | 3 | NOT listed (browser verified) |
| x402info.com/ecosystem | Sep 16 | 2 | NOT listed (14-featured curated only, our entry in queue) |
| aiagentcensus.com | Sep 17 | 1 | NOT listed (landing page only) |
| aiagentslist.io | Sep 17 | 1 | NOT listed (69 agents page, 48h review window - check Sep 19+) |
| MeshKore | Sep 17 | 1 | NOT listed |
| SwarmBazaar | Sep 17 | 1 | PENDING |

Confirmed: 5-7 day review cycles are the norm. First candidates expected ~Sep 20-22.

### New surfaces evaluated this run (all not submittable)
- **aiagentsdirectory.com** (/submit-agent, 3k+ agents) — requires sign-in/account to submit. NOT keyless.
- **x402.eco** — deployment PAUSED ("Deployment Paused" page). Cannot submit.
- **x402nano.org** — x402 facilitator for Nano (existing tool, relevant), site is also paused.
- No new keyless agent-payments or x402 SDK directories found.

### Release downloads
- wheel: 164 (unchanged from Sep 18 07:55)
- sdist: 7 (unchanged)
- No organic growth detected between runs (all self-traffic)

### Traffic (GitHub 14-day)
- GitHub traffic API returned 0/0 (traffic data reset or expired beyond 14-day window)
- Last recorded: 76 views / 29 uniques, 812 clones / 260 uniques (earlier this run cycle)

### Access keys (unchanged)
- req1 (PyPI, ID 1) — still open
- req2 (GH PR scope, ID 2) — still open

### PR branches
- Last known: 20/22 clean, x402-foundation/x402 2/2 ready
- Both x402 PRs (docs + specs) highest-value when req2 arrives

### Next actions
- Sep 19-20: re-check aiagentslist.io (48h window)
- Sep 20-22: bulk directory re-check (5-7 day candidates: agents.net, theagentrank.com, bestaiagents.org)
- Sep 22: weekly X post slot (draft: "164+ wheel downloads | AgentMRR | Nano x402 for OpenAI Agents SDK")
- Keep req1/req2 visible (both still pending customer action)