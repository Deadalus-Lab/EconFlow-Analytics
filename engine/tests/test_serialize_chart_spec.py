# SPDX-License-Identifier: AGPL-3.0-only
"""The two wire-facing conversions, against the inputs that break them. Box 2.1.11.

WHAT WAS UNTESTED. ``serialize.py`` and ``chart_spec.py`` are the only two modules
every wrapper result passes through, and until now the suite touched two private
label predicates and nothing else: ``to_mcp``, ``to_json``, ``stub``,
``McpDistance``, ``flatten_htest``, ``chart_spec`` and ``assert_pure`` had no test
of any kind. Both modules were nevertheless rewritten in places to satisfy a type
checker, which is a behaviour change wearing the clothes of a lint fix.

EVERY CASE HERE ASSERTS A VALUE, never merely that nothing was raised. A test that
only says "does not raise" passes just as happily over a function that returns
garbage, and garbage is exactly what a total conversion produces when it goes
wrong -- it is total by design, so it cannot signal failure by raising. The
serialized bytes, or the exact ``detail_code`` of the refusal, is therefore the
assertion in every case below. The values were MEASURED against this tree, not
predicted.

THE FIXTURES ARE LITERAL CONSTRUCTORS IN THIS MODULE. The 18 hostile fixtures this
box was written around lived under ``engine/fixtures/`` and went with that
directory on 2026-08-22. They do not come back as files: a fixture directory is a
second sealed artifact with a sidecar, a schema and an inventory constant, and
none of that buys anything for inputs that fit on one line each. Reading the
constructor beside the assertion is also the only way to see WHAT is hostile about
a case.

THE PURITY GATE IS PROVED LIVE, not by inspection. The ``"=>"`` label case exists
so that one assertion in this file fails if ``_FORBIDDEN_PATTERNS`` is ever
narrowed or ``assert_pure`` stops being called on the finished specification.
Proving the round trip works would not have noticed either.
"""

from __future__ import annotations

import datetime as dt
import decimal
import json
from typing import Any

import numpy as np
import pandas as pd
import pytest

from econflow_engine.chart_spec import (
    _FORBIDDEN_PATTERNS,
    CHART_MAX_CELLS,
    CHART_MAX_POINTS,
    _table_spec,
    assert_pure,
    chart_spec,
)
from econflow_engine.errors import GateError
from econflow_engine.serialize import (
    McpDistance,
    flatten_htest,
    stub,
    to_json,
    to_mcp,
)

# ---------------------------------------------------------------------------
# The hostile inputs, one constructor each
# ---------------------------------------------------------------------------


def test_non_finite_floats_become_null() -> None:
    """JSON has no NaN and no Infinity. The contract says null, so orjson's
    native non-finite handling is the behaviour and not a rounding of it."""
    assert to_json(pd.Series([np.inf, -np.inf, np.nan])) == '{"values":[null,null,null]}'
    assert to_mcp(float("inf")) is None
    assert to_mcp(float("nan")) is None
    assert to_mcp(-float("inf")) is None


def test_nat_is_not_none() -> None:
    """THE CASE THAT LOOKS LIKE A BUG AND IS NOT. ``pd.NaT`` is an instance of
    ``datetime.datetime``, so it reaches the datetime branch and serialises to the
    string 'NaT' -- distinct from ``None``, which becomes null. Inside a temporal
    index it takes the OTHER path, ``_iso_index_label``, and becomes null there.
    The two answers are deliberate and neither is a fallback."""
    assert to_json([pd.NaT, None]) == '["NaT",null]'
    assert to_mcp(pd.NaT) == "NaT"
    assert to_mcp(None) is None
    index = pd.DatetimeIndex([pd.Timestamp("2026-01-01"), pd.NaT])
    assert json.loads(to_json(pd.Series([1.0, 2.0], index=index)))["index"] == [
        "2026-01-01T00:00:00",
        None,
    ]


def test_pandas_na_is_stubbed_rather_than_nulled() -> None:
    """``pd.NA`` is NOT ``None`` and is NOT a float, so no registered branch claims
    it and the total catch-all stubs it. Recorded because the alternative -- a
    silent null -- would erase the difference between 'missing' and 'a type this
    layer does not model', and the stub is the designed answer."""
    converted = to_mcp(pd.NA)
    assert converted["@mcp_class"] == ["NAType"]
    assert converted["@mcp_serialized"] is False
    assert converted["length"] is None


