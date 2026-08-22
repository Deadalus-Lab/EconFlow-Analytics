# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``readability`` -- method card #585.

#585 Readability and linguistic complexity

Category 26-text-as-data; module ``readability``.

Reference implementation: nltk.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c26_text_as_data import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "tx_readability",
    "NODE_META",
    "wire_model",
]


def tx_readability(
    *,
    documents: pd.DataFrame,
    text: str,
    indices: Sequence[str] | None = None,
    standardise_length: bool | None = None,
) -> dict[str, Any]:
    """Node ``tx_readability`` -- method card #585.

    Readability and linguistic complexity.

    Category 26-text-as-data; memory class ``light``.

    Args:
        documents: [df_handle, required] Documents with a text column.
        text: [string, required] Column holding the text.
        indices: [series_codes, optional] Indices to compute; omitted = the standard set.
        standardise_length: [boolean, optional] Standardise length-dependent measures. Default
            ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "tx_readability: not implemented."
    )
