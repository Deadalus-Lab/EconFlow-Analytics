# SPDX-License-Identifier: AGPL-3.0-only
"""Tool descriptions.

The text a model reads before it chooses a tool. Assembled from tier 3
(descriptions and input examples) plus the kind hints in
:mod:`econflow_engine.kinds`, so a description is never written twice.

WHY THE KIND HINT MATTERS MORE THAN THE PROSE: the argument description says what
the value MEANS; the kind hint says HOW to supply it. A handle socket cannot be
filled with a literal -- it needs an edge from a producing node -- and a path
cannot be a local file. A model that reads only the prose invents a plausible
local path every time.
"""

from __future__ import annotations

from typing import Any

from econflow_engine.kinds import KIND_LLM_HINT, NodeMeta
from econflow_engine.loader import node_docs, node_meta

__all__ = ["argument_lines", "describe_method", "tool_description"]


def argument_lines(meta: NodeMeta, docs: dict[str, Any]) -> list[str]:
    arg_docs: dict[str, str] = docs.get("args", {})
    lines: list[str] = []
    for arg in meta.args:
        marker = "required" if arg.required else "optional"
        text = arg_docs.get(arg.name, "").strip()
        hint = KIND_LLM_HINT.get(arg.kind)
        parts = [f"- {arg.name} [{arg.kind}, {marker}]"]
        if text:
            parts.append(text)
        if hint:
            parts.append(hint)
        if arg.enum:
            parts.append(f"One of: {', '.join(arg.enum)}.")
        if arg.name in meta.defaults:
            parts.append(f"Default: {meta.defaults[arg.name]!r}.")
        lines.append(" ".join(parts))
    return lines


def tool_description(fn: str) -> str:
    """One block of prose describing a node and every argument it accepts."""
    meta = node_meta(fn)
    docs = node_docs(fn)
    head = [docs.get("description", fn), ""]
    if meta.executability.status != "executable":
        head += [
            f"NOT AVAILABLE ({meta.executability.status}): {meta.executability.reason}",
            "",
        ]
    return "\n".join([*head, "Arguments:", *argument_lines(meta, docs)])


def describe_method(fn: str) -> dict[str, Any]:
    """The machine-readable half: the JSON Schema plus provenance.

    The JSON Schema is DERIVED from the same pydantic model that validates the
    call, never written alongside it. A schema that can disagree with its
    validator is worse than no schema, because the caller trusts it.
    """
    from econflow_engine.loader import wire_model

    meta = node_meta(fn)
    docs = node_docs(fn)
    return {
        "fn": fn,
        "category": meta.category,
        "card_id": meta.card_id,
        "contract_hash": meta.contract_hash,
        "memory_class": meta.memory_class,
        "register_field": meta.register_field,
        "executability": {
            "status": meta.executability.status,
            "reason_code": meta.executability.reason_code,
            "reason": meta.executability.reason,
            "blocked_arg": meta.executability.blocked_arg,
        },
        "description": tool_description(fn),
        "input_schema": wire_model(fn).model_json_schema(),
        "input_example": docs.get("input_example", {}),
        "defaults": dict(meta.defaults),
    }
