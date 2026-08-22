# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``hierarchical_global_local`` -- method card #143.

#143 Hierarchical global-local shrinkage Bayesian VAR + stochastic volatility (HS/DL/R2D2/NG/SSVS
    priors, posterior fan charts + LPL)

Category 03-multivariate-nowcasting; module ``hierarchical_global_local``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c03_multivariate_nowcasting import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "bvs_estimate",
    "bvs_irf",
    "bvs_predict",
    "NODE_META",
    "wire_model",
]


def bvs_estimate(
    *,
    data: np.ndarray,
    lags: int | None = None,
    prior: Literal["HS", "DL", "R2D2", "NG", "SSVS", "normal"] | None = None,
    draws: int | None = None,
    burnin: int | None = None,
    thin: int | None = None,
    sv_keep: Literal["last", "all"] | None = None,
    seed: int,
    min_draws: int | None = None,
    ess_min: float | None = None,
    allow_nonconvergence: bool | None = None,
) -> dict[str, Any]:
    """Node ``bvs_estimate`` -- method card #143.

    Hierarchical global-local shrinkage Bayesian VAR + stochastic volatility (HS/DL/R2D2/NG/SSVS
    priors, posterior fan charts + LPL).

    Category 03-multivariate-nowcasting; memory class ``mcmc``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        data: [matrix_handle, required] Handle to a numeric matrix with >=2 columns (multivariate
            VAR)· no NA/Inf· nrow>lags+1.
        lags: [integer, optional] VAR order (positive integer· default 1). Default ``1``.
        prior: [enum, optional] Global-local shrinkage prior on Phi (default HS = Horseshoe)·
            specify_prior_phi.
        draws: [integer, optional] Retained posterior draws (positive integer· TINY default 200).
            Default ``200``.
        burnin: [integer, optional] Burn-in draws (non-negative integer· default 100). Default
            ``100``.
        thin: [integer, optional] Thinning factor (positive integer <= draws· default 1). Default
            ``1``.
        sv_keep: [enum, optional] Which log-variance draws to keep (default last).
        seed: [integer, required] MANDATORY seed (seeded before the MCMC· cache key· bvar is
            stochastic).
        min_draws: [integer, optional] Minimum retained draws for convergence (non-negative· default
            100). Default ``100``.
        ess_min: [number, optional] Minimum effective sample size of Phi (positive· default 1).
            Default ``1``.
        allow_nonconvergence: [boolean, optional] True = return the posterior with converged=False
            instead of stop when the gate fires . Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bvs_estimate: not implemented."
    )


def bvs_predict(
    *,
    model: Any,
    ahead: int | None = None,
    stable: bool | None = None,
    quantiles: Sequence[float] | None = None,
    LPL: bool | None = None,
    Y_obs: np.ndarray | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``bvs_predict`` -- method card #143.

    Hierarchical global-local shrinkage Bayesian VAR + stochastic volatility (HS/DL/R2D2/NG/SSVS
    priors, posterior fan charts + LPL).

    Category 03-multivariate-nowcasting; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a 'bayesianVARs_bvar' model (bvs_estimate.model).
        ahead: [integer, optional] Forecast horizon· horizons 1..ahead (positive integer· default
            4). Default ``4``.
        stable: [boolean, optional] Discard non-stable draws before forecasting (stable_bvar·
            default True). Default ``True``.
        quantiles: [num_array, optional] Quantiles of the predictive fan chart ∈ (0,1) (default
            0.05/0.25/0.5/0.75/0.95).
        LPL: [boolean, optional] True = compute the log predictive likelihood (requires Y_obs).
            Default ``False``.
        Y_obs: [matrix_handle, optional] Realised values [ahead x M] for LPL (only when LPL=True).
        seed: [integer, required] MANDATORY seed (predict is stochastic· simulate_predictive).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bvs_predict: not implemented."
    )


def bvs_irf(
    *,
    model: Any,
    ahead: int | None = None,
    quantiles: Sequence[float] | None = None,
) -> dict[str, Any]:
    """Node ``bvs_irf`` -- method card #143.

    Hierarchical global-local shrinkage Bayesian VAR + stochastic volatility (HS/DL/R2D2/NG/SSVS
    priors, posterior fan charts + LPL).

    Category 03-multivariate-nowcasting; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a 'bayesianVARs_bvar' model (bvs_estimate.model).
        ahead: [integer, optional] Impulse response horizon 0..ahead (positive integer· default 8).
            Default ``8``.
        quantiles: [num_array, optional] Quantile bands of the IRF ∈ (0,1) (default 0.05/0.5/0.95).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bvs_irf: not implemented."
    )
