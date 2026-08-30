# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``curve_bootstrapping`` -- method card #536.

#536 Zero-coupon bootstrapping and spline curve fitting from coupon bonds

Category 18-yield-curve; module ``curve_bootstrapping``.

Reference implementation: QuantLib.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c18_yield_curve import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "yc_bootstrap_curve",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def yc_bootstrap_curve(
    *,
    instruments: pd.DataFrame,
    method: (
        Literal[
            "bootstrap",
            "cubic_spline",
            "monotone_convex",
            "nelson_siegel",
            "svensson",
        ]
        | None
    ) = None,
    interpolation: Literal["zero_rate", "log_discount", "forward"] | None = None,
    day_count: Literal["act360", "act365", "thirty360", "actact"] | None = None,
) -> dict[str, Any]:
    """Node ``yc_bootstrap_curve`` -- method card #536.

    Zero-coupon bootstrapping and spline curve fitting from coupon bonds.

    Category 18-yield-curve; memory class ``light``.

    Registers its result under ``curve``, so a later node can consume it as a handle.

    Args:
        instruments: [df_handle, required] Instrument table: maturity, coupon, price or rate.
        method: [enum, optional] Construction method. Default ``'bootstrap'``.
        interpolation: [enum, optional] Interpolation variable. Default ``'log_discount'``.
        day_count: [enum, optional] Day-count convention. Default ``'act365'``.

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
        "yc_bootstrap_curve: not implemented."
    )
