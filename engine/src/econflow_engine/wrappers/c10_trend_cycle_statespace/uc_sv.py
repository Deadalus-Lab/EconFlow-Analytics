# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``uc_sv`` -- method card #477.

#477 Unobserved components with stochastic volatility

Category 10-trend-cycle-statespace; module ``uc_sv``.

Reference implementation: pymc.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c10_trend_cycle_statespace import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "tc_uc_stochastic_volatility",
    "NODE_META",
    "wire_model",
]


def tc_uc_stochastic_volatility(
    *,
    y: pd.Series,
    draws: int | None = None,
    warmup: int | None = None,
    trend: Literal["local_level", "local_linear", "smooth_trend"] | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``tc_uc_stochastic_volatility`` -- method card #477.

    Unobserved components with stochastic volatility.

    Category 10-trend-cycle-statespace; memory class ``mcmc``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Series.
        draws: [integer, optional] Posterior draws. Default ``5000``.
        warmup: [integer, optional] Warm-up draws discarded. Default ``1000``.
        trend: [enum, optional] Trend specification. Default ``'local_level'``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "tc_uc_stochastic_volatility: not implemented."
    )
