# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``blp_instruments`` -- method card #267.

#267 Optimal instruments and differentiation instruments for demand systems

Category 31-discrete-choice-demand; module ``blp_instruments``.

Reference implementation: pyblp.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c31_discrete_choice_demand import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "dcd_blp_instruments",
    "dcd_optimal_instruments",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def dcd_blp_instruments(
    *,
    product_data: pd.DataFrame,
    market_ids: str,
    characteristics: Sequence[str] | None = None,
    kind: Literal["blp", "differentiation", "local", "quadratic"] | None = None,
) -> dict[str, Any]:
    """Node ``dcd_blp_instruments`` -- method card #267.

    Optimal instruments and differentiation instruments for demand systems.

    Category 31-discrete-choice-demand; memory class ``light``.

    Args:
        product_data: [df_handle, required] Product-by-market table.
        market_ids: [string, required] Column identifying the market.
        characteristics: [series_codes, optional] Characteristic columns the instruments are built
            from.
        kind: [enum, optional] Instrument family. Default ``'differentiation'``.

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
        "dcd_blp_instruments: not implemented."
    )


def dcd_optimal_instruments(
    *,
    results: Any,
    method: Literal["approximate", "monte_carlo"] | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``dcd_optimal_instruments`` -- method card #267.

    Optimal instruments and differentiation instruments for demand systems.

    Category 31-discrete-choice-demand; memory class ``light``.

    Args:
        results: [raw_handle, required] Handle to consistent first-stage BLP results.
        method: [enum, optional] How the expectation is approximated. Default ``'approximate'``.
        seed: [integer, optional] Seed for the random number generator.

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
        "dcd_optimal_instruments: not implemented."
    )
