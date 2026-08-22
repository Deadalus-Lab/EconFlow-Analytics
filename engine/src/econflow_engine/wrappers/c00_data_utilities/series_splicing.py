# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``series_splicing`` -- method card #380.

#380 Series splicing, linking and backcasting

Category 00-data-utilities; module ``series_splicing``.

Reference implementation: pandas.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c00_data_utilities import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "du_backcast",
    "du_splice_series",
    "NODE_META",
    "wire_model",
]


def du_splice_series(
    *,
    series: pd.DataFrame,
    method: Literal["ratio", "difference", "mean_ratio"] | None = None,
    overlap: int | None = None,
    anchor: Literal["latest", "earliest"] | None = None,
) -> dict[str, Any]:
    """Node ``du_splice_series`` -- method card #380.

    Series splicing, linking and backcasting.

    Category 00-data-utilities; memory class ``light``.

    Args:
        series: [multiseries_handle, required] Overlapping vintages, oldest first.
        method: [enum, optional] Link method. Default ``'ratio'``.
        overlap: [integer, optional] Periods of overlap used for the link. Default ``1``.
        anchor: [enum, optional] Which vintage sets the level. Default ``'latest'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "du_splice_series: not implemented."
    )


def du_backcast(
    *,
    target: pd.Series,
    indicator: pd.Series,
    method: Literal["regression", "ratio", "growth_rate"] | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``du_backcast`` -- method card #380.

    Series splicing, linking and backcasting.

    Category 00-data-utilities; memory class ``light``.

    Args:
        target: [series_handle, required] Short series to extend backwards.
        indicator: [series_handle, required] Longer related indicator.
        method: [enum, optional] Backcast method. Default ``'regression'``.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "du_backcast: not implemented."
    )
