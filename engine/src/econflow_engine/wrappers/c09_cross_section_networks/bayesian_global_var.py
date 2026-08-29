# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``bayesian_global_var`` -- method card #176.

#176 Bayesian Global VAR (multi-country shrinkage + SV): estimation + generalized-FEVD
    spillovers/GIRF + a posterior-predictive forecast

Category 09-cross-section-networks; module ``bayesian_global_var``.

Reference implementation: 10.1002/jae.2504.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import numpy as np

from econflow_engine.generated.args.c09_cross_section_networks import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "bgvar_fit",
    "bgvar_predict",
    "bgvar_spillover",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def bgvar_fit(
    *,
    Data: Any,
    W: np.ndarray,
    plag: int | None = None,
    draws: int | None = None,
    burnin: int | None = None,
    prior: Literal["MN", "SSVS", "NG"] | None = None,
    SV: bool | None = None,
    hold_out: int | None = None,
    thin: int | None = None,
    eigen: bool | None = None,
    trend: bool | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``bgvar_fit`` -- method card #176.

    Bayesian Global VAR (multi-country shrinkage + SV): estimation + generalized-FEVD
    spillovers/GIRF + a posterior-predictive forecast.

    Category 09-cross-section-networks; memory class ``mcmc``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        Data: [raw, required] Named list of countries (numeric matrices/ts, same nrow) or matrix T x
            K with column names "Country.Variable". Country/variable names WITHOUT a dot.
        W: [matrix_handle, required] N x N weight matrix (trade/spatial), diag(W)=0, row sums=1,
            row/col names = country names.
        plag: [integer, optional] Lag order (domestic & weakly-exogenous). Default 1. Default ``1``.
        draws: [integer, optional] Number of retained MCMC draws. Default 200 (keep it small).
            Default ``200``.
        burnin: [integer, optional] Number of burn-in draws. Default 200. Default ``200``.
        prior: [enum, optional] Shrinkage prior: MN (Minnesota, default/fast) · SSVS · NG
            (Normal-Gamma). Default ``'MN'``.
        SV: [boolean, optional] Stochastic volatility. Default False. Default ``False``.
        hold_out: [integer, optional] Hold-out sample (>0 required for LPS/RMSE in bgvar_predict).
            Default 0. Default ``0``.
        thin: [integer, optional] Thinning interval of the MCMC. Default 1. Default ``1``.
        eigen: [boolean, optional] Trimming of unstable draws (stability). Default True. Default
            ``True``.
        trend: [boolean, optional] Deterministic trend. Default False. Default ``False``.
        seed: [integer, optional] Reproducibility seed (MCMC). Default 2025. Default ``2025``.

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
        "bgvar_fit: not implemented."
    )


def bgvar_spillover(
    *,
    object: Any,
    n_ahead: int | None = None,
    type: Literal["gfevd", "girf"] | None = None,
    shock: str | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``bgvar_spillover`` -- method card #176.

    Bayesian Global VAR (multi-country shrinkage + SV): estimation + generalized-FEVD
    spillovers/GIRF + a posterior-predictive forecast.

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        object: [raw_handle, required] Fitted 'bgvar' object (bgvar_fit(...)$object).
        n_ahead: [integer, optional] Horizon. Default 8. Default ``8``.
        type: [enum, optional] gfevd: generalized FEVD spillover matrix + Diebold-Yilmaz
            (to/from/net). girf: generalized IRF for a shock variable. Default ``'gfevd'``.
        shock: [string, optional] ONLY for type='girf': shock variable name "Country.Variable" (e.g.
            "US.stir").
        seed: [integer, optional] Reproducibility seed. Default 2025. Default ``2025``.

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
        "bgvar_spillover: not implemented."
    )


def bgvar_predict(
    *,
    object: Any,
    n_ahead: int | None = None,
    quantiles: Sequence[float] | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``bgvar_predict`` -- method card #176.

    Bayesian Global VAR (multi-country shrinkage + SV): estimation + generalized-FEVD
    spillovers/GIRF + a posterior-predictive forecast.

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        object: [raw_handle, required] Fitted 'bgvar' object (bgvar_fit(...)$object).
        n_ahead: [integer, optional] Forecast horizon. Default 4. Default ``4``.
        quantiles: [num_array, optional] Posterior quantiles in (0,1). Default [0.16,0.5,0.84].
            Default ``[0.16, 0.5, 0.84]``.
        seed: [integer, optional] Reproducibility seed (posterior predictive). Default 2025. Default
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
        "bgvar_predict: not implemented."
    )
