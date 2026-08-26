# SPDX-License-Identifier: AGPL-3.0-only
"""Published tables, written down once, so an oracle case can reach past the 103.

THE PROBLEM. An oracle case names its inputs as JSON literals, and
``oracle.literal_callable_nodes`` counts how far that reaches: 103 of 1456. The
other 1353 take a handle or a path, and a case file holds neither. Measured over
the committed contract, and the four tiers are disjoint and sum to 1456::

    103   every required argument is a literal kind                 reachable today
    894   required data handles only -- series, frame, matrix       reachable by a fixture
    440   at least one required raw_handle or raw_handle_array      part fixture, part chain
     19   at least one required `path`                              NOT reachable

The 19 stay out of reach and are named here rather than quietly rounded away: a
``path`` is the ticket of a dataset somebody uploaded through the data plane, and
this design does not invent one. The 440 split into raw handles holding plain
data, which a fixture reaches, and raw handles holding a FITTED OBJECT, which need
a producer to run first. That split is not derivable from the artifact -- the
contract records the kind, never what a caller put behind it -- so it is measured
by what actually ran and never asserted from the spec.

A FIXTURE IS A VALUE FORM INSIDE ``inputs``, NOT AN EIGHTH CASE KEY::

    "inputs": {"data": {"$fixture": "anscombe_1973_data_set_i"}, "alpha": 0.05}

``CASE_KEYS`` does not move. A case that reaches for a fixture says so where the
argument is, which is where a reader looks to find out what the call receives.

THE DATASET FILE. ``engine/tests/fixtures/<name>.json``, ONE PER PUBLISHED TABLE,
seven keys, every one required and no key beyond them::

    shape     series | irregular_series | frame | matrix | vector | object
    index     how the labels are BUILT, or null where the shape has none
    columns   the column names, or the series name as a one-element list, or null
    values    the numbers, as JSON literals
    dtype     float | int | str | bool, or null for `object`
    citation  the published locator, checked by the same rule a case's is
    notes     what was transcribed, and what the dataset does not support

THERE IS NO ``kind`` FIELD. The argument's kind is already in node-specs.json, and
a second copy here would be free to drift from the contract in silence -- the same
reason the harness reads ``pointer_handle_kinds`` from the artifact rather than
listing it.

``values`` IS JSON LITERALS AND NOTHING ELSE. No import slot, no seed, no class
name, and the closed key set above is what makes that structural rather than a
convention: there is nowhere to put one. THE REASON IS NOT TIDINESS. A fixture
that built a fitted object by calling the same library the wrapper wraps would
make a wrong fixture and a wrong body agree, and the case would go green having
compared the library with itself -- in the one harness whose whole purpose is to
refuse a silent pass. A fitted object is reached by running a real producer node
through the real gateway (``$produce``), never by importing one here.

THE CITATION IS CHECKED BY THE CASE'S OWN RULE, imported rather than reimplemented.
A transcribed table is a claim about the literature exactly as a result is, and a
dataset admitted on a weaker rule than the number computed from it is the softer
half of the same gate.

WHERE THIS DIRECTORY IS NOT. NOT under ``tests/oracle/``: ``_case_files`` globs
that tree by file name, so a dataset there would be discovered as a case and die
on the three-segment rule. NOT ``tests/payloads/``: that directory's ABSENCE is
what keeps ``engine.invocation_payloads`` in its deliberately-owed OWED branch,
which ``assert.sh`` keys on with ``[ ! -d tests/payloads ]``. Creating it here
would silently retire a debt this change has not paid.
"""

from __future__ import annotations

import json
import math
from collections.abc import Callable
from functools import cache
from pathlib import Path
from typing import Any

ENGINE_ROOT = Path(__file__).resolve().parent.parent.parent
FIXTURES = ENGINE_ROOT / "tests" / "fixtures"

#: The value form. One key, and the value is the dataset's file stem.
FIXTURE_SIGIL = "$fixture"

#: The chain form. One key, and the value is ``{"fn": ..., "inputs": {...}}``.
PRODUCE_SIGIL = "$produce"

