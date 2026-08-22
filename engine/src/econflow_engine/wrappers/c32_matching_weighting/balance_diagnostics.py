# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``balance_diagnostics`` -- method card #279.

#279 Balance diagnostics: standardised differences, variance ratios and love plots

Category 32-matching-weighting; module ``balance_diagnostics``.

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
    "mw_balance",
    "mw_balance_distribution",
    "NODE_META",
    "wire_model",
]


def mw_balance(
    *,
    data: pd.DataFrame,
    treatment: str,
    covariates: Sequence[str] | None = None,
    weights: pd.Series | None = None,
    threshold: float | None = None,
) -> dict[str, Any]:
    """Node ``mw_balance`` -- method card #279.

    Balance diagnostics: standardised differences, variance ratios and love plots.

    Category 32-matching-weighting; memory class ``light``.

    Args:
        data: [df_handle, required] One row per unit.
        treatment: [string, required] Binary treatment column.
        covariates: [series_codes, optional] Covariates to assess.
        weights: [series_handle, optional] Design weights; omitted = unadjusted.
        threshold: [number, optional] Standardised difference regarded as balanced. Default ``0.1``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mw_balance: not implemented."
    )


def mw_balance_distribution(
    *,
    data: pd.DataFrame,
    treatment: str,
    covariates: Sequence[str] | None = None,
    weights: pd.Series | None = None,
    statistic: Literal["ks", "cvm", "wasserstein"] | None = None,
) -> dict[str, Any]:
    """Node ``mw_balance_distribution`` -- method card #279.

    Balance diagnostics: standardised differences, variance ratios and love plots.

    Category 32-matching-weighting; memory class ``light``.

    Args:
        data: [df_handle, required] One row per unit.
        treatment: [string, required] Binary treatment column.
        covariates: [series_codes, optional] Covariates to assess.
        weights: [series_handle, optional] Design weights.
        statistic: [enum, optional] Distance measure. Default ``'ks'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mw_balance_distribution: not implemented."
    )
