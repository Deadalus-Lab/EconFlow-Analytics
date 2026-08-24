# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``multilateral_indices`` -- method card #487.

#487 Multilateral and scanner-data price indices: GEKS and time-product dummy

Category 11-decomposition-accounting; module ``multilateral_indices``.

Reference implementation: PriceIndexCalc.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c11_decomposition_accounting import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "da_multilateral_index",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def da_multilateral_index(
    *,
    data: pd.DataFrame,
    product: str,
    period: str,
    price: str,
    quantity: str | None = None,
    method: Literal["geks", "tpd", "gk", "tornqvist", "jevons"] | None = None,
    window: int | None = None,
    splice: Literal["movement", "window", "half", "mean"] | None = None,
) -> dict[str, Any]:
    """Node ``da_multilateral_index`` -- method card #487.

    Multilateral and scanner-data price indices: GEKS and time-product dummy.

    Category 11-decomposition-accounting; memory class ``light``.

    Args:
        data: [df_handle, required] Transaction data: product, period, price and quantity.
        product: [string, required] Product identifier.
        period: [string, required] Period identifier.
        price: [string, required] Price column.
        quantity: [string, optional] Quantity column.
        method: [enum, optional] Index method. Default ``'geks'``.
        window: [integer, optional] Estimation window in periods. Default ``13``.
        splice: [enum, optional] Splicing method. Default ``'movement'``.

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
        "da_multilateral_index: not implemented."
    )
