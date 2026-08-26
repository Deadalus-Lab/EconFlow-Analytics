# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``cox_ph`` -- method card #259.

#259 Cox proportional-hazards regression with time-varying covariates and stratification

Category 30-duration-survival; module ``cox_ph``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c30_duration_survival import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "srv_cox_fit",
    "srv_cox_predict",
    "srv_cox_timevarying",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def srv_cox_fit(
    *,
    data: pd.DataFrame,
    time: str,
    event: str,
    covariates: Sequence[str] | None = None,
    strata: Sequence[str] | None = None,
    ties: Literal["efron", "breslow"] | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``srv_cox_fit`` -- method card #259.

    Cox proportional-hazards regression with time-varying covariates and stratification.

    Category 30-duration-survival; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] Table holding the durations, the event indicator and the
            covariates.
        time: [string, required] Column holding the observed duration.
        event: [string, required] Column holding the event indicator.
        covariates: [series_codes, optional] Covariate column names.
        strata: [series_codes, optional] Columns to stratify the baseline hazard on.
        ties: [enum, optional] Handler for tied event times. Default ``'efron'``.
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
        "srv_cox_fit: not implemented."
    )


def srv_cox_predict(
    *,
    fit: Any,
    newdata: pd.DataFrame | None = None,
    what: Literal["survival", "cumhazard", "linear_predictor", "hazard_ratio"] | None = None,
) -> dict[str, Any]:
    """Node ``srv_cox_predict`` -- method card #259.

    Cox proportional-hazards regression with time-varying covariates and stratification.

    Category 30-duration-survival; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a fitted Cox model.
        newdata: [df_handle, optional] Covariate rows to predict for; omitted = the training rows.
        what: [enum, optional] Quantity to return. Default ``'survival'``.

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
        "srv_cox_predict: not implemented."
    )


def srv_cox_timevarying(
    *,
    data: pd.DataFrame,
    start: str,
    stop: str,
    event: str,
    covariates: Sequence[str] | None = None,
    id: str,
) -> dict[str, Any]:
    """Node ``srv_cox_timevarying`` -- method card #259.

    Cox proportional-hazards regression with time-varying covariates and stratification.

    Category 30-duration-survival; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] Counting-process table: one row per unit per interval.
        start: [string, required] Column holding the interval start.
        stop: [string, required] Column holding the interval end.
        event: [string, required] Column holding the event indicator for the interval.
        covariates: [series_codes, optional] Covariate column names.
        id: [string, required] Column identifying the unit.

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
        "srv_cox_timevarying: not implemented."
    )