def test_a_mixed_int_and_float_frame_keeps_both_types() -> None:
    """Record-oriented output, and an int stays an int: a frame is not silently
    promoted to one dtype on the way out."""
    frame = pd.DataFrame({"a": [1, 2], "b": [1.5, 2.5]})
    assert to_json(frame) == '[{"a":1,"b":1.5},{"a":2,"b":2.5}]'


def test_an_unsorted_datetime_index_is_not_reordered() -> None:
    """``to_mcp`` is pure and does not repair its input. Sorting here would make
    the values and the index disagree in every caller that already sorted."""
    index = pd.DatetimeIndex(["2026-02-01", "2026-01-01"])
    assert to_json(pd.Series([1, 2], index=index)) == (
        '{"values":[1,2],"index":["2026-02-01T00:00:00","2026-01-01T00:00:00"]}'
    )


def test_a_duplicated_index_is_carried_through_unchanged() -> None:
    """A duplicate label is data, not an error: de-duplicating would drop a row."""
    assert to_json(pd.Series([1, 2], index=["a", "a"])) == (
        '{"values":[1,2],"index":["a","a"]}'
    )


def test_a_period_index_is_labelled_at_its_start_and_declares_its_frequency() -> None:
    series = pd.Series([1.0, 2.0], index=pd.PeriodIndex(["2026-01", "2026-02"], freq="M"))
    assert to_json(series) == (
        '{"values":[1.0,2.0],"index":["2026-01-01T00:00:00","2026-02-01T00:00:00"],'
        '"frequency":"M"}'
    )


def test_a_timedelta_index_is_stubbed_element_by_element() -> None:
    """A ``TimedeltaIndex`` is neither datetime nor period, so it takes the
    generic index path and each ``Timedelta`` reaches the catch-all. The stub is
    the honest answer -- a duration has no ISO-8601 instant to become -- and it is
    asserted so that a later branch for it is a visible change."""
    converted = to_mcp(pd.Series([1.0], index=pd.TimedeltaIndex(["1 days"])))
    assert converted["values"] == [1.0]
    assert converted["index"][0]["@mcp_class"] == ["Timedelta"]
    assert converted["index"][0]["@mcp_serialized"] is False


def test_a_tz_aware_stamp_keeps_its_offset_and_a_naive_one_has_none() -> None:
    """The offset is part of the instant. Dropping it silently moves every stamp
    by the machine's zone, which is the failure the pinned TZ exists to prevent."""
    aware = pd.Series([1.0], index=pd.DatetimeIndex(["2026-01-01T00:00:00+02:00"]))
    naive = pd.Series([1.0], index=pd.DatetimeIndex(["2026-01-01T00:00:00"]))
    assert json.loads(to_json(aware))["index"] == ["2026-01-01T00:00:00+02:00"]
    assert json.loads(to_json(naive))["index"] == ["2026-01-01T00:00:00"]
    assert to_mcp(dt.datetime(2026, 1, 1, tzinfo=dt.UTC)) == "2026-01-01T00:00:00+0000"
    assert to_mcp(dt.datetime(2026, 1, 1)) == "2026-01-01T00:00:00"


@pytest.mark.parametrize(
    ("label", "expected"),
    [
        ("עברית", '{"values":[1.0],"index":["עברית"]}'),
        ("時系列", '{"values":[1.0],"index":["時系列"]}'),
        ('a"b\\c', '{"values":[1.0],"index":["a\\"b\\\\c"]}'),
    ],
    ids=["rtl", "cjk", "quote-and-backslash"],
)
def test_a_label_survives_the_round_trip_verbatim(label: str, expected: str) -> None:
    """Non-ASCII is emitted as itself rather than escaped, and the two characters
    that can end a JSON string early are escaped and only those. Asserting the
    exact bytes is the point: a quote that closed the string early would still
    parse as SOMETHING and a laxer assertion would not notice."""
    payload = to_json(pd.Series([1.0], index=[label]))
    assert payload == expected
    assert json.loads(payload)["index"] == [label]


def test_an_empty_frame_serialises_to_an_empty_array() -> None:
    """Record-oriented output of no records. Not null, not an object with empty
    columns: a consumer iterating rows gets zero rows and needs no special case."""
    assert to_json(pd.DataFrame()) == "[]"
    assert to_mcp(pd.DataFrame()) == []


