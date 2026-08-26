# SPDX-License-Identifier: AGPL-3.0-only
"""Box 2.1.16 -- property tests, and the proof that the properties can fail.

THREE GROUPS, AND ALL THREE ARE LOAD-BEARING.

1. REACHABILITY. Each named edge shape is proved reachable from the strategy
   that claims to emit it, with :func:`hypothesis.find` inside a pinned budget.
   Without this group the rest is decorative: a strategy that only ever produced
   comfortable mid-range series would satisfy every property below and prove
   nothing, and nothing else here would notice.

2. THE REAL PROPERTIES, stated against code that exists in this tree TODAY --
   ``serialize.py``, ``chart_spec.py`` and ``kinds.py``. There are no implemented
   method families yet (``engine.n_implemented`` is 0), so a property written
   against a wrapper body would be a property with no subject.

3. THE PLANTED CONTROLS. Every property is applied to a method built to break it
   and to one built to satisfy it. The property FUNCTIONS are shared with group
   2 -- the same code, a different subject -- so a property that could not fail
   would be caught here rather than being mistaken for a passing suite.

TWO DOMAINS, AND THE DIFFERENCE IS A CLAIM RATHER THAN AN ACCIDENT OF SEEDING.

    series()            every finite float, subnormals and 1e308 included
    estimable_series()  zero, or magnitudes in [1e-100, 1e6]

Group 2 uses the WIDE one, because ``serialize.py`` and ``chart_spec.py`` claim
to be total and a subnormal is an ordinary finite float. Verified over ten
hypothesis seeds (1, 2, 3, 7, 11, 42, 99, 1234, 31337, 2026): they are.

The three ESTIMATOR properties use the narrow one, because an estimator squares
and divides, and ``tests/conftest.py`` sets ``np.seterr(all="raise")`` so an
underflow raises instead of flushing to zero. Below sqrt(tiny) --
1.4916681462400413e-154 -- the square of a perfectly normal float is subnormal,
so ``variance`` has no value there and the property has no subject. That is a
restriction on the DOMAIN OF THE PROPERTY, stated here and at ``estimable_floats``
so a reader sees the boundary; it is NOT a restriction on the code under test,
which is still exercised over everything. Each such test says so on its own line.
"""

from __future__ import annotations

import json
from collections.abc import Callable
from typing import Any

import numpy as np
import pandas as pd
import pytest
from hypothesis import assume, find, given
from hypothesis import strategies as st

from econflow_engine.chart_spec import assert_pure, chart_spec
from econflow_engine.kinds import ENGINE_REASON_CODES, NODE_ARG_KINDS, reason_from_kind
from econflow_engine.serialize import to_json, to_mcp
from tests.controls.property_controls import (
    adds_a_constant,
    assert_nan_preserving,
    assert_scale_equivariant,
    drops_nan,
    needs_two,
    observed,
    scaled_mean,
)
from tests.controls.strategies import (
    CONTROL_SETTINGS,
    FIND_BUDGET,
    PROPERTY_SETTINGS,
    estimable_series,
    frames,
    matrices,
    payloads,
    series,
)

# A scale factor away from 1.0. At exactly 1.0 the shift control satisfies
# equivariance by accident -- f(1 * x) really is 1 * f(x) for any f -- and the
# positive control would fail to fire for a reason that has nothing to do with
# the method.
_FACTORS = st.floats(min_value=1.5, max_value=8.0)


def _reject_non_json(token: str) -> object:
    """``json`` accepts ``NaN`` and ``Infinity`` by DEFAULT; this refuses them.

    The wire contract says a non-finite value is written as ``null``, because
    those two tokens are not JSON and every strict parser downstream rejects
    them. ``json.loads`` is not a strict parser unless it is told to be, so a
    round-trip test without this hook would pass on exactly the output the
    contract forbids.
    """
    raise AssertionError(f"the payload carries the non-JSON token {token!r}")


def _strict_loads(text: str) -> Any:
    return json.loads(text, parse_constant=_reject_non_json)


def _has_a_value(values: pd.Series) -> bool:
    return bool(np.isfinite(values.to_numpy()).any())


def _is_constant(values: pd.Series) -> bool:
    """Every observation the same. Compared elementwise, not via ``nunique``.

    ``nunique`` builds a hash set of the whole column to answer a question that
    one comparison against the first element answers -- which is what ruff's
    PD101 objects to, and it is right.
    """
    array = values.to_numpy()
    return bool(len(array) > 0 and (array == array[0]).all())


# ---------------------------------------------------------------------------
# 1. REACHABILITY -- the strategies really do emit the shapes they claim to
# ---------------------------------------------------------------------------


