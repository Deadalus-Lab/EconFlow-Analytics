# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``bayesian_var_vhar`` -- method card #147.

#147 Bayesian VAR & VHAR (Vector Heterogeneous AR; day/week/month long memory) with a Minnesota
    conjugate (analytic) / SSVS / Horseshoe prior + a posterior forecast fan

Category 03-multivariate-nowcasting; module ``bayesian_var_vhar``.

Reference implementation: 10.1080/00949655.2023.2281644.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c03_multivariate_nowcasting import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "bvh_predict",
    "bvh_var",
    "bvh_vhar",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def bvh_var(
    *,
    y: pd.DataFrame,
    p: int | None = None,
    prior: Literal["minnesota", "ssvs", "horseshoe"] | None = None,
    lambda_: float | None = None,
    num_chains: int | None = None,
    num_iter: int | None = None,
    num_burn: int | None = None,
    thinning: int | None = None,
    include_mean: bool | None = None,
    seed: int | None = None,
    rhat_max: float | None = None,
    ess_min: float | None = None,
    allow_nonconvergence: bool | None = None,
) -> dict[str, Any]:
    """Node ``bvh_var`` -- method card #147.

    Bayesian VAR & VHAR (Vector Heterogeneous AR; day/week/month long memory) with a Minnesota
    conjugate (analytic) / SSVS / Horseshoe prior + a posterior forecast fan.

    Category 03-multivariate-nowcasting; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        y: [multiseries_handle, required] Handle to multivariate data (>=2 columns, finite).
        p: [integer, optional] VAR lag order (default 1). Default ``1``.
        prior: [enum, optional] Prior: minnesota=conjugate/analytic· ssvs/horseshoe=MCMC (seed
            mandatory + convergence gate). Default ``'minnesota'``.
        lambda_ (wire name ``lambda``): [number, optional] Minnesota tightness > 0 (default 0.1).
            Default ``0.1``.
        num_chains: [integer, optional] MCMC chains (>=2 for a valid Rhat· default 2). Default
            ``2``.
        num_iter: [integer, optional] MCMC iterations (default 200· small). Default ``200``.
        num_burn: [integer, optional] Burn-in (< num_iter· default 100). Default ``100``.
        thinning: [integer, optional] Thinning step (default 1). Default ``1``.
        include_mean: [boolean, optional] Include a constant term (default True). Default ``True``.
        seed: [integer, optional] Seed· MANDATORY for ssvs/horseshoe (MCMC).
        rhat_max: [number, optional] Maximum acceptable Rhat convergence gate (default 1.1). Default
            ``1.1``.
        ess_min: [number, optional] Minimum acceptable Bulk-ESS (default 100). Default ``100``.
        allow_nonconvergence: [boolean, optional] True -> return draws with converged=False instead
            of stop (default False). Default ``False``.

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
        "bvh_var: not implemented."
    )


def bvh_vhar(
    *,
    y: pd.DataFrame,
    har: Sequence[int] | None = None,
    prior: Literal["minnesota", "ssvs", "horseshoe"] | None = None,
    lambda_: float | None = None,
    num_chains: int | None = None,
    num_iter: int | None = None,
    num_burn: int | None = None,
    thinning: int | None = None,
    include_mean: bool | None = None,
    seed: int | None = None,
    rhat_max: float | None = None,
    ess_min: float | None = None,
    allow_nonconvergence: bool | None = None,
) -> dict[str, Any]:
    """Node ``bvh_vhar`` -- method card #147.

    Bayesian VAR & VHAR (Vector Heterogeneous AR; day/week/month long memory) with a Minnesota
    conjugate (analytic) / SSVS / Horseshoe prior + a posterior forecast fan.

    Category 03-multivariate-nowcasting; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        y: [multiseries_handle, required] Handle to multivariate data (>=2 columns, finite).
        har: [int_array, optional] VHAR thresholds (week, month)· 2 increasing positive integers
            (default [5,22]). Default ``[5, 22]``.
        prior: [enum, optional] Prior: minnesota=conjugate/analytic· ssvs/horseshoe=MCMC. Default
            ``'minnesota'``.
        lambda_ (wire name ``lambda``): [number, optional] Minnesota tightness > 0 (default 0.1).
            Default ``0.1``.
        num_chains: [integer, optional] MCMC chains (>=2· default 2). Default ``2``.
        num_iter: [integer, optional] MCMC iterations (default 200). Default ``200``.
        num_burn: [integer, optional] Burn-in (< num_iter· default 100). Default ``100``.
        thinning: [integer, optional] Thinning step (default 1). Default ``1``.
        include_mean: [boolean, optional] Include a constant term (default True). Default ``True``.
        seed: [integer, optional] Seed· MANDATORY for ssvs/horseshoe.
        rhat_max: [number, optional] Maximum Rhat gate (default 1.1). Default ``1.1``.
        ess_min: [number, optional] Minimum Bulk-ESS (default 100). Default ``100``.
        allow_nonconvergence: [boolean, optional] True -> converged=False instead of stop (default
            False). Default ``False``.

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
        "bvh_vhar: not implemented."
    )


def bvh_predict(
    *,
    model: Any,
    n_ahead: int | None = None,
    level: float | None = None,
    sparse: bool | None = None,
) -> dict[str, Any]:
    """Node ``bvh_predict`` -- method card #147.

    Bayesian VAR & VHAR (Vector Heterogeneous AR; day/week/month long memory) with a Minnesota
    conjugate (analytic) / SSVS / Horseshoe prior + a posterior forecast fan.

    Category 03-multivariate-nowcasting; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a bvhar model (from bvh_var/bvh_vhar).
        n_ahead: [integer, optional] Forecast horizon (default 8). Default ``8``.
        level: [number, optional] Significance level ∈ (0,1)· 0.05 -> 95% interval (default 0.05).
            Default ``0.05``.
        sparse: [boolean, optional] True -> sparsified (SAVS) coefficients (MCMC only· default
            False). Default ``False``.

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
        "bvh_predict: not implemented."
    )
