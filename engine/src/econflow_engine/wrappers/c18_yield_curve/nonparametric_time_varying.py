# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``nonparametric_time_varying`` -- METHOD-SELECTION card #212.

#212 Nonparametric time-varying yield curve / discount function estimation from coupon-bond
    cash-flow data (the Koo-La Vecchia-Linton kernel estimator)

Category 18-yield-curve; module ``nonparametric_time_varying``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c18_yield_curve import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ycevo_estimate",
    "NODE_META",
    "wire_model",
]


def ycevo_estimate(
    *,
    data: pd.DataFrame,
    x: Sequence[str],
    tau: Sequence[float] | None = None,
    span_x: float | None = None,
    hx: Sequence[float] | None = None,
    ht: Sequence[float] | None = None,
    smooth: bool | None = None,
) -> dict[str, Any]:
    """Node ``ycevo_estimate`` -- METHOD-SELECTION card #212.

    Nonparametric time-varying yield curve / discount function estimation from coupon-bond cash-flow
    data (the Koo-La Vecchia-Linton kernel estimator).

    Category 18-yield-curve; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a bond cash-flow panel with columns qdate(Date), id,
            price, tupq(>0, days), pdint.
        x: [series_codes, required] Estimation time points as dates 'YYYY-MM-DD' (same class/range
            as qdate).
        tau: [num_array, optional] Maturity grid in years (>0); default None = the package's
            automatic grid.
        span_x: [number, optional] Half-width of the kernel time window (default 60; ignored if hx
            is given). Default ``60``.
        hx: [num_array, optional] Bandwidths per point x (positive; length = length(x)); overrides
            span_x.
        ht: [num_array, optional] Bandwidths per maturity tau (positive; length = length(tau);
            requires explicit tau).
        smooth: [boolean, optional] loess smoothing of the curve with respect to tau (default False
            = raw estimator points). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ycevo_estimate: not implemented. The method card is in ./README.md."
    )
