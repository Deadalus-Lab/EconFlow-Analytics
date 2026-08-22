# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``network_formation`` -- method card #475.

#475 Network formation models and graph embeddings

Category 09-cross-section-networks; module ``network_formation``.

Reference implementation: graspologic.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c09_cross_section_networks import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "cs_graph_embedding",
    "cs_network_statistics",
    "NODE_META",
    "wire_model",
]


def cs_graph_embedding(
    *,
    adjacency: np.ndarray,
    method: Literal["ase", "lse", "node2vec", "omnibus", "mase"] | None = None,
    n_dimensions: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``cs_graph_embedding`` -- method card #475.

    Network formation models and graph embeddings.

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        adjacency: [matrix_handle, required] Adjacency matrix.
        method: [enum, optional] Embedding method. Default ``'ase'``.
        n_dimensions: [integer, optional] Embedding dimension; omitted = selected by elbow.
        seed: [integer, optional] Seed for the random number generator.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cs_graph_embedding: not implemented."
    )


def cs_network_statistics(
    *,
    adjacency: np.ndarray,
    statistics: Sequence[str] | None = None,
    communities: bool | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``cs_network_statistics`` -- method card #475.

    Network formation models and graph embeddings.

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        adjacency: [matrix_handle, required] Adjacency matrix.
        statistics: [series_codes, optional] Statistics to compute; omitted = the standard set.
        communities: [boolean, optional] Detect communities. Default ``True``.
        seed: [integer, optional] Seed for the random number generator.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cs_network_statistics: not implemented."
    )
