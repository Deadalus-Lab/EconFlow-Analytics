# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``bayesian_time_varying`` -- METHOD-SELECTION card #183.

#183 Bayesian time-varying-parameter (TVP) regression with global-local shrinkage
    (triple/double/ridge) + SV

Category 10-trend-cycle-statespace; module ``bayesian_time_varying``.

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
    "stvp_fit",
    "stvp_forecast",
    "stvp_lpds",
    "NODE_META",
    "wire_model",
]


def stvp_fit(
    *,
    formula: str,
    data: pd.DataFrame,
    mod_type: Literal["triple", "double", "ridge"] | None = None,
    sv: bool | None = None,
    niter: int | None = None,
    nburn: int | None = None,
    nthin: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``stvp_fit`` -- METHOD-SELECTION card #183.

    Bayesian time-varying-parameter (TVP) regression with global-local shrinkage
    (triple/double/ridge) + SV.

    Category 10-trend-cycle-statespace; memory class ``mcmc``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        formula: [formula, required] Regression formula, e.g. 'y ~ x1 + x2' (Intercept is added
            automatically, as TVP).
        data: [df_handle, required] Handle to a DataFrame· ALL the formula variables numeric,
            without NA.
        mod_type: [enum, optional] Shrinkage prior: triple (default, triple gamma) / double (NG
            horseshoe-like) / ridge (without shrinkage).
        sv: [boolean, optional] Stochastic volatility in the observation variance (sigma2 ->
            time-varying path). Default ``False``.
        niter: [integer, optional] Number of MCMC iterations (>=2)· keep SMALL. Default ``2000``.
        nburn: [integer, optional] Burn-in draws (0 <= nburn < niter)· None -> round(niter/2).
        nthin: [integer, optional] Thinning (>=1)· (niter-nburn) must be >= nthin. Default ``1``.
        seed: [integer, optional] RNG seed (required for reproducibility in a stateless node).
            Default ``2025``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "stvp_fit: not implemented. The method card is in ./README.md."
    )


def stvp_forecast(
    *,
    object: Any,
    newdata: pd.DataFrame,
    n_ahead: int | None = None,
) -> dict[str, Any]:
    """Node ``stvp_forecast`` -- METHOD-SELECTION card #183.

    Bayesian time-varying-parameter (TVP) regression with global-local shrinkage
    (triple/double/ridge) + SV.

    Category 10-trend-cycle-statespace; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a fitted 'shrinkTVP' model (from stvp_fit).
        newdata: [df_handle, required] DataFrame with the RHS covariates for the horizons (numeric,
            without NA)· nrow >= n.ahead.
        n_ahead: [integer, optional] Forecast horizon (integer >=1). Default ``1``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "stvp_forecast: not implemented. The method card is in ./README.md."
    )


def stvp_lpds(
    *,
    object: Any,
    data_test: pd.DataFrame,
) -> dict[str, Any]:
    """Node ``stvp_lpds`` -- METHOD-SELECTION card #183.

    Bayesian time-varying-parameter (TVP) regression with global-local shrinkage
    (triple/double/ridge) + SV.

    Category 10-trend-cycle-statespace; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a fitted 'shrinkTVP' model (from stvp_fit).
        data_test: [df_handle, required] DataFrame with EXACTLY one hold-out row (dependent +
            covariates, numeric).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "stvp_lpds: not implemented. The method card is in ./README.md."
    )
