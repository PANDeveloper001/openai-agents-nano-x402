# openai-agents-nano

Pay any x402-priced HTTP endpoint in **self-custodied Nano (XNO)** from an
OpenAI Agents SDK agent. A thin adapter on the MIT-licensed
[feeless402](https://feeless402.com) client — it rebuilds **no** Nano payment
logic; it just exposes feeless402's `request_with_payment`, `Wallet` and `RPC`
as an OpenAI Agents SDK `Tool`.

Built by an AI agent. Scope approved by `rai-scope`; see `scope-manifest.json`.

## Why

Every major agent framework's x402 payer settles **USDC (EVM/Base) only**: the
OpenAI Agents SDK ships AsterPay (USDC), Cloudflare Agents SDK pays EVM USDC,
paygraph and x402-agent cover LangGraph/CrewAI with USDC. **None speaks the
Nano x402 dialect.** This tool gives OpenAI agents the first fee-free, instant,
self-custody XNO rail — verified on the ledger, no gas, no freezeable
stablecoin.

## Install

```bash
pip install openai-agents-nano
```

## Usage

```python
from agents import Agent, Runner
from openai_agents_nano import make_nano_x402_tool

# The wallet is bound here, never exposed to the model.
# Default: $X402_WALLET_PATH or ~/.nano-pay/wallet.json
# Default cap: $X402_MAX_XNO or 0.01 XNO
tool = make_nano_x402_tool()

agent = Agent(
    name="Paying agent",
    instructions=(
        "You can buy from paid x402 APIs. Always call nano_x402_fetch with "
        "dry_run=true first to see the price; only call with dry_run=false "
        "if the price is within an acceptable cap."
    ),
    tools=[tool],
)

result = Runner.run_sync(agent, "Fetch https://api.example.com/report")
```

### Tool behaviour

- One tool, `nano_x402_fetch(url, method="GET", json_body="", max_xno=None,
  dry_run=False)`.
- **`dry_run=true` is spendless**: reads the server's 402 quote and returns the
  price, pay_to and cap as agent-readable text. Never signs or broadcasts.
- **`dry_run=false`**: re-reads the quote, and refuses (plain refusal string,
  not an exception) if the price exceeds `min(max_xno, default cap)`. Only then
  signs locally via feeless402, retries with the payment header, and verifies
  on the ledger before returning a receipt (status, body, amount_xno, pay_to,
  block, settled, ledger, note).
- Payments are serialised behind an `asyncio.Lock`: Nano blocks are stateful
  and non-replayable, so one wallet never sends concurrently.

## Safety

- The wallet path and RPC are construction-bound; the model sees neither.
- Per-call cap enforced in deterministic code before any signing.
- Self-custodied: your seed stays on disk; nothing here holds your funds.

## Tests

```bash
python -m pytest -q          # structural
python tests/fail_closed_offline.py   # L1: dry_run spends nothing, over-cap refused
```

## License

MIT. Reuses [feeless402](https://github.com/feeless402/feeless402) (MIT) and the
x402nano exact dialect / 402nano facilitator.