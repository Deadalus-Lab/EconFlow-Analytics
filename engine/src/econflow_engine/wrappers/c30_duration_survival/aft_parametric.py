# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``aft_parametric`` -- method card #260.

#260 Parametric accelerated-failure-time models: Weibull, log-normal, log-logistic and exponential

Category 30-duration-survival; module ``aft_parametric``.

Reference implementation: lifelines.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c30_duration_survival import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "srv_aft_compare",
    "srv_aft_fit",
    "srv_aft_predict",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def srv_aft_fit(
    *,
    data: pd.DataFrame,
    time: str,
    event: str,
    covariates: Sequence[str] | None = None,
    distribution: Literal["weibull", "lognormal", "loglogistic", "exponential"] | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``srv_aft_fit`` -- method card #260.

    Parametric accelerated-failure-time models: Weibull, log-normal, log-logistic and exponential.

    Category 30-duration-survival; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] Table holding the durations, the event indicator and the
            covariates.
        time: [string, required] Column holding the observed duration.
        event: [string, required] Column holding the event indicator.
        covariates: [series_codes, optional] Covariate column names.
        distribution: [enum, optional] Failure-time distribution. Default ``'weibull'``.
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
        "srv_aft_fit: not implemented."
    )


def srv_aft_compare(
    *,
    data: pd.DataFrame,
    time: str,
    event: str,
    covariates: Sequence[str] | None = None,
    criterion: Literal["aic", "bic"] | None = None,
) -> dict[str, Any]:
    """Node ``srv_aft_compare`` -- method card #260.

    Parametric accelerated-failure-time models: Weibull, log-normal, log-logistic and exponential.

    Category 30-duration-survival; memory class ``light``.

    Args:
        data: [df_handle, required] Table holding the durations, the event indicator and the
            covariates.
        time: [string, required] Column holding the observed duration.
        event: [string, required] Column holding the event indicator.
        covariates: [series_codes, optional] Covariate column names.
        criterion: [enum, optional] Information criterion used to rank the families. Default
            ``'aic'``.

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
        "srv_aft_compare: not implemented."
    )


def srv_aft_predict(
    *,
    fit: Any,
    newdata: pd.DataFrame | None = None,
    what: Literal["survival", "quantile", "mean", "median"] | None = None,
    q: float | None = None,
) -> dict[str, Any]:
    """Node ``srv_aft_predict`` -- method card #260.

    Parametric accelerated-failure-time models: Weibull, log-normal, log-logistic and exponential.

    Category 30-duration-survival; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a fitted parametric model.
        newdata: [df_handle, optional] Covariate rows to predict for.
        what: [enum, optional] Quantity to return. Default ``'survival'``.
        q: [number, optional] Quantile to return when what='quantile'. Default ``0.5``.

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
        "srv_aft_predict: not implemented."
    )
