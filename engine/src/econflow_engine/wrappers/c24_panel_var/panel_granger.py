# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``panel_granger`` -- method card #570.

#570 Panel Granger non-causality: Dumitrescu-Hurlin

Category 24-panel-var; module ``panel_granger``.

Reference implementation: 10.1016/j.econmod.2012.02.014.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any

import pandas as pd

from econflow_engine.generated.args.c24_panel_var import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "pv_panel_granger",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def pv_panel_granger(
    *,
    data: pd.DataFrame,
    y: str,
    x: str,
    unit: str,
    time: str,
    lags: int | None = None,
    nboot: int | None = None,
    seed: int | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``pv_panel_granger`` -- method card #570.

    Panel Granger non-causality: Dumitrescu-Hurlin.

    Category 24-panel-var; memory class ``heavy``.

    Args:
        data: [df_handle, required] Panel data.
        y: [string, required] Dependent variable.
        x: [string, required] Potential causal variable.
        unit: [string, required] Unit identifier.
        time: [string, required] Time identifier.
        lags: [integer, optional] Lag order. Default ``1``.
        nboot: [integer, optional] Number of bootstrap replications. Default ``0``.
        seed: [integer, optional] Seed for the random number generator.
        alpha: [number, optional] Significance level. Default ``0.05``.

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
        "pv_panel_granger: not implemented."
    )
