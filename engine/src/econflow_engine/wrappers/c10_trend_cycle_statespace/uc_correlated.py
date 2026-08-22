# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``uc_correlated`` -- method card #482.

#482 Unobserved components with correlated trend and cycle innovations

Category 10-trend-cycle-statespace; module ``uc_correlated``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c10_trend_cycle_statespace import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "tc_uc_correlated",
    "NODE_META",
    "wire_model",
]


def tc_uc_correlated(
    *,
    y: pd.Series,
    cycle_order: int | None = None,
    restrict_correlation: bool | None = None,
    profile_rho: bool | None = None,
) -> dict[str, Any]:
    """Node ``tc_uc_correlated`` -- method card #482.

    Unobserved components with correlated trend and cycle innovations.

    Category 10-trend-cycle-statespace; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Series.
        cycle_order: [integer, optional] Autoregressive order of the cycle. Default ``2``.
        restrict_correlation: [boolean, optional] Impose zero correlation. Default ``False``.
        profile_rho: [boolean, optional] Return the profile likelihood in rho. Default ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "tc_uc_correlated: not implemented."
    )
