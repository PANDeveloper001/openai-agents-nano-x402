"""openai-agents-nano — a thin OpenAI Agents SDK Tool that lets any OpenAI
agent pay any x402-priced HTTP endpoint in self-custodied Nano (XNO).

This adapter REUSES the MIT-licensed feeless402 client (Wallet, RPC,
request_with_payment) verbatim. It rebuilds no Nano payment logic: the whole
x402 handshake (quote parse, price cap, local signing, retry with payment
header, on-ledger verification) lives in feeless402.
"""

from .tool import make_nano_x402_tool, NanoX402ToolError

__all__ = ["make_nano_x402_tool", "NanoX402ToolError"]