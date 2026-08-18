# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``sequential_monte_carlo`` -- METHOD-SELECTION card #205.

#205 Sequential Monte Carlo / particle filters for non-linear/non-Gaussian state-space models
    (bootstrap / auxiliary / Liu-West / ensemble Kalman)

Category 14-bayesian-toolkit; module ``sequential_monte_carlo``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

from econflow_engine.generated.args.c14_bayesian_toolkit import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "smc_filter",
    "NODE_META",
    "wire_model",
]


def smc_filter(
    *,
    code: str,
    inits: Any,
    latentNodes: Sequence[str],
    seed: int,
    constants: Any | None = None,
    data: Any | None = None,
    method: Literal["bootstrap", "auxiliary", "liuWest", "ensembleKF"] | None = None,
    nParticles: int | None = None,
    params: Sequence[str] | None = None,
    thresh: float | None = None,
    lookahead: Literal["simulate", "mean"] | None = None,
    d: float | None = None,
    probs: Sequence[float] | None = None,
) -> dict[str, Any]:
    """Node ``smc_filter`` -- METHOD-SELECTION card #205.

    Sequential Monte Carlo / particle filters for non-linear/non-Gaussian state-space models
    (bootstrap / auxiliary / Liu-West / ensemble Kalman).

    Category 14-bayesian-toolkit; memory class ``light``.

    Args:
        code: [string, required] BUGS-style state-space model definition AS A STRING (parse ONLY,
            injection-safe — no eval).
        inits: [raw_handle, required] Handle to a named list of initial values (covers ALL the
            top-level stochastic parameters).
        latentNodes: [series_codes, required] Non-empty character vector of stochastic latent nodes
            in time order (e.g. ['x'] or ['x[1:10]']).
        seed: [integer, required] REQUIRED single integer seed (reproducibility· set.seed before the
            run).
        constants: [raw_handle, optional] Handle to a named list of constants/dimensions (e.g. Tn)·
            optional.
        data: [raw_handle, optional] Handle to a named list of observations (WITHOUT NA -> silent
            MISSING-node imputation).
        method: [enum, optional] Particle filter· default bootstrap. Only bootstrap/auxiliary return
            logLik+ESS.
        nParticles: [integer, optional] Number of particles m for run(m) (integer >= 1· default
            1000). Default ``1000``.
        params: [series_codes, optional] (liuWest ONLY) top-level parameters to estimate· empty ->
            auto (top-level except latent).
        thresh: [number, optional] (ONLY bootstrap) resampling threshold· MUST be == 1 (resample at
            every step => equally weighted mvEWSamples => correct per-time summaries)· thresh<1 is
            blocked. Default ``1``.
        lookahead: [enum, optional] (auxiliary ONLY) lookahead for the auxiliary weights· default
            simulate.
        d: [number, optional] (liuWest ONLY) discount factor in (0,1) — close to but NOT above 1
            (default 0.99). Default ``0.99``.
        probs: [num_array, optional] Quantiles for the per-time filtered summaries (default
            0.025/0.25/0.5/0.75/0.975).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "smc_filter: not implemented. The method card is in ./README.md."
    )
