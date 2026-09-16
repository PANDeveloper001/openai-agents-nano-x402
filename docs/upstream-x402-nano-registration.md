# openai-agents-nano-x402 — prepared upstream contribution to `x402-foundation/x402`

Status: **branch prepared, drift-clean, PR blocked on token scope** (`POST /repos/*/pulls` → 403 for the
fine-grained token the agent holds; one signed-in click from a human opens it).
Written 2026-09-16. Everything in this file is measured; the raw evidence files are named inline.

## Why this contribution exists (two measurements, 20 minutes apart, both keyless)

**1. A Nano-only x402 route passes a third-party conformance checker.**
`StelarDigital/x402-starter-kit` ships **x402 Doctor** (`GET https://api.stelardigital.com/doctor?url=…`), a
free keyless checker whose suite supports Base *and* Algorand rails. Pointed at a live route whose `accepts[]`
holds exactly one entry — `scheme: exact`, `network: nano:mainnet`, `asset: XNO` — it returned
**9 checks, 8 pass, 1 warn, 0 fail — score 94.4, grade B, `recommendation: "ready"`**, including:

> `network_caip2` **pass** — "network matches CAIP-2 shape (namespace:reference) — **nano**."

The **same route, same minute**, through the CDP Bazaar validator (`POST
api.cdp.coinbase.com/platform/v2/x402/validate`) returns `valid: false`, with exactly four failed checks and
21 of 25 passing:

| failed check | message |
|---|---|
| `accepts[0].network` | Network "nano:mainnet" is not supported |
| `accepts[0].asset` | Asset "XNO" is not USDC |
| `accepts[0].amount` | Amount "1000000000000000000000000000" is not a base-10 integer |
| `accepts[0].payTo` | Missing or invalid payTo address |

Everything else passes on both: HTTP 402, the JSON challenge in the body, the `PAYMENT-REQUIRED` header,
`x402Version: 2`, `accepts[]` completeness, `maxTimeoutSeconds`, `has_bazaar_extension`, `bazaar.info.input`
/output/schema, parse.

**What that means, stated exactly:** the Nano declaration is **valid x402** — a second, independent
implementation says so and names `nano` as a CAIP-2 namespace. The CDP rejection is **facilitator policy**
(which networks it will verify and settle), not a malformed payload. Raw evidence:
`.ledger/tmp/evidence/two-validator-nano.json`; reproducer: `scripts/two_validator_probe.py <https-base-url>`.

**2. The gap in x402's own repository: registration, not payment.**
`main` at 2026-09-16 has:

- per-network `exact` scheme specs for **17** networks (`specs/schemes/exact/scheme_exact_*.md`):
  algo, aptos, canton, cardano, casper, concordium, evm, hedera, keeta, near, starknet, stellar, sui, svm,
  ton, tvm, xrpl — **no nano**;
- a CAIP-2 identifier list in `docs/core-concepts/network-and-token-support.mdx` — **no nano line**;
- default-asset registries per mechanism (`typescript/packages/mechanisms/<chain>/src/defaultAssets.ts`,
  `go/mechanisms/<chain>/default_assets.go`, `python/x402/mechanisms/<chain>/default_assets.py`) — **no
  nano directory in any of the three SDKs**;
- `.github/labeler-networks.json` and the e2e mechanism catalog drive off the same network list.

Meanwhile, on the payment side, there are **two live third-party implementations**: the facilitator at
`facilitator.pursekeeper.dev` (source `pursekeeper/api`, `facilitator.js`) implementing the nine `/verify`
checks, and a Python `x402ResourceServer` scheme for `nano:mainnet` at `pursekeeper/x402-nano-exact`, with at
least one independent seller live on it and a second registered next to a USDC rail
([PR #3432 comment, 2026-09-11](https://github.com/x402-foundation/x402/pull/3432)). The seller-side
`/verify` failure modes for this rail are published (a `frontier_moved` case, the work thresholds, a paid
independent reproduction), so the spec text is the only artifact still missing from upstream.

## The exact three edits the upstream docs ask for

`docs/core-concepts/network-and-token-support.mdx`, **Adding Support for New Networks**, offers two paths:
runtime registration (no PR) and *"Contributing a New Default Asset … Requires a PR updating the
TypeScript, Go, and Python SDK registries."* For a non-EVM chain the third edit is the per-network scheme
spec, whose required contents are fixed by `.agents/skills/authoring-specs/references/new-network-scheme-spec.md`
(scheme-specific fields go in `extra`; every `extra` field must be consumed by client or facilitator; reuse
established field names such as `extra.feePayer`; fee sponsorship preferred — which for Nano is total, since
the rail has no fees at all).

1. `specs/schemes/exact/scheme_exact_nano.md` — see the prepared branch `specs/exact-nano-mainnet`
   (`PANDeveloper001/x402` @ `cbef150a`), which also carries an offline checker
   (`specs/schemes/exact/.nano_spec_check.py`) with a demonstrated mutation failure.
2. the CAIP-2 identifier line: `nano:mainnet`, per the CAIP-2 namespace convention, consistent with the
   live declarations indexed today.
3. one default-asset row per network in the three SDK registries (`typescript`, `go`, `python`).

**Design question a maintainer will raise, and the honest answer.** Those tables are documented as
*"Default **USD-pegged** assets by CAIP-2 network; index 0 is the `"$0.10"` default"*, i.e. they exist so a
server can write `price: "$0.01"`. XNO is not USD-pegged, so a Nano row is not an automatic fit: either
Nano's row is registered with a documented `null`/absent USD default (and `price` must be given as a
`TokenAmount` in atomic units, as the doc already allows for unlisted chains via `registerMoneyParser()` or
an explicit `TokenAmount`), or the table's "USD-pegged" premise is extended to "default asset" with the
USD assumption stated per row. This is a maintainer decision, and the PR should ask it explicitly rather
than pretend a decision has been made. The *identifier* and *spec* edits do not depend on that answer.

## What is already prepared and verified

| artifact | where | state |
|---|---|---|
| missing per-network scheme spec + offline checker | fork branch `specs/exact-nano-mainnet` @ `cbef150a` | ahead 1 / behind 0 vs current `main`; compare page 200 signed out |
| docs row: `openai-agents-nano` in `docs/dev-tools/third-party-sdks.md` | fork branch `docs/list-openai-agents-nano-v6` @ `3917a836` | ahead 1 / behind 0 vs current `main`; compare page 200 signed out |
| two-validator measurement | this repo, `docs/x402-discovery-study.md` + `scripts/two_validator_probe.py` | published on `main` |

Both x402 branches were re-checked against upstream `main` on 2026-09-16 with the compare API
(`scripts/prepared_pr_drift.py`); `x402-foundation/x402` moves several commits a day, so **re-check
immediately before opening**.

## Deliberately not done

- **No fork-issue outreach to x402-foundation for this finding.** The live discussion on PR #3432 is
  substantive and the people who need this measurement are already in it; nobody in that thread has asked
  "does any checker accept this", and the measurement is published in this repo for anyone who needs it.
  A second thread on the same question is noise, not distribution.
- **No ask attached.** The only thing this contribution wants is review.
