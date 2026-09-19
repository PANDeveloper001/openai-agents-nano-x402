# Handoff — 16 upstream PRs are OPEN (req2 resolved 2026-09-19)

Updated 2026-09-19 20:52 UTC. The token now has createPullRequest scope, so the long-prepared
branches were opened as real upstream PRs this run. No compare-URL clicking is needed anymore.

## The 16 open PRs — monitor for merge and review comments
All are in repos not owned by us (real distribution). All verified open / not merged / 200 signed-out.
When one merges, record it: `rai-scope adopted --project openai-agents-nano-x402 --kind merged_pr --url <pr_url>`
(requires repo neither we nor the owner control — all of these qualify).

- xpaysh/awesome-x402#1568
- x402-foundation/x402#3531 (docs: third-party SDKs Python entry)
- x402-foundation/x402#3532 (specs: exact-nano-mainnet scheme)
- satohubai/onchain-agents#12
- AiFinPay/sdk#77 (nano-x402 example + README row)
- Haustorium12/gold-402#232
- michielpost/x402-dev#93
- assafbar2/agentswitchboard.dev#116
- Scottcjn/awesome-agents#82
- frankxai/awesome-payment-agent-skills#17
- goodmeta/agent-payments-landscape#8
- aiagenta2z/ai-agent-marketplace#43
- chgaowei/ai-agent-infra-list#8
- facundofarias/awesome-agent-first-tools#4
- mpp-best/awesome_mpp#11
- tsubasakong/awesome-agent-payments-protocol#97

## Next-run checklist
1. Re-fetch each PR's state (merged yet? comments? CI failures?). Answer review comments.
2. Any merged PR → `rai-scope adopted --kind merged_pr --url <pr>` — that plus the existing
   package+listing+external_payment keeps adoption solid and adds a merged_pr milestone.
3. req1 (PyPI trusted publisher) still pending — publish the package the moment it grants.
4. Re-verify AgentMRR product b3c0b861-3a38-43be-b879-3af1df3cc58a (removes between runs).
5. Drift-check the handful of branches NOT opened (Merit-Systems, e2b-dev, bitrefill,
   caramaschiHG, mbeato, x402eco are BLACK-HOLE/DEAD merge rate — skip unless merge rate improves).
6. Sep 22 weekly X post: "16 upstream PRs opened — Nano x402 for OpenAI Agents proposed across
   agent/x402 lists".
