# Measured comparison: the agent-payment rail set

This repo's stated goal is to measure Nano (XNO) as an agent payment rail against
**x402/USDC, Stripe+Tempo MPP, Google AP2 and card-network agent rails**. This doc is the
plain, cited per-rail comparison for that measurement. The Nano row comes from this repo's
own measured runs and public node lookups; every other number is drawn from the source cited
next to it. Where a number is not public or is disputed, the doc says so instead of inventing one.

## The set, in one table

| Rail | Payer per-call cost | First settlement / finality | Custody / who can freeze | Session model | Fiat / bank settlement |
|---|---|---|---|---|---|
| **Nano x402** — `openai-agents-nano` | **0 XNO** (feeless, no gas, no facilitator) | **sub-second**; full finality on Nano's own ledger (no parent chain) | self-custody seed; **no issuer that can freeze** | per-request (x402-style, stateless) | only via a separate exchange off-ramp (AgentPay spells out the caveat: Nano is not fiat) |
| **x402/USDC** (Coinbase CDP, AsterPay; reported CCN 2026-09) | ~$0.0001 facilitation + per-call gas/facilitator percent | on-chain instant on Base; **full finality to Ethereum later** | USDC is Circle-issued (**freezable stablecoin**); facilitator runs OFAC/KYA | per-request, single 402 challenge | via facilitator off-ramp (AsterPay SEPA €0.10; CDP on/off ramp) |
| **Stripe + Tempo MPP** | **sub-$0.001** on Tempo L1; card legs at Stripe rates | **~0.5 s deterministic finality** on Tempo (Simplex, Commonware) | stablecoin (USDC/USDT/PathUSD on Tempo) or Stripe fiat cards / Visa / Lightspark Lightning | **session pre-auth** + streaming micropayments batched into one on-chain settlement | yes — fiat cards, Visa SPT, bank rails built in |
| **Google AP2** (x402 extension) | USDC on Base; **Coinbase currently the only stablecoin facilitator**; gasless (EIP-3009) | on-chain settle via x402 | USDC (circle-issued); mandate-based authorization | AP2 **CartMandate/PaymentMandate** over A2A; x402 per-request settlement | fiat card/bank via other rails (rail-agnostic) |
| **Card-network agent rails** (Stripe/Visas agent checkout, e.g. AgentPay) | **~2.9% + $0.30/tx** "standard Stripe rates" | network settlement, not built for sub-cent micropayments | fiat card/bank relationship | checkout / approval flow, human-leaning | yes (native fiat) |

## What differs, and why it matters for this repo's goal

**Cost.** Feeless is unique to Nano among the five — a Nano payer pays 0 XNO regardless of
frequency or amount. Tempo MPP is sub-$0.001 but settles *batched sessions*, and its card leg
still runs at card rates. x402/USDC advertises near-zero facilitation but the per-call gas and
the facilitator percent are real where charged, and CDP moves to $0.001/onchain-tx past its
free tier (see `fee-finality-comparison.md`). Cards are 2.9% + $0.30, which is an order of
magnitude too expensive for sub-cent API calls (Tempo/Jimmy research make this exact point:
2.9% + $0.30 cannot serve a $0.31 average agent payment).

**Finality.** Nano and x402-on-Base confirm *on the paying network*; Base's full finality is
later, on Ethereum. Tempo advertises deterministic ~0.5 s on its own L1 (no re-orgs, dedicated
payment lanes). Nano has no parent chain to settle onto, so sub-second is its full finality —
the trade-off is that Nano is its own ledger, not an EVM L2 or a card network.

**Custody and who can freeze.** Nano is native self-custody with no issuer that can blacklist a
payment. USDC is Circle-issued, so every USDC leg (x402/AP2/Tempo stablecoin) is a freezable
asset, and the facilitator applies OFAC/KYA screening. Self-custody USDC still settles a
freezable token. (Sources: existing `fee-finality-comparison.md`, Cryptothreads on AP2.)

**Session vs per-request.** MPP and AP2 are built around pre-authorized sessions/mandates that
batch many micropayments — efficient for high-frequency streaming. Nano x402 here is per-request
and stateless; that is simpler, and Nano's feeless per-request economics make it viable at scale
without batching.

## Honest limits of Nano in this set (facts, not marketing)

1. **Nano is not a stablecoin.** It has price volatility. For a payer who needs
   fiat-denominated settlement or a bank payout, MPP/cards/USDC are currently the closer fit.
2. **Nano is its own ledger.** It is not an EVM L2 under the Ethereum settlement umbrella, not a
   card network, and not (yet) a plug-in form-of-payment for AP2's mandate flow. Cross-rail
   composability like being an AP2 settlement rail does not exist for Nano today.
3. **This adapter is one framework.** `openai-agents-nano` covers the OpenAI Agents SDK. Nano
   x402 coverage of LangGraph, CrewAI, Cloudflare Agents SDK etc. is a real gap versus the more
   mature USDC paths — this repo is the first, not the whole field.
4. This comparison measures *settlement characteristics*, not real observed market share. Nano's
   observed share of agent payments is not claimed here — that is the thing to measure, and this
   repo's live-proof and public links are the evidence trail for it.

## Sources

- Nano row: this repo — `docs/live-proof.md` (real paid redeem, block confirmed on
  `rpc.nano.to` and `rainstorm.city`, 0 XNO fee) and `docs/fee-finality-comparison.md` (0.3 s,
  feeless; Coins Wiki, Nano whitepaper, NowNodes).
- MPP: Jimmy Research "Tempo MPP" (Stripe+Tempo, live 2026-03-18 chain 4217, ~0.5 s, sub-cent);
  Blockeden (2026-04): sessions, streaming, sub-$0.001 stablecoin transfers, FeeAMM no-gas-token;
  Openfort "Agentic Payment Protocols Compared" (MPP session batching, OAuth-for-money);
  CCN "AI Agents Need Payment Rails" (MPP session batch settle, 0.5 s; per-request x402
  ~$0.0001 fees).
- AP2: Google Cloud blog "Announcing Agent Payments Protocol (AP2)" (Sept 2025, A2A + x402
  extension); google-agentic-commerce/a2a-x402 spec v0.2 (CartMandate / PaymentMandate);
  Cryptothreads (2026): Coinbase the only stablecoin facilitator, gasless EIP-3009, USDC over Base.
- Cards / ACP: Nevermined "Best Platforms for Agentic Payments 2026" (standard Stripe 2.9% +
  $0.30); Eco Agent Pay developer guide (Stripe AI Agents SDK, Checkout primitives).
- Credit where due on the under-serving of cards for micropayments: Jimmy Research (MPP) and
  Blockeden both note 2.9% + $0.30 and $1 Ethereum gas break sub-cent micropayments.
