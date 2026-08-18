# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``fast_lead_lag`` -- METHOD-SELECTION card #108.

#108 Fast (C) lead/lag + rolling-window aggregates + rolling robust reducers (shift, froll family,
    frollapply closed reducer set)

Category 00-data-utilities; module ``fast_lead_lag``.

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
    "dt_roll",
    "dt_roll_apply",
    "dt_shift",
    "NODE_META",
    "wire_model",
]


def dt_shift(
    *,
    x: pd.Series,
    n: Sequence[int] | None = None,
    type: Literal["lag", "lead", "shift", "cyclic"] | None = None,
    fill: float | None = None,
) -> dict[str, Any]:
    """Node ``dt_shift`` -- METHOD-SELECTION card #108.

    Fast (C) lead/lag + rolling-window aggregates + rolling robust reducers (shift, froll family,
    frollapply closed reducer set).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a single numeric series (vector).
        n: [int_array, optional] Integer offset or vector of offsets (several -> list of series;
            default 1). Default ``1``.
        type: [enum, optional] lag=backwards, lead=forwards, shift==lag, cyclic=wrap-around (default
            lag).
        fill: [number, optional] Padding value for the gaps (default NA).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "dt_shift: not implemented. The method card is in ./README.md."
    )


def dt_roll(
    *,
    x: pd.Series,
    n: Sequence[int],
    statistic: Literal["mean", "sum", "sd", "max", "min"] | None = None,
    fill: float | None = None,
    align: Literal["right", "left", "center"] | None = None,
    na_rm: bool | None = None,
    adaptive: bool | None = None,
) -> dict[str, Any]:
    """Node ``dt_roll`` -- METHOD-SELECTION card #108.

    Fast (C) lead/lag + rolling-window aggregates + rolling robust reducers (shift, froll family,
    frollapply closed reducer set).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a single numeric series (vector).
        n: [int_array, required] Window size (integer >=1); with adaptive=True a vector of length
            length(x).
        statistic: [enum, optional] Rolling aggregate (froll*); default mean.
        fill: [number, optional] Padding value for the initial positions (default NA).
        align: [enum, optional] Window alignment (default right; center is forbidden when adaptive).
        na_rm: [boolean, optional] Ignore NA inside the window (default False). Default ``False``.
        adaptive: [boolean, optional] Per-observation window (n a vector of length length(x));
            default False. Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "dt_roll: not implemented. The method card is in ./README.md."
    )


def dt_roll_apply(
    *,
    x: pd.Series,
    n: int,
    FUN: (
        Literal[
            "median",
            "mad",
            "IQR",
            "var",
            "sd",
            "mean",
            "sum",
            "min",
            "max",
            "prod",
        ]
        | None
    ) = None,
    fill: float | None = None,
    align: Literal["right", "left", "center"] | None = None,
    na_rm: bool | None = None,
) -> dict[str, Any]:
    """Node ``dt_roll_apply`` -- METHOD-SELECTION card #108.

    Fast (C) lead/lag + rolling-window aggregates + rolling robust reducers (shift, froll family,
    frollapply closed reducer set).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a single numeric series (vector).
        n: [integer, required] Rolling window size (integer >=1).
        FUN: [enum, optional] Closed set of named reducers (SECURITY: NEVER caller code); default
            median.
        fill: [number, optional] Padding value for the initial positions (default NA).
        align: [enum, optional] Window alignment (default right).
        na_rm: [boolean, optional] Ignore NA inside the window (default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "dt_roll_apply: not implemented. The method card is in ./README.md."
    )
