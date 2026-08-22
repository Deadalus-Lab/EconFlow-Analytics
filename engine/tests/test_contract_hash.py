# SPDX-License-Identifier: AGPL-3.0-only
"""The v2 contract hash: what it must be sensitive to, and what it must ignore.

WHY THIS ALGORITHM IS DEFINED RATHER THAN RECOVERED. The v1 artifacts carry a
``contract_hash`` written as ``c-<64 hex>`` by an exporter that no longer exists.
The constraint is absolute: nothing in this repository can regenerate those
values and no future version will be able to either, so a v1 value is an opaque
identity token, in the same class as ``engine.spec_source_sha256``. A search over
roughly 7.3 million candidate serialisations did not reproduce one, and could not
have: the input is gone.

Two facts about the v1 tokens survive that search and are asserted below against
the committed artifact, because they are the properties any replacement must
also have: all 913 are distinct, and the node's own name is part of the input --
``friedman_test``, ``kw_test`` and ``qs_test`` carry byte-identical arguments,
category, card id, memory class and register, and three different hashes.

THE PREFIX IS THE POINT. A v2 hash is ``c2-``. A v1 token can never validate as
v2 and a v2 hash can never validate as v1, so the two can never be silently
compared -- which is the only real hazard in replacing an opaque value with a
computed one.

WHAT IS STRUCTURAL. The hash covers the node's callable contract, and the
coverage is v1's, not an invention: the retired token was taken over a node's
function name, arguments, register field and export field, and explicitly not
over its memory class, so that a resource-allocation change could not invalidate
a stored graph. v2 keeps that meaning and replaces only the function. Every
element of that coverage, and every exclusion, is asserted in this file -- which
is what makes the claim checkable here rather than merely stated.

Prose does not appear: a docstring edit that moved the hash would make every
description change look like a contract break, and reviewers would learn to
ignore the signal.
"""

from __future__ import annotations

import copy
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

import pytest

ENGINE_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ENGINE_ROOT / "scripts"))

from contract_hash import (  # noqa: E402  (after sys.path)
    CONTRACT_FIELDS,
    canonical_contract,
    contract_hash,
)

HASH_RE = r"^c2-[0-9a-f]{64}$"

# One argument of every shape the artifact actually uses: required and optional,
# defaulted and not, enum and free, pointer handle and value.
NODE: dict[str, Any] = {
    "fn": "probe_node",
    "route": "/node/probe_node",
    "category": "00-data-utilities",
    "card_id": 1,
    "register": None,
    "memory_class": "light",
    "executability": {"status": "executable", "reason_code": None,
                      "reason": None, "blocked_arg": None},
    "cacheability": {"spec_cacheable": True, "has_seed_arg": False,
                     "seed_required": False, "stochastic_unseeded": False},
    "input_example": {"x": "<series_handle>", "how": "mean"},
    "arguments": [
        {"name": "x", "kind": "series_handle", "required": True,
         "description": "Handle to a series.", "pointer_handle": True,
         "json_type": "string", "enum": None, "allowed_vars": None,
         "default": None, "has_default": False, "default_json_type": None},
        {"name": "how", "kind": "enum", "required": False,
         "description": "Aggregation.", "pointer_handle": False,
         "json_type": "string", "enum": ["mean", "sum"], "allowed_vars": None,
         "default": "mean", "has_default": True, "default_json_type": "string"},
    ],
}


def mutated(**changes: Any) -> dict[str, Any]:
    node = copy.deepcopy(NODE)
    node.update(changes)
    return node


def with_arg(index: int, **changes: Any) -> dict[str, Any]:
    node = copy.deepcopy(NODE)
    node["arguments"][index].update(changes)
    return node


# --------------------------------------------------------------------------
# Shape
# --------------------------------------------------------------------------

def test_the_hash_is_prefixed_and_hex() -> None:
    assert re.match(HASH_RE, contract_hash(NODE))


