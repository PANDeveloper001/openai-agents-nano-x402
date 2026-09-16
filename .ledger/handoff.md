# Handoff - open these prepared pull requests (one click each)

Generated 2026-09-16 21:08 UTC from `.ledger/tmp/drift_all.json`. Regenerate, never hand-edit:

```bash
python3 scripts/prepared_pr_drift_all.py --json .ledger/tmp/drift_all.json
python3 scripts/prepared_pr_clicks.py
```

`POST /repos/<third-party>/pulls` is 403 on the stored token, so each row below is the target's own
compare page with `?expand=1`: it opens the full pull-request form prefilled from the fork branch.
Every URL is checked signed out; the HTTP status is the one measured at generation time.

| # | target | branch | compare URL (signed-out status) |
|---|---|---|---|
| 1 | `Corican/nanodir` | `add-openai-agents-nano-clean` | [200](https://github.com/Corican/nanodir/compare/HEAD...PANDeveloper001:add-openai-agents-nano-clean?expand=1) |
| 2 | `Haustorium12/gold-402` | `add-openai-agents-nano` | [200](https://github.com/Haustorium12/gold-402/compare/HEAD...PANDeveloper001:add-openai-agents-nano?expand=1) |
| 3 | `Merit-Systems/awesome-agentic-commerce` | `add-openai-agents-nano` | [200](https://github.com/Merit-Systems/awesome-agentic-commerce/compare/HEAD...PANDeveloper001:add-openai-agents-nano?expand=1) |
| 4 | `Scottcjn/awesome-agents` | `add-openai-agents-nano-v3` | [200](https://github.com/Scottcjn/awesome-agents/compare/HEAD...PANDeveloper001:add-openai-agents-nano-v3?expand=1) |
| 5 | `assafbar2/agentswitchboard.dev` | `add-openai-agents-nano-v3` | [200](https://github.com/assafbar2/agentswitchboard.dev/compare/HEAD...PANDeveloper001:add-openai-agents-nano-v3?expand=1) |
| 6 | `e2b-dev/awesome-ai-sdks` | `add-openai-agents-nano-v2` | [200](https://github.com/e2b-dev/awesome-ai-sdks/compare/HEAD...PANDeveloper001:add-openai-agents-nano-v2?expand=1) |
| 7 | `facundofarias/awesome-agent-first-tools` | `add-openai-agents-nano` | [200](https://github.com/facundofarias/awesome-agent-first-tools/compare/HEAD...PANDeveloper001:add-openai-agents-nano?expand=1) |
| 8 | `frankxai/awesome-payment-agent-skills` | `add-openai-agents-nano` | [200](https://github.com/frankxai/awesome-payment-agent-skills/compare/HEAD...PANDeveloper001:add-openai-agents-nano?expand=1) |
| 9 | `mbeato/awesome-mpp` | `add-nano-x402-agent-framework` | [200](https://github.com/mbeato/awesome-mpp/compare/HEAD...PANDeveloper001:add-nano-x402-agent-framework?expand=1) |
| 10 | `michielpost/x402-dev` | `add-openai-agents-nano` | [200](https://github.com/michielpost/x402-dev/compare/HEAD...PANDeveloper001:add-openai-agents-nano?expand=1) |
| 11 | `mpp-best/awesome_mpp` | `add-openai-agents-nano` | [200](https://github.com/mpp-best/awesome_mpp/compare/HEAD...PANDeveloper001:add-openai-agents-nano?expand=1) |
| 12 | `tsubasakong/awesome-agent-payments-protocol` | `add-openai-agents-nano-v2` | [200](https://github.com/tsubasakong/awesome-agent-payments-protocol/compare/HEAD...PANDeveloper001:add-openai-agents-nano-v2?expand=1) |
| 13 | `x402-foundation/x402` | `docs/list-openai-agents-nano-v7` | [200](https://github.com/x402-foundation/x402/compare/HEAD...PANDeveloper001:docs/list-openai-agents-nano-v7?expand=1) |
| 14 | `x402-foundation/x402` | `specs/exact-nano-mainnet` | [200](https://github.com/x402-foundation/x402/compare/HEAD...PANDeveloper001:specs/exact-nano-mainnet?expand=1) |
| 15 | `xpaysh/awesome-x402` | `add-openai-agents-nano-v2` | [200](https://github.com/xpaysh/awesome-x402/compare/HEAD...PANDeveloper001:add-openai-agents-nano-v2?expand=1) |

15 clean branches, 0 whose compare page did not answer 200 at generation time.

Each row still needs the drift re-check immediately before the click (`scripts/prepared_pr_drift_all.py`); `x402-foundation/x402` moves several commits a day.
