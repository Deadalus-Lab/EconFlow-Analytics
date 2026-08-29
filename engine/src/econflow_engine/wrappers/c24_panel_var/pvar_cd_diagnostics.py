# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``pvar_cd_diagnostics`` -- method card #572.

#572 Cross-section-dependence diagnostics for panel VAR

Category 24-panel-var; module ``pvar_cd_diagnostics``.

Reference implementation: statsmodels.

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
    "pv_cd_diagnostics",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def pv_cd_diagnostics(
    *,
    residuals: pd.DataFrame,
    unit: str,
    time: str,
    n_factors: int | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``pv_cd_diagnostics`` -- method card #572.

    Cross-section-dependence diagnostics for panel VAR.

    Category 24-panel-var; memory class ``light``.

    Args:
        residuals: [df_handle, required] Panel VAR residuals.
        unit: [string, required] Unit identifier.
        time: [string, required] Time identifier.
        n_factors: [integer, optional] Factors to extract from the residuals. Default ``3``.
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
        "pv_cd_diagnostics: not implemented."
    )
