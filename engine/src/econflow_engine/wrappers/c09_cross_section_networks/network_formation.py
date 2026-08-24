# --- gen_wrappers: header begin ---
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

# --- gen_wrappers: header end ---


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

    Gates:
        None declared. The ``precondition_gates`` field of this method card is empty; the checks a
        body must run are named here once the field carries them.

    .. gen_wrappers: end of generated docstring

    Examples:
        None yet. This node raises ``NotImplementedError``; its example is written with its body and
        belongs to whoever writes it.

    Note:
        The implementation note is written with the body: the library functions it calls and their
        versions, what the method leaves out, and every gate added with the source that requires it.
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

    Gates:
        None declared. The ``precondition_gates`` field of this method card is empty; the checks a
        body must run are named here once the field carries them.

    .. gen_wrappers: end of generated docstring

    Examples:
        None yet. This node raises ``NotImplementedError``; its example is written with its body and
        belongs to whoever writes it.

    Note:
        The implementation note is written with the body: the library functions it calls and their
        versions, what the method leaves out, and every gate added with the source that requires it.
    """
    raise NotImplementedError(
        "cs_network_statistics: not implemented."
    )
