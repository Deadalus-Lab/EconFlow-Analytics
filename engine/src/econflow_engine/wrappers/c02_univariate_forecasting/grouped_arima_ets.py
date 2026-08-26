# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``grouped_arima_ets`` -- method card #8.

#8 Tidy ARIMA and ETS forecasting over grouped series

Category 02-univariate-forecasting; module ``grouped_arima_ets``.

Reference implementation: statsforecast.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c02_univariate_forecasting import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "run_grouped_arima",
    "run_grouped_ets",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def run_grouped_arima(
    *,
    data: pd.DataFrame,
    formula: str,
    ic: Literal["aicc", "aic", "bic"] | None = None,
    stepwise: bool | None = None,
    h: int | None = None,
) -> dict[str, Any]:
    """Node ``run_grouped_arima`` -- method card #8.

    Tidy ARIMA and ETS forecasting over grouped series.

    Category 02-univariate-forecasting; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a series (index + value variable).
        formula: [formula, required] Model spec, e.g. 'value ~ 1' (automatic order selection). NOTE:
            the special order functions pdq/PDQ are NOT allowed by the security allowlist.
        ic: [enum, optional] Information criterion (default aicc).
        stepwise: [boolean, optional] Stepwise search (default True).
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
        "run_grouped_arima: not implemented."
    )


def run_grouped_ets(
    *,
    data: pd.DataFrame,
    formula: str,
    opt_crit: Literal["lik", "amse", "mse", "sigma", "mae"] | None = None,
    ic: Literal["aicc", "aic", "bic"] | None = None,
    h: int | None = None,
) -> dict[str, Any]:
    """Node ``run_grouped_ets`` -- method card #8.

    Tidy ARIMA and ETS forecasting over grouped series.

    Category 02-univariate-forecasting; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a series (WITHOUT missing values — ETS does not
            support them).
        formula: [formula, required] ETS model spec; NOTE: the order functions error/trend/season
            are NOT allowed by the security allowlist.
        opt_crit: [enum, optional] Optimization criterion (default lik).
        ic: [enum, optional] Information criterion (default aicc).
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
        "run_grouped_ets: not implemented."
    )