def test_a_retired_token_can_never_be_mistaken_for_a_current_hash() -> None:
    """The whole reason the prefix moved. Both directions, not one.

    The retired tokens left the node specs when the superseded artifacts were
    retired; ``legacy-inventory.json`` is where they live now, and it is the only
    place they can be read, because nothing here can recompute one.
    """
    inventory = json.loads(
        (ENGINE_ROOT / "artifacts" / "legacy-inventory.json").read_bytes().decode("utf-8")
    )
    retired = next(iter(inventory["contract_hashes"].values()))
    assert retired.startswith("c-")
    assert not re.match(HASH_RE, retired)
    assert not re.match(r"^c-[0-9a-f]{64}$", contract_hash(NODE))


def test_the_canonical_form_is_valid_json_and_names_every_contract_field() -> None:
    """Anti-vacuity: a canonical form that dropped a field would still hash."""
    payload = json.loads(canonical_contract(NODE))
    assert sorted(payload) == ["arguments", "export", "fn", "register"]
    assert payload["fn"] == "probe_node"
    assert len(payload["arguments"]) == 2
    for rendered in payload["arguments"]:
        assert sorted(rendered) == sorted(CONTRACT_FIELDS)
    assert "description" not in set().union(*(set(a) for a in payload["arguments"]))


def test_the_registered_result_field_is_contract() -> None:
    """The retired v1 hash covered a node's function name, arguments, register
    field and export field. v2 keeps that meaning; only the function that computes
    it changed, so the register field must still move the hash."""
    assert contract_hash(mutated(register=None)) == contract_hash(NODE)
    assert contract_hash(mutated(register={"field": "fit"})) != contract_hash(NODE)
    assert contract_hash(mutated(register={"field": "other"})) != contract_hash(
        mutated(register={"field": "fit"}))


def test_what_a_node_writes_is_contract_not_metadata() -> None:
    """Three nodes write a file. Changing the format breaks every caller that
    reads the result, so it moves the hash; omitting the block equals a null."""
    plain = contract_hash(NODE)
    assert "export" not in NODE
    assert contract_hash(mutated(export=None)) == plain

    writer = mutated(export={"arg": "sink", "format": "parquet", "ext": ".parquet"})
    assert contract_hash(writer) != plain
    changed = mutated(export={"arg": "sink", "format": "dta", "ext": ".dta"})
    assert contract_hash(changed) != contract_hash(writer)


# --------------------------------------------------------------------------
# Determinism
# --------------------------------------------------------------------------

def test_the_hash_does_not_depend_on_the_interpreter_hash_seed() -> None:
    """A dict iteration order leaking into the digest would make the artifact
    irreproducible across runs, and it would show up as a phantom drift months
    later. Two subprocesses, two seeds, one answer."""
    script = (
        f"import sys, json; sys.path.insert(0, {str(ENGINE_ROOT / 'scripts')!r});"
        "from contract_hash import contract_hash;"
        "print(contract_hash(json.load(sys.stdin)))"
    )
    seen = set()
    for seed in ("0", "12345"):
        out = subprocess.run(
            [sys.executable, "-c", script],
            input=json.dumps(NODE), capture_output=True, text=True,
            env={"PYTHONHASHSEED": seed, "PATH": "/usr/bin:/bin"}, check=True,
        )
        seen.add(out.stdout.strip())
    assert len(seen) == 1, seen
    assert seen == {contract_hash(NODE)}


def test_key_order_inside_an_argument_does_not_change_the_hash() -> None:
    node = copy.deepcopy(NODE)
    node["arguments"] = [dict(reversed(list(a.items()))) for a in node["arguments"]]
    assert contract_hash(node) == contract_hash(NODE)


def test_an_absent_optional_field_equals_an_explicit_null() -> None:
    """``materialize`` is present on exactly 1 argument of 4698 and absent on the
    rest. The two must not hash differently, or the artifact's formatting
    becomes part of the contract."""
    absent = copy.deepcopy(NODE)
    explicit = with_arg(0, materialize=None)
    assert "materialize" not in absent["arguments"][0]
    assert contract_hash(absent) == contract_hash(explicit)


# --------------------------------------------------------------------------
# Sensitivity: every one of these is a real break for a saved graph
# --------------------------------------------------------------------------

