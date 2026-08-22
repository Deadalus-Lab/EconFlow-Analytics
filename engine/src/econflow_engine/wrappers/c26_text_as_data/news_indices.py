# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``news_indices`` -- method card #583.

#583 News-based uncertainty and policy indices

Category 26-text-as-data; module ``news_indices``.

Reference implementation: nltk.

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
    "tx_news_index",
    "NODE_META",
    "wire_model",
]


def tx_news_index(
    *,
    documents: pd.DataFrame,
    text: str,
    date: str,
    terms: Any,
    normalise_by: Literal["none", "article_count", "word_count"] | None = None,
    frequency: Literal["daily", "weekly", "monthly", "quarterly"] | None = None,
    standardise: bool | None = None,
) -> dict[str, Any]:
    """Node ``tx_news_index`` -- method card #583.

    News-based uncertainty and policy indices.

    Category 26-text-as-data; memory class ``light``.

    Args:
        documents: [df_handle, required] Documents with a date and text column.
        text: [string, required] Column holding the text.
        date: [string, required] Column holding the document date.
        terms: [raw, required] Term groups that must co-occur.
        normalise_by: [enum, optional] Normalisation. Default ``'article_count'``.
        frequency: [enum, optional] Aggregation frequency. Default ``'monthly'``.
        standardise: [boolean, optional] Standardise to unit variance. Default ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "tx_news_index: not implemented."
    )
