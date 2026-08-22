# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``panel_granger`` -- method card #570.

#570 Panel Granger non-causality: Dumitrescu-Hurlin

Category 24-panel-var; module ``panel_granger``.

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
    "pv_panel_granger",
    "NODE_META",
    "wire_model",
]


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
    """
    raise NotImplementedError(
        "pv_panel_granger: not implemented."
    )
