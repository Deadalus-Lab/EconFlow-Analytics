# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``bry_boschan`` -- method card #541.

#541 Monthly Bry-Boschan dating with smoothing and cycle statistics

Category 19-business-cycle-dating; module ``bry_boschan``.

Reference implementation: scipy.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c19_business_cycle_dating import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "bc_bry_boschan",
    "bc_cycle_statistics",
    "NODE_META",
    "wire_model",
]


def bc_bry_boschan(
    *,
    y: pd.Series,
    min_phase: int | None = None,
    min_cycle: int | None = None,
    smoothing: Literal["none", "mcd", "spencer", "henderson"] | None = None,
    end_censor: int | None = None,
) -> dict[str, Any]:
    """Node ``bc_bry_boschan`` -- method card #541.

    Monthly Bry-Boschan dating with smoothing and cycle statistics.

    Category 19-business-cycle-dating; memory class ``light``.

    Args:
        y: [series_handle, required] Series.
        min_phase: [integer, optional] Minimum phase duration in periods. Default ``5``.
        min_cycle: [integer, optional] Minimum cycle duration in periods. Default ``15``.
        smoothing: [enum, optional] Pre-dating smoother. Default ``'spencer'``.
        end_censor: [integer, optional] Periods excluded at each end. Default ``6``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bc_bry_boschan: not implemented."
    )


def bc_cycle_statistics(
    *,
    y: pd.Series,
    peaks: Sequence[int],
    troughs: Sequence[int],
) -> dict[str, Any]:
    """Node ``bc_cycle_statistics`` -- method card #541.

    Monthly Bry-Boschan dating with smoothing and cycle statistics.

    Category 19-business-cycle-dating; memory class ``light``.

    Args:
        y: [series_handle, required] Series.
        peaks: [int_array, required] Peak indices.
        troughs: [int_array, required] Trough indices.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bc_cycle_statistics: not implemented."
    )
