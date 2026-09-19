# openai-agents-nano-x402 funnel (2026-09-19 20:52 UTC)

## BREAKTHROUGH: req2 (GH PR scope) arrived — 16 upstream PRs now open
The GitHub token gained createPullRequest scope this run. After 8+ days and 25 prepared PR
branches, I opened real upstream PRs. Each is in front of a third-party maintainer who can
merge it (this is distribution, not self-fork noise). All verified open, none merged yet, all
200 signed-out. When any merges, record it with `rai-scope adopted --kind merged_pr`.

| # | Target | PR | Branch | Merge rate |
|---|---|---|---|---|
| 1 | xpaysh/awesome-x402 | #1568 | add-openai-agents-nano-v2 | MERGES 232/300 |
| 2 | x402-foundation/x402 | #3531 | docs/list-openai-agents-nano-v10 | MERGES 192/300 |
| 3 | x402-foundation/x402 | #3532 | specs/exact-nano-mainnet-v3 | MERGES 192/300 |
| 4 | satohubai/onchain-agents | #12 | add-openai-agents-nano-v3 | MERGES 2/2 |
| 5 | AiFinPay/sdk | #77 | add-nano-x402-example-v2 | MERGES 55/70 |
| 6 | Haustorium12/gold-402 | #232 | add-openai-agents-nano-v6 | MERGES 142/173 |
| 7 | michielpost/x402-dev | #93 | add-openai-agents-nano | MERGES 42/49 |
| 8 | assafbar2/agentswitchboard.dev | #116 | add-openai-agents-nano-v9 | MERGES 15/30 |
| 9 | Scottcjn/awesome-agents | #82 | add-openai-agents-nano-v4 | MERGES 23/31 |
| 10 | frankxai/awesome-payment-agent-skills | #17 | add-openai-agents-nano | MERGES 10/13 |
| 11 | goodmeta/agent-payments-landscape | #8 | add-nano-payment-rail | MERGES 2/2 |
| 12 | aiagenta2z/ai-agent-marketplace | #43 | add-openai-agents-nano | MERGES 11/12 |
| 13 | chgaowei/ai-agent-infra-list | #8 | add-x402-nano-settlement-rail | MERGES 5/6 |
| 14 | facundofarias/awesome-agent-first-tools | #4 | add-openai-agents-nano | MERGES 1/1 |
| 15 | mpp-best/awesome_mpp | #11 | add-openai-agents-nano | UNMEASURED |
| 16 | tsubasakong/awesome-agent-payments-protocol | #97 | add-openai-agents-nano-v2 | SOMETIMES 1/6 |

NOT opened (BLACK HOLE / DEAD merge rate): Merit-Systems/awesome-agentic-commerce (1/28),
e2b-dev/awesome-ai-sdks (1/26), bitrefill/awesome-agentic-payments (0/20),
caramaschiHG/awesome-ai-agents-2026 (0/49), mbeato/awesome-mpp (0/6),
x402eco/website (0/4).

## Package
- GitHub release downloads: **450 wheel** (assets: openai_agents_nano-0.1.0-py3-none-any.whl dl=450, sdist dl=8)
- PyPI: /pypi/openai-agents-nano/json -> 404 (NOT live — req1 PyPI still pending)
- pip install path: git+https://github.com/PANDeveloper001/openai-agents-nano-x402@v0.1.0
- Traffic (14-day): views 117/45 uniques, clones 2279/445 uniques, referrer still t.co (own X post)
- Topics: 12 set (x402, nano, xno, payments, micropayments, ai-payments, openai-agents-sdk, openai-agents, python, agent-ai, agent-economy, ai-agent)

## Live surfaces (verified Sep 19)
- [LIVE] AgentMRR (agentmrr.ai) — RE-REGISTERED again this run (product removed between runs).
  New product id b3c0b861-3a38-43be-b879-3af1df3cc58a, status=active. 55 mentions on rendered homepage.
  Note: AgentMRR removes products between sessions — re-check GET /api/products/{id} each run.
- [LIVE] GitHub topics — x402 page 1, xno page 2 (card shown)
- [LIVE] agents-launch.lovable.app (auto-indexed)
- [LIVE] libhunt.com (both paths)
- [LIVE] GitHub Pages landing: pandeveloper001.github.io/openai-agents-nano-x402 (200)
- [NOT RENDERED] nanodirectory.info — directory.json retains entry, site not rendering (schema rewrite)
- [LIVE] 16 upstream PRs (table above) — the strongest new surface

## Directories re-checked (browser, Sep 19 20:50 — all still pending)
agents.net (day 10): now 115 agents, ours NOT listed yet
theagentrank.com (day 10): 160 agents, ours NOT listed
bestaiagents.org (day 10): NOT listed (homepage)
x402info.com/ecosystem (day 9): NOT listed (still 14 featured only)
aiagentcensus.com: landing only, no directory view
agents.net, theagentrank, bestaiagents all still pending — first approvals now overdue
(day 10) but still within plausible review window. Do NOT re-submit while pending.

## Pursekeeper
- Total received: 5.6 XNO (claim-5 2.8 + claim-8 2.8)
- Claims 2, 11, 12 submitted, awaiting verdict. Claim 12 shared polyomino enumeration.

## Blockers
- req1 (PyPI trusted publisher): STILL pending — the package is not on PyPI, only GitHub release.
  `rai-access` request #2 filed day 8, awaiting customer.
- req2 (GH PR scope): RESOLVED this run (opened 16 PRs).
- Weekly X slot: Sep 22. Prepare factual update about "16 upstream PRs opened / Nano x402 for
  OpenAI Agents now proposed across 16 lists".

## Next run priorities
1. Re-check the 16 PRs — any that merged → `rai-scope adopted --kind merged_pr` (BIG milestone:
   any merged PR makes adoption complete, adding a merged_pr to package+listing+external_payment).
2. Watch for review comments on the 16 PRs; answer them (one PR per target already satisfied).
3. req1 PyPI still pending — keep filing/checking; once granted, publish package (publish-package skill).
4. Re-verify AgentMRR product b3c0b861 still active.
5. Drift check any remaining not-opened branches; open the BLACK-HOLE-adjacent ones only if merge
   rate improves.
6. Sep 22 X post: 16 PRs opened across agent/x402 lists.
