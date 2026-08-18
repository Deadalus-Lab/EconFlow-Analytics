# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``fast_row_column`` -- METHOD-SELECTION card #116.

#116 Fast row/column panel statistics (median/var/sd/quantiles) + a diffusion index (breadth) over a
    numeric wide panel matrix

Category 00-data-utilities; module ``fast_row_column``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c00_data_utilities import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "panel_col_stats",
    "panel_diffusion_index",
    "panel_quantiles",
    "panel_row_stats",
    "NODE_META",
    "wire_model",
]


def panel_row_stats(
    *,
    x: np.ndarray,
    stat: Literal["median", "var", "sd"] | None = None,
    na_rm: bool | None = None,
) -> dict[str, Any]:
    """Node ``panel_row_stats`` -- METHOD-SELECTION card #116.

    Fast row/column panel statistics (median/var/sd/quantiles) + a diffusion index (breadth) over a
    numeric wide panel matrix.

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a numeric panel matrix (rows=time, cols=series).
            Plain numeric matrix — NOT ts/mts/DataFrame.
        stat: [enum, optional] Per-period cross-sectional statistic across the series
            (rowMedians/rowVars/rowSds). Default ``'median'``.
        na_rm: [boolean, optional] Ignore NA; False => NA propagates visibly (NOT a silent drop).
            Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "panel_row_stats: not implemented. The method card is in ./README.md."
    )


def panel_col_stats(
    *,
    x: np.ndarray,
    stat: Literal["median", "var", "sd"] | None = None,
    na_rm: bool | None = None,
) -> dict[str, Any]:
    """Node ``panel_col_stats`` -- METHOD-SELECTION card #116.

    Fast row/column panel statistics (median/var/sd/quantiles) + a diffusion index (breadth) over a
    numeric wide panel matrix.

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a numeric panel matrix (rows=time, cols=series).
        stat: [enum, optional] Per-series over-time statistic of each column
            (colMedians/colVars/colSds). Default ``'median'``.
        na_rm: [boolean, optional] Ignore NA; False => NA propagates visibly. Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "panel_col_stats: not implemented. The method card is in ./README.md."
    )


def panel_quantiles(
    *,
    x: np.ndarray,
    probs: Sequence[float] | None = None,
    type: int | None = None,
    na_rm: bool | None = None,
) -> dict[str, Any]:
    """Node ``panel_quantiles`` -- METHOD-SELECTION card #116.

    Fast row/column panel statistics (median/var/sd/quantiles) + a diffusion index (breadth) over a
    numeric wide panel matrix.

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a numeric panel matrix (rows=time, cols=series).
        probs: [num_array, optional] Quantile probabilities in [0,1] (cross-sectional per period;
            rowQuantiles). Default ``[0, 0.25, 0.5, 0.75, 1]``.
        type: [integer, optional] Quantile algorithm integer 1..9 (the quantile estimator type).
            Default ``7``.
        na_rm: [boolean, optional] Ignore NA when computing the quantiles. Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "panel_quantiles: not implemented. The method card is in ./README.md."
    )


def panel_diffusion_index(
    *,
    x: np.ndarray,
    na_rm: bool | None = None,
) -> dict[str, Any]:
    """Node ``panel_diffusion_index`` -- METHOD-SELECTION card #116.

    Fast row/column panel statistics (median/var/sd/quantiles) + a diffusion index (breadth) over a
    numeric wide panel matrix.

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a numeric panel matrix (rows=time >=2, cols=series).
        na_rm: [boolean, optional] Ignore series with an NA change; False => the period becomes NA.
            Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "panel_diffusion_index: not implemented. The method card is in ./README.md."
    )
