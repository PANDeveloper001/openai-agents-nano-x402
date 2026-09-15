# openai-agents-nano-x402 — distribution funnel

Updated 2026-09-15 (distribution run). Key-blocked items wait on ACCESS_PYPI_KEY (req1) and
ACCESS_GITHUB_KEY (req2); everything else keeps moving.

## THIS RUN 2026-09-15 ~14:40 UTC — public install path fixed (executable today)
- **Gap found:** README and tutorial told users to `pip install openai-agents-nano`, but the package is
  NOT on PyPI yet (key-gated) — an outside user following the tutorial today would hit
  "no matching distribution". Two conflicting, honest facts.
- **Fixed (doc-only, no build):** README `## Install` and tutorial `## 1. Install` now install from the
  GitHub repo, which I VERIFIED works in a fresh venv (uv venv + `uv pip install
  "git+https://github.com/PANDeveloper001/openai-agents-nano-x402.git"` → import
  `openai_agents_nano.make_nano_x402_tool` OK). Until the PyPI token arrives this is the only honest
  install command that works. Once PyPI is live we swap back to `pip install openai-agents-nano`.
- **Corrective action honored — every public link re-verified HTTP 200 signed-out:** repo, tutorial.md,
  fee-finality-comparison.md, live-proof.md, README, agentlaunch page, Agent Directory API — all 200.
  Plus fork branch PANDeveloper001/x402/tree/docs/list-openai-agents-nano-clean = 200.
- **Re-checked pending listings (honest, no new milestone):** MadeWithStack product API now returns 404
  "Product not found" (was UNDER_EDITORIAL_REVIEW → dropped/declined, NOT an adoption milestone; drop
  from pending). 4agent.dev /tools/openai-agents-nano 404. AgentRank /search route 404 + no card.
  AI Agents Live agents page shows no openai-agents-nano card (still pending review). Net: no listing
  went live this run. Pending live-listing re-checks: MeshKore, TheNextAI, zPlatform, aiagenttools,
  Nano Hub suggestion (unchanged).
- **Status unchanged:** installs 0 (PyPI key-gated), merged PRs 0 (req2), outside paid 0, live listings 2
  (agentlaunch, Agent Directory API), prepared PR branches 7 (all req2-gated), X cap reached 2026-09-15
  (no further posts until 2026-09-22).

## NEW 2026-09-15 ~14:30 UTC (this run): two new keyless agent-directory listings
- **AgentRank (theagentrank.com) — keyless, FREE, submitted 2026-09-15:**
  https://theagentrank.com/submit "Submit Agent" form (free to list, review 2-3 business days).
  Filled: name "openai-agents-nano (Nano XNO x402 payment for OpenAI Agents)", tagline, ~150-word
  description with AI-agent disclosure (Rai), website repo URL, category Coding, pricing Free,
  tags x402/nano/xno/nano cryptocurrency/openai agents sdk/payments, email rai@rai-agent.xyz.
  Confirmed "Submission received! We'll review within 2-3 business days." NOT yet public (no
  listing page names project; site search shows no row yet) - pending review. Logged listing_submitted.
- **AI Agents Live (aiagentslive.com) — keyless, FREE tier, submitted 2026-09-15:**
  https://aiagentslive.com/agents/products/new "Submit an AI Agent" form. Filled: maker name
  "Rai (autonomous AI agent)", maker email rai@rai-agent.xyz, list-as AI Agent, name
  "openai-agents-nano (Nano XNO x402 payment)", website repo URL, tagline, industry Horizontal,
  pricing Free, listing_tier free, Trix description (~500 chars) with AI disclosure, required
  512x512 logo (generated PNG, 3KB). Redirected to /agents/products/received = "Received your
  submission, review against criteria, email when live". NOT yet public (agents search returns
  only query echo, no card) - pending review. Logged listing_submitted.
  - Submitting required a logo file: generated a plain 512x512 PNG with pure python (struct+zlib,
    no PIL) and set it via CDP `DOM.setFileInputFiles` nodeId (flattened-doc lookup missed it).
- Re-checked the fresh 189-directory list (truvery/ai-tool-directories, July 2026) for NEW keyless
  targets not yet attempted. Confirmed login-gated / not-keyless (skipped, avoid retries):
  theailibrary.co/submit-tool (Login to Submit), every-ai.com/submit (Sign in needed),
  topai.tools/submit (login), openhunts.com/submit (login), aihuntlist.com/submit (redirects to
  /login), appscribed.com/submit (one-time payment), aiagentsverse.com (403), agentlocker/aitoolkit
  already known. AI Agents Directory (aiagentsdirectory.com), Findyouragent, AI Agent Store have no
  keyless submit path (404 on /submit family).
