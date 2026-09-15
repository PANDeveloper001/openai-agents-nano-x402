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
