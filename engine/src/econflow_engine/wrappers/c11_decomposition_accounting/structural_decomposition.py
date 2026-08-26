# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``structural_decomposition`` -- method card #490.

#490 Structural decomposition analysis of input-output tables

Category 11-decomposition-accounting; module ``structural_decomposition``.

Reference implementation: pymrio.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

from econflow_engine.generated.args.c11_decomposition_accounting import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "da_structural_decomposition",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def da_structural_decomposition(
    *,
    table_start: Any,
    table_end: Any,
    extension: str | None = None,
    form: Literal["average_polar", "first_polar", "second_polar", "all_forms"] | None = None,
) -> dict[str, Any]:
    """Node ``da_structural_decomposition`` -- method card #490.

    Structural decomposition analysis of input-output tables.

    Category 11-decomposition-accounting; memory class ``light``.

    Args:
        table_start: [raw_handle, required] Handle to the earlier table.
        table_end: [raw_handle, required] Handle to the later table.
        extension: [string, optional] Environmental extension to decompose.
        form: [enum, optional] Decomposition form. Default ``'average_polar'``.

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
        "da_structural_decomposition: not implemented."
    )
