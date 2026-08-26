# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``trade_classification`` -- method card #336.

#336 Trade classification and order-flow imbalance

Category 39-market-microstructure; module ``trade_classification``.

Reference implementation: 10.1111/j.1540-6261.1991.tb02683.x.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c39_market_microstructure import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ms_classify_trades",
    "ms_order_flow_imbalance",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def ms_classify_trades(
    *,
    price: pd.Series,
    bid: pd.Series | None = None,
    ask: pd.Series | None = None,
    rule: Literal["tick", "quote", "lee_ready", "emo", "clnv"] | None = None,
    quote_lag: float | None = None,
) -> dict[str, Any]:
    """Node ``ms_classify_trades`` -- method card #336.

    Trade classification and order-flow imbalance.

    Category 39-market-microstructure; memory class ``light``.

    Args:
        price: [series_handle, required] Trade price.
        bid: [series_handle, optional] Prevailing bid.
        ask: [series_handle, optional] Prevailing ask.
        rule: [enum, optional] Classification rule. Default ``'lee_ready'``.
        quote_lag: [number, optional] Quote alignment offset in seconds. Default ``0.0``.

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
        "ms_classify_trades: not implemented."
    )


def ms_order_flow_imbalance(
    *,
    signed_volume: pd.Series,
    frequency: Literal["1min", "5min", "15min", "30min", "1h", "daily"] | None = None,
) -> dict[str, Any]:
    """Node ``ms_order_flow_imbalance`` -- method card #336.

    Trade classification and order-flow imbalance.

    Category 39-market-microstructure; memory class ``light``.

    Args:
        signed_volume: [series_handle, required] Signed trade volume.
        frequency: [enum, optional] Aggregation frequency. Default ``'5min'``.

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
        "ms_order_flow_imbalance: not implemented."
    )
