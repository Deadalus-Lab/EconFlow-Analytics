# SPDX-License-Identifier: AGPL-3.0-only
"""Box 2.1.16 -- one hypothesis strategy per input kind, and the edge shapes named.

WHAT A STRATEGY HAS TO DO HERE, AND WHAT MOST OF THEM DO NOT. A generator that
produces a hundred comfortable middle-of-the-range series satisfies every
property in the tree and proves nothing: the inputs that break numerical code are
the ones nobody types by hand. Three of them are named explicitly and are
asserted to be reachable in ``tests/test_properties.py`` with
:func:`hypothesis.find`, inside a pinned example budget:

  * the CONSTANT series      -- zero variance, so every scale, standardisation
                                and correlation denominator is zero;
  * the ALL-NaN series       -- every reduction is an empty reduction, which is
                                where numpy stops warning and starts returning
                                nan quietly;
  * n = 1                    -- one observation, so every estimator with a
                                (n - 1) denominator divides by zero and every
                                difference, lag and autocorrelation is empty.

Each strategy below therefore branches EXPLICITLY into those shapes rather than
hoping the search finds them. The reachability assertion is what keeps that
honest: delete a branch and the corresponding ``find`` fails.

THE SETTINGS ARE SHARED AND EXPLICIT, NOT A PROFILE. ``PROPERTY_SETTINGS`` is
applied per test rather than registered as a global hypothesis profile, so
importing this module changes nothing about anybody else's test session -- four
other clusters are editing this suite in parallel. Two of its values are
deliberate:

``database=None``
    Hypothesis otherwise writes replayed counterexamples into ``.hypothesis/``
    beside the suite. Nothing in this repository's ``.gitignore`` covers that
    directory (the root denies by default and re-admits ``/engine`` whole), so it
    would surface as untracked state in every ``git status``; worse, it makes a
    run's behaviour depend on an uncommitted local directory, which is precisely
    what this tree's determinism rules forbid.

``deadline=None``
    ``tests/conftest.py`` installs ``beartype_package("econflow_engine")``, an
    import hook that rewrites and type-checks every function in the package as it
    is called. Under it a single ``to_mcp`` call over a DataFrame runs well past
    hypothesis's 200 ms default deadline on a loaded machine, and a deadline
    failure would report a flaky timing artefact as a falsified property.
"""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd
from hypothesis import HealthCheck, settings
from hypothesis import strategies as st

#: Applied per test. See the module docstring for why each value is what it is.
PROPERTY_SETTINGS = settings(
    max_examples=150,
    database=None,
    deadline=None,
    # The strategies below build DataFrames and matrices, which is slow enough
    # under the beartype hook to trip the default data-generation health check
    # without anything actually being wrong.
    suppress_health_check=[HealthCheck.data_too_large, HealthCheck.too_slow],
)

#: Used ONLY where a property is expected to be falsified -- the positive
#: controls. ``report_multiple_bugs=False`` is the load-bearing difference:
#: hypothesis otherwise collects every distinct failure it finds and raises them
#: together as an ``ExceptionGroup``, which ``pytest.raises(AssertionError)``
#: does not match. The control would then look like a harness error rather than
#: the falsification it is.
CONTROL_SETTINGS = settings(
    max_examples=150,
    database=None,
    deadline=None,
    report_multiple_bugs=False,
    suppress_health_check=[HealthCheck.data_too_large, HealthCheck.too_slow],
)

#: The budget for every reachability probe in tests/test_properties.py. Pinned
#: rather than left to the default so that "the strategy can emit this" is a
#: statement about the strategy and not about how long the search was given.
FIND_BUDGET = settings(max_examples=2_000, database=None, deadline=None)

# THE UPPER BOUND OF THE ESTIMATOR DOMAIN, and it belongs to that domain alone --
# `finite_floats` below is deliberately unbounded. A scale-equivariance property
# multiplies its input by a factor of up to 8, and 1e308 * 8 is inf: the property
# would then fail on the arithmetic rather than on the method under test, which
# says nothing about either. 1e6 is far above any magnitude these controls need.
_MAGNITUDE = 1e6

