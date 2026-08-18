# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``deterministic_rolling_window`` -- METHOD-SELECTION card #105.

#105 Deterministic rolling-window aggregations
    (slide_dbl/slide_index_dbl/slide_period_dbl/hop_index_vec)

Category 00-data-utilities; module ``deterministic_rolling_window``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
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
    "sld_hop_index",
    "sld_slide",
    "sld_slide_index",
    "sld_slide_period",
    "NODE_META",
    "wire_model",
]


def sld_slide(
    *,
    x: pd.Series,
    reducer: Literal["mean", "sum", "sd", "min", "max", "median"] | None = None,
    before: float | None = None,
    after: float | None = None,
    step: int | None = None,
    complete: bool | None = None,
    na_rm: bool | None = None,
) -> dict[str, Any]:
    """Node ``sld_slide`` -- METHOD-SELECTION card #105.

    Deterministic rolling-window aggregations
    (slide_dbl/slide_index_dbl/slide_period_dbl/hop_index_vec).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a numeric series.
        reducer: [enum, optional] Closed reducer (default mean).
        before: [number, optional] Observations before (integer or Inf; negative=look-forward;
            default 0). Default ``0``.
        after: [number, optional] Observations after (integer or Inf; default 0; before+after>=0).
            Default ``0``.
        step: [integer, optional] Slide step >=1 (default 1). Default ``1``.
        complete: [boolean, optional] Complete windows only (default False). Default ``False``.
        na_rm: [boolean, optional] Ignore NA in the reducer (default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "sld_slide: not implemented. The method card is in ./README.md."
    )


def sld_slide_index(
    *,
    x: pd.Series,
    i: Sequence[float],
    reducer: Literal["mean", "sum", "sd", "min", "max", "median"] | None = None,
    before: float | None = None,
    after: float | None = None,
    complete: bool | None = None,
    na_rm: bool | None = None,
) -> dict[str, Any]:
    """Node ``sld_slide_index`` -- METHOD-SELECTION card #105.

    Deterministic rolling-window aggregations
    (slide_dbl/slide_index_dbl/slide_period_dbl/hop_index_vec).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a numeric series.
        i: [num_array, required] Index (same length as x, no NA, increasing); the bounds are
            i-before, i+after.
        reducer: [enum, optional] Closed reducer (default mean).
        before: [number, optional] Backward width in index units (default 0). Default ``0``.
        after: [number, optional] Forward width in index units (default 0). Default ``0``.
        complete: [boolean, optional] Complete windows only (default False). Default ``False``.
        na_rm: [boolean, optional] Ignore NA (default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "sld_slide_index: not implemented. The method card is in ./README.md."
    )


def sld_slide_period(
    *,
    x: pd.Series,
    i: Sequence[float],
    period: (
        Literal[
            "month",
            "quarter",
            "year",
            "week",
            "day",
            "hour",
            "minute",
            "second",
        ]
        | None
    ) = None,
    reducer: Literal["mean", "sum", "sd", "min", "max", "median"] | None = None,
    every: int | None = None,
    before: float | None = None,
    after: float | None = None,
    complete: bool | None = None,
    na_rm: bool | None = None,
) -> dict[str, Any]:
    """Node ``sld_slide_period`` -- METHOD-SELECTION card #105.

    Deterministic rolling-window aggregations
    (slide_dbl/slide_index_dbl/slide_period_dbl/hop_index_vec).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a numeric series.
        i: [num_array, required] Index (same length as x, increasing); split into period blocks.
        period: [enum, optional] Calendar block period (default month).
        reducer: [enum, optional] Closed reducer (default mean).
        every: [integer, optional] Number of periods per block >=1 (default 1). Default ``1``.
        before: [number, optional] BLOCKS backward (default 0). Default ``0``.
        after: [number, optional] BLOCKS forward (default 0). Default ``0``.
        complete: [boolean, optional] Complete windows only (default False). Default ``False``.
        na_rm: [boolean, optional] Ignore NA (default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "sld_slide_period: not implemented. The method card is in ./README.md."
    )


def sld_hop_index(
    *,
    x: pd.Series,
    i: Sequence[float],
    starts: Sequence[float],
    stops: Sequence[float],
    reducer: Literal["mean", "sum", "sd", "min", "max", "median"] | None = None,
    na_rm: bool | None = None,
) -> dict[str, Any]:
    """Node ``sld_hop_index`` -- METHOD-SELECTION card #105.

    Deterministic rolling-window aggregations
    (slide_dbl/slide_index_dbl/slide_period_dbl/hop_index_vec).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a numeric series.
        i: [num_array, required] Index (same length as x, increasing, no NA).
        starts: [num_array, required] Window starts (same length as stops; start<=stop).
        stops: [num_array, required] Window ends; output length = length(starts).
        reducer: [enum, optional] Closed reducer (default mean).
        na_rm: [boolean, optional] Ignore NA (default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "sld_hop_index: not implemented. The method card is in ./README.md."
    )
