# SPDX-License-Identifier: AGPL-3.0-only
"""The dispatch gateway.

ONE entry point, :func:`run_method`, for every one of the 913 nodes. It resolves
the wrapper implementation, runs it through the tool pipeline, and turns every
outcome -- success, refusal, or an unimplemented body -- into the SAME response
shape, so a caller never has to guess which failure mode it is looking at.

WHY A GATEWAY RATHER THAN 913 ROUTES: the preflight, the reason-code mapping, the
cache verdict and the memory-class annotation are properties of A NODE CALL, not
of a particular method. Put them in one place and they cannot rot apart; spread
them across the wrapper modules and the 251st one will be subtly different.

WRAPPER RESOLUTION IS LAZY AND BY NAME. A category's module is imported the first
time one of its nodes is called, so a process that touches three categories never
imports the other twenty-seven -- and a body that has not been written yet fails
with a clear ``not-implemented`` rather than an import error at boot.
"""

from __future__ import annotations

import json
from collections.abc import Callable
from dataclasses import dataclass
from functools import cache
from importlib import import_module
from typing import Any

from econflow_engine.loader import MANIFEST, node_meta
from econflow_engine.mcp.make_tool import ToolResult, make_tool
from econflow_engine.naming import category_package, wrapper_module_name
from econflow_engine.node.cache import cache_key, is_cacheable

__all__ = ["NodeResponse", "list_methods", "run_method", "wrapper_callable"]


@dataclass(frozen=True, slots=True)
class NodeResponse:
    """The one response shape. ``state`` is the discriminator, not the status."""

    state: str  # "succeeded" | "refused" | "not-implemented"
    fn: str
    payload: Any = None
    handle: str | None = None
    reason_code: str | None = None
    message: str | None = None
    memory_class: str = "light"
    cache: str = "bypass"
    contract_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "state": self.state,
            "fn": self.fn,
            "payload": self.payload,
            "handle": self.handle,
            "reason_code": self.reason_code,
            "message": self.message,
            "memory_class": self.memory_class,
            "cache": self.cache,
            "contract_hash": self.contract_hash,
        }


@cache
def _wrapper_module_for(fn: str) -> Any:
    """Import the module that owns ``fn``, resolving the wrapper file by card."""
    entry = MANIFEST[fn]
    card_id = entry["card_id"]
    docs_free_lookup = _card_index()
    wrapper_file = docs_free_lookup[card_id]
    module = f"econflow_engine.wrappers.{category_package(entry['category'])}."
    return import_module(module + wrapper_module_name(wrapper_file))


@cache
def _card_index() -> dict[int, str]:
    """card id -> wrapper file, read from the committed method cards.

    The mapping lives in the artifact rather than in code because it is the same
    fact the wrapper generator used to lay the modules out; deriving it twice
    would let the two drift.
    """
    from pathlib import Path

    artifact = Path(__file__).resolve().parents[3] / "artifacts" / "method-cards.v1.json"
    cards = json.loads(artifact.read_bytes().decode("utf-8"))["cards"]
    return {int(c["id"]): str(c["wrapper_file"]) for c in cards}


def wrapper_callable(fn: str) -> Callable[..., Any]:
    """Resolve the wrapper body for one node. Raises ``AttributeError`` if absent."""
    implementation: Callable[..., Any] = getattr(_wrapper_module_for(fn), fn)
    return implementation


def list_methods(category: str | None = None) -> list[str]:
    """Every node name, optionally narrowed to one category."""
    if category is None:
        return sorted(MANIFEST)
    return sorted(fn for fn, e in MANIFEST.items() if e["category"] == category)


def run_method(fn: str, body: dict[str, Any], fetch_pointer: Any = None) -> NodeResponse:
    """Run one node and return the single response shape."""
    if fn not in MANIFEST:
        return NodeResponse(
            state="refused",
            fn=fn,
            reason_code="other",
            message=f"unknown method '{fn}' (not one of the {len(MANIFEST)} nodes).",
        )
    meta = node_meta(fn)
    verdict = "bypass" if not is_cacheable(_spec_view(meta), body) else "miss"
    common = {
        "fn": fn,
        "memory_class": meta.memory_class,
        "contract_hash": meta.contract_hash,
        "cache": verdict,
    }
    try:
        implementation = wrapper_callable(fn)
    except (AttributeError, ModuleNotFoundError) as exc:
        return NodeResponse(
            state="not-implemented",
            reason_code="other",
            message=f"{fn}: the wrapper body is not implemented yet ({exc}).",
            **common,
        )
    try:
        result: ToolResult = make_tool(fn, implementation, fetch_pointer)(body)
    except NotImplementedError as exc:
        # An empty stub is a KNOWN state, not a crash: the contract is already
        # live and callable, only the body is outstanding.
        return NodeResponse(
            state="not-implemented", reason_code="other", message=str(exc), **common
        )
    if not result.ok:
        return NodeResponse(
            state="refused", reason_code=result.reason_code, message=result.message, **common
        )
    return NodeResponse(
        state="succeeded", payload=result.payload, handle=result.handle, **common
    )


def _spec_view(meta: Any) -> dict[str, Any]:
    """The mapping shape the cache and memory-class rules read."""
    return {
        "fn": meta.fn,
        "arguments": [{"name": a.name, "kind": a.kind, "required": a.required} for a in meta.args],
        "register": meta.register_field,
        "memory_class": meta.memory_class,
    }


def cache_key_for(fn: str, body: dict[str, Any]) -> str:
    """The idempotency key for one call, over the RAW body."""
    return cache_key(_spec_view(node_meta(fn)), body)