# THE FULL FINITE DOMAIN, SUBNORMALS INCLUDED, AND IT STAYS THAT WAY.
#
# serialize.py and chart_spec.py claim to be TOTAL: `to_mcp` converts ANY wrapper
# output and `to_json` "NEVER blows up". A subnormal, and a value at the top of
# the float range, are both ordinary finite floats and both must survive. This
# strategy is therefore deliberately NOT bounded.
#
# An earlier version bounded it at +/-1e6 and set allow_subnormal=False, to stop
# a counterexample that had nothing to do with either module -- the underflow was
# raised inside numpy's mean, called from a planted CONTROL. Narrowing a shared
# strategy to silence a failure in one consumer is how a property suite becomes
# decorative, and it would have removed every subnormal and every large magnitude
# from the serialisation properties as a side effect. The restriction belongs to
# the consumer that needs it: see `estimable_floats` below.
finite_floats = st.floats(allow_nan=False, allow_infinity=False)

# THE DOMAIN OF AN ESTIMATOR IS NARROWER THAN THE DOMAIN OF THE SERIALISER, and
# conflating the two is what made the properties flaky under a changed seed.
#
# `finite_floats` above is right for serialize.py and chart_spec.py: those must
# be TOTAL, and a tiny value is an ordinary value to write out as JSON. But a
# variance SQUARES its deviations, and `np.seterr(all="raise")` makes an
# underflow raise. Excluding subnormals is not enough, because the square of a
# perfectly NORMAL float can be subnormal: the boundary is sqrt(tiny), measured
# as 1.4916681462400413e-154.
#
# Found by a mutmut run whose hypothesis seed differed from the suite's -- the
# falsifying series printed as three copies of 2.278379e-167, and pandas' repr
# had truncated three values that differ in their low digits, so the DEVIATIONS
# were around 1e-183 and squaring them underflowed:
#
#     FloatingPointError: underflow encountered in multiply
#         numpy/lib/_nanfunctions_impl.py -> sqr = np.multiply(arr, arr, ...)
#
# 1e-100 is the floor, with wide headroom over sqrt(tiny): floats near magnitude
# M are spaced about M * 2.2e-16 apart, so the smallest non-zero deviation at
# 1e-100 is around 1e-116 and its square around 1e-232 -- comfortably normal.
# Exact zero is admitted separately, because zero squares to zero and a
# constant-at-zero series is a shape that matters.
_ESTIMABLE_MIN = 1e-100

estimable_floats = st.one_of(
    st.just(0.0),
    st.floats(min_value=_ESTIMABLE_MIN, max_value=_MAGNITUDE, allow_subnormal=False),
    st.floats(min_value=-_MAGNITUDE, max_value=-_ESTIMABLE_MIN, allow_subnormal=False),
)

#: Values a wrapper may legitimately return inside a result mapping.
json_scalars = st.one_of(
    st.none(),
    st.booleans(),
    st.integers(min_value=-(2**53), max_value=2**53),
    finite_floats,
    st.text(max_size=32),
)

#: The float column of a series or frame: finite values AND NaN, because a
#: missing observation is an ordinary input, not an error.
_cell = st.one_of(finite_floats, st.just(float("nan")))


def _values(min_size: int = 1, max_size: int = 24) -> st.SearchStrategy[list[float]]:
    return st.lists(_cell, min_size=min_size, max_size=max_size)


@st.composite
def _constant_values(draw: st.DrawFn) -> list[float]:
    """The zero-variance shape, generated deliberately rather than hoped for."""
    value = draw(finite_floats)
    n = draw(st.integers(min_value=1, max_value=12))
    return [value] * n


@st.composite
def _all_nan_values(draw: st.DrawFn) -> list[float]:
    """Every observation missing: the empty-reduction shape."""
    n = draw(st.integers(min_value=1, max_value=12))
    return [float("nan")] * n


@st.composite
def _single_value(draw: st.DrawFn) -> list[float]:
    """n = 1: the shape every (n - 1) denominator divides by zero on."""
    return [draw(_cell)]


#: The float payload of a univariate series, across all four shapes.
series_values = st.one_of(
    _values(),
    _constant_values(),
    _all_nan_values(),
    _single_value(),
)


