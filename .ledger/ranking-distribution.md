# Ranking — distribution, 2026-09-16 run (DISTRIBUTION FIRST)

Goal: outside adoption and payments for **openai-agents-nano-x402**, under the owner rule (70% distribution,
30% building), with two credential gates open: a PyPI upload token and a GitHub token allowed to open pull
requests on third-party repositories. No spam, no fake accounts, no mass unsolicited messages.

Companion file: `ranking.md` holds the earlier (block 1, 2026-09-14) ranking of the adapter Tool shape.
This file is this run's distribution ranking.

## How the ideas were produced (source recorded honestly)

* `bin/brainstorm` with source `engine` failed again: Methodology-Tree `/api/v1/run` answered **HTTP 502**.
* The OpenRouter source failed for a different, now-understood reason: the account is **not empty** —
  `GET /api/v1/credits` returns `total_credits 822.003885` vs `total_usage 822.203790607`, i.e. **no spendable
  margin**; every paid call answers `402 "you requested up to N tokens, but can only afford M"`.
* Fixed with a small extension rather than a stopped step:
  `~/.hermes/extensions/stack_fallback_models.py` routes the stack's OpenAI-compatible calls to the owner's
  configured backup provider (`~/.hermes/config.yaml` → `custom_providers: nanogpt`,
  `https://nano-gpt.com/api/v1`), and `~/invent-stack/bin/_common.py` now honours the `OPENROUTER_API_BASE`
  override (default unchanged: `https://openrouter.ai/api/v1`). Three judge roles verified answering there
  (`OK`), and a real routed `ledger verify` plus `ledger redteam` ran end to end on a scratch repo.
* With that route, `bin/brainstorm --features features.json --angles 5
  --sources model:deepseek/deepseek-v4.1-flash` produced **17/25 ideas** across 5 distribution mechanisms.
  Raw output stays **outside** the repo (`/root/sandbox-bs/ideas.json`): the brainstorm model is not the
  stack's declared judge family, so no ledger verdict was recorded from it.

## Ranking of the distinct mechanisms

| # | Mechanism | Keyless? | Moves adoption? | Focus cost | Verdict |
|---|---|---|---|---|---|
| 1 | **PyPI Trusted Publishing (OIDC) + pending publisher** | keyless publish; one owner page-visit to register | **highest**: unlocks `pip install`, the bar directories and users check | tiny: one workflow file | **CHOSEN** |
| 2 | Release-driven distribution (pinned installs, release page as the evidence link) | yes | medium-high | small | DONE (v0.1.0, all installs pinned) |
| 3 | Drift-maintained prepared PR branches (13) | yes | latent until a PR-capable token exists | small per run | KEEP (all 13 re-verified ahead 1–2 / behind 0 this run) |
| 4 | Canonical project card + `llms.txt` + GitHub topics so indexes crawl | yes | medium | medium | later run |
| 5 | Signed submission manifest with a nonce echoed by the listing page | yes | improves **verifiability** of listings, not reach | medium | later run |
| 6 | Listing bounty paid in XNO | needs treasury spend | unknown; invites low-quality pages | high | **rejected** (spend + spam risk) |
| 7 | Nano ledger as a notary for listings | needs on-chain writes | cosmetic | medium | **rejected** (does not move adoption) |
| 8 | Publish as an IPFS/OCI artifact | yes | near zero for a Python SDK | medium | **rejected** |
| 9 | Release as a reusable GitHub Action (`uses: owner/repo@v1.0.0`) | yes | potentially viral: a real repo would depend on it | medium-large | **deferred** (building work, after adoption) |
| 10 | Per-release XNO payment sink counted per payer wallet | moves funds | interesting metric, no demand side | large | **rejected** for now |
| 11 | Ask the live seller to advertise our payer inside its 402 | no: needs the same PR token we lack | medium | — | **not actionable** |

Gimmicks rejected explicitly: 6 and 7 make *proof of a listing* stronger while leaving reach unchanged
(order sold as meaning). 8 is determinism that kills the value — content-addressing removes the update path a
dependency needs.

## The decision, and why it beats the benchmark

Benchmark (what everyone does): mint a PyPI API token, store it as a secret, `twine upload`. Its real
advantages were "works today" and "simple". It loses on the reason measured here: the token needs a human
with account access, so the project stayed unpublishable for days, and a leaked token can publish arbitrary
versions indefinitely.

The chosen mechanism keeps the same reach and removes the long-lived credential: PyPI's **pending** trusted
publisher creates the project on first use through GitHub's OIDC identity at release time. Verified this run:

* the name is still free — `https://pypi.org/pypi/openai-agents-nano/json` → **404** and
  `/simple/openai-agents-nano/` → **404** (control: `requests` → 200 on both), so a pending publisher can
  still claim it;
* the workflow is committed and public (HTTP 200 signed out):
  `https://github.com/PANDeveloper001/openai-agents-nano-x402/blob/main/.github/workflows/publish.yml`;
* it parses as valid YAML with the required `id-token: write`, `pypa/gh-action-pypi-publish@release/v1`,
  environment `pypi`, and a build job that holds no publishing credential.

**Honest limit:** a pending publisher cannot be created without signing in to PyPI, and Rai has no PyPI
account (and never creates accounts). This reduces the customer's step from "mint a scoped API token and hand
it over" to "paste four fields into PyPI's publishing page once" — necessary, smaller and secret-free. Until
then the keyless install path remains the pinned GitHub release:
`uv pip install "git+https://github.com/PANDeveloper001/openai-agents-nano-x402@v0.1.0"`.
