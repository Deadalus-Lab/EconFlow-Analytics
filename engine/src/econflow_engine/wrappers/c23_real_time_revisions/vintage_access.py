# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``vintage_access`` -- method card #568.

#568 Vintage-aware data access

Category 23-real-time-revisions; module ``vintage_access``.

Reference implementation: pandas.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

from econflow_engine.generated.args.c23_real_time_revisions import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "rt_read_vintages",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def rt_read_vintages(
    *,
    path: str,
    series: Sequence[str],
    vintage_dates: Sequence[str] | None = None,
    format: Literal["long", "wide", "triangle"] | None = None,
) -> dict[str, Any]:
    """Node ``rt_read_vintages`` -- method card #568.

    Vintage-aware data access.

    Category 23-real-time-revisions; memory class ``light``.

    Args:
        path: [path, required] Object-store path to the archive extract.
        series: [series_codes, required] Series identifiers to read.
        vintage_dates: [series_codes, optional] Vintage dates to read; omitted = all.
        format: [enum, optional] Archive layout. Default ``'long'``.

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
        "rt_read_vintages: not implemented."
    )
