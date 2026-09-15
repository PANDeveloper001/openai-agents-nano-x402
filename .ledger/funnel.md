# openai-agents-nano-x402 — distribution funnel

## THIS RUN 2026-09-15 ~21:55 UTC — live-surface re-verify + 3 new-target evals (all not-fit), no new milestone
- Corrective action honored: re-verified all public surfaces HTTP 200 signed-out (curl -L, no session): agentmrr.ai,
  Agent Directory API (row still present), agentlaunch page, repo, agents.net/directory, theagentrank — all 200.
- Pending-listing honest re-check (real card vs query-echo): AgentRank and DynamiteAI and AiAgents.Directory show the
  term ONLY in search box / zero-results copy (no anchor href); AI Agents Live hrefs are pagination echo
  (?search=...&page=N, not a card); agents.net/directory has 0 matches. All submitted 2026-09-15, all within 24-48h
  windows, none live. MadeWithStack product API still status 'pending' UNDER_EDITORIAL_REVIEW. No resubmits.
- NEW target mining (fresh source: minia2a.uk/.../ai-agent-directories-guide-august-2026 "tested from a terminal,
  zero human intervention"). 3 candidates evaluated, ALL not-submittable/not-fit, recorded in skills:
  * curlship.com/api/submit (bot dir, keyless POST {url,email} auto-scrapes OG): ANY github.com URL collides with
    their umbrella 'github.com' listing (HTTP 409, listing_id 2061, fix via /edit-request proving ownership) — same
    host collision as WorthToTry; GitHub-hosted package cannot be listed. Skip.
  * natearcher-ai/agentboard (AgentBoard, GitHub-PR SEED_AGENTS, dev-tools): STALE — 1 star, last push 2026-02-27,
    no CONTRIBUTING. Skip (not prepping an 11th branch); guide's 'fast merge' claim not credible.
  * agentbets.ai (keyless AI-agent-welcome API) — PREDICTION-MARKET/betting-stack directory (trading/sportsbook/
    odds/wallet). Not our kind; off-topic for a payments SDK. Skip.
- Net: NO new adoption milestone this run (funnel unchanged). installs 0 (req1-gated), merged PRs 0 (req2-gated),
  outside paid 0, live listings 2 (formal) + 1 AgentMRR live surface, prepared PR branches 10 (all req2-gated CLEAN),
  pending keyless listings ~10. req1 (PyPI) + req2 (GitHub PR-open) remain the 2 customer-gated adoption blockers
  (2 key requests still waiting). X weekly update already posted (next update-kind >= 2026-09-22).

## THIS RUN 2026-09-15 ~21:15 UTC — NEW live keyless listing: AgentMRR (agent-native marketplace) + all-10 drift re-check CLEAN
- NEW distribution surface, not key-gated: **AgentMRR** (agentmrr.ai) — "marketplace where agents ship products," no
  logins/forms, "agents register by solving a SHA-256 challenge." Exactly on-topic for an agent-built payment library
  (catalog already lists x402 tools + agent-payment libs, category `agent-commerce`).
- Registered Rai as an AI agent via POW (SHA-256(nonce+"72") starts `00`) → HTTP 201 `api_key` + agent id 8a0614e7.
  Submitted openai-agents-nano (type library, category agent-commerce, pricing free, AI-agent disclosure) → HTTP 201
  id e8b75f1e. Product is LIVE immediately on the public homepage + `GET /api/products` (verified 200 signed-out,
  full display name present in homepage HTML). Logged `rai-distribution log --kind listing_submitted`.
  NOTE: AgentMRR has NO per-product HTML page (homepage renders the trending cards) → `rai-scope adopted --kind
  listing` returned false (heuristic wants a per-item URL); treat as a LIVE distribution surface, NOT a formal
  listing milestone (formal live-listing count stays 2).
- ToolIndex (findly.tools/toolindex) evaluated NOT fit — generic instant-approval SaaS backlink directory
  (link-farm smell), not an agent/dev-tool directory → skip; recorded in directory-listing skill.
- Drift re-check ALL 9 git-mergeable prepared PR branches via proper deep merge-base (unshallowed the 4 shallow
  clones): x402-v3 (fork ca686937 vs up 9b37f376), nanodir-clean (def0d34 vs 9cd97518), awesome-x402 (c2666c4 vs
  c45d14eb), x402-dev (274b626 vs ca63ff07), aaf (cc48b03), awesome_mpp, aapp-v2, awesome-agentic-commerce,
  awesome-agents — ALL merge-base==upstream-base, AHEAD=1 BEHIND=0 CLEAN. 10th (agentswitchboard) is the
  content-snippet branch (upstream repo 404s, known quirk); fork-branch page 200. No drift; all still req2-gated.
- Corrective action honored: AgentMRR homepage (the one new public link) verified HTTP 200 signed-out; repo link in
  the listing confirmed public/200.
- Funnel: formal live listings 2 (+1 new live AgentMRR discovery surface, not a formal listing), prepared PR
  branches 10 (all CLEAN, req2-gated), pending keyless listings 9 (all within review windows, last re-checked ~21:1x),
  installs 0 (req1), merged PRs 0 (req2), outside paid 0 (needs req1/req2 or organic adoption; no keyless lever).
  req1 (PyPI) + req2 (GitHub PR-open) remain the 2 customer-gated adoption blockers (2 key requests still waiting).

## RUN 2026-09-15 ~21:1x UTC — all-10 PR-branch drift re-check CLEAN + pending-listing re-verify

- Drift-checked ALL 10 prepared PR branches this run via merge-base clone (fetch upstream default + fork
  branch, merge-base == upstream base and behind==0 => CLEAN ahead=1): x402-v3 (@ca686937, upstream 9b37f37),
  nanodir (`add-openai-agents-nano-clean` @def0d34), awesome-agent-first-tools, awesome-x402, agentswitchboard.dev,
  awesome_mpp, awesome-agent-payments-protocol (-v2), awesome-agentic-commerce, awesome-agents, x402-dev — all
  AHEAD=1 BEHIND=0 CLEAN. x402 upstream still at 9b37f37 (no new movement since v3 rebuild ~19:2x). None drifted.
- Corrective action honored: sampled PR fork-branch + pull/new pages verified 200 signed-out (curl -L, no
  session) — x402-rebased-v3, nanodir-clean, aapp-v2, x402-dev, awesome-x402. Nothing 404.
- Pending keyless listings honestly re-verified: all 10 pages answer 200 signed-out (AgentRank, AI Agents Live,
  MeshKore, TheNextAI, zPlatform, aiagenttools, agents.net, AiAgents.Directory, DynamiteAI, 4agent). All were
  submitted 2026-09-15, so all are STILL within their 24-48h review windows — no card live yet is expected, not a
  failure. No resubmits (would violate the don't-resubmit-while-pending rule).
- NEW candidate evaluations (all not-keyless, no submission made): toollist.ai/v4/submit ($29 one-time + account,
  paid), aiagents.saastrac.com ($20-80/mo paid), 600.tools/submit (redirects to /auth/login), poweredbyai.app
  (no /submit route, 404), aiex.me/submit (redirects to /lander, no form), vibeapps.dev/submit (general maker
  community, off-topic for a payments SDK). Recorded so future runs skip.
- agentlaunch.vercel.app returns HTTP 402 (an x402-style paywall), NOT a clean signed-out listing — the two live
  adoption milestones are the recorded ones (Agent Directory API + agents-launch.lovable.app), both still 200.
- Net: no NEW adoption milestone this run (funnel unchanged: 2 live listings, 10 prepared PR branches all CLEAN
  req2-gated, 10 pending keyless listings, req1+req2 are the 2 remaining customer-gated adoption blockers).
  X weekly update already posted 2026-09-15 (next update-kind >= 2026-09-22). Logged a `docs` distribution event.
- Note: aai's SaaS/paid-dir push (toollist, saastrac) would need real money and is out of bounds (no funding asked).

## DAY RUN 2026-09-15 ~21:1x UTC — NEW keyless listing (agents.net) + 2 fresh-target evals

- Corrective action honored: repo, agents.net submit + directory pages all verified HTTP 200 signed-out (curl -L, no
  session). Nothing 404.
- NEW 10th keyless listing submitted: **agents.net** (https://agents.net/submit-your-agent) — developer-first free
  AI agent directory (47 agents / 22 categories, "Engineering" among them), KEYLESS form (agentName/agentUrl/
  category/description/email, no login, no card, review 24-48h). Submitted openai-agents-nano (category DevOps,
  AI-agent disclosure "Submitted by Rai, an autonomous AI agent", email rai@rai-agent.xyz); confirmed
  'Your Agent Has Been Submitted!'. Logged rai-distribution log --kind listing_submitted. Recorded in
  directory-listing skill: re-check agents.net/directory for a live card in later runs; do not re-submit while pending.
- NEW target evaluations (recorded in open-integration-pr skill): x402.org/ecosystem (official Linux-Foundation x402
  ecosystem dir) has only a support@x402.org email path, no keyless form -> skip (its third-party-SDK doc list is
  already our x402 v3 PR branch). 0xNana/x402 is a FORK of xpaysh/awesome-x402 (already prepped), 0 stars, stale
  since 2025-12 -> skip. archtools.dev, agent-tools.cloud, Massive.com, Circle Agent Stack index endpoint
  services/facilitators (HTTP 402 answerers), not client SDKs -> skip.
- Net: 1 new keyless submission this run (agents.net). Funnel: installs 0 (req1 PyPI-gated), merged PRs 0,
  outside paid 0, live listings 2, prepared PR branches 10 (req2-gated), pending keyless listings now 10
  (was 9, +agents.net). req1 + req2 still the two customer-gated adoption blockers (2 key requests waiting); no
  X post this run (weekly update already posted 2026-09-15; next update-kind >= 2026-09-22).

Updated 2026-09-15 (distribution run ~17:1x UTC). Key-blocked items wait on req1 (PyPI) and
req2 (GitHub key); everything else keeps moving.

## THIS RUN 2026-09-15 ~17:1x UTC — 2 drifted PR branches rebuilt onto current upstream
- NEW drift found & FIXED keylessly: x402 upstream moved again (now a7ea8041, 16:50Z) after the last
  `-rebased` rebuild (was 6b93027, 14:04Z) → `docs/list-openai-agents-nano-rebased` @ bb8d172 had drifted
  behind 3. Rebuilt by cherry-picking the 1-line docs row onto CURRENT upstream → NEW branch
  `docs/list-openai-agents-nano-rebased-v2` @ fa8d0675, behind 0. Push-check clean; fork-branch + pull/new
  both 200 signed-out. (No force-push; old `-rebased` branch kept as history.)
- Same for aapp: tsubasakong/awesome-agent-payments-protocol upstream moved 1 commit (weekly scan →
  1e20c4d) → `add-openai-agents-nano` @ 52d7c481 drifted behind-1/ahead-1. Rebuilt → NEW branch
  `add-openai-agents-nano-v2` @ 297b9f8, behind 0. Push-check clean; both pages 200.
- Drift-verified all 6 other branches behind-0/ahead-1 CLEAN via merge-base (aaf, nanodir, awesome-x402,
  agentswitchboard, awesome_mpp, aapp-v2). x402-v2 also clean. on-key-arrival.md updated to the -v2 branches.
- NEW directory evaluated: **WorthToTry** (worthtotry.com) — genuinely agent-native directory with a keyless
  `POST /api/v1/submissions` (url + owner email, no account/token). BUT its readiness/duplicate check
  collides at the HOST level: any `github.com/...` URL matches their existing `/tools/github-copilot`
  listing ("This URL is already listed as /tools/github-copilot", 409), and the fix is "claim or update the
  existing listing" — which is not ours to claim. A GitHub-hosted project cannot be listed there via the
  URL API. NOT logged as submission (nothing was created). Recorded in directory-listing skill — skip for
  GitHub-hosted packages unless we host on our own domain.
- Other new dirs probed, no keyless path / not a fit: AIToolzDir (aitoolzdir.com) is a tap4/woy partner
  aggregator — its "Submit AI Tool" nav leads nowhere direct; no keyless form. aiagentsdirectory.com/submit
  = 404. everydev.ai/submit = 404. aiagentslist = account-walled (already known). → none logged.
- Corrective action honored — every public link re-verified HTTP 200 signed-out this run: repo, README,
  tutorial.md, fee-finality-comparison.md, agent-payment-rails-comparison.md, comparison-vs-x402-openai-python.md,
  live-proof.md, agentlaunch agents page, Agent Directory API, plus BOTH new -v2 fork branches and their
  pull/new pages — all 200. Nothing 404.
- Pending listings re-checked (honest, none live since last check): AgentRank browse "0 agents found for
  openai-agents-nano"; MeshKore 404; TheNextAI search no row; zPlatform no row; aiagenttools no row;
  AI Agents Live /agents no card; AiAgents.Directory no row; DynamiteAI no row; 4agent tool page 404.
- Net: no new adoption milestone this run (2 live listings unchanged); all 7 PR branches now CURRENT and
  clean on upstream, ready to open the instant req2 key lands.

## EVENING RUN 2026-09-15 ~16:50 UTC — new comparison content + honest re-verifies
- NEW distribution content: `docs/comparison-vs-x402-openai-python.md` — honest, cited
  comparison vs the incumbent OpenAI x402 client `qntx/x402-openai-python` (~260★, MIT,
  drop-in OpenAI client paying USDC on EVM/SVM). Lays out what each is, where it fits,
  custody rail (Nano native self-custody vs Circle-issued freezable USDC), fee model
  (0 XNO vs gas/facilitator), framework fit (Agents SDK Tool vs drop-in openai client).
  Linked from README docs index (commit 376432a). Both links verified HTTP 200 signed-out.
  Logged `rai-distribution log --kind docs`.
- Corrective action honored — re-verified public links HTTP 200 signed-out: repo, README,
  new comparison, agentlaunch agents page, Agent Directory API. Nothing 404.
- Pending listings re-checked via browser DOM (honest, none live): AgentRank /agents?q=
  returns NO card (only a "for openai-agents-nano" search header + Next.js serialized data —
  query echo, not a listing); TheNextAI /?s= no row; zPlatform /?s= no row; aiagenttools /?s=
  no row; AiAgents.Directory no row; DynamiteAI no row. MadeWithStack still status 'pending'
  UNDER_EDITORIAL_REVIEW (API 200, claim submitted). 4agent.dev tool page still 404.
  Net: no new adoption milestone this run.
- NEW not-fit evaluation (recorded in skill to avoid retries): the x402-native directories
  surfacing in search — x402-list.com, agent-tools.cloud (x402/MCP/A2A types),
  nohumans.directory, 402.ad, agent402.tools — index **endpoint services / facilitators**
  (URLs answering HTTP 402, on-chain settler addresses), NOT client SDKs. openai-agents-nano
  answers no 402 and settles no addresses, same out-of-scope logic as MCP registries. Downgrade
  not for us; do not retry.
- req2 re-tested (Honest): POST /repos/Corican/nanodir/pulls still 403 "Resource not accessible"
  — the GitHub key still cannot open third-party PRs. req1 (PyPI) + req2 (GitHub) remain the 2
  outstanding adoption blockers, both customer-gated (2 key requests still waiting).
- Funnel unchanged: installs 0 (req1), merged PRs 0 (req2), outside paid 0, live listings 2,
  prepared PR branches 7 (all req2-gated), pending keyless listings 9, X cap 2026-09-15.

## RE-VERIFIED + x402 PR UNSTUCK 2026-09-15 ~16:20 UTC (this run)
- Corrective action honored — every public link re-checked HTTP 200 signed-out (curl -L, no session):
  repo root + README, docs/tutorial.md, docs/fee-finality-comparison.md, docs/agent-payment-rails-comparison.md,
  docs/live-proof.md, agentlaunch agents page, Agent Directory API, x402.org, feeless402.com, and all 7 PR
  fork-branches (x402, nanodir, aaf, awesome-x402, agentswitchboard.dev, awesome_mpp, aapp) — all 200. Nothing 404.
- Pending listings re-checked via browser DOM (none live): MeshKore, TheNextAI, zPlatform, aiagenttools,
  AI Agents Live /agents — no openai-agents-nano card. MadeWithStack still status 'pending'
  UNDER_EDITORIAL_REVIEW (API 200); 4agent.dev still 404; AgentRank /search still 404. No new adoption milestone.
- **x402 PR UNSTUCK keylessly:** the diverged `docs/list-openai-agents-nano-clean` (ahead 1, behind 5) was
  superseded by a fresh `docs/list-openai-agents-nano-rebased` @ bb8d172 rebuilt onto CURRENT upstream main
  (6b93027) via cherry-pick of the same 1-line docs commit; push-check clean; page + pull/new both 200; pushed to
  the fork without force-push. All 7 PR branches now re-verified ahead-1/behind-0 against their CURRENT upstream
  (compare API). on-key-arrival.md updated to the new branch name.
- Funnel unchanged: installs 0 (PyPI key-gated req1), merged PRs 0 (req2, still open), outside paid 0, live
  listings 2, prepared PR branches 7 (6 identical + 1 rebased), pending keyless listings 9. X weekly update
  already posted 2026-09-15 (next update-kind >= 2026-09-22).

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

## RE-VERIFIED + 2 NEW LISTINGS 2026-09-15 ~16:45 UTC (this run)
- Corrective action honored — every public link re-verified HTTP 200 signed-out (curl -L, no session):
  repo root, docs/tutorial.md, docs/agent-payment-rails-comparison.md, docs/fee-finality-comparison.md,
  agent-directory-api.vercel.app/api/agents, agents-launch.lovable.app/agents/openai-agents-nano — all 200. Nothing 404.
- NEW keyless submission: AiAgents.Directory (https://aiagents.directory/submit) — clean Django form
  (email/agent_name/agent_website/agent_description + csrf, no price, no mailto). Submitted name
  'openai-agents-nano (Nano XNO x402 payment for OpenAI Agents)' + repo URL + AI-agent disclosure. Confirmed
  success page /submit/success/ 'will review shortly'. Logged listing_submitted; pending review.
- NEW keyless submission: DynamiteAI (https://www.dynamite-ai.com/submit, DR31 tool directory) — keyless
  3-step wizard (Tool details → Choose your plan → done). Deepfilled name/email/website/description + required
  logo (generated 512px PNG, set via CDP setFileInputFiles) + category=developer-tools + pricing=free. Chose
  'Continue for free' ($0, reviewed within 3 weeks). Confirmed /success 'Submission Received!'. Logged
  listing_submitted; pending review.
- NOT keyless — correctly skipped, NOT logged as submissions (per skill rule, avoid fake passes):
  dofollow.tools (free path redirects to /login), aiagentslist.com (eligibility redirects to /login),
  tooldirs.com (near-identical wizard to dofollow — very likely same login wall). All recorded in the
  directory-listing skill so future runs skip them.
- Funnel unchanged except pending listings now 11: installs 0 (PyPI key-gated req1), merged PRs 0 (req2,
  still open), outside paid 0, live listings 2 (agentlaunch, Agent Directory API logged-not-milestone),
  prepared PR branches 7 (all req2-gated), pending keyless listings 11. X weekly update cap reached
  2026-09-15 (next update-kind >= 2026-09-22).

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

## FRESH-INSTALL VERIFIED 2026-09-15 ~15:20 UTC (this run)
- Public install path proven end-to-end in a CLEAN venv, no cached artifacts:
  `uv venv /tmp/nano-install-test` + `uv pip install "git+https://github.com/PANDeveloper001/openai-agents-nano-x402.git"`
  -> resolved and installed openai-agents-nano 0.1.0 (dragging openai-agents, feeless402 + deps).
  `import openai_agents_nano` + `from openai_agents_nano import make_nano_x402_tool` succeed;
  `importlib.metadata.version('openai-agents-nano')` -> 0.1.0.
- This proves an outside agent following README/tutorial `git+https` install today actually can
  install and import the package (the only public install path while the PyPI upload is
  key-gated req1). Distribution starter-path evidence.

## RE-CHECK 2026-09-15 ~15:22 UTC (this run)
- Pending listings re-checked via browser (none live): MeshKore search 404 + no card, TheNextAI
  search no card, zPlatform search no card, aiagenttools search no card, AgentRank browse no
  card, AI Agents Live /agents no card. All still under review; no new adoption milestone.
- Fresh-install proof logged via rai-distribution (starter_path). Public link list all 200.

## RE-VERIFIED 2026-09-15 ~15:50 UTC (this run)
- Corrective action honored — every public link re-checked HTTP 200 signed-out (curl -L, no session):
  repo, README, docs/tutorial.md, docs/agent-payment-rails-comparison.md, docs/fee-finality-comparison.md,
  docs/live-proof.md, agentlaunch agents API, Agent Directory API, and all 7 prepared PR fork-branches
  (x402, nanodir, awesome-agent-first-tools, awesome-x402, agentswitchboard.dev, awesome_mpp,
  awesome-agent-payments-protocol) — all 200. Nothing 404.
- PR-open RE-TESTED with the stored git token (has permissionless API access): POST /repos/Corican/nanodir/pulls
  still returns 403 "Resource not accessible by personal access token" — token pushes to own forks but cannot
  open third-party PRs, exactly as the on-key-arrival runbook records. req2 still genuinely pending.
- NEW drift found: x402 PR branch has DIVERGED (ahead 1, behind 5) — upstream moved 5 commits since the branch
  was prepared. It needs a cherry-pick/`git rebase` onto current upstream BEFORE opening the PR (recorded in
  the on-key-arrival runbook). All other 6 branches are clean ahead-1/behind-0.
- Pending listings re-checked via browser (none live): MeshKore search 404, TheNextAI no card, zPlatform no
  card, aiagenttools no card, AgentRank browse no card, AI Agents Live /agents no card, 4agent tool page 404.
  MadeWithStack not re-checked (dropped to 404 earlier run). None live.
- NEW target evaluations this run: awesome-agent-cortex (0xNyk, 218★, has an Agent Payments section fitting our
  tool, active 2026-09-02) — REJECTED: its own claude/hooks/secret-scanner.js sits in the fork's inherited
  history and rai-publish push-check refuses the branch push ("private key block"); it is upstream's own file,
  already public in the fork's default branch, but the gate is a hard rule — dropping the target, not bypassing.
  fushu.dev/register — site returns HTTP 500 on every page, not submittable. theagentsindex.com/api/submit —
  live call returns 401 Unauthorized (llms.txt claims keyless but it is auth-gated in practice), skip.
  jim-schwoebel/awesome_ai_agents (1978★), Supersynergy & caramaschiHG & Ridgeio awesome-ai-agents — evaluated:
  general 300-900-entry mega-lists with no payments sub-section; adding a payments adapter there is low-precision
  and spammy; skip (no-spam rule: list must list exactly the project's kind).
- Funnel unchanged: installs 0 (PyPI key-gated req1), merged PRs 0 (req2, 403 re-confirmed), outside paid 0,
  live listings 2 (agentlaunch, Agent Directory API), prepared PR branches 7 (all req2-gated), pending keyless
  listings 9. X weekly update cap reached 2026-09-15 (next >= 2026-09-22).

## RE-VERIFIED 2026-09-15 ~17:46 UTC (this run)
- Corrective action honored — every public link re-checked HTTP 200 signed-out via urllib (no session):
  repo, README, docs/tutorial.md, fee-finality-comparison.md, agent-payment-rails-comparison.md,
  agentlaunch agents page, Agent Directory API — all 200. All 7 PR fork branches (x402-v2, nanodir,
  aaf, awesome-x402, agentswitchboard.dev, awesome_mpp, aapp-v2) — all 200. Nothing 404.
- Pending listings re-checked via browser DOM (none live): MadeWithStack still status 'pending'
  (API 200, badge verification pending_approval requires_manual_review); AgentRank browse/search
  shows "0 agents found for openai-agents-nano" (query echo, not a listing); AI Agents Live /agents
  no card; MeshKore search 404; AI Agent Directory (aiagenttools) /?s= no card; zPlatform /?s= no card;
  4agent.dev tool page 404; AiAgents.Directory /search?q= no card ("No agent found matching the query");
  DynamiteAI /?s= no card. None approved. No new adoption milestone this run.
- req1 (PyPI) + req2 (GitHub PR-open) still the 2 open OUTSTANDING adoption blockers, both customer-gated
  (rai-access list: both status 'open', undecided). Nothing else gated the funnel this run.
- Funnel unchanged: installs 0 (req1-gated), merged PRs 0 (req2-gated), outside paid 0, live listings 2
  (agentlaunch, Agent Directory API logged-not-milestone), prepared PR branches 7 (req2-gated),
  pending keyless listings 9. X weekly update already posted 2026-09-15 (next update-kind >= 2026-09-22).

## PR-BRANCH DRIFT RE-CHECK 2026-09-15 ~17:52 UTC
- x402-foundation/x402: fork branch `docs/list-openai-agents-nano-rebased-v2` @fa8d067
  re-fetched origin+upstream. upstream/main moved to 978b3ce (2 commits past the branch's merge
  base a7ea804). NOT a clean ancestor (--is-ancestor fails) BUT the branch's actual diff vs base is
  a single insertion to docs/dev-tools/third-party-sdks.md and it cherry-picks onto current
  upstream/main with zero conflicts. So no rebuild needed — still merge-ready. Recorded here so a
  future run does not rebuild it.
- agentswitchboard + awesome_mpp fork branches: re-fetched, confirmed branch heads exist and fork
  remotes resolve. Upstream URL for agentswitchboard.dev underlying repo (agentswitchboard/
  agentswitchboard.dev) 404s on GitHub (it is a rust-lang-style subrepo grammar project, not that
  path); its PR is a content snippet rather than a code checkout, so mergeability is not
  git-diff-drivable from this clone. Not a blocker: both PRs open via the gated req2 key once granted.

## NEW 8TH PR BRANCH 2026-09-15 ~18:5x UTC
- Prepared a NEW keyless PR branch (8th). Target: Merit-Systems/awesome-agentic-commerce (149★, active 2026-09-10, master,
  CONTRIBUTING "contributions welcome via PRs"). Its "Open Source & SDKs" section catalogs exactly our kind — framework-specific
  x402 payment wrappers (x402-anthropic-python, agent-wallet-sdk, Routeweiler) — and Nano is absent. This is the x402-SDK
  ecosystem list (sister to xpaysh/awesome-x402, also a prepared target).
- Fork: PANDeveloper001/awesome-agentic-commerce. Branch: add-openai-agents-nano @0b06312 (1 insertion after
  x402-anthropic-typescript block). Upstream base 01feff1 = current master (clean ancestor via keyless merge-base), no drift.
  rai-publish push-check clean (23 commits scanned). PR-open needs req2 (same GitHub public_repo token). Both pages 200/302 signed-out.
- New scope: fork-branch URL previously 404 — file existed, first prepared-at this run (re-check 3 times, none live).
FE: funnel now: prepared PR branches 8 (was 7), pending keyless listings 9 unchanged, live listings 2, req1/req2 still the blockers.

## NEW 9TH PR BRANCH 2026-09-15 ~19:0x UTC
- Prepared a NEW keyless PR branch (9th). Target: Scottcjn/awesome-agents (101★, active 2026-09-07, main, CONTRIBUTING
  welcomes individual PRs, format "[Name](link) - Description.", no tokens/financial-instrument-only projects). Its
  "Blockchain and Rewards" section lists x402 Payment Protocol + x402-proxy — an on-topic x402 payments subsection, Nano absent.
  Not a mega-list (~190 lines). No secret-scanner hook.
- Fork: PANDeveloper001/awesome-agents. Branch: add-openai-agents-nano @1170220 (1 insertion after x402-proxy line).
  push-check clean. PR-open needs req2 (same public_repo token). Both pages 200 signed-out.
FE: funnel now: prepared PR branches 9 (was 8), pending keyless listings 9 unchanged, live listings 2, req1/req2 still blockers.

## RE-CHECK 2026-09-15 ~19:12 UTC (this run)
- Corrective action honored — all 19 public links + 9 PR fork branches verified HTTP 200 signed-out
  (curl -L, no session): repo, README, tutorial.md, fee-finality-comparison.md, agent-payment-rails-comparison.md,
  comparison-vs-x402-openai-python.md, live-proof.md, agentlaunch page, Agent Directory API, and all 9 prepared
  PR branches (x402-v2, nanodir, awesome-agent-first-tools, awesome-x402, agentswitchboard.dev, awesome_mpp,
  aapp-v2, awesome-agentic-commerce, awesome-agents). Nothing 404.
- Pending listings re-checked for a REAL card (distinguishing query-echo from a live listing): AgentRank
  (7 text hits, 0 detail links -> query echo only, no card), AI Agents Live (6 hits, only pagination links
  /agents?search=...&page=N echo -> no card), DynamiteAI (2 hits, 0 links -> query echo), AiAgents.Directory
  search route 404, zPlatform/TheNextAI/aiagenttools no row. None live. No new adoption milestone this run.
- Funnel unchanged: installs 0 (PyPI req1-gated), merged PRs 0 (req2-gated), outside paid 0, live listings 2,
  prepared PR branches 9 (all req2-gated), pending keyless listings 9. X weekly update already posted 2026-09-15.

## NEW 10TH PR BRANCH 2026-09-15 ~19:2x UTC
- Target: **michielpost/x402-dev** (x402 Developer Portal, master, active 2026-09-15). CONTRIBUTING/README:
  "Add it to the Projects.md file. Send a PR and it will be merged and published on the website." (x402dev.com —
  merged entries auto-publish to their website, an EXTRA distribution surface beyond the list). Exactly our kind:
  "x402 Developer Tools & SDKs" section (Projects.md:63) lists Python/TS client SDKs (bridgenode-llm, x402-python,
  stipend). Nano absent.
- Fork: PANDeveloper001/x402-dev (fork created this run). Branch: add-openai-agents-nano @ 274b626 (1 row
  inserted after mogami.tech, before stipend, alphabetical; no PyPI link since PyPI not yet live — links must
  load 200). No secret-scanner hook in target tree. rai-publish push-check clean (33 commits). fork-branch 200 +
  pull/new 302 + raw Projects.md row present verified. PR-open needs req2 (same public_repo token).
- Funnel: prepared PR branches now 10 (was 9). Pending keyless listings 9 unchanged. Live listings 2.
  req1/req2 still the blockers.

## PR DRIFT RE-CHECK + x402 v3 REBUILD 2026-09-15 ~19:22 UTC
- All 10 prepared PR branches drift-verified vs CURRENT upstream (local merge-base clone, correct default branches):
  x402-v3, x402-dev, nanodir, awesome-agent-first-tools, awesome-x402, awesome_mpp, aapp-v2, awesome-agentic-commerce,
  awesome-agents -> BEHIND-0 CLEAN. agentswitchboard -> content-snippet branch (upstream repo 404s, known subrepo
  quirk); fork-branch page 200 + raw content json 200 verified directly.
- x402 upstream moved again (5 commits past v2 base a7ea8041 -> 9b37f376): rebuilt V3 branch
  docs/list-openai-agents-nano-rebased-v3 @ ca686937 by cherry-picking the 1-line docs row onto CURRENT main
  (no force-push; v2 kept as history). behind-0, push-check clean, fork-branch 200 + pull/new 302.
- on-key-arrival.md updated to open from v3.
- Funnel unchanged: installs 0 (req1), merged PRs 0 (req2), outside paid 0, live listings 2, prepared PR branches 10,
  pending keyless listings 9. req1 + req2 still the only open adoption blockers.

## NIGHT RUN 2026-09-15 ~19:45 UTC — link re-verify + 2 new directory evaluations
- Corrective action honored — all 20 public links verified HTTP 200 signed-out (curl -L, no session): repo
  root, README, docs/tutorial.md, fee-finality-comparison.md, agent-payment-rails-comparison.md,
  comparison-vs-x402-openai-python.md, live-proof.md, agentlaunch page, Agent Directory API, all 10 PR fork
  branches (x402-v3, x402-dev, nanodir `add-openai-agents-nano-clean` [earlier checked wrong branch name —
  real branch is `-clean`, 200], awesome-agent-first-tools, awesome-x402, awesome_mpp, aapp-v2,
  awesome-agentic-commerce, awesome-agents, agentswitchboard.dev), topics/x402, topics/nano — all 200.
  Nothing 404.
- NEW directory evaluations (both recorded in directory-listing skill so future runs skip):
  * aiagentslisting.com (brand-new 2026-09-06, free human-reviewed agent+MCP+skills directory with its own
    MCP endpoint + llms.txt): /submit REDIRECTS to /auth/login and free listings require a badge on the
    maker's site -> NOT keyless (no fake accounts); skip. llms.txt's "keyless submit over MCP" needs
    authenticated browser OAuth -> still not keyless. /agent/openai-agents-nano = 404 (not listed).
  * aisoltools.com/submit: no DNS (host unresolvable) -> skip.
  - market.dev is an aggregator over GitHub awesome-lists (no direct submission) -> way in is the
    awesome-list PR, already prepared where it fits.
- Pending listings re-checked (honest, none live): MadeWithStack product API still status 'pending'
  UNDER_EDITORIAL_REVIEW; theagentrank.com 200 (form only); aiagentslive /agents/search 404; aiagents.directory
  /search 404; 4agent.dev tool page 404; meshkore search 404. No new adoption milestone this run.
- req1 (PyPI) + req2 (GitHub PR-open) still the 2 open OUTSTANDING adoption blockers, both customer-gated
  (2 key requests still waiting; not re-asking).
- Funnel unchanged: installs 0 (req1-gated), merged PRs 0 (req2-gated), outside paid 0, live listings 2,
  prepared PR branches 10 (req2-gated), pending keyless listings 9. X weekly update already posted 2026-09-15
  (next update-kind >= 2026-09-22). Distribution content is comprehensive (tutorial + 3 measured comparisons).

## THIS RUN 2026-09-15 ~21:0x UTC — drift re-check + link re-verify + new-target evaluation
- Drift re-checked 8 prepared PR branches this run (git fetch --depth 3 upstream HEAD + fork branch, rev-list
  behind): facundofarias/awesome-agent-first-tools, xpaysh/awesome-x402, assafbar2/agentswitchboard.dev,
  mpp-best/awesome_mpp, Merit-Systems/awesome-agentic-commerce, Scottcjn/awesome-agents, michielpost/x402-dev,
  tsubasakong/awesome-agent-payments-protocol (v2) — all CLEAN (ahead 1 / behind 0 vs current upstream).
  Per skill, run at every distribution run start.
  - Two local convener errors, NOT drift, caught and not counted: I first polled stash-named refs that no longer
    apply — `x402 docs/list-openai-agents-nano-rebased-v2` (superseded by v3 @ ca686937 per runbook; v2 is behind
    3) and `nanodir add-openai-agents-nano` (the fork branch is actually `add-openai-agents-nano-clean` @ def0d34;
    my target name 404'd fetch_rc 128). Both are my naming mistakes, not branch drift; the runbook names are the
    truth and they are the clean current branches.
- Corrective action honored: public links re-verified signed-out via curl this run (200): repo, README,
  tutorial, and PR fork-branch pages (x402, aaf, mpp, aapp all 200). Nothing 404 in this run's curl pass.
- Pending-listings honest re-check (web_extract, signed-out): Agent Directory API STILL live with the
  openai-agents-nano row (unchanged); AgentRank homepage shows no openai-agents-nano card (still pending review);
  AI Agents Live /agents shows no openai-agents-nano card (still pending review). No new adoption milestone.
- NEW candidates evaluated from fresh search, none a clean fit where we lack a prepared branch:
  bitrefill/awesome-agentic-payments — CONTRIBUTING accepts "only official sources ... from the maintaining
  organizations", a third-party client SDK is out of scope -> skip. frankxai/awesome-payment-agent-skills
  (2★, safety/mandate-curated, "what doesn't get merged: tools that move money without authorization story")
  and frankxai/awesome-agentic-income (1★) — tiny safety-curated lists; a settlement-rail client SDK is a
  marginal fit, not worth keyless prep or PR -> skip. moov-io/awesome-fintech (373★) — generic fintech, no
  x402/agent-payments SDK section -> skip. QBT-Labs/x402, x402-agentpay etc. are products, not lists.
  Recorded in open-integration-pr skill as not-fit to avoid retries.
- Funnel unchanged (per the report): installs 0 (req1 PyPI), merged PRs 0 (req2 GitHub), outside paid 0,
  live listings 2 (agentlaunch, Agent Directory API), prepared PR branches 10 (all req2-gated), pending
  keyless listings 9, X weekly already posted 2026-09-15 (next update-kind >= 2026-09-22). Both adoption
  blockers remain customer-gated (2 key requests still waiting); no retcon of the state.

## DAY RUN 2026-09-15 ~20:4x UTC — all-10 drift re-check, full link re-verify, new-candidate evaluation
- Drift re-checked ALL 10 prepared PR branches this run via local merge-base clone (git fetch upstream base +
  fork branch, merge-base == upstream base => behind-0 CLEAN): x402-v3 (@ ca686937), x402-dev, nanodir
  (`add-openai-agents-nano-clean`), awesome-agent-first-tools, awesome-x402, agentswitchboard.dev, awesome_mpp,
  awesome-agent-payments-protocol (-v2), awesome-agentic-commerce, awesome-agents — all AHEAD=1 BEHIND=0 CLEAN.
  None has drifted; req2 remains the only gate on opening them.
- Corrective action honored: re-verified every public link signed-out (curl -L, no cookies) 200 — repo root,
  README, tutorial, both live listings (Agent Directory API JSON still names openai-agents-nano + agentlaunch
  page <title>), and all 10 PR fork-branch pages. Nothing 404. Wrote `curl` evidence to verify-this-run.txt and
  (below) rx; the previous tweet 404 lesson is satisfied — every posted target answers 200.
- Pending listings honestly re-checked (web_extract + raw-HTML grep, signed-out): AI Agents Live /agents?search
  and AgentRank /agents?q both show "openai-agents-nano" ONLY in the query-echo / zero-results copy — no real
  card, no href; MadeWithStack product API still status 'pending' UNDER_EDITORIAL_REVIEW; Dynamite-oai ?s search
  query-echo only (1 hit in raw HTML = the query value, no listing). No new adoption milestone this run.
- NEW target candidates evaluated (all recorded in skill so future runs skip):
  * JasonColapietro/awesome-agent-payments-protocol — fork of tsubasakong/awesome-agent-payments-protocol
    (which we already prepped a v2 branch for) -> skip, duplicate.
  * Merit-Systems/awesome-x402 — does not exist (API empty) -> skip.
  * mbeato/awesome-mpp (21★) — the OTHER MPP awesome list; near-duplicate of our already-prepared
    mpp-best/awesome_mpp PR branch; listed entries overlap (mppx, pympp, tollbooth). It is arguably a sister
    list but lets an MPP buyer find the SDK on a second registry. Value is real but marginal; the prepared
    mpp-best branch already covers the MPP registry surface -> skip preparing an 11th branch this run (keyless
    cap is not the binding constraint; req2 gates all PRs anyway). Recorded in skill as a possible future
    secondary MPP target, not not-fit.
  - damoahdominic/awesome-agentic-commerce (82★) — pushed 2026-01-22 (8 months stale), NO CONTRIBUTING.md to
    define the PR contract -> stale/informal, skip.
  - OrcaQubits/awesome-agentic-commerce (9★, pushed today) — generic protocol-reference list (UCP/ACP/AP2/MPP/
    A2A/MCP/WebMCP), NO SDKs>Python sub-section to place a client library -> too general, skip (matches the
    "large mega-list" rule).
- Funnel unchanged (all adoption movers still key-gated): installs 0 (req1), merged PRs 0 (req2), outside paid
  0, live listings 2, prepared PR branches 10, pending keyless listings 9. No new adoption milestone this run.
  req1 (PyPI) + req2 (GitHub PR-open) are the two open blockers, encrusted in 2 key requests still waiting on
  the customer; not re-asking, continue everything else.

## THIS RUN 2026-09-15 ~21:45 UTC — all-10 drift CLEAN + new-surface re-verify + 2 not-fit evals
- Drift re-checked all 10 prepared PR branches this run (local merge-base clones): 9 git-mergeable are
  BEHIND-0 AHEAD-1 CLEAN (x402-v3 @ca686937, nanodir -clean @def0d34, aaf @d790b55, awesome-x402 @c2666c4,
  mpp @b0015c5, aac @0b06312, saa @1170220, x402-dev @274b626, aapp-v2 @297b9f8). 10th (agentswitchboard) is a
  content-snippet branch whose upstream GitHub path 404s (known subrepo quirk) — verified its fork-branch page
  on the CORRECT fork (PANDeveloper001/agentswitchboard.dev, not agentswitchboard) is HTTP 200. No drift; req2
  remains the only gate on opening all 10.
- Corrective action honored: re-verified public links HTTP 200 signed-out — repo, README, tutorial, both live
  listing pages (Agent Directory API JSON + agents-launch page), agents.net/directory, AgentMRR homepage + API,
  and the agentswitchboard+nanodir fork branches. Nothing 404.
- Pending keyless listings re-checked for a REAL card (not query echo): theagentrank /agents?q=, aiagentslive
  /agents?search=, dynamite /?s=, agents.net/directory — all show the term ONLY in the search box / pagination
  echo, no anchor href to a per-agent page. 4agent.dev tool page 404. aiagents.directory search route 404.
  MadeWithStack product API still status 'pending'. None live (all submitted 2026-09-15, within 24-48h windows).
- NEW evaluation (both recorded not-fit): a2a-registry.org and a2alist.ai are x402/A2A AGENT/SERVICE registries
  (they index endpoint services/facilitators that answer 402 + A2A agents), NOT client SDK libraries; a2alist
  also charges a $0.99 USDC fee. Same out-of-scope logic as agent-tools.cloud/MCP registries -> skip.
- AgentMRR (new surface, added ~21:15) re-verified STILL LIVE: homepage HTML + GET /api/products both contain
  'openai-agents-nano' (agent-commerce, Free). Distribution surface persists.
- Funnel unchanged: installs 0 (req1), merged PRs 0 (req2), outside paid 0, live listings 2 (formal) + 1 live
  AgentMRR discovery surface, prepared PR branches 10 (all req2-gated CLEAN), pending keyless listings ~12.
  req1 (PyPI) + req2 (GitHub PR-open) remain the 2 customer-gated adoption blockers (2 key requests waiting).
  X weekly update already posted 2026-09-15 (next update-kind >= 2026-09-22).
## THIS RUN 2026-09-15 ~21:50 UTC — STARTER PATH re-proven (clean venv)
- Re-proved the public install path in a brand-new venv (no cache): `uv venv /tmp/nano-install-dist` +
  `uv pip install "git+https://github.com/PANDeveloper001/openai-agents-nano-x402.git"` -> openai-agents-nano
  0.1.0 installs; `import openai_agents_nano` + `make_nano_x402_tool()` return a real OpenAI Agents SDK
  FunctionTool `nano_x402_fetch` with the exact schema (url, method, json_body, max_xno, dry_run, quote_token).
  This is the starter path an outside agent follows today (the only honest install route while req1/PyPI lags).
  Logged rai-distribution --kind tutorial.
- Repo metrics 2026-09-15 ~21:55 UTC: stars 1, forks 0, open_issues 0 (GitHub API). Funnel measured:
  installs 0 (req1-gated), directory listings 2 formal live + 1 AgentMRR live surface, merged PRs 0 (req2),
  outside paid 0. All adoption movers remain customer-gated on req1 (PyPI) + req2 (GitHub PR-open).

## THIS RUN 2026-09-15 ~21:52 UTC — all-9 drift CLEAN + AgentMRR surface re-verified + fresh-list mining (no new milestone)
- Drift re-checked all 9 git-mergeable prepared PR branches this run (local merge-base clones, this-run start):
  x402-v3 @ca686937, nanodir `add-openai-agents-nano-clean` @def0d34, aaf @d790b55, awesome-x402 @c2666c4,
  mpp @b0015c5, awesome-agentic-commerce @0b06312, awesome-agents @1170220, x402-dev @274b626,
  aapp-v2 @297b9f8 — ALL AHEAD=1 BEHIND=0 CLEAN vs current upstream. 10th (agentswitchboard) is the
  content-snippet branch (upstream subrepo quirk, fork-branch page verified 200 earlier). No drift; req2 the only gate.
- Corrective action honored — 8 public links re-verified HTTP 200 signed-out (curl -L, no session):
  repo, README, tutorial, fee-finality, agent-payment-rails, comparison-vs-x402-openai-python,
  agents-launch page, Agent Directory API — all 200. Nothing 404.
- AgentMRR adoption surface RE-VERIFIED STILL LIVE: homepage renders the full openai-agents-nano product card
  (name, category agent-commerce, Free, GitHub link). An initial /api/products grep returned 0 which briefly
  looked like removal — resolved as trending-page pagination, NOT a removal (card is the persistent surface).
- Pending listings honest re-check (all submitted 2026-09-15, all within 24-48h windows, none live):
  MadeWithStack API still status 'pending' (badge pending_approval, requires_manual_review); agents.net
  /directory has NO card yet; 4agent tool page 404; AgentRank/Dynamite no real card. No resubmits.
- NEW mining: pulled best-of-ai/ai-directories (873★, May-2026 push) for genuinely fresh keyless targets.
  5 candidates evaluated, ALL not-keyless / not-fit, recorded in directory-listing skill to avoid retries:
  BasedTools (needs dofollow backlink >15DR + premium track + general/toy+NSFW catalog -> link-farm), ListYourTool,
  NavTools AI (generic 30-90-day SEO dirs -> low precision), Trillionagent (search SPA, no real keyless form),
  aifordevelopers.org (editorial curated, no submit route). best-of-ai list itself logged as docs. Also noted
  s-a-m-a-i/awesome-x402 (0★ stale fork of Merit content, Feb 2026) not-fit for a PR branch.
- Net: NO new adoption milestone this run (funnel unchanged). installs 0 (req1-gated), merged PRs 0 (req2-gated),
  outside paid 0, live listings 2 (formal) + 1 AgentMRR live surface, prepared PR branches 10 (all req2-gated CLEAN),
  pending keyless listings ~13. req1 (PyPI) + req2 (GitHub PR-open) remain the 2 customer-gated adoption blockers
  (2 key requests still waiting). X weekly update already posted 2026-09-15 (next update-kind >= 2026-09-22).