def test_strategy_reaches_a_constant_series() -> None:
    """Zero variance: every scale and correlation denominator is zero."""
    found = find(
        series(),
        lambda s: len(s) > 1 and bool(s.notna().all()) and _is_constant(s),
        settings=FIND_BUDGET,
    )
    assert len(found) > 1
    assert _is_constant(found)


def test_strategy_reaches_an_all_nan_series() -> None:
    """Every observation missing: the empty-reduction shape."""
    found = find(
        series(),
        lambda s: len(s) > 0 and bool(s.isna().all()),
        settings=FIND_BUDGET,
    )
    assert len(found) > 0
    assert found.isna().all()


def test_strategy_reaches_a_single_observation() -> None:
    """n = 1: every (n - 1) denominator divides by zero here."""
    found = find(series(), lambda s: len(s) == 1, settings=FIND_BUDGET)
    assert len(found) == 1


def test_strategy_reaches_every_index_kind() -> None:
    """``to_mcp`` branches three ways on the index; all three must be reachable."""
    kinds: tuple[tuple[Callable[[pd.Series], bool], str], ...] = (
        (lambda s: isinstance(s.index, pd.DatetimeIndex), "DatetimeIndex"),
        (lambda s: isinstance(s.index, pd.PeriodIndex), "PeriodIndex"),
        (lambda s: isinstance(s.index, pd.RangeIndex), "RangeIndex"),
    )
    for predicate, label in kinds:
        found = find(series(), predicate, settings=FIND_BUDGET)
        assert predicate(found), label


# ---------------------------------------------------------------------------
# 2. THE REAL PROPERTIES -- serialize.py, chart_spec.py, kinds.py
# ---------------------------------------------------------------------------


@PROPERTY_SETTINGS
@given(payloads)
def test_to_json_is_total_and_emits_strict_json(payload: object) -> None:
    """``to_json`` NEVER blows up, and never writes a token JSON does not have.

    Totality is the module's stated contract: an unknown or dangerous object
    becomes an explicit stub rather than raising. The strict-parser hook is the
    other half -- a non-finite float must arrive as ``null``.
    """
    _strict_loads(to_json(payload))


@PROPERTY_SETTINGS
@given(payloads)
def test_to_mcp_does_not_mutate_its_input(payload: object) -> None:
    """Purity, as the module docstring claims: the input is not touched."""
    before = to_json(payload)
    to_mcp(payload)
    assert to_json(payload) == before


@PROPERTY_SETTINGS
@given(payloads)
def test_to_mcp_is_idempotent(payload: object) -> None:
    """Converting an already-converted payload changes nothing.

    The output of ``to_mcp`` is by definition JSON-safe, so feeding it back in
    must be the identity. A branch that re-wrapped or re-stubbed its own output
    would break this and would silently double-encode any nested result.
    """
    once = to_mcp(payload)
    assert to_mcp(once) == once


@PROPERTY_SETTINGS
@given(series())
def test_chart_spec_of_a_series_keeps_every_point_and_stays_data(values: pd.Series) -> None:
    """The purity gate holds, and no observation is dropped on the way to the axis."""
    option = chart_spec(values, title="control")
    assert option is not None
    assert_pure(option)
    assert len(option["series"][0]["data"]) == len(values)
    assert len(option["xAxis"][0]["data"]) == len(values)
    _strict_loads(to_json(option))


@PROPERTY_SETTINGS
@given(frames())
def test_chart_spec_of_a_frame_stays_data(frame: pd.DataFrame) -> None:
    """Every numeric column becomes exactly one series, and nothing executable."""
    option = chart_spec(frame, title="control")
    assert option is not None
    assert_pure(option)
    numeric = [c for c in frame.columns if pd.api.types.is_numeric_dtype(frame[c])]
    assert len(option["series"]) == len(numeric)
    _strict_loads(to_json(option))


@PROPERTY_SETTINGS
@given(matrices())
def test_chart_spec_of_a_matrix_covers_every_cell(matrix: np.ndarray) -> None:
    """A heatmap carries one datum per cell, and the datum carries its coordinates."""
    option = chart_spec(matrix, title="control")
    assert option is not None
    assert_pure(option)
    rows, cols = matrix.shape
    assert len(option["series"][0]["data"]) == rows * cols
    _strict_loads(to_json(option))


@PROPERTY_SETTINGS
@given(st.sampled_from(sorted(NODE_ARG_KINDS)))
def test_reason_from_kind_is_total_over_the_contract(kind: str) -> None:
    """Every kind in the contract maps to a reason code the wire layer knows.

    ``kinds.py`` is where the contract says to validate, and a kind with no
    reason code would surface as an unmappable rejection at the wire boundary
    rather than as a 422 the caller can act on.
    """
    assert reason_from_kind(kind) in ENGINE_REASON_CODES


