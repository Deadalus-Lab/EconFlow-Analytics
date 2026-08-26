# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``nested_logit`` -- method card #270.

#270 Nested logit demand

Category 31-discrete-choice-demand; module ``nested_logit``.

Reference implementation: pyblp.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c31_discrete_choice_demand import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "dcd_nested_logit_elasticities",
    "dcd_nested_logit_fit",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def dcd_nested_logit_fit(
    *,
    product_data: pd.DataFrame,
    market_ids: str,
    shares: str,
    nesting_ids: str,
    characteristics: Sequence[str] | None = None,
    instruments: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Node ``dcd_nested_logit_fit`` -- method card #270.

    Nested logit demand.

    Category 31-discrete-choice-demand; memory class ``light``.

    Registers its result under ``results``, so a later node can consume it as a handle.

    Args:
        product_data: [df_handle, required] Product-by-market table.
        market_ids: [string, required] Column identifying the market.
        shares: [string, required] Column holding observed shares.
        nesting_ids: [string, required] Column assigning each product to a nest.
        characteristics: [series_codes, optional] Characteristic columns.
        instruments: [series_codes, optional] Excluded instruments for price and the within-nest
            share.

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
        "dcd_nested_logit_fit: not implemented."
    )


def dcd_nested_logit_elasticities(
    *,
    results: Any,
    market_id: str | None = None,
) -> dict[str, Any]:
    """Node ``dcd_nested_logit_elasticities`` -- method card #270.

    Nested logit demand.

    Category 31-discrete-choice-demand; memory class ``light``.

    Args:
        results: [raw_handle, required] Handle to fitted nested-logit results.
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
        "dcd_nested_logit_elasticities: not implemented."
    )
