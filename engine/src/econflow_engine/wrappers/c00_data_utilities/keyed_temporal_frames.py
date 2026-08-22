# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``keyed_temporal_frames`` -- method card #113.

#113 Tidy temporal data frames — an explicit key/index contract + structural gap handling
    (detect/list/count/fill) + CLOSED-vocabulary calendar aggregation

Category 00-data-utilities; module ``keyed_temporal_frames``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c00_data_utilities import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "tt_build",
    "tt_fill_gaps",
    "tt_gaps",
    "tt_index_aggregate",
    "NODE_META",
    "wire_model",
]


def tt_build(
    *,
    data: pd.DataFrame,
    index: str,
    key: Sequence[str] | None = None,
    regular: bool | None = None,
) -> dict[str, Any]:
    """Node ``tt_build`` -- method card #113.

    Tidy temporal data frames — an explicit key/index contract + structural gap handling
    (detect/list/count/fill) + CLOSED-vocabulary calendar aggregation.

    Category 00-data-utilities; memory class ``light``.

    Registers its result under ``series``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] Handle to a long DataFrame (index column + optional key cols +
            measured values).
        index: [string, required] ONE time column name (index). For monthly/quarterly data pass a
            yearmonth/yearquarter index, NOT a raw Date (otherwise interval=1D — a silent trap).
        key: [series_codes, optional] Grouping columns (key); one series per (key,index) combination
            — validated.
        regular: [boolean, optional] True=regular interval (default); False=irregular. Default
            ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "tt_build: not implemented."
    )


def tt_gaps(
    *,
    x: pd.DataFrame,
    kind: Literal["has", "scan", "count"] | None = None,
    full: bool | None = None,
) -> dict[str, Any]:
    """Node ``tt_gaps`` -- method card #113.

    Tidy temporal data frames — an explicit key/index contract + structural gap handling
    (detect/list/count/fill) + CLOSED-vocabulary calendar aggregation.

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [df_handle, required] Handle to a series (tbl_ts — from tt_build; the class is preserved
            through df_handle).
        kind: [enum, optional] has=1 logical/key; scan=the missing (key,index) rows;
            count=(.from,.to,.n) (default has).
        full: [boolean, optional] True=common span across all keys; False=per key (default). Default
            ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "tt_gaps: not implemented."
    )


def tt_fill_gaps(
    *,
    x: pd.DataFrame,
    full: bool | None = None,
) -> dict[str, Any]:
    """Node ``tt_fill_gaps`` -- method card #113.

    Tidy temporal data frames — an explicit key/index contract + structural gap handling
    (detect/list/count/fill) + CLOSED-vocabulary calendar aggregation.

    Category 00-data-utilities; memory class ``light``.

    Registers its result under ``series``, so a later node can consume it as a handle.

    Args:
        x: [df_handle, required] Handle to a series (tbl_ts).
        full: [boolean, optional] True=fill up to the common span of all keys; False=per key
            (default). Deterministic NA-fill only. Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "tt_fill_gaps: not implemented."
    )


def tt_index_aggregate(
    *,
    x: pd.DataFrame,
    value_cols: Sequence[str],
    to: Literal["year", "quarter", "month", "week"] | None = None,
    reducer: Literal["mean", "sum", "min", "max", "median"] | None = None,
    by_key: bool | None = None,
) -> dict[str, Any]:
    """Node ``tt_index_aggregate`` -- method card #113.

    Tidy temporal data frames — an explicit key/index contract + structural gap handling
    (detect/list/count/fill) + CLOSED-vocabulary calendar aggregation.

    Category 00-data-utilities; memory class ``light``.

    Registers its result under ``series``, so a later node can consume it as a handle.

    Args:
        x: [df_handle, required] Handle to a series (tbl_ts).
        value_cols: [series_codes, required] Numeric measured columns to aggregate (not index/key).
        to: [enum, optional] Calendar bucketer towards a LOWER frequency (default year).
        reducer: [enum, optional] Closed reducer (default mean) — NEVER free long-format-eval.
        by_key: [boolean, optional] True=per key (group_by_key); False=collapse all keys together
            (default True — otherwise a silent key-collapse). Default ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "tt_index_aggregate: not implemented."
    )
