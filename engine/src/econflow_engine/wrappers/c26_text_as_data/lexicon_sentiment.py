# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``lexicon_sentiment`` -- method card #584.

#584 Lexicon sentiment with negation handling

Category 26-text-as-data; module ``lexicon_sentiment``.

Reference implementation: vaderSentiment.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c26_text_as_data import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "tx_lexicon_sentiment",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def tx_lexicon_sentiment(
    *,
    documents: pd.DataFrame,
    text: str,
    lexicon: Literal["loughran_mcdonald", "vader", "harvard_iv", "custom"] | None = None,
    custom_lexicon: pd.DataFrame | None = None,
    negation: bool | None = None,
    normalise: Literal["none", "word_count", "sentence_count"] | None = None,
) -> dict[str, Any]:
    """Node ``tx_lexicon_sentiment`` -- method card #584.

    Lexicon sentiment with negation handling.

    Category 26-text-as-data; memory class ``light``.

    Args:
        documents: [df_handle, required] Documents with a text column.
        text: [string, required] Column holding the text.
        lexicon: [enum, optional] Lexicon. Default ``'loughran_mcdonald'``.
        custom_lexicon: [df_handle, optional] Custom term-polarity table.
        negation: [boolean, optional] Apply negation handling. Default ``True``.
        normalise: [enum, optional] Score normalisation. Default ``'word_count'``.

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
        "tx_lexicon_sentiment: not implemented."
    )
