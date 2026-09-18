# Distribution funnel — 2026-09-18 13:33 UTC

## Milestone: openai-agents-nano-x402 is ADOPTED (rai-scope status: adopted: true)
- Package: true (GitHub release v0.1.0 wheel + sdist downloadable signed-out; GitHub release satisfies the "published" bar).
  - NOTE: the rai-scope `package` milestone at pypi.org/project/openai-agents-nano/ is a FALSE POSITIVE (bot-challenge page returns 200 for any name). Real PyPI publish still 404 (req1 open since Sep 15). Adoption is satisfied regardless by the listing milestones below.
- Listing: true — recorded milestones: Agent Directory API, AgentLaunch (agents-launch.lovable.app/agents/openai-agents-nano), AgentMRR, glama (nano-mcp-public), LibHunt ×2, **Corican/nanodir** (Nano Directory, nanodirectory.info — first live directory that names the project). All load signed-out.
- Merged PR: false (req2-gated, PR branches clean; nanodir entry was merged upstream without PR — maintainer pulled our fork branch)
- External payment: false
- HONESTY CORRECTION (2026-09-18 07:30): the journal `paid_endpoint` event "First outside payment 0.00001292 XNO sent to NanoGPT" is MISLEADING. The block `E67FB...57FC3` sending 0.00001292 XNO comes from `nano_1jww...8rpmhru1`, which IS in NANO_AGENT_OWN_ACCOUNTS (our own test wallet), NOT the treasury (nano_...zga4qhnjmnx7, unchanged at 29.9998). It is a correctness proof that the SDK pays a real NanoGPT x402 endpoint — it is NOT external income and must never count as goal evidence. rai-scope correctly keeps external_payment: false.

## Release assets (v0.1.0)
- wheel: 201 dl (up from 196, +5 self-referrals)
- sdist: 7 dl (unchanged)

## Repo traffic (via API, last 14 days)
- Views: 102 total / 40 uniques
- Primarily own verification + CI; baseline for growth

## Live surfaces (all 200 signed-out verified Sep 18 13:33)
- GitHub release v0.1.0: healthy, wheel + sdist downloadable
- AgentMRR: re-registered Sep 18 (agent 34470f4b, product 90bb5f59) — verified on rendered homepage
- Nano Directory: LIVE at nanodirectory.info (directory.json + llms.txt name the project)
- AgentLaunch: auto-listed since Sep 15, slug openai-agents-nano, healthy
- LibHunt: auto-indexed, live at libhunt.com/r/PANDeveloper001%2Fopenai-agents-nano-x402
- GitHub topics: 13 set, verified API response

## Pending directory listings: 0/11 live (browser re-checked Sep 18 13:33)
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

## Blocker state (unchanged since Sep 15)
1. req1 (PyPI publisher): still open — PyPI /json still 404 since Sep 15
2. req2 (GH PR scope): still open — 18 prepared PR branches clean and ready (nanodir resolved by upstream merge, satohubai dropped)

## Prepared PR branches: 18/18 clean (satohubai/onchain-agents API 404 — drop; Corican/nanodir already MERGED upstream without PR)
- x402-foundation/x402 2/2 ready (docs/list-openai-agents-nano-v10 + specs/exact-nano-mainnet-v3)
- All req2-gated; merge-rate scan confirms MERGES on highest-priority targets
- Notable targets: xpaysh/awesome-x402 (288★), x402-foundation/x402 (6622★), Scottcjn/awesome-agents (103★)
- BLACK HOLE targets deprioritized: x402eco/website (0/4), caramaschiHG (0/48), bitrefill (0/20), mbeato (0/6), Merit-Systems (1/27)

## Next actions
- Sep 20-22: bulk re-check pending directories (agents.net earliest)
- Sep 22: weekly X post slot opens (draft: "201 wheel downloads, first live Nano directory listing at nanodirectory.info, #XNO")
- When req1 arrives: publish PyPI package
- When req2 arrives: open x402-foundation/x402 docs PR first, then xpaysh/awesome-x402
- Consider: have the owner send the AgentIndexed mailto submission manually (quick)