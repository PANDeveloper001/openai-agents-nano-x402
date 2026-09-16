||| ## THIS RUN 2026-09-16 23:45-23:59 UTC — DISTRIBUTION: drift 15/15, X update capped, 4 new dirs evaluated, funnel recorded

### State at start
- req1 (PyPI pending publisher) and req2 (GH PR scope) still pending customer
- 15 clean PR branches (before: clean)
- 24 listing submissions in review
- X weekly update capped: next slot Sep 22 (7-day limit resets)
- The latest corrective action (stack audit: skip invention phase, no unwind, same-model verify) recorded

### Work done this run
1. **Corrective actions applied**: read corrections.md. The stack audit points out 3 method gaps. DISTRIBUTION FIRST means no building this run — applied the audit as note for when building resumes.
2. **Drift re-check**: all 15 prepared PR branches clean (ahead 1-2, behind 0). Corican/nanodir (ahead 1/behind 0), x402-foundation/x402 (2/2), all others ahead 1-2.
3. **PyPI name check**: free (404 on /json/ and /simple/)
4. **Bazaar Nano count**: 55 accepts, 1 host (pyfile-agent.taile3ff35.ts.net), 16 pages scanned — unchanged
5. **X weekly update**: tried to post via `rai-x post --dry-run` — refused until Sep 22 10:39 UTC (7-day cap). Saved text + link ready: `Fee and finality: Nano (free, 0.3s) vs x402 USDC (capped)` + link to fee-finality-comparison.md
6. **Pending directories re-checked via browser**: TheNextAI (404), zPlatform (DNS error), AgentRank (timeout), AI Agents Live (DNS error), MeshKore (404), agents.net (404) — none published yet. All still in review.
7. **NEW directories evaluated**:
   - aiagentslisting.com (just launched Sep 6 — agents, MCP servers, skills. Next.js SPA, needs browser automation for form.)
   - AgentIndexed (agentindexed.com/submit — "Frameworks & SDKs" category perfect. Next.js SPA.)
   - Vibedonalds (vibedonalds.com/submit — free with reciprocal badge. Not a great fit: for "apps made with AI.")
   - AgentBets.ai (post API no auth, 48h review, but for prediction markets/sports betting — not a fit for payment SDK.)
8. **Dead targets eliminated**: Omnivalent/awesome-x402 (0★, Jun), bido75/awesome-ai-agents-2026 (0★, May), zacfire/awesome-x-for-agents (0★, Mar). All 0-star repos with no PR merges.
9. **Ecosystem health**: awesome_mpp, Scottcjn/awesome-agents, Corican/nanodir still don't list us. Expected (req2).
10. **Access request check**: req1 and req2 still open. No progress from customer.

### Funnel
15 clean PR branches · 24 listing submissions · 27 outreach issues across 22 targets · 1 live marketplace listing (AgentMRR) · 1 keyless directory listing (agents-launch) · 2 live agent-directory listings · 1 x402eco/website fork issue · installs 0 (PyPI req1) · merged 0 (GH PR req2) · outside paid 0 · release wheel downloads 12, sdist 5 · Bazaar nano accepts 55

### Bottlenecks
- req1 (id=1): PyPI trusted publisher registration (owner: pypi.org/manage/projects/openai-agents-nano → settings → publishing)
- req2 (id=2): GitHub PR-open scope token (opens 15 prepared PRs)
- X weekly update: next slot Sep 22 (7-day cap)
- New SPA directories (aiagentslisting, AgentIndexed) need browser automation or email capability

### Next steps for next run
1. Re-check req1/req2 status
2. Re-check pending directories (48h+ now for most)
3. Run drift re-check
4. Verify PyPI name still free
5. Try aiagentslisting.com or AgentIndexed submission via browser automation
6. Look for keylessly-submittable new directories

|||| ## THIS RUN 2026-09-16 23:17-23:45 UTC — DISTRIBUTION: drift check 15/15, X update capped, new dirs evaluated, funnel updated

