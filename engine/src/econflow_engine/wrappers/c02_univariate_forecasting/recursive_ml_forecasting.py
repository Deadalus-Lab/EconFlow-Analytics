# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``recursive_ml_forecasting`` -- method card #134.

#134 Recursive autoregressive machine-learning forecasting with conformal prediction intervals

Category 02-univariate-forecasting; module ``recursive_ml_forecasting``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
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
    "rml_conformal",
    "rml_fit",
    "rml_variable_importance",
    "NODE_META",
    "wire_model",
]


def rml_fit(
    *,
    y: pd.Series,
    seed: int,
    max_lag: int | None = None,
    learner_method: Literal["lm", "elastic_net", "ridge", "lasso"] | None = None,
    pre_process: Any | None = None,
    cv: bool | None = None,
    cv_horizon: int | None = None,
    seasonal: bool | None = None,
    exog: np.ndarray | None = None,
    new_exog: np.ndarray | None = None,
    h: int | None = None,
) -> dict[str, Any]:
    """Node ``rml_fit`` -- method card #134.

    Recursive autoregressive machine-learning forecasting with conformal prediction intervals.

    Category 02-univariate-forecasting; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Handle to a univariate ts (the series to forecast).
        seed: [integer, required] REQUIRED seed (seeded before resampling; cache key; uncacheable
            without it).
        max_lag: [integer, optional] Maximum lag of the autoregressive features (positive integer;
            default 5; length(y)>max_lag+1).
        learner_method: [enum, optional] CLOSED whitelist of lightweight learners (default lm); maps
            internally to the learner method and tuning grid; NEVER a free string.
        pre_process: [raw, optional] Optional preprocessing steps (center/scale/range/BoxCox etc.;
            gated to an allowed set; None=none).
        cv: [boolean, optional] Model selection with time-slice CV (default True; cv=False is
            rejected — requires a forbidden tuning grid).
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
        "rml_fit: not implemented."
    )


def rml_conformal(
    *,
    model: Any,
    h: int | None = None,
    confidence: float | None = None,
    new_exog: np.ndarray | None = None,
    y_min: float | None = None,
    y_max: float | None = None,
) -> dict[str, Any]:
    """Node ``rml_conformal`` -- method card #134.

    Recursive autoregressive machine-learning forecasting with conformal prediction intervals.

    Category 02-univariate-forecasting; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to an ARml model (rml_fit.model) — conformal PI from
            its in-sample residuals.
        h: [integer, optional] Forecast horizon (positive integer; None -> frequency(model.y)).
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
        "rml_conformal: not implemented."
    )


def rml_variable_importance(
    *,
    model: Any,
) -> dict[str, Any]:
    """Node ``rml_variable_importance`` -- method card #134.

    Recursive autoregressive machine-learning forecasting with conformal prediction intervals.

    Category 02-univariate-forecasting; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to an ARml or forecast object (rml_fit) — variable
            importance of the lags/regressors.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "rml_variable_importance: not implemented."
    )
