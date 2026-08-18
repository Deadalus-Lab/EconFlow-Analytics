# SPDX-License-Identifier: AGPL-3.0-only
"""Lazy access to the generated tiers -- the Python twin of ``registry/loader.ts``.

Tier 1 (``manifest``) is always loaded: it is small and every routing decision
needs it. Tiers 2 and 3 are imported PER CATEGORY on first use, so a process that
touches three categories never pays for the other twenty-seven -- and a worker
never imports tier 3 at all.
"""

from __future__ import annotations

from functools import cache
from importlib import import_module
from typing import Any

from pydantic import BaseModel

from econflow_engine.generated.manifest import ENGINE_INFO, MANIFEST
from econflow_engine.kinds import NodeMeta
from econflow_engine.naming import category_package

__all__ = [
    "ENGINE_INFO",
    "MANIFEST",
    "authoring_model",
    "category_package",
    "category_of",
    "node_docs",
    "node_meta",
    "wire_model",
]


def category_of(fn: str) -> str:
    entry = MANIFEST.get(fn)
    if entry is None:
        raise KeyError(f"unknown node '{fn}' (not in the manifest of {len(MANIFEST)} nodes).")
    return str(entry["category"])


@cache
def _args_module(category: str) -> Any:
    return import_module(f"econflow_engine.generated.args.{category_package(category)}")


@cache
def _docs_module(category: str) -> Any:
    return import_module(f"econflow_engine.generated.docs.{category_package(category)}")


def node_meta(fn: str) -> NodeMeta:
    """Tier 2 metadata for one node."""
    meta: NodeMeta = _args_module(category_of(fn)).NODE_META[fn]
    return meta


def wire_model(fn: str) -> type[BaseModel]:
    """The model the ENGINE validates for one node."""
    model: type[BaseModel] = _args_module(category_of(fn)).wire_model(fn)
    return model


def authoring_model(fn: str) -> type[BaseModel]:
    """The model a GRAPH EDITOR edits for one node."""
    model: type[BaseModel] = _args_module(category_of(fn)).authoring_model(fn)
    return model


def node_docs(fn: str) -> dict[str, Any]:
    """Tier 3 documentation for one node. Never import this from a worker."""
    docs: dict[str, Any] = _docs_module(category_of(fn)).NODE_DOCS[fn]
    return docs
