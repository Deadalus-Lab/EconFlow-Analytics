# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``staggered_did`` -- method cards #36, #445.

#36 Staggered DiD (Callaway-Sant'Anna)
#445 Heterogeneity-robust staggered DiD: Sun-Abraham, ETWFE, stacked, did2s and LP-DiD

Category 07-causality-policy; module ``staggered_did``.

Reference implementation: diff-diff.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c07_causality_policy import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "cp_bacon_decomposition",
    "cp_staggered_did",
    "did_aggregate_att",
    "did_att_gt",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def did_att_gt(
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
    """Node ``did_att_gt`` -- method card #36.

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
        "did_att_gt: not implemented."
    )


def did_aggregate_att(
    *,
    MP: Any,
    type: Literal["dynamic", "simple", "group", "calendar"] | None = None,
    min_e: float | None = None,
    max_e: float | None = None,
    na_rm: bool | None = None,
) -> dict[str, Any]:
    """Node ``did_aggregate_att`` -- method card #36.

    Staggered DiD (Callaway-Sant'Anna).

    Category 07-causality-policy; memory class ``light``.

    Args:
        MP: [raw_handle, required] Handle to an att_gt object (from did_att_gt).
        type: [enum, optional] Aggregation: event-study/overall/cohort/calendar (default dynamic).
        min_e: [number, optional] Minimum event time (default -Inf).
        max_e: [number, optional] Maximum event time (default Inf).
        na_rm: [boolean, optional] Drop NA ATT(g,t) (default False). Default ``False``.

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
        "did_aggregate_att: not implemented."
    )


def cp_staggered_did(
    *,
    data: pd.DataFrame,
    outcome: str,
    unit: str,
    time: str,
    cohort: str,
    estimator: (
        Literal[
            "sun_abraham",
            "etwfe",
            "stacked",
            "did2s",
            "lp_did",
            "callaway_santanna",
        ]
        | None
    ) = None,
    control_group: Literal["never_treated", "not_yet_treated"] | None = None,
    covariates: Sequence[str] | None = None,
    cluster: str | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``cp_staggered_did`` -- method card #445.

    Heterogeneity-robust staggered DiD: Sun-Abraham, ETWFE, stacked, did2s and LP-DiD.

    Category 07-causality-policy; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] Panel data.
        outcome: [string, required] Outcome column.
        unit: [string, required] Unit identifier.
        time: [string, required] Time identifier.
        cohort: [string, required] Column holding the first treatment period.
        estimator: [enum, optional] Estimator. Default ``'sun_abraham'``.
        control_group: [enum, optional] Comparison group. Default ``'not_yet_treated'``.
        covariates: [series_codes, optional] Covariate columns.
        cluster: [string, optional] Clustering variable.
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
        "cp_staggered_did: not implemented."
    )


def cp_bacon_decomposition(
    *,
    data: pd.DataFrame,
    outcome: str,
    unit: str,
    time: str,
    treatment: str,
) -> dict[str, Any]:
    """Node ``cp_bacon_decomposition`` -- method card #445.

    Heterogeneity-robust staggered DiD: Sun-Abraham, ETWFE, stacked, did2s and LP-DiD.

    Category 07-causality-policy; memory class ``light``.

    Args:
        data: [df_handle, required] Panel data.
        outcome: [string, required] Outcome column.
        unit: [string, required] Unit identifier.
        time: [string, required] Time identifier.
        treatment: [string, required] Treatment indicator column.

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
        "cp_bacon_decomposition: not implemented."
    )
