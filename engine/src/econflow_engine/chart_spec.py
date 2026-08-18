# SPDX-License-Identifier: AGPL-3.0-only
"""ECharts specification emitter.

Sibling of :mod:`econflow_engine.serialize`, same reasoning, different output:

    to_mcp(x)      -> JSON-safe DATA        (what the node computed)
    chart_spec(x)  -> JSON-safe ECharts SPEC (how it is drawn)

THE INVARIANT: charts are drawn ONLY by the client. Nothing here produces an
image, HTML or a widget -- only a mapping that becomes JSON and is rendered by
the browser.

THE THREAT THE PURITY GATE CLOSES. The danger
was concrete: a JavaScript-callback marker landed inside the options as a string of
class ``JS_EVAL``, i.e. EXECUTABLE CODE travelling from the engine to the browser
and running there -- cross-site scripting with the engine as the source. This
port builds the option mapping directly, so no widget library can inject a
callback behind our back. THE GATE STAYS ANYWAY, for a reason that has not
changed: a wrapper body may build part of a spec itself, and a specification that
contains code is WRONG, not dirty. It is refused as a GATE, never silently
cleaned.
"""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd

from econflow_engine.errors import GateError

__all__ = ["CHART_MAX_CELLS", "CHART_MAX_POINTS", "assert_pure", "chart_spec"]

_FORBIDDEN_PATTERNS = ("function(", "=>", "<script", "javascript:", "new Function")

#: A specification with more points than the screen has pixels is not a chart.
CHART_MAX_POINTS = 200_000
CHART_MAX_CELLS = 20_000


def _gate(message: str) -> GateError:
    return GateError("other", message, detail_code="chart-spec")


def _check_text(value: str, path: str, what: str) -> None:
    for pattern in _FORBIDDEN_PATTERNS:
        if pattern in value:
            raise _gate(
                f"chart_spec: the specification contains executable code at {path} "
                f"({what}: '{pattern}'). The engine emits ONLY data and specification; "
                "chart code belongs exclusively to the client."
            )


def assert_pure(spec: object, path: str = "spec") -> object:
    """Refuse any specification that carries code, a live object, or markup."""
    if callable(spec):
        raise _gate(
            f"chart_spec: the specification contains a callable at {path}. An ECharts "
            "specification is DATA -- nothing executable leaves the engine."
        )
    if isinstance(spec, str):
        _check_text(spec, path, "pattern")
        return spec
    if isinstance(spec, dict):
        for key, item in spec.items():
            if not isinstance(key, str):
                raise _gate(f"chart_spec: non-string key at {path} ({type(key).__name__}).")
            _check_text(key, f"{path}.{key}", "field name")
            assert_pure(item, f"{path}.{key}")
        return spec
    if isinstance(spec, list | tuple):
        for i, item in enumerate(spec):
            assert_pure(item, f"{path}[{i}]")
        return spec
    if spec is None or isinstance(spec, bool | int | float):
        return spec
    raise _gate(
        f"chart_spec: the specification contains a non JSON-safe object "
        f"('{type(spec).__name__}') at {path}."
    )


def _check_points(n: int, what: str) -> None:
    if n > CHART_MAX_POINTS:
        raise _gate(
            f"chart_spec: {what} gives {n} points -- the maximum per specification is "
            f"{CHART_MAX_POINTS}. Restrict the time range or the number of series."
        )


def _label(value: object, fallback: str) -> str:
    text = "" if value is None else str(value)
    if not text or text == "nan":
        text = fallback
    return "".join(" " if ord(c) < 32 or ord(c) == 127 else c for c in text)


def _decorate(option: dict[str, Any], title: str | None, trigger: str) -> dict[str, Any]:
    if title is not None:
        option["title"] = [{"text": _label(title, "chart")}]
    option["tooltip"] = {"trigger": trigger}
    return option


def _empty(text: str, subtext: str | None = None) -> dict[str, Any]:
    title: dict[str, Any] = {"text": _label(text, "chart")}
    if subtext is not None:
        title["subtext"] = subtext
    return {
        "title": [title],
        "xAxis": [{"type": "category", "data": []}],
        "yAxis": [{"type": "value"}],
        "series": [],
    }


