# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``coarsened_exact_matching`` -- method card #277.

#277 Coarsened exact matching and stratified matching

Category 32-matching-weighting; module ``coarsened_exact_matching``.

Reference implementation: causallib.

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
    "mw_cem",
    "mw_imbalance_l1",
    "NODE_META",
    "wire_model",
]


def mw_cem(
    *,
    data: pd.DataFrame,
    treatment: str,
    covariates: Sequence[str] | None = None,
    coarsening: Literal["sturges", "scott", "fd", "quantile", "manual"] | None = None,
    n_bins: int | None = None,
) -> dict[str, Any]:
    """Node ``mw_cem`` -- method card #277.

    Coarsened exact matching and stratified matching.

    Category 32-matching-weighting; memory class ``light``.

    Registers its result under ``matched``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] One row per unit.
        treatment: [string, required] Binary treatment column.
        covariates: [series_codes, optional] Covariates to coarsen and match on.
        coarsening: [enum, optional] Binning rule for continuous covariates. Default ``'sturges'``.
        n_bins: [integer, optional] Bins per covariate when the rule is manual. Default ``5``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mw_cem: not implemented."
    )


def mw_imbalance_l1(
    *,
    data: pd.DataFrame,
    treatment: str,
    covariates: Sequence[str] | None = None,
    weights: pd.Series | None = None,
) -> dict[str, Any]:
    """Node ``mw_imbalance_l1`` -- method card #277.

    Coarsened exact matching and stratified matching.

    Category 32-matching-weighting; memory class ``light``.

    Args:
        data: [df_handle, required] One row per unit.
        treatment: [string, required] Binary treatment column.
        covariates: [series_codes, optional] Covariates to measure imbalance over.
        weights: [series_handle, optional] Matching weights; omitted = unweighted.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mw_imbalance_l1: not implemented."
    )
