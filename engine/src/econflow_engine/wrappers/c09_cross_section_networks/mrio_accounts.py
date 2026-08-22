# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``mrio_accounts`` -- method card #474.

#474 Multi-regional input-output and environmentally extended accounts

Category 09-cross-section-networks; module ``mrio_accounts``.

Reference implementation: pymrio.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c09_cross_section_networks import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "cs_mrio_load",
    "cs_mrio_multipliers",
    "NODE_META",
    "wire_model",
]


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
    """
    raise NotImplementedError(
        "cs_mrio_multipliers: not implemented."
    )
