# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``risk_neutral_moments`` -- method card #344.

#344 Risk-neutral moments as uncertainty proxies

Category 40-option-implied-derivatives; module ``risk_neutral_moments``.

Reference implementation: scipy.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c40_option_implied_derivatives import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "opt_risk_neutral_moments",
    "NODE_META",
    "wire_model",
]


def opt_risk_neutral_moments(
    *,
    strikes: pd.Series,
    prices: pd.Series,
    option_type: pd.Series,
    forward: float,
    time_to_expiry: float,
    rate: float,
) -> dict[str, Any]:
    """Node ``opt_risk_neutral_moments`` -- method card #344.

    Risk-neutral moments as uncertainty proxies.

    Category 40-option-implied-derivatives; memory class ``light``.

    Args:
        strikes: [series_handle, required] Strikes.
        prices: [series_handle, required] Option prices.
        option_type: [series_handle, required] Option types.
        forward: [number, required] Forward price.
        time_to_expiry: [number, required] Time to expiry in years.
        rate: [number, required] Risk-free rate.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "opt_risk_neutral_moments: not implemented."
    )
