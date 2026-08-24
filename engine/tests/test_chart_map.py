# SPDX-License-Identifier: AGPL-3.0-only
"""Every node resolves to a declared chart kind. Box 2.1.12, decision U35.

WHAT THIS CLOSES. ``econflow_engine.chart_spec`` has existed since the engine was
laid down and NOTHING declared which chart any method's result should get: the
emitter inferred a kind from the runtime type of whatever it was handed, so the
catalogue had no opinion at all and two nodes returning the same Python type were
drawn the same way however differently they should read. ``chart_kind`` on the
method card is that opinion, written once per card, next to the
``output_key_fields`` it is derived from.

THE DERIVATION RULE, so a reader can check any card against it. ``chart_kind``
names the single chart a client draws for the card's PRINCIPAL result -- the
object the method exists to produce, not its diagnostics. Read the card's
``output_key_fields`` in order together with its ``method`` text, and take the
first of these that describes that principal result:

    heatmap     a matrix read over two labelled axes: a correlation, covariance
                or distance matrix; a transition, adjacency or exposure matrix; a
                spillover or connectedness table; an impulse-response surface over
                horizon x pair; a time-frequency grid.
    multi-line  two or more series over one shared axis: an impulse response with
                bands, a forecast with intervals, a decomposition into components,
                factor or regime paths, a fan chart, a curve family.
    line        exactly one series over an ordered axis.
    table       named scalars, or one row per term: coefficients, standard errors,
                test statistics, indices, weights, diagnostics.
    none        nothing to display: file and format I/O, calendars, parsers,
                schema verdicts, handles, and transforms whose output is another
                node's input.

``none`` IS A REAL ANSWER AND IS NOT A SHRUG. 23 of the 600 cards carry it, all of
them plumbing that produces no displayable result, and stretching one of the four
chart kinds to cover them would have made every one of those declarations a lie.

THE DENOMINATOR IS ASSERTED, NOT ASSUMED. A resolution walk that silently visited
no node would pass every assertion below, which is the one failure this file
exists to refuse. The node count is read from ``.github/inventory.json`` with NO
default, so a manifest that cannot be read is a failure rather than a floor of
zero -- the exact shape that made run_verifications.sh's collected floor vacuous
inside the image for its whole existence.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest

ENGINE_ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ENGINE_ROOT / "artifacts"
INVENTORY = ENGINE_ROOT.parent / ".github" / "inventory.json"


def read(name: str) -> Any:
    return json.loads((ARTIFACTS / name).read_bytes().decode("utf-8"))


def inventory(section: str, key: str) -> int:
    """One asserted constant, read from the one manifest. NO DEFAULT.

    A missing manifest or a missing key raises here. Substituting a zero would
    turn every comparison below into a tautology, and the run would still print
    as a pass.
    """
    return int(json.loads(INVENTORY.read_bytes().decode("utf-8"))[section][key])


def resolve(nodes: list[dict[str, Any]], cards: list[dict[str, Any]]) -> dict[str, str]:
    """node fn -> the chart kind its card declares.

    Raises ``KeyError`` on a node whose ``card_id`` names no card, which is the
    other half of the property: a node that resolves to nothing is not a node
    that resolves to ``none``.
    """
    by_id = {int(c["id"]): c for c in cards}
    return {n["fn"]: by_id[int(n["card_id"])]["chart_kind"] for n in nodes}


def test_every_node_resolves_to_a_declared_chart_kind() -> None:
    specs = read("node-specs.json")
    cards = read("method-cards.json")["cards"]
    declared = set(specs["vocabulary"]["chart_kinds"])
    assert declared, "the chart vocabulary is empty, so nothing below proves anything"

    resolved = resolve(specs["nodes"], cards)
    undeclared = sorted(
        (fn, kind) for fn, kind in resolved.items() if kind not in declared
    )
    assert undeclared == [], undeclared[:10]

    expected = inventory("artifacts", "n_nodes")
    assert len(resolved) == expected, (
        f"resolved {len(resolved)} node(s) against a catalogue of {expected}; the walk "
        "did not visit the tree it claims to have checked"
    )


def test_the_resolution_refuses_a_card_that_declares_an_unknown_kind() -> None:
    """THE NEGATIVE CONTROL, kept rather than run once and deleted.

    A check that has never been observed failing is a check nobody knows works.
    The mis-declared card is built here rather than planted in the corpus, so the
    control cannot be left behind in the committed tree by mistake.
    """
    specs = read("node-specs.json")
    declared = set(specs["vocabulary"]["chart_kinds"])
    cards = [dict(c) for c in read("method-cards.json")["cards"]]
    cards[0]["chart_kind"] = "sankey"

    resolved = resolve(specs["nodes"], cards)
    undeclared = [fn for fn, kind in resolved.items() if kind not in declared]
    assert undeclared, (
        "a card declaring 'sankey' was accepted; the check reads a field nothing "
        "constrains, and would accept any value at all"
    )


def test_every_card_declares_a_chart_kind_from_the_closed_set() -> None:
    declared = set(read("node-specs.json")["vocabulary"]["chart_kinds"])
    cards = read("method-cards.json")["cards"]
    offenders = sorted(
        (c["id"], c.get("chart_kind")) for c in cards if c.get("chart_kind") not in declared
    )
    assert offenders == [], offenders[:10]
    assert len(cards) == inventory("artifacts", "n_cards")


def test_no_declared_chart_kind_is_dead() -> None:
    """A vocabulary entry no card uses is a dead entry, exactly as in
    intentional-divergences.json: it widens what the catalogue accepts and
    nothing exercises it."""
    declared = set(read("node-specs.json")["vocabulary"]["chart_kinds"])
    used = {c["chart_kind"] for c in read("method-cards.json")["cards"]}
    assert declared - used == set(), sorted(declared - used)


def test_precondition_gates_names_exactly_what_the_resolver_accepts() -> None:
    """THREE HOMES FOR ONE CLOSED SET, AND THIS IS WHAT STOPS THEM DRIFTING.

    The set of gate names a card may declare is written down three times, because
    each home enforces it against a different reader:

        ``gates/registry.py``            ``PRIMITIVES`` -- what ``resolve_gates``
                                         accepts at run time. AUTHORITATIVE.
        ``corpus/_vocabulary.json``      what a card author is told is legal,
                                         carried into the sealed artifact.
        ``method-cards.schema.json``     what the artifact-drift job validates.

    THE DEFECT THIS TEST EXISTS FOR WAS REAL AND LIVED HERE. Until 2026-08-24 the
    vocabulary declared ``gate_cross_section_only`` and ``gate_sliding_window_step``
    -- the normative gate FUNCTION names -- while ``resolve_gates`` accepted the
    eight ``precondition-*`` DETAIL CODES. Two closed sets, both called
    ``precondition_gates``, with an EMPTY intersection: the corpus authorised
    exactly the two tokens its own consumer raised ``KeyError`` on. It survived
    because the test standing here compared the vocabulary against
    ``gates.__all__`` and never against the resolver, and nothing compared a card
    against either. A closed set can be closed over the wrong namespace, and only
    resolving one home through another shows it.

    ``gate_sliding_window_step`` could never have been a precondition in any case:
    ``gates/__init__.py`` documents it as a DETECTOR, not a blocker -- it returns a
    step and the caller decides.
    """
    from econflow_engine.gates import GATE_DETAIL_CODES
    from econflow_engine.gates.registry import PRIMITIVES

    accepted = set(PRIMITIVES)
    assert accepted, "an empty resolver would make every comparison below vacuous"

    vocabulary = read("node-specs.json")["vocabulary"]["precondition_gates"]
    assert set(vocabulary) == accepted, (
        f"the corpus vocabulary is {sorted(vocabulary)} and resolve_gates accepts "
        f"{sorted(accepted)}; a name in one and not the other is either a card "
        "authorised to declare a gate that raises, or a gate no card may reach"
    )

    schema = json.loads(
        (ARTIFACTS / "schema" / "method-cards.schema.json").read_bytes().decode("utf-8")
    )
    enum = schema["$defs"]["card"]["properties"]["precondition_gates"]["items"]["enum"]
    assert set(enum) == accepted, (
        f"the schema admits {sorted(enum)}; the artifact-drift job would pass an "
        "artifact the resolver refuses"
    )

    assert accepted <= set(GATE_DETAIL_CODES), sorted(accepted - set(GATE_DETAIL_CODES))


@pytest.mark.parametrize("field", ["chart_kind"])
def test_the_authored_chart_field_reaches_the_artifact_from_the_corpus(field: str) -> None:
    """``chart_kind`` is AUTHORED, not derived: nothing in the tree can compute
    which chart a method's result deserves. It therefore lives in the corpus and
    is carried through, which is the opposite of ``embed_text``."""
    import sys

    sys.path.insert(0, str(ENGINE_ROOT / "scripts"))
    import gen_artifacts as G

    categories, _ = G.read_corpus()
    authored = {c["id"]: c[field] for block in categories for c in block["cards"]}
    emitted = {c["id"]: c[field] for c in read("method-cards.json")["cards"]}
    assert authored == emitted
