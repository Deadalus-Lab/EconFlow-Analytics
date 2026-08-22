# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``time_varying_parameter`` -- method card #146.

#146 Time-Varying-Parameter VAR with stochastic volatility + dynamic global-local shrinkage
    (triple/double gamma or ridge)

Category 03-multivariate-nowcasting; module ``time_varying_parameter``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c03_multivariate_nowcasting import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "stv_estimate",
    "stv_forecast",
    "stv_tvp",
    "NODE_META",
    "wire_model",
]


def stv_estimate(
    *,
    y: pd.DataFrame,
    p: int | None = None,
    mod_type: Literal["double", "triple", "ridge"] | None = None,
    const: bool | None = None,
    niter: int | None = None,
    nburn: int | None = None,
    nthin: int | None = None,
    seed: int,
    ess_min: float | None = None,
    min_draws: int | None = None,
    allow_nonconvergence: bool | None = None,
) -> dict[str, Any]:
    """Node ``stv_estimate`` -- method card #146.

    Time-Varying-Parameter VAR with stochastic volatility + dynamic global-local shrinkage
    (triple/double gamma or ridge).

    Category 03-multivariate-nowcasting; memory class ``mcmc``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        y: [multiseries_handle, required] Handle to a multivariate series (panel, T x k, k>=2, no
            NA/Inf, nrow>p+1).
        p: [integer, optional] VAR lag order (positive integer, default 1). Default ``1``.
        mod_type: [enum, optional] Prior shrinkage: double gamma (default) / triple gamma / ridge.
        const: [boolean, optional] Include a time-varying intercept (default True). Default
            ``True``.
        niter: [integer, optional] MCMC iterations including burn-in (positive integer, default
            200). Default ``200``.
        nburn: [integer, optional] Burn-in draws (non-negative, <= niter-2, default 100). Default
            ``100``.
        nthin: [integer, optional] Thinning: every nthin-th draw is kept (default 1). Default ``1``.
        seed: [integer, required] MANDATORY seed (integer) — MCMC· seeded before sampling.
        ess_min: [number, optional] Minimum acceptable min-ESS (convergence gate· production >=200).
            Default ``10``.
        min_draws: [integer, optional] Minimum retained draws for the convergence assessment
            (default 20). Default ``20``.
        allow_nonconvergence: [boolean, optional] If True, return a non-converged result
            (converged=False) instead of stop. Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "stv_estimate: not implemented."
    )


def stv_forecast(
    *,
    model: Any,
    n_ahead: int | None = None,
    probs: Sequence[float] | None = None,
) -> dict[str, Any]:
    """Node ``stv_forecast`` -- method card #146.

    Time-Varying-Parameter VAR with stochastic volatility + dynamic global-local shrinkage
    (triple/double gamma or ridge).

    Category 03-multivariate-nowcasting; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a 'shrinkTVPVAR' model (from stv_estimate).
        n_ahead: [integer, optional] Posterior predictive horizon (positive integer, default 1).
            Default ``1``.
        probs: [num_array, optional] Quantiles ∈ (0,1) for the fan grid (default
            0.05/0.25/0.5/0.75/0.95).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "stv_forecast: not implemented."
    )


def stv_tvp(
    *,
    model: Any,
    equation: int | None = None,
    probs: Sequence[float] | None = None,
    include_intercept: bool | None = None,
) -> dict[str, Any]:
    """Node ``stv_tvp`` -- method card #146.

    Time-Varying-Parameter VAR with stochastic volatility + dynamic global-local shrinkage
    (triple/double gamma or ridge).

    Category 03-multivariate-nowcasting; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a 'shrinkTVPVAR' model (from stv_estimate).
        equation: [integer, optional] Equation/variable index 1..m for extracting coefficient paths
            (default 1). Default ``1``.
        probs: [num_array, optional] Quantiles ∈ (0,1) for the posterior bands over time (default
            0.05/0.5/0.95).
        include_intercept: [boolean, optional] Include the time-varying intercept path (if const,
            default True). Default ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "stv_tvp: not implemented."
    )
