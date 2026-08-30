# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``nonparametric_time_varying`` -- method card #212.

#212 Nonparametric time-varying yield curve / discount function estimation from coupon-bond
    cash-flow data (the Koo-La Vecchia-Linton kernel estimator)

Category 18-yield-curve; module ``nonparametric_time_varying``.

Reference implementation: 10.1016/j.jeconom.2020.04.014.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

import pandas as pd

from econflow_engine.generated.args.c18_yield_curve import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ycnp_estimate",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def ycnp_estimate(
    *,
    data: pd.DataFrame,
    x: Sequence[str],
    tau: Sequence[float] | None = None,
    span_x: float | None = None,
    hx: Sequence[float] | None = None,
    ht: Sequence[float] | None = None,
    smooth: bool | None = None,
) -> dict[str, Any]:
    """Node ``ycnp_estimate`` -- method card #212.

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

    Gates:
        None declared. The ``precondition_gates`` field of this method card is empty; the checks a
        body must run are named here once the field carries them.

    .. gen_wrappers: end of generated docstring

    Examples:
        None yet. This node raises ``NotImplementedError``; its example is written with its body and
        belongs to whoever writes it.

    Note:
        The implementation note is written with the body: the library functions it calls and their
        versions, what the method leaves out, and every gate added with the source that requires it.
    """
    raise NotImplementedError(
        "ycnp_estimate: not implemented."
    )
