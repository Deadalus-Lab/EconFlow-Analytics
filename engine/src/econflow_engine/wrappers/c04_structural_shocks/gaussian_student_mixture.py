# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``gaussian_student_mixture`` -- METHOD-SELECTION card #151.

#151 Gaussian / Student's-t Mixture VAR (regime switching through mixture-density weights) +
    GIRF/GFEVD/linear IRF — gmvarkit

Category 04-structural-shocks; module ``gaussian_student_mixture``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c04_structural_shocks import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "gmv_fit",
    "gmv_gfevd",
    "gmv_girf",
    "gmv_linear_irf",
    "NODE_META",
    "wire_model",
]


def gmv_fit(
    *,
    data: pd.DataFrame,
    p: int | None = None,
    M: Sequence[int] | None = None,
    model: Literal["GMVAR", "StMVAR", "G-StMVAR"] | None = None,
    conditional: bool | None = None,
    parametrization: Literal["intercept", "mean"] | None = None,
    structural_W: np.ndarray | None = None,
    ncalls: int | None = None,
    ncores: int | None = None,
    maxit: int | None = None,
    seed: int,
    allow_nonconvergence: bool | None = None,
) -> dict[str, Any]:
    """Node ``gmv_fit`` -- METHOD-SELECTION card #151.

    Gaussian / Student's-t Mixture VAR (regime switching through mixture-density weights) +
    GIRF/GFEVD/linear IRF — gmvarkit.

    Category 04-structural-shocks; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        data: [multiseries_handle, required] Handle to a multivariate series (matrix/ts, T x d,
            d>=2, no NA/Inf).
        p: [integer, optional] VAR lag order (positive integer, default 1). Default ``1``.
        M: [int_array, optional] Number of regimes· positive integer (GMVAR/StMVAR) or a length-2
            vector [M1,M2] for G-StMVAR (default 2). Default ``2``.
        model: [enum, optional] Mixture type: Gaussian (GMVAR), Student's-t (StMVAR), or mixed
            G-StMVAR (default GMVAR).
        conditional: [boolean, optional] Conditional (True) or exact (False) log-likelihood (default
            True). Default ``True``.
        parametrization: [enum, optional] Intercept or mean parametrization (default intercept).
        structural_W: [matrix_handle, optional] Optional d x d constraint matrix W for structural
            identification through conditional heteroskedasticity (NA=free, +/-=sign, 0=zero)·
            requires M>=2. None => reduced-form (recursive Cholesky).
        ncalls: [integer, optional] Number of GA estimation rounds (default 2 — TINY· production
            raises it to (M+1)^5). Default ``2``.
        ncores: [integer, optional] CPU cores (default 1· use_parallel only when >1). Default ``1``.
        maxit: [integer, optional] Maximum variable-metric optim iterations per round (default 100).
            Default ``100``.
        seed: [integer, required] MANDATORY seed (integer) — stochastic GA· set.seed + reproducible
            seeds vector.
        allow_nonconvergence: [boolean, optional] True to bypass the convergence gate (degenerate
            estimates· the IRF/FEVD will be UNRELIABLE· default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "gmv_fit: not implemented. The method card is in ./README.md."
    )


def gmv_girf(
    *,
    model: Any,
    which_shocks: Sequence[int] | None = None,
    N: int | None = None,
    n_iterations: int | None = None,
    n_initial_values: int | None = None,
    shock_size: float | None = None,
    ci: Sequence[float] | None = None,
    include_mixweights: bool | None = None,
    ncores: int | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``gmv_girf`` -- METHOD-SELECTION card #151.

    Gaussian / Student's-t Mixture VAR (regime switching through mixture-density weights) +
    GIRF/GFEVD/linear IRF — gmvarkit.

    Category 04-structural-shocks; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a fitted 'gsmvar' model (from gmv_fit).
        which_shocks: [int_array, optional] Indices of the structural shocks in [1, d] (default 1).
            Default ``1``.
        N: [integer, optional] GIRF horizon (positive integer, default 10). Default ``10``.
        n_iterations: [integer, optional] MC iterations per initial value (default 50 — TINY).
            Default ``50``.
        n_initial_values: [integer, optional] Number of initial values from the stationary
            distribution (default 50 — TINY). Default ``50``.
        shock_size: [number, optional] Size/sign of the shock· non-zero (default 1). Default ``1``.
        ci: [num_array, optional] Confidence levels of the bands in (0,1) (default [0.95, 0.8]).
        include_mixweights: [boolean, optional] GIRF for the mixing weights as well (default False).
            Default ``False``.
        ncores: [integer, optional] CPU cores (default 1). Default ``1``.
        seed: [integer, required] MANDATORY seed — simulation-based· set.seed for reproducibility.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "gmv_girf: not implemented. The method card is in ./README.md."
    )


def gmv_gfevd(
    *,
    model: Any,
    N: int | None = None,
    n_iterations: int | None = None,
    n_initial_values: int | None = None,
    initval_type: Literal["data", "random"] | None = None,
    shock_size: float | None = None,
    include_mixweights: bool | None = None,
    ncores: int | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``gmv_gfevd`` -- METHOD-SELECTION card #151.

    Gaussian / Student's-t Mixture VAR (regime switching through mixture-density weights) +
    GIRF/GFEVD/linear IRF — gmvarkit.

    Category 04-structural-shocks; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a fitted 'gsmvar' model (from gmv_fit).
        N: [integer, optional] GFEVD horizon (positive integer, default 10). Default ``10``.
        n_iterations: [integer, optional] MC iterations per initial value (default 50 — TINY).
            Default ``50``.
        n_initial_values: [integer, optional] Number of random initial values when
            initval_type='random' (default 50 — TINY). Default ``50``.
        initval_type: [enum, optional] Initial values of the GIRFs: all p-histories of the data
            ('data') or random draws from the stationary distribution ('random') (default data).
        shock_size: [number, optional] Size/sign of the shocks· non-zero (default 1). Default ``1``.
        include_mixweights: [boolean, optional] GFEVD for the mixing weights as well (default
            False). Default ``False``.
        ncores: [integer, optional] CPU cores (default 1). Default ``1``.
        seed: [integer, required] MANDATORY seed — simulation-based· set.seed for reproducibility.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "gmv_gfevd: not implemented. The method card is in ./README.md."
    )


def gmv_linear_irf(
    *,
    model: Any,
    N: int | None = None,
    regime: int | None = None,
    ci: float | None = None,
    bootstrap_reps: int | None = None,
    ncores: int | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``gmv_linear_irf`` -- METHOD-SELECTION card #151.

    Gaussian / Student's-t Mixture VAR (regime switching through mixture-density weights) +
    GIRF/GFEVD/linear IRF — gmvarkit.

    Category 04-structural-shocks; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a fitted 'gsmvar' model (structural W or
            reduced-form -> recursive Cholesky).
        N: [integer, optional] Linear-IRF horizon (positive integer, default 10). Default ``10``.
        regime: [integer, optional] Regime 1..sum(M) on which the linear IRF is computed (default
            1). Default ``1``.
        ci: [number, optional] Confidence level of the wild-bootstrap bands in (0,1)· only for
            linear-AR models (default None = no bands).
        bootstrap_reps: [integer, optional] Bootstrap replications when ci != None (default 100).
            Default ``100``.
        ncores: [integer, optional] CPU cores (default 1). Default ``1``.
        seed: [integer, required] MANDATORY seed — stochastic bootstrap· set.seed for
            reproducibility.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "gmv_linear_irf: not implemented. The method card is in ./README.md."
    )