#: CLOSED. Every key required, no key beyond these -- the same doctrine as
#: ``CASE_KEYS``: a misspelt key that is merely ignored turns a reviewed
#: declaration into no declaration at all.
FIXTURE_KEYS = frozenset(
    {"shape", "index", "columns", "values", "dtype", "citation", "notes"}
)

SHAPES = frozenset(
    {"series", "irregular_series", "frame", "matrix", "vector", "object"}
)

#: The shapes that carry an index, and the shapes whose ``columns`` names a series
#: rather than a set of columns. Declared rather than spelled out at each use, so
#: a seventh shape is admitted in one place.
INDEXED = frozenset({"series", "irregular_series", "frame"})
SERIES_SHAPES = frozenset({"series", "irregular_series"})

#: An index is a SPECIFICATION, never a transcription: the labels are produced by
#: the builder from these few fields. A dataset that listed its own labels beside
#: its own values could not tell a reader which of the two the source printed.
INDEX_KINDS = frozenset({"range", "period", "dates"})

DTYPES = frozenset({"float", "int", "str", "bool"})


class FixtureError(Exception):
    """A dataset file that must not be built: the reason is the message."""


def _read(path: Path) -> Any:
    return json.loads(path.read_bytes().decode("utf-8"))


def fixture_files() -> list[Path]:
    """Every dataset file. ``_``-prefixed names are reserved, as under oracle/."""
    if not FIXTURES.is_dir():
        return []
    return sorted(p for p in FIXTURES.glob("*.json") if not p.name.startswith("_"))


def fixture_names() -> list[str]:
    return [p.stem for p in fixture_files()]


# --------------------------------------------------------------------------- #
# validation
# --------------------------------------------------------------------------- #


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise FixtureError(message)


def _check_leaves(values: Any, dtype: str, depth: int) -> int:
    """Assert every leaf matches ``dtype`` and every nesting level is rectangular.

    Returns the number of leaves. ``bool`` is checked before ``int`` throughout,
    because ``isinstance(True, int)`` is true in Python and a boolean silently
    admitted as an integer is a value the source never printed.
    """
    if isinstance(values, list):
        _require(bool(values), "`values` holds an empty list; a fixture with no data "
                               "compares nothing")
        _require(depth > 0, "`values` nests deeper than this shape allows")
        widths = {len(v) if isinstance(v, list) else -1 for v in values}
        _require(len(widths) == 1, f"`values` is ragged: row lengths {sorted(widths)}")
        return sum(_check_leaves(v, dtype, depth - 1) for v in values)
    if dtype == "bool":
        _require(isinstance(values, bool), f"`values` holds {values!r}, and dtype is bool")
    elif dtype == "int":
        _require(isinstance(values, int) and not isinstance(values, bool),
                 f"`values` holds {values!r}, and dtype is int")
    elif dtype == "float":
        _require(isinstance(values, int | float) and not isinstance(values, bool),
                 f"`values` holds {values!r}, and dtype is float")
    else:
        _require(isinstance(values, str), f"`values` holds {values!r}, and dtype is str")
    return 1


def _check_no_sigil(value: Any) -> None:
    """No mapping key inside a dataset may open with ``$``.

    The two sigils are read out of a case's ``inputs``, and data that could carry
    one would be data the harness might interpret. Refusing the character
    outright is cheaper to reason about than deciding where interpretation stops.
    """
    if isinstance(value, dict):
        for key, item in value.items():
            _require(not str(key).startswith("$"),
                     f"the key {key!r} opens with '$', which is reserved for the "
                     f"{FIXTURE_SIGIL} and {PRODUCE_SIGIL} forms")
            _check_no_sigil(item)
    elif isinstance(value, list):
        for item in value:
            _check_no_sigil(item)


