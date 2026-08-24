# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``choice_welfare`` -- method card #273.

#273 Willingness to pay, compensating variation and consumer welfare from discrete choice

Category 31-discrete-choice-demand; module ``choice_welfare``.

Reference implementation: pyblp.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c31_discrete_choice_demand import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "dcd_compensating_variation",
    "dcd_consumer_surplus",
    "dcd_wtp",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def dcd_wtp(
    *,
    results: Any,
    price_variable: str | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``dcd_wtp`` -- method card #273.

    Willingness to pay, compensating variation and consumer welfare from discrete choice.

    Category 31-discrete-choice-demand; memory class ``light``.

    Args:
        results: [raw_handle, required] Handle to fitted demand results.
        price_variable: [string, optional] Name of the price coefficient. Default ``'prices'``.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

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
        "dcd_wtp: not implemented."
    )


def dcd_compensating_variation(
    *,
    results: Any,
    prices_post: pd.Series | None = None,
    available_post: pd.Series | None = None,
) -> dict[str, Any]:
    """Node ``dcd_compensating_variation`` -- method card #273.

    Willingness to pay, compensating variation and consumer welfare from discrete choice.

    Category 31-discrete-choice-demand; memory class ``light``.

    Args:
        results: [raw_handle, required] Handle to fitted demand results.
        prices_post: [series_handle, optional] Counterfactual prices.
        available_post: [series_handle, optional] Counterfactual availability flags.

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
        "dcd_compensating_variation: not implemented."
    )


def dcd_consumer_surplus(
    *,
    results: Any,
    market_id: str | None = None,
) -> dict[str, Any]:
    """Node ``dcd_consumer_surplus`` -- method card #273.

    Willingness to pay, compensating variation and consumer welfare from discrete choice.

    Category 31-discrete-choice-demand; memory class ``light``.

    Args:
        results: [raw_handle, required] Handle to fitted demand results.
        market_id: [string, optional] Restrict to one market.

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
        "dcd_consumer_surplus: not implemented."
    )
