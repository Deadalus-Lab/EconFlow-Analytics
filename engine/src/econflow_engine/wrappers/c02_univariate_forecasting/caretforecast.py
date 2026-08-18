# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``caretforecast`` -- METHOD-SELECTION card #134.

#134 caretForecast (recursive autoregressive ML forecasting via caret + conformal prediction
    intervals + variable importance)

Category 02-univariate-forecasting; module ``caretforecast``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c02_univariate_forecasting import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "caf_arml",
    "caf_conformal",
    "caf_varimp",
    "NODE_META",
    "wire_model",
]


def caf_arml(
    *,
    y: pd.Series,
    seed: int,
    max_lag: int | None = None,
    caret_method: Literal["lm", "glmnet", "ridge", "lasso"] | None = None,
    pre_process: Any | None = None,
    cv: bool | None = None,
    cv_horizon: int | None = None,
    seasonal: bool | None = None,
    exog: np.ndarray | None = None,
    new_exog: np.ndarray | None = None,
    h: int | None = None,
) -> dict[str, Any]:
    """Node ``caf_arml`` -- METHOD-SELECTION card #134.

    caretForecast (recursive autoregressive ML forecasting via caret + conformal prediction
    intervals + variable importance).

    Category 02-univariate-forecasting; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Handle to a univariate ts (the series to forecast).
        seed: [integer, required] REQUIRED seed (set.seed before caret resampling; cache key;
            uncacheable without it).
        max_lag: [integer, optional] Maximum lag of the autoregressive features (positive integer;
            default 5; length(y)>max_lag+1).
        caret_method: [enum, optional] CLOSED whitelist of lightweight learners (default lm); maps
            internally to caret method+tune_grid; NEVER a free string.
        pre_process: [raw, optional] Optional preprocessing steps (center/scale/range/BoxCox etc.;
            gated to an allowed set; None=none).
        cv: [boolean, optional] Model selection with time-slice CV (default True; cv=False is
            rejected — requires a forbidden tune_grid).
        cv_horizon: [integer, optional] Number of consecutive values in the test set of each
            resample (positive integer; default 4).
        seasonal: [boolean, optional] Fourier terms for seasonality (default True).
        exog: [exog_handle, optional] In-sample exogenous regressors (matrix, nrow==length(y); NOT a
            data frame).
        new_exog: [exog_handle, optional] Future exogenous regressors for the forecast (nrow==h,
            same columns as exog_handle; required if exog_handle is given).
        h: [integer, optional] Forecast horizon (positive integer; None -> frequency(y)).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "caf_arml: not implemented. The method card is in ./README.md."
    )


def caf_conformal(
    *,
    model: Any,
    h: int | None = None,
    confidence: float | None = None,
    new_exog: np.ndarray | None = None,
    y_min: float | None = None,
    y_max: float | None = None,
) -> dict[str, Any]:
    """Node ``caf_conformal`` -- METHOD-SELECTION card #134.

    caretForecast (recursive autoregressive ML forecasting via caret + conformal prediction
    intervals + variable importance).

    Category 02-univariate-forecasting; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to an ARml model (caf_arml$model) — conformal PI from
            its in-sample residuals.
        h: [integer, optional] Forecast horizon (positive integer; None -> frequency(model$y)).
        confidence: [number, optional] Confidence level of the conformal interval ∈ (0,1) (default
            0.95).
        new_exog: [exog_handle, optional] Future regressors if the model was trained with
            exog_handle (NOT a data frame).
        y_min: [number, optional] Lower clip of the intervals (default -Inf).
        y_max: [number, optional] Upper clip of the intervals (> y_min; default Inf).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "caf_conformal: not implemented. The method card is in ./README.md."
    )


def caf_varimp(
    *,
    model: Any,
) -> dict[str, Any]:
    """Node ``caf_varimp`` -- METHOD-SELECTION card #134.

    caretForecast (recursive autoregressive ML forecasting via caret + conformal prediction
    intervals + variable importance).

    Category 02-univariate-forecasting; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to an ARml or forecast object (caf_arml) — variable
            importance of the lags/regressors.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "caf_varimp: not implemented. The method card is in ./README.md."
    )
