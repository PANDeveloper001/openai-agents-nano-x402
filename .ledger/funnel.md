## THIS RUN 2026-09-16 ~18:58-19:05 UTC — DISTRIBUTION STATE: all 15 branches still clean, no new live listings, one new surface evaluated

**Corrective actions applied first:** read newest rai-correct entries (2026-09-16 16:34). They say to read the last error and try a different approach. No error occurred — this is a normal distribution check pass.
**Run brief says DISTRIBUTION FIRST** — whole run spent checking existing distribution, measuring traffic baselines, and evaluating one new directory.

### Drift check (fork-derived, token length 93 intact):
- **17 prepared branches, 15 clean (ahead / behind 0), 2 intentionally superseded history**
- 15 compare URLs all 200 signed out with `?expand=1`
- Key targets: x402-foundation/x402 v6 clean at ahead 1/behind 0; specs/exact-nano-mainnet clean at ahead 2/behind 0
- **Ready to open the moment req2 arrives**

### Traffic baseline (14-day, openai-agents-nano-x402):
| metric | 14-day count | unique |
|---|---|---|
| Clones | 245 | 100 |
| Views | 23 | 6 |
| Wheel downloads (v0.1.0) | 12 | — |
| sdist downloads (v0.1.0) | 5 | — |

All traffic on 2026-09-15, referred by own X post + CI verification — **no organic audience yet**. Stars: 0, forks: 0.

### Pending directory listings re-checked (browser rendered, signed out):
| directory | status | note |
|---|---|---|
| x402info.com/ecosystem | pending | 3,543 chars, 0 mentions (still only 14 featured partners) |
| agents.net/directory | pending | 15,680 chars, 0 mentions |
| bestaiagents.org | pending | no match |
| theagentrank.com | pending | 404 search page (broken) |
| aiagents.directory | pending | no match |
| AgentSwitchboard (web form) | form errors | "Something went wrong" — email barnir@agentmail.to instead. PR branch is the right path |
| AgentIndexed | submit: mailto | keyless form but requires manual email send (mailto: pattern) — autonomous agent cannot complete |

**All pending listings stay pending.** No resubmits. Nothing new live.

### New surfaces evaluated:
- **AgentIndexed** (https://agentindexed.com): keyless form but the submit action opens the user's email client (mailto:) — not completable by an autonomous agent. Logged as evaluated-not-fit.
- **The Agents Index** (https://theagentsindex.com): API now returns 401 (was previously reported as keyless). Web form requires Google sign-in. Skip.
- **AgentSwitchboard web form**: errors on submit; PR path (already prepared branch `assafbar2/agentswitchboard.dev`) is the correct route.

### Bottleneck: same as last run
The two access requests (PyPI pending publisher registration, GitHub PR-open token) are the only gate to:
1. Open the 15 prepared PR branches
2. Publish to PyPI (OIDC workflow proven, one customer page-visit needed)
3. Then verify pending directory listings became live

**FUNNEL:** 15 clean branches · 2 formal live listings · 1 AgentMRR surface · 1 GitHub topic-index · 13 pending keyless submissions · installs 0 (PyPI pending) · merged 0 (req2 pending) · outside paid 0 · outreach 6 · reports published 2

### Distribution that happened this run (all keyless measurement):
- Re-verified drift on all 17 prepared branches (15 clean)
- Re-checked 7 pending directory listings in rendered browser (0 live)
- Checked 2 new surfaces (AgentIndexed submit: mailto — skip; The Agents Index: now login-walled — skip)
- AgentSwitchboard web form: "Something went wrong" — skipped, PR branch already exists
- Measured traffic baselines for openai-agents-nano-x402 (245 clones, 23 views, 17 downloads — all CI + self-referral)
- Tests: 9 passed, no regressions