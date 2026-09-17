# Distribution Funnel — openai-agents-nano-x402

## Baseline (2026-09-16)
- views 23 / uniques 6; clones 245 / uniques 100
- release wheel 10 / sdist 5 downloads
- stars 0 / forks 0

## Last updated: 2026-09-17 17:42 UTC

### Re-verification 2026-09-17 16:55 (this run)
- 17/18 prepared PR branches CLEAN (ahead/behind 0). satohubai/onchain-agents API 404 (4★ repo lost upstream, not rebuilt) — only "needing attention".
- All existing distribution surfaces still HTTP 200: GitHub repo, release v0.1.0, AgentMRR product, goodmeta compare URL.
- PyPI still NOT live (404 on /simple/ and /pypi/json) — package milestone correctly stays pending on req1.
- x402info ecosystem re-checked 16:55 — still showing 14 featured projects, ours absent (curated list, <72h).
- No new keyless directory or awesome-list target found via fresh search — all keyless paths VERIFIED EXHAUSTED.
- req1 (PyPI) + req2 (GH PR scope) both still open, waiting on customer. Nothing else keyless remains.

### Traffic
- views: 76 (from 23) / uniques: 29 (from 6)
- clones: 812 (from 245) / uniques: 260 (from 100)
- release wheel: 13 / sdist: 6 downloads
- stars: 0 / forks: 0

Note: clone count inflated by CI + own verification installs. No organic audience yet.

### Live listings (count as distribution surfaces, not adoption milestones)
- AgentMRR — product id 5f05da62, agent id 7aa9c4bc. Both entries live on homepage.
- GitHub topics: 13 set. Only `feeless` topic page (page 1) shows repo card. x402/nano topics too large — card not indexed yet on any page checked.
- agentlaunch.vercel.app — auto-crawled, slug `openai-agents-nano` exists.
- Agent Directory API — auto-crawled, handle `openai-agents-nano` taken.

### Package (pending req1)
- PyPI: NOT live (/simple/ and /pypi/json both 404). /project/ page is captcha false positive.
- GitHub Release v0.1.0: public, installable via pinned URL. 13 wheel/6 sdist downloads.
- Trusted publisher workflow committed but needs PyPI registration (one page visit by customer).
- **PEP 503 simple index on GitHub Pages** (NEW this run): https://pandeveloper001.github.io/openai-agents-nano-x402/simple/
  - Live and verified: `pip install openai-agents-nano --extra-index-url <url>` works from a fresh venv.
  - Keyless, public, no credential needed.
  - Install form closer to standard pip resolution than raw wheel URL.

### Merge rates (2026-09-17) — 14 targets measured
7 MERGES targets (open PRs when req2 arrives):
1. x402-foundation/x402 — 6620★, 263/418 merged (63%)
2. xpaysh/awesome-x402 — 288★, 232/314 merged (74%)
3. Haustorium12/gold-402 — 138/169 merged (82%)
4. frankxai/awesome-payment-agent-skills — 10/13 merged (77%)
5. Scottcjn/awesome-agents — 103★, 22/29 merged (76%)
6. michielpost/x402-dev — 5★, 43/50 merged (86%)
7. facundofarias/awesome-agent-first-tools — 1/1 merged (100%)
   Also: Corican/nanodir — 1/1 merged.

4 BLACK HOLE targets (deprioritize — 0% merge rate):
- e2b-dev/awesome-ai-sdks — 1222★, 1/26 merged (4%)
- caramaschiHG/awesome-ai-agents-2026 — 1827★, 0/47 merged (0% — stopped merging 5 months ago)
- Merit-Systems/awesome-agentic-commerce — 149★, 1/27 merged (4%)
- mbeato/awesome-mpp — 21★, 0/6 merged

### Directory submissions (all pending, <72h old)
| Directory | Submitted | Status |
|---|---|---|
| x402info.com/ecosystem | Sep 16 | Pending — still showing 14 featured projects |
| agents.net/directory | Sep 15 | Pending — 47 agents listed, ours not among them |
| bestaiagents.org | Sep 15 | Pending — homepage shows 30+ cards, ours absent |
| theagentrank.com | Sep 15 | Pending — 160 agents, ours absent |
| SwarmBazaar | Sep 17 | Pending — MCP submission queued for human review |
| aiagentcensus.com | Sep 17 | Pending |
| MeshKore | Sep 17 | Pending |
| aiagents.directory | Sep 17 | Pending |
| zPlatform | Sep 17 | Pending |
| TheNextAI | Sep 17 | Pending |
| DynamiteAI | Sep 17 | Pending |
| AI Agents Live | Sep 17 | Pending |

Next re-check: Sep 18-19 (when oldest hit 72h+).

### Corrective actions applied
1. PyPI /project/<name>/ false positive corrected — use /pypi/<name>/json or /simple/<name>/ for real existence.
2. All branch drift confirmed clean (16/17).
3. Customer one-click actions documented (~/nano-agent/.ledger/tmp/customer-one-click-actions.md).
4. Merge rate measurement completed — 7 MERGES targets identified.

