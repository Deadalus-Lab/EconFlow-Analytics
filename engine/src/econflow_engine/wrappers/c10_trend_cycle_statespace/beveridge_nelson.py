# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``beveridge_nelson`` -- method card #476.

#476 Beveridge-Nelson decomposition and the BN filter

Category 10-trend-cycle-statespace; module ``beveridge_nelson``.

Reference implementation: 10.1016/0304-3932(81)90040-4.

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
    "tc_beveridge_nelson",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def tc_beveridge_nelson(
    *,
    y: pd.Series,
    order: Sequence[int] | None = None,
    filter: bool | None = None,
    delta: float | None = None,
) -> dict[str, Any]:
    """Node ``tc_beveridge_nelson`` -- method card #476.

    Beveridge-Nelson decomposition and the BN filter.

    Category 10-trend-cycle-statespace; memory class ``light``.

    Args:
        y: [series_handle, required] Series, usually in logs.
        order: [int_array, optional] ARIMA order; omitted = selected.
        filter: [boolean, optional] Use the BN filter with a persistence prior. Default ``False``.
        delta: [number, optional] Persistence prior for the BN filter. Default ``0.05``.

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
        "tc_beveridge_nelson: not implemented."
    )
