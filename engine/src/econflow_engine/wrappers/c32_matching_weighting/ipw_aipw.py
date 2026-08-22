# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``ipw_aipw`` -- method card #278.

#278 Inverse probability weighting, stabilised weights and doubly-robust AIPW

Category 32-matching-weighting; module ``ipw_aipw``.

Reference implementation: doubleml.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c32_matching_weighting import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "mw_aipw",
    "mw_ipw",
    "mw_weight_diagnostics",
    "NODE_META",
    "wire_model",
]


def mw_ipw(
    *,
    data: pd.DataFrame,
    treatment: str,
    outcome: str,
    pscore: str | None = None,
    covariates: Sequence[str] | None = None,
    stabilised: bool | None = None,
    trim: float | None = None,
    estimand: Literal["ate", "att", "atc"] | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``mw_ipw`` -- method card #278.

    Inverse probability weighting, stabilised weights and doubly-robust AIPW.

    Category 32-matching-weighting; memory class ``light``.

    Args:
        data: [df_handle, required] One row per unit.
        treatment: [string, required] Binary treatment column.
        outcome: [string, required] Outcome column.
        pscore: [string, optional] Pre-computed propensity column.
        covariates: [series_codes, optional] Covariates for the treatment model when no score is
            supplied.
        stabilised: [boolean, optional] Use stabilised weights. Default ``True``.
        trim: [number, optional] Trim propensities to [trim, 1-trim]. Default ``0.01``.
        estimand: [enum, optional] Estimand to report. Default ``'ate'``.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mw_ipw: not implemented."
    )


def mw_aipw(
    *,
    data: pd.DataFrame,
    treatment: str,
    outcome: str,
    covariates: Sequence[str] | None = None,
    outcome_model: Literal["linear", "gradient_boosting", "random_forest"] | None = None,
    treatment_model: Literal["logit", "gradient_boosting", "random_forest"] | None = None,
    n_folds: int | None = None,
    seed: int | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``mw_aipw`` -- method card #278.

    Inverse probability weighting, stabilised weights and doubly-robust AIPW.

    Category 32-matching-weighting; memory class ``light``.

    Args:
        data: [df_handle, required] One row per unit.
        treatment: [string, required] Binary treatment column.
        outcome: [string, required] Outcome column.
        covariates: [series_codes, optional] Covariates for both the treatment and outcome models.
        outcome_model: [enum, optional] Learner for the outcome regression. Default ``'linear'``.
        treatment_model: [enum, optional] Learner for the propensity. Default ``'logit'``.
        n_folds: [integer, optional] Cross-fitting folds; 1 disables cross-fitting. Default ``5``.
        seed: [integer, optional] Seed for the random number generator.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mw_aipw: not implemented."
    )


def mw_weight_diagnostics(
    *,
    weights: pd.Series,
    treatment: pd.Series,
) -> dict[str, Any]:
    """Node ``mw_weight_diagnostics`` -- method card #278.

    Inverse probability weighting, stabilised weights and doubly-robust AIPW.

    Category 32-matching-weighting; memory class ``light``.

    Args:
        weights: [series_handle, required] Estimated weights per unit.
        treatment: [series_handle, required] Binary treatment indicator.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mw_weight_diagnostics: not implemented."
    )
