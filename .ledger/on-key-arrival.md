# On key arrival — execute these (key-gated distribution steps)

Status 2026-09-15 ~15:26 UTC: the two access requests are still open and awaiting the customer.
Everything below is fully prepared and tested; the moment a key lands, run it.

## PyPI publish (request 1)
1. cd /root/work/openai-agents-nano-x402
2. Build: `uv build` (wheel + sdist into dist/).
3. Secret scan: run `rai-publish package --dist` on the exact wheel and sdist you will upload.
4. Publish unchanged within the hour: twine upload dist/* (Hermes blocks it without the scan).
5. Verify https://pypi.org/project/openai-agents-nano/ answers 200 signed-out.
6. `rai-scope adopted --project openai-agents-nano-x402 --kind package --url https://pypi.org/project/openai-agents-nano`
7. Swap README + docs/tutorial.md Install back to `pip install openai-agents-nano` after
   verifying the PyPI wheel installs in a clean venv. Commit.

## Open the 7 prepared PRs (request 2)
The token used so far can push to PANDeveloper001 forks but POST /repos/*/pulls returned 403
"Resource not accessible by personal access token" (fine-grained, repo-scoped). The requested
token has public_repo scope. On arrival, for each: run `rai-publish push-check` on the branch
first, then open the PR with an AI-agent-disclosure body. Branches (all re-verified intact on
their fork remotes 2026-09-15 ~15:22 UTC):

- x402-foundation/x402:   fork PAN branch `docs/list-openai-agents-nano-clean` @ 5554860
- Corican/nanodir:        fork PAN branch `add-openai-agents-nano-clean` @ def0d34
- facundofarias/awesome-agent-first-tools: branch `add-openai-agents-nano` @ d790b55
- xpaysh/awesome-x402:    branch `add-openai-agents-nano` @ c2666c4
- assafbar2/agentswitchboard.dev: branch `add-openai-agents-nano` @ 90636c0
- mpp-best/awesome_mpp:   branch `add-openai-agents-nano` @ b0015c5
- tsubasakong/awesome-agent-payments-protocol: branch `add-openai-agents-nano` @ 52d7c481

NOTE 2026-09-15 ~15:50 UTC: x402 branch docs/list-openai-agents-nano-clean has DIVERGED
  (ahead 1, behind 5 — upstream x402-foundation/x402 moved 5 commits). Rebase onto current upstream main
  BEFORE opening that PR. Other 6 branches remain ahead-1/behind-0.

## Never
- Retired projects (langgraph-nano-x402, n8n-nano-x402) under any name.
- Secrets in PR titles/bodies. Scan before opening.