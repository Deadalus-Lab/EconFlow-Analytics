# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``bayesian_structural_var_sign_zero`` -- method card #149.

#149 Bayesian Structural VAR with SIGN + ZERO + NARRATIVE restrictions (set-identified, importance
    sampling; a Waggoner-Zha Gibbs sampler + a uniform rotation Q)

Category 04-structural-shocks; module ``bayesian_structural_var_sign_zero``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c04_structural_shocks import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "bss_estimate",
    "bss_fevd",
    "bss_forecast",
    "bss_irf",
    "NODE_META",
    "wire_model",
]


def bss_estimate(
    *,
    data: pd.DataFrame,
    p: int | None = None,
    sign_irf: np.ndarray | None = None,
    sign_structural: np.ndarray | None = None,
    S: int | None = None,
    thin: int | None = None,
    max_tries: int | None = None,
    ess_min_ratio: float | None = None,
    allow_nonconvergence: bool | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``bss_estimate`` -- method card #149.

    Bayesian Structural VAR with SIGN + ZERO + NARRATIVE restrictions (set-identified, importance
    sampling; a Waggoner-Zha Gibbs sampler + a uniform rotation Q).

    Category 04-structural-shocks; memory class ``mcmc``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        data: [multiseries_handle, required] Handle to a multivariate series (matrix/series/panel,
            (T+p) x N, N>=2, no NA/Inf).
        p: [integer, optional] VAR lag order (positive integer, default 1). Default ``1``.
        sign_irf: [matrix_handle, optional] NxN (horizon-0) matrix restrictions on the IRF: 1/-1
            sign, 0 ZERO restriction, NA unrestricted. (For an NxNxH array see the L1 wrapper.)
        sign_structural: [matrix_handle, optional] NxN matrix {-1,1,NA} — sign restrictions on the
            contemporaneous relation B (BE=U).
        S: [integer, optional] Number of posterior draws (positive integer· default 100 — TINY·
            production raises it). Default ``100``.
        thin: [integer, optional] MCMC thinning frequency (positive integer, default 1). Default
            ``1``.
        max_tries: [integer, optional] Maximum attempts to find a valid rotation Q per iteration
            (finite -> prevents a hang on infeasible restrictions· L1 default Inf). Default
            ``10000``.
        ess_min_ratio: [number, optional] Degeneracy threshold for the importance weights:
            ess/n_draws < this -> STOP (unreliable posterior). In (0,1], default 0.01. Default
            ``0.01``.
        allow_nonconvergence: [boolean, optional] True -> return with converged=False instead of
            STOP on degenerate weights (default False). Default ``False``.
        seed: [integer, required] MANDATORY seed (integer) — the Gibbs sampler is stochastic· seeded
            beforehand.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bss_estimate: not implemented."
    )


def bss_irf(
    *,
    model: Any,
    horizon: int | None = None,
    standardise: bool | None = None,
    lower_q: float | None = None,
    upper_q: float | None = None,
) -> dict[str, Any]:
    """Node ``bss_irf`` -- method card #149.

    Bayesian Structural VAR with SIGN + ZERO + NARRATIVE restrictions (set-identified, importance
    sampling; a Waggoner-Zha Gibbs sampler + a uniform rotation Q).

    Category 04-structural-shocks; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a posterior 'PosteriorBSVARSIGN' (from
            bss_estimate).
        horizon: [integer, optional] IRF horizon (positive integer, default 8). Default ``8``.
        standardise: [boolean, optional] True -> standardise so that the own-shock response at
            horizon 0 = 1 (default False). Default ``False``.
        lower_q: [number, optional] Lower quantile of the credible band in (0,1), < upper_q (default
            0.16). Default ``0.16``.
        upper_q: [number, optional] Upper quantile of the credible band in (0,1), > lower_q (default
            0.84). Default ``0.84``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bss_irf: not implemented."
    )


def bss_fevd(
    *,
    model: Any,
    horizon: int | None = None,
    lower_q: float | None = None,
    upper_q: float | None = None,
) -> dict[str, Any]:
    """Node ``bss_fevd`` -- method card #149.

    Bayesian Structural VAR with SIGN + ZERO + NARRATIVE restrictions (set-identified, importance
    sampling; a Waggoner-Zha Gibbs sampler + a uniform rotation Q).

    Category 04-structural-shocks; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a posterior 'PosteriorBSVARSIGN' (from
            bss_estimate).
        horizon: [integer, optional] FEVD horizon (positive integer, default 8). Default ``8``.
        lower_q: [number, optional] Lower quantile of the credible band in (0,1), < upper_q (default
            0.16). Default ``0.16``.
        upper_q: [number, optional] Upper quantile of the credible band in (0,1), > lower_q (default
            0.84). Default ``0.84``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bss_fevd: not implemented."
    )


def bss_forecast(
    *,
    model: Any,
    horizon: int | None = None,
    conditional_forecast: np.ndarray | None = None,
    exogenous_forecast: np.ndarray | None = None,
    lower_q: float | None = None,
    upper_q: float | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``bss_forecast`` -- method card #149.

    Bayesian Structural VAR with SIGN + ZERO + NARRATIVE restrictions (set-identified, importance
    sampling; a Waggoner-Zha Gibbs sampler + a uniform rotation Q).

    Category 04-structural-shocks; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a posterior 'PosteriorBSVARSIGN' (from
            bss_estimate).
        horizon: [integer, optional] Forecast horizon (positive integer, default 4). Default ``4``.
        conditional_forecast: [matrix_handle, optional] horizon x N matrix with numeric/NA —
            conditional forecast on the non-NA future values.
        exogenous_forecast: [matrix_handle, optional] horizon x d matrix of forecast exogenous
            variables (only if the model has exogenous).
        lower_q: [number, optional] Lower quantile of the predictive band in (0,1), < upper_q
            (default 0.16). Default ``0.16``.
        upper_q: [number, optional] Upper quantile of the predictive band in (0,1), > lower_q
            (default 0.84). Default ``0.84``.
        seed: [integer, required] MANDATORY seed (integer) — the predictive-density sampling is
            stochastic· seeded beforehand.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bss_forecast: not implemented."
    )