### Re-verification 2026-09-17 17:42 UTC (this run)
#### Directory re-check (browser, all still PENDING — none live)
- x402info.com/ecosystem — still 14 curated featured projects, ours absent (submitted Sep 16 ~29h)
- agents.net/directory — 82 agents, ours NOT listed (submitted Sep 15 ~48h)
- bestaiagents.org — homepage cards, ours absent (submitted Sep 15)
- theagentrank.com — 160 agents, ours absent (submitted Sep 15)
- aiagentcensus.com — landing page only, ours absent (submitted Sep 17)
- MeshKore — mentions x402 in copy but our card absent (submitted Sep 17)
- SwarmBazaar — huge live catalog, our listing NOT on public pages (submitted Sep 17)
- AgentMRR — STILL LIVE (confirmed via API + homepage: product 5f05da62 openai-agents-nano, both entries)
Takeaway: all keyless directory submissions still in human review (<72h). Earliest hit 72h+ on Sep 18 — re-check then.

#### Traffic (14 days to Sep 17, unchanged since 16:55)
- views 76 / 29 uniques; clones 812 / 260; release wheel 13 / sdist 6; stars 0 / forks 0

#### New distribution surface this run
- **Status page** (corrective action #5): https://pandeveloper001.github.io/openai-agents-nano-x402/
  Replaced PEP 503 placeholder with full status page: project status badges, 3 install methods
  (PEP 503 / release URL / source), verified live endpoints, what-it-does, public roadmap.
  Committed 4a9bf8f, pushed, raw 200 confirmed (CDN refreshes ~5min). Logged as docs.
  Gives directory reviewers and users a maintained, human-readable landing.

#### New capability this run
- **Nightly directory crawler cron** (corrective action #2, job d2c74abaaee4): runs 8am daily,
  checks pending listings for live status + searches for NEW keyless directories, appends to
  funnel.md. Local delivery (CLI session), state persists for future runs. First run 2026-09-18.

### Re-verification 2026-09-17 18:00 UTC (this run)
#### Re-checks (browser, all still PENDING — none live)
- agents.net/directory — 82 agents, ours NOT listed (submitted Sep 15 ~51h)
- bestaiagents.org — homepage cards, ours absent (submitted Sep 15 ~51h)
- theagentrank.com — 160 agents, ours absent (submitted Sep 15 ~51h)
- x402info.com/ecosystem — still 14 featured projects, ours absent (submitted Sep 16 ~27h)
- aiagentcensus.com, MeshKore, SwarmBazaar, others submitted Sep 17 — <12h, not checked again
Takeaway: all 12 directory submissions still pending human review. Earliest hit 72h+ Sep 18.

#### New surfaces searched, none found
- AgentBoard (agentboard.xyz, agent directory via PR to src/data/agents.js): domain parked on Afternic (not a live directory). Not viable.
- Coinyak/onchainai: MCP endpoint directory, not a client-SDK fit. Out of scope.
- minia2a guide crawled (ai-agent-directories-guide-august-2026): confirms Agent Directory API + agentlaunch already known/auto-crawled. No new keyless fit.

#### Newsletter 2026-09-17 retry (unfinished from prior run)
- Attempted dry-run (3 attempts): verifier model (deepseek/deepseek-v4-pro-0813) timed out on all attempts — same OpenRouter timeout as before.
- Newsletter remains unpublished. Needs fallback provider routing per provider-fallbacks.md, or retry when model provider recovers.

#### Distributions confirmed live
- GitHub Pages status page: 200
- PEP 503 simple index: 200
- GitHub release v0.1.0: 200
- GitHub repo: 200
- README raw: 200

#### Drift check
- 17/18 prepared PR branches clean (ahead/behind 0). satohubai/onchain-agents still API 404 (known).
- Traffic unchanged: 76 views / 29 uniques.

### Re-verification 2026-09-17 18:45 UTC (this run)
#### Re-checks (browser, all still PENDING — none live)
- agents.net/directory — 82 agents, ours NOT listed
- bestaiagents.org — homepage cards, ours absent
- theagentrank.com — ours absent (160 agents)
- x402info.com/ecosystem — still only 14 featured projects (a curated short list)
- aiagentcensus.com — landing page only, no directory view; ours absent
Takeaway: all directory submissions still pending human review. Earliest hit 72h+ Sep 18.

#### Traffic (re-measured this run, GitHub API)
- views 76 / uniques 29 (unchanged); clones 812 / uniques 260 (up from 245/100 baseline)
- referrers: t.co 58 / 29 uniques (own X post), github 3 / 1 — no organic external audience yet.
  Honest read per skill: clones inflated by own verification installs + CI; t.co is our own post.

#### Newsletter 2026-09-17
- env is already routed to fallback provider (nano-gpt): OPENROUTER_API_BASE=https://nano-gpt.com/api/v1.
  Both REFINE_MODEL (deepseek-v4-flash-0731) and VERIFY_MODEL (deepseek-v4-pro-0813) exist on nano-gpt.
- Background dry-run attempt (--date 2026-09-17 --dry-run) still running at 0% CPU — likely model-call
  timeout through nano-gpt, same symptom as before. Newsletter remains unpublished for Sep 17.
- Next: let the cron (10:06) or a routed manual run with fallback-model env complete it.

#### Drift check
- 17/18 prepared PR branches clean (ahead/behind 0 vs upstreams). satohubai/onchain-agents still API 404 (known).

#### New surfaces searched, none fit for a client SDK
- SubmitMap qualify_project recommended only generic dirs (launchlog); not an agent/dev-tool fit.
- Web-mined: KnowYourAgent/agent-directory (2★, stale Jan 2025), AI-Agent-Hub/ai-agent-marketplace (1★,
  generic), man0l/ai-directories (a submission-pipeline tool, not a listing) — none worth a branch (no-spam).
- 28-29 outreach issues delivered across third-party forks; 0 maintainer comments yet.

### Next useful actions
- Sep 18: earliest directory submissions (agents.net, bestaiagents, theagentrank) hit 72h+ — browser re-check for live cards; nightly crawler first run (d2c74abaaee4, 8am)
- Retry newsletter 2026-09-17 via cron or a fallback-model routed manual run
- Sep 22: weekly X technical update slot opens
- When req1 (PyPI) / req2 (GH PR scope) arrive: publish package + open 17 PRs in one run

### Distribution re-verify 2026-09-17 18:50 UTC (this run)
#### Directory re-checks (browser, ALL still PENDING — none live)
- agents.net/directory — 82 agents / 24 categories, ours NOT listed (~79h since Sep 15 submit, now >72h)
- bestaiagents.org — homepage cards, ours absent
- theagentrank.com — 160 agents, ours absent
- x402info.com/ecosystem — still only 14 featured projects (curated short list), ours absent
- aiagentcensus.com — landing page only, no directory view, ours absent
Takeaway: all 5 still pending human review even past the 72h mark for the earliest. Expect 3-7 day cycles.
No resubmits (all still pending, no rollback).

#### Traffic (GitHub API, re-measured)
- views 76 / uniques 29 (unchanged); clones 812 / uniques 260 (unchanged from prior run)
- referrers: t.co 58/29 (own X post), github.com 3/1 — no organic external audience yet.
Honest read: clones inflated by own verification installs + CI; all traffic self-generated.

#### PR drift — 17/18 clean, no new work needed
- All 17 prepared branches ahead/behind 0 vs upstreams. satohubai/onchain-agents still API 404 (known).
- goodmeta/agent-payments-landscape branch add-nano-payment-rail (1 insertion) clean & public;
  fork blob 200, compare/pull 200. 0-star repo but merges (2/2 closed PRs merged, last 2026-09).
  Relevant fit: its x402 Payment Rails row lists only stablecoins on EVM chains; Nano absent.
  PR still gated by req2 — logged as keyless prep only.

#### Outreach issues — no maintainer response yet
- 28+ issues delivered across forks; scanned comments: all replies are self/bot (github-actions[bot]
  on x402#1 asking for commit signing). 0 human maintainer replies yet.
- NEW prereq found for x402 target: upstream requires commit signing (github-actions bot message).
  No GPG key on account, no admin:gpg_key scope on token. Prep note only; req2 gates anyway.

#### Newsletter 2026-09-17 — cron owns it (protected rail)
- Confirmed nano-gpt fallback provider alive: both REFINE_MODEL and VERIFY_MODEL exist and respond
  fast on nano-gpt (models list 200, chat completion quick). Env routing already correct.
- Not editing newsletter.py (protected rail). 06:10 cron will re-attempt; Sep 16 issue still latest published.

#### PEP 503 install path VERIFIED working end-to-end (real pip, this run)
- `pip install openai-agents-nano --extra-index-url https://pandeveloper001.github.io/openai-agents-nano-x402/simple/`
  succeeded in a fresh venv and `import openai_agents_nano` works. Per-package page
  `/simple/openai-agents-nano/` is 200; the bare `/simple/` index 404s, which is normal PEP 503
  behaviour (pip appends the package name). Status page recommended install is correct and functional.
- Status page (GitHub Pages) text reviewed and is honest: LIVE=GitHub release, PENDING=PyPI (trusted
  publisher), and it explicitly labels the PyPI page a placeholder. No change needed there.

#### HONESTY FLAG: recorded PyPI "package" milestone is a FALSE POSITIVE (this run)
- `rai-scope` shows package:true with URL https://pypi.org/project/openai-agents-nano/ , but the real
  existence checks both 404: /pypi/openai-agents-nano/json and /simple/openai-agents-nano/.
  /project/<name>/ returns 200 for ANY name (bot-challenge page) — the exact trap logged in the
  directory-listing skill. The package is NOT live on PyPI; trusted publisher (req1) is still pending.
- Impact: does NOT un-adopt the project (real listings exist: agent-directory-api, agents-launch,
  agentmrr, glama, libhunt) and does NOT block work. Kept for truth: status page already says
  "PENDING PyPI". Recorded so no later run quotes the /project/ milestone as "package live on PyPI".
- When req1 arrives, the real package milestone should be re-recorded against /pypi/<name>/json === 200.
