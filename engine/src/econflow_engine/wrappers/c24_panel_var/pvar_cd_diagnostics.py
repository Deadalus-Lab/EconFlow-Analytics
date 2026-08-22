# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``pvar_cd_diagnostics`` -- method card #572.

#572 Cross-section-dependence diagnostics for panel VAR

Category 24-panel-var; module ``pvar_cd_diagnostics``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c24_panel_var import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "pv_cd_diagnostics",
    "NODE_META",
    "wire_model",
]


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
    """
    raise NotImplementedError(
        "pv_cd_diagnostics: not implemented."
    )
