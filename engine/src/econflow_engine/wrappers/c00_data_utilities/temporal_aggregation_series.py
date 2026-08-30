# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``temporal_aggregation_series`` -- method card #79.

#79 Temporal (dis)aggregation of series (Chow-Lin/Fernandez/Litterman/Denton disaggregation +
    aggregation)

Category 00-data-utilities; module ``temporal_aggregation_series``.

Reference implementation: tsdisagg.

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
    "td_aggregate",
    "td_disaggregate",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def td_disaggregate(
    *,
    formula: str,
    conversion: Literal["sum", "average", "first", "last"] | None = None,
    to: str | None = None,
    method: (
        Literal[
            "chow-lin-maxlog",
            "chow-lin-minrss-ecotrim",
            "chow-lin-minrss-quilis",
            "chow-lin-fixed",
            "dynamic-maxlog",
            "dynamic-minrss",
            "dynamic-fixed",
            "fernandez",
            "litterman-maxlog",
            "litterman-minrss",
            "litterman-fixed",
            "denton-cholette",
            "denton",
            "fast",
            "uniform",
            "ols",
        ]
        | None
    ) = None,
    criterion: Literal["proportional", "additive"] | None = None,
    h: int | None = None,
) -> dict[str, Any]:
    """Node ``td_disaggregate`` -- method card #79.

    Temporal (dis)aggregation of series (Chow-Lin/Fernandez/Litterman/Denton disaggregation +
    aggregation).

    Category 00-data-utilities; memory class ``light``.

    Args:
        formula: [formula, required] lm-like formula (low ~ indicator[s]) or (low ~ 1); the
            indicator MUST cover the low-freq series.
        conversion: [enum, optional] low<->high relation (flow->sum, index/rate->average,
            stock->last/first).
        to: [string, optional] Target frequency (e.g. 'quarterly') when there is no indicator; or an
            integer ratio. Default ``'quarterly'``.
        method: [enum, optional] Disaggregation method (default chow-lin-maxlog with an indicator).
        criterion: [enum, optional] Denton criterion (default proportional).
        h: [integer, optional] Denton differencing order ∈ {0,1,2} (default 1). Default ``1``.

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
        "td_disaggregate: not implemented."
    )


def td_aggregate(
    *,
    x: pd.Series,
    conversion: Literal["sum", "average", "first", "last"] | None = None,
    to: str | None = None,
) -> dict[str, Any]:
    """Node ``td_aggregate`` -- method card #79.

    Temporal (dis)aggregation of series (Chow-Lin/Fernandez/Litterman/Denton disaggregation +
    aggregation).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a high-frequency series/panel to aggregate.
        conversion: [enum, optional] Aggregation function (flow->sum, index/rate->average,
            stock->last/first).
        to: [string, optional] Target frequency (e.g. 'annual') or an integer frequency ratio.
            Default ``'annual'``.

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
        "td_aggregate: not implemented."
    )
