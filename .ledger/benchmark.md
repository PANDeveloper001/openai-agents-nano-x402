# Benchmark: how do AI-agent frameworks pay x402 endpoints today?

Goal: give a major AI-agent ecosystem a self-custodied Nano (XNO) rail for paying
x402-priced HTTP endpoints, by reusing an existing Nano tool as a thin adapter.

## Why the OpenAI Agents SDK is the best outside target here

| Best existing "solver" for the goal | Concrete reason it's the leader | Source |
|---|---|---|
| AsterPay for OpenAI Agents SDK (`asterpay-openai-agents`) | The OpenAI Agents SDK's own x402 payer; drop-in `paid_fetch` tool; `check_balance`/`make_payment`; auto-pays challenges | pypi.org/project/asterpay-openai-agents |
| Cloudflare Agents SDK `withX402Client` | MCP-client x402 payment for agents, `paidTool` server side | developers.cloudflare.com/agents |
| paygraph (AgentWallet) | Spend governance + x402 gateway for LangGraph/CrewAI | github.com/paygraph-ai/paygraph |
| x402-agent / x402-langchain | Framework-agnostic / LangChain x402 payer | pypi.org/project/x402-agent, x402-langchain |

## The concrete weakness to attack

**Every one of these settles in USDC (EVM/Base) or Solana only. None can settle an
x402 endpoint in Nano (XNO).** OpenAI's own cookbook example ("Controlled Agentic
Commerce") is EVM USDC. Cloudflare's coding-tool plugins and Claude Code hooks are
all EVM USDC. There is no Nano payer for the OpenAI Agents SDK, or for any of these,
anywhere.

Nano already HAS the missing rail but only as a CLI/MCP client: the MIT-licensed
`feeless402` package exposes `Wallet`, `RPC` and `request_with_payment(...)` — a
self-custodied, price-capped, on-ledger-verified Nano x402 handshake that speaks
both the x402nano-exact v2 and NanoGPT v1 dialects. It is not available as an
OpenAI Agents SDK Tool.

## The invention

A thin OpenAI Agents SDK `Tool` that wraps `feeless402.request_with_payment` so any
OpenAI agent can pay any x402 endpoint in XNO from its own wallet, self-custodied,
fee-free, with a hard per-call cap and an honest on-ledger receipt.

Trade-offs vs the leaders: no EVM gas, no wallet custody by third parties, no
freezeable stablecoin — but XNO faces volatility and has a smaller merchant surface,
so the adapter keeps the price-cap and reveals the exact on-ledger verdict.