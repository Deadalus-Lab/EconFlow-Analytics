# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``schema_validation`` -- method card #387.

#387 Schema validation and data contracts

Category 00-data-utilities; module ``schema_validation``.

Reference implementation: pandera.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c00_data_utilities import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "du_infer_schema",
    "du_validate_schema",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def du_validate_schema(
    *,
    data: pd.DataFrame,
    schema: Any,
    coerce: bool | None = None,
    lazy: bool | None = None,
) -> dict[str, Any]:
    """Node ``du_validate_schema`` -- method card #387.

    Schema validation and data contracts.

    Category 00-data-utilities; memory class ``light``.

    Args:
        data: [df_handle, required] Table to validate.
        schema: [raw, required] Schema declaration.
        coerce: [boolean, optional] Coerce types where possible rather than failing. Default
            ``False``.
        lazy: [boolean, optional] Collect every failure rather than stopping at the first. Default
            ``True``.

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
        "du_validate_schema: not implemented."
    )


def du_infer_schema(
    *,
    data: pd.DataFrame,
    strict: bool | None = None,
) -> dict[str, Any]:
    """Node ``du_infer_schema`` -- method card #387.

    Schema validation and data contracts.

    Category 00-data-utilities; memory class ``light``.

    Args:
        data: [df_handle, required] Table to profile.
        strict: [boolean, optional] Infer tight rather than permissive constraints. Default
            ``False``.

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
        "du_infer_schema: not implemented."
    )
