# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``coherent_forecast_reconciliation`` -- METHOD-SELECTION card #208.

#208 Coherent forecast reconciliation (cross-sectional / temporal / cross-temporal) via an optimal
    least-squares projection (MinT: ols/str/wls/shr/sam)

Category 17-forecast-combination; module ``coherent_forecast_reconciliation``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c17_forecast_combination import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "foreco_reconcile",
    "NODE_META",
    "wire_model",
]


def foreco_reconcile(
    *,
    type: Literal["cs", "te", "ct"],
    base: np.ndarray,
    agg_mat: np.ndarray | None = None,
    agg_order: Sequence[int] | None = None,
    comb: str | None = None,
    tew: Literal["sum", "avg", "first", "last"] | None = None,
    approach: Literal["proj", "strc", "proj_osqp", "strc_osqp"] | None = None,
    res: np.ndarray | None = None,
    nn: Literal["none", "osqp", "sntz", "bpv", "nfca", "nnic"] | None = None,
) -> dict[str, Any]:
    """Node ``foreco_reconcile`` -- METHOD-SELECTION card #208.

    Coherent forecast reconciliation (cross-sectional / temporal / cross-temporal) via an optimal
    least-squares projection (MinT: ols/str/wls/shr/sam).

    Category 17-forecast-combination; memory class ``light``.

    Args:
        type: [enum, required] Reconciliation framework: 'cs' cross-sectional (csrec; agg_mat), 'te'
            temporal (terec; agg_order), 'ct' cross-temporal (ctrec; agg_mat+agg_order).
        base: [matrix_handle, required] Handle to the base forecasts. cs: (h x n) matrix, columns
            [upper..., bottom...] (n=n_a+n_b). te: (h*(k*+m)) vector lowest->highest freq. ct: (n x
            h*(k*+m)) matrix.
        agg_mat: [matrix_handle, optional] Handle to the (n_a x n_b) aggregation matrix (map
            bottom->upper). Required for type='cs' and 'ct'.
        agg_order: [int_array, optional] Max temporal aggregation m (e.g. 4 quarterly->annual, 12
            monthly) or a vector of factors of m. Required for 'te'/'ct'.
        comb: [string, optional] Covariance/MinT method (closed set PER type). cs:
            ols/str/wls/shr/oasd/sam. te: ols/str/wlsh/wlsv/acov/strar1/sar1/har1/shr/sam. ct:
            ols/str/csstr/testr/wlsh/wlsv/acov/bdshr/bdsam/Sshr/Ssam/shr/sam/hbshr/hbsam/bshr/bsam/
            hshr/hsam. WLS/GLS/MinT require 'res'. Default 'ols'. Default ``'ols'``.
        tew: [enum, optional] Type of temporal aggregation (te/ct): sum/avg/first/last (default
            sum).
        approach: [enum, optional] Approach: proj(ection)/strc(structural)/*_osqp (default proj).
        res: [matrix_handle, optional] Handle to in-sample residuals/validation errors (required for
            WLS/GLS/MinT comb). cs: (N x n) matrix. te: (N*(k*+m)) vector. ct: (n x N*(k*+m))
            matrix.
        nn: [enum, optional] Non-negativity algorithm for reconciled forecasts (default 'none').

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "foreco_reconcile: not implemented. The method card is in ./README.md."
    )
