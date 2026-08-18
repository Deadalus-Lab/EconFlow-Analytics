# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``staggered_did`` -- METHOD-SELECTION card #36.

#36 Staggered DiD (Callaway-Sant'Anna)

Category 07-causality-policy; module ``staggered_did``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c07_causality_policy import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "wrap_aggte",
    "wrap_att_gt",
    "NODE_META",
    "wire_model",
]


def wrap_att_gt(
    *,
    yname: str,
    tname: str,
    gname: str,
    idname: str | None = None,
    xformla: str | None = None,
    data: pd.DataFrame,
    panel: bool | None = None,
    control_group: Literal["nevertreated", "notyettreated"] | None = None,
    est_method: Literal["dr", "ipw", "reg"] | None = None,
    base_period: Literal["varying", "universal"] | None = None,
    bstrap: bool | None = None,
    biters: int | None = None,
    cband: bool | None = None,
    alp: float | None = None,
) -> dict[str, Any]:
    """Node ``wrap_att_gt`` -- METHOD-SELECTION card #36.

    Staggered DiD (Callaway-Sant'Anna).

    Category 07-causality-policy; memory class ``heavy``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        yname: [string, required] Outcome column name.
        tname: [string, required] Time column name (period).
        gname: [string, required] Cohort/first-treatment-period column name (0 = never-treated).
        idname: [string, optional] Unit id column name (required when panel=True).
        xformla: [formula, optional] Covariate formula, e.g. '~ x1' (default: none).
        data: [df_handle, required] Handle to a long-format panel DataFrame.
        panel: [boolean, optional] True=panel (default), False=repeated cross-sections. Default
            ``True``.
        control_group: [enum, optional] Control group (default nevertreated).
        est_method: [enum, optional] Estimator: doubly-robust/IPW/regression (default dr).
        base_period: [enum, optional] Base period for the event study (default varying).
        bstrap: [boolean, optional] Bootstrap inference (default True). Default ``True``.
        biters: [integer, optional] Bootstrap iterations (default 1000). Default ``1000``.
        cband: [boolean, optional] Uniform confidence bands (default True). Default ``True``.
        alp: [number, optional] Significance level (default 0.05). Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "wrap_att_gt: not implemented. The method card is in ./README.md."
    )


def wrap_aggte(
    *,
    MP: Any,
    type: Literal["dynamic", "simple", "group", "calendar"] | None = None,
    min_e: float | None = None,
    max_e: float | None = None,
    na_rm: bool | None = None,
) -> dict[str, Any]:
    """Node ``wrap_aggte`` -- METHOD-SELECTION card #36.

    Staggered DiD (Callaway-Sant'Anna).

    Category 07-causality-policy; memory class ``light``.

    Args:
        MP: [raw_handle, required] Handle to an att_gt object (from wrap_att_gt).
        type: [enum, optional] Aggregation: event-study/overall/cohort/calendar (default dynamic).
        min_e: [number, optional] Minimum event time (default -Inf).
        max_e: [number, optional] Maximum event time (default Inf).
        na_rm: [boolean, optional] Drop NA ATT(g,t) (default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "wrap_aggte: not implemented. The method card is in ./README.md."
    )
