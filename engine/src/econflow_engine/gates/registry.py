# SPDX-License-Identifier: AGPL-3.0-only
"""Which gates apply to which method: the card declares, this module resolves.

TWO SOURCES OF TRUTH, EACH ANSWERING ITS OWN QUESTION, AND THAT SPLIT IS THE
DESIGN. What a rule DOES is Python -- :mod:`econflow_engine.gates.primitives` is
the only place a refusal is written. WHICH rules apply to a method is the CARD:
``precondition_gates`` in ``artifacts/method-cards.json``, authored in
``engine/corpus/<category>.json`` beside the ``when`` / ``when_not`` prose that
justifies them. Putting the second fact in Python would mean a 600-branch table
that no reviewer of a method card could see, and a method's preconditions are
part of what the card documents.

WHAT THE FIELD HOLDS TODAY -- MEASURED, 2026-08-24::

    python3 -c "import json,collections; d=json.load(open('artifacts/method-cards.json'));
    print(collections.Counter(x['precondition_gates'] is None for x in d['cards']))"
    # Counter({True: 600})

All 600 cards carry ``null``. The field is a closed set of gate names and holds
nothing else: ``corpus/_vocabulary.json``, the ``enum`` in
``artifacts/schema/method-cards.schema.json`` and :data:`PRIMITIVES` below are
one set, which ``tests/test_chart_map.py`` asserts, and
``tests/test_gates_registry.py`` walks every card against it. Phase 2.2 authors
the first real declaration.

WHAT IT USED TO HOLD, because this module's own reading of the field was the
argument that settled it. Cards 96 to 100 carried fifteen free-prose sentences
here -- filesystem state, argument grammar, a sheet checked against a workbook's
real sheet list, a validate-before-fetch ordering, two post-conditions and a
default. Every primitive below takes a numeric vector, a panel or one scalar
parameter, so fourteen of the fifteen had no name in this vocabulary and never
could have. They are ``validation_notes`` on the same five cards, rendered into
the same wrapper docstrings, and none was reworded to fit.

THE DISCRIMINATOR BELOW IS A LIVE SILENT SKIP, AND IT IS STILL HERE ON PURPOSE.
:func:`_is_prose` skips an entry containing whitespace instead of raising on it,
which was how the two shapes coexisted without a flag day.

BE PRECISE ABOUT WHAT PROTECTS IT, BECAUSE THE SCHEMA DOES NOT. The ``enum`` on
``precondition_gates`` is checked by ``check-jsonschema`` in ``ci.yml`` only.
:func:`_gates_by_card_id` below reads ``artifacts/method-cards.json`` off disk
with a bare ``json.loads`` and validates nothing, so at RUN TIME a spaced entry
reaching this module is skipped in silence and the wrapper runs no gate while
reporting success. That cannot happen from the committed artifact today -- the
field is empty on all 600 cards -- but it is a property of the tree, not of this
function, and phase 2.2 is what makes the branch live.

It stays because removing it tightens what ``resolve_gates`` accepts, and that is
a change to a shipped module worth its own diff rather than a line inside a
migration. ``tests/test_gates_registry.py`` pins the behaviour so that diff
cannot be a silent one. The durable fix is to raise here and let the enum be the
only place a spaced entry is described as legal.
"""

from __future__ import annotations

import json
from collections.abc import Callable, Mapping, Sequence
from functools import cache
from pathlib import Path
from typing import Final

from econflow_engine.gates.primitives import (
    require_balanced_panel,
    require_cross_section,
    require_full_rank,
    require_in_range,
    require_min_length,
    require_no_missing,
    require_regular_frequency,
    require_variance,
)

__all__ = ["PRIMITIVES", "GatePrimitive", "card_gate_names", "gates_for", "resolve_gates"]

#: Every primitive refuses by raising; none returns a value. The uniform shape is
#: what lets the registry hold them in one mapping.
GatePrimitive = Callable[..., None]

#: detail code -> the primitive that emits it. The KEY is the detail code
#: deliberately: a card names the rule by the same token the refusal carries, so a
#: client that sees ``precondition-rank`` can look up exactly which gate produced
#: it. ``tests/test_gates_registry.py`` asserts the mapping is total in both
#: directions -- no key outside ``GATE_DETAIL_CODES``, and no primitive absent.
PRIMITIVES: Final[Mapping[str, GatePrimitive]] = {
    "precondition-sample-size": require_min_length,
    "precondition-missing": require_no_missing,
    "precondition-degenerate": require_variance,
    "precondition-frequency": require_regular_frequency,
    "precondition-domain": require_in_range,
    "precondition-rank": require_full_rank,
    "precondition-panel": require_balanced_panel,
    "precondition-cross-section": require_cross_section,
}


def _is_prose(entry: str) -> bool:
    """A declared gate name is one hyphenated token; anything spaced is a sentence."""
    return any(character.isspace() for character in entry)


def resolve_gates(names: Sequence[str]) -> tuple[GatePrimitive, ...]:
    """Turn a card's ``precondition_gates`` list into the primitives it names.

    Prose entries are skipped. A name that is not prose and does not resolve is a
    CORPUS BUG and raises: silently skipping it would mean a card that documents a
    gate the engine never runs, which is worse than no declaration at all.
    """
    resolved: list[GatePrimitive] = []
    for entry in names:
        if _is_prose(entry):
            continue
        primitive = PRIMITIVES.get(entry)
        if primitive is None:
            raise KeyError(
                f"the card declares precondition gate {entry!r}, which is not a "
                f"registered primitive. Known: {sorted(PRIMITIVES)}. A card names a "
                "gate by the detail code its refusal carries."
            )
        resolved.append(primitive)
    return tuple(resolved)


@cache
def _gates_by_card_id() -> Mapping[int, tuple[str, ...]]:
    """``card id -> the raw precondition_gates entries``, read once.

    RETAINS THE FIELD, NOT THE CARD. Holding all 600 parsed cards to serve a field
    that is non-null on five of them kept 11 MB resident for the life of the
    process; the projection is 600 short tuples, five of them non-empty.

    A SECOND READER OF ``method-cards.json``, AND THAT IS THE DEBT HERE.
    ``mcp/gateway.py`` reads the same artifact behind its own ``@cache`` for its
    own projection (``card id -> wrapper_file``), so the file is parsed twice per
    process and ``parents[3]`` is written twice -- correct only while both modules
    sit at the same depth, which this change moved. The right home for one shared
    card accessor is ``loader.py`` (both already import it); ``gates`` must not
    import ``mcp``, because ``mcp.gateway`` lazily imports the wrappers and those
    import ``gates.primitives``. Recorded, not done here.
    """
    artifact = Path(__file__).resolve().parents[3] / "artifacts" / "method-cards.json"
    cards = json.loads(artifact.read_bytes().decode("utf-8"))["cards"]
    return {
        int(card["id"]): tuple(str(name) for name in (card.get("precondition_gates") or ()))
        for card in cards
    }


def card_gate_names(fn: str) -> tuple[str, ...]:
    """The raw ``precondition_gates`` entries the card declares for one node."""
    from econflow_engine.loader import MANIFEST

    entry = MANIFEST.get(fn)
    if entry is None:
        raise KeyError(f"unknown method {fn!r}; it is not one of the catalogue's nodes.")
    return _gates_by_card_id()[int(entry["card_id"])]


def gates_for(fn: str) -> tuple[GatePrimitive, ...]:
    """The primitives the card declares for one node, in declaration order."""
    return resolve_gates(card_gate_names(fn))
