"""Structural tests for L0: the tool factory returns an OpenAI Agents SDK
FunctionTool named nano_x402_fetch that reuses feeless402's client.

Offline and deterministic: no real Nano network, no wallet spend.
"""
import asyncio
import json
import os
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from agents.tool_context import ToolContext

from openai_agents_nano.tool import make_nano_x402_tool


async def invoke(tool, json_args: str) -> str:
    ctx = ToolContext(
    context={"nano": True},
    tool_name=tool.name,
    tool_arguments=json_args,
    tool_call_id="call_test_01",
)
    return await tool.on_invoke_tool(ctx, json_args)


def _make(wallet_path, default_max_xno="0.01"):
    return make_nano_x402_tool(wallet_path=wallet_path, default_max_xno=default_max_xno)


def test_returns_named_functiontool():
    with tempfile.TemporaryDirectory() as td:
        tool = _make(str(Path(td) / "w.json"))
        assert tool.name == "nano_x402_fetch"
        assert hasattr(tool, "on_invoke_tool")


def test_factory_binds_wallet_not_exposing_it_to_model():
    with tempfile.TemporaryDirectory() as td:
        tool = _make(str(Path(td) / "wallet.json"))
        # Wallet path and RPC are construction-bound, never tool args.
        schema = json.dumps(tool.params_json_schema)
        assert "wallet" not in schema.lower()
        assert "rpc" not in schema.lower()


def test_dry_run_returns_text_not_exception():
    with tempfile.TemporaryDirectory() as td:
        tool = _make(str(Path(td) / "w.json"))
        out = asyncio.run(
            invoke(tool, json.dumps({"url": "https://example.invalid/x", "dry_run": True}))
        )
        assert isinstance(out, str)
        assert out.startswith("ERROR") or out.startswith("NOTE") or "QUOTE" in out


def test_cap_validation_returns_refusal_string():
    with tempfile.TemporaryDirectory() as td:
        tool = _make(str(Path(td) / "w.json"), default_max_xno="0.02")
        out = asyncio.run(
            invoke(tool, json.dumps({"url": "https://example.invalid/x", "max_xno": "-5", "dry_run": True}))
        )
        assert out.startswith("REFUSED")