def _check_index(record: dict[str, Any], n_rows: int) -> None:
    shape, index = record["shape"], record["index"]
    if shape not in INDEXED:
        _require(index is None,
                 f"shape '{shape}' carries no index, and `index` is not null")
        return
    _require(isinstance(index, dict), f"shape '{shape}' needs an `index` object")
    kind = index.get("kind")
    _require(kind in INDEX_KINDS, f"index kind {kind!r} is not one of {sorted(INDEX_KINDS)}")
    if shape == "irregular_series":
        _require(kind == "dates",
                 "an irregular series is irregular BECAUSE its labels are listed; "
                 "index kind 'dates' is the only admissible one")
    else:
        _require(kind != "dates",
                 f"index kind 'dates' names an irregular series; shape is '{shape}'")
    if kind == "range":
        _require(set(index) == {"kind", "start"}, f"a range index takes `start`: {sorted(index)}")
        _require(isinstance(index["start"], int) and not isinstance(index["start"], bool),
                 "a range index `start` is an integer")
    elif kind == "period":
        _require(set(index) == {"kind", "start", "freq"},
                 f"a period index takes `start` and `freq`: {sorted(index)}")
        _require(isinstance(index["start"], str) and isinstance(index["freq"], str),
                 "a period index `start` and `freq` are strings")
    else:
        _require(set(index) == {"kind", "values"}, f"a dates index takes `values`: {sorted(index)}")
        labels = index["values"]
        _require(isinstance(labels, list) and all(isinstance(x, str) for x in labels),
                 "a dates index `values` is a list of date strings")
        _require(len(labels) == n_rows,
                 f"the index lists {len(labels)} label(s) and `values` has {n_rows} row(s)")


def _check_columns(record: dict[str, Any]) -> None:
    shape, columns, values = record["shape"], record["columns"], record["values"]
    if shape in SERIES_SHAPES:
        _require(isinstance(columns, list) and len(columns) == 1
                 and isinstance(columns[0], str),
                 f"shape '{shape}' names ONE series; `columns` is a one-element list")
        return
    if shape == "frame":
        _require(isinstance(columns, list) and bool(columns)
                 and all(isinstance(c, str) for c in columns),
                 "shape 'frame' needs `columns` as a non-empty list of names")
        _require(len(set(columns)) == len(columns), f"`columns` names one twice: {columns}")
        widths = {len(row) for row in values}
        _require(widths == {len(columns)},
                 f"`columns` names {len(columns)} and the rows are {sorted(widths)} wide")
        return
    _require(columns is None, f"shape '{shape}' carries no column names")


def validate(raw: Any) -> dict[str, Any]:
    """Every rule a dataset must satisfy BEFORE anything is built from it."""
    _require(isinstance(raw, dict),
             f"the dataset file holds a {type(raw).__name__}, not an object")
    record: dict[str, Any] = raw
    unknown = sorted(set(record) - FIXTURE_KEYS)
    missing = sorted(FIXTURE_KEYS - set(record))
    _require(not unknown, f"unknown key(s) {unknown}. The key set is CLOSED.")
    _require(not missing, f"missing key(s) {missing}. Every key is REQUIRED and none "
                          f"of them has a default.")

    shape = record["shape"]
    _require(shape in SHAPES, f"shape {shape!r} is not one of {sorted(SHAPES)}")

    dtype, values = record["dtype"], record["values"]
    _check_no_sigil(values)
    if shape == "object":
        _require(dtype is None, "shape 'object' carries no single dtype; `dtype` is null")
        _require(isinstance(values, dict) and bool(values),
                 "shape 'object' holds a non-empty mapping in `values`")
        _require(record["columns"] is None and record["index"] is None,
                 "shape 'object' carries neither columns nor an index")
    else:
        _require(dtype in DTYPES, f"dtype {dtype!r} is not one of {sorted(DTYPES)}")
        _require(isinstance(values, list), f"shape '{shape}' holds a list in `values`")
        depth = 2 if shape in {"frame", "matrix"} else 1
        _check_leaves(values, str(dtype), depth)
        _check_columns(record)
        _check_index(record, len(values))

    from tests.conformance.test_conformance import Inadmissible, _require_a_published_locator

    try:
        _require_a_published_locator(str(record["citation"]))
    except Inadmissible as refusal:
        raise FixtureError(str(refusal)) from refusal
    _require(bool(str(record["notes"]).strip()),
             "`notes` is empty. A dataset states what was transcribed and what it "
             "does not support; a blank one leaves the next reader to guess.")
    return record


