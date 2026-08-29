# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``boosted_hp`` -- method card #480.

#480 Boosted Hodrick-Prescott filter

Category 10-trend-cycle-statespace; module ``boosted_hp``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c10_trend_cycle_statespace import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "tc_boosted_hp",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def tc_boosted_hp(
    *,
    y: pd.Series,
    lamb: float | None = None,
    stopping: Literal["bic", "aic", "adf", "max_iter"] | None = None,
    max_iter: int | None = None,
) -> dict[str, Any]:
    """Node ``tc_boosted_hp`` -- method card #480.

    Boosted Hodrick-Prescott filter.

    Category 10-trend-cycle-statespace; memory class ``light``.

    Args:
        y: [series_handle, required] Series.
        lamb: [number, optional] Smoothing parameter. Default ``1600.0``.
        stopping: [enum, optional] Stopping rule. Default ``'bic'``.
        max_iter: [integer, optional] Maximum boosting rounds. Default ``100``.

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
        "tc_boosted_hp: not implemented."
    )
