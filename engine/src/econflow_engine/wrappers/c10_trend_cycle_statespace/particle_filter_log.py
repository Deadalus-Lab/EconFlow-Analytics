# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``particle_filter_log`` -- method card #185.

#185 Particle-filter (bootstrap) log-likelihood + iterated filtering (IF2) MLE for non-linear
    non-Gaussian state-space models

Category 10-trend-cycle-statespace; module ``particle_filter_log``.

Reference implementation: particles.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

from econflow_engine.generated.args.c10_trend_cycle_statespace import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "pf_iterated_filtering",
    "pf_loglik",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def pf_loglik(
    *,
    model: Literal["gompertz", "ricker", "ou2"] | None = None,
    params: Any | None = None,
    Np: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``pf_loglik`` -- method card #185.

    Particle-filter (bootstrap) log-likelihood + iterated filtering (IF2) MLE for non-linear
    non-Gaussian state-space models.

    Category 10-trend-cycle-statespace; memory class ``light``.

    Args:
        model: [enum, optional] Built-in POMP template (gompertz=stochastic Gompertz· ricker=Ricker
            map· ou2=bivariate OU). ONLY built-in — no user C-code. Default ``'gompertz'``.
        params: [raw, optional] Optional named list/vector override of the template parameters (e.g.
            list(r=0.15)). Unknown names -> gate error.
        Np: [integer, optional] Number of particles (positive integer)· larger = more accurate
            loglik, heavier compute. Default ``500``.
        seed: [integer, optional] Seed for the stochastic particle filter (reproducibility). Default
            ``2025``.

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
        "pf_loglik: not implemented."
    )


def pf_iterated_filtering(
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
    """Node ``pf_iterated_filtering`` -- method card #185.

    Particle-filter (bootstrap) log-likelihood + iterated filtering (IF2) MLE for non-linear
    non-Gaussian state-space models.

    Category 10-trend-cycle-statespace; memory class ``light``.

    Args:
        model: [enum, optional] Built-in POMP template (same as pf_loglik). ONLY built-in — no user
            C-code. Default ``'gompertz'``.
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
        "pf_iterated_filtering: not implemented."
    )
