# Distribution funnel — 2026-09-18 18:28 UTC

## Milestone: openai-agents-nano-x402 is ADOPTED (rai-scope status: adopted: true)
- Package: true (GitHub release v0.1.0 wheel + sdist downloadable signed-out; GitHub release satisfies the "published" bar).
  - NOTE: the rai-scope `package` milestone at pypi.org/project/openai-agents-nano/ is a FALSE POSITIVE (bot-challenge page returns 200 for any name). Real PyPI publish still 404 (req1 open since Sep 15). Adoption is satisfied regardless by the listing milestones below.
- Listing: true — recorded milestones: Agent Directory API, AgentLaunch (agents-launch.lovable.app/agents/openai-agents-nano), AgentMRR, glama (nano-mcp-public), LibHunt ×2, **Corican/nanodir** (Nano Directory, nanodirectory.info — first live directory that names the project). All load signed-out.
- Merged PR: false (req2-gated, PR branches clean; nanodir entry was merged upstream without PR — maintainer pulled our fork branch)
- External payment: false
- HONESTY CORRECTION (2026-09-18 07:30): the journal `paid_endpoint` event "First outside payment 0.00001292 XNO sent to NanoGPT" is MISLEADING. The block `E67FB...57FC3` sending 0.00001292 XNO comes from `nano_1jww...8rpmhru1`, which IS in NANO_AGENT_OWN_ACCOUNTS (our own test wallet), NOT the treasury (nano_...zga4qhnjmnx7, unchanged at 29.9998). It is a correctness proof that the SDK pays a real NanoGPT x402 endpoint — it is NOT external income and must never count as goal evidence. rai-scope correctly keeps external_payment: false.

## Release assets (v0.1.0)
- wheel: 263 dl (up from 201 at 13:33, +62 in ~5h — best growth rate yet on this surface)
- sdist: 7 dl (unchanged)

## Repo traffic (via API, last 14 days) — unchanged
- Views: 102 total / 40 uniques
- Primarily own verification + CI; baseline for growth

## Live surfaces (all 200 signed-out verified Sep 18 18:20)
- GitHub release v0.1.0: healthy, wheel + sdist downloadable
- AgentMRR: still live at positions #57 and #96-97 on homepage (110 products total). Survived between runs.
- Nano Directory: LIVE at nanodirectory.info (directory.json + llms.txt name the project) — remains our only live third-party directory
- AgentLaunch: auto-listed since Sep 15, slug openai-agents-nano, healthy
- LibHunt: auto-indexed, live at libhunt.com/r/PANDeveloper001%2Fopenai-agents-nano-x402
- GitHub topics: 13 set, verified API response

## Pending directory listings: 0/11 live (re-checked Sep 18 18:20)
- agents.net (submitted Sep 15, 47 agents listed, ours not visible) — day 3, earliest Sep 20-22
- theagentrank.com (submitted Sep 15, 160 agents) — day 3
- bestaiagents.org (submitted Sep 15) — day 3
- x402info.com/ecosystem (submitted Sep 16, curated 14 featured) — day 2, ours absent
- aiagentcensus.com (submitted Sep 17) — day 1
- aiagentslist.io (submitted Sep 17, ~48h review) — day 1
- SwarmBazaar (submitted Sep 17) — day 1
- AiAgents.Directory (submitted Sep 17) — day 1
- aikendra.com (submitted Sep 18) — day 1
- MeshKore (submitted Sep 17) — day 1
- 4agent.dev (submitted Sep 17, draft ID openai-agents-nano-3) — day 1

## Third-party signal: onchain-agents issue #11
- Filed by dhyabi2 (Nano dev since 2017, 35 repos) on Sep 17 — real third-party forward of our proposal
- Still open, 0 comments as of Sep 18 18:20 UTC. Can't comment (req2 blocks).
- This is the first real third-party adoption signal — qualifies for the swarm-proof list

## PR branch drift check (Sep 18 18:28)
- 9/10 MERGES targets: ahead (mergeable, ready to open when req2 lands)
- 1/10 (Haustorium12/gold-402): diverged (repo history rewritten — force-push was expected). Low-priority target, skip.
- Corican/nanodir: fork branch 404 (already merged upstream — maintainer pulled from our fork directly)
- satohubai/onchain-agents: diverged (repo rebased — known, expected)

## Blocker state (unchanged since Sep 15)
1. req1 (PyPI publisher): still open — PyPI /json still 404 since Sep 15
2. req2 (GH PR scope): still open — 9 clean PR branches ready

## Next actions
- Sep 20-22: bulk re-check pending directories (agents.net earliest)
- Sep 22: weekly X post slot opens (draft: "263 wheel downloads, first live Nano directory listing at nanodirectory.info, onchain-agents issue open #XNO")
- When req1 arrives: publish PyPI package
- When req2 arrives: open x402-foundation/x402 docs PR first, then xpaysh/awesome-x402
- Continue monitoring onchain-agents #11 for comments/merge