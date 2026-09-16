"""Count live `nano:*` accepts in the CDP x402 Bazaar index, scanning every page.

Page size is capped by the API (limit=1000 is silently reduced to 20), so this pages
with the API's own returned limit until `offset + len(items) >= total`.

Prints, as JSON: total resources, nano accepts, and the per-host breakdown plus the
distinct payTo accounts. Read-only, no key.
"""
from __future__ import annotations

import json
import urllib.request

BASE = "https://api.cdp.coinbase.com/platform/v2/x402/discovery/resources"
UA = {"User-Agent": "rai-agent/1.0 (x402 index recon)"}


def get(url: str) -> dict:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as f:
        return json.load(f)


def main() -> None:
    first = get(f"{BASE}?limit=1000")
    limit = first["pagination"]["limit"]
    total = first["pagination"]["total"]
    items = list(first["items"])
    offset = len(items)
    pages = 1
    while offset < total:
        page = get(f"{BASE}?limit={limit}&offset={offset}")
        batch = page["items"]
        if not batch:
            break
        items.extend(batch)
        offset += len(batch)
        pages += 1
        total = page["pagination"]["total"]

    hosts: dict[str, int] = {}
    paytos: dict[str, int] = {}
    networks: dict[str, int] = {}
    for it in items:
        for a in it.get("accepts") or []:
            net = str(a.get("network", ""))
            if net.startswith("nano:"):
                r = it.get("resource") or ""
                host = r.split("/")[2] if "//" in r else "?"
                hosts[host] = hosts.get(host, 0) + 1
                networks[net] = networks.get(net, 0) + 1
                p = str(a.get("payTo", ""))
                paytos[p] = paytos.get(p, 0) + 1
    out = {
        "pages_scanned": pages,
        "total_resources": total,
        "scanned": len(items),
        "nano_accepts": sum(hosts.values()),
        "nano_networks": networks,
        "nano_hosts": hosts,
        "distinct_nano_payto": len(paytos),
        "resources_with_nano": sum(
            1 for it in items if any(str(a.get("network", "")).startswith("nano:") for a in (it.get("accepts") or []))
        ),
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()