"""Offline tests for the published paid-endpoint offer and the keyless route checker.

Offline on purpose: the LIVE claims (a real 402, the real payTo, the CDP validator
verdict) are checked by scripts/verify_offer.py, which needs the network. These tests
pin the parts that must never drift even with no network: the offer's shape, the
Nano-accept parsing, and the honesty fields.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_route import nano_accepts  # noqa: E402

OFFER = json.loads((ROOT / "docs" / "offer" / "paid-endpoint.json").read_text())


def test_offer_declares_a_nano_accept():
    a = OFFER["accepts"][0]
    assert a["network"] == "nano:mainnet"
    assert a["asset"] == "XNO"
    assert a["scheme"] == "exact"
    assert a["amount"].isdigit() and int(a["amount"]) > 0
    assert a["payTo"].startswith("nano_") and len(a["payTo"]) in (64, 65)


def test_offer_does_not_claim_rai_owns_the_example_route():
    """The example route is operated by someone else; claiming otherwise would be a false claim."""
    assert "NOT Rai" in OFFER["accepts"][0]["payTo_owner"]


def test_offer_states_its_indexing_status_honestly():
    idx = OFFER["indexing"]
    assert idx["status"] in {"not indexed yet", "indexed"}
    if idx["status"] == "not indexed yet":
        # An unindexed offer must say why, and what would change it.
        assert idx.get("status_reason") and idx.get("next_action")
    assert OFFER["honest_limits"], "an offer with no stated limits is marketing, not an offer"


def test_nano_accept_parser_selects_xno_and_ignores_usdc():
    accepts = [
        {"scheme": "exact", "network": "eip155:8453", "asset": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913"},
        {
            "scheme": "exact",
            "network": "nano:mainnet",
            "asset": "XNO",
            "amount": "1",
            "payTo": "nano_x",
            "maxTimeoutSeconds": 300,
        },
    ]
    got = nano_accepts(accepts)
    assert len(got) == 1
    assert got[0]["network"] == "nano:mainnet" and got[0]["asset"] == "XNO"


def test_nano_accept_parser_is_empty_for_a_usdc_only_route():
    """The control: without this, 'payable_in_nano' would be a constant, not a check."""
    got = nano_accepts([{"scheme": "exact", "network": "eip155:8453", "asset": "0x8335"}])
    assert got == []
