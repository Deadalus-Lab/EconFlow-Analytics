# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``network`` -- method card #55.

#55 Network analysis

Category 09-cross-section-networks; module ``network``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c09_cross_section_networks import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "net_centrality",
    "net_community_louvain",
    "net_connectivity",
    "net_from_adjacency",
    "net_from_edgelist",
    "NODE_META",
    "wire_model",
]


def net_from_edgelist(
    *,
    edges: pd.DataFrame,
    directed: bool | None = None,
) -> dict[str, Any]:
    """Node ``net_from_edgelist`` -- method card #55.

    Network analysis.

    Category 09-cross-section-networks; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        edges: [df_handle, required] DataFrame with >=2 columns (from, to + edge attributes).
        directed: [boolean, optional] Directed graph (default True).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "net_from_edgelist: not implemented."
    )


def net_from_adjacency(
    *,
    adjmatrix: np.ndarray,
    mode: Literal["directed", "undirected", "max", "min", "upper", "lower", "plus"] | None = None,
    diag: bool | None = None,
) -> dict[str, Any]:
    """Node ``net_from_adjacency`` -- method card #55.

    Network analysis.

    Category 09-cross-section-networks; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        adjmatrix: [matrix_handle, required] Square numeric adjacency matrix.
        mode: [enum, optional] Matrix interpretation (default directed).
        diag: [boolean, optional] Include the diagonal (self-loops) (default True).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "net_from_adjacency: not implemented."
    )


def net_centrality(
    *,
    graph: Any,
    degree_mode: Literal["all", "out", "in", "total"] | None = None,
) -> dict[str, Any]:
    """Node ``net_centrality`` -- method card #55.

    Network analysis.

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        graph: [raw_handle, required] igraph object (ig_from_* $handle).
        degree_mode: [enum, optional] degree: direction (default all).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "net_centrality: not implemented."
    )


def net_community_louvain(
    *,
    graph: Any,
    resolution: float | None = None,
) -> dict[str, Any]:
    """Node ``net_community_louvain`` -- method card #55.

    Network analysis.

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        graph: [raw_handle, required] UNDIRECTED igraph object (ig_from_* $handle).
        resolution: [number, optional] Resolution parameter modularity (default 1). Default ``1``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "net_community_louvain: not implemented."
    )


def net_connectivity(
    *,
    graph: Any,
    directed: bool | None = None,
    component_mode: Literal["weak", "strong"] | None = None,
) -> dict[str, Any]:
    """Node ``net_connectivity`` -- method card #55.

    Network analysis.

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        graph: [raw_handle, required] igraph object (ig_from_* $handle).
        directed: [boolean, optional] Path direction for diameter/mean_distance/assortativity
            (default True).
        component_mode: [enum, optional] components/is_connected: weak/strong (default weak).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "net_connectivity: not implemented."
    )
