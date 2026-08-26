# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``diebold_mariano_backtest`` -- method card #74.

#74 Diebold-Mariano test + rolling-origin backtest

Category 15-model-evaluation; module ``diebold_mariano_backtest``.

Reference implementation: dieboldmariano.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c15_model_evaluation import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "eval_dm_test",
    "eval_rolling_origin",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def eval_dm_test(
    *,
    e1: pd.Series,
    e2: pd.Series,
    alternative: Literal["two.sided", "less", "greater"] | None = None,
    h: int | None = None,
    power: float | None = None,
    varestimator: Literal["acf", "bartlett"] | None = None,
) -> dict[str, Any]:
    """Node ``eval_dm_test`` -- method card #74.

    Diebold-Mariano test + rolling-origin backtest.

    Category 15-model-evaluation; memory class ``light``.

    Args:
        e1: [series_handle, required] Handle to the forecast error series of method 1 (e1).
        e2: [series_handle, required] Handle to the forecast error series of method 2 (e2, same
            length).
        alternative: [enum, optional] Alternative hypothesis (default two.sided· less => e1 is more
            accurate).
        h: [integer, optional] Forecast horizon of the errors (positive integer < length, default
            1). Default ``1``.
        power: [number, optional] Loss power (2 = squared error, 1 = absolute error· default 2).
            Default ``2``.
        varestimator: [enum, optional] Long-run variance estimator (default acf).

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
        "eval_dm_test: not implemented."
    )


def eval_rolling_origin(
    *,
    y: pd.Series,
    forecastfunction: (
        Literal[
            "naive",
            "snaive",
            "drift",
            "mean",
            "ses",
            "holt",
            "ets",
            "auto_arima",
            "theta",
        ]
    ),
    h: int | None = None,
    window: int | None = None,
    initial: int | None = None,
) -> dict[str, Any]:
    """Node ``eval_rolling_origin`` -- method card #74.

    Diebold-Mariano test + rolling-origin backtest.

    Category 15-model-evaluation; memory class ``light``.

    Args:
        y: [series_handle, required] Handle to the time series for the rolling-origin backtest.
        forecastfunction: [forecastfn_enum, required] The model/pipeline that is backtested:
            rolling-origin cross-validation of ONE forecasting function with signature function(y,
            h) that returns a forecast object (card 74). Given ONLY as a name from a closed
            allowlist, never as executable code. Options: naive = Naive / random walk: f(t+k)=y(T).
            The classic benchmark (FPP3). · seasonal-naive = Seasonal naive: f(t+k)=y(T+k-m).
            Benchmark for seasonal series; at frequency=1 it degenerates IDENTICALLY to naive
            (lag=1). · drift = Random walk with drift: naive + mean historical change (FPP3
            benchmark). · mean = Mean forecast: f(t+k)=mean(y). Benchmark; bootstrap=True (5000
            stochastic paths) is PINNED to False for determinism. · ses = Simple exponential
            smoothing = ETS(A,N,N) (without trend/seasonality). · holt = Holt linear trend =
            ETS(A,A,N) (linear trend, without seasonality). · ets = Automatic ETS state-space
            (error/trend/season selection with AICc); same method as the run_ets node (cat. 02). ·
            auto_arima = Automatic (S)ARIMA with stepwise Hyndman-Khandakar; same method as the
            run_auto_arima node (cat. 02). · theta = Theta method (Assimakopoulos & Nikolopoulos
            2000, M3 winner); same family as the run_theta node (cat. 02). Caution: tsCV re-fits at
            EVERY origin -> ets/auto_arima are significantly slower than the benchmarks.
        h: [integer, optional] Forecast horizon per origin (positive integer, default 1). Default
            ``1``.
        window: [integer, optional] Rolling window length (None = expanding· positive integer).
        initial: [integer, optional] Observations omitted from the start (>= 0, default 0). Default
            ``0``.

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
        "eval_rolling_origin: not implemented."
    )
