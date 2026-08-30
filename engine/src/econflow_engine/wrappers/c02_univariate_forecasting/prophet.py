# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``prophet`` -- method card #9.

#9 Additive/logistic-trend forecasting with holidays and multiple seasonalities (Prophet)

Category 02-univariate-forecasting; module ``prophet``.

Reference implementation: prophet.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c02_univariate_forecasting import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "run_prophet",
    "run_prophet_cv",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def run_prophet(
    *,
    df: pd.DataFrame,
    growth: Literal["linear", "logistic", "flat"] | None = None,
    seasonality_mode: Literal["additive", "multiplicative"] | None = None,
    date_col: str | None = None,
    value_col: str | None = None,
    periods: int | None = None,
    freq: str | None = None,
) -> dict[str, Any]:
    """Node ``run_prophet`` -- method card #9.

    Additive/logistic-trend forecasting with holidays and multiple seasonalities (Prophet).

    Category 02-univariate-forecasting; memory class ``heavy``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        df: [df_handle, required] Handle to a DataFrame; either ds/y or long-format
            (date_col/value_col).
        growth: [enum, optional] Trend growth (default linear; 'logistic' requires a cap column).
        seasonality_mode: [enum, optional] Seasonality mode (default additive).
        date_col: [string, optional] Date column name for mapping to ds (default 'period').
        value_col: [string, optional] Value column name for mapping to y (default 'value').
        periods: [integer, optional] Forecast horizon (future steps; default 0).
        freq: [string, optional] Frequency of future dates (e.g. 'month'; None -> auto-infer).

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
        "run_prophet: not implemented."
    )


def run_prophet_cv(
    *,
    model: Any,
    horizon: int,
    units: str,
    period: int | None = None,
    initial: int | None = None,
    rolling_window: float | None = None,
) -> dict[str, Any]:
    """Node ``run_prophet_cv`` -- method card #9.

    Additive/logistic-trend forecasting with holidays and multiple seasonalities (Prophet).

    Category 02-univariate-forecasting; memory class ``heavy``.

    Args:
        model: [raw_handle, required] Handle to a fitted prophet model (from run_prophet).
        horizon: [integer, required] Horizon of each fold (in 'units').
        units: [string, required] Time unit (e.g. 'days', 'weeks').
        period: [integer, optional] Cutoff spacing (units; None -> 0.5*horizon).
        initial: [integer, optional] Initial training window (units; None -> 3*horizon).
        rolling_window: [number, optional] Aggregation window of the performance metrics (default
            0.1).

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
        "run_prophet_cv: not implemented."
    )
