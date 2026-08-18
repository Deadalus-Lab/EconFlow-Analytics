# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``bayesian_change_point`` -- METHOD-SELECTION card #214.

#214 Bayesian change point (the Barry-Hartigan Product-Partition Model, MCMC)

Category 19-business-cycle-dating; module ``bayesian_change_point``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c19_business_cycle_dating import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "detect_change_points",
    "NODE_META",
    "wire_model",
]


def detect_change_points(
    *,
    y: pd.Series,
    p0: float | None = None,
    w0: float | None = None,
    burnin: int | None = None,
    mcmc: int | None = None,
    threshold: float | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``detect_change_points`` -- METHOD-SELECTION card #214.

    Bayesian change point (the Barry-Hartigan Product-Partition Model, MCMC).

    Category 19-business-cycle-dating; memory class ``mcmc``.

    Args:
        y: [series_handle, required] Handle to a univariate numeric series (ts); without NA/Inf;
            length >= 4.
        p0: [number, optional] Prior probability of a change U(0,p0) per position; ∈ (0,1] (default
            0.2). Default ``0.2``.
        w0: [number, optional] Prior signal-to-noise ratio· ∈ (0,1] (default 0.2). Default ``0.2``.
        burnin: [integer, optional] Number of MCMC burnin iterations (default 50). Default ``50``.
        mcmc: [integer, optional] Number of MCMC iterations after burnin (default 500). Default
            ``500``.
        threshold: [number, optional] posterior.prob threshold for change-point detection; ∈ (0,1)
            (default 0.5). Default ``0.5``.
        seed: [integer, optional] Seed for MCMC reproducibility (default 20240719). Default
            ``20240719``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "detect_change_points: not implemented. The method card is in ./README.md."
    )
