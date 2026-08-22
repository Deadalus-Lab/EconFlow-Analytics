# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``record_linkage`` -- method card #388.

#388 Record linkage, deduplication and fuzzy matching

Category 00-data-utilities; module ``record_linkage``.

Reference implementation: recordlinkage.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c00_data_utilities import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "du_deduplicate",
    "du_link_records",
    "NODE_META",
    "wire_model",
]


def du_link_records(
    *,
    left: pd.DataFrame,
    right: pd.DataFrame,
    blocking: Sequence[str],
    compare: Sequence[str],
    method: Literal["exact", "levenshtein", "jarowinkler", "jaro", "numeric", "date"] | None = None,
    threshold: float | None = None,
) -> dict[str, Any]:
    """Node ``du_link_records`` -- method card #388.

    Record linkage, deduplication and fuzzy matching.

    Category 00-data-utilities; memory class ``light``.

    Args:
        left: [df_handle, required] First table.
        right: [df_handle, required] Second table.
        blocking: [series_codes, required] Columns used to block comparisons.
        compare: [series_codes, required] Columns compared within a block.
        method: [enum, optional] Comparison method. Default ``'jarowinkler'``.
        threshold: [number, optional] Score above which a pair is accepted. Default ``0.85``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "du_link_records: not implemented."
    )


def du_deduplicate(
    *,
    data: pd.DataFrame,
    blocking: Sequence[str],
    compare: Sequence[str],
    threshold: float | None = None,
    resolution: Literal["first", "last", "most_complete", "flag_only"] | None = None,
) -> dict[str, Any]:
    """Node ``du_deduplicate`` -- method card #388.

    Record linkage, deduplication and fuzzy matching.

    Category 00-data-utilities; memory class ``light``.

    Args:
        data: [df_handle, required] Table to deduplicate.
        blocking: [series_codes, required] Columns used to block comparisons.
        compare: [series_codes, required] Columns compared within a block.
        threshold: [number, optional] Score above which records are the same entity. Default
            ``0.9``.
        resolution: [enum, optional] How duplicates are resolved. Default ``'first'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "du_deduplicate: not implemented."
    )
