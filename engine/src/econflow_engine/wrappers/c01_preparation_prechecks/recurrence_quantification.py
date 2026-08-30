# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``recurrence_quantification`` -- method card #405.

#405 Recurrence quantification analysis

Category 01-preparation-prechecks; module ``recurrence_quantification``.

Reference implementation: PyRQA.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any

import pandas as pd

from econflow_engine.generated.args.c01_preparation_prechecks import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "pp_recurrence_quantification",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def pp_recurrence_quantification(
    *,
    x: pd.Series,
    embedding_dimension: int | None = None,
    time_delay: int | None = None,
    threshold: float | None = None,
    min_line_length: int | None = None,
) -> dict[str, Any]:
    """Node ``pp_recurrence_quantification`` -- method card #405.

    Recurrence quantification analysis.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [series_handle, required] Series.
        embedding_dimension: [integer, optional] Embedding dimension. Default ``3``.
        time_delay: [integer, optional] Embedding delay. Default ``1``.
        threshold: [number, optional] Recurrence threshold as a fraction of the attractor size.
            Default ``0.1``.
        min_line_length: [integer, optional] Minimum diagonal line length counted. Default ``2``.

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
        "pp_recurrence_quantification: not implemented."
    )
