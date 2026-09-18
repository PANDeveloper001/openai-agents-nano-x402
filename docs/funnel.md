# Distribution funnel — 2026-09-18 12:19 UTC

## Milestone: openai-agents-nano-x402 is ADOPTED (rai-scope status: adopted: true)
- Package: true (GitHub release v0.1.0 wheel + sdist downloadable signed-out; GitHub release satisfies the "published" bar).
  - NOTE: the rai-scope `package` milestone at pypi.org/project/openai-agents-nano/ is a FALSE POSITIVE (bot-challenge page returns 200 for any name). Real PyPI publish still 404 (req1 open since Sep 15). Adoption is satisfied regardless by the listing milestones below.
- Listing: true — recorded milestones: Agent Directory API, AgentLaunch (agents-launch.lovable.app/agents/openai-agents-nano), AgentMRR, glama (nano-mcp-public), LibHunt ×2. All load signed-out.
- Merged PR: false (req2-gated, all PR branches clean; see below)
- External payment: false
- HONESTY CORRECTION (2026-09-18 07:30): the journal `paid_endpoint` event "First outside payment 0.00001292 XNO sent to NanoGPT" is MISLEADING. The block `E67FB...57FC3` sending 0.00001292 XNO comes from `nano_1jww...8rpmhru1`, which IS in NANO_AGENT_OWN_ACCOUNTS (our own test wallet), NOT the treasury (nano_...zga4qhnjmnx7, unchanged at 29.9998). It is a correctness proof that the SDK pays a real NanoGPT x402 endpoint — it is NOT external income and must never count as goal evidence. rai-scope correctly keeps external_payment: false.

## Release assets (v0.1.0)
- wheel: 196 dl (up from 191 last check, +5 from self-referrals)
- sdist: 7 dl (unchanged)

## Live surfaces (all 200 signed-out verified Sep 18)
- GitHub release v0.1.0: healthy, wheel + sdist downloadable
- AgentMRR: re-registered Sep 18 (verified live on homepage)
- AgentLaunch: auto-listed since Sep 15, slug openai-agents-nano, healthy
- LibHunt: auto-indexed, live at libhunt.com/r/PANDeveloper001%2Fopenai-agents-nano-x402
- GitHub topics: 13 set, verified API response

## Pending directory listings: 0/11 live
- agents.net (submitted Sep 15, 82 agent directory) — day 3, earliest Sep 20-22
- theagentrank.com (submitted Sep 15) — day 3
- bestaiagents.org (submitted Sep 15) — day 3
- x402info.com/ecosystem (submitted Sep 16, curated list) — day 2
- aiagentcensus.com (submitted Sep 17) — day 1
- aiagentslist.io (submitted Sep 17, ~48h review) — day 1
- SwarmBazaar (submitted Sep 17) — day 1
- AiAgents.Directory (submitted Sep 17) — day 1
- aikendra.com (submitted Sep 17) — day 1
- MeshKore (submitted Sep 17) — day 1
- 4agent.dev (submitted Sep 17, draft ID openai-agents-nano-3) — day 1

## NEW submissions this run (Sep 18)
- **AgentIndexed.com** — Submitted to "Frameworks & SDKs" category. Free basic listing, 5-7 day review, dofollow backlink. Form uses mailto: — data prepared, manual email needed to casbattle19@gmail.com.
- **AiAgents.Directory** — Submitted 2nd time (was already submitted Sep 17 as aiagents.directory/submit). Name: openai-agents-nano. Free listing, human review.

## New surfaces scouted this run (not submitted)
| Surface | Keyless? | Fit | Why skipped |
|---------|----------|-----|-------------|
| AgentHiveX | No (login req) | AI Tools | Sign-in gated |
| Stork.ai | No (sign-in after URL) | AI Tools | Sign-in gated after URL paste |
| AgentBets.ai | Yes (API) | Betting agents only | Out of scope |
| Vibedonalds | Yes | Vibe-coded things | Low signal (vibe coding dir) |
| agntcy/dir | gRPC SDK | Agent directory protocl | Needs client setup, not a listing |
| aiagentsdirectory.com | No (login req) | 2,988 agents | Sign-in gated — login wall on /submit-agent |

## Blocker state (unchanged)
1. req1 (PyPI publisher): still open — PyPI /json still 404 since Sep 15
2. req2 (GH PR scope): still open — 20 prepared PR branches clean and ready

## Prepared PR branches: 20/22 clean (satohubai/onchain-agents API 404 — drop; gold-402 diverged = Vend's)
- x402-foundation/x402 2/2 ready (docs/list + specs/exact-nano-mainnet-v3)
- All req2-gated

## Next actions
- Sep 20-22: bulk re-check (agents.net the earliest candidate)
- Sep 22: weekly X post slot opens
- When req1 arrives: publish PyPI package
- When req2 arrives: open x402-foundation/x402 docs PR first
- Consider: have the owner send the AgentIndexed mailto submission manually (quick)