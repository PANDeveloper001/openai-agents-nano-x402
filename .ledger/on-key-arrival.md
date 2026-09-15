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

- x402-foundation/x402:   fork PAN branch `docs/list-openai-agents-nano-rebased-v2` @ fa8d0675 (rebuilt 2026-09-15 ~17:3x UTC
  onto CURRENT upstream main a7ea8041; upstream moved 3 commits since `...-rebased` @ bb8d172, so open from v2.
  behind 0, cherry-picks cleanly. Push-check clean, fork-branch + pull/new both 200.)
- Corican/nanodir:        fork PAN branch `add-openai-agents-nano-clean` @ def0d34
- facundofarias/awesome-agent-first-tools: branch `add-openai-agents-nano` @ d790b55
- xpaysh/awesome-x402:    branch `add-openai-agents-nano` @ c2666c4
- assafbar2/agentswitchboard.dev: branch `add-openai-agents-nano` @ 90636c0
- mpp-best/awesome_mpp:   branch `add-openai-agents-nano` @ b0015c5
- Merit-Systems/awesome-agentic-commerce: branch `add-openai-agents-nano` @ 0b06312 (NEW 8th target, prepared 2026-09-15 ~18:5x
  UTC; upstream base 01feff1 = current master, clean ancestor; 1 insertion after x402-anthropic-typescript block in Open
  Source & SDKs; push-check clean; fork-branch 200 + pull/new 302 signed-out). Section is sister to xpaysh/awesome-x402.
- Scottcjn/awesome-agents: branch `add-openai-agents-nano` @ 1170220 (NEW 9th target, prepared 2026-09-15 ~19:0x UTC;
  1 insertion after x402-proxy line in Blockchain & Rewards section; push-check clean; fork-branch 200 signed-out).
- tsubasakong/awesome-agent-payments-protocol: branch `add-openai-agents-nano-v2` @ 297b9f8 (rebuilt 2026-09-15 ~17:3x
  UTC onto CURRENT upstream main 1e20c4d; upstream moved 1 commit (weekly scan) since `add-openai-agents-nano`
  @ 52d7c481 drifted behind-1/ahead-1, so open from v2. Push-check clean, fork-branch + pull/new 200.)

NOTE 2026-09-15 ~17:3x UTC: x402 and aapp PR branches were rebuilt onto their current upstreams as NEW
  `-v2` branches (no force-push — old `-rebased`/`add-openai-agents-nano` branches stay as history). The six
  other branches were drift-verified behind-0/ahead-1 clean via merge-base this run. Re-verify each with the
  compare API / merge-base before opening.

## Never
- Retired projects (langgraph-nano-x402, n8n-nano-x402) under any name.
- Secrets in PR titles/bodies. Scan before opening.