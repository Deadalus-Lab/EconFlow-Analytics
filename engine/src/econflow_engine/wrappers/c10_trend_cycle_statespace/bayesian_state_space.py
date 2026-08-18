# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``bayesian_state_space`` -- METHOD-SELECTION card #60.

#60 Bayesian state space

Category 10-trend-cycle-statespace; module ``bayesian_state_space``.

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
    "bs_ar1_lg",
    "bs_bsm_lg",
    "bs_prior_spec",
    "bs_run_mcmc",
    "NODE_META",
    "wire_model",
]


def bs_prior_spec(
    *,
    distribution: Literal["halfnormal", "normal", "tnormal", "uniform", "gamma"] | None = None,
    init: float,
    sd: float | None = None,
    mean: float | None = None,
    min: float | None = None,
    max: float | None = None,
    shape: float | None = None,
    rate: float | None = None,
) -> dict[str, Any]:
    """Node ``bs_prior_spec`` -- METHOD-SELECTION card #60.

    Bayesian state space.

    Category 10-trend-cycle-statespace; memory class ``light``.

    Args:
        distribution: [enum, optional] Prior family (default halfnormal).
        init: [number, required] Initial parameter value (within the support of the distribution).
        sd: [number, optional] Standard deviation (halfnormal/normal/tnormal)· > 0.
        mean: [number, optional] Mean (normal/tnormal).
        min: [number, optional] Lower bound (uniform/tnormal).
        max: [number, optional] Upper bound (uniform/tnormal).
        shape: [number, optional] Shape parameter (gamma)· > 0.
        rate: [number, optional] Rate parameter (gamma)· > 0.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bs_prior_spec: not implemented. The method card is in ./README.md."
    )


def bs_bsm_lg(
    *,
    y: pd.Series,
    sd_y: Any,
    sd_level: Any,
    sd_slope: Any | None = None,
    sd_seasonal: Any | None = None,
    period: int | None = None,
) -> dict[str, Any]:
    """Node ``bs_bsm_lg`` -- METHOD-SELECTION card #60.

    Bayesian state space.

    Category 10-trend-cycle-statespace; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Handle to a univariate ts· basic structural (level + optional
            slope/seasonal).
        sd_y: [raw_handle, required] Handle to a prior (bs_prior_spec) for the obs standard
            deviation.
        sd_level: [raw_handle, required] Handle to a prior for the level standard deviation.
        sd_slope: [raw_handle, optional] Handle to a prior for the slope (None -> without a slope
            term).
        sd_seasonal: [raw_handle, optional] Handle to a prior for the seasonality (None -> without a
            seasonal term).
        period: [integer, optional] Seasonal period (>=2, < n)· required with sd_seasonal.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bs_bsm_lg: not implemented. The method card is in ./README.md."
    )


def bs_ar1_lg(
    *,
    y: pd.Series,
    rho: Any,
    sigma: Any,
    mu: Any,
    sd_y: Any,
) -> dict[str, Any]:
    """Node ``bs_ar1_lg`` -- METHOD-SELECTION card #60.

    Bayesian state space.

    Category 10-trend-cycle-statespace; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Handle to a univariate ts· stationary AR(1) latent cycle
            (Bayesian gap).
        rho: [raw_handle, required] Handle to a prior for the AR(1) rho (e.g. uniform ∈ (-1,1)).
        sigma: [raw_handle, required] Handle to a prior for the state standard deviation.
        mu: [raw_handle, required] Handle to a prior for the stationary mean (REQUIRED).
        sd_y: [raw_handle, required] Handle to a prior for the obs standard deviation.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bs_ar1_lg: not implemented. The method card is in ./README.md."
    )


def bs_run_mcmc(
    *,
    model: Any,
    iter: int,
    seed: int,
    burnin: int | None = None,
    thin: int | None = None,
    output_type: Literal["full", "summary", "theta"] | None = None,
) -> dict[str, Any]:
    """Node ``bs_run_mcmc`` -- METHOD-SELECTION card #60.

    Bayesian state space.

    Category 10-trend-cycle-statespace; memory class ``mcmc``.

    Args:
        model: [raw_handle, required] Handle to a lineargaussian model (from bs_bsm_lg/bs_ar1_lg).
        iter: [integer, required] Number of MCMC iterations.
        seed: [integer, required] Seed REQUIRED (determinism -- the bssm default is random).
        burnin: [integer, optional] Iterations burn-in ∈ [0, iter)· default floor(iter/2).
        thin: [integer, optional] Thinning interval (positive integer). Default ``1``.
        output_type: [enum, optional] full -> states+theta· summary· theta only (default full).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bs_run_mcmc: not implemented. The method card is in ./README.md."
    )