@cache
def fixture(name: str) -> dict[str, Any]:
    """The validated record for one dataset. Cached: the file does not move."""
    path = FIXTURES / f"{name}.json"
    if not path.is_file():
        known = fixture_names()
        raise FixtureError(
            f"no dataset '{name}' under tests/fixtures/ (known: {known})."
        )
    return validate(_read(path))


# --------------------------------------------------------------------------- #
# building
# --------------------------------------------------------------------------- #


def _index_of(record: dict[str, Any], n_rows: int) -> Any:
    import pandas as pd

    index = record["index"]
    if index is None:
        return None
    if index["kind"] == "range":
        start = int(index["start"])
        return pd.RangeIndex(start, start + n_rows)
    if index["kind"] == "period":
        return pd.period_range(start=index["start"], periods=n_rows, freq=index["freq"])
    return pd.DatetimeIndex(index["values"])


def build(record: dict[str, Any]) -> Any:
    """A validated record -> the object a wrapper argument expects.

    EVERY CONSTRUCTOR HERE IS pandas OR numpy. Nothing in this function imports a
    statistical library, and nothing fits, estimates or draws: the whole point of
    a fixture is that the numbers came from a page and not from the code under
    test.
    """
    import numpy as np
    import pandas as pd

    shape, values = record["shape"], record["values"]
    if shape == "object":
        return dict(values)

    dtype = {"float": float, "int": int, "str": str, "bool": bool}[record["dtype"]]
    if shape == "vector":
        return np.array(values, dtype=dtype)
    if shape == "matrix":
        return np.array(values, dtype=dtype)

    index = _index_of(record, len(values))
    if shape == "frame":
        return pd.DataFrame(values, index=index, columns=list(record["columns"]))
    return pd.Series(values, index=index, name=record["columns"][0], dtype=dtype)


def build_fixture(name: str) -> Any:
    """The dataset named by a ``$fixture`` value form, as an object."""
    return build(fixture(name))


# --------------------------------------------------------------------------- #
# moving a dataset, which is how anything proves the data reached the body
# --------------------------------------------------------------------------- #


def move_leaf(value: Any, rtol: float, atol: float) -> Any:
    """Move one leaf far enough that a comparison at this tolerance must refuse it.

    DTYPE-AWARE, AND THE INTEGER BRANCH IS THE ONE THAT MATTERS. The tolerance
    answer is ten times ``rtol``, or ten times ``atol`` where ``rtol`` is zero, or
    one representable step where both are -- and a representable step below an
    integer is a float that :func:`build` coerces straight back to the integer it
    started from. The move would vanish inside ``np.array(..., dtype=int)``, and a
    control watching for a payload that did not move would report a body ignoring
    its input when in truth the input never changed. Booleans are negated and
    strings are extended, so every dtype this module admits can actually be moved.
    """
    if isinstance(value, bool):
        return not value
    if isinstance(value, int):
        return value + 1
    if isinstance(value, float):
        if rtol > 0.0:
            moved = value * (1.0 + 10.0 * rtol)
        elif atol > 0.0:
            moved = value + 10.0 * atol
        else:
            moved = math.nextafter(value, math.inf)
        return moved if moved != value else value + 1.0
    if isinstance(value, str):
        return value + "~"
    return value


def move_values(record: dict[str, Any], rtol: float, atol: float) -> dict[str, Any]:
    """A copy of ``record`` with every leaf of ``values`` moved. Shapes untouched."""

    def walk(value: Any) -> Any:
        if isinstance(value, list):
            return [walk(item) for item in value]
        if isinstance(value, dict):
            return {k: walk(v) for k, v in value.items()}
        return move_leaf(value, rtol, atol)

    moved = dict(record)
    moved["values"] = walk(record["values"])
    return moved


def moved_builder(rtol: float, atol: float) -> Callable[[str], Any]:
    """A drop-in for :func:`build_fixture` that returns each dataset MOVED.

    Handed to the same code path the real builder goes through, never to a copy of
    it: a control that re-implemented delivery in order to perturb it would be
    proving something about the copy.
    """

    def builder(name: str) -> Any:
        return build(move_values(fixture(name), rtol, atol))

    return builder
