# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``liquidity_measures`` -- method card #334.

#334 Amihud illiquidity, turnover and zero-return measures

Category 39-market-microstructure; module ``liquidity_measures``.

Reference implementation: 10.1016/s1386-4181(01)00024-6.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any

import pandas as pd

from econflow_engine.generated.args.c39_market_microstructure import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ms_amihud",
    "ms_liquidity_panel",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def ms_amihud(
    *,
    returns: pd.Series,
    volume: pd.Series,
    window: int | None = None,
    min_observations: int | None = None,
) -> dict[str, Any]:
    """Node ``ms_amihud`` -- method card #334.

    Amihud illiquidity, turnover and zero-return measures.

    Category 39-market-microstructure; memory class ``light``.

    Args:
        returns: [series_handle, required] Daily returns.
        volume: [series_handle, required] Daily dollar volume.
        window: [integer, optional] Aggregation window in days. Default ``21``.
        min_observations: [integer, optional] Minimum non-zero-volume days required. Default ``15``.

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
        "ms_amihud: not implemented."
    )


def ms_liquidity_panel(
    *,
    returns: pd.Series,
    volume: pd.Series,
    shares_outstanding: pd.Series | None = None,
    window: int | None = None,
) -> dict[str, Any]:
    """Node ``ms_liquidity_panel`` -- method card #334.

    Amihud illiquidity, turnover and zero-return measures.

    Category 39-market-microstructure; memory class ``light``.

    Args:
        returns: [series_handle, required] Daily returns.
        volume: [series_handle, required] Daily share volume.
        shares_outstanding: [series_handle, optional] Shares outstanding for turnover.
        window: [integer, optional] Aggregation window in days. Default ``21``.

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
        "ms_liquidity_panel: not implemented."
    )