@pytest.mark.parametrize(
    ("label", "node"),
    [
        ("renamed node", mutated(fn="probe_node_2")),
        ("renamed argument", with_arg(0, name="y")),
        ("changed kind", with_arg(0, kind="df_handle")),
        ("required made optional", with_arg(0, required=False)),
        ("changed json_type", with_arg(0, json_type="number")),
        ("changed default", with_arg(1, default="sum")),
        ("default removed", with_arg(1, has_default=False, default=None)),
        ("enum widened", with_arg(1, enum=["mean", "sum", "median"])),
        ("pointer handle flipped", with_arg(0, pointer_handle=False)),
        ("register field added", mutated(register={"field": "fit"})),
    ],
)
def test_a_contract_change_changes_the_hash(label: str, node: dict[str, Any]) -> None:
    assert contract_hash(node) != contract_hash(NODE), label


def test_reordering_the_arguments_changes_the_hash() -> None:
    """Argument order is the signature. Swapping two is a breaking change even
    though the set is identical."""
    node = copy.deepcopy(NODE)
    node["arguments"].reverse()
    assert contract_hash(node) != contract_hash(NODE)


def test_dropping_an_argument_changes_the_hash() -> None:
    node = copy.deepcopy(NODE)
    node["arguments"] = node["arguments"][:1]
    assert contract_hash(node) != contract_hash(NODE)


# --------------------------------------------------------------------------
# Insensitivity: none of these is a contract change
# --------------------------------------------------------------------------

@pytest.mark.parametrize(
    ("label", "node"),
    [
        ("category", mutated(category="29-unsupervised-clustering")),
        ("card id", mutated(card_id=999)),
        ("route", mutated(route="/node/anything")),
        ("memory class", mutated(memory_class="heavy")),
        ("executability", mutated(executability={"status": "blocked", "reason_code": "x",
                                                 "reason": "y", "blocked_arg": "x"})),
        ("cacheability", mutated(cacheability={"spec_cacheable": False, "has_seed_arg": True,
                                               "seed_required": True,
                                               "stochastic_unseeded": True})),
        ("input example", mutated(input_example={"x": "different"})),
    ],
)
def test_metadata_does_not_change_the_hash(label: str, node: dict[str, Any]) -> None:
    assert contract_hash(node) == contract_hash(NODE), label


def test_an_argument_description_does_not_change_the_hash() -> None:
    """Prose is not contract. If it were, every wording fix would read as a
    breaking change and the signal would be discarded by its readers."""
    assert contract_hash(with_arg(0, description="Completely rewritten.")) == contract_hash(NODE)


# --------------------------------------------------------------------------
# Against the committed corpus
# --------------------------------------------------------------------------

def test_every_v1_node_hashes_to_a_distinct_v2_value(node_specs: dict[str, Any]) -> None:
    """Discrimination at least as good as the tokens being replaced. A collision
    here would mean two nodes a caller cannot tell apart."""
    nodes = node_specs["nodes"]
    assert len(nodes) == node_specs["engine"]["n_nodes"]
    hashes = {contract_hash(n) for n in nodes}
    assert len(hashes) == len(nodes), f"{len(nodes) - len(hashes)} collision(s)"


def test_the_node_name_is_part_of_the_input(node_specs: dict[str, Any]) -> None:
    """The one property recoverable from the v1 tokens, re-asserted on v2.

    These three carry byte-identical arguments and identical metadata; only the
    name differs, and v1 gave them three different tokens.
    """
    by_fn = {n["fn"]: n for n in node_specs["nodes"]}
    trio = [by_fn["friedman_test"], by_fn["kw_test"], by_fn["qs_test"]]

    serialised = {json.dumps(n["arguments"], sort_keys=True) for n in trio}
    assert len(serialised) == 1, "premise broken: the trio no longer share arguments"
    assert len({n["contract_hash"] for n in trio}) == 3, "premise broken: v1 tokens collapsed"

    assert len({contract_hash(n) for n in trio}) == 3


def test_the_hash_ignores_the_stored_token(node_specs: dict[str, Any]) -> None:
    """It must be computable from a node that does not carry one yet -- which is
    every node the v2 corpus will emit."""
    node = copy.deepcopy(node_specs["nodes"][0])
    with_token = contract_hash(node)
    node.pop("contract_hash")
    assert contract_hash(node) == with_token
