# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``indexed_time_series`` -- method card #106.

#106 Indexed (time-stamped) time-series toolbox (periodicity->OHLC, calendar-period aggregation,
    index merge/join, intraday alignment)

Category 00-data-utilities; module ``indexed_time_series``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c00_data_utilities import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "idx_align_time",
    "idx_apply_monthly",
    "idx_merge",
    "idx_period_apply",
    "idx_to_period",
    "NODE_META",
    "wire_model",
]


def idx_to_period(
    *,
    x: pd.Series,
    period: (
        Literal[
            "months",
            "quarters",
            "years",
            "weeks",
            "days",
            "hours",
            "minutes",
            "seconds",
        ]
        | None
    ) = None,
    k: int | None = None,
    OHLC: bool | None = None,
) -> dict[str, Any]:
    """Node ``idx_to_period`` -- method card #106.

    Indexed (time-stamped) time-series toolbox (periodicity->OHLC, calendar-period aggregation,
    index merge/join, intraday alignment).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [irregular_series_handle, required] Handle to a time series with a valid time index;
            univariate or genuine 4-col OHLC.
        period: [enum, optional] Target OHLC frequency (it must be LOWER; default months).
        k: [integer, optional] Sub-periods per new period (positive integer; default 1). Default
            ``1``.
        OHLC: [boolean, optional] True=Open/High/Low/Close per period; False=closing value only
            (default True). Default ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "idx_to_period: not implemented."
    )


def idx_period_apply(
    *,
    x: pd.Series,
    on: (
        Literal[
            "months",
            "quarters",
            "years",
            "weeks",
            "days",
            "hours",
            "minutes",
            "seconds",
        ]
        | None
    ) = None,
    k: int | None = None,
    fun: Literal["mean", "sum", "median", "sd", "min", "max", "first", "last"] | None = None,
    na_rm: bool | None = None,
) -> dict[str, Any]:
    """Node ``idx_period_apply`` -- method card #106.

    Indexed (time-stamped) time-series toolbox (periodicity->OHLC, calendar-period aggregation,
    index merge/join, intraday alignment).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [irregular_series_handle, required] Handle to a time series with a time index, to
            aggregate per period.
        on: [enum, optional] Calendar aggregation period (default months).
        k: [integer, optional] Periods per interval (positive integer; default 1). Default ``1``.
        fun: [enum, optional] Whitelisted aggregator per column (default mean).
        na_rm: [boolean, optional] Ignore NA in the aggregation (default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "idx_period_apply: not implemented."
    )


def idx_apply_monthly(
    *,
    x: pd.Series,
    fun: Literal["mean", "sum", "median", "sd", "min", "max", "first", "last"] | None = None,
    na_rm: bool | None = None,
) -> dict[str, Any]:
    """Node ``idx_apply_monthly`` -- method card #106.

    Indexed (time-stamped) time-series toolbox (periodicity->OHLC, calendar-period aggregation,
    index merge/join, intraday alignment).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [irregular_series_handle, required] Handle to a time series with a time index, to
            aggregate monthly.
        fun: [enum, optional] Whitelisted aggregator per calendar month (default mean).
        na_rm: [boolean, optional] Ignore NA in the aggregation (default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "idx_apply_monthly: not implemented."
    )


def idx_merge(
    *,
    x: pd.Series,
    y: pd.Series,
    join: Literal["outer", "inner", "left", "right"] | None = None,
    fill: float | None = None,
) -> dict[str, Any]:
    """Node ``idx_merge`` -- method card #106.

    Indexed (time-stamped) time-series toolbox (periodicity->OHLC, calendar-period aggregation,
    index merge/join, intraday alignment).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [irregular_series_handle, required] Handle to the 1st time series (index join key).
        y: [irregular_series_handle, required] Handle to the 2nd time series, to join on the common
            time index.
        join: [enum, optional] outer=all rows, inner=common index, left=all of x, right=all of y
            (default outer).
        fill: [number, optional] Value for empty cells (default NA).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "idx_merge: not implemented."
    )


def idx_align_time(
    *,
    x: pd.Series,
    n: float | None = None,
) -> dict[str, Any]:
    """Node ``idx_align_time`` -- method card #106.

    Indexed (time-stamped) time-series toolbox (periodicity->OHLC, calendar-period aggregation,
    index merge/join, intraday alignment).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [irregular_series_handle, required] Handle to an intraday time series with a timestamp
            index (required).
        n: [number, optional] Rounding window in SECONDS (positive; default 60). Default ``60``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "idx_align_time: not implemented."
    )