### State at start
- 2 access requests still open (req1: PyPI pending publisher, req2: GitHub PR scope)
- 15 clean PR branches (verified previous run)
- All 24 listing submissions still in review (24-48h queues)
- X daily cap reached for today (3/3 posts)
- Weekly X update slot free but must wait until tomorrow

### Work done this run
1. Re-checked pending directory listings via browser: TheNextAI (not live), zPlatform (not live), AgentRank (not live), AI Agents Live (not live) — all still pending review as expected. Corrective action said "re-check after 2 days" — these were submitted ~31h ago, still too early.
2. Measured x402nano.org facilitator: deployment disabled (Vercel DEPLOYMENT_DISABLED, returns 402 text/plain but non-functional). Not usable.
3. Confirmed robgilmore26/nanoroute IS a real Nano x402 facilitator (README confirms it, live node at 204.168.181.90:3402 — currently connection refused, may be intermittent or a demo node). NanoRoute settlement engine batch-settles to merchants on L1. Good ecosystem sign.
4. Confirmed PyPI name still free: /pypi/openai-agents-nano/json -> 404
5. Release downloads unchanged (12 wheel, 5 sdist) — no new distribution action since last measurement
6. Compiled status update and saved learning to .ledger/tmp/run-20260916-2.txt

### Funnel
15 clean PR branches · 24 listing submissions · 25 outreach logged · 1 live marketplace listing (AgentMRR) · 1 keyless directory listing (agents-launch) · 2 live agent-directory listings · 1 x402eco/website fork issue requesting addition · installs 0 (PyPI req1) · merged 0 (GitHub PR req2) · outside paid 0 · release wheel downloads 12, sdist 5

### Bottlenecks
- req1 (PyPI trusted publisher) and req2 (GitHub PR scope) — both pending customer action. Three checkable directories still pending 24-48h review.

### Next run
- Post weekly X update (free slot, first thing before daily cap consumed)
- Re-check pending directory listings (most should be live after 48h)
- Run drift re-check on all 15 prepared PR branches
- Check if customer has processed either access request
- Verify PyPI name still free

### State at start
- 15 clean PR branches (all ahead/behind 0)
- 23 outreach issues delivered across 21 targets
- 24 listing submissions (keyless directories and forms)
- PyPI trusted publisher (req1) and GH PR-open scope (req2) still pending
- X daily cap at 3/3 for today; weekly update slot reopens ~Sep 22

### Distribution this run
|4. **Re-verified pending MeshKore/TheNextAI/zPlatform** — resubmissions confirmed still pending (not live). Logged as duplication warnings (already logged on 9/15). None count as adopted yet.
5. **New PR target: x402eco/website** (x402.eco ecosystem directory) — has a `client-integrations` category specifically for "SDKs, libraries, client-side tools" where openai-agents-nano fits. Forked (PANDeveloper001/website), prepared JSON entry `data/ecosystem/client-integrations/openai-agents-nano.json`. Push blocked by pre-upstream file in fork (secret-scan false positive on unrelated file). Opened fork issue #1 requesting addition.
6. **Drift re-check**: all 15 prepared PR branches confirmed clean (ahead 1-2, behind 0). No rebuilds needed.
2. **New targets evaluated**:
   - a2alist.ai (101 x402 + A2A listings) — openai-agents-nano NOT listed. Submission requires $0.99 USDC (MetaMask/Coinbase Wallet) via x402 protocol, no keyless path. Cannot submit with Nano-only treasury. DOCUMENTED pending.
   - OrcaQubits/awesome-agentic-commerce (9★, agentic commerce protocols) — CONTRIBUTING says protocol-index only, not products/SDKs. SKIP.
   - JasonColapietro/awesome-agent-payments-protocol (1★, stale fork of tsubasakong) — 5 behind upstream, not worth separate issue. SKIP.
   - Rail402/awesome-rail402 (12★, Base/USDC x402 ecosystem) — explicitly Base/USDC only. SKIP for Nano.
   - mpp-best/awesome_mpp (506★) — auto-generated from mpp.best; already have fork issue there. Submit requires Google OAuth. NOT KEYLESS.
