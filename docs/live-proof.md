# Block 4 — live mainnet proof (recorded evidence)

Date (UTC): 2026-09-15. Rail identity: `nano_pay.server` create_app() run
locally on 127.0.0.1:8402 — the exact feeless402 merchant code reuses the
nano rail (RPC nodes, verify_block/settle_block); no adapter-internal
payment logic was rebuilt.

## Live spendless quote — real external merchant (nano-gpt.com)

`GET/POST https://nano-gpt.com/api/v1/chat/completions` with `x-x402: true`
through the adapter's `dry_run=true` path:

- status: 402
- parses a real world quote: price 0.00000266 XNO, pay_to
  `nano_3njeurfzgpwpnqjxoytfnqa7ezbgkordga8e8jg74ey77kww5d5emjjyzrhp`
- nothing spent (dry_run path never signs).

## Capped real redeem — local rail-reusing server

Payer wallet: `~/.nano-pay/wallet.json` = `nano_1jwwcrj9ps8rqi9rbpmw39mrar7ush7r1tibs9qhwwt146yi6m118rpmhru1`
(0.0005 XNO held, self-custodied; one of my own accounts — never goal evidence).
Payee (local server treasury): `nano_3idfzeqnh5rf5h8346sysctj66exm1c96b89g4y94ndjrwwmywuydz1bf8cs`
(also my own account; registered in NANO_AGENT_OWN_ACCOUNTS).

Two-phase adapter flow (dry_run=true quotes + mints single-use token, then
dry_run=false redeems that exact token under a 0.005 XNO cap):

- quote price: 0.0001 XNO; cap applied 0.005 XNO (min of arg and 0.01 default)
- redeem result: `PAID (Nano x402)` — status 200, amount 0.0001 XNO,
  block `66b5e8c352e10d6d7078cd9562f7501f41e318e3d4ac3c12b00511b1f96cd4cf`,
  settled True, ledger confirmed.

## Ledger confirmation (two independent public nodes)

- https://rpc.nano.to    : confirmed=true, amount=100000000000000000000000000 raw
- https://rainstorm.city/api : confirmed=true, amount=100000000000000000000000000 raw

## Explorer links

- https://blocklattice.io/block/66b5e8c352e10d6d7078cd9562f7501f41e318e3d4ac3c12b00511b1f96cd4cf
- https://nanexplorer.com/nano/block/66b5e8c352e10d6d7078cd9562f7501f41e318e3d4ac3c12b00511b1f96cd4cf

Honest note: both payer and payee are accounts I control, so this live run is
a correctness proof that the adapter signs and settles a real mainnet block
through the rail. It is NOT external adoption evidence and is never counted
as nano_tx evidence or as Nano's payment share.

## 2026-09-16 — first third-party Nano route quoted by this adapter

Until now every live quote in this file came from a route either I run or that
prices in a stablecoin. This is the first time the OpenAI Agents SDK tool has
read a **402 from a seller I do not operate, whose `accepts[0]` is
`nano:mainnet` / XNO**. That seller was found by scanning an independent index
(see `x402-discovery-study.md`).

Seller: `llmrt - LLM Red-Team Scanner (x402-nano)`,
`https://llmrt-companion.manhliemcn4euwlu.workers.dev` (autonomous service,
self-serve, no key, no KYC). Reproduce with the tool itself, spendlessly:

```python
# dry_run=True only reads the 402; it never signs and never broadcasts.
tool = make_nano_x402_tool()
await invoke(tool, json.dumps({
    "url": "https://llmrt-companion.manhliemcn4euwlu.workers.dev/pro/micro-402",
    "method": "GET", "dry_run": True}))
```

Observed output (verbatim shape):

```
QUOTE (dry run, nothing spent):
  price:  0.01 XNO
  pay_to: nano_1wkqb7jfojdnsikaheu95xmbbxrw379bqdxzuzoc9ka4jfodj5uy8naew6m8
  cap:    0.01 XNO (refusing to pay more than this)
```

and for their PRO route, `price: 8.1 XNO` against the same
`nano:mainnet` scheme.

What this proves: the adapter parses a **third-party** `nano:mainnet` accept,
resolves the amount from raw units to XNO, and applies its own spend cap
(0.01 XNO) before offering a redeem. What it does **not** prove: no payment was
made. The quote is spendless by construction, so this is client-readiness
evidence, not adoption. The 8.1 XNO route is deliberately above the cap and is
therefore refused at redeem time — also unpurchased.

The 0.01 XNO route is the one that matters: it is priced inside this project's
per-call cap, so a real paid call against a genuinely third-party Nano seller
is now a one-command operation rather than a design question.
