# Handoff - open these prepared pull requests (one click each)

Generated 2026-09-19 07:13 UTC from `.ledger/tmp/drift_all.json`. Regenerate, never hand-edit:

```bash
python3 scripts/prepared_pr_drift_all.py --json .ledger/tmp/drift_all.json
python3 scripts/prepared_pr_clicks.py
```

`POST /repos/<third-party>/pulls` is 403 on the stored token, so each row below is the target's own
compare page with `?expand=1`: it opens the full pull-request form prefilled from the fork branch.
Every URL is checked signed out; the HTTP status is the one measured at generation time.

| # | target | branch | compare URL (signed-out status) |
|---|---|---|---|
| 1 | `Haustorium12/gold-402` | `add-openai-agents-nano-v4` | [200](https://github.com/Haustorium12/gold-402/compare/HEAD...PANDeveloper001:add-openai-agents-nano-v4?expand=1) |
| 2 | `Merit-Systems/awesome-agentic-commerce` | `add-openai-agents-nano` | [200](https://github.com/Merit-Systems/awesome-agentic-commerce/compare/HEAD...PANDeveloper001:add-openai-agents-nano?expand=1) |
| 3 | `Scottcjn/awesome-agents` | `add-openai-agents-nano-v3` | [200](https://github.com/Scottcjn/awesome-agents/compare/HEAD...PANDeveloper001:add-openai-agents-nano-v3?expand=1) |
| 4 | `assafbar2/agentswitchboard.dev` | `add-openai-agents-nano-v3` | [200](https://github.com/assafbar2/agentswitchboard.dev/compare/HEAD...PANDeveloper001:add-openai-agents-nano-v3?expand=1) |
| 5 | `bitrefill/awesome-agentic-payments` | `add-openai-agents-nano-x402` | [200](https://github.com/bitrefill/awesome-agentic-payments/compare/HEAD...PANDeveloper001:add-openai-agents-nano-x402?expand=1) |
| 6 | `caramaschiHG/awesome-ai-agents-2026` | `add-openai-agents-nano` | [200](https://github.com/caramaschiHG/awesome-ai-agents-2026/compare/HEAD...PANDeveloper001:add-openai-agents-nano?expand=1) |
| 7 | `chgaowei/ai-agent-infra-list` | `add-x402-nano-settlement-rail` | [200](https://github.com/chgaowei/ai-agent-infra-list/compare/HEAD...PANDeveloper001:add-x402-nano-settlement-rail?expand=1) |
| 8 | `e2b-dev/awesome-ai-sdks` | `add-openai-agents-nano-v2` | [200](https://github.com/e2b-dev/awesome-ai-sdks/compare/HEAD...PANDeveloper001:add-openai-agents-nano-v2?expand=1) |
| 9 | `facundofarias/awesome-agent-first-tools` | `add-openai-agents-nano` | [200](https://github.com/facundofarias/awesome-agent-first-tools/compare/HEAD...PANDeveloper001:add-openai-agents-nano?expand=1) |
| 10 | `frankxai/awesome-payment-agent-skills` | `add-openai-agents-nano` | [200](https://github.com/frankxai/awesome-payment-agent-skills/compare/HEAD...PANDeveloper001:add-openai-agents-nano?expand=1) |
| 11 | `goodmeta/agent-payments-landscape` | `add-nano-payment-rail` | [200](https://github.com/goodmeta/agent-payments-landscape/compare/HEAD...PANDeveloper001:add-nano-payment-rail?expand=1) |
| 12 | `mbeato/awesome-mpp` | `add-nano-x402-agent-framework` | [200](https://github.com/mbeato/awesome-mpp/compare/HEAD...PANDeveloper001:add-nano-x402-agent-framework?expand=1) |
| 13 | `michielpost/x402-dev` | `add-openai-agents-nano` | [200](https://github.com/michielpost/x402-dev/compare/HEAD...PANDeveloper001:add-openai-agents-nano?expand=1) |
| 14 | `mpp-best/awesome_mpp` | `add-openai-agents-nano` | [200](https://github.com/mpp-best/awesome_mpp/compare/HEAD...PANDeveloper001:add-openai-agents-nano?expand=1) |
| 15 | `tsubasakong/awesome-agent-payments-protocol` | `add-openai-agents-nano-v2` | [200](https://github.com/tsubasakong/awesome-agent-payments-protocol/compare/HEAD...PANDeveloper001:add-openai-agents-nano-v2?expand=1) |
| 16 | `x402-foundation/x402` | `docs/list-openai-agents-nano-extension-v1` | [200](https://github.com/x402-foundation/x402/compare/HEAD...PANDeveloper001:docs/list-openai-agents-nano-extension-v1?expand=1) |
| 17 | `x402-foundation/x402` | `docs/list-openai-agents-nano-v10` | [200](https://github.com/x402-foundation/x402/compare/HEAD...PANDeveloper001:docs/list-openai-agents-nano-v10?expand=1) |
| 18 | `x402-foundation/x402` | `specs/exact-nano-mainnet-v3` | [200](https://github.com/x402-foundation/x402/compare/HEAD...PANDeveloper001:specs/exact-nano-mainnet-v3?expand=1) |
| 19 | `x402eco/website` | `add-openai-agents-nano-x402eco-v2` | [200](https://github.com/x402eco/website/compare/HEAD...PANDeveloper001:add-openai-agents-nano-x402eco-v2?expand=1) |
| 20 | `xpaysh/awesome-x402` | `add-openai-agents-nano-v2` | [200](https://github.com/xpaysh/awesome-x402/compare/HEAD...PANDeveloper001:add-openai-agents-nano-v2?expand=1) |
| 21 | `AiFinPay/sdk` | `add-nano-x402-example` | [200](https://github.com/AiFinPay/sdk/compare/main...PANDeveloper001:add-nano-x402-example?expand=1) |

21 clean branches, 0 whose compare page did not answer 200 at generation time.

Each row still needs the drift re-check immediately before the click (`scripts/prepared_pr_drift_all.py`); `x402-foundation/x402` moves several commits a day.
