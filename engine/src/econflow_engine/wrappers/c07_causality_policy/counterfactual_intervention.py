# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``counterfactual_intervention`` -- METHOD-SELECTION card #90.

#90 Counterfactual intervention analysis (BSTS)

Category 07-causality-policy; module ``counterfactual_intervention``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c07_causality_policy import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "run_causal_impact",
    "NODE_META",
    "wire_model",
]


def run_causal_impact(
    *,
    data: np.ndarray,
    pre_period: Any,
    post_period: Any,
    alpha: float | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``run_causal_impact`` -- METHOD-SELECTION card #90.

    Counterfactual intervention analysis (BSTS).

    Category 07-causality-policy; memory class ``light``.

    Args:
        data: [matrix_handle, required] Handle to a ts/mts/matrix: 1st column=response, the
            rest=covariates.
        pre_period: [raw_handle, required] Handle to a length-2 vector [start, end]
            pre-intervention.
        post_period: [raw_handle, required] Handle to a length-2 vector [start, end]
            post-intervention.
        alpha: [number, optional] Significance level for the credible intervals (default 0.05).
            Default ``0.05``.
        seed: [integer, required] Seed (required: bsts MCMC reproducibility).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "run_causal_impact: not implemented. The method card is in ./README.md."
    )
