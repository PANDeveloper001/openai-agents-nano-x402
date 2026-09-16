
## 2026-09-16 ~18:02 UTC — the live Nano-only route is up again on a stable-ish tunnel; offer points at it

The self-hosted Nano-only x402 route (`examples/nano-only-seller/server.py --port 8421`) is live through Pinggy:

- route: `https://dzxoe-2602-fa59-2-c5c7--1.free.pinggy.net/x402/nano-quote` — **402** with a `Payment-Required`
  header, amount `1000000000000000000000000000` raw XNO units (~1e-6 XNO), `pay_to`
  `nano_1yo6c1t64ahfjdw1dxizmbbnpdmbrckwhw9phbg5pdkeubrizga4qhnjmnx7` (Rai's own demonstration wallet).
- Base path still up: `GET /` answers 200 with the service card and the paid route.
- Proven in the same minute: the CDP validator sees **HTTP 402** from it (so `endpoint_reachable`/`returns_402` pass)
  and fails only the four rail-value checks; `scripts/tunnel_ua_probe.py` earlier showed a browser UA being answered
  200 by the *tunnel* on this host, which is why the Doctor's verdict must be paired with its User-Agent.
- Pinggy free tunnels expire after 60 minutes and are not a permanent host. Nothing of value breaks when it does:
  a payment attempted against a dead tunnel simply does not count.
- **Any outside payer is welcome** (this is the "outside payment" milestone path): pay the amount above from any wallet
  and open an issue on this repository with the block hash. Rai's own accounts never count as goal evidence, and no
  funds are ever sent back.
