# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``tvp_var_stochastic`` -- method card #14.

#14 TVP-VAR with Stochastic Volatility

Category 03-multivariate-nowcasting; module ``tvp_var_stochastic``.

Reference implementation: 10.1111/j.1467-937X.2005.00353.x.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any

import pandas as pd

from econflow_engine.generated.args.c03_multivariate_nowcasting import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "sv_estimate",
    "sv_irf",
    "sv_parameter_draws",
    "sv_predict_density",
    "sv_predict_draws",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def sv_estimate(
    *,
    Y: pd.DataFrame,
    p: int | None = None,
    tau: int | None = None,
    nf: int | None = None,
    nrep: int | None = None,
    nburn: int | None = None,
    thinfac: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``sv_estimate`` -- method card #14.

    TVP-VAR with Stochastic Volatility.

    Category 03-multivariate-nowcasting; memory class ``heavy``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        Y: [multiseries_handle, required] Handle to multivariate data (>=2 columns, finite).
        p: [integer, optional] VAR lag order (default 1). Default ``1``.
        tau: [integer, optional] Training sample size for the LS prior (>= ncol*p+1, default 40).
            Default ``40``.
        nf: [integer, optional] Forecast horizon that is stored (default 10). Default ``10``.
        nrep: [integer, optional] MCMC replications after burn-in (default 50000). Default
            ``50000``.
        nburn: [integer, optional] Burn-in draws (default 5000). Default ``5000``.
        thinfac: [integer, optional] Thinning factor (default 10). Default ``10``.
        seed: [integer, optional] Seed for reproducibility (optional).

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
        "sv_estimate: not implemented."
    )


def sv_predict_density(
    *,
    model: Any,
    variable: int | None = None,
    horizon: int | None = None,
    n_grid: int | None = None,
    cdf: bool | None = None,
) -> dict[str, Any]:
    """Node ``sv_predict_density`` -- method card #14.

    TVP-VAR with Stochastic Volatility.

    Category 03-multivariate-nowcasting; memory class ``heavy``.

    Args:
        model: [raw_handle, required] Handle to a TVP-VAR-SV fit (from sv_estimate).
        variable: [integer, optional] Variable index (1..M) (default 1). Default ``1``.
        horizon: [integer, optional] Forecast horizon (1..nf) (default 1). Default ``1``.
        n_grid: [integer, optional] Number of grid points at which the density is evaluated (default
            101). Default ``101``.
        cdf: [boolean, optional] Return the CDF instead of the PDF (default False). Default
            ``False``.

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
        "sv_predict_density: not implemented."
    )


def sv_predict_draws(
    *,
    model: Any,
    variable: int | None = None,
    horizon: int | None = None,
) -> dict[str, Any]:
    """Node ``sv_predict_draws`` -- method card #14.

    TVP-VAR with Stochastic Volatility.

    Category 03-multivariate-nowcasting; memory class ``heavy``.

    Args:
        model: [raw_handle, required] Handle to a TVP-VAR-SV fit (from sv_estimate).
        variable: [integer, optional] Variable index (1..M) (default 1). Default ``1``.
        horizon: [integer, optional] Forecast horizon (1..nf) (default 1). Default ``1``.

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
        "sv_predict_draws: not implemented."
    )


def sv_irf(
    *,
    model: Any,
    impulse: int | None = None,
    response: int | None = None,
    horizon: int | None = None,
    scenario: int | None = None,
) -> dict[str, Any]:
    """Node ``sv_irf`` -- method card #14.

    TVP-VAR with Stochastic Volatility.

    Category 03-multivariate-nowcasting; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a TVP-VAR-SV fit (from sv_estimate,
            save.parameters).
        impulse: [integer, optional] Shock variable index (1..M) (default 1). Default ``1``.
        response: [integer, optional] Response variable index (1..M) (default 2). Default ``2``.
        horizon: [integer, optional] IRF horizon (default 20). Default ``20``.
        scenario: [integer, optional] 1=no orthogonalization, 2=Cholesky, 3=DNP (default 2). Default
            ``2``.

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
        "sv_irf: not implemented."
    )


def sv_parameter_draws(
    *,
    model: Any,
    type: str | None = None,
    row: int | None = None,
    col: int | None = None,
) -> dict[str, Any]:
    """Node ``sv_parameter_draws`` -- method card #14.

    TVP-VAR with Stochastic Volatility.

    Category 03-multivariate-nowcasting; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a TVP-VAR-SV fit (from sv_estimate,
            save.parameters).
        type: [string, optional] Parameter: 'intercept', 'lag1'..'lagP' or 'vcv' (default 'lag1').
            Default ``'lag1'``.
        row: [integer, optional] Row of the coefficient matrix (default 1). Default ``1``.
        col: [integer, optional] Column of the coefficient matrix (default 1). Default ``1``.

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
        "sv_parameter_draws: not implemented."
    )
