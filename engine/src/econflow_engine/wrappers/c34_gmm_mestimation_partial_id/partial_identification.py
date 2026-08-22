# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``partial_identification`` -- method card #299.

#299 Partial identification: Manski bounds, Lee bounds and moment-inequality sets

Category 34-gmm-mestimation-partial-id; module ``partial_identification``.

Reference implementation: cvxpy.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c34_gmm_mestimation_partial_id import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "gme_lee_bounds",
    "gme_manski_bounds",
    "gme_moment_inequality_set",
    "NODE_META",
    "wire_model",
]


def gme_manski_bounds(
    *,
    outcome: pd.Series,
    selection: pd.Series,
    treatment: pd.Series | None = None,
    y_min: float | None = None,
    y_max: float | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``gme_manski_bounds`` -- method card #299.

    Partial identification: Manski bounds, Lee bounds and moment-inequality sets.

    Category 34-gmm-mestimation-partial-id; memory class ``light``.

    Args:
        outcome: [series_handle, required] Observed outcome, missing where unobserved.
        selection: [series_handle, required] Indicator that the outcome is observed.
        treatment: [series_handle, optional] Treatment indicator for an effect bound.
        y_min: [number, optional] Logical lower bound on the outcome.
        y_max: [number, optional] Logical upper bound on the outcome.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "gme_manski_bounds: not implemented."
    )


def gme_lee_bounds(
    *,
    outcome: pd.Series,
    treatment: pd.Series,
    selection: pd.Series,
    covariates: Sequence[str] | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``gme_lee_bounds`` -- method card #299.

    Partial identification: Manski bounds, Lee bounds and moment-inequality sets.

    Category 34-gmm-mestimation-partial-id; memory class ``light``.

    Args:
        outcome: [series_handle, required] Observed outcome.
        treatment: [series_handle, required] Treatment indicator.
        selection: [series_handle, required] Indicator that the outcome is observed.
        covariates: [series_codes, optional] Covariates for tightened bounds.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "gme_lee_bounds: not implemented."
    )


def gme_moment_inequality_set(
    *,
    data: pd.DataFrame,
    inequalities: str,
    grid: Sequence[float] | None = None,
    method: Literal["subsampling", "bootstrap", "self_normalised"] | None = None,
    nboot: int | None = None,
    seed: int | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``gme_moment_inequality_set`` -- method card #299.

    Partial identification: Manski bounds, Lee bounds and moment-inequality sets.

    Category 34-gmm-mestimation-partial-id; memory class ``heavy``.

    Args:
        data: [df_handle, required] Data the inequalities are evaluated on.
        inequalities: [formula, required] Moment-inequality specification.
        grid: [num_array, optional] Parameter grid to test over.
        method: [enum, optional] Critical-value construction. Default ``'subsampling'``.
        nboot: [integer, optional] Number of bootstrap replications. Default ``999``.
        seed: [integer, optional] Seed for the random number generator.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "gme_moment_inequality_set: not implemented."
    )
