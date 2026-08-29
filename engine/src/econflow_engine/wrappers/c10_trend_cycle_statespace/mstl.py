# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``mstl`` -- method card #478.

#478 MSTL and robust multiple-seasonality decomposition

Category 10-trend-cycle-statespace; module ``mstl``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

import pandas as pd

from econflow_engine.generated.args.c10_trend_cycle_statespace import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "tc_mstl",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def tc_mstl(
    *,
    y: pd.Series,
    periods: Sequence[int],
    robust: bool | None = None,
    seasonal_smoother: Sequence[int] | None = None,
    iterate: int | None = None,
) -> dict[str, Any]:
    """Node ``tc_mstl`` -- method card #478.

    MSTL and robust multiple-seasonality decomposition.

    Category 10-trend-cycle-statespace; memory class ``light``.

    Args:
        y: [series_handle, required] Series.
        periods: [int_array, required] Seasonal periods to extract.
        robust: [boolean, optional] Use outlier-resistant weights. Default ``True``.
        seasonal_smoother: [int_array, optional] Seasonal smoother length per period.
        iterate: [integer, optional] Outer iterations. Default ``2``.

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
        "tc_mstl: not implemented."
    )
