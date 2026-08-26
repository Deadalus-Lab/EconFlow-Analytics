# SPDX-License-Identifier: AGPL-3.0-only
"""The card declares which gates apply; the registry resolves them to primitives.

BOTH DIRECTIONS ARE ASSERTED, because each catches a different defect. A declared
name that resolves to nothing is a card documenting a gate the engine never runs.
A primitive absent from the registry is a rule no card can ever reach -- code that
looks like a gate and is one only in the sense that nothing calls it.

THE RESOLUTION PATH IS TESTED AGAINST A SYNTHETIC CARD. ``precondition_gates`` is
``null`` on all 600 real cards, so a test that only read the artifact would
exercise nothing and report success -- exactly the vacuous-gate shape this
repository refuses. The synthetic fixture drives the resolver directly; the
real-card tests then assert what the artifact can prove -- that the join reaches
every card -- and name the floor to raise when phase 2.2 populates the field.

THE FIELD WAS EMPTIED, NOT FOUND EMPTY, and a reader of these tests needs that.
Cards 96 to 100 carried fifteen free-prose sentences here: filesystem state,
argument grammar, a sheet checked against a workbook's real sheet list, an
ordering that is a security property, two post-conditions and a default. Fourteen
of the fifteen have no name in any vocabulary of cross-cutting numeric gates,
because every primitive takes a numeric vector, a panel or one scalar parameter.
They moved intact to ``validation_notes``, and ``precondition_gates`` became what
its name always claimed: a closed set of gate names, and nothing else.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

import pytest

from econflow_engine.gates import GATE_DETAIL_CODES, gates_for
from econflow_engine.gates.primitives import __all__ as PRIMITIVE_NAMES
from econflow_engine.gates.registry import (
    PRIMITIVES,
    card_gate_names,
    resolve_gates,
)
from econflow_engine.metrics import find_manifest

ENGINE_ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ENGINE_ROOT / "artifacts"
INVENTORY = find_manifest(Path(__file__))

#: Raise this when phase 2.2 starts populating ``precondition_gates`` with the
#: structured vocabulary. It is 0 today because the field is empty on all 600
#: cards -- measured, not assumed, by the tests below, which print the live
#: figure in their failure messages so the next reader knows what to raise it to.
#:
#: WHY A ZERO FLOOR IS NOT A VACUOUS ONE, which is the question a reader should
#: ask of any floor at zero. The walk it guards is not the only thing standing
#: between a mis-declared card and a green suite:
#: :func:`test_every_declared_precondition_gate_is_in_the_closed_vocabulary`
#: checks all 600 cards against the closed set with its denominator asserted, and
#: is red for a name outside that set whether or not any card declares one.
CARDS_WITH_DECLARED_GATES_FLOOR = 0


#: sha256 over the fifteen validation_notes sentences in card order, newline
#: joined. Measured, with the command in the test that reads it.
SENTENCES_SHA256 = "3210a469ea080e47d4448dd7818d387640a40d95b60b7bebe6d61d04138f3336"


def read(name: str) -> Any:
    return json.loads((ARTIFACTS / name).read_bytes().decode("utf-8"))


def inventory(section: str, key: str) -> int:
    """One asserted constant, read from the one manifest. NO DEFAULT.

    A missing manifest or a missing key raises here. Substituting a zero would
    turn the denominator below into a tautology and the run would still print as
    a pass -- which is the whole failure mode a closed-vocabulary gate exists to
    refuse.
    """
    return int(json.loads(INVENTORY.read_bytes().decode("utf-8"))[section][key])


def test_every_registry_key_is_a_declared_detail_code() -> None:
    """A key outside the closed set is a code no client was told about."""
    assert set(PRIMITIVES) <= set(GATE_DETAIL_CODES)


def test_no_primitive_is_unreachable_from_the_registry() -> None:
    """DIRECTION 2. A primitive no card can name is a rule that cannot be applied."""
    exported = {name for name in PRIMITIVE_NAMES if name.startswith("require_")}
    registered = {primitive.__name__ for primitive in PRIMITIVES.values()}
    assert exported == registered, (
        f"unreachable primitive(s): {sorted(exported - registered)}; "
        f"registered but unexported: {sorted(registered - exported)}"
    )


def test_the_registry_holds_the_eight_primitives() -> None:
    """The count is the anti-vacuity guard on the two set comparisons above."""
    assert len(PRIMITIVES) == 8


# --------------------------------------------------------------------------
# The resolution path, against a synthetic card
# --------------------------------------------------------------------------


def test_a_synthetic_card_resolves_its_declared_names_in_order() -> None:
    """DIRECTION 1, and the only test today that exercises resolution at all."""
    declared = ["precondition-sample-size", "precondition-rank", "precondition-panel"]
    resolved = resolve_gates(declared)
    assert [primitive.__name__ for primitive in resolved] == [
        "require_min_length",
        "require_full_rank",
        "require_balanced_panel",
    ]


def test_a_synthetic_card_may_mix_prose_with_gate_names() -> None:
    """A TRANSITIONAL SHAPE, KEPT AS A TEST OF THE RESOLVER, NOT OF THE TREE.

    No real card can reach this branch any more: the schema enum on
    ``precondition_gates`` refuses an entry that is not one of the eight names.
    ``resolve_gates`` still skips a spaced entry rather than raising on it, and
    this pins that behaviour so its removal is a visible diff rather than a
    silent tightening of what the resolver accepts.
    """
    declared = [
        "path: a non-empty string, NOT a directory, existing, size>0 bytes",
        "precondition-missing",
    ]
    resolved = resolve_gates(declared)
    assert [primitive.__name__ for primitive in resolved] == ["require_no_missing"]


def test_a_misspelt_gate_name_is_a_hard_error() -> None:
    """LOUD IN THE DIRECTION THAT MATTERS. Skipping it would run no gate silently."""
    with pytest.raises(KeyError, match="precondition-sampel-size"):
        resolve_gates(["precondition-sampel-size"])


def test_an_empty_declaration_resolves_to_no_gates() -> None:
    """All 600 cards are in exactly this state; it must not raise."""
    assert resolve_gates([]) == ()


# --------------------------------------------------------------------------
# The real cards
# --------------------------------------------------------------------------


def test_every_gate_name_declared_by_a_real_card_resolves(
    node_specs: dict[str, object],
) -> None:
    """Tolerant of the empty field of today; loud the moment a NAME appears.

    Walks every node in the catalogue, so a card that starts declaring a gate is
    checked from the first one -- there is no second switch to remember to throw.
    """
    nodes = node_specs["nodes"]
    assert isinstance(nodes, list)
    assert len(nodes) == inventory("artifacts", "n_nodes"), (
        f"walked {len(nodes)} node(s); the fixture is not the catalogue, and a "
        "floor of zero over an empty walk is what this line exists to refuse"
    )
    with_declared_gates = 0
    for node in nodes:
        fn = str(node["fn"])
        declared = card_gate_names(fn)
        resolved = gates_for(fn)  # raises KeyError on an unresolvable name
        if resolved:
            with_declared_gates += 1
        assert len(resolved) <= len(declared)
    assert with_declared_gates >= CARDS_WITH_DECLARED_GATES_FLOOR, (
        f"{with_declared_gates} node(s) now resolve a declared gate, below the floor "
        f"{CARDS_WITH_DECLARED_GATES_FLOOR}; the floor never falls"
    )


def test_the_card_join_actually_reached_the_catalogue(
    node_specs: dict[str, object],
) -> None:
    """ANTI-VACUITY. The walk above proves nothing if the join returned nothing.

    ``card_gate_names`` goes manifest -> ``card_id`` -> card. A broken join would
    raise, but a join that silently resolved to an empty card set would let the
    tolerant test above pass over zero nodes.

    THE WITNESS IS THE JOIN'S REACH, NOT THE FIELD'S CONTENTS, and that is the
    change. This test used to count the five cards carrying a non-empty
    ``precondition_gates`` and assert every entry of theirs contained whitespace
    -- it asserted the entries were PROSE, which was true of the tree and is the
    opposite of what the field now means. Those fifteen sentences are
    ``validation_notes`` and the field is empty on all 600 cards, so a count of
    non-empty ones is zero and proves nothing for anybody to hold on to.
    Asserting instead that the 1456 nodes reach every one of the 600 cards is a
    property of the JOIN, which is what this test was always about, and it stays
    true and stays load-bearing whatever the field goes on to carry.

    The vocabulary those entries must draw from is asserted by
    :func:`test_every_declared_precondition_gate_is_in_the_closed_vocabulary`,
    which is the check the old assertion's own failure message pointed at.
    """
    from econflow_engine.loader import MANIFEST

    nodes = node_specs["nodes"]
    assert isinstance(nodes, list)
    assert len(nodes) == inventory("artifacts", "n_nodes")

    reached = {int(MANIFEST[str(node["fn"])]["card_id"]) for node in nodes}
    on_card = {int(card["id"]) for card in read("method-cards.json")["cards"]}
    assert reached <= on_card, sorted(reached - on_card)[:10]
    assert len(reached) == inventory("artifacts", "n_cards"), (
        f"the manifest-to-card join reaches {len(reached)} of the catalogue's "
        f"{len(on_card)} card(s); it is reading a narrower artifact than it should"
    )
    assert all(card_gate_names(str(node["fn"])) == () for node in nodes), (
        "a node sees a non-empty precondition_gates field; the vocabulary gate is "
        "the check that now owns what it may hold"
    )


def test_an_unknown_method_name_is_refused() -> None:
    with pytest.raises(KeyError, match="not_a_node"):
        card_gate_names("not_a_node")


# --------------------------------------------------------------------------
# The closed vocabulary, over every card
# --------------------------------------------------------------------------


def _offenders(cards: list[dict[str, Any]], declared: set[str]) -> list[tuple[int, str]]:
    """``(card id, entry)`` for every entry the closed vocabulary does not admit."""
    return [
        (int(card["id"]), str(entry))
        for card in cards
        for entry in (card["precondition_gates"] or ())
        if str(entry) not in declared
    ]


def test_every_declared_precondition_gate_is_in_the_closed_vocabulary() -> None:
    """THE GATE. Every entry on every card, no named exception, denominator asserted.

    ZERO EXCEPTIONS IS THE DESIGN, not an accident of the tree being clean today.
    ``check-vocabulary.sh`` carries the reading in its own header: an exemption
    list accumulates until somebody deletes the rule to make the gate green. A
    card that wants to say something this vocabulary cannot say has a field for
    it -- ``validation_notes`` -- and that is the whole reason the two were split.
    """
    declared = set(read("node-specs.json")["vocabulary"]["precondition_gates"])
    assert declared, "an empty vocabulary would admit every entry and prove nothing"

    cards = read("method-cards.json")["cards"]
    offenders = _offenders(cards, declared)
    assert offenders == [], (
        f"{len(offenders)} entry/entries outside the closed vocabulary, across "
        f"{len({card_id for card_id, _ in offenders})} card(s): {offenders[:10]}. "
        f"The vocabulary is {sorted(declared)}. Prose describing what a wrapper "
        "validates belongs in validation_notes, not here."
    )

    expected = inventory("artifacts", "n_cards")
    assert len(cards) == expected, (
        f"examined {len(cards)} card(s) against a catalogue of {expected}; the walk "
        "did not visit the tree it claims to have checked"
    )


def test_the_vocabulary_check_refuses_a_card_that_names_an_unregistered_gate() -> None:
    """THE NEGATIVE CONTROL. A check nobody has watched refuse is not yet a check.

    Built here rather than planted in the corpus, so the control cannot be left
    behind in the committed tree by mistake.
    """
    declared = set(read("node-specs.json")["vocabulary"]["precondition_gates"])
    cards = [dict(card) for card in read("method-cards.json")["cards"]]
    cards[0]["precondition_gates"] = ["precondition-raank"]

    assert _offenders(cards, declared) == [(int(cards[0]["id"]), "precondition-raank")], (
        "a card naming 'precondition-raank' was accepted; the check reads a field "
        "nothing constrains and would admit any string at all"
    )


def test_the_sentences_the_gate_displaced_are_still_documented() -> None:
    """THE DECAY GUARD, and it is the reason the migration was safe to make.

    Emptying ``precondition_gates`` moved fifteen authored sentences to
    ``validation_notes``. Nothing else in the tree would notice if a later edit
    dropped them: they reach no hash, no schema count and no wire, so they would
    vanish inside a re-seal diff no reviewer reads. This pins them to the exact
    five cards that carried them, with the count they carried.

    IT IS AN EQUALITY, AND A CARD AUTHORED WITH NOTES TURNS IT RED ON PURPOSE.
    ``validation_notes`` is a field any card may use, so this map will need
    extending -- and the extension is the point. Adding a card here is a one-line
    diff that says a note was authored; a card silently LEAVING is the same
    one-line diff, and a reviewer sees both. A floor would only catch the second
    kind and would let the fifteen be replaced by fifteen others.
    """
    cards = {int(card["id"]): card for card in read("method-cards.json")["cards"]}
    #: card id -> how many notes it carries. Extend this when a card is authored
    #: with notes; never shrink it to match a card that lost some.
    carried = {96: 3, 97: 3, 98: 3, 99: 3, 100: 3}

    documented = {
        card_id: len(card["validation_notes"] or ())
        for card_id, card in cards.items()
        if card["validation_notes"]
    }
    assert documented == carried, (
        f"validation_notes is non-empty on {sorted(documented)} carrying "
        f"{documented}; this test expects exactly {carried}. If a card was newly "
        "AUTHORED with notes, add it to the map above. If a card LOST notes, that "
        "is the deletion this test exists to catch: cards 96-100 carry the fifteen "
        "sentences precondition_gates held before it became enum-typed, and nothing "
        "else in the tree would notice them going."
    )
    for card_id in carried:
        for note in cards[card_id]["validation_notes"]:
            assert " " in str(note), (
                f"card {card_id} carries the whitespace-free entry {note!r} in "
                "validation_notes; a gate NAME belongs in precondition_gates"
            )

    # THE COUNT IS NOT THE CONTENT. Everything above passes if all fifteen
    # sentences are replaced by fifteen different ones, and "summarised, reworded
    # for brevity, or dropped" is exactly what these were protected from. The
    # digest is over the sentences in card order, so a reword is as loud as a
    # deletion. Editing one deliberately means recomputing it, in a diff that
    # shows the sentence and the new digest together:
    #     python -c "import json,hashlib; d=json.load(open('artifacts/method-cards.json'));
    #     print(hashlib.sha256('\n'.join(n for c in d['cards'] if c['validation_notes']
    #     for n in c['validation_notes']).encode()).hexdigest())"
    sentences = [
        str(note)
        for card_id in sorted(cards)
        for note in (cards[card_id]["validation_notes"] or ())
    ]
    assert len(sentences) == 15, len(sentences)
    digest = hashlib.sha256("\n".join(sentences).encode("utf-8")).hexdigest()
    assert digest == SENTENCES_SHA256, (
        f"the fifteen sentences digest to {digest}, not {SENTENCES_SHA256}; one has "
        "been reworded or reordered. They were moved verbatim out of "
        "precondition_gates and are the documented refusals a user would otherwise "
        "meet undocumented -- if the edit is deliberate, recompute the constant."
    )
