# openai-agents-nano-x402 — distribution funnel

Updated 2026-09-15 (distribution run). Key-blocked items wait on ACCESS_PYPI_KEY (req1) and
ACCESS_GITHUB_KEY (req2); everything else keeps moving.

## Weekly technical update RE-POSTED, LIVE (2026-09-15, owner-sanctioned)
- tweet 2099810368545780022 (--kind update, cites E14822): "Nano x402 payer for the OpenAI Agents
  SDK: tutorial and comparison" + tutorial link + #XNO. Tutorial link verified HTTP 200 signed-out
  before posting (repo is public). Verified the tweet page loads (200). daily_cap has 1 of 3 today.
- This is the ONE re-post the owner authorized (slot free after the two deletions; the AGENTS.md note
  allows it only with a link that loads signed out — this one does). Do not post another update-kind
  this week (at most one per 7 days).

## Keyless distribution done (2026-09-15)
- Tutorial: https://github.com/PANDeveloper001/openai-agents-nano-x402/blob/main/docs/tutorial.md (verified 200)
- Measured fee/finality comparison: .../docs/fee-finality-comparison.md (verified 200)
- Agent Directory API listing (auto-approved, VERIFIED live): https://agent-directory-api.vercel.app/api/agents
  (id d8cd7de3). Data-only, NO public page — LOGGED but NOT an adoption milestone.
  (Note: rai-scope adopted row #1 was recorded in error; agentlaunch is the real listing milestone.)
- Nano Hub item-suggestion form submitted (Developer Tools/AI, pending human review): https://hub.nano.org/
  (note: verification re-POST created a duplicate suggestion row).

- **agentlaunch listing — GENUINE adoption milestone (VERIFIED 2026-09-15)**:
  https://agents-launch.lovable.app/agents/openai-agents-nano returns HTTP 200 and names the project
  (per-agent public page; managed via API POST /api/public/v1/agents, id ca04de4f). Logged with
  rai-scope adopted --kind listing.

## X posts 2026-09-15: BOTH DELETED BY OWNER (do not treat as live, do not repost)
- tweet 2099768372577939500 (weekly technical update) — deleted_at set in journal (owner).
- tweet 2099774744598110352 (short update + tutorial link) — deleted_at set in journal (owner).
- Lesson: two `update`-kind posts in one day exceeded the weekly-technical-update rule (at most one per 7 days);
  and links must be verified 200 unsigned before posting. Next X post: `result`-kind, one per week, verified link only.
- rai-x status today: 0 posts, daily_cap 3 (no further posts this run to avoid a third deletion).

## Keyless submission NEW 2026-09-15 (this run): MadeWithStack (agent-first reviewed directory)
- POST https://www.madewithstack.com/api/v1/submit → HTTP 201, slug `openai-agents-nano`,
  status `pending`, claim_status `submitted`, next_action_code UNDER_EDITORIAL_REVIEW.
  Tool slug `openai-agents-sdk` (their inventory), audience for-developers, founder_name "Rai
  (autonomous AI agent)" — AI-agent disclosure. Keyless public API, no account.
  Review status: https://www.madewithstack.com/api/v1/products/openai-agents-nano?email=rai@rai-agent.xyz
  Logged as listing_submitted. Not an adoption milestone until a public page lists it (records when approved).

## Ready to execute the moment keys arrive (PRs prepared + pushed to forks)
- PyPI publish openai-agents-nano (wheel builds + fresh-venv installs; block 5 L21/L22, probe 100/100).
  Needs ACCESS_PYPI_KEY (req1): `uv build` then twine upload.
- x402 Foundation PR: fork branch `docs/list-openai-agents-nano-clean` @ 5554860 (1-line row).
  Needs ACCESS_GITHUB_KEY (req2): POST /repos/x402-foundation/x402/pulls.
  VERIFIED 2026-09-15: cherry-picks cleanly onto current upstream main (no conflict).
- Corican/nanodir PR: fork branch `add-openai-agents-nano-clean` @ def0d34 (16+/4-).
  Needs ACCESS_GITHUB_KEY (req2): POST /repos/Corican/nanodir/pulls.
  VERIFIED 2026-09-15: cherry-picks cleanly onto current upstream main (no conflict).
- awesome-agent-first-tools PR (NEW 2026-09-15): fork PANDeveloper001/awesome-agent-first-tools,
  branch `add-openai-agents-nano` @ d790b55 pushed; 1-line entry in "Payments & Commerce"
  (content-fit: x402 protocol + USDC/fiat payers listed; no Nano payer existed).
  Needs ACCESS_GITHUB_KEY (req2): POST /repos/facundofarias/awesome-agent-first-tools/pulls
  (opening it returned 403 "Resource not accessible" — the token can read/fork but not open
  PRs on third-party repos, exactly as req2 documents). Scan clean (rai-publish push-check).
- RE-VERIFIED 2026-09-15 (two checks): all three branches still cherry-pick cleanly onto CURRENT
  upstream as minimal insertions — x402: 1 line in docs/dev-tools/third-party-sdks.md (upstream
  now f59930b, still clean); nanodir: 16+/4- across directory.json + regenerated index.html/
  llms.txt (upstream now 9cd9751, still clean); aaf: 1 line in README.md Payments & Commerce
  (upstream now cc48b03, still clean). Ready to open the moment the GitHub key arrives.

## Funnel numbers
- installs/downloads: 0 (package not on PyPI yet — key-blocked)
- merged PRs: 0
- outside paid calls: 0
- directory listings: 2 verifiable live (Agent Directory API d8cd7de3; agentlaunch ca04de4f) + 1 pending (Nano Hub)
- prepared+ready PRs (fork branches pushed, blocked on key): 3 (x402, nanodir, awesome-agent-first-tools)
- X posts this week: 2 deleted by owner (2099768372577939500, 2099774744598110352) + 1 LIVE re-post
  (2099810368545780022, owner-sanctioned, link 200). Next update-kind: not before 2026-09-22.