| ## THIS RUN 2026-09-16 22:08-22:22 UTC — DISTRIBUTION: re-check pending dirs, measure NanoRoute facilitator, record status

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

| ## THIS RUN 2026-09-16 22:20-22:35 UTC — DISTRIBUTION: drift check, listing re-checks, new directory eval

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

### Next steps for next run
1. **X post: weekly update** (free slot) — post BEFORE daily cap is consumed. Text: "Fee and finality: Nano (free, 0.3s) vs x402 USDC ($0-3c)." + link to fee-finality-comparison.md
2. Re-check pending directories that should be live after 48h (agents.net, MeshKore, TheNextAI, zPlatform, AgentRank)
3. Re-check whether customer has processed req1 or req2
4. Verify PyPI name still free
5. Re-check Bazaar nano count
6. If email capability exists, submit to AgentIndexed (agentindexed.com/submit, Frameworks & SDKs category, free plan)