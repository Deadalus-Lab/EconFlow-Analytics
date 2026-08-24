# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``columnar_engine`` -- method card #391.

#391 Columnar and lazy execution for large panels

Category 00-data-utilities; module ``columnar_engine``.

Reference implementation: polars.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from econflow_engine.generated.args.c00_data_utilities import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "du_lazy_query",
    "du_query_plan",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def du_lazy_query(
    *,
    source: str,
    select: Sequence[str] | None = None,
    filter: str | None = None,
    group_by: Sequence[str] | None = None,
    aggregations: Any | None = None,
    collect: bool | None = None,
) -> dict[str, Any]:
    """Node ``du_lazy_query`` -- method card #391.

    Columnar and lazy execution for large panels.

    Category 00-data-utilities; memory class ``light``.

    Args:
        source: [path, required] Object-store path to the dataset.
        select: [series_codes, optional] Columns to project.
        filter: [formula, optional] Row filter pushed into the scan.
        group_by: [series_codes, optional] Grouping columns.
        aggregations: [raw, optional] Aggregation specification.
        collect: [boolean, optional] Materialise the result. Default ``True``.

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
        "du_lazy_query: not implemented."
    )


def du_query_plan(
    *,
    source: str,
    filter: str | None = None,
    select: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Node ``du_query_plan`` -- method card #391.

    Columnar and lazy execution for large panels.

    Category 00-data-utilities; memory class ``light``.

    Args:
        source: [path, required] Object-store path to the dataset.
        filter: [formula, optional] Row filter.
        select: [series_codes, optional] Columns to project.

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
        "du_query_plan: not implemented."
    )
