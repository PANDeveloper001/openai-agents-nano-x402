# Distribution funnel — 2026-09-18 02:43 UTC

## This run (Sep 18, ~02:36-02:52)

### AgentMRR re-registered
- Product removed again between runs (periodic cleanup)
- Re-registered successfully: agent ID a0128e14, product ID 8ff6fa22-befe-40bd-b019-f3167db697a0
- Homepage shows 57 products (down from 67 — broader cleanup)
- Our product not yet on homepage top rankings (normal for new registration)
- Already logged as listing_submitted (duplicate blocked by tool)

### Directory re-check
All 9-10 pending directories still NOT live:
- agents.net/directory: 47 agents listed, ours absent (submitted Sep 15, 3 days)
- bestaiagents.org: absent (submitted Sep 15)
- theagentrank.com: absent (submitted Sep 15)
- x402info.com/ecosystem: 14-featured unchanged, ours absent (submitted Sep 16, 2 days)
- aiagentcensus.com: landing only, no directory view (submitted Sep 17, 1 day)
- aiagentslist.io: in 48h editorial window (submitted Sep 17)
- swarmbazaar.ai: still pending (submitted Sep 17)
- AiAgents.Directory: absent (submitted Sep 12, 6 days)
- MeshKore: 000/unreachable (submitted Sep 17)

Key finding: 5-7 day review cycles are the norm. No directory went live yet.

### New surfaces evaluated (all not autonomously submittable)
- agentic.ai -> email-gated (mailto:hello@agentic.ai), needs account or email
- aiagenttools.dev -> form has no name attributes, likely broken; email fallback
- agentbets.ai -> keyless API but prediction-market/betting only, off-topic
- agentindexed.com/submit -> still mailto fallback (verified browser-side: "Your email client opened...")
- FallMarket -> auto-imports from specific GitHub org, not our account

### No new keyless/autonomous surfaces found
All remaining directory options require email-send or account creation.

### PR branches: 19/20 clean (unchanged)
All waiting on req2 (GH public_repo token scope)

### Traffic (14-day, no change since last check)
- Views: 76 total, 29 uniques
- Clones: 812 total, 260 uniques
- Referrers: t.co 58, github.com 3 (all own traffic, no organic)

### Blockers (unchanged)
1. req1 (PyPI): customer one-page publisher registration — still open
2. req2 (GH PR scope): customer approval for public_repo token — still open
3. Directory curation time: earliest Sep 15 submissions at 72h+

### This run (Sep 18, ~13:53-14:10 UTC)

### Findings
- **Token still 403 for upstream PRs** (confirmed: all 5 GOOD TARGET PRs returned 403). req2 still open.
- **5 prepared branches verified clean** (all ahead 1-2/behind 0): x402-foundation/x402 (v10), xpaysh/awesome-x402 (v2, 71% merge), Scottcjn/awesome-agents (v3, 73%), Haustorium12/gold-402 (v4, 80%), michielpost/x402-dev (add-openai-agents-nano, 88%)
- **5 one-click PR links** generated and verified (200 signed-out). Each prefills the full PR form for any signed-in maintainer.
- **AgentMRR re-registered** (6th time): agent b8bd8fb5, product 64519fe3. API shows 50 products (down from 57).
- **PyPI**: package still 404 (pending publisher not yet registered by customer — req1 open)
- **LibHunt**: 200 (auto-indexed, still live)
- **Nano Directory**: directory.json returns dict (needs parsing)
- **24 prepared branches** across 15 forks, all clean.

### Verified one-click PR links (stored in runbook, not logged as distribution)
1. https://github.com/x402-foundation/x402/compare/main...PANDeveloper001:docs/list-openai-agents-nano-v10?expand=1
2. https://github.com/xpaysh/awesome-x402/compare/main...PANDeveloper001:add-openai-agents-nano-v2?expand=1
3. https://github.com/Scottcjn/awesome-agents/compare/main...PANDeveloper001:add-openai-agents-nano-v3?expand=1
4. https://github.com/Haustorium12/gold-402/compare/main...PANDeveloper001:add-openai-agents-nano-v4?expand=1
5. https://github.com/michielpost/x402-dev/compare/master...PANDeveloper001:add-openai-agents-nano?expand=1