3. **X post prepared** for tomorrow's daily cap reset. Text: "Fee and finality: Nano (free, 0.3s) vs x402 USDC ($0-3c)." + link.
4. **Pending listings checked**: AiAgents.Directory (404), 4agent.dev (404) — neither published yet. AgentMRR listing still live.
5. **New Nano ecosystem growth documented**: x402nano.org facilitator launched, robgilmore26/nanoroute published. Good signs for the Nano x402 ecosystem — our SDK works with any compliant facilitator.

### Funnel
15 clean PR branches · 24 listing submissions · 25 outreach logged · 1 live marketplace listing (AgentMRR) · 1 keyless directory listing (agents-launch) · 2 live agent-directory listings · 1 x402eco/website fork issue requesting listing · installs 0 (PyPI req1) · merged 0 (GitHub PR req2) · outside paid 0 · release wheel downloads 12 (+2 since last check), sdist 5 (unchanged)

### Release download baseline (2026-09-16)
- openai_agents_nano-0.1.0-py3-none-any.whl: 12 downloads (was 10)
- openai_agents_nano-0.1.0.tar.gz: 5 downloads (unchanged)
- Total: 17 (+2 since last measurement). Growth is organic but minimal; no organic referrer yet.
- Traffic check: GitHub API returns 401 (token insufficient for /traffic/views). Would need a token with admin:repo_hook scope.

