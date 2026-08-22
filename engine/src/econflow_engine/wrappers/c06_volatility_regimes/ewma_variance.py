# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``ewma_variance`` -- method card #438.

#438 EWMA and RiskMetrics variance

Category 06-volatility-regimes; module ``ewma_variance``.

Reference implementation: arch.

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
    "vr_ewma",
    "NODE_META",
    "wire_model",
]


def vr_ewma(
    *,
    y: pd.Series,
    lambda_: float | None = None,
    initial: Literal["sample_variance", "first_observation", "backcast"] | None = None,
) -> dict[str, Any]:
    """Node ``vr_ewma`` -- method card #438.

    EWMA and RiskMetrics variance.

    Category 06-volatility-regimes; memory class ``light``.

    Args:
        y: [series_handle, required] Return series.
        lambda_: [number, optional] Decay factor. Default ``0.94``.
        initial: [enum, optional] Initialisation of the recursion. Default ``'sample_variance'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "vr_ewma: not implemented."
    )
