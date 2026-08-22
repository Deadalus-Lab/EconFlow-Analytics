# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``distributional_impact`` -- method card #364.

#364 Static distributional impact: winners, losers and decile incidence

Category 43-microsimulation-taxbenefit; module ``distributional_impact``.

Reference implementation: policyengine-core.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c43_microsimulation_taxbenefit import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "tb_distributional_impact",
    "NODE_META",
    "wire_model",
]


def tb_distributional_impact(
    *,
    baseline: Any,
    reform: Any,
    weights: pd.Series | None = None,
    equivalence_scale: Literal["none", "oecd", "oecd_modified", "square_root"] | None = None,
    n_groups: int | None = None,
) -> dict[str, Any]:
    """Node ``tb_distributional_impact`` -- method card #364.

    Static distributional impact: winners, losers and decile incidence.

    Category 43-microsimulation-taxbenefit; memory class ``light``.

    Args:
        baseline: [raw_handle, required] Handle to a baseline simulation.
        reform: [raw_handle, required] Handle to a reform simulation.
        weights: [series_handle, optional] Survey weights.
        equivalence_scale: [enum, optional] Equivalence scale for ranking. Default
            ``'oecd_modified'``.
        n_groups: [integer, optional] Number of income groups. Default ``10``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "tb_distributional_impact: not implemented."
    )
