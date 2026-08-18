# SPDX-License-Identifier: AGPL-3.0-only
"""The MCP tool surface.

Three meta-tools:

    list_methods(category=None)   the catalogue, cheap: names only.
    describe_method(fn)           the full schema, description and example.
    run_method(fn, args)          execute.

WHY THE CATALOGUE IS NAMES ONLY: 913 full descriptions are most of the artifact,
and a model that has to read all of them to pick one has already lost. The
catalogue narrows, ``describe_method`` explains, ``run_method`` acts.

TRANSPORT IS NOT DECIDED HERE. These are plain functions returning plain
mappings; the caller decides how they are reached. Keeping the surface
transport-free is what lets the parity and conformance suites call it directly.
"""

from __future__ import annotations

from typing import Any

from econflow_engine.loader import ENGINE_INFO, MANIFEST
from econflow_engine.mcp.descriptions import describe_method
from econflow_engine.mcp.gateway import list_methods, run_method

__all__ = ["META_TOOLS", "catalogue", "describe_method", "engine_info", "list_methods",
           "run_method"]

META_TOOLS: tuple[str, ...] = ("list_methods", "describe_method", "run_method")


def engine_info() -> dict[str, Any]:
    """Provenance: the identity of the contract this build validates."""
    return dict(ENGINE_INFO)


def catalogue(category: str | None = None) -> list[dict[str, Any]]:
    """Names, categories and routing metadata -- deliberately WITHOUT descriptions.

    Non-executable nodes are listed with their status rather than hidden: a
    caller that cannot see them will keep proposing them.
    """
    return [
        {
            "fn": fn,
            "category": MANIFEST[fn]["category"],
            "card_id": MANIFEST[fn]["card_id"],
            "memory_class": MANIFEST[fn]["memory_class"],
            "executability": MANIFEST[fn]["executability"]["status"],
        }
        for fn in list_methods(category)
    ]