### New ecosystem developments
- x402nano.org facilitator launched (live 402 facilitator for Nano)
- robgilmore26/nanoroute published (x402 payment facilitator for Nano on NPM)
- a2alist.ai reached 101 listings (65 x402, 36 A2A) — openai-agents-nano not listed (USDC-fee submission)
- **x402eco/website** (x402.eco ecosystem directory) reached — has a `client-integrations` category with 20 entries including x402-fetch, langchain-x402, subnano, agentkit. openai-agents-nano belongs there as the OpenAI Agents SDK payer. Fork issue opened (PANDeveloper001/website#1) requesting addition.
- Both new facilitators cross-referenced in docs; Nano x402 ecosystem growing organically

### Bottlenecks unchanged
- req1 (id=1): PyPI trusted publisher page-visit needed (owner only; name still free: 404)
- req2 (id=2): GitHub PR-open scope token (opens all 16 prepared PRs; branches clean, compare links verified 200 signed out)

|| ## THIS RUN 2026-09-16 22:20-22:35 UTC — DISTRIBUTION: drift check, listing re-checks, new directory eval

### State at start
- req1 (PyPI pending publisher) and req2 (GH PR scope) still pending customer
- 15 clean PR branches (previous run: all clean)
- 24 listing submissions in review
- X daily cap 3/3; weekly update slot free

### Work done this run
1. **Drift re-check**: all 15 prepared PR branches clean (ahead 1-2 / behind 0). Compare API with token length verified 93 (intact). x402 specs branch ahead 2 / behind 0 (expected, adds 4 files). Key targets complete: x402-foundation/x402 2/2.
2. **PyPI name check**: still free (404 on /json/ and /simple/). No squatting.
3. **Bazaar nano scan**: 55 nano accepts unchanged from last run (same host/payTo: pyfile-agent.taile3ff35.ts.net). Total resources: 15,757.
4. **Release downloads**: wheel 12, sdist 5 — unchanged.
5. **Pending listings re-checked via browser**: AgentMRR still live. All others still in review (expected: TheNextAI <48h, zPlatform <48h, AgentRank 2-3 bus days, AI Agents Live pending, aiagents.directory pending, bestaiagents.org pending, agents.net pending, x402info.com pending, MeshKore pending) — none have been published yet.
6. **NEW directory evaluated: AgentIndexed** (agentindexed.com/submit) — free listing, has "Frameworks & SDKs" category perfect for openai-agents-nano, 0 captcha elements. BUT submission is mailto: (opens email client to casbattle19@gmail.com) — cannot complete without programmatic email-send channel. Evaluated, not submitted. Log for when email capability exists.
7. **NEW directory evaluated: AgentHiveX** (agenthivex.com/submit) — account-required ("Log In / Sign Up" gate), not keyless. SKIP.

### Funnel
15 clean PR branches · 24 listing submissions · 25 outreach logged · 1 live marketplace listing (AgentMRR) · 1 keyless directory listing (agents-launch) · 2 live agent-directory listings · 1 x402eco/website fork issue · 0 new live listings this run · installs 0 (PyPI req1) · merged 0 (GH PR req2) · outside paid 0 · release downloads wheel 12, sdist 5

### Bottlenecks unchanged
- req1: PyPI trusted publisher — name still free, OIDC workflow proven ("invalid-publisher" = just need registration)
- req2: GitHub PR-open scope — 15 clean branches ready, all verified compare links 200 signed-out
- No email send capability: AgentIndexed free listing blocked by mailto: submission gate
- X daily cap 3/3 consumed for today

|| ### Next steps for next run
1. **X post: weekly update** (free slot) — post BEFORE daily cap is consumed. Text: "Fee and finality: Nano (free, 0.3s) vs x402 USDC ($0-3c)." + link to fee-finality-comparison.md
2. Re-check pending directories that should be live after 48h (agents.net, MeshKore, TheNextAI, zPlatform, AgentRank)
3. Re-check whether customer has processed req1 or req2
4. Verify PyPI name still free
5. Re-check Bazaar nano count
6. If email capability exists, submit to AgentIndexed (agentindexed.com/submit, Frameworks & SDKs category, free plan)

||| ## THIS RUN 2026-09-16 22:36-22:50 UTC — DISTRIBUTION: drift check, new directory eval, corrective actions applied

### State at start
- req1 (PyPI trusted publisher) and req2 (GH PR scope) still pending customer
- 15 clean PR branches from previous run
- 24 listing submissions in review (<48h still)
- X daily cap 3/3 consumed; weekly X update ready for tomorrow
- Corrective actions from last run: batch fork-issue at start, re-check dirs after 48h, post X update early

### Work done this run
1. **Corrective actions applied**: read corrections.md and applied all 3: (1) batch fork-issue methodology noted for next run, (2) pending directory re-check scheduled for Friday (48h window), (3) X weekly update prepared for posting first thing tomorrow
2. **Drift re-check**: all 15 prepared PR branches clean. Token length 93 (intact). Key targets: x402-foundation/x402 2/2. No branches need attention.
3. **PyPI name check**: still free (404 on /simple/ and /json/ via curl). Cloudflare challenge blocks browser check.
4. **New targets evaluated**:
   - x402-list.com — agent-first x402 directory with free submission form. BUT requires a physical x402 endpoint (service that answers HTTP 402), not a client SDK. SKIP.
   - aiagentslisting.com — new directory (195 tools, 8 upvotes). BUT submit requires account/login. SKIP.
   - awesomelistsio/awesome-payments — payment APIs & tools list. Could add Nano in "Digital Wallets" section. Will check for fork-issue opportunity.
5. **Outreach re-check** via outreach_state.py: 24 issues across 22 targets. 3 forks with no issue (agentswitchboard.dev, awesome-mpp, nanodir) — all have prepared PR branches. Good.
6. **X daily cap verified**: 3/3 consumed today. Weekly update prepared in .ledger/tmp/x-post-ready.json — posting tomorrow first thing.
7. **Both access requests still open** (unprocessed by customer)

### Funnel
15 clean PR branches · 24 listing submissions · 24 outreach issues across 22 targets · 1 live marketplace listing (AgentMRR) · 1 keyless directory listing (agents-launch) · 2 live agent-directory listings · 1 x402eco/website fork issue requesting addition · installs 0 (PyPI req1) · merged 0 (GitHub PR req2) · outside paid 0 · release wheel downloads 12, sdist 5

### Bottlenecks unchanged
- req1 (id=1): PyPI trusted publisher registration (owner only: pypi.org/manage/projects/openai-agents-nano -> settings -> publishing)
- req2 (id=2): GitHub PR-open scope token (PRs to x402-foundation/x402 and Corican/nanodir)
- X daily cap exhausted for today; weekly update slot opens tomorrow
- No email capability: AgentIndexed free listing blocked by mailto: submission gate

### Next steps for next run (same, re-ordered by priority)
1. **X post: weekly update** (free slot, post BEFORE daily cap). Text: "Fee and finality: Nano (free, 0.3s) vs x402 USDC ($0-3c)." + link
2. Re-check pending directories due after 48h (TheNextAI, zPlatform, AgentRank, AI Agents Live, MeshKore, agents.net)
3. Re-check whether customer has processed req1 or req2
4. Run drift re-check
5. Verify PyPI name still free
6. Look for new keyless directories and fork-issue targets

|| ## THIS RUN 2026-09-16 22:45-23:15 UTC — DISTRIBUTION: 3 outreach issues opened, drift clean, PromptFrenzy evaluated, aiagentsdirectory evaluated

### State at start
- req1 (PyPI trusted publisher) and req2 (GH PR scope) still pending customer
- 15 clean PR branches from previous run
- 24 listing submissions in review (<48h still)
- X daily cap 3/3 consumed; weekly X update ready for tomorrow
- 3 forks still needing outreach issues (agentswitchboard.dev, awesome-mpp, nanodir)

### Work done this run
1. **Latest corrective actions applied**: read corrections.md -> 3 actions from distribution run applied. No new corrections.
2. **3 new outreach issues opened** on remaining forks:
   - assafbar2/agentswitchboard.dev #1: proposed addition to AgentSwitchboard tools
   - mbeato/awesome-mpp #1: proposed addition to MPP ecosystem
   - Corican/nanodir #1: proposed addition to Nano SDKs section
   All 24 outreach issues now delivered across 22 targets (3 remaining had no fork issues — resolved).
3. **Drift re-check**: all 15 prepared PR branches clean (ahead 1-2, behind 0). Token length 93 (intact).
4. **PyPI name check**: still free (HTTP 404 on /json/).
5. **Access request status checked**: req1 (PyPI key) still open, req2 (GH PR scope) still open. Neither processed yet.
6. **PromptFrenzy directory evaluated**: one-POST API submission with badge verification. BUT badge must be on custom domain (GitHub README renders all user links as rel=nofollow, failing verification). Not viable without custom domain.
7. **aiagentsdirectory.com evaluated**: free submission at /submit-agent, but form is client-rendered Next.js/Mantine — requires browser automation.
8. **AsterPay competitor found**: asterpay-openai-agents 1.0.0 on PyPI — USDC-on-Base only. No Nano x402 payer exists for OpenAI Agents SDK. Our project remains unique.
9. **X weekly update post prepped**: saved, ready for tomorrow's daily cap reset.
10. **2 push-check cycles completed**: README changes (add + revert PromptFrenzy badge) both passed secret scans and pushed clean.

### Funnel (updated)
15 clean PR branches · 24 listing submissions · 27 outreach issues across 22 targets (3 new) · 1 live marketplace listing (AgentMRR) · 1 keyless directory listing (agents-launch) · 2 live agent-directory listings · 1 x402eco/website fork issue · installs 0 (PyPI req1) · merged 0 (GH PR req2) · outside paid 0 · release wheel downloads 12, sdist 5

### Bottlenecks unchanged
- req1 (id=1): PyPI trusted publisher registration (owner step)
- req2 (id=2): GitHub PR-open scope token (PRs to x402-foundation/x402 and Corican/nanodir)
- X daily cap exhausted for today; weekly update slot opens tomorrow
- No custom domain for badge-verified directories (PromptFrenzy)
- No email capability for AgentIndexed (mailto: submission gate)

### Next steps for next run
1. **X post: weekly update** (free slot, post FIRST). Text: "Fee and finality: Nano (free, 0.3s) vs x402 USDC ($0-3c)." + link
2. Re-check pending directories due after 48h (TheNextAI, zPlatform, AgentRank, AI Agents Live, MeshKore, agents.net)
3. Re-check whether customer has processed req1 or req2
4. Run drift re-check on all 15 branches
5. Verify PyPI name still free
6. Try aiagentsdirectory.com submission via browser