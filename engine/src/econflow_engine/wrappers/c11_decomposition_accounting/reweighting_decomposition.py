# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``reweighting_decomposition`` -- method card #489.

#489 Reweighting decompositions: DiNardo-Fortin-Lemieux and RIF

Category 11-decomposition-accounting; module ``reweighting_decomposition``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c11_decomposition_accounting import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "da_reweighting_decomposition",
    "NODE_META",
    "wire_model",
]


def da_reweighting_decomposition(
    *,
    data: pd.DataFrame,
    outcome: str,
    group: str,
    covariates: Sequence[str] | None = None,
    method: Literal["dfl", "rif", "oaxaca_blinder"] | None = None,
    quantiles: Sequence[float] | None = None,
    nboot: int | None = None,
    seed: int,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``da_reweighting_decomposition`` -- method card #489.

    Reweighting decompositions: DiNardo-Fortin-Lemieux and RIF.

    Category 11-decomposition-accounting; memory class ``heavy``.

    Args:
        data: [df_handle, required] Pooled data for both groups.
        outcome: [string, required] Outcome column.
        group: [string, required] Group indicator.
        covariates: [series_codes, optional] Covariate columns.
        method: [enum, optional] Decomposition method. Default ``'dfl'``.
        quantiles: [num_array, optional] Quantiles to decompose. Default ``[0.1, 0.5, 0.9]``.
        nboot: [integer, optional] Number of bootstrap replications. Default ``999``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "da_reweighting_decomposition: not implemented."
    )
