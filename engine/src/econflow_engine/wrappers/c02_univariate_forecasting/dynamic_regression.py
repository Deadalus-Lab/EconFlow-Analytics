# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``dynamic_regression`` -- method card #408.

#408 Dynamic regression and regARIMA with exogenous regressors

Category 02-univariate-forecasting; module ``dynamic_regression``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

import numpy as np
import pandas as pd

from econflow_engine.generated.args.c02_univariate_forecasting import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "uf_dynamic_regression",
    "uf_dynamic_regression_forecast",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def uf_dynamic_regression(
    *,
    y: pd.Series,
    exog: np.ndarray,
    order: Sequence[int] | None = None,
    seasonal_order: Sequence[int] | None = None,
    season_length: int | None = None,
) -> dict[str, Any]:
    """Node ``uf_dynamic_regression`` -- method card #408.

    Dynamic regression and regARIMA with exogenous regressors.

    Category 02-univariate-forecasting; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Dependent series.
        exog: [exog_handle, required] Exogenous regressors.
        order: [int_array, optional] ARIMA order. Default ``[1, 0, 0]``.
        seasonal_order: [int_array, optional] Seasonal ARIMA order.
        season_length: [integer, optional] Seasonal period. Default ``1``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.

    Gates:
        None declared. The ``precondition_gates`` field of this method card is empty; the checks a
        body must run are named here once the field carries them.

    .. gen_wrappers: end of generated docstring

    Examples:
        None yet. This node raises ``NotImplementedError``; its example is written with its body and
        belongs to whoever writes it.

    Note:
        The implementation note is written with the body: the library functions it calls and their
        versions, what the method leaves out, and every gate added with the source that requires it.
    """
    raise NotImplementedError(
        "uf_dynamic_regression: not implemented."
    )


def uf_dynamic_regression_forecast(
    *,
    fit: Any,
    exog_future: np.ndarray,
    h: int,
    levels: Sequence[float] | None = None,
) -> dict[str, Any]:
    """Node ``uf_dynamic_regression_forecast`` -- method card #408.

    Dynamic regression and regARIMA with exogenous regressors.

    Category 02-univariate-forecasting; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a fitted model.
        exog_future: [exog_handle, required] Future regressor values.
        h: [integer, required] Forecast horizon.
        levels: [num_array, optional] Prediction interval levels. Default ``[0.8, 0.95]``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.

    Gates:
        None declared. The ``precondition_gates`` field of this method card is empty; the checks a
        body must run are named here once the field carries them.

    .. gen_wrappers: end of generated docstring

    Examples:
        None yet. This node raises ``NotImplementedError``; its example is written with its body and
        belongs to whoever writes it.

    Note:
        The implementation note is written with the body: the library functions it calls and their
        versions, what the method leaves out, and every gate added with the source that requires it.
    """
    raise NotImplementedError(
        "uf_dynamic_regression_forecast: not implemented."
    )
