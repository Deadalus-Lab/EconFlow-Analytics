# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``beast_bayesian_decomposition`` -- method card #186.

#186 BEAST — a Bayesian decomposition into trend + seasonality + change points with posterior change
    probabilities

Category 10-trend-cycle-statespace; module ``beast_bayesian_decomposition``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

from econflow_engine.generated.args.c10_trend_cycle_statespace import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "beast_changepoints",
    "beast_decompose",
    "NODE_META",
    "wire_model",
]


def beast_decompose(
    *,
    y: Sequence[float],
    season: Literal["harmonic", "dummy", "none"] | None = None,
    period: int | None = None,
    tcp_minmax: Sequence[int] | None = None,
    scp_minmax: Sequence[int] | None = None,
    mcmc_samples: int | None = None,
    mcmc_burnin: int | None = None,
    mcmc_chains: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``beast_decompose`` -- method card #186.

    BEAST — a Bayesian decomposition into trend + seasonality + change points with posterior change
    probabilities.

    Category 10-trend-cycle-statespace; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        y: [num_array, required] Regular (equally spaced) numeric series· without NA/Inf (hard
            gate).
        season: [enum, optional] Seasonality form· 'none' = trend-only (the period is ignored).
            Default ``'harmonic'``.
        period: [integer, optional] Seasonality period (>=2)· REQUIRED for harmonic/dummy· otherwise
            silent period-guess.
        tcp_minmax: [int_array, optional] [min,max] of the allowed number of trend change-points
            (non-negative integers, min<=max). Default ``[0, 10]``.
        scp_minmax: [int_array, optional] [min,max] of the allowed number of seasonal change-points
            (non-negative integers, min<=max). Default ``[0, 10]``.
        mcmc_samples: [integer, optional] MCMC samples per chain (keep it small, ~2000). Default
            ``2000``.
        mcmc_burnin: [integer, optional] MCMC burn-in samples (>=0). Default ``200``.
        mcmc_chains: [integer, optional] Number of MCMC chains (>=1· 1 for speed/determinism).
            Default ``1``.
        seed: [integer, optional] mcmc.seed for reproducibility (>=0)· same seed ⇒ identical trend.
            Default ``2025``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "beast_decompose: not implemented."
    )


def beast_changepoints(
    *,
    object: Any,
    component: Literal["trend", "season"] | None = None,
    threshold: float | None = None,
) -> dict[str, Any]:
    """Node ``beast_changepoints`` -- method card #186.

    BEAST — a Bayesian decomposition into trend + seasonality + change points with posterior change
    probabilities.

    Category 10-trend-cycle-statespace; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a fitted beast (output of beast_decompose.object).
        component: [enum, optional] Which component's change-points to extract· 'season' only if the
            fit had seasonality. Default ``'trend'``.
        threshold: [number, optional] Minimum posterior probability cpPr ∈ [0,1] for a change-point
            to be kept. Default ``0``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "beast_changepoints: not implemented."
    )