def test_a_one_by_one_frame_is_still_a_list_of_records() -> None:
    """The degenerate shape stays the general shape. The contract has no
    scalar-unboxing switch, so a single cell does not collapse into a scalar."""
    assert to_json(pd.DataFrame({"a": [1]})) == '[{"a":1}]'


def test_an_object_column_of_decimals_is_stubbed_per_cell() -> None:
    """``Decimal`` carries a precision that a float cannot hold, so converting it
    would silently lose exactly what it was chosen for. The stub says so."""
    converted = to_mcp(pd.DataFrame({"d": [decimal.Decimal("1.5")]}))
    assert converted[0]["d"]["@mcp_class"] == ["Decimal"]
    assert converted[0]["d"]["@mcp_serialized"] is False
    assert to_mcp(decimal.Decimal("1.5"))["@mcp_class"] == ["Decimal"]


def test_the_round_trip_is_byte_deterministic() -> None:
    """Serialising the same payload twice must give the same bytes. A set or a
    dict iterated in hash order would not, and the wire contract's digests and the
    parity corpus both rest on this."""
    payload = {
        "frame": pd.DataFrame({"b": [2.0, np.nan], "a": [1, 2]}),
        "series": pd.Series([1.0], index=pd.DatetimeIndex(["2026-01-01"])),
        "labels": ["時系列", "עברית", 'q"\\'],
        "distance": McpDistance(condensed=[1.0, 2.0, 3.0], size=3, labels=["a", "b", "c"]),
    }
    first = to_json(payload).encode("utf-8")
    second = to_json(payload).encode("utf-8")
    assert first == second
    first_indented = to_json(payload, indent=True).encode("utf-8")
    second_indented = to_json(payload, indent=True).encode("utf-8")
    assert first_indented == second_indented


# ---------------------------------------------------------------------------
# The stub policy, the distance form and the hypothesis-test flattening
# ---------------------------------------------------------------------------


def test_a_foreign_object_is_stubbed_and_never_walked() -> None:
    """The default branch is the whole safety property: walking a fitted model
    leaks its call, its data and its environment."""
    class Fitted:
        def __init__(self) -> None:
            self.training_data = "the caller's private series"

    converted = to_mcp(Fitted())
    assert converted == {
        "@mcp_class": ["Fitted"],
        "@mcp_serialized": False,
        "length": None,
        "@mcp_note": (
            "foreign / non-serialisable object -- see the sibling fields for the "
            "extracted values."
        ),
    }
    assert "private series" not in to_json(Fitted())


def test_a_callable_is_stubbed_with_its_own_note() -> None:
    assert to_mcp(len)["@mcp_note"] == "callable -- not serialised."


def test_stub_reads_a_shape_when_there_is_one_and_a_length_otherwise() -> None:
    """``dim`` comes from ``shape`` and ``length`` from ``len``; an object with
    neither reports ``length: null`` rather than omitting the field, so a consumer
    never has to distinguish 'absent' from 'unknown'."""
    assert stub(np.zeros((2, 3)))["dim"] == [2, 3]
    assert stub([1, 2, 3])["length"] == 3
    assert stub(object())["length"] is None
    assert stub(object(), note="why", extra={"k": 1})["@mcp_note"] == "why"
    assert stub(object(), extra={"k": 1})["k"] == 1


def test_a_distance_vector_keeps_its_declared_size_and_never_infers_one() -> None:
    """THE TRAP THIS CLASS EXISTS FOR. A condensed vector of length n(n-1)/2 must
    not be reported with a square matrix's shape: the size and the labels are read
    from what was DECLARED, never inferred from the container."""
    converted = to_mcp(
        McpDistance(condensed=[1.0, 2.0, 3.0], size=3, labels=["a", "b", "c"],
                    method="euclidean")
    )
    assert converted == {
        "lower_tri": [1.0, 2.0, 3.0],
        "length": 3,
        "size": 3,
        "labels": ["a", "b", "c"],
        "method": "euclidean",
    }
    assert to_mcp(McpDistance(condensed=[1.0], size=2))["labels"] is None


