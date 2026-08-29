# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``currency_conversion`` -- method card #382.

#382 Currency, purchasing-power-parity and constant-price conversion with group aggregates

Category 00-data-utilities; module ``currency_conversion``.

Reference implementation: pandas.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c00_data_utilities import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "du_convert_currency",
    "du_group_aggregate",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def du_convert_currency(
    *,
    series: pd.DataFrame,
    factors: pd.DataFrame,
    basis: Literal["market", "ppp", "constant_price"] | None = None,
    base_period: str | None = None,
) -> dict[str, Any]:
    """Node ``du_convert_currency`` -- method card #382.

    Currency, purchasing-power-parity and constant-price conversion with group aggregates.

    Category 00-data-utilities; memory class ``light``.

    Args:
        series: [multiseries_handle, required] Series to convert.
        factors: [multiseries_handle, required] Conversion factors, aligned to the series.
        basis: [enum, optional] Conversion basis. Default ``'market'``.
        base_period: [string, optional] Base period for a constant-price conversion.

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
        "du_convert_currency: not implemented."
    )


def du_group_aggregate(
    *,
    series: pd.DataFrame,
    weights: pd.DataFrame | None = None,
    method: Literal["sum", "weighted_mean", "median", "geometric_mean"] | None = None,
) -> dict[str, Any]:
    """Node ``du_group_aggregate`` -- method card #382.

    Currency, purchasing-power-parity and constant-price conversion with group aggregates.

    Category 00-data-utilities; memory class ``light``.

    Args:
        series: [multiseries_handle, required] Converted series.
        weights: [multiseries_handle, optional] Aggregation weights.
        method: [enum, optional] Aggregation function. Default ``'sum'``.

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
        "du_group_aggregate: not implemented."
    )
