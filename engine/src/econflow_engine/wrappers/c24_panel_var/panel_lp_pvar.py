# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``panel_lp_pvar`` -- method card #571.

#571 Panel local projections with fixed effects and Driscoll-Kraay errors

Category 24-panel-var; module ``panel_lp_pvar``.

Reference implementation: localprojections.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c24_panel_var import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "pv_panel_lp",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def pv_panel_lp(
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
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``pv_panel_lp`` -- method card #571.

    Panel local projections with fixed effects and Driscoll-Kraay errors.

    Category 24-panel-var; memory class ``light``.

    Args:
        data: [df_handle, required] Panel data.
        y: [string, required] Response variable.
        shock: [string, required] Shock variable.
        unit: [string, required] Unit identifier.
        time: [string, required] Time identifier.
        controls: [series_codes, optional] Control columns.
        horizons: [integer, optional] Maximum horizon. Default ``20``.
        lags: [integer, optional] Lags included. Default ``4``.
        cov_type: [enum, optional] Covariance estimator. Default ``'driscoll_kraay'``.
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
        "pv_panel_lp: not implemented."
    )
