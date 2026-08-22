# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``matrix_factorisation_topics`` -- method card #581.

#581 Matrix-factorisation topics: NMF and latent semantic analysis

Category 26-text-as-data; module ``matrix_factorisation_topics``.

Reference implementation: scikit-learn.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

from econflow_engine.generated.args.c26_text_as_data import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "tx_matrix_topics",
    "NODE_META",
    "wire_model",
]


def tx_matrix_topics(
    *,
    dtm: Any,
    n_components: int | None = None,
    method: Literal["nmf", "lsa", "pca"] | None = None,
    init: Literal["random", "nndsvd", "nndsvda"] | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``tx_matrix_topics`` -- method card #581.

    Matrix-factorisation topics: NMF and latent semantic analysis.

    Category 26-text-as-data; memory class ``light``.

    Args:
        dtm: [raw_handle, required] Handle to a document-term matrix.
        n_components: [integer, optional] Number of components. Default ``20``.
        method: [enum, optional] Factorisation. Default ``'nmf'``.
        init: [enum, optional] Initialisation. Default ``'nndsvd'``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "tx_matrix_topics: not implemented."
    )
