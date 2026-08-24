# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``bayesian_averaging`` -- method card #219.

#219 Bayesian Model Averaging (BMA, g-priors: enumeration + MCMC)

Category 20-highdim-shrinkage-ml; module ``bayesian_averaging``.

Reference implementation: 10.18637/jss.v068.i04.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c20_highdim_shrinkage_ml import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "bma_average",
    "bma_coefficients",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def bma_average(
    *,
    X_data: np.ndarray,
    mprior: Literal["uniform", "fixed", "random", "pip"] | None = None,
    g: str | None = None,
    mcmc: Literal["enumerate", "bd", "rev.jump"] | None = None,
    nmodel: int | None = None,
    burn: int | None = None,
    iter: int | None = None,
    mprior_size: float | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``bma_average`` -- method card #219.

    Bayesian Model Averaging (BMA, g-priors: enumeration + MCMC).

    Category 20-highdim-shrinkage-ml; memory class ``mcmc``.

    Registers its result under ``bma``, so a later node can consume it as a handle.

    Args:
        X_data: [matrix_handle, required] Handle to a numeric data matrix: 1st column = dependent y,
            remaining columns = regressors (K >= 1). Without NA/Inf; N > K+1.
        mprior: [enum, optional] Model prior (default uniform): uniform (each model equiprobable);
            fixed (fixed expected size); random (beta-binomial, Ley-Steel)· pip (fixed inclusion
            probs).
        g: [string, optional] g-prior: 'UIP' (unit info, g=N· default)· 'BRIC' (g=max(N,K^2))· 'RIC'
            (g=K^2)· 'HQ' (Hannan-Quinn), or a positive number as a string (e.g. '10') for a custom
            g.
        mcmc: [enum, optional] Sampler (default enumerate): 'enumerate' = exact enumeration of ALL
            2^K models (DETERMINISTIC; only K<=20 — prefer it there); 'bd' = birth-death MCMC;
            'rev.jump' = reversible-jump MCMC. THE MCMC ARE STOCHASTIC and are NOT bit-reproducible
            even with a fixed seed (see $reproducibility in the output).
        nmodel: [integer, optional] Number of top models kept (default 100). Default ``100``.
        burn: [integer, optional] MCMC burn-in draws (only for bd/rev.jump; default 1000). Default
            ``1000``.
        iter: [integer, optional] MCMC posterior draws (only for bd/rev.jump; default 3000). Default
            ``3000``.
        mprior_size: [number, optional] Expected model size for fixed/random priors, in (0, K);
            default K/2 of the package.
        seed: [integer, optional] MCMC reproducibility seed (inert in enumerate; default 42).
            Default ``42``.

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
        "bma_average: not implemented."
    )


def bma_coefficients(
    *,
    object: Any,
    exact: bool | None = None,
    order_by_pip: bool | None = None,
) -> dict[str, Any]:
    """Node ``bma_coefficients`` -- method card #219.

    Bayesian Model Averaging (BMA, g-priors: enumeration + MCMC).

    Category 20-highdim-shrinkage-ml; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a fitted bma object (from bma_average register).
        exact: [boolean, optional] True = analytical (exact) posterior moments· False =
            MCMC-frequency-based (default False· use True after enumerate). Default ``False``.
        order_by_pip: [boolean, optional] Sorting of regressors by descending PIP (default True).
            Default ``True``.

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
        "bma_coefficients: not implemented."
    )