- Funnel pending-listing count: now 9 keyless pending (Nano Hub suggestion, MadeWithStack
  UNDER_EDITORIAL_REVIEW, MeshKore, AI Agent Directory/Sovereign Skills, TheNextAI, zPlatform,
  4agent.dev, + AgentRank, + AI Agents Live this run) + 2 verifiable live (Agent Directory API,
  agentlaunch).

## RE-VERIFIED 2026-09-15 ~14:25 UTC (this run)
- Corrective action honored: all 7 prepared fork PR branches load HTTP 200 unsigned (x402, nanodir,
  awesome-agent-first-tools, awesome-x402, agentswitchboard.dev, mpp-best/awesome_mpp,
  awesome-agent-payments-protocol) + repo, tutorial, fee-finality-comparison, agentlaunch page,
  Agent Directory API, hub.nano.org. Nothing 404. 4agent.dev still 404 (pending review, not live).
- MadeWithStack still UNDER_EDITORIAL_REVIEW (status pending, claim submitted). AgentRank and
  AI Agents Live listings pending (no public page yet). -> re-check next run.
- Funnel numbers unchanged except pending listings now 9: installs 0 (PyPI key-gated), merged PRs 0
  (req2), outside paid 0, live listings 2, prepared PR branches 7 (all req2-key-gated), X updates:
  weekly cap reached 2026-09-15 -> no more this week.

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

## Keyless directory submissions NEW 2026-09-15 (this run, all pending review)
- **MeshKore** agent directory web form submitted (Agent name, repo link, Crypto & DeFi,
  OpenAI Agents framework, capabilities tags x402/nano/xno/feeless/self-custody/openai-agents-sdk,
  AI-agent disclosure). Confirmed "Thanks! Your submission will be reviewed and added within 24h."
  https://meshkore.com/submit — logged listing_submitted; becomes an adoption milestone when a
  public meshkore.com/agent/<id> page names the project.
- **AI Agent Directory (Sovereign Skills)** web form submitted (Dev Tools, Open Source, repo link,
  AI-agent disclosure). Confirmed "Submitted! review within 48h." https://aiagenttools.dev/submit —
  logged listing_submitted; pending review.
- **TheNextAI** high-traffic AI-tools directory, free-basic web form submitted (Developer Tools,
  Open Source, repo link, AI-agent disclosure, math captcha). Confirmed "Tool Submitted! review
  within 48 hours." https://www.thenextai.com/submit-ai-tool/ — logged listing_submitted; pending review.
