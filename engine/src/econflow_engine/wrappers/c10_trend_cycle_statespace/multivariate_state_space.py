# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``multivariate_state_space`` -- METHOD-SELECTION card #61.

#61 Multivariate state space (output gap / NAIRU / DFA)

Category 10-trend-cycle-statespace; module ``multivariate_state_space``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c10_trend_cycle_statespace import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "marss_dfa",
    "marss_forecast",
    "marss_glance",
    "marss_param_cis",
    "marss_prepare_data",
    "NODE_META",
    "wire_model",
]


def marss_prepare_data(
    *,
    df: pd.DataFrame,
    series_col: str | None = None,
    standardize: bool | None = None,
) -> dict[str, Any]:
    """Node ``marss_prepare_data`` -- METHOD-SELECTION card #61.

    Multivariate state space (output gap / NAIRU / DFA).

    Category 10-trend-cycle-statespace; memory class ``light``.

    Args:
        df: [df_handle, required] Handle to a long DataFrame (series/period/value)· owns the
            transpose.
        series_col: [string, optional] Series identifier column· None -> auto
            (series_code/series_name/series).
        standardize: [boolean, optional] z-score per series (recommended for DFA). Default
            ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "marss_prepare_data: not implemented. The method card is in ./README.md."
    )


def marss_dfa(
    *,
    data: Any,
    m: int | None = None,
    method: Literal["kem", "BFGS"] | None = None,
    maxit: int | None = None,
    allow_nonconvergence: bool | None = None,
) -> dict[str, Any]:
    """Node ``marss_dfa`` -- METHOD-SELECTION card #61.

    Multivariate state space (output gap / NAIRU / DFA).

    Category 10-trend-cycle-statespace; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        data: [raw_handle, required] Handle to a marss_prepare_data result (n x T matrix).
        m: [integer, optional] Number of common latent factors (<= n). Default ``1``.
        method: [enum, optional] Optimizer (default kem EM).
        maxit: [integer, optional] Maximum iterations. Default ``5000``.
        allow_nonconvergence: [boolean, optional] If True, allows a non-converged result (default
            False = hard gate). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "marss_dfa: not implemented. The method card is in ./README.md."
    )


def marss_param_cis(
    *,
    object: Any,
    method: Literal["hessian", "parametric", "innovations"] | None = None,
    alpha: float | None = None,
    nboot: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``marss_param_cis`` -- METHOD-SELECTION card #61.

    Multivariate state space (output gap / NAIRU / DFA).

    Category 10-trend-cycle-statespace; memory class ``heavy``.

    Args:
        object: [raw_handle, required] Handle to a fitted marssMLE (from marss_dfa).
        method: [enum, optional] hessian (default, deterministic)· parametric/innovations = seeded
            bootstrap.
        alpha: [number, optional] Significance level ∈ (0,1). Default ``0.05``.
        nboot: [integer, optional] Bootstrap replications (only parametric/innovations). Default
            ``1000``.
        seed: [integer, optional] Seed REQUIRED for parametric/innovations bootstrap (determinism).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "marss_param_cis: not implemented. The method card is in ./README.md."
    )


def marss_forecast(
    *,
    object: Any,
    n_ahead: int | None = None,
    level: float | None = None,
    type: Literal["ytT", "ytt1", "ytt", "xtT", "xtt1"] | None = None,
    interval: Literal["prediction", "confidence", "none"] | None = None,
) -> dict[str, Any]:
    """Node ``marss_forecast`` -- METHOD-SELECTION card #61.

    Multivariate state space (output gap / NAIRU / DFA).

    Category 10-trend-cycle-statespace; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a fitted marssMLE (from marss_dfa).
        n_ahead: [integer, optional] Forecast horizon (0 = only in-sample fitted). Default ``0``.
        level: [number, optional] Confidence level ∈ (0,1). Default ``0.95``.
        type: [enum, optional] Requested quantity (default ytT = smoothed observations).
        interval: [enum, optional] Interval type (default prediction).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "marss_forecast: not implemented. The method card is in ./README.md."
    )


def marss_glance(
    *,
    object: Any,
    tidy: bool | None = None,
) -> dict[str, Any]:
    """Node ``marss_glance`` -- METHOD-SELECTION card #61.

    Multivariate state space (output gap / NAIRU / DFA).

    Category 10-trend-cycle-statespace; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a fitted marssMLE (from marss_dfa).
        tidy: [boolean, optional] If True, adds a tidy parameter table. Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "marss_glance: not implemented. The method card is in ./README.md."
    )
