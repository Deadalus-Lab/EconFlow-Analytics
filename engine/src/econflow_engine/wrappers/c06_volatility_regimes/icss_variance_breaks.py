# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``icss_variance_breaks`` -- method card #441.

#441 ICSS variance change-point detection

Category 06-volatility-regimes; module ``icss_variance_breaks``.

Reference implementation: ruptures.

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
    "vr_variance_breaks",
    "NODE_META",
    "wire_model",
]


def vr_variance_breaks(
    *,
    y: pd.Series,
    method: Literal["icss", "icss_corrected", "binseg", "pelt", "dynp"] | None = None,
    penalty: float | None = None,
    max_breaks: int | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``vr_variance_breaks`` -- method card #441.

    ICSS variance change-point detection.

    Category 06-volatility-regimes; memory class ``light``.

    Args:
        y: [series_handle, required] Return series.
        method: [enum, optional] Detection method. Default ``'icss'``.
        penalty: [number, optional] Penalty for the segmentation methods.
        max_breaks: [integer, optional] Maximum breaks considered. Default ``10``.
        alpha: [number, optional] Significance level. Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "vr_variance_breaks: not implemented."
    )
