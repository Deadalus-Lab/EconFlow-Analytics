# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``classical_univariate_forecasting`` -- method card #7.

#7 Classical univariate forecasting: ARIMA, ETS, Theta and TBATS

Category 02-univariate-forecasting; module ``classical_univariate_forecasting``.

Reference implementation: statsforecast.

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
    "run_auto_arima",
    "run_ets",
    "run_tbats",
    "run_theta",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def run_auto_arima(
    *,
    y: pd.Series,
    h: int | None = None,
    ic: Literal["aicc", "aic", "bic"] | None = None,
    stepwise: bool | None = None,
    seasonal: bool | None = None,
    exog: np.ndarray | None = None,
) -> dict[str, Any]:
    """Node ``run_auto_arima`` -- method card #7.

    Classical univariate forecasting: ARIMA, ETS, Theta and TBATS.

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
        "run_auto_arima: not implemented."
    )


def run_ets(
    *,
    y: pd.Series,
    model: str | None = None,
    damped: bool | None = None,
    h: int | None = None,
    ic: Literal["aicc", "aic", "bic"] | None = None,
) -> dict[str, Any]:
    """Node ``run_ets`` -- method card #7.

    Classical univariate forecasting: ARIMA, ETS, Theta and TBATS.

    Category 02-univariate-forecasting; memory class ``light``.

    Args:
        y: [series_handle, required] Handle to a univariate ts.
        model: [string, optional] ETS spec, 3 letters E/T/S (default 'ZZZ' = automatic selection).
        damped: [boolean, optional] Damped trend (None -> auto; True/False forces it).
        h: [integer, optional] Forecast horizon.
        ic: [enum, optional] Information criterion (default aicc).

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
        "run_ets: not implemented."
    )


def run_theta(
    *,
    y: pd.Series,
    h: int | None = None,
) -> dict[str, Any]:
    """Node ``run_theta`` -- method card #7.

    Classical univariate forecasting: ARIMA, ETS, Theta and TBATS.

    Category 02-univariate-forecasting; memory class ``light``.

    Args:
        y: [series_handle, required] Handle to a univariate ts.
        h: [integer, optional] Forecast horizon.

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
        "run_theta: not implemented."
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
    """Node ``run_tbats`` -- method card #7.

    Classical univariate forecasting: ARIMA, ETS, Theta and TBATS.

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
        "run_tbats: not implemented."
    )
