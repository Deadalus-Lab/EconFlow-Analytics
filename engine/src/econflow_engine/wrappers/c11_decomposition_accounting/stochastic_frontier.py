# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``stochastic_frontier`` -- method card #485.

#485 Stochastic frontier analysis

Category 11-decomposition-accounting; module ``stochastic_frontier``.

Reference implementation: pystoned.

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
    "da_stochastic_frontier",
    "NODE_META",
    "wire_model",
]


def da_stochastic_frontier(
    *,
    y: pd.Series,
    x: pd.DataFrame,
    frontier: Literal["production", "cost"] | None = None,
    distribution: Literal["half_normal", "truncated_normal", "exponential", "gamma"] | None = None,
    inefficiency_covariates: Sequence[str] | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``da_stochastic_frontier`` -- method card #485.

    Stochastic frontier analysis.

    Category 11-decomposition-accounting; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Output or cost.
        x: [df_handle, required] Input table.
        frontier: [enum, optional] Frontier type. Default ``'production'``.
        distribution: [enum, optional] Inefficiency distribution. Default ``'half_normal'``.
        inefficiency_covariates: [series_codes, optional] Covariates explaining inefficiency.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "da_stochastic_frontier: not implemented."
    )
