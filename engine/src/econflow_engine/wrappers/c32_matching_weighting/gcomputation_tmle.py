# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``gcomputation_tmle`` -- method card #282.

#282 G-computation, standardisation and targeted maximum likelihood

Category 32-matching-weighting; module ``gcomputation_tmle``.

Reference implementation: zepid.

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
    "mw_gcomputation",
    "mw_tmle",
    "NODE_META",
    "wire_model",
]


def mw_gcomputation(
    *,
    data: pd.DataFrame,
    treatment: str,
    outcome: str,
    covariates: Sequence[str] | None = None,
    outcome_model: Literal["linear", "logit", "gradient_boosting", "random_forest"] | None = None,
    estimand: Literal["ate", "att", "atc"] | None = None,
    nboot: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``mw_gcomputation`` -- method card #282.

    G-computation, standardisation and targeted maximum likelihood.

    Category 32-matching-weighting; memory class ``heavy``.

    Args:
        data: [df_handle, required] One row per unit.
        treatment: [string, required] Binary treatment column.
        outcome: [string, required] Outcome column.
        covariates: [series_codes, optional] Covariates in the outcome model.
        outcome_model: [enum, optional] Learner for the outcome regression. Default ``'linear'``.
        estimand: [enum, optional] Population to standardise over. Default ``'ate'``.
        nboot: [integer, optional] Number of bootstrap replications. Default ``999``.
        seed: [integer, optional] Seed for the random number generator.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mw_gcomputation: not implemented."
    )


def mw_tmle(
    *,
    data: pd.DataFrame,
    treatment: str,
    outcome: str,
    covariates: Sequence[str] | None = None,
    outcome_model: Literal["linear", "logit", "gradient_boosting", "random_forest"] | None = None,
    treatment_model: Literal["logit", "gradient_boosting", "random_forest"] | None = None,
    trim: float | None = None,
    seed: int | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``mw_tmle`` -- method card #282.

    G-computation, standardisation and targeted maximum likelihood.

    Category 32-matching-weighting; memory class ``light``.

    Args:
        data: [df_handle, required] One row per unit.
        treatment: [string, required] Binary treatment column.
        outcome: [string, required] Outcome column.
        covariates: [series_codes, optional] Covariates for both models.
        outcome_model: [enum, optional] Learner for the outcome regression. Default
            ``'gradient_boosting'``.
        treatment_model: [enum, optional] Learner for the propensity. Default ``'logit'``.
        trim: [number, optional] Trim propensities to [trim, 1-trim]. Default ``0.01``.
        seed: [integer, optional] Seed for the random number generator.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mw_tmle: not implemented."
    )
