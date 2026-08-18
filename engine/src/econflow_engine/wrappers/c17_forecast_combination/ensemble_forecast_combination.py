# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``ensemble_forecast_combination`` -- METHOD-SELECTION card #85.

#85 Ensemble forecast combination (equal / in-sample / CV weights)

Category 17-forecast-combination; module ``ensemble_forecast_combination``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c17_forecast_combination import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "run_hybrid",
    "NODE_META",
    "wire_model",
]


def run_hybrid(
    *,
    y: pd.Series,
    models: str | None = None,
    weights: Literal["equal", "insample.errors", "cv.errors"] | None = None,
    errorMethod: Literal["RMSE", "MAE", "MASE"] | None = None,
    h: int | None = None,
    PI_combination: Literal["extreme", "mean"] | None = None,
    cvHorizon: int | None = None,
    windowSize: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``run_hybrid`` -- METHOD-SELECTION card #85.

    Ensemble forecast combination (equal / in-sample / CV weights).

    Category 17-forecast-combination; memory class ``light``.

    Args:
        y: [series_handle, required] Handle to a univariate ts/numeric series to forecast.
        models: [string, optional] String of component-model letters (>=2 distinct): a=auto.arima
            e=ets f=thetam n=nnetar s=stlm t=tbats z=snaive (default 'aefnst'). Default
            ``'aefnst'``.
        weights: [enum, optional] Combination weighting method (default equal).
        errorMethod: [enum, optional] Error metric for the weights (when weights != equal; default
            RMSE).
        h: [integer, optional] Forecast horizon (positive integer); default 2*frequency if seasonal,
            otherwise 10.
        PI_combination: [enum, optional] How the components' prediction intervals are combined
            (default extreme; the PI are OVER-CONSERVATIVE, non-nominal coverage).
        cvHorizon: [integer, optional] CV horizon (only weights='cv.errors'; default frequency(y)).
        windowSize: [integer, optional] CV window length (only weights='cv.errors'; default 84).
            Default ``84``.
        seed: [integer, optional] Seed for DETERMINISM (nnetar's 'n' is stochastic; default 42).
            Default ``42``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "run_hybrid: not implemented. The method card is in ./README.md."
    )
