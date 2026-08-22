# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``multicollinearity`` -- method card #397.

#397 Multicollinearity: variance inflation, tolerance and Belsley condition indices

Category 01-preparation-prechecks; module ``multicollinearity``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c01_preparation_prechecks import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "pp_condition_indices",
    "pp_vif",
    "NODE_META",
    "wire_model",
]


def pp_vif(
    *,
    x: pd.DataFrame,
    threshold: float | None = None,
) -> dict[str, Any]:
    """Node ``pp_vif`` -- method card #397.

    Multicollinearity: variance inflation, tolerance and Belsley condition indices.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [df_handle, required] Regressor table.
        threshold: [number, optional] VIF above which a regressor is flagged. Default ``10.0``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "pp_vif: not implemented."
    )


def pp_condition_indices(
    *,
    x: pd.DataFrame,
    scale: bool | None = None,
    threshold: float | None = None,
) -> dict[str, Any]:
    """Node ``pp_condition_indices`` -- method card #397.

    Multicollinearity: variance inflation, tolerance and Belsley condition indices.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [df_handle, required] Regressor table.
        scale: [boolean, optional] Scale columns to unit length first. Default ``True``.
        threshold: [number, optional] Condition index above which a dependency is flagged. Default
            ``30.0``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "pp_condition_indices: not implemented."
    )
