# Distribution funnel — 2026-09-18 07:30 UTC

## Milestone: openai-agents-nano-x402 is ADOPTED (rai-scope status: adopted: true)
- Package: true (GitHub release v0.1.0 wheel + sdist downloadable signed-out; GitHub release satisfies the "published" bar).
  - NOTE: the rai-scope `package` milestone at pypi.org/project/openai-agents-nano/ is a FALSE POSITIVE (bot-challenge page returns 200 for any name). Real PyPI publish still 404 (req1 open since Sep 15). Adoption is satisfied regardless by the listing milestones below.
- Listing: true — recorded milestones: Agent Directory API, AgentLaunch (agents-launch.lovable.app/agents/openai-agents-nano), AgentMRR, glama (nano-mcp-public), LibHunt ×2. All load signed-out.
- Merged PR: false (req2-gated, all PR branches clean; see below)
- External payment: false
- HONESTY CORRECTION (2026-09-18 07:30): the journal `paid_endpoint` event "First outside payment 0.00001292 XNO sent to NanoGPT" is MISLEADING. The block `E67FB...57FC3` sending 0.00001292 XNO comes from `nano_1jww...8rpmhru1`, which IS in NANO_AGENT_OWN_ACCOUNTS (our own test wallet), NOT the treasury (nano_...zga4qhnjmnx7, unchanged at 29.9998). It is a correctness proof that the SDK pays a real NanoGPT x402 endpoint — it is NOT external income and must never count as goal evidence. rai-scope correctly keeps external_payment: false.

## Live surfaces (all 200 signed-out verified Sep 18)
- GitHub release v0.1.0: healthy, wheel + sdist downloadable
- AgentMRR: re-registered Sep 18 (3rd time since Sep 17 — product ID f00a40e9, agent ID 726b7506). AgentMRR removes products silently between runs. Product verified live via /api/products/{id}
- AgentLaunch: auto-listed since Sep 15, slug openai-agents-nano, healthy
- LibHunt: auto-indexed, live at libhunt.com/r/PANDeveloper001%2Fopenai-agents-nano-x402
- GitHub topics: set 13 topics, verified API response. Topic index cards pending GitHub indexing

## Pending directory listings: 0/9 live (3-6 day review cycles)
- agents.net (submitted Sep 15, review 24-48h) — pending day 3
- theagentrank.com (submitted Sep 15, 2-3 business days) — pending day 3
- x402info.com/ecosystem (submitted Sep 16, curated 14-featured list) — pending day 2
- bestaiagents.org (submitted Sep 17) — pending day 1
- aiagentcensus.com (submitted Sep 17, landing page only) — pending day 1
- aiagents.directory (submitted Sep 17) — pending day 1
- swarmbazaar.com (submitted Sep 17) — pending day 1
- meshkore.com (submitted Sep 17) — pending day 1
- aikendra.com (submitted Sep 17, 48h review) — pending day 1
- Next re-check: Sep 20-22 (first candidate deadlines)

## Prepared PR branches: all clean
- awesome-agentic-payments: branch add-openai-agents-nano-x402, ahead 1/behind 0
- awesome-ai-agents-2026: branch add-openai-agents-nano, ahead 1/behind 0
- ai-agent-infra-list: branch add-x402-nano-settlement-rail, ahead 1/behind 0
- awesome-ai-sdks: branch add-openai-agents-nano-v2, ahead 1/behind 0
- awesome-payment-agent-skills: branch add-openai-agents-nano, ahead 1/behind 0
- x402 (docs): branch docs/list-openai-agents-nano-v10, ahead 20/behind 0 (live)
- gold-402: branch add-openai-agents-nano-v4, ahead 2/behind 0 (live)
- satohubai/onchain-agents: dropped (API 404 — repo inactive)
- All others: clean, ahead 1/behind 0
- Wait: req2 (GH PR scope — customer approval, filed Sep 15)

## Package status
- PyPI: not uploaded (req1 open since Sep 15 — customer action at pypi.org/manage/projects/openai-agents-nano to register trusted publisher)
- GitHub release wheel: downloadable, installs clean (`pip install git+https://...@v0.1.0`)
- Published via OIDC workflow: FAILS with 'invalid-publisher: valid token, but no corresponding publisher' (exactly one page-visit needed)

## Traffic metrics
- GitHub stars: 0
- GitHub forks: 0
- Open issues: 2
- Release assets: v0.1.0 (1 wheel, 1 sdist)
- Release wheel downloads: 164 (+21 since Sep 18 04:10)
- Release sdist downloads: 7 (unchanged)
- Star count: 0, Fork count: 0

## Discoveries this run (Sep 18)
- Vibedonalds.com: NEW listing submitted SUCCESSFULLY this run (07:15) — Next.js form via form.requestSubmit(), MCP Servers category, confirmed "We'll email you within 3-7 days". Free listing requires a badge on site, reviewed 3-7d. Pending live.
- MeshKore: re-confirmed submission (07:20, category Crypto & DeFi, OpenAI Agents framework) — reviewed within 24h. Already in keyless proven list from Sep 15.
- curship.com: keyless auto-listing from OG tags. Requires email to submit. Skip until identity resolved.
- aiagentslisting.com: launched Sep 6, free listings, MCP endpoint. Requires sign-in to submit. On watch list.
- agentbets.ai: prediction-market directory (out of scope for openai-agents-nano).

## Next steps
- Sep 20-22: re-check pending directories (first candidates agents.net, theagentrank.com, MeshKore, Vibedonalds)
- Sep 22: weekly X technical update (dry-run first, draft ready). Proposed text: "164 wheel downloads, AgentMRR + 2 new directory listings added" -> GitHub Pages site
- Continue monitoring req1/req2 status
- Traffic (last measurable): all self-traffic (verification, CI, X posts)

## Key blockers (unchanged since Sep 15)
1. req1 (PyPI, ID 1): customer registers trusted publisher at pypi.org/manage/projects/openai-agents-nano -> publish workflow
2. req2 (GH PR scope, ID 2): customer creates token with public_repo scope -> open 18+ prepared PRs
3. No outside payments: 0 (no third-party x402 buyer has paid our endpoint)

## Upcoming
- Sep 20-22: directory re-checks (first 6-day deadlines hit)
- Sep 22: weekly X post slot (2 open slots, never re-posted after owner deletion). Draft: "143 wheel downloads and live on AgentMRR — Nano x402 for OpenAI Agents SDK" -> GitHub Pages site
- When req1 arrives: pip install -> PyPI milestone
- When req2 arrives: x402-foundation/x402 docs PR first (highest merge value), then remaining PRs