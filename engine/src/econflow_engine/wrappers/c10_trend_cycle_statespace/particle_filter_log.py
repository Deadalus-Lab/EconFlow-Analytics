# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``particle_filter_log`` -- METHOD-SELECTION card #185.

#185 Particle-filter (bootstrap) log-likelihood + iterated filtering (IF2) MLE for non-linear
    non-Gaussian state-space models

Category 10-trend-cycle-statespace; module ``particle_filter_log``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

from econflow_engine.generated.args.c10_trend_cycle_statespace import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "pomp_mif2",
    "pomp_pfilter",
    "NODE_META",
    "wire_model",
]


def pomp_pfilter(
    *,
    model: Literal["gompertz", "ricker", "ou2"] | None = None,
    params: Any | None = None,
    Np: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``pomp_pfilter`` -- METHOD-SELECTION card #185.

    Particle-filter (bootstrap) log-likelihood + iterated filtering (IF2) MLE for non-linear
    non-Gaussian state-space models.

    Category 10-trend-cycle-statespace; memory class ``light``.

    Args:
        model: [enum, optional] Built-in pomp template (gompertz=stochastic Gompertz· ricker=Ricker
            map· ou2=bivariate OU). ONLY built-in — no user C-code. Default ``'gompertz'``.
        params: [raw, optional] Optional named list/vector override of the template parameters (e.g.
            list(r=0.15)). Unknown names -> gate error.
        Np: [integer, optional] Number of particles (positive integer)· larger = more accurate
            loglik, heavier compute. Default ``500``.
        seed: [integer, optional] Seed for the stochastic particle filter (reproducibility). Default
            ``2025``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "pomp_pfilter: not implemented. The method card is in ./README.md."
    )


def pomp_mif2(
    *,
    model: Literal["gompertz", "ricker", "ou2"] | None = None,
    params: Any | None = None,
    estimate: Any | None = None,
    Nmif: int | None = None,
    Np: int | None = None,
    cooling_fraction_50: float | None = None,
    rw_sd_value: float | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``pomp_mif2`` -- METHOD-SELECTION card #185.

    Particle-filter (bootstrap) log-likelihood + iterated filtering (IF2) MLE for non-linear
    non-Gaussian state-space models.

    Category 10-trend-cycle-statespace; memory class ``light``.

    Args:
        model: [enum, optional] Built-in pomp template (same as pomp_pfilter). ONLY built-in — no
            user C-code. Default ``'gompertz'``.
        params: [raw, optional] Optional named list/vector of initial parameter values (starting
            point of IF2). Unknown names -> gate error.
        estimate: [raw, optional] Character vector of parameter names to estimate (rw.sd
            perturbation)· None -> the dynamic parameters of the template (the initial-value …_0 are
            excluded).
        Nmif: [integer, optional] Number of IF2 iterations (positive integer)· more = better MLE
            convergence. Default ``10``.
        Np: [integer, optional] Number of particles per IF2 iteration (positive integer). Default
            ``500``.
        cooling_fraction_50: [number, optional] Reduction fraction of rw.sd over the first 50
            iterations, in (0,1] (cooling schedule). Default ``0.5``.
        rw_sd_value: [number, optional] Random-walk perturbation standard deviation (>0), common to
            all the estimate parameters. Default ``0.02``.
        seed: [integer, optional] Seed for the stochastic IF2 perturbations (reproducibility).
            Default ``2025``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "pomp_mif2: not implemented. The method card is in ./README.md."
    )
