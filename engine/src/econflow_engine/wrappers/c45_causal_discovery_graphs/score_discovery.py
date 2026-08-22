# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``score_discovery`` -- method card #375.

#375 Score-based structure learning: GES, exact search and permutation methods

Category 45-causal-discovery-graphs; module ``score_discovery``.

Reference implementation: causal-learn.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c45_causal_discovery_graphs import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "cd_exact_search",
    "cd_ges",
    "NODE_META",
    "wire_model",
]


def cd_ges(
    *,
    data: pd.DataFrame,
    score: Literal["bic", "bdeu", "generalised_score", "marginal_likelihood"] | None = None,
    max_parents: int | None = None,
) -> dict[str, Any]:
    """Node ``cd_ges`` -- method card #375.

    Score-based structure learning: GES, exact search and permutation methods.

    Category 45-causal-discovery-graphs; memory class ``light``.

    Args:
        data: [df_handle, required] Observational data.
        score: [enum, optional] Scoring function. Default ``'bic'``.
        max_parents: [integer, optional] Maximum parents per node.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cd_ges: not implemented."
    )


def cd_exact_search(
    *,
    data: pd.DataFrame,
    score: Literal["bic", "bdeu"] | None = None,
    max_parents: int | None = None,
) -> dict[str, Any]:
    """Node ``cd_exact_search`` -- method card #375.

    Score-based structure learning: GES, exact search and permutation methods.

    Category 45-causal-discovery-graphs; memory class ``light``.

    Args:
        data: [df_handle, required] Observational data.
        score: [enum, optional] Scoring function. Default ``'bic'``.
        max_parents: [integer, optional] Maximum parents per node. Default ``3``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cd_exact_search: not implemented."
    )
