# SPDX-License-Identifier: AGPL-3.0-only
"""Box 2.1.1.2: `chronology` is OPTIONAL at the adapter, refused in the body.

WHY THIS SUITE EXISTS AT ALL. ``nber_recessions`` and ``nber_recession_flag``
compute over a chronology the CALLER supplies -- this engine ships no table and
reaches no network. The obvious way to express "you must supply one" is a
required argument, and it is the wrong one. This file pins the choice so that a
later reader who thinks `required: true` was an oversight finds the measurement
instead of re-making the mistake.

WHAT REQUIRED WOULD HAVE COST, measured on 2026-08-26 rather than argued.
``nber_recessions`` carries no required argument today. Making ``chronology``
required moves it into the population that
``TestCorpusHygiene.test_family_sizes_are_the_expected_ones`` counts, taking the
live ``with_required`` from 900 to 901 against a FROZEN ``missing-required``
family of exactly 900 cases. That assertion is corpus hygiene, not P3, so no
entry in ``artifacts/intentional-divergences.json`` can absorb it: P3 covers
``{python.reject AND frozen.accept}`` and this is neither. Four fixtures would
additionally have flipped accept -> reject
(``spec/nber_recessions/{accept,optional-omitted}`` and the same pair on
``nber_recession_flag``), each a new declared divergence. Optional costs none of
it: the two ``contract_hash`` values move because ``arguments`` is inside the
hash's canonical form, and nothing else does.

THE BOUNDARY THIS SUITE DOES NOT CROSS, STATED RATHER THAN PAPERED OVER. The
adapter accepting a call with no chronology is HALF the design. The other half
-- a ``GateError`` naming the missing chronology -- belongs to the body, and
every body in this tree is a stub while ``engine.n_implemented`` is 0. So
:func:`test_the_body_still_refuses_every_call_because_it_is_a_stub` asserts
today's ``NotImplementedError``, and it is written to FAIL the moment a body
lands. That failure is the signal to replace it with the gate assertion, not a
regression: a suite that quietly tolerated either outcome would be proving
nothing about the half of the design that does the actual refusing.
"""

from __future__ import annotations

from typing import Any

import pytest

from econflow_engine.kinds import validate_wire
from econflow_engine.loader import wire_model
from econflow_engine.wrappers.c00_data_utilities.nber_recession_chronology import (
    nber_recession_flag,
    nber_recessions,
)

#: The two nodes the box changed, with a body that omits ``chronology`` entirely
#: and one that supplies it. Both must be ACCEPTED by the adapter.
WITHOUT: dict[str, dict[str, Any]] = {
    "nber_recessions": {"as_date": False},
    "nber_recession_flag": {"dates": ["2008-01-01"], "as_date": False},
}
WITH: dict[str, dict[str, Any]] = {
    "nber_recessions": {
        "chronology": [{"peak": "2007-12-01", "trough": "2009-06-01"}],
        "as_date": False,
    },
    "nber_recession_flag": {
        "dates": ["2008-01-01"],
        "chronology": [{"peak": "2007-12-01", "trough": "2009-06-01"}],
        "as_date": False,
    },
}
FNS = tuple(WITHOUT)


def _kinds(fn: str) -> dict[str, str]:
    from tests.parity.replay import _read

    node = next(n for n in _read("node-specs.json")["nodes"] if n["fn"] == fn)
    return {a["name"]: a["kind"] for a in node["arguments"]}


def _validate(fn: str, body: dict[str, Any]) -> tuple[bool, str | None]:
    ok, reason = validate_wire(wire_model(fn), body, _kinds(fn))
    return ok, reason


@pytest.mark.parametrize("fn", FNS)
def test_the_adapter_accepts_a_call_that_omits_the_chronology(fn: str) -> None:
    """THE POINT OF THE BOX. Omitting it is an adapter ACCEPT, so the refusal can
    be a ``GateError`` naming the argument rather than a 422 from the schema."""
    ok, reason = _validate(fn, WITHOUT[fn])
    assert ok, f"{fn}: the adapter refused a call omitting chronology ({reason})"


@pytest.mark.parametrize("fn", FNS)
def test_the_adapter_accepts_a_call_that_supplies_one(fn: str) -> None:
    ok, reason = _validate(fn, WITH[fn])
    assert ok, f"{fn}: the adapter refused a well-formed chronology ({reason})"


@pytest.mark.parametrize("fn", FNS)
def test_chronology_is_declared_optional_and_raw(fn: str) -> None:
    """The two properties every other assertion here depends on, read from the
    sealed artifact rather than from the corpus that produced it."""
    from tests.parity.replay import _read

    node = next(n for n in _read("node-specs.json")["nodes"] if n["fn"] == fn)
    arg = next(a for a in node["arguments"] if a["name"] == "chronology")
    assert arg["required"] is False
    assert arg["kind"] == "raw"


@pytest.mark.parametrize(
    "nonsense",
    [42, "1857-06-01", {"peak": "2007-12-01"}, [], [{"peak": 1, "trough": None}], True],
    ids=["int", "bare-string", "unpaired-mapping", "empty", "null-trough", "bool"],
)
@pytest.mark.parametrize("fn", FNS)
def test_the_wire_layer_validates_nothing_about_a_raw_chronology(
    fn: str, nonsense: Any
) -> None:
    """NEGATIVE CONTROL, and the reason the body gate is not optional.

    ``raw`` is documented as "passed to the engine UNTOUCHED (no coercion
    whatsoever)", so every one of these malformed chronologies is ACCEPTED here.
    If any were refused, the wire layer would be doing shape validation that
    ``raw`` promises it does not do, and the body's gate would have been written
    against a guarantee it does not have.
    """
    ok, reason = _validate(fn, {**WITHOUT[fn], "chronology": nonsense})
    assert ok, f"{fn}: raw refused {nonsense!r} ({reason}) -- raw coerces nothing"


@pytest.mark.parametrize("fn", FNS)
def test_an_unknown_key_is_still_refused(fn: str) -> None:
    """The adapter got LOOSER by exactly one argument, and no looser than that."""
    ok, reason = _validate(fn, {**WITHOUT[fn], "chronologyy": []})
    assert not ok and reason == "unknown-args", f"{fn}: {reason}"


@pytest.mark.parametrize("fn", FNS)
def test_the_body_still_refuses_every_call_because_it_is_a_stub(fn: str) -> None:
    """THE 2.2 BOUNDARY, ASSERTED RATHER THAN ASSUMED -- see this module's
    docstring. Replace this with the ``GateError`` assertion when the body lands;
    it is written to fail then, and that failure is the reminder."""
    body = {nber_recessions: WITH["nber_recessions"],
            nber_recession_flag: WITH["nber_recession_flag"]}
    fnobj = nber_recessions if fn == "nber_recessions" else nber_recession_flag
    with pytest.raises(NotImplementedError, match=fn):
        fnobj(**body[fnobj])
