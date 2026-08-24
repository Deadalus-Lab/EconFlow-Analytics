# SPDX-License-Identifier: AGPL-3.0-only
"""Behaviour of three engine helpers that carried no test module of their own.

``naming``, ``kinds._strip_before_validators`` and ``mcp.registry.listing`` were
each reached only indirectly -- through the generators, through a built model,
through the MCP surface -- so the expression at the centre of each was covered by
nobody's assertion. Every rule below is stated against an OBSERVABLE OUTCOME
rather than the shape of the expression that produces it, which is what lets the
expression be rewritten and the rule still hold.

The three rules, and the input that separates each from its plausible neighbour:

* ``python_arg_name`` folds under ``re.ASCII``. A bare ``\\W`` on a str pattern is
  Unicode-aware, so ``café.value`` would keep its accent instead of folding.
* ``_strip_before_validators`` drops the ``BeforeValidator`` and KEEPS every other
  piece of metadata. Dropping the rest would silently discard a constraint.
* ``registry_list`` orders by handle. Handles are minted from a rising counter, so
  insertion order and sorted order agree through the public API and only a store
  filled out of order can tell the sort from no sort at all.
"""

from __future__ import annotations

import json
from typing import Annotated, get_args

import numpy as np
from annotated_types import Ge
from pydantic import BeforeValidator

from econflow_engine.kinds import _strip_before_validators
from econflow_engine.mcp import registry as mcp_registry
from econflow_engine.naming import category_package, python_arg_name, wrapper_module_name
from tests.support import ENGINE_ROOT

# The accent and the superscript are the two shapes that separate the ASCII fold
# from the Unicode one: both are word characters to a bare ``\W`` and neither may
# reach a Python identifier.
NON_ASCII_CASES: list[tuple[str, str]] = [
    ("café.value", "caf_value"),
    ("²super", "_super"),
    ("naïve.est", "na_ve_est"),
]


def test_a_non_ascii_character_folds_out_of_the_identifier() -> None:
    """Under a Unicode-aware fold the accent SURVIVES; that is the whole difference."""
    for wire_name, expected in NON_ASCII_CASES:
        assert python_arg_name(wire_name) == expected, (
            f"{wire_name!r} must fold to {expected!r}: a non-ASCII character is not "
            f"legal in a Python parameter name."
        )
        assert python_arg_name(wire_name).isascii()
        assert python_arg_name(wire_name).isidentifier()


def test_the_ascii_fold_reaches_the_two_sibling_rules() -> None:
    """``category_package`` and ``wrapper_module_name`` share the one pattern."""
    assert category_package("00-naïve-tools") == "c00_na_ve_tools"
    assert wrapper_module_name("c01_preparation_prechecks/auto_ordérs.py") == "auto_ord_rs"


def test_the_documented_ascii_cases_still_hold() -> None:
    """The docstring's own examples, so the fold cannot be widened into a no-op."""
    assert python_arg_name("p.adjust.method") == "p_adjust_method"
    assert python_arg_name("class") == "class_"
    assert python_arg_name("2x") == "_2x"
    assert category_package("00-data-utilities") == "c00_data_utilities"
    assert wrapper_module_name("c01_preparation_prechecks/auto_orders.py") == "auto_orders"


def test_no_node_renames_two_of_its_arguments_onto_one_name() -> None:
    """Collision-freedom, read from the committed artifact rather than from the rule.

    A collision here is a SILENTLY DROPPED argument at the adapter, not an error.
    The expectation comes from node-specs.json -- the source the rule is applied
    to -- so widening the fold shows up as a collision instead of as agreement.
    """
    specs = json.loads(
        (ENGINE_ROOT / "artifacts" / "node-specs.json").read_text(encoding="utf-8")
    )
    nodes = specs["nodes"]
    assert nodes, "node-specs.json declares no nodes; the walk would assert nothing."
    checked = 0
    for node in nodes:
        names = [argument["name"] for argument in node["arguments"]]
        renamed = [python_arg_name(name) for name in names]
        assert len(set(renamed)) == len(renamed), (
            f"node {node['fn']!r} renames two arguments onto one Python name: "
            f"{sorted(n for n in renamed if renamed.count(n) > 1)}"
        )
        assert all(name.isidentifier() for name in renamed)
        checked += len(names)
    assert checked > 1000, f"only {checked} argument names were examined; expected the tree."


def test_stripping_before_validators_keeps_every_other_piece_of_metadata() -> None:
    """The rebuilt alias must equal the one the tuple constructor produced."""
    base = Annotated[int, BeforeValidator(lambda v: v), Ge(0)]
    origin, *metadata = get_args(base)
    keep = [m for m in metadata if not isinstance(m, BeforeValidator)]

    stripped = _strip_before_validators(base)

    assert stripped == Annotated[tuple([origin, *keep])]
    assert get_args(stripped)[0] is int
    assert stripped.__metadata__ == (Ge(0),)
    assert not any(isinstance(m, BeforeValidator) for m in stripped.__metadata__)


def test_stripping_the_only_metadata_yields_the_bare_origin() -> None:
    """With nothing left to keep the alias collapses, and no empty Annotated is built."""
    stripped = _strip_before_validators(Annotated[float, BeforeValidator(lambda v: v)])
    assert stripped is float


def _entry(value: object, meta: object = None) -> mcp_registry._Entry:
    return mcp_registry._Entry(value=value, meta=meta)


def test_the_listing_is_ordered_by_handle_not_by_insertion() -> None:
    """A store filled out of order is the only input that can see the sort.

    Through ``registry_put`` the counter rises monotonically, so insertion order
    and sorted order agree and a listing that never sorted would look identical.
    """
    registry = mcp_registry._Registry()
    registry._entries["h_000009_zzzzzzzz"] = _entry([1, 2, 3], {"note": "third"})
    registry._entries["h_000002_aaaaaaaa"] = _entry(np.zeros((3, 4)))
    registry._entries["h_000005_mmmmmmmm"] = _entry("abc")

    listing = registry.listing()

    assert list(listing) == [
        "h_000002_aaaaaaaa",
        "h_000005_mmmmmmmm",
        "h_000009_zzzzzzzz",
    ]
    assert list(listing) != list(registry._entries), "insertion order must not survive"


def test_the_listing_is_a_snapshot_and_carries_no_values() -> None:
    """Value-free metadata, and a mapping that a later store mutation cannot reach."""
    registry = mcp_registry._Registry()
    registry._entries["h_000001_aaaaaaaa"] = _entry(np.zeros((3, 4)), {"note": "kept"})

    listing = registry.listing()
    registry._entries["h_000002_bbbbbbbb"] = _entry([9, 9])

    assert list(listing) == ["h_000001_aaaaaaaa"], "the snapshot must not track the store"
    row = listing["h_000001_aaaaaaaa"]
    assert row == {
        "handle": "h_000001_aaaaaaaa",
        "class": "ndarray",
        "length": 3,
        "dim": [3, 4],
        "meta": {"note": "kept"},
    }
    assert "value" not in row
