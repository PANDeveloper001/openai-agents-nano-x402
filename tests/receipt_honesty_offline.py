"""Offline proof for L11 (block 3): the redeem result label is truthful.

A receipt whose block did NOT settle (settled False) or whose settlement is
indeterminate must not be headed PAID; only a ledger-confirmed settled
receipt may be headed PAID. The block hash and the ledger verdict are always
shown. No real Nano network and no wallet spend happen here; drives the
_format_receipt label logic directly.

Prints RECEIPT_HONESTY_OK on success (the ledger oracle's expected output);
any broken assertion raises before that marker prints.
"""
import os
import sys
import types

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from openai_agents_nano.tool import _format_receipt


def resp(status=200, text="ok"):
    return types.SimpleNamespace(status_code=status, text=text)


def fmt(settled, ledger, note, block="B1"):
    rec = {
        "amount_xno": "0.0001",
        "pay_to": "nano_testpay",
        "block": block,
        "settled": settled,
        "ledger": ledger,
    }
    if note:
        rec["note"] = note
    return _format_receipt(resp(), rec, "0.05")


def main():
    # settled True -> PAID is the truthful label, block shown.
    out = fmt(True, "confirmed", "payment is on the ledger")
    assert out.startswith("PAID (Nano x402):"), f"settled True must be headed PAID: {out!r}"
    assert "B1" in out, "a settled receipt must show the block hash"

    # settled False -> must NOT be headed PAID (block not on ledger).
    out = fmt(False, "absent", "merchant refused and the ledger does not hold the block; nothing was paid")
    assert not out.startswith("PAID"), f"settled False must never start 'PAID: {out!r}"
    assert "NOT PAID" in out, f"settled False must name the failure: {out!r}"
    assert "B1" in out, "the block hash must still be shown"

    # settled indeterminate -> must NOT be headed PAID, must warn about re-pay.
    out = fmt("indeterminate", "unconfirmed", "no confirmation from merchant or ledger; check this block hash before paying again")
    assert not out.startswith("PAID"), f"indeterminate must never start 'PAID: {out!r}"
    assert "UNCONFIRMED" in out or "UNCERTAIN" in out, out
    assert "B1" in out, "the block hash must still be shown"

    print("RECEIPT_HONESTY_OK")


if __name__ == "__main__":
    main()