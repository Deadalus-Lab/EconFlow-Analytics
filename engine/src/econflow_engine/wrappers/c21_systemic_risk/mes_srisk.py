# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``mes_srisk`` -- method card #553.

#553 Marginal expected shortfall, SES and SRISK

Category 21-systemic-risk; module ``mes_srisk``.

Reference implementation: arch.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c21_systemic_risk import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "sr_mes_srisk",
    "NODE_META",
    "wire_model",
]


def sr_mes_srisk(
    *,
    returns: pd.DataFrame,
    market: pd.Series,
    liabilities: pd.Series | None = None,
    market_cap: pd.Series | None = None,
    crisis_decline: float | None = None,
    prudential_ratio: float | None = None,
    horizon: int | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``sr_mes_srisk`` -- method card #553.

    Marginal expected shortfall, SES and SRISK.

    Category 21-systemic-risk; memory class ``light``.

    Args:
        returns: [df_handle, required] Institution return panel.
        market: [series_handle, required] Market return.
        liabilities: [series_handle, optional] Book liabilities per institution.
        market_cap: [series_handle, optional] Market capitalisation per institution.
        crisis_decline: [number, optional] Assumed market decline defining the crisis. Default
            ``0.4``.
        prudential_ratio: [number, optional] Required capital ratio. Default ``0.08``.
        horizon: [integer, optional] Crisis horizon in days. Default ``126``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "sr_mes_srisk: not implemented."
    )
