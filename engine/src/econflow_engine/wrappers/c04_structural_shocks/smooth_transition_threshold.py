# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``smooth_transition_threshold`` -- method card #150.

#150 Smooth-transition / threshold / (m)logistic STRUCTURAL VAR (nonlinear, regime-dependent
    dynamics) + GIRF/GFEVD/linear IRF

Category 04-structural-shocks; module ``smooth_transition_threshold``.

Reference implementation: 10.1080/07474938.2026.2673986.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c04_structural_shocks import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "sst_fit",
    "sst_gfevd",
    "sst_girf",
    "sst_linear_irf",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def sst_fit(
    *,
    data: pd.DataFrame,
    p: int | None = None,
    M: int | None = None,
    weight_function: (
        Literal[
            "relative_dens",
            "logistic",
            "mlogit",
            "exponential",
            "threshold",
            "exogenous",
        ]
        | None
    ) = None,
    cond_dist: Literal["Gaussian", "Student", "ind_Student", "ind_skewed_t"] | None = None,
    parametrization: Literal["intercept", "mean"] | None = None,
    weightfun_pars: Sequence[float] | None = None,
    nrounds: int | None = None,
    ngen: int | None = None,
    maxit: int | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``sst_fit`` -- method card #150.

    Smooth-transition / threshold / (m)logistic STRUCTURAL VAR (nonlinear, regime-dependent
    dynamics) + GIRF/GFEVD/linear IRF.

    Category 04-structural-shocks; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        data: [multiseries_handle, required] Handle to a multivariate series (matrix/ts, T x d,
            d>=2, no NA/Inf).
        p: [integer, optional] VAR lag order (positive integer, default 1). Default ``1``.
        M: [integer, optional] Number of regimes (positive integer, default 2). Default ``2``.
        weight_function: [enum, optional] Transition-weight function (default relative_dens —
            Gaussian ONLY).
        cond_dist: [enum, optional] Conditional error distribution (default Gaussian).
        parametrization: [enum, optional] Intercept or mean parametrization (default intercept).
        weightfun_pars: [num_array, optional] Weight-function parameters· [switch_var, lag] for
            logistic/exponential/threshold (mandatory when weight_function != relative_dens).
        nrounds: [integer, optional] Number of GA estimation rounds (default 2 — TINY· production
            raises it). Default ``2``.
        ngen: [integer, optional] Genetic-algorithm generations per round (default 30 — TINY).
            Default ``30``.
        maxit: [integer, optional] Maximum variable-metric optim iterations (default 300). Default
            ``300``.
        seed: [integer, required] MANDATORY seed (integer) — stochastic GA· seeded + seeds vector.

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
        "sst_fit: not implemented."
    )


def sst_girf(
    *,
    model: Any,
    which_shocks: Sequence[float] | None = None,
    N: int | None = None,
    shock_size: float | None = None,
    n_iterations: int | None = None,
    n_initial_values: int | None = None,
    init_regime: int | None = None,
    ci: Sequence[float] | None = None,
    burn_in: int | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``sst_girf`` -- method card #150.

    Smooth-transition / threshold / (m)logistic STRUCTURAL VAR (nonlinear, regime-dependent
    dynamics) + GIRF/GFEVD/linear IRF.

    Category 04-structural-shocks; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a fitted 'stvar' model (from sst_fit).
        which_shocks: [num_array, optional] Indices of the structural shocks in [1, d] (default 1).
        N: [integer, optional] GIRF horizon (positive integer, default 16). Default ``16``.
        shock_size: [number, optional] Size/sign of the shock (default 1). Default ``1``.
        n_iterations: [integer, optional] MC iterations per initial value (default 50 — TINY).
            Default ``50``.
        n_initial_values: [integer, optional] Number of initial values from init_regime (default 50
            — TINY). Default ``50``.
        init_regime: [integer, optional] Regime generating the initial values 1..M (default 1).
            Default ``1``.
        ci: [num_array, optional] Confidence levels of the bands (default [0.95, 0.8]).
        burn_in: [integer, optional] Simulation burn-in (default 200). Default ``200``.
        seed: [integer, required] MANDATORY seed — simulation-based· seeded for reproducibility.

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
        "sst_girf: not implemented."
    )


def sst_gfevd(
    *,
    model: Any,
    N: int | None = None,
    shock_size: float | None = None,
    initval_type: Literal["random", "data", "fixed"] | None = None,
    n_iterations: int | None = None,
    n_initial_values: int | None = None,
    init_regime: int | None = None,
    burn_in: int | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``sst_gfevd`` -- method card #150.

    Smooth-transition / threshold / (m)logistic STRUCTURAL VAR (nonlinear, regime-dependent
    dynamics) + GIRF/GFEVD/linear IRF.

    Category 04-structural-shocks; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a fitted 'stvar' model (from sst_fit).
        N: [integer, optional] GFEVD horizon (positive integer, default 16). Default ``16``.
        shock_size: [number, optional] Size/sign of the shocks (default 1). Default ``1``.
        initval_type: [enum, optional] Type of initial values for the GIRFs (default random).
        n_iterations: [integer, optional] MC iterations per initial value (default 50 — TINY).
            Default ``50``.
        n_initial_values: [integer, optional] Number of initial values (random/fixed) (default 50 —
            TINY). Default ``50``.
        init_regime: [integer, optional] Regime of the initial values 1..M (default 1). Default
            ``1``.
        burn_in: [integer, optional] Simulation burn-in (default 200). Default ``200``.
        seed: [integer, required] MANDATORY seed — simulation-based· seeded for reproducibility.

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
        "sst_gfevd: not implemented."
    )


def sst_linear_irf(
    *,
    model: Any,
    N: int | None = None,
    regime: int | None = None,
    ci: float | None = None,
    bootstrap_reps: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``sst_linear_irf`` -- method card #150.

    Smooth-transition / threshold / (m)logistic STRUCTURAL VAR (nonlinear, regime-dependent
    dynamics) + GIRF/GFEVD/linear IRF.

    Category 04-structural-shocks; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a fitted 'stvar' model (reduced-form -> recursive
            ID).
        N: [integer, optional] Linear-IRF horizon (positive integer, default 16). Default ``16``.
        regime: [integer, optional] Regime 1..M on which the linear IRF is computed (default 1).
            Default ``1``.
        ci: [number, optional] Confidence level of the wild-bootstrap bands in (0,1)· only for
            linear-AR models (default None = no bands).
        bootstrap_reps: [integer, optional] Bootstrap replications when ci != None (default 100).
            Default ``100``.
        seed: [integer, optional] Seed for the ci bootstrap (default None· deterministic when
            ci=None).

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
        "sst_linear_irf: not implemented."
    )
