# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``trade_indices`` -- method card #596.

#596 Trade indices: revealed comparative advantage, Lafay and Grubel-Lloyd

Category 28-trade-gravity; module ``trade_indices``.

Reference implementation: pandas.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c28_trade_gravity import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "tg_trade_indices",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def tg_trade_indices(
    *,
    trade: pd.DataFrame,
    country: str,
    product: str,
    exports: str,
    imports: str | None = None,
    indices: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Node ``tg_trade_indices`` -- method card #596.

    Trade indices: revealed comparative advantage, Lafay and Grubel-Lloyd.

    Category 28-trade-gravity; memory class ``light``.

    Args:
        trade: [df_handle, required] Trade flows by country and product.
        country: [string, required] Country identifier.
        product: [string, required] Product identifier.
        exports: [string, required] Export value column.
        imports: [string, optional] Import value column.
        indices: [series_codes, optional] Indices to compute; omitted = the standard set.

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
        "tg_trade_indices: not implemented."
    )
