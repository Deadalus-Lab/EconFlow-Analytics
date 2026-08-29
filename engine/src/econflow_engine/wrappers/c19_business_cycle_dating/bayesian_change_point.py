# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``bayesian_change_point`` -- method card #214.

#214 Bayesian change point (the Barry-Hartigan Product-Partition Model, MCMC)

Category 19-business-cycle-dating; module ``bayesian_change_point``.

Reference implementation: 10.1080/01621459.1993.10594323.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any

import pandas as pd

from econflow_engine.generated.args.c19_business_cycle_dating import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "detect_change_points",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


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
    """Node ``detect_change_points`` -- method card #214.

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
        "detect_change_points: not implemented."
    )
