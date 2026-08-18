# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``forecast`` -- METHOD-SELECTION card #7.

#7 forecast (ARIMA/ETS/Theta/TBATS)

Category 02-univariate-forecasting; module ``forecast``.

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
    "run_auto_arima",
    "run_ets",
    "run_tbats",
    "run_theta",
    "NODE_META",
    "wire_model",
]


def run_auto_arima(
    *,
    y: pd.Series,
    h: int | None = None,
    ic: Literal["aicc", "aic", "bic"] | None = None,
    stepwise: bool | None = None,
    seasonal: bool | None = None,
    exog: np.ndarray | None = None,
) -> dict[str, Any]:
    """Node ``run_auto_arima`` -- METHOD-SELECTION card #7.

    forecast (ARIMA/ETS/Theta/TBATS).

    Category 02-univariate-forecasting; memory class ``light``.

    Args:
        y: [series_handle, required] Handle to a univariate ts (the series to forecast).
        h: [integer, optional] Forecast horizon (number of steps; None -> documented default).
        ic: [enum, optional] Information criterion for the selection (default aicc).
        stepwise: [boolean, optional] Stepwise search (default True; False = exhaustive, slow).
        seasonal: [boolean, optional] Allow seasonal ARIMA terms (default True).
        exog: [exog_handle, optional] Handle to exogenous regressors (matrix, same rows as y; NOT a
            data frame).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "run_auto_arima: not implemented. The method card is in ./README.md."
    )


def run_ets(
    *,
    y: pd.Series,
    model: str | None = None,
    damped: bool | None = None,
    h: int | None = None,
    ic: Literal["aicc", "aic", "bic"] | None = None,
) -> dict[str, Any]:
    """Node ``run_ets`` -- METHOD-SELECTION card #7.

    forecast (ARIMA/ETS/Theta/TBATS).

    Category 02-univariate-forecasting; memory class ``light``.

    Args:
        y: [series_handle, required] Handle to a univariate ts.
        model: [string, optional] ETS spec, 3 letters E/T/S (default 'ZZZ' = automatic selection).
        damped: [boolean, optional] Damped trend (None -> auto; True/False forces it).
        h: [integer, optional] Forecast horizon.
        ic: [enum, optional] Information criterion (default aicc).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "run_ets: not implemented. The method card is in ./README.md."
    )


def run_theta(
    *,
    y: pd.Series,
    h: int | None = None,
) -> dict[str, Any]:
    """Node ``run_theta`` -- METHOD-SELECTION card #7.

    forecast (ARIMA/ETS/Theta/TBATS).

    Category 02-univariate-forecasting; memory class ``light``.

    Args:
        y: [series_handle, required] Handle to a univariate ts.
        h: [integer, optional] Forecast horizon.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "run_theta: not implemented. The method card is in ./README.md."
    )


def run_tbats(
    *,
    y: pd.Series,
    use_box_cox: bool | None = None,
    use_trend: bool | None = None,
    use_damped_trend: bool | None = None,
    use_arma_errors: bool | None = None,
    h: int | None = None,
) -> dict[str, Any]:
    """Node ``run_tbats`` -- METHOD-SELECTION card #7.

    forecast (ARIMA/ETS/Theta/TBATS).

    Category 02-univariate-forecasting; memory class ``light``.

    Args:
        y: [series_handle, required] Handle to a univariate ts (univariate only; multiple seasonal
            periods possible).
        use_box_cox: [boolean, optional] Box-Cox transformation (None -> auto).
        use_trend: [boolean, optional] Inclusion of trend (None -> auto).
        use_damped_trend: [boolean, optional] Damped trend (None -> auto).
        use_arma_errors: [boolean, optional] ARMA errors on the residuals (default True).
        h: [integer, optional] Forecast horizon.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "run_tbats: not implemented. The method card is in ./README.md."
    )
