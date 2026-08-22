# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``discrete_time_markov`` -- method card #164.

#164 Discrete-time Markov chain: estimating the transition matrix (MLE/Laplace/bootstrap CI) +
    long-run analytics (the stationary distribution, mean first passage times, irreducibility,
    period)

Category 06-volatility-regimes; module ``discrete_time_markov``.

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
    "mc_analytics",
    "mc_fit",
    "NODE_META",
    "wire_model",
]


def mc_fit(
    *,
    data: Sequence[str],
    method: Literal["mle", "laplace", "bootstrap"] | None = None,
    laplacian: float | None = None,
    confidencelevel: float | None = None,
    nboot: int | None = None,
    sanitize: bool | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``mc_fit`` -- method card #164.

    Discrete-time Markov chain: estimating the transition matrix (MLE/Laplace/bootstrap CI) +
    long-run analytics (the stationary distribution, mean first passage times, irreducibility,
    period).

    Category 06-volatility-regimes; memory class ``heavy``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        data: [series_codes, required] State sequence: character codes (or int_array). Length>=2,
            >=2 distinct, without NA.
        method: [enum, optional] Transition matrix estimator (default mle· bootstrap=STOCHASTIC CI).
            Default ``'mle'``.
        laplacian: [number, optional] Laplacian smoothing pseudo-count (>=0, default 0· effective
            for method='laplace'). Default ``0``.
        confidencelevel: [number, optional] CI confidence level in (0,1) (default 0.95). Default
            ``0.95``.
        nboot: [integer, optional] Bootstrap replicates for method='bootstrap' (positive integer,
            default 10). Default ``10``.
        sanitize: [boolean, optional] Convert NaN rows to uniform (default False). Default
            ``False``.
        seed: [integer, optional] Reproducibility seed for method='bootstrap' (default 2025).
            Default ``2025``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mc_fit: not implemented."
    )


def mc_analytics(
    *,
    object: Any,
) -> dict[str, Any]:
    """Node ``mc_analytics`` -- method card #164.

    Discrete-time Markov chain: estimating the transition matrix (MLE/Laplace/bootstrap CI) +
    long-run analytics (the stationary distribution, mean first passage times, irreducibility,
    period).

    Category 06-volatility-regimes; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a 'markovchain' object (from mc_fit).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mc_analytics: not implemented."
    )
