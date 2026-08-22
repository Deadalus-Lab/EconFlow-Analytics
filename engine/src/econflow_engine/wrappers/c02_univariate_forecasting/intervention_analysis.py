# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``intervention_analysis`` -- method card #409.

#409 Intervention analysis and transfer functions

Category 02-univariate-forecasting; module ``intervention_analysis``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c02_univariate_forecasting import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "uf_intervention",
    "NODE_META",
    "wire_model",
]


def uf_intervention(
    *,
    y: pd.Series,
    intervention_date: str,
    shape: Literal["step", "pulse", "ramp", "decaying_pulse"] | None = None,
    decay: float | None = None,
    order: Sequence[int] | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``uf_intervention`` -- method card #409.

    Intervention analysis and transfer functions.

    Category 02-univariate-forecasting; memory class ``light``.

    Args:
        y: [series_handle, required] Series.
        intervention_date: [string, required] Date the intervention begins.
        shape: [enum, optional] Intervention shape. Default ``'step'``.
        decay: [number, optional] Decay parameter for a gradual response. Default ``0.5``.
        order: [int_array, optional] ARIMA order. Default ``[1, 0, 0]``.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "uf_intervention: not implemented."
    )