@st.composite
def indexes(draw: st.DrawFn, n: int) -> pd.Index:
    """One index per index kind the serialiser branches on.

    ``serialize.to_mcp`` has three distinct branches -- DatetimeIndex/PeriodIndex,
    RangeIndex, and everything else -- so a strategy that only ever produced a
    RangeIndex would leave two of them untested.
    """
    which = draw(st.sampled_from(("range", "datetime", "period", "labels")))
    if which == "range":
        return pd.RangeIndex(n)
    if which == "datetime":
        return pd.date_range("2020-01-31", periods=n, freq="ME")
    if which == "period":
        return pd.period_range("2020-01", periods=n, freq="M")
    return pd.Index([f"r{i}" for i in range(n)])


@st.composite
def series(draw: st.DrawFn) -> pd.Series:
    """kind: ``series_handle`` -- a univariate series with a named index."""
    values = draw(series_values)
    index = draw(indexes(len(values)))
    name = draw(st.one_of(st.none(), st.text(min_size=1, max_size=12)))
    return pd.Series(values, index=index, name=name, dtype=float)


@st.composite
def estimable_series(draw: st.DrawFn) -> pd.Series:
    """A series an ESTIMATOR can be stated over -- see ``estimable_floats``.

    Same four shapes as :func:`series` (general, constant, all-NaN, n = 1), with
    every value either exactly zero or of a magnitude whose square is still a
    normal float. Used by the scale-equivariance and sample-variance properties;
    the serialisation and chart properties use the wider :func:`series`, because
    those must be total over every finite float.
    """
    cell = st.one_of(estimable_floats, st.just(float("nan")))
    shape = draw(st.sampled_from(("general", "constant", "all_nan", "single")))
    if shape == "constant":
        values = [draw(estimable_floats)] * draw(st.integers(min_value=1, max_value=12))
    elif shape == "all_nan":
        values = [float("nan")] * draw(st.integers(min_value=1, max_value=12))
    elif shape == "single":
        values = [draw(cell)]
    else:
        values = draw(st.lists(cell, min_size=1, max_size=24))
    return pd.Series(values, index=draw(indexes(len(values))), dtype=float)


@st.composite
def frames(draw: st.DrawFn) -> pd.DataFrame:
    """kind: ``df_handle`` / ``multiseries_handle`` -- a numeric panel."""
    n_rows = draw(st.integers(min_value=1, max_value=12))
    n_cols = draw(st.integers(min_value=1, max_value=4))
    columns = {
        f"c{j}": draw(st.lists(_cell, min_size=n_rows, max_size=n_rows))
        for j in range(n_cols)
    }
    return pd.DataFrame(columns, index=draw(indexes(n_rows)), dtype=float)


@st.composite
def matrices(draw: st.DrawFn) -> np.ndarray:
    """kind: ``matrix_handle`` -- a 2-D numeric array.

    NOT all-NaN. ``chart_spec._matrix_spec`` calls ``np.nanmin``/``np.nanmax`` to
    build the visual map, and an all-NaN slice makes numpy raise a RuntimeWarning
    that this suite turns into an error (``filterwarnings = ["error"]``). At
    least one finite cell is therefore part of what a matrix input MEANS here,
    and ``tests/test_properties.py`` pins the all-NaN case separately as the
    documented boundary rather than hiding it.
    """
    rows = draw(st.integers(min_value=1, max_value=8))
    cols = draw(st.integers(min_value=1, max_value=8))
    flat = draw(st.lists(_cell, min_size=rows * cols, max_size=rows * cols))
    out = np.asarray(flat, dtype=float).reshape(rows, cols)
    if not np.isfinite(out).any():
        out[0, 0] = draw(finite_floats)
    return out


#: kind: ``raw`` -- an arbitrary nested result mapping, which is what a wrapper
#: actually hands the serialiser: scalars, series and frames inside dicts and
#: lists. Depth is bounded because the property under test is totality, not
#: recursion limits.
payloads: st.SearchStrategy[Any] = st.recursive(
    st.one_of(json_scalars, series(), frames()),
    lambda children: st.one_of(
        st.lists(children, max_size=4),
        st.dictionaries(st.text(min_size=1, max_size=8), children, max_size=4),
    ),
    max_leaves=8,
)
