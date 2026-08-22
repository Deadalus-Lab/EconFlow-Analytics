# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``panel_local_projections`` -- method card #431.

#431 Panel and group local projections with Driscoll-Kraay errors

Category 04-structural-shocks; module ``panel_local_projections``.

Reference implementation: localprojections.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c04_structural_shocks import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ss_panel_lp",
    "NODE_META",
    "wire_model",
]


def ss_panel_lp(
    *,
    data: pd.DataFrame,
    y: str,
    shock: str,
    unit: str,
    time: str,
    controls: Sequence[str] | None = None,
    horizons: int | None = None,
    lags: int | None = None,
    cov_type: Literal["driscoll_kraay", "cluster", "robust"] | None = None,
    group: str | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``ss_panel_lp`` -- method card #431.

    Panel and group local projections with Driscoll-Kraay errors.

    Category 04-structural-shocks; memory class ``light``.

    Args:
        data: [df_handle, required] Panel data.
        y: [string, required] Response column.
        shock: [string, required] Shock column.
        unit: [string, required] Unit identifier.
        time: [string, required] Time identifier.
        controls: [series_codes, optional] Control columns.
        horizons: [integer, optional] Maximum horizon. Default ``20``.
        lags: [integer, optional] Lags included. Default ``4``.
        cov_type: [enum, optional] Covariance estimator. Default ``'driscoll_kraay'``.
        group: [string, optional] Column defining groups for separate responses.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ss_panel_lp: not implemented."
    )
