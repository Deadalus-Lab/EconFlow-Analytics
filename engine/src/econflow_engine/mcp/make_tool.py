# SPDX-License-Identifier: AGPL-3.0-only
"""Tool factory.

Turns one node spec into one callable tool. The pipeline is fixed and each stage
has exactly one job:

    preflight   -> is this node executable at all?
    validate    -> the wire model (kinds.py); produces the reason code
    adapt       -> handles become objects, wire names become Python names
    call        -> the wrapper body
    register    -> heavy results go to the registry, only a handle comes back
    serialise   -> to_mcp, so nothing unserialisable escapes

THE PREFLIGHT IS FIRST FOR A REASON: a node blocked by a schema-versus-gate
mismatch must answer 422 BEFORE the caller pays for a store fetch and a full
execution, with a message that says the SCHEMA is at fault and not their data.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import Any

from econflow_engine.errors import GateError
from econflow_engine.kinds import NodeMeta, validate_wire
from econflow_engine.loader import node_meta, wire_model
from econflow_engine.mcp.adapters import adapt_args
from econflow_engine.mcp.registry import registry_put
from econflow_engine.node.executability import is_non_executable
from econflow_engine.serialize import to_mcp

__all__ = ["ToolResult", "make_tool"]


@dataclass(frozen=True, slots=True)
class ToolResult:
    ok: bool
    payload: Any = None
    reason_code: str | None = None
    message: str | None = None
    handle: str | None = None


def make_tool(
    fn: str, implementation: Callable[..., Any], fetch_pointer: Any = None
) -> Callable[[dict[str, Any]], ToolResult]:
    """Build the callable that serves one node."""
    meta: NodeMeta = node_meta(fn)
    model = wire_model(fn)
    kinds = {a.name: a.kind for a in meta.args}

    def call(body: dict[str, Any]) -> ToolResult:
        if is_non_executable(meta):
            return ToolResult(
                ok=False,
                reason_code=meta.executability.reason_code or "other",
                message=meta.executability.reason,
            )
        ok, reason = validate_wire(model, body, kinds)
        if not ok:
            return ToolResult(
                ok=False,
                reason_code=reason,
                message=f"{fn}: the arguments were refused by the wire contract ({reason}).",
            )
        try:
            kwargs = adapt_args(meta, body, fetch_pointer)
            result = implementation(**kwargs)
        except GateError as exc:
            return ToolResult(ok=False, reason_code=exc.reason_code, message=str(exc))
        handle = registry_put(result, meta={"fn": fn}) if meta.register_field else None
        return ToolResult(ok=True, payload=to_mcp(result), handle=handle)

    call.__name__ = f"tool_{fn}"
    call.__doc__ = f"Run node {fn} (card #{meta.card_id}, category {meta.category})."
    return call
