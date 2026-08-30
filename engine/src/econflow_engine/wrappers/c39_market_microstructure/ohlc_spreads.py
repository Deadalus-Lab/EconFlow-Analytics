# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``ohlc_spreads`` -- method card #333.

#333 OHLC spread estimators: Roll, Corwin-Schultz, Abdi-Ranaldo and EDGE

Category 39-market-microstructure; module ``ohlc_spreads``.

Reference implementation: bidask.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c39_market_microstructure import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ms_ohlc_spread",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def ms_ohlc_spread(
    *,
    open: pd.Series,
    high: pd.Series,
    low: pd.Series,
    close: pd.Series,
    estimator: Literal["roll", "corwin_schultz", "abdi_ranaldo", "edge"] | None = None,
    negative: Literal["keep", "zero", "drop"] | None = None,
    window: int | None = None,
) -> dict[str, Any]:
    """Node ``ms_ohlc_spread`` -- method card #333.

    OHLC spread estimators: Roll, Corwin-Schultz, Abdi-Ranaldo and EDGE.

    Category 39-market-microstructure; memory class ``light``.

    Args:
        open: [series_handle, required] Open price.
        high: [series_handle, required] High price.
        low: [series_handle, required] Low price.
        close: [series_handle, required] Close price.
        estimator: [enum, optional] Estimator family. Default ``'edge'``.
        negative: [enum, optional] Handling of negative estimates. Default ``'zero'``.
        window: [integer, optional] Rolling window in periods; omitted = full sample.

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
        "ms_ohlc_spread: not implemented."
    )
