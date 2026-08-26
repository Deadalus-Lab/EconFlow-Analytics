# SPDX-License-Identifier: AGPL-3.0-only
"""Continuous benchmarks for ``serialize.to_mcp``, the response path.

EVERY node reply leaves the engine through ``to_mcp``. A regression there is
paid once per call and no correctness gate can see it: the assertions stay green
while the answer arrives slower. These four measure it against the payload
SHAPES THE CONTRACT ACTUALLY RETURNS, which is the whole design constraint here.

WHY NOT A SCALAR. ``to_mcp(42)`` dispatches once and returns; it measures
``functools.singledispatch`` and nothing this engine owns. The cost that matters
is per element -- ``to_mcp`` recurses into every value of a Series, every cell of
a frame, and calls ``_clean_float`` on each float to fold NaN and inf to null --
so a benchmark only says something if the payload is the size a real reply is.

A DatetimeIndex IS NOT SERIALISED ELEMENT-WISE, measured rather than assumed:
``pd.DatetimeIndex`` is not a ``collections.abc.Sequence``, registers no handler,
and so reaches the catch-all and STUBS. The index work the engine really does is
the ``_iso_index_label`` call per label inside the Series handler, which is where
the nested payload below puts its timestamps. ``test_a_bare_index_stubs`` pins
the stub outcome so this note cannot rot into a false claim.

Each benchmark ASSERTS its result. A benchmark that measures a function which has
started returning the wrong answer is a stopwatch on a broken clock.
"""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd

from econflow_engine.serialize import to_mcp

# Built once at import: the fixture measures the CALL, never the construction.
_N = 1000
SERIES = pd.Series(
    np.linspace(0.0, 100.0, _N),
    index=pd.date_range("1990-01-31", periods=_N, freq="ME"),
    name="gdp_growth",
)

FRAME = pd.DataFrame(
    np.arange(100 * 20, dtype=float).reshape(100, 20),
    columns=[f"v{i}" for i in range(20)],
)

# A fitted-model reply: point estimates, a covariance matrix, a dated fitted
# series and a metadata block -- arrays, dicts and timestamps in one object.
NESTED: dict[str, Any] = {
    "coefficients": np.linspace(-1.0, 1.0, 200),
    "covariance": np.eye(30),
    "fitted": pd.Series(
        np.linspace(0.0, 1.0, 240),
        index=pd.date_range("2005-01-01", periods=240, freq="MS"),
        name="fitted",
    ),
    "residuals": [float(v) for v in np.linspace(-0.5, 0.5, 200)],
    "diagnostics": {"n_obs": 240, "converged": True, "aic": 812.5, "note": "ok"},
}

# One in four values is null, so `_clean_float` returns None on a real share of
# the elements rather than on none of them.
WITH_NAN = pd.Series(
    [np.nan if i % 4 == 0 else float(i) for i in range(_N)],
    index=pd.date_range("1990-01-31", periods=_N, freq="ME"),
    name="with_gaps",
)


def test_to_mcp_on_a_thousand_point_dated_series(benchmark: Any) -> None:
    """The commonest reply in the catalogue: one series, one datetime index."""
    out = benchmark(lambda: to_mcp(SERIES))

    assert len(out["values"]) == _N
    assert out["frequency"] == "ME"
    assert out["index"][0] == "1990-01-31T00:00:00"
    assert out["name"] == "gdp_growth"


def test_to_mcp_on_a_hundred_by_twenty_frame(benchmark: Any) -> None:
    """Record-oriented output: 2000 cells become 100 objects of 20 keys."""
    out = benchmark(lambda: to_mcp(FRAME))

    assert len(out) == 100
    assert len(out[0]) == 20
    assert out[0]["v0"] == 0.0
    assert out[99]["v19"] == 1999.0


def test_to_mcp_on_a_nested_fitted_result(benchmark: Any) -> None:
    """Arrays, a matrix, a dated series and a metadata dict in one payload."""
    out = benchmark(lambda: to_mcp(NESTED))

    assert out["covariance"]["dim"] == [30, 30]
    assert len(out["coefficients"]) == 200
    assert out["fitted"]["index"][0] == "2005-01-01T00:00:00"
    assert out["diagnostics"]["converged"] is True


def test_to_mcp_on_a_series_carrying_nulls(benchmark: Any) -> None:
    """NaN folds to null per element, which is the cost this one isolates."""
    out = benchmark(lambda: to_mcp(WITH_NAN))

    values = out["values"]
    assert len(values) == _N
    assert values[0] is None
    assert values[1] == 1.0
    assert sum(v is None for v in values) == _N // 4


def test_a_bare_index_stubs_rather_than_serialising() -> None:
    """The premise of the nested payload above, pinned so it cannot rot.

    Not a benchmark: it states WHY the timestamps travel inside a Series.
    """
    out = to_mcp(pd.date_range("2020-01-01", periods=3, freq="MS"))

    assert out["@mcp_serialized"] is False
    assert out["@mcp_class"] == ["DatetimeIndex"]
