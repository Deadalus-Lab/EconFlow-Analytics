# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``detection_structural_breaks`` -- METHOD-SELECTION card #128.

#128 Detection of structural breaks in the trend & seasonality of seasonal time series (BFAST:
    iterative STL + breakpoints) + near-real-time disturbance monitoring

Category 01-preparation-prechecks; module ``detection_structural_breaks``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c01_preparation_prechecks import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "bf_bfast",
    "bf_monitor",
    "NODE_META",
    "wire_model",
]


def bf_bfast(
    *,
    Yt: pd.Series,
    h: float | None = None,
    season: Literal["dummy", "harmonic", "none"] | None = None,
    max_iter: int | None = None,
    breaks: Any | None = None,
    level: Sequence[float] | None = None,
    decomp: Literal["stl", "stlplus"] | None = None,
) -> dict[str, Any]:
    """Node ``bf_bfast`` -- METHOD-SELECTION card #128.

    Detection of structural breaks in the trend & seasonality of seasonal time series (BFAST:
    iterative STL + breakpoints) + near-real-time disturbance monitoring.

    Category 01-preparation-prechecks; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        Yt: [series_handle, required] Handle to a univariate regular 'ts', frequency > 1, n >=
            2*frequency (NA only with decomp='stlplus').
        h: [number, optional] Minimum segment as a fraction of the sample, strictly (0,1) (default
            0.15). Default ``0.15``.
        season: [enum, optional] Seasonal model: dummy (RSE-1) / harmonic (RSE-2) / none (default
            dummy).
        max_iter: [integer, optional] Maximum breakpoint estimation iterations (positive integer,
            default 10). Default ``10``.
        breaks: [raw, optional] None=auto· positive integer, 1-2 values (trend, seasonal)· or a
            string statistic (BIC/LWZ/RSS...).
        level: [num_array, optional] Threshold sctest.efp· 1 or 2 values (trend, seasonal), each in
            (0,1) (default 0.05). Default ``0.05``.
        decomp: [enum, optional] Decomposition: stl (default) or stlplus (handles NA· mandatory if
            NA are present).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bf_bfast: not implemented. The method card is in ./README.md."
    )


def bf_monitor(
    *,
    data: pd.Series,
    start: Sequence[float],
    history: Literal["ROC", "BP", "all"] | None = None,
    order: int | None = None,
    h: float | None = None,
    level: Sequence[float] | None = None,
) -> dict[str, Any]:
    """Node ``bf_monitor`` -- METHOD-SELECTION card #128.

    Detection of structural breaks in the trend & seasonality of seasonal time series (BFAST:
    iterative STL + breakpoints) + near-real-time disturbance monitoring.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        data: [series_handle, required] Handle to a univariate 'ts', frequency > 1 (for the harmon
            component).
        start: [num_array, required] Start of the monitoring period: float (e.g. 2013.0) or a
            length-2 vector [year, period].
        history: [enum, optional] Stable history selection: ROC (rev-CUSUM, default) / BP
            (Bai-Perron) / all.
        order: [integer, optional] Order of the harmonic term (positive integer, default 3). Default
            ``3``.
        h: [number, optional] Bandwidth of the MOSUM monitoring process, strictly (0,1) (default
            0.25). Default ``0.25``.
        level: [num_array, optional] Significance levels (monitoring, ROC)· 1 or 2 values in (0,1)
            (default 0.05,0.05). Default ``[0.05, 0.05]``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bf_monitor: not implemented. The method card is in ./README.md."
    )
