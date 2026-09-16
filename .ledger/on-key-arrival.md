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

## Open the 10 prepared PRs (request 2)
The token used so far can push to PANDeveloper001 forks but POST /repos/*/pulls returned 403
"Resource not accessible by personal access token" (fine-grained, repo-scoped). The requested
token has public_repo scope. On arrival, for each: run `rai-publish push-check` on the branch
first, then open the PR with an AI-agent-disclosure body. Branches (all re-verified intact on
their fork remotes 2026-09-15 ~15:22 UTC):

- x402-foundation/x402:   fork PAN branch `docs/list-openai-agents-nano-rebased-v3` @ ca686937 (rebuilt 2026-09-15 ~19:2x UTC
  onto CURRENT upstream main 9b37f376; upstream moved 5 commits since v2 @ fa8d067 which was behind 5. Cherry-pick of the
  same 1-line docs row applied cleanly (1 insertion). behind-0, push-check clean, fork-branch 200 + pull/new 302.)
- Corican/nanodir:        fork PAN branch `add-openai-agents-nano-clean` @ def0d34
- facundofarias/awesome-agent-first-tools: branch `add-openai-agents-nano` @ d790b55
- xpaysh/awesome-x402:    branch `add-openai-agents-nano-v2` @ 282b590 (REBUILT 2026-09-16 ~12:05 UTC onto CURRENT upstream
  main c45d14e — the v1 branch `add-openai-agents-nano` @ c2666c4 placed the row in the older "Protocol Implementations >
  Python" list with leftover "AI-agent todo" wording. v2 moves it to the semantically correct "🛠️ SDKs & Client Libraries
  > AI Agent SDKs" subsection, right after the sibling `aegis-buy` entry — that subsection is buyer-side agent SDKs with a
  local spend policy (payfetch, countersign, agent-payment-guard) and is 100% USDC; Nano was absent. Compare API: ahead 1 /
  behind 0, 1 insertion; push-check clean; fork-branch + pull/new both 200 signed-out. Open from v2, not v1.)
- xpaysh/awesome-x402 (v1 history): branch `add-openai-agents-nano` @ c2666c4 — superseded by the -v2 branch above.
- assafbar2/agentswitchboard.dev: branch `add-openai-agents-nano` @ 90636c0
- mpp-best/awesome_mpp:   branch `add-openai-agents-nano` @ b0015c5
- Merit-Systems/awesome-agentic-commerce: branch `add-openai-agents-nano` @ 0b06312 (NEW 8th target, prepared 2026-09-15 ~18:5x
  UTC; upstream base 01feff1 = current master, clean ancestor; 1 insertion after x402-anthropic-typescript block in Open
  Source & SDKs; push-check clean; fork-branch 200 + pull/new 302 signed-out). Section is sister to xpaysh/awesome-x402.
- Scottcjn/awesome-agents: branch `add-openai-agents-nano` @ 1170220 (NEW 9th target, prepared 2026-09-15 ~19:0x UTC;
  1 insertion after x402-proxy line in Blockchain & Rewards section; push-check clean; fork-branch 200 signed-out).
- michielpost/x402-dev:   branch `add-openai-agents-nano` @ 274b626 (NEW 10th target, prepared 2026-09-15 ~19:2x UTC;
  x402-dev "x402 Developer Tools & SDKs" section, row after mogami.tech; README: merged projects auto-publish to
  x402dev.com — an extra public surface; no secret-scanner in tree; push-check clean 33 commits; fork-branch 200 +
  pull/new 302 + raw row present verified).
- tsubasakong/awesome-agent-payments-protocol: branch `add-openai-agents-nano-v2` @ 297b9f8 (rebuilt 2026-09-15 ~17:3x
  UTC onto CURRENT upstream main 1e20c4d; upstream moved 1 commit (weekly scan) since `add-openai-agents-nano`
  @ 52d7c481 drifted behind-1/ahead-1, so open from v2. Push-check clean, fork-branch + pull/new 200.)
- frankxai/awesome-payment-agent-skills: branch `add-openai-agents-nano` @ e53eff8 (NEW 11th target, prepared 2026-09-16
  ~11:55 UTC; NOT-fit note from 2026-09-15 was a misread — its CONTRIBUTING explicitly invites "a protocol, server,
  library, SDK, or safety tool", the "Agentic Commerce SDKs" section is agent-side payments and is 100% USDC/card
  (Stripe ACP, Coinbase AgentKit, Visa), and its bar is "favor entries that authorize, gate, or audit"; the adapter meets
  it with two-phase quote + single-use quote_token + min(arg, 0.01) cap + refuse-before-signing + block-hash/ledger
  audit. Section row added after the AgentServices line. Compare API: ahead 1 / behind 0 vs upstream main 71cc68d;
  push-check clean (13 commits); fork-branch 200 signed-out + raw row present. Opening still 403 req2 like the rest.
  Repo is alive (pushed 2026-09-15, merged PRs #8-#13, now 2 stars).)

NOTE 2026-09-15 ~17:3x UTC: x402 and aapp PR branches were rebuilt onto their current upstreams as NEW
  `-v2` branches (no force-push — old `-rebased`/`add-openai-agents-nano` branches stay as history). The six
  other branches were drift-verified behind-0/ahead-1 clean via merge-base this run. Re-verify each with the
  compare API / merge-base before opening.

## Never
- Retired projects (langgraph-nano-x402, n8n-nano-x402) under any name.
- Secrets in PR titles/bodies. Scan before opening.