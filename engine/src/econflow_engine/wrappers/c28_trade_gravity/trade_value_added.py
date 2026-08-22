# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``trade_value_added`` -- method card #595.

#595 Trade in value added and global value-chain participation

Category 28-trade-gravity; module ``trade_value_added``.

Reference implementation: pymrio.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

from econflow_engine.generated.args.c28_trade_gravity import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "tg_gvc_participation",
    "tg_trade_value_added",
    "NODE_META",
    "wire_model",
]


def tg_trade_value_added(
    *,
    io_table: Any,
    decomposition: Literal["koopman_wang_wei", "borin_mancini", "wang_wei_zhu"] | None = None,
    country: str | None = None,
) -> dict[str, Any]:
    """Node ``tg_trade_value_added`` -- method card #595.

    Trade in value added and global value-chain participation.

    Category 28-trade-gravity; memory class ``light``.

    Args:
        io_table: [raw_handle, required] Handle to a multi-regional input-output system.
        decomposition: [enum, optional] Decomposition. Default ``'koopman_wang_wei'``.
        country: [string, optional] Country to report for; omitted = all.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "tg_trade_value_added: not implemented."
    )


def tg_gvc_participation(
    *,
    io_table: Any,
    measures: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Node ``tg_gvc_participation`` -- method card #595.

    Trade in value added and global value-chain participation.

    Category 28-trade-gravity; memory class ``light``.

    Args:
        io_table: [raw_handle, required] Handle to a multi-regional input-output system.
        measures: [series_codes, optional] Measures to compute.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "tg_gvc_participation: not implemented."
    )