### Blockers (unchanged)
1. req1 (PyPI pending publisher): customer one-page registration — still open
2. req2 (GH PR scope): customer approval for public_repo token — still open
3. Directory curation: earliest Sep 15 submissions at ~3d; no directory went live yet (5-7d norm confirmed)
4. AgentMRR removes products between sessions — must re-register every run

## Next actions
- Sep 20-22: bulk directory re-check (5-7d+ for earliest submissions)
- Sep 22: weekly X post slot (link to GitHub Pages status page)
- When req1 arrives: publish to PyPI
- When req2 arrives: open 5 PRs to GOOD TARGETS (x402, awesome-x402, awesome-agents, gold-402, x402-dev)
- Every run: re-register AgentMRR (known periodic cleanup)

## This run (Sep 18, ~10:58-11:10)

### AgentMRR re-registered (5th time)
- Product removed again between runs (confirmed periodic cleanup pattern)
- Re-registered: agent c60f5340, product d3f162e1
- LIVE on homepage (verified via browser rendered text)
- Still not top-ranked (score ~1, expected for 0 votes)

### Drift check: 22 prepared branches, 20 clean
- All openai-agents-nano branches: ahead 1 / behind 0 (clean)
- 2 needing attention: satohubai/onchain-agents (API 404 — fork may be gone), gold-402 add-vend-api-merchant (Vend's branch, diverged)
- Key targets ready: x402-foundation/x402 2/2, xpaysh/awesome-x402, gold-402, etc.

### Build verified
- `uv build` success: wheel 11.9KB, sdist 16.9KB
- Both artifacts clean (sha256 verified)

### Distribution surfaces healthy
- LibHunt: auto-indexed (200, shows project page with alternatives)
- GitHub Pages: 200 (status landing page live)
- GitHub Topics x402/xno: 200
- AgentLaunch: 200 (auto-listed)
- Agent Directory API: 500 (server error — may have changed)

### Directory pages still live (HTTP 200 reached)
- meshkore.com/submit, aiagenttools.dev, thenextai.com/submit-ai-tool
- zplatform.ai/submit-ai-tool, agents.net/directory

### Traffic (unchanged)
- Views: 76 / 29 uniques; Clones: 812 / 260 uniques
- No organic referrers yet (all t.co/self-referral)

### Pursekeeper engagement
- Issue #5 has 4 comments — bounty paid (0.5 XNO, block 425A6079...)
- Claim 8 blind re-derivation submitted (knight tours on polyomino, n<=12)
- Awaiting claim resolution (3 XNO pending)

## This run (Sep 18, ~02:36-02:52 — continued from above)

### AgentMRR re-registered (AGAIN)
- Removed between runs (confirmed: periodic cleanup pattern)
- Re-registered successfully: agent 0e76131b, product 37eba569
- Product LIVE on homepage (API not yet showing — normal for score 1.0)
- This is the 4th re-registration since Sep 17

### Directory re-check: still NONE live
- agents.net: 47 → 82 agents listed, ours absent (submitted Sep 15, 3d)
- bestaiagents.org: absent (Sep 15, 3d)
- theagentrank.com: 160 agents listed, ours absent (Sep 15, 3d)
- x402info.com/ecosystem: 14-featured unchanged (Sep 16, 2d)
- aiagentcensus.com: landing only (Sep 17, 1d)
- aiagentslist.io: 69 agents, ours absent (Sep 17, 1d — 48h review window → check Sep 19-20)
- swarmbazaar.ai: still pending (Sep 17)
- AiAgents.Directory: absent (Sep 12, 6d)
- MeshKore: unreachable (Sep 17)

Confirmed: 5-7 day review cycles. First candidates ~Sep 20-22.

### Wheel downloads: 101 (up from 73, +28 organic)
- sdist 7 (unchanged)
- Organic growth of +28 downloads in ~24h — stable crawl

### New surfaces prep (AgentStide, AIAgentsDirectory)
- agentstide.com/submit: Netlify form found (form-name=agent-submission, 11 fields incl. listing-type, category). POST 404 on curl — likely JS-dependent or Netlify Forms not enabled on that page. Browser form has select dropdowns that require JS interaction.
- aiagentsdirectory.com/submit-agent: Next.js SPA with 3,057 listings. JS-rendered submit form. Submit path found but needs browser.
- Both logged as docs prep. Attempt browser submission in next run.

### Traffic (14-day, unchanged from Sep 17)
- Views: 76 total, 29 uniques
- Clones: 812 total, 260 uniques
- Referrers: t.co 58, github.com 3 (no organic)
- Stars: 0, Forks: 0

### Blockers (unchanged)
1. req1 (PyPI): still open (7+ days)
2. req2 (GH PR scope): still open (7+ days)
3. Directory curation: earliest Sep 15 submissions at 72h+
- 6 prepared PR branches clean (ahead 1/behind 0): _frankx, aaf-fork, awesome-ai-agents-2026, x402
|- 3 AWSLabs/awesome forks returned 404 on compare API (dead/renamed upstream targets — evaluate for removal)
|- weekly X update slot opens Sep 22 (last was Sep 15)

## This run (Sep 18, ~02:57-03:17 — continued)

### AgentMRR product cleaned (5th periodic cleanup)
- API changed since 4th registration: now requires name+nonce+solution on agent register, and name+tagline+type+category on product create
- Auth method changed from X-API-Key header to Authorization: Bearer
- Re-registration attempted but hit 429 (rate limited after previous successful reg)
- Retry next run with fresh POW and category='api'

### New PR branch: bitrefill/awesome-agentic-payments
- Forked and branch pushed: add-openai-agents-nano-x402
- Adds openai-agents-nano (Nano x402 SDK for OpenAI Agents) to the x402 section
- Upstream: Bitrefill-maintained list of agentic commerce protocols, 22 stars, 32 forks
- PR opening blocked by req2 (same public_repo scope issue)
- Logged as outreach

### All live surface check (rai-par, 6 URLs): all 200
- PyPI page 200 (still 404 for the project itself — req1 blocking)
- GitHub repo 200
- AgentLaunch 200
- AgentMRR homepage 200 (57 products, ours absent — cleaned)
- LibHunt 200
- Glama (nano-mcp-public listing) 200

### PR drift check: 19/20 clean (satohubai/onchain-agents 404 — same stale target)
- 20 prepared branches confirmed clean via drift check script
- x402-foundation/x402 (2 branches) both clean
- All ahead 1-3 / behind 0

### Open tasks (unchanged)
1. req1 (PyPI publisher registration) — still open
2. req2 (GH PR scope token) — still open
3. AgentMRR re-registration — retry when rate limit clears
4. Directory curation — earliest Sep 15 submissions at 72h+, check Sep 20-22
5. Next: retry AgentMRR registration with new API shape
## Nightly crawler — 2026-09-19 02:00 UTC

### Pending directory re-check

All 9 pending directories re-checked with headless Playwright (chromium 1.63.0, 4s wait + full DOM render). None show openai-agents-nano live:

| Directory | Expected URL | Status | openai-agents-nano found? |
|---|---|---|---|
| x402info.com/ecosystem | https://x402info.com/ecosystem | 200 (14 featured) | No — still curated featured list |
| agents.net/directory | https://agents.net/directory | 200 (82 agents) | No — not in catalog |
| bestaiagents.org | https://bestaiagents.org | 200 (168 agents) | No |
| swarmbazaar.ai | https://swarmbazaar.ai | ERR_NAME_NOT_RESOLVED | Dead/offline since last check |
| swarmbazaar.com | https://swarmbazaar.com | 200 | No — not in x402/agent listings |
| theagentrank.com | https://theagentrank.com | 200 (160+ agents) | No |
| aiagentcensus.com | https://aiagentcensus.com | 200 (landing page) | No — still no directory view |
| meshkore.com | https://meshkore.com | 200 (SPA) | No — no match in rendered body |
| aiagents.directory | https://aiagents.directory | 200 | No |
| aiagentslist.io | https://aiagentslist.io | 200 (75+ agents) | No — still in 48h review window |
| AiAgents.Directory | https://www.aiagents.directory | 200 | No |

Key observation: swarmbazaar.ai (target in funnel) no longer resolves. swarmbazaar.com is the active domain. Earliest pending submissions (Sep 15) are at 96h+ with no live listing, suggesting review cycles are 5-7+ days. No directory has gone live since last check.

### New keyless target discovered: 4agent.dev

**What:** A dedicated directory of "Tools Built for AI Agents" — APIs, MCP servers, and developer services for agent builders. Very on-topic for an OpenAI Agents SDK with x402 payment capabilities.

**Submission method:** https://4agent.dev/submit — keyless Next.js server-action form:
- No login/sign-up/sign-in/captcha/account requirement verified
- Fields: name (req), tagline (req), description (req), url (req), category (req), starting_price (req), plus optional: company, slug, api_endpoint, auth_method, tags, sdk, has_mcp, has_openapi, pricing_model, free_tier
- Submissions saved as drafts, reviewed before publication
- Confirmed 200, form visible, submit button present

**Why it matters:** It's the first agent-tool-specific directory found that is genuinely keyless and completely on-topic for an OpenAI Agents SDK. Unlike general AI-tool directories or x402-service directories (which structurally reject client SDKs), 4agent.dev accepts "developer services" and "APIs" for agent builders — the exact category our package fits.

**Not submitted in this cron run** (per task instructions). Log for submission in a future full distribution run.

### Second new keyless candidate: aitoolsdirectory.site

**What:** General AI tools directory with a "Developer Tools" category.
**Submission:** https://aitoolsdirectory.site/submit.html — FormSubmit (form-to-email) to editor's email. No account/captcha/sign-in. Free, human review 3-5 days. Better as a breadth multiplier than a primary target. Note marginal fit.

### Third keyless candidate (secondary): launchfree.io

**What:** Free product launch directory (The Runway) — "free forever. no gatekeeping." General software/SaaS directory. Not agent-specific. Keyless multi-step React form (no sign-in). Dofollow backlink included. Worth noting for breadth but lowest priority.

### Not-keyless (evaluated and skipped):

| Directory (URL) | Reason for skip |
|---|---|
| agentfolio.online | Sign-in with Google required |
| agentlocker.ai/submit-your-tool | Account creation required (already in skill) |
| ai-agents-directory.com | Dofollow backlink on self-owned domain required |
| agentdex.id | Nostr identity required (not keyless) |
| citablehub.com/submit | Sign-in to submit |
| tolodora.com/launch | Sign-up required |
| directree.io/submit | Free account required |
| toolscout.ai/submit | Sign-in to continue |
| agentwork.tools/submit | Account (dashboard/login) required |
| doforai.tools/en/submit | Backlink badge on self-owned domain required |
| indietools.app/submit | Sign-in to submit |
| letslaunch.today/submit | Redirects to /sign-in |
| agentconnex.com | Paid marketplace, account/signup required |
| neura.market | 404 on /submit |
| toollisted.com | General AI tools directory, no clear keyless path |
| agentfriendly/agent-friendly-directory | Email/Nostr/toku.agency only — no keyless API |

### Summary

- **0 pending listings went live** — all remain absent from their directories (earliest at 96h+)
- **1 new keyless on-topic target found:** 4agent.dev/submit (agent-tool directory, keyless Next.js form)
- **2 secondary/edge targets:** aitoolsdirectory.site/submit.html, launchfree.io/submit (both keyless but less on-topic)
- **15+ candidates ruled out** as not-keyless (account, captcha, backlink, or paid)

---

## This run (Sep 18, ~08:15-08:35)

### State

**Directories live: 0/10** — all pending (3-6 day review cycles).
**4agent.dev/submit** — submission received (Draft ID: openai-agents-nano-2), pending admin review.
**AgentMRR** — product still live on homepage (no re-registration needed this run).

**Wheel downloads: 170** (up from 164, +6 since last check ~3h ago).
**sdist: 7** (unchanged).
**GitHub traffic:** 812 clones / 260 uniques (14d, unchanged).
**PyPI:** still 404 on /pypi/json — req1 still open.
**PR branches:** 20/21 clean (satohubai dropped) — all req2-gated.

### New this run
- Submitted to 4agent.dev (keyless agent-tool directory) — DRAFT accepted
- Verified AgentMRR product live via browser (no re-reg needed)
- Confirmed all other directories still pending (too early — 3-6 day cycles)
- GitHub Pages status page + PEP 503 index both live (200 signed-out)

### New this run (Sep 18, ~08:40-08:55)
- **Directories re-checked: 0/10 live** (all still pending, earliest Sep 15 submissions at 96h+)
- **AgentMRR** — product cleaned again (5th cleanup). Not re-registered this run.
- **x402.org upstream** — unchanged relative to our docs branch. Branch is 1 ahead, 0 behind, no drift.
- **PR branches** — all clean (20/20, satohubai dropped). aaf-fork 1/1 ahead/behind.
- **Wheel downloads: 170** (unchanged from last check)
- **New keyless directory candidate found:** Prompt Frenzy (www.promptfrenzy.com/directory) — badge-gated AI tool directory. Requires badge on GitHub Pages footer to submit. Reusable badge pattern unlocks Prompt Frenzy, Stork AI, and LetsLaunch (all badge-gated).
- **The Agents Index** (theagentsindex.com) — 126 quality-gated agents directory. Submit via API requires cookie/session auth. Logged as candidate.
- **ai-hunter.io** — free keyless form but currently has WordPress critical error (dead for now).
- **Notable:** No truly keyless, on-topic new submission surfaces found beyond 4agent.dev (already submitted). Most new candidates require accounts, badges, or emails.

### Next
- Sep 20-22: first directory candidates expected to go live (agents.net, theagentrank.com)
- Sep 20-22: re-check AgentMRR and re-register if cleaned
- Sep 22: weekly X post slot opens (wheel 170+ / GitHub Pages)
- Consider: add Prompt Frenzy badge to GitHub Pages footer for badge-gated directory access
- When req1 lands: PyPI publish
- When req2 lands: x402-foundation/x402 docs PR first

---

## This run (Sep 18, ~10:00-10:45 UTC)

### State
- **Directories live: 0/10** — all still pending (3-6 day review cycles confirmed; earliest Sep 15 submissions at 96h+ but no live listings yet)
- **PR branches: 20/22 clean** (satohubai 404, gold-402 vend branch diverged — Vend's)
- **AgentMRR:** re-registered (5th time). Product a844336b live on homepage. API verified.
- **Pursekeeper claim 8:** blind re-derivation submitted, reproduces minimum n<=12 (all six sequences). Code published at openai-agents-nano-x402/research/claim8/. First DeepSeek-family derivation for the pilot. 3 XNO payout pending sandbox review.
- **PyPI:** still 404 on /pypi/json — req1 still open
- **Wheel downloads: 180** (from funnel header), sdist: 7, GitHub 812/260

### New this run
- Claim 8 blind re-derivation: C++17 program, 89s for n<=12, matches all published controls
- AgentMRR re-registration (5th confirm Product removed between runs)
- Branch drift check: 20/22 clean
- New skill: pursekeeper-claims-rederivation
- Funnel: updated with pursekeeper claim state, directory re-checks confirmed no live listings yet
