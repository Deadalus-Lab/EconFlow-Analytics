# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``bayesian_univariate_stochastic`` -- method card #162.

#162 Bayesian univariate Stochastic Volatility (vanilla / Student-t / leverage) via MCMC

Category 06-volatility-regimes; module ``bayesian_univariate_stochastic``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

from econflow_engine.generated.args.c06_volatility_regimes import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "sv_predict",
    "sv_sample",
    "sv_simulate",
    "NODE_META",
    "wire_model",
]


def sv_sample(
    *,
    y: Sequence[float],
    model: Literal["vanilla", "t", "leverage"] | None = None,
    draws: int | None = None,
    burnin: int | None = None,
    priormu: Sequence[float] | None = None,
    priorphi: Sequence[float] | None = None,
    priorsigma: float | None = None,
    priornu: float | None = None,
    priorrho: Sequence[float] | None = None,
    keeptime: Literal["all", "last"] | None = None,
    thin: int | None = None,
    ess_min: float | None = None,
) -> dict[str, Any]:
    """Node ``sv_sample`` -- method card #162.

    Bayesian univariate Stochastic Volatility (vanilla / Student-t / leverage) via MCMC.

    Category 06-volatility-regimes; memory class ``mcmc``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        y: [num_array, required] Numeric vector of returns (without NA/Inf, length > 1).
        model: [enum, optional] SV variant: vanilla (Gaussian), t (Student-t errors), leverage
            (asymmetric)· default vanilla.
        draws: [integer, optional] MCMC draws after burnin (default 500· keep it small). Default
            ``500``.
        burnin: [integer, optional] Burn-in draws (default 200). Default ``200``.
        priormu: [num_array, optional] Normal prior on mu: [mean, sd] (default [0,100]).
        priorphi: [num_array, optional] Beta prior on (phi+1)/2: [a0,b0] positive (default [5,1.5]).
        priorsigma: [number, optional] Scale of the Gamma prior on sigma (positive, default 1).
            Default ``1``.
        priornu: [number, optional] Rate of the exp. prior on nu — model='t' only (default 0.1).
        priorrho: [num_array, optional] Beta prior on (rho+1)/2: [a,b] positive — model='leverage'
            only (default [4,4]).
        keeptime: [enum, optional] 'all'=full latent path (vol chart-data)· 'last'=last only
            (default all).
        thin: [integer, optional] Thinning interval draws (default 1). Default ``1``.
        ess_min: [number, optional] Minimum ESS threshold for the converged flag (default 20).
            Default ``20``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "sv_sample: not implemented."
    )


def sv_predict(
    *,
    object: Any,
    steps: int | None = None,
) -> dict[str, Any]:
    """Node ``sv_predict`` -- method card #162.

    Bayesian univariate Stochastic Volatility (vanilla / Student-t / leverage) via MCMC.

    Category 06-volatility-regimes; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to an 'svdraws' (from sv_sample).
        steps: [integer, optional] Forecast horizon for future volatility (>=1, default 1). Default
            ``1``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "sv_predict: not implemented."
    )


def sv_simulate(
    *,
    len: int,
    mu: float | None = None,
    phi: float | None = None,
    sigma: float | None = None,
    nu: float | None = None,
    rho: float | None = None,
) -> dict[str, Any]:
    """Node ``sv_simulate`` -- method card #162.

    Bayesian univariate Stochastic Volatility (vanilla / Student-t / leverage) via MCMC.

    Category 06-volatility-regimes; memory class ``light``.

    Args:
        len: [integer, required] Length of the simulated series (>=2).
        mu: [number, optional] Level of the log-variance (default -10). Default ``-10``.
        phi: [number, optional] Persistence in (-1,1) (default 0.98). Default ``0.98``.
        sigma: [number, optional] Vol-of-vol, positive (default 0.2). Default ``0.2``.
        nu: [number, optional] Student-t degrees of freedom (>2· default Inf=Gaussian).
        rho: [number, optional] Leverage correlation in (-1,1) (default 0=no leverage). Default
            ``0``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "sv_simulate: not implemented."
    )
