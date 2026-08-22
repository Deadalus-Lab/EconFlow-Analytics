# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``quantile_treatment_effects`` -- method card #451.

#451 Changes-in-changes and quantile treatment effects

Category 07-causality-policy; module ``quantile_treatment_effects``.

Reference implementation: econml.

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
    "cp_changes_in_changes",
    "cp_quantile_treatment_effect",
    "NODE_META",
    "wire_model",
]


def cp_changes_in_changes(
    *,
    data: pd.DataFrame,
    outcome: str,
    treatment: str,
    time: str,
    quantiles: Sequence[float] | None = None,
    nboot: int | None = None,
    seed: int,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``cp_changes_in_changes`` -- method card #451.

    Changes-in-changes and quantile treatment effects.

    Category 07-causality-policy; memory class ``heavy``.

    Args:
        data: [df_handle, required] Panel or repeated cross-section.
        outcome: [string, required] Outcome column.
        treatment: [string, required] Treatment indicator.
        time: [string, required] Period indicator.
        quantiles: [num_array, optional] Quantiles to report. Default ``[0.1, 0.25, 0.5, 0.75,
            0.9]``.
        nboot: [integer, optional] Number of bootstrap replications. Default ``999``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cp_changes_in_changes: not implemented."
    )


def cp_quantile_treatment_effect(
    *,
    data: pd.DataFrame,
    outcome: str,
    treatment: str,
    covariates: Sequence[str] | None = None,
    quantiles: Sequence[float] | None = None,
    method: Literal["ipw", "regression", "doubly_robust"] | None = None,
    nboot: int | None = None,
    seed: int,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``cp_quantile_treatment_effect`` -- method card #451.

    Changes-in-changes and quantile treatment effects.

    Category 07-causality-policy; memory class ``heavy``.

    Args:
        data: [df_handle, required] Data.
        outcome: [string, required] Outcome column.
        treatment: [string, required] Treatment indicator.
        covariates: [series_codes, optional] Covariate columns.
        quantiles: [num_array, optional] Quantiles to report. Default ``[0.1, 0.25, 0.5, 0.75,
            0.9]``.
        method: [enum, optional] Estimator. Default ``'ipw'``.
        nboot: [integer, optional] Number of bootstrap replications. Default ``999``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cp_quantile_treatment_effect: not implemented."
    )
