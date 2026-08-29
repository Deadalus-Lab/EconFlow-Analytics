# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``heterogeneous_panel`` -- method card #459.

#459 Mean group, pooled mean group and common correlated effects

Category 08-panel-data; module ``heterogeneous_panel``.

Reference implementation: 10.1016/0304-4076(94)01644-F.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c08_panel_data import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "pd_heterogeneous_panel",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def pd_heterogeneous_panel(
    *,
    data: pd.DataFrame,
    formula: str,
    unit: str,
    time: str,
    estimator: (
        Literal[
            "mean_group",
            "pooled_mean_group",
            "cce_mean_group",
            "cce_pooled",
        ]
        | None
    ) = None,
    trim: float | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``pd_heterogeneous_panel`` -- method card #459.

    Mean group, pooled mean group and common correlated effects.

    Category 08-panel-data; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] Panel data.
        formula: [formula, required] Model formula.
        unit: [string, required] Unit identifier.
        time: [string, required] Time identifier.
        estimator: [enum, optional] Estimator. Default ``'mean_group'``.
        trim: [number, optional] Trimming of outlying unit estimates. Default ``0.0``.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

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
        "pd_heterogeneous_panel: not implemented."
    )
