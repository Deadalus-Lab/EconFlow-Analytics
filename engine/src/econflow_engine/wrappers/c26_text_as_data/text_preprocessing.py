# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``text_preprocessing`` -- method card #579.

#579 Preprocessing and keyword extraction

Category 26-text-as-data; module ``text_preprocessing``.

Reference implementation: nltk.

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
    "tx_preprocess",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def tx_preprocess(
    *,
    documents: pd.DataFrame,
    text: str,
    normalise: Literal["none", "stem", "lemmatise"] | None = None,
    stop_words: Sequence[str] | None = None,
    ngram_range: Sequence[int] | None = None,
    min_df: float | None = None,
    max_df: float | None = None,
    weighting: Literal["count", "tfidf", "binary", "log_count"] | None = None,
) -> dict[str, Any]:
    """Node ``tx_preprocess`` -- method card #579.

    Preprocessing and keyword extraction.

    Category 26-text-as-data; memory class ``light``.

    Registers its result under ``dtm``, so a later node can consume it as a handle.

    Args:
        documents: [df_handle, required] Documents with an identifier and text column.
        text: [string, required] Column holding the text.
        normalise: [enum, optional] Word normalisation. Default ``'lemmatise'``.
        stop_words: [series_codes, optional] Stop-word list; omitted = a generic English list.
        ngram_range: [int_array, optional] Minimum and maximum n-gram length. Default ``[1, 2]``.
        min_df: [number, optional] Minimum document frequency. Default ``0.01``.
        max_df: [number, optional] Maximum document frequency. Default ``0.95``.
        weighting: [enum, optional] Term weighting. Default ``'tfidf'``.

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
        "tx_preprocess: not implemented."
    )
