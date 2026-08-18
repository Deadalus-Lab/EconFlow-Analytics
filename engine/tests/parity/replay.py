# SPDX-License-Identifier: AGPL-3.0-only
"""Replay every frozen verdict through the wire models.

The corpus (``artifacts/parity-fixtures.v1.json``) is NOT hand-written: every
verdict was produced by the frozen argument adapter
(the frozen corpus) with ``resolve_handle`` stubbed at
the "handle = non-empty string" gate only, INSIDE the exporter's environment.

Anything the Python model accepts may still come back 422 blocked-by-gate from a
wrapper -- that is CORRECT behaviour, not a parity failure: the statistical gates
are functions of REAL DATA and are therefore not replayable.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from pydantic import BaseModel

from econflow_engine.kinds import (
    NodeArgMeta,
    NodeExecutabilityMeta,
    NodeMeta,
    build_wire_model,
    validate_wire,
)
from econflow_engine.loader import wire_model
from econflow_engine.mcp.allowlists import is_pointer_handle_kind
from econflow_engine.node.store_pointers import SYNTHETIC_HANDLE

ENGINE_ROOT = Path(__file__).resolve().parent.parent.parent
ARTIFACTS = ENGINE_ROOT / "artifacts"


def _read(name: str) -> Any:
    return json.loads((ARTIFACTS / name).read_bytes().decode("utf-8"))


@dataclass(frozen=True, slots=True)
class Row:
    case: dict[str, Any]
    body: dict[str, Any]
    py_ok: bool
    py_reason: str | None

    @property
    def r_accepts(self) -> bool:
        return bool(self.case["verdict"]["verdict"] == "accept")

    @property
    def frozen_reason(self) -> str | None:
        code = self.case["verdict"]["reason_code"]
        return None if code is None else str(code)

    def show(self) -> str:
        body = json.dumps(self.body, default=str)[:220]
        py = "accept" if self.py_ok else f"reject/{self.py_reason or '-'}"
        return (
            f"{self.case['id']} [{self.case['family']}] body={body} "
            f"frozen={self.case['verdict']['verdict']}/{self.frozen_reason or '-'} py={py}"
        )


def _is_placeholder(value: object) -> bool:
    return isinstance(value, str) and value.startswith("<") and value.endswith(">")


def substitute_handle_placeholders(
    base: dict[str, Any], node: dict[str, Any] | None
) -> dict[str, Any]:
    """Replace ``<series_handle>``-style example placeholders with a REAL handle shape.

    The synthetic examples name their sockets rather than filling them; a
    placeholder is not a handle and would be refused by the registry gate for the
    wrong reason.
    """
    out = dict(base)
    if node is None:
        return out
    for arg in node["arguments"]:
        if not is_pointer_handle_kind(arg["kind"]):
            continue
        value = out.get(arg["name"])
        if _is_placeholder(value):
            out[arg["name"]] = SYNTHETIC_HANDLE
        elif isinstance(value, list):
            out[arg["name"]] = [
                SYNTHETIC_HANDLE if _is_placeholder(el) else el for el in value
            ]
    return out


def materialise(case: dict[str, Any], base: dict[str, Any]) -> dict[str, Any]:
    """Apply the case's patch semantics, IN ORDER.

    NOT JSON-merge-patch: ``drop`` (key removal) -> ``patch`` (set/override,
    never null) -> ``set_null`` (an EXPLICIT null). merge-patch cannot express
    both "explicit null" and "deletion", and here they are DIFFERENT cases --
    adapt_args reads the explicit null as ABSENT while the wire model rejects it.
    """
    body = dict(base)
    for key in case.get("drop") or []:
        body.pop(key, None)
    for key, value in (case.get("patch") or {}).items():
        body[key] = value
    for key in case.get("set_null") or []:
        body[key] = None
    return body


def _ad_hoc_model(case: dict[str, Any]) -> tuple[type[BaseModel], dict[str, str]]:
    """Build a model for a case that names no node, only ``arg_specs``."""
    args = tuple(
        NodeArgMeta(
            name=name,
            kind=spec["kind"],
            required=bool(spec["required"]),
            enum=tuple(spec["values"]) if spec.get("values") else None,
            allowed_vars=(
                tuple(spec["allowed_vars"]) if spec.get("allowed_vars") is not None else None
            ),
        )
        for name, spec in (case.get("arg_specs") or {}).items()
    )
    meta = NodeMeta(
        fn=case["id"].replace("/", "_").replace("-", "_"),
        category="<ad-hoc>",
        card_id=0,
        contract_hash="c-" + "0" * 64,
        register_field=None,
        executability=NodeExecutabilityMeta(status="executable"),
        memory_class="light",
        args=args,
        defaults={},
    )
    return build_wire_model(meta), {a.name: a.kind for a in args}


def divergence_key(case: dict[str, Any]) -> str:
    """The CLASS a divergence belongs to -- not the fixture id.

    ``<kind>/<mutation>`` for the kind-matrix and mutation families (the same
    pair recurs across hundreds of cases), the id itself for pointer and formula,
    and ``<family>/<fn>`` otherwise.
    """
    family = str(case["family"])
    if family == "pointer" or family.startswith("formula"):
        return str(case["id"])
    if case.get("kind") is not None and case.get("mutation") is not None:
        return f"{case['kind']}/{case['mutation']}"
    if case.get("fn") is not None:
        return f"{family}/{case['fn']}"
    return f"{family}/{case.get('mutation') or 'base'}"


def build_rows() -> tuple[list[Row], dict[str, Any], dict[str, Any], dict[str, Any]]:
    specs = _read("node-specs.v1.json")
    fixtures = _read("parity-fixtures.v1.json")
    divergences = _read("intentional-divergences.json")
    node_by_fn = {n["fn"]: n for n in specs["nodes"]}

    ad_hoc: dict[str, tuple[type[BaseModel], dict[str, str]]] = {}
    rows: list[Row] = []
    for case in fixtures["cases"]:
        fn = case.get("fn")
        node = node_by_fn.get(fn) if fn is not None else None
        base = substitute_handle_placeholders(node["input_example"] if node else {}, node)
        body = materialise(case, base)
        if fn is None:
            if case["id"] not in ad_hoc:
                ad_hoc[case["id"]] = _ad_hoc_model(case)
            model, kinds = ad_hoc[case["id"]]
        else:
            model = wire_model(fn)
            kinds = {a["name"]: a["kind"] for a in node["arguments"]} if node else {}
        ok, reason = validate_wire(model, body, kinds)
        rows.append(Row(case=case, body=body, py_ok=ok, py_reason=reason))
    return rows, specs, fixtures, divergences
