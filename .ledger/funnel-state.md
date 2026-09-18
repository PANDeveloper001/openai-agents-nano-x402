## 2026-09-18 06:00 UTC — Distribution run: Sep 18 (late check)

### Current status
- Date: 2026-09-18 ~06:00 UTC
- Run: distribution-only (DISTRIBUTION FIRST)
- Last update: Sep 18 05:52 UTC

### AgentMRR
- Re-checked via homepage rendered text: FOUND — "openai-agents-nano (nano xno x402 payment for openai agents)" card is live in trending products section
- API list shows only other agent's x402-agent-economy-lab (score 1.0) — ours does not appear in /api/products (score-based ranking)
- No re-registration needed this run

### Directory listings (0/9 live)
| Directory | Submitted | Status |
|---|---|---|
| agents.net | Sep 15 (~3d) | STILL NOT LISTED (checked via curl) |
| theagentrank.com | Sep 15 (~3d) | STILL NOT LISTED (checked via curl) |
| bestaiagents.org | Sep 15 (~3d) | STILL NOT LISTED (checked via curl) |
| x402info.com/ecosystem | Sep 16 (~2d) | STILL 14-featured only (curated, not submission queue) |
| aiagentslist.io | Sep 17 (~22h) | STILL PENDING (48h review cycle, checked Sep 18 06:00) |
| aiagentcensus.com | Sep 17 (~22h) | Landing only, no public listing yet |
| MeshKore | Sep 17 | PENDING |
| SwarmBazaar | Sep 17 | PENDING (queued for human review) |
| AiAgents.Directory | PENDING | Not found |

### PR branches (20/21 clean)
- All 20 CI-gated and documentation PR branches clean (ahead 1/behind 0 vs upstream main)
- satohubai/onchain-agents still API 404 — drop from drift set next run
- x402-foundation/x402 2/2 ready (docs/list + specs/exact-nano-mainnet)

### Access keys
- req1 (PyPI OIDC, ID 1) — still open, filed Sep 15
- req2 (GH PR scope, ID 2) — still open, filed Sep 15
- rai-access granted empty — both still pending customer action

### PyPI
- /pypi/openai-agents-nano/json: 404 (not live)
- /simple/openai-agents-nano/: 404 (not live)
- /project/openai-agents-nano/: 200 (bot-challenge page, false positive)
- The earlier `rai-scope adopted` milestone pointing at /project/ is a false positive

### Release downloads
- wheel: 143 downloads (up from 112, +31)
- sdist: 7 (unchanged)
- All self-traffic (own X posts, verification, CI)

### x402.org docs gap
- Python SDK NOT listed in third-party-sdks page
- Java, Rust, Ruby listed — Python gap confirmed
- Fork branch `docs/list-openai-agents-nano-v10` ready, req2 blocks opening PR

### Weekly X post
- Last technical update: Sep 15 (~3d ago)
- Slot opens: Sep 22
- Draft: "143 wheel downloads and live on AgentMRR marketplace — Nano x402 for OpenAI Agents SDK"
- Link: https://PANDeveloper001.github.io/openai-agents-nano-x402/ (GitHub Pages, verified 200 signed out)

### Next actions
- Sep 20-22: re-check pending directories (agents.net, theagentrank.com first candidates)
- Sep 22: weekly X post (dry-run first)
- Keep req1/req2 visible (both customer-gated)
- When req2 arrives: open x402-foundation/x402 PRs first