def test_flatten_htest_recognises_a_shape_and_declines_everything_else() -> None:
    """A statistic AND a p-value make a test result. Anything else returns None so
    the caller falls through to the normal dispatch rather than being handed a
    half-flattened object."""
    class Result:
        statistic = 1.5
        pvalue = 0.25
        parameter = 3
        method = "probe"
        nuisance = "not a declared field"

    flattened = flatten_htest(Result())
    assert flattened == {
        "statistic": 1.5,
        "pvalue": 0.25,
        "parameter": 3,
        "method": "probe",
    }

    class OnlyStatistic:
        statistic = 1.5

    assert flatten_htest(OnlyStatistic()) is None
    assert flatten_htest(object()) is None


def test_an_integer_inside_the_64_bit_range_serialises_exactly() -> None:
    """Full precision, no float promotion. The boundary above this range is a
    separate question and is NOT settled here -- see the report for box 2.1.11:
    ``to_json`` raises on an int wider than 64 bits, which contradicts
    serialize.py's own stated invariant, and choosing what it should do instead
    is a wire-contract decision rather than a test one."""
    assert to_json({"big": 2**62}) == '{"big":4611686018427387904}'
    assert to_json({"big": -(2**62)}) == '{"big":-4611686018427387904}'


# ---------------------------------------------------------------------------
# chart_spec: the purity gate, the limits, and the table fallback
# ---------------------------------------------------------------------------


def test_a_forbidden_pattern_in_a_label_is_refused_by_the_purity_gate() -> None:
    """THE GATE, PROVED LIVE. ``=>`` is an arrow function: a specification
    carrying it is EXECUTABLE CODE travelling from the engine to the browser. It
    is refused, never cleaned. This assertion fails if the pattern list is
    narrowed or if assert_pure stops running over the finished specification."""
    assert "=>" in _FORBIDDEN_PATTERNS
    with pytest.raises(GateError) as raised:
        chart_spec(pd.Series([1.0], index=["a=>b"]))
    assert raised.value.reason_code == "other"
    assert raised.value.detail_code == "chart-spec"
    assert "executable code" in str(raised.value)


@pytest.mark.parametrize("pattern", _FORBIDDEN_PATTERNS)
def test_every_forbidden_pattern_is_refused_in_a_value_and_in_a_key(pattern: str) -> None:
    """Both halves, because a key is as much a channel as a value."""
    for spec in ({"title": f"x{pattern}y"}, {f"x{pattern}y": "title"}):
        with pytest.raises(GateError) as raised:
            assert_pure(spec)
        assert raised.value.detail_code == "chart-spec"


def test_assert_pure_refuses_a_callable_a_non_string_key_and_a_foreign_object() -> None:
    for spec in ({"formatter": len}, {1: "one"}, {"when": dt.date(2026, 1, 1)}):
        with pytest.raises(GateError) as raised:
            assert_pure(spec)
        assert raised.value.detail_code == "chart-spec"


def test_assert_pure_returns_a_clean_specification_unchanged() -> None:
    """The negative control of the gate: pure data must NOT be flagged, or the
    exemption has widened into 'match nothing'."""
    spec: dict[str, Any] = {
        "title": [{"text": "時系列"}],
        "series": [{"type": "line", "data": [1.0, None, 2]}],
        "flag": True,
        "nothing": None,
    }
    assert assert_pure(spec) is spec


def test_a_series_above_the_point_limit_is_refused() -> None:
    with pytest.raises(GateError) as raised:
        chart_spec(pd.Series(np.zeros(CHART_MAX_POINTS + 1)))
    assert raised.value.detail_code == "chart-spec"
    assert str(CHART_MAX_POINTS) in str(raised.value)


def test_a_table_above_the_cell_limit_is_refused() -> None:
    """The same ceiling the heatmap enforces, for the same reason: a table with
    more cells than the screen has pixels is not a table."""
    frame = pd.DataFrame({"t": ["x"] * (CHART_MAX_CELLS + 1)})
    with pytest.raises(GateError) as raised:
        chart_spec(frame)
    assert raised.value.detail_code == "chart-spec"
    assert str(CHART_MAX_CELLS) in str(raised.value)


def test_a_one_by_one_numeric_frame_is_a_line_chart() -> None:
    """The degenerate numeric shape still takes the numeric path."""
    assert chart_spec(pd.DataFrame({"a": [1.0]})) == {
        "xAxis": [{"type": "category", "data": ["0"]}],
        "yAxis": [{"type": "value"}],
        "series": [{"type": "line", "name": "a", "data": [1.0]}],
        "tooltip": {"trigger": "axis"},
    }


