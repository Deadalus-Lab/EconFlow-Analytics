# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``bayesian_structural_var_identified_through`` -- method card #148.

#148 Bayesian Structural VAR identified through heteroskedasticity/non-normality (SV /
    Markov-switching heteroskedasticity / Student-t) + IRF/FEVD/HD/structural shocks + a
    Savage-Dickey (SDDR) identification check

Category 04-structural-shocks; module ``bayesian_structural_var_identified_through``.

Reference implementation: 10.1016/j.jedc.2020.103862.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import numpy as np

from econflow_engine.generated.args.c04_structural_shocks import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "bsv_estimate",
    "bsv_fevd",
    "bsv_hd",
    "bsv_irf",
    "bsv_shocks",
    "bsv_verify",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def bsv_estimate(
    *,
    data: np.ndarray,
    model: Literal["sv", "msh", "t"] | None = None,
    p: int | None = None,
    S: int | None = None,
    burnin: int | None = None,
    thin: int | None = None,
    M: int | None = None,
    stationary: bool | None = None,
    seed: int,
    allow_nonconvergence: bool | None = None,
) -> dict[str, Any]:
    """Node ``bsv_estimate`` -- method card #148.

    Bayesian Structural VAR identified through heteroskedasticity/non-normality (SV /
    Markov-switching heteroskedasticity / Student-t) + IRF/FEVD/HD/structural shocks + a
    Savage-Dickey (SDDR) identification check.

    Category 04-structural-shocks; memory class ``mcmc``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        data: [matrix_handle, required] Handle to a multivariate system (matrix/panel, K>=2, >=3
            rows, no NA/Inf).
        model: [enum, optional] Identification through statistical structure: sv=stochastic
            volatility, msh=Markov-switching heteroskedasticity, t=Student-t (default sv).
        p: [integer, optional] VAR order (positive integer, default 1). Default ``1``.
        S: [integer, optional] Retained posterior draws (TINY default 100· production raises it).
            Default ``100``.
        burnin: [integer, optional] Burn-in draws (non-negative, default 50). Default ``50``.
        thin: [integer, optional] Thinning factor (positive integer, default 1). Default ``1``.
        M: [integer, optional] Number of variance regimes (model='msh' only, >=2, default 2).
            Default ``2``.
        stationary: [boolean, optional] Impose the stationarity prior on the AR coefficients
            (default False). Default ``False``.
        seed: [integer, required] MANDATORY seed (the MCMC is stochastic· cache key).
        allow_nonconvergence: [boolean, optional] True = return the posterior with converged=False
            instead of stop on degenerate draws . Default ``False``.

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
        "bsv_estimate: not implemented."
    )


def bsv_irf(
    *,
    model: Any,
    horizon: int | None = None,
    standardise: bool | None = None,
    probs: Sequence[float] | None = None,
) -> dict[str, Any]:
    """Node ``bsv_irf`` -- method card #148.

    Bayesian Structural VAR identified through heteroskedasticity/non-normality (SV /
    Markov-switching heteroskedasticity / Student-t) + IRF/FEVD/HD/structural shocks + a
    Savage-Dickey (SDDR) identification check.

    Category 04-structural-shocks; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a 'PosteriorBSVAR*' model (bsv_estimate.model).
        horizon: [integer, optional] Impulse-response horizon 0..horizon (positive integer, default
            12). Default ``12``.
        standardise: [boolean, optional] Standardise the IRF in standard-deviation units (default
            False). Default ``False``.
        probs: [num_array, optional] Quantile bands of the posterior IRF ∈ (0,1) (default
            0.16/0.84).

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
        "bsv_irf: not implemented."
    )


def bsv_fevd(
    *,
    model: Any,
    horizon: int | None = None,
    probs: Sequence[float] | None = None,
) -> dict[str, Any]:
    """Node ``bsv_fevd`` -- method card #148.

    Bayesian Structural VAR identified through heteroskedasticity/non-normality (SV /
    Markov-switching heteroskedasticity / Student-t) + IRF/FEVD/HD/structural shocks + a
    Savage-Dickey (SDDR) identification check.

    Category 04-structural-shocks; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a 'PosteriorBSVAR*' model.
        horizon: [integer, optional] FEVD horizon (positive integer, default 12). Default ``12``.
        probs: [num_array, optional] Quantile bands ∈ (0,1) (default 0.16/0.84).

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
        "bsv_fevd: not implemented."
    )


def bsv_hd(
    *,
    model: Any,
    probs: Sequence[float] | None = None,
) -> dict[str, Any]:
    """Node ``bsv_hd`` -- method card #148.

    Bayesian Structural VAR identified through heteroskedasticity/non-normality (SV /
    Markov-switching heteroskedasticity / Student-t) + IRF/FEVD/HD/structural shocks + a
    Savage-Dickey (SDDR) identification check.

    Category 04-structural-shocks; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a 'PosteriorBSVAR*' model.
        probs: [num_array, optional] Quantile bands ∈ (0,1) (default 0.16/0.84).

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
        "bsv_hd: not implemented."
    )


def bsv_shocks(
    *,
    model: Any,
    probs: Sequence[float] | None = None,
) -> dict[str, Any]:
    """Node ``bsv_shocks`` -- method card #148.

    Bayesian Structural VAR identified through heteroskedasticity/non-normality (SV /
    Markov-switching heteroskedasticity / Student-t) + IRF/FEVD/HD/structural shocks + a
    Savage-Dickey (SDDR) identification check.

    Category 04-structural-shocks; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a 'PosteriorBSVAR*' model.
        probs: [num_array, optional] Quantile bands ∈ (0,1) (default 0.16/0.84).

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
        "bsv_shocks: not implemented."
    )


def bsv_verify(
    *,
    model: Any,
    allow_nonconvergence: bool | None = None,
) -> dict[str, Any]:
    """Node ``bsv_verify`` -- method card #148.

    Bayesian Structural VAR identified through heteroskedasticity/non-normality (SV /
    Markov-switching heteroskedasticity / Student-t) + IRF/FEVD/HD/structural shocks + a
    Savage-Dickey (SDDR) identification check.

    Category 04-structural-shocks; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a 'PosteriorBSVAR*' model (SDDR identification
            check).
        allow_nonconvergence: [boolean, optional] True = return a degenerate SDDR instead of stop
            (default False). Default ``False``.

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
        "bsv_verify: not implemented."
    )