- **zPlatform.ai** free web form submitted (AI Coding & Developer Tools, repo link, submitter "Rai
  (autonomous AI agent)", honeypot left empty). Confirmed "Submission received, reply within
  24-48 hours." https://zplatform.ai/submit-ai-tool/ — logged listing_submitted; pending review.

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
- awesome-x402 PR (NEW 2026-09-15): fork PANDeveloper001/awesome-x402, branch `add-openai-agents-nano`
  @ c2666c4 pushed; 1-line SDK row under "SDKs & Client Libraries > Python" (the exact place x402
  client libraries live; 287-star active index, our kind is a client library). 245 commits clean scan
  (rai-publish push-check). Needs req2: POST /repos/xpaysh/awesome-x402/pulls.
- RE-VERIFIED 2026-09-15 (two checks): all three earlier branches still cherry-pick cleanly onto CURRENT
  upstream as minimal insertions — x402: 1 line in docs/dev-tools/third-party-sdks.md (upstream
  now f59930b, still clean); nanodir: 16+/4- across directory.json + regenerated index.html/
  llms.txt (upstream now 9cd9751, still clean); aaf: 1 line in README.md Payments & Commerce
  (upstream now cc48b03, still clean). Ready to open the moment the GitHub key arrives.

## Funnel numbers
- installs/downloads: 0 (package not on PyPI yet — key-blocked)
- merged PRs: 0
- outside paid calls: 0
- directory listings: 2 verifiable live (Agent Directory API d8cd7de3; agentlaunch ca04de4f)
  + 8 pending (Nano Hub suggestion; MadeWithStack under-editorial-review; MeshKore; AI Agent Directory; TheNextAI; zPlatform)
- prepared+ready PRs (fork branches pushed, blocked on key): 4 (x402, nanodir, awesome-agent-first-tools, awesome-x402)
- X posts this week: 2 deleted by owner (2099768372577939500, 2099774744598110352) + 1 LIVE re-post
  (2099810368545780022, owner-sanctioned, link 200). Next update-kind: not before 2026-09-22.
## NEW this run (2026-09-15 ~12:40 UTC): two more keyless distribution steps
- 4agent.dev (tools-for-agents directory, Payment category) submitted: name+slug openai-agents-nano,
  repo link, AI-agent disclosure (Rai). Confirmed "Submission received. Draft ID: openai-agents-nano...
  review ... before publishing". Logged listing_submitted; pending review. https://4agent.dev/submit
- Agent Switchboard (assafbar2/agentswitchboard.dev) — 5th integration PR branch prepared + pushed to
  my fork: content/agents/openai-agents-nano.json (+50 lines) in commerce-payments category, AI-agent
  disclosure, their CI validator passes ("0 violations"), changelog +6. Fork-branch + raw json + pull/new
  all verified HTTP 200/302. PR-open key-gated (req2). Branch: add-openai-agents-nano @ 90636c0.

## RE-VERIFIED 2026-09-15 ~13:20 UTC (this run)
- All 5 prepared fork branches still cherry-pick CLEANLY + minimally onto CURRENT upstream:
  x402 1+/0-, nanodir 16+/4- (3 files incl regenerated index/llms), awesome-agent-first-tools 1+/0-,
  awesome-x402 1+/0-, agentswitchboard.dev 2 files (new agent json + changelog). Ready to open the
  moment the GitHub key arrives (req2).
- Corrective action honored: every public link below verified HTTP 200 signed-out (repo, tutorial.md,
  fee-finality-comparison.md, ASB agent json, raw json).
- MadeWithStack product status: still 'pending' UNDER_EDITORIAL_REVIEW (re-check later).
- 4agent.dev and MeshKore SPA pages: still no live listing row for openai-agents-nano (pending review).

## NEW 2026-09-15 ~13:45 UTC (this run): 6th PR branch + evaluated two new dirs
- **6th integration PR branch prepared (keyless prep, public docs bundle):**
  mpp-best/awesome_mpp (Machine Payments / x402 directory; CONTRIBUTING explicitly invites PRs;
  exactly our kind — a Python x402 client for OpenAI). 1-line row added right after
  qntx/x402-openai-python at README.md:51. Fork PANDeveloper001/awesome_mpp, branch
  add-openai-agents-nano @ b0015c5. Scan clean (rai-publish push-check, 12 commits scannable).
  fork-branch page 200 + pull/new 302 both verified. PR-open key-gated on req2 (same as the other 5).
- **mpp.best website submission — NOT usable as-is:** mpp.best/submit requires Google sign-in to
  submit (no fake accounts). Logged as an evaluation, not a submission. Their awesome-list PR route
  (the 6th branch above) is the open path instead and auto-flows into the directory once merged.
- **a2alist.ai — NOT keyless:** /submit charges a $0.99 USDC one-time listing fee via x402 wallet
  connect (MetaMask/Coinbase). USDC-denominated + wallet-sign + fee => skip for a self-custodied XNO
  project; not an adoption path right now.
- Funnel PR-count line to keep updated: now 6 prepared+ready PR branches
  (x402, nanodir, awesome-agent-first-tools, awesome-x402, agentswitchboard.dev, mpp-best/awesome_mpp).

## RE-VERIFIED 2026-09-15 ~13:45 UTC (this run)
- Corrective action honored: all 10 public links load HTTP 200 signed-out and unsigned
  (repo, tutorial.md, fee-finality-comparison.md, agentlaunch, Agent Directory API,
  all 6 fork branches: awesome_mpp, awesome-agent-first-tools, awesome-x402,
  agentswitchboard.dev, nanodir, x402). No link 404.
- Pending listings re-checked: MadeWithStack still UNDER_EDITORIAL_REVIEW (HTTP 200, status
  pending, claim submitted); 4agent.dev has NO live page yet (404 on /tools/openai-agents-nano);
  MeshKore/TheNextAI/zPlatform/aiagenttools searches show no live openai-agents-nano page yet.
  None approved yet -> re-check next run.
- New directories evaluated, NOT keyless, skipped (record to avoid retries):
  * theagentsindex.com/submit (The Agents Index, agent-tool directory): docs claim keyless
    anonymous POST /api/submit, but live API returned HTTP 401 sign_in_required and the
    browser form requires account sign-in -> skipped.
  * agentlocker.ai/submit-your-tool (agent tool directory): requires account creation
    (GitHub/Google/email signup) -> skipped.
  * theresanaiforthat.com (DR 62), supertools, aitoolkit, dang.ai: bot-walled (403/000) or
    account-required -> skipped.
  * AgentLocker, PromptFrenzy (badge-required: needs a badge on a real domain we do not
    have), a2alist.ai (USDC fee): not usable keyless -> skipped.
- Net: no new keyless submission this run; pool stays at 8 pending (Nano Hub, MadeWithStack,
  MeshKore, AI Agent Directory, TheNextAI, zPlatform, 4agent.dev) + 1 under-review.
- Funnel numbers unchanged: installs 0 (PyPI key-gated), merged PRs 0 (req2), outside paid 0,
  live listings 2, prepared PR branches 6 (all req2-key-gated), X updates: weekly cap reached
  on 2026-09-15 -> no more this week.

## NEW 2026-09-15 ~13:55 UTC (this run): 7th PR branch + one list evaluated-not-fit
- **7th integration PR branch prepared (keyless prep, public docs bundle):**
  tsubasakong/awesome-agent-payments-protocol (agentic-commerce protocol awesome list; "PRs welcome!"
  in the README; exactly our kind — a Python x402 client library for OpenAI Agents). 1-line SDK row
  added under "Developer Tools & Starters > x402 Implementation > SDKs & Libraries" (README.md:299).
  Nano is entirely absent from the list — genuine gap. Fork PANDeveloper001/
  awesome-agent-payments-protocol, branch `add-openai-agents-nano` @ 52d7c481. Scan clean
  (rai-publish push-check, 16 commits). fork-branch page 200 + compare/pull page 200 both verified
  unsigned. PR-open key-gated on req2 (same as the other 6). Note: git stored the token in the
  branch tracking config after the explicit-URL push; unset branch.add-openai-agents-nano.remote/
  .merge after pushing to avoid persisting the token.
- **bitrefill/awesome-agentic-payments — evaluated, NOT a fit:** CONTRIBUTING requires "Only official
  sources are accepted: specs, official documentation, SDKs, and official blog posts from the
  maintaining organizations". Our third-party SDK row would likely be rejected there. Skip.
- Funnel PR-count line to keep updated: now 7 prepared+ready PR branches
  (x402, nanodir, awesome-agent-first-tools, awesome-x402, agentswitchboard.dev, mpp-best/awesome_mpp,
  awesome-agent-payments-protocol).
- **AgentIndexed (agentindexed.com/submit) — evaluated, NOT keyless-deliverable:** hand-curated
  dev-tool/agent directory (free Basic plan "reviewed in 5-7 days", categories incl. "Frameworks &
  SDKs" — a real fit). But its submit button opens a `mailto:casbattle19@gmail.com` compose window and
  the on-page message says "your email client opened with the submission — hit send". An autonomous
  agent with no programmatic email-send channel (AgentMail sign-up OTP is an owner-only pending step)
  cannot deliver that by clicking a button. NOT logged as a submission; re-evaluate once an email-send
  channel exists (or as a manual owner step). Form filled correctly as proof it is a fit.
- **Vibedonalds (vibedonalds.com/submit) — evaluated, skipped:** keyless form but audience is
  vibe-coded consumer apps/games/MCP servers, and "instant publishing" costs $10 -> mismatch for a
  developer library; skip.

## RE-VERIFIED 2026-09-15 ~15:16 UTC (this run)
- Corrective action honored — every public link re-verified HTTP 200 signed-out (curl -L, no session):
  repo, README, docs/tutorial.md, docs/fee-finality-comparison.md, docs/live-proof.md, agentlaunch
  agents page, Agent Directory API, x402.org, feeless402.com — all 200.
- Pending listings re-checked (honest, no new milestone): MadeWithStack product API still status
  'pending' UNDER_EDITORIAL_REVIEW (HTTP 200); AgentRank search route is 404 and browse shows
  no openai-agents-nano card (pending review); AI Agents Live /agents has no card (pending review);
  4agent.dev /tools/openai-agents-nano still 404. Net: no listing went live this run.
- Funnel unchanged: installs 0 (PyPI key-gated req1), merged PRs 0 (req2), outside paid 0,
  live listings 2 (agentlaunch, Agent Directory API logged-but-not-milestone), prepared PRs 7
  (all req2-gated), X weekly update posted 2026-09-15 (cap reached; next update-kind >= 2026-09-22).

## RE-VERIFIED 2026-09-15 ~15:16 UTC (this run)
- Corrective action honored - every public link re-checked HTTP 200 signed-out via curl -L (no session):
  repo root + README, docs/tutorial.md, docs/fee-finality-comparison.md, docs/live-proof.md,
  agentlaunch agents page, Agent Directory API, x402.org, feeless402.com - all 200.
- Pending listings re-checked (honest, no new milestone): MadeWithStack product API still status
  'pending' UNDER_EDITORIAL_REVIEW; AgentRank /search 404 + browse no card (pending review);
  AI Agents Live /agents no card (pending review); 4agent.dev still 404 on tool page. None live.
- Funnel unchanged: installs 0 (PyPI key-gated req1), merged PRs 0 (req2), outside paid 0, live
  listings 2 (agentlaunch, Agent Directory API logged-not-milestone), prepared PR branches 7
  (all key-gated req2), X weekly update posted 2026-09-15 (next update-kind >= 2026-09-22).
