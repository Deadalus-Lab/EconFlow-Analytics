# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``rolling_windowed_series`` -- METHOD-SELECTION card #107.

#107 Rolling / windowed series transforms (rate-of-change, momentum, moving-average smoothers,
    single-series rolling stats, rolling cor/cov)

Category 00-data-utilities; module ``rolling_windowed_series``.

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
    "ttr_ma",
    "ttr_momentum",
    "ttr_roc",
    "ttr_run",
    "ttr_run_cor",
    "NODE_META",
    "wire_model",
]


def ttr_roc(
    *,
    x: pd.Series,
    n: int | None = None,
    type: Literal["continuous", "discrete"] | None = None,
) -> dict[str, Any]:
    """Node ``ttr_roc`` -- METHOD-SELECTION card #107.

    Rolling / windowed series transforms (rate-of-change, momentum, moving-average smoothers,
    single-series rolling stats, rolling cor/cov).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a univariate series (coerced to numeric).
        n: [integer, optional] Rate-of-change periods (integer in [1, length]; default 1). Default
            ``1``.
        type: [enum, optional] continuous=log return (default), discrete=simple % change.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ttr_roc: not implemented. The method card is in ./README.md."
    )


def ttr_momentum(
    *,
    x: pd.Series,
    n: int | None = None,
) -> dict[str, Any]:
    """Node ``ttr_momentum`` -- METHOD-SELECTION card #107.

    Rolling / windowed series transforms (rate-of-change, momentum, moving-average smoothers,
    single-series rolling stats, rolling cor/cov).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a univariate series.
        n: [integer, optional] Momentum difference periods (integer in [1, length]; default 1).
            Default ``1``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ttr_momentum: not implemented. The method card is in ./README.md."
    )


def ttr_ma(
    *,
    x: pd.Series,
    n: int | None = None,
    type: Literal["SMA", "EMA", "WMA", "DEMA", "ZLEMA", "HMA", "ALMA"] | None = None,
    wilder: bool | None = None,
    ratio: float | None = None,
    wts: Sequence[float] | None = None,
    v: float | None = None,
    offset: float | None = None,
    sigma: float | None = None,
) -> dict[str, Any]:
    """Node ``ttr_ma`` -- METHOD-SELECTION card #107.

    Rolling / windowed series transforms (rate-of-change, momentum, moving-average smoothers,
    single-series rolling stats, rolling cor/cov).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a univariate series to smooth.
        n: [integer, optional] MA window length (integer in [1, length]; default 10). Default
            ``10``.
        type: [enum, optional] Moving-average type (default SMA).
        wilder: [boolean, optional] EMA/DEMA: Wilder exponential smoothing (default False). Default
            ``False``.
        ratio: [number, optional] EMA/DEMA/ZLEMA: smoothing ratio in (0,1]; empty=use n.
        wts: [num_array, optional] WMA: weights of length n or length(series); empty=1:n.
        v: [number, optional] DEMA volume factor in [0,1] (default 1). Default ``1``.
        offset: [number, optional] ALMA offset in [0,1] (default 0.85). Default ``0.85``.
        sigma: [number, optional] ALMA sigma > 0 (default 6). Default ``6``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ttr_ma: not implemented. The method card is in ./README.md."
    )


def ttr_run(
    *,
    x: pd.Series,
    n: int | None = None,
    fun: Literal["sum", "mean", "sd", "min", "max", "median", "mad", "var"] | None = None,
) -> dict[str, Any]:
    """Node ``ttr_run`` -- METHOD-SELECTION card #107.

    Rolling / windowed series transforms (rate-of-change, momentum, moving-average smoothers,
    single-series rolling stats, rolling cor/cov).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a univariate series.
        n: [integer, optional] Rolling window length (integer in [1, length]; default 10). Default
            ``10``.
        fun: [enum, optional] Rolling-window statistic (default sum).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ttr_run: not implemented. The method card is in ./README.md."
    )


def ttr_run_cor(
    *,
    x: pd.Series,
    y: pd.Series,
    n: int | None = None,
    method: Literal["cor", "cov"] | None = None,
) -> dict[str, Any]:
    """Node ``ttr_run_cor`` -- METHOD-SELECTION card #107.

    Rolling / windowed series transforms (rate-of-change, momentum, moving-average smoothers,
    single-series rolling stats, rolling cor/cov).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to the 1st univariate series.
        y: [series_handle, required] Handle to the 2nd univariate series (SAME length as x).
        n: [integer, optional] Rolling window length (integer in [1, length]; default 10). Default
            ``10``.
        method: [enum, optional] cor=correlation, cov=covariance (default cor).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ttr_run_cor: not implemented. The method card is in ./README.md."
    )