def test_a_subnormal_serialises_but_will_not_survive_scaling() -> None:
    """The boundary between the two domains, pinned by hand instead of implied.

    ``estimable_series`` excludes magnitudes below 1e-100 while ``series`` does
    not, and a difference between two strategies that exists only in a comment is
    a difference nothing checks. This asserts it directly.

    BOTH HALVES ARE THE POINT, and they point opposite ways:

      * SERIALISATION IS TOTAL over a subnormal, so ``series`` is right to keep
        generating them and group 2 is right to run over the full domain;
      * THE ARITHMETIC HAS NO ANSWER there, one frame below any method under
        test, because ``tests/conftest.py`` makes an underflow raise instead of
        flushing silently to zero -- so the estimator properties are right to
        exclude it.
    """
    subnormal = 2.225074e-313
    assert 0.0 < abs(subnormal) < np.finfo(float).tiny

    values = pd.Series([0.0, subnormal], dtype=float)
    assert _strict_loads(to_json(values)) == {"values": [0.0, subnormal]}
    assert np.isfinite(np.nanmean(values.to_numpy()))

    with pytest.raises(FloatingPointError, match="underflow"):
        np.nanmean((values * 1.5).to_numpy())


# ---------------------------------------------------------------------------
# 3. THE PLANTED CONTROLS -- the properties above are proved able to fail
# ---------------------------------------------------------------------------


def test_positive_control_a_shift_falsifies_scale_equivariance() -> None:
    """POSITIVE. A method that adds a constant MUST break scale equivariance.

    DOMAIN: ``estimable_series`` -- scale equivariance is a claim about a MEAN,
    and a mean divides. Below sqrt(tiny) that division underflows inside numpy
    before this method can be right or wrong. See the module docstring.
    """

    @CONTROL_SETTINGS
    @given(estimable_series(), _FACTORS)
    def check(values: pd.Series, factor: float) -> None:
        assume(_has_a_value(values))
        assert_scale_equivariant(adds_a_constant, values, factor)

    with pytest.raises(AssertionError, match="scale equivariance violated"):
        check()


def test_positive_control_dropna_falsifies_nan_preservation() -> None:
    """POSITIVE. A method that discards missing observations MUST be caught."""

    @CONTROL_SETTINGS
    @given(series())
    def check(values: pd.Series) -> None:
        assume(bool(values.isna().any()))
        assert_nan_preserving(drops_nan, values)

    with pytest.raises(AssertionError, match="a missing observation was dropped"):
        check()


@PROPERTY_SETTINGS
@given(estimable_series(), _FACTORS)
def test_negative_control_a_scaled_mean_satisfies_scale_equivariance(
    values: pd.Series, factor: float
) -> None:
    """NEGATIVE. A genuinely scale-free statistic MUST NOT be flagged.

    DOMAIN: ``estimable_series``, for the same reason as the positive control
    above -- the mean's division underflows below sqrt(tiny). See the module
    docstring.
    """
    assume(_has_a_value(values))
    assert_scale_equivariant(scaled_mean, values, factor)


@PROPERTY_SETTINGS
@given(estimable_series())
def test_negative_control_refusing_a_single_observation_is_not_a_violation(
    values: pd.Series,
) -> None:
    """NEGATIVE. Raising on n = 1 is an ANSWER; a property must not call it a bug.

    A property written as "returns a finite number for every input" would fail
    here and would push whoever wrote the method toward returning nan instead --
    the silent failure this repository refuses. The property is "answers or
    refuses, never fabricates".

    THE CONDITION IS THE OBSERVATION COUNT, NOT THE LENGTH. A series of length 2
    carrying one NaN is a one-observation sample and must be refused exactly like
    a series of length 1.

    DOMAIN: ``estimable_series`` -- a sample variance SQUARES its deviations, and
    the square of a normal float below sqrt(tiny) is subnormal, so numpy raises
    an underflow before the refusal logic is reached. This is the counterexample
    a mutmut run found at a different seed. See the module docstring.
    """
    if observed(values) < 2:
        with pytest.raises(ValueError, match="at least 2 observations"):
            needs_two(values)
        return
    result = needs_two(values)
    assert np.isfinite(result)
    assert result >= 0.0


@PROPERTY_SETTINGS
@given(series())
def test_a_missing_observation_never_counts_toward_the_sample(values: pd.Series) -> None:
    """The sample size is the observed count, and it never exceeds the length.

    Stated separately from the control above because it is the invariant the
    control got WRONG on its first version -- guarding on ``len`` let a
    one-observation sample through as if it were two.
    """
    n = observed(values)
    assert 0 <= n <= len(values)
    assert n == len(values) - int(values.isna().sum())