def test_an_empty_frame_still_draws_an_empty_chart() -> None:
    """No columns is nothing to draw, which is not the same as a shape this
    emitter cannot render -- so it keeps the empty chart rather than becoming a
    table of no rows."""
    spec = chart_spec(pd.DataFrame())
    assert spec is not None, "an empty frame is still a specification, not an absence"
    assert spec["title"] == [
        {"text": "data frame", "subtext": "no numeric column to draw"}
    ]


def test_a_frame_with_no_numeric_column_becomes_a_table() -> None:
    """WHAT THE TABLE FALLBACK REPLACED: an empty chart with a subtitle explaining
    that there was nothing to draw. The data was there the whole time; only the
    line chart was impossible."""
    spec = chart_spec(pd.DataFrame({"name": ["a", "b"], "note": ["x", "y"]}), "labels")
    assert spec == {
        "title": [{"text": "labels"}],
        "dataset": [{"source": [["", "name", "note"], ["0", "a", "x"], ["1", "b", "y"]]}],
        "series": [],
        "tooltip": {"trigger": "item"},
    }


def test_a_decimal_column_becomes_a_table_of_its_labels() -> None:
    """A ``Decimal`` column is object dtype, so it is not numeric and cannot be a
    line -- but it reads perfectly well as a table, and the cell keeps the exact
    text rather than a float that lost the precision Decimal was chosen for."""
    spec = _table_spec(pd.DataFrame({"d": [decimal.Decimal("1.5")]}), None)
    assert spec["dataset"] == [{"source": [["", "d"], ["0", "1.5"]]}]


def test_a_scalar_becomes_a_one_cell_table() -> None:
    """The type inference is unchanged; only its last branch is. A scalar used to
    produce an empty chart titled with its own type name."""
    assert chart_spec(7, "answer") == {
        "title": [{"text": "answer"}],
        "dataset": [{"source": [["value"], [7]]}],
        "series": [],
        "tooltip": {"trigger": "item"},
    }


def test_a_mapping_becomes_a_field_and_value_table() -> None:
    """A plain mapping that is NOT a caller-built option: ``chart_spec`` still
    passes a dict straight through, so this is reached through ``_table_spec``."""
    assert _table_spec({"alpha": 1, "beta": None}, None)["dataset"] == [
        {"source": [["field", "value"], ["alpha", 1], ["beta", None]]}
    ]


def test_a_sequence_becomes_a_single_column_table() -> None:
    assert _table_spec(["a", 2, None], None)["dataset"] == [
        {"source": [["value"], ["a"], [2], [None]]}
    ]


def test_a_foreign_object_becomes_a_table_naming_its_type() -> None:
    """THE REGRESSION THIS PINS, found by this test on the first run of the table
    fallback: a class that defines neither ``__str__`` nor ``__repr__`` renders
    through ``object.__repr__``, so the cell read
    ``<...Fitted object at 0x78ba845cfef0>`` -- a MEMORY ADDRESS, which differs
    between runs and travels to the browser. Two specifications for the same
    object were therefore not equal, breaking the determinism this module asserts
    elsewhere. The cell now names the type, as serialize.stub does."""
    class Fitted:
        pass

    assert _table_spec(Fitted(), None)["dataset"] == [
        {"source": [["value"], ["Fitted"]]}
    ]
    first_spec = _table_spec(Fitted(), None)
    second_spec = _table_spec(Fitted(), None)
    assert first_spec == second_spec, (
        "two specifications for the same type differ, so something run-specific "
        "reached the cell"
    )


def test_a_table_specification_passes_the_purity_gate() -> None:
    """The fallback is built inside the emitter, so it runs through the same gate
    as every other branch -- including on a hostile cell."""
    with pytest.raises(GateError) as raised:
        chart_spec(pd.DataFrame({"note": ["a=>b"]}))
    assert raised.value.detail_code == "chart-spec"


def test_a_dict_is_still_passed_through_as_a_caller_built_option() -> None:
    """A wrapper body may build part of a specification itself. That path is
    unchanged and is exactly why the purity gate has to stay."""
    assert chart_spec({"series": [{"type": "bar", "data": [1]}]}) == {
        "series": [{"type": "bar", "data": [1]}]
    }


def test_none_is_the_only_input_that_yields_no_specification() -> None:
    assert chart_spec(None) is None
