# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``implied_density_gar`` -- method card #498.

#498 Option-implied risk-neutral density as a growth-at-risk input

Category 12-distribution-risk; module ``implied_density_gar``.

Reference implementation: py-vollib.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c12_distribution_risk import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "dr_implied_density_input",
    "NODE_META",
    "wire_model",
]


def dr_implied_density_input(
    *,
    strikes: pd.Series,
    prices: pd.Series,
    forward: float,
    time_to_expiry: float,
    rate: float,
    quantiles: Sequence[float] | None = None,
    risk_premium: float | None = None,
) -> dict[str, Any]:
    """Node ``dr_implied_density_input`` -- method card #498.

    Option-implied risk-neutral density as a growth-at-risk input.

    Category 12-distribution-risk; memory class ``light``.

    Args:
        strikes: [series_handle, required] Strikes.
        prices: [series_handle, required] Option prices.
        forward: [number, required] Forward price.
        time_to_expiry: [number, required] Time to expiry in years.
        rate: [number, required] Risk-free rate.
        quantiles: [num_array, optional] Quantiles to extract. Default ``[0.05, 0.25, 0.5, 0.75,
            0.95]``.
        risk_premium: [number, optional] Adjustment applied to convert to physical. Default ``0.0``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "dr_implied_density_input: not implemented."
    )
