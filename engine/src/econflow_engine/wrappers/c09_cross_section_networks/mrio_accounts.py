# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``mrio_accounts`` -- method card #474.

#474 Multi-regional input-output and environmentally extended accounts

Category 09-cross-section-networks; module ``mrio_accounts``.

Reference implementation: pymrio.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c09_cross_section_networks import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "cs_mrio_load",
    "cs_mrio_multipliers",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def cs_mrio_load(
    *,
    path: str,
    year: int | None = None,
    aggregate: pd.DataFrame | None = None,
) -> dict[str, Any]:
    """Node ``cs_mrio_load`` -- method card #474.

    Multi-regional input-output and environmentally extended accounts.

    Category 09-cross-section-networks; memory class ``light``.

    Registers its result under ``io_table``, so a later node can consume it as a handle.

    Args:
        path: [path, required] Object-store path to the table.
        year: [integer, optional] Year to load.
        aggregate: [df_handle, optional] Region or sector aggregation mapping.

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
        "cs_mrio_load: not implemented."
    )


def cs_mrio_multipliers(
    *,
    io_table: Any,
    kind: Literal["output", "value_added", "employment", "emissions"] | None = None,
) -> dict[str, Any]:
    """Node ``cs_mrio_multipliers`` -- method card #474.

    Multi-regional input-output and environmentally extended accounts.

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        io_table: [raw_handle, required] Handle to a loaded system.
        kind: [enum, optional] Multiplier type. Default ``'output'``.

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
        "cs_mrio_multipliers: not implemented."
    )
