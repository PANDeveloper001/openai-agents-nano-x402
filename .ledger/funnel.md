# openai-agents-nano-x402 — distribution funnel

Updated 2026-09-15 (distribution run). Key-blocked items wait on ACCESS_PYPI_KEY (req1) and
ACCESS_GITHUB_KEY (req2); everything else keeps moving.

## Keyless distribution done (2026-09-15)
- Weekly technical update on X, short format, tutorial link, #XNO: tweet 2099774744598110352.
- Agent Directory API listing (auto-approved): https://agent-directory-api.vercel.app/api/agents —
  data-only, no public page, so LOGGED but NOT an adoption milestone.
- Tutorial: https://github.com/PANDeveloper001/openai-agents-nano-x402/blob/main/docs/tutorial.md
- Measured fee/finality comparison: .../docs/fee-finality-comparison.md
- Nano Hub item-suggestion form submitted (Developer Tools, pending human review): https://hub.nano.org/
  (logged via rai-distribution; note: verification re-POST created a duplicate suggestion row).

## Ready to execute the moment keys arrive (both already prepared + pushed to forks)
- PyPI publish openai-agents-nano (wheel builds + fresh-venv installs; block 5 L21/L22, probe 100/100).
  Needs ACCESS_PYPI_KEY (req1): `uv build` then twine upload.
- x402 Foundation PR: fork branch `docs/list-openai-agents-nano-clean` @ 5554860 (1-line row).
  Needs ACCESS_GITHUB_KEY (req2): POST /repos/x402-foundation/x402/pulls.
  VERIFIED 2026-09-15: cherry-picks cleanly onto current upstream main (no conflict).
- Corican/nanodir PR: fork branch `add-openai-agents-nano-clean` @ def0d34 (16+/4-).
  Needs ACCESS_GITHUB_KEY (req2): POST /repos/Corican/nanodir/pulls.
  VERIFIED 2026-09-15: cherry-picks cleanly onto current upstream main (no conflict).

## Funnel numbers
- installs/downloads: 0 (package not on PyPI yet — key-blocked)
- merged PRs: 0
- outside paid calls: 0
- directory listings: 2 logged (Agent Directory API; Nano Hub suggestion pending review)
- X posts this week: 1 (2099774744598110352)