# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``advanced_sv`` -- method card #443.

#443 Advanced stochastic volatility: log-normal, Heston and rough volatility calibration

Category 06-volatility-regimes; module ``advanced_sv``.

Reference implementation: stochvolmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c06_volatility_regimes import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "vr_stochastic_volatility",
    "NODE_META",
    "wire_model",
]


def vr_stochastic_volatility(
    *,
    y: pd.Series,
    model: Literal["lognormal", "heston", "rough_bergomi"] | None = None,
    method: Literal["mcmc", "particle_filter", "method_of_moments"] | None = None,
    draws: int | None = None,
    warmup: int | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``vr_stochastic_volatility`` -- method card #443.

    Advanced stochastic volatility: log-normal, Heston and rough volatility calibration.

    Category 06-volatility-regimes; memory class ``mcmc``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Return series.
        model: [enum, optional] Model family. Default ``'lognormal'``.
        method: [enum, optional] Estimation method. Default ``'mcmc'``.
        draws: [integer, optional] Posterior draws. Default ``5000``.
        warmup: [integer, optional] Warm-up draws discarded. Default ``1000``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "vr_stochastic_volatility: not implemented."
    )
