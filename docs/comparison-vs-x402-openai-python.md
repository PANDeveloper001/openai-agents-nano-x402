# Comparison: openai-agents-nano vs qntx/x402-openai-python

A plain, honest comparison with the closest existing project that also pays x402
endpoints from Python: [`qntx/x402-openai-python`](https://github.com/qntx/x402-openai-python)
("drop-in OpenAI Python client with transparent x402 payment support", ~260 stars,
MIT). It is the incumbent language-client route for paying x402 APIs; this repo is
the OpenAI *Agents SDK* route. Neither replaces the other; the table is so you can
pick the right one for your stack.

## The short version

| | qntx/x402-openai-python | openai-agents-nano (this repo) |
|---|---|---|
| What it is | A drop-in replacement for the `openai` client | An OpenAI Agents SDK `Tool` |
| Where it fits | Code that calls `openai`'s Chat/Embeddings API directly | Agents built with the Agents SDK (`Agent`, `Runner`) |
| Pays in | USDC on EVM (Base/Ethereum), Solana/SVM | native **Nano (XNO)** |
| Fee to the payer | facilitator + gas (stablecoin rails; Circle-issued USDC) | **0 XNO** (feeless, no gas, no facilitator) |
| First finality | on-chain instant on L2, full finality later on the parent chain | sub-second, full finality on Nano's own ledger |
| Issuer that can freeze | USDC is Circle-issued (freezable stablecoin) | none (self-custody, no stablecoin) |
| Install | `pip install x402-openai[evm\|svm\|all]` (on PyPI) | `pip install openai-agents-nano` (pending PyPI; `git+https` today) |
| Rebuilt payment logic | implements its own wallet/x402 signing | reuses MIT `feeless402` (no rebuilt payment internals) |

Numbers and sources: same facts as `docs/fee-finality-comparison.md` and
`docs/agent-payment-rails-comparison.md`.

## What is genuinely different

**Custody rail.** `qntx/x402-openai-python` pays stablecoins on EVM/SVM chains (USDC —
a Circle-issued, freezeable asset; the facilitator applies screening). This repo pays
**Nano (XNO)** — a native, self-custodied asset with no issuer that can blacklist a
payment. If `no-one-can-freeze` matters for your agent's payment rail, only a
non-stablecoin self-custody rail gives it.

**Fee model.** USDC x402 pays per-call gas (EVM) or slot fees (Solana), plus whatever the
facilitator charges once volume passes a free tier. Nano charges **0 XNO** on every call,
regardless of frequency or amount — the reason this repo reuses the feeless402 rail rather
than synthesizing a fee model.

**Framework fit.** The qnq client drops into direct `openai` calls. If your agent runs on
the OpenAI **Agents SDK**, you glue tools into `function_tool` — an adapter that wraps an
x402 *endpoint* as a `Tool` is the natural shape, and reusing `make_nano_x402_tool` keeps
the Agents SDK idioms (`ToolContext`, `on_invoke_tool`, over-cap REFUSED) intact.

## Honest limits (facts, not marketing)

1. `qntx/x402-openai-python` is **already on PyPI** and multi-chain; this repo is not yet
   on PyPI (token-gated) and covers the OpenAI Agents SDK only. For a plain `openai` client
   call, keep using qnq.
2. **Nano is not a stablecoin.** It has price volatility; if your payer needs
   fiat-denominated settlement, USDC rails are the closer fit today.
3. Both are x402 *clients*. Neither is registered in a service/facilitator directory
   (those are for endpoints that answer HTTP 402).

## Sources

- http qnq client README (2026-09-15): features (drop-in OpenAI, EVM+SVM wallets,
  multi-chain, policies) and install commands.
- This repo `docs/fee-finality-comparison.md`, `docs/agent-payment-rails-comparison.md`,
  `docs/live-proof.md`: Nano payer costs, finality, custody, and the real paid redeem.
- X-currency issuer: USDC is issued by Circle; Nano has no issuer.