def _numbers(values: Any) -> list[float | None]:
    return [None if v is None or not np.isfinite(v) else float(v) for v in np.asarray(values,
                                                                                      dtype=float)]


def _axis_labels(index: pd.Index) -> list[str]:
    if isinstance(index, pd.DatetimeIndex | pd.PeriodIndex):
        return [pd.Timestamp(str(t)).isoformat() for t in index]
    return [str(v) for v in index]


def _series_spec(series: pd.Series, title: str | None) -> dict[str, Any]:
    _check_points(len(series), "the series")
    option = {
        "xAxis": [{"type": "category", "data": _axis_labels(series.index)}],
        "yAxis": [{"type": "value"}],
        "series": [
            {
                "type": "line",
                "name": _label(series.name, "value"),
                "data": _numbers(series.to_numpy()),
            }
        ],
    }
    return _decorate(option, title, "axis")


def _frame_spec(frame: pd.DataFrame, title: str | None) -> dict[str, Any]:
    numeric = [c for c in frame.columns if pd.api.types.is_numeric_dtype(frame[c])]
    if not numeric:
        return _empty(title or "data frame", "no numeric column to draw")
    _check_points(len(frame) * len(numeric), "the panel")
    option = {
        "xAxis": [{"type": "category", "data": _axis_labels(frame.index)}],
        "yAxis": [{"type": "value"}],
        "series": [
            {
                "type": "line",
                "name": _label(c, f"s{j + 1}"),
                "data": _numbers(frame[c].to_numpy()),
            }
            for j, c in enumerate(numeric)
        ],
    }
    return _decorate(option, title, "axis")


def _matrix_spec(matrix: np.ndarray, title: str | None) -> dict[str, Any]:
    if not np.issubdtype(matrix.dtype, np.number):
        raise _gate(
            "chart_spec: a heatmap needs a NUMERIC matrix -- the array given is "
            f"'{matrix.dtype}'."
        )
    rows, cols = matrix.shape
    if rows == 0 or cols == 0:
        return _empty(title or "matrix", "empty matrix")
    if rows * cols > CHART_MAX_CELLS:
        raise _gate(
            f"chart_spec: a heatmap of {rows}x{cols} = {rows * cols} cells -- the maximum "
            f"is {CHART_MAX_CELLS}. A heatmap with more cells than pixels is unreadable "
            "in any case."
        )
    values = matrix.astype(float)
    data = [
        [j, i, None if not np.isfinite(values[i, j]) else float(values[i, j])]
        for i in range(rows)
        for j in range(cols)
    ]
    option = {
        "xAxis": [{"type": "category", "data": [f"c{j + 1}" for j in range(cols)]}],
        "yAxis": [{"type": "category", "data": [f"r{i + 1}" for i in range(rows)]}],
        "visualMap": [
            {"min": float(np.nanmin(values)), "max": float(np.nanmax(values)),
             "calculable": True}
        ],
        "series": [{"type": "heatmap", "data": data}],
    }
    return _decorate(option, title, "item")


def chart_spec(value: object, title: str | None = None) -> dict[str, Any] | None:
    """Build an ECharts option mapping, then run the purity gate over it.

    The gate runs LAST and over the finished specification, as the contract
    requires: it
    must see whatever actually leaves the engine, not what the emitter intended.
    """
    if value is None:
        return None
    if isinstance(value, pd.Series):
        option = _series_spec(value, title)
    elif isinstance(value, pd.DataFrame):
        option = _frame_spec(value, title)
    elif isinstance(value, np.ndarray) and value.ndim == 2:
        option = _matrix_spec(value, title)
    elif isinstance(value, np.ndarray) and value.ndim == 1:
        option = _series_spec(pd.Series(value), title)
    elif isinstance(value, dict):
        option = dict(value)
    else:
        option = _empty(
            title or type(value).__name__,
            f"there is no chart specification for type '{type(value).__name__}'",
        )
    assert_pure(option)
    return option
