# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``embeddings`` -- method card #582.

#582 Word and document embeddings

Category 26-text-as-data; module ``embeddings``.

Reference implementation: gensim.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c26_text_as_data import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "tx_embeddings",
    "tx_similarity",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def tx_embeddings(
    *,
    documents: pd.DataFrame,
    text: str,
    model: Literal["word2vec", "fasttext", "doc2vec"] | None = None,
    dimensions: int | None = None,
    window: int | None = None,
    min_count: int | None = None,
    epochs: int | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``tx_embeddings`` -- method card #582.

    Word and document embeddings.

    Category 26-text-as-data; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        documents: [df_handle, required] Tokenised documents.
        text: [string, required] Column holding the tokens.
        model: [enum, optional] Embedding model. Default ``'word2vec'``.
        dimensions: [integer, optional] Vector dimension. Default ``100``.
        window: [integer, optional] Context window. Default ``5``.
        min_count: [integer, optional] Minimum token frequency. Default ``5``.
        epochs: [integer, optional] Training epochs. Default ``10``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.

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
        "tx_embeddings: not implemented."
    )


def tx_similarity(
    *,
    model: Any,
    terms: Sequence[str],
    top_n: int | None = None,
) -> dict[str, Any]:
    """Node ``tx_similarity`` -- method card #582.

    Word and document embeddings.

    Category 26-text-as-data; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to trained embeddings.
        terms: [series_codes, required] Terms or document ids to query.
        top_n: [integer, optional] Neighbours returned. Default ``10``.

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
        "tx_similarity: not implemented."
    )
