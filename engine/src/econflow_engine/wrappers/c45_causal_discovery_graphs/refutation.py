# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``refutation`` -- method card #378.

#378 Refutation: placebo treatment, random common cause, subset and unobserved confounder

Category 45-causal-discovery-graphs; module ``refutation``.

Reference implementation: dowhy.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c45_causal_discovery_graphs import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "cd_refute",
    "cd_sensitivity_confounder",
    "NODE_META",
    "wire_model",
]


def cd_refute(
    *,
    estimand: Any,
    data: pd.DataFrame,
    refuters: Sequence[str] | None = None,
    n_simulations: int | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``cd_refute`` -- method card #378.

    Refutation: placebo treatment, random common cause, subset and unobserved confounder.

    Category 45-causal-discovery-graphs; memory class ``light``.

    Args:
        estimand: [raw_handle, required] Handle to a derived estimand.
        data: [df_handle, required] Data the estimate was produced on.
        refuters: [series_codes, optional] Refuters to run; omitted = the standard set.
        n_simulations: [integer, optional] Simulations per refuter. Default ``100``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cd_refute: not implemented."
    )


def cd_sensitivity_confounder(
    *,
    estimand: Any,
    data: pd.DataFrame,
    effect_strength_treatment: Sequence[float] | None = None,
    effect_strength_outcome: Sequence[float] | None = None,
) -> dict[str, Any]:
    """Node ``cd_sensitivity_confounder`` -- method card #378.

    Refutation: placebo treatment, random common cause, subset and unobserved confounder.

    Category 45-causal-discovery-graphs; memory class ``light``.

    Args:
        estimand: [raw_handle, required] Handle to a derived estimand.
        data: [df_handle, required] Data the estimate was produced on.
        effect_strength_treatment: [num_array, optional] Confounder-treatment strengths to scan.
        effect_strength_outcome: [num_array, optional] Confounder-outcome strengths to scan.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cd_sensitivity_confounder: not implemented."
    )
