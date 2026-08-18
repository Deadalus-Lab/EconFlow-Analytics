# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``fast_transformation`` -- METHOD-SELECTION card #103.

#103 Fast (grouped/panel) data transformation
    (fgrowth/fdiff/flag/fcumsum/fscale/fwithin/collap/qsu/TRA)

Category 00-data-utilities; module ``fast_transformation``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c00_data_utilities import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "cll_collap",
    "cll_cumsum",
    "cll_diff",
    "cll_growth",
    "cll_lag",
    "cll_qsu",
    "cll_scale",
    "cll_transform",
    "cll_within",
    "NODE_META",
    "wire_model",
]


def cll_growth(
    *,
    x: pd.Series,
    n: int | None = None,
    diff: int | None = None,
    logdiff: bool | None = None,
    scale: float | None = None,
    power: float | None = None,
    g: Sequence[str] | None = None,
    t: Sequence[float] | None = None,
    fill: float | None = None,
) -> dict[str, Any]:
    """Node ``cll_growth`` -- METHOD-SELECTION card #103.

    Fast (grouped/panel) data transformation
    (fgrowth/fdiff/flag/fcumsum/fscale/fwithin/collap/qsu/TRA).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a series.
        n: [integer, optional] Lag order (default 1). Default ``1``.
        diff: [integer, optional] Iteration order >=1 (default 1). Default ``1``.
        logdiff: [boolean, optional] Log-difference growth (default False = exact %). Default
            ``False``.
        scale: [number, optional] Scale (default 100 = percentages). Default ``100``.
        power: [number, optional] Annualization exponent (default 1). Default ``1``.
        g: [series_codes, optional] Panel grouping labels (length = observations).
        t: [num_array, optional] Time vector (without g: NO duplicates).
        fill: [number, optional] Padding value (default NA).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cll_growth: not implemented. The method card is in ./README.md."
    )


def cll_diff(
    *,
    x: pd.Series,
    n: int | None = None,
    diff: int | None = None,
    log: bool | None = None,
    rho: float | None = None,
    g: Sequence[str] | None = None,
    t: Sequence[float] | None = None,
    fill: float | None = None,
) -> dict[str, Any]:
    """Node ``cll_diff`` -- METHOD-SELECTION card #103.

    Fast (grouped/panel) data transformation
    (fgrowth/fdiff/flag/fcumsum/fscale/fwithin/collap/qsu/TRA).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a series.
        n: [integer, optional] Lag order (default 1). Default ``1``.
        diff: [integer, optional] Iteration order >=1 (default 1). Default ``1``.
        log: [boolean, optional] Log-difference (default False). Default ``False``.
        rho: [number, optional] Quasi-differencing coef (rho=1 = plain difference). Default ``1``.
        g: [series_codes, optional] Panel grouping labels.
        t: [num_array, optional] Time vector.
        fill: [number, optional] Padding value (default NA).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cll_diff: not implemented. The method card is in ./README.md."
    )


def cll_lag(
    *,
    x: pd.Series,
    n: int | None = None,
    g: Sequence[str] | None = None,
    t: Sequence[float] | None = None,
    fill: float | None = None,
) -> dict[str, Any]:
    """Node ``cll_lag`` -- METHOD-SELECTION card #103.

    Fast (grouped/panel) data transformation
    (fgrowth/fdiff/flag/fcumsum/fscale/fwithin/collap/qsu/TRA).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a series.
        n: [integer, optional] n>0 lag, n<0 lead (default 1). Default ``1``.
        g: [series_codes, optional] Panel grouping labels.
        t: [num_array, optional] Time vector.
        fill: [number, optional] Padding value (default NA).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cll_lag: not implemented. The method card is in ./README.md."
    )


def cll_cumsum(
    *,
    x: pd.Series,
    g: Sequence[str] | None = None,
    na_rm: bool | None = None,
    fill: bool | None = None,
) -> dict[str, Any]:
    """Node ``cll_cumsum`` -- METHOD-SELECTION card #103.

    Fast (grouped/panel) data transformation
    (fgrowth/fdiff/flag/fcumsum/fscale/fwithin/collap/qsu/TRA).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a series.
        g: [series_codes, optional] Panel grouping labels (grouped cumsum).
        na_rm: [boolean, optional] Ignore NA (default True). Default ``True``.
        fill: [boolean, optional] Fill NA with the previous sum (default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cll_cumsum: not implemented. The method card is in ./README.md."
    )


def cll_scale(
    *,
    x: pd.Series,
    g: Sequence[str] | None = None,
    w: Sequence[float] | None = None,
    na_rm: bool | None = None,
    mean: float | None = None,
    sd: float | None = None,
) -> dict[str, Any]:
    """Node ``cll_scale`` -- METHOD-SELECTION card #103.

    Fast (grouped/panel) data transformation
    (fgrowth/fdiff/flag/fcumsum/fscale/fwithin/collap/qsu/TRA).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a series.
        g: [series_codes, optional] Panel grouping labels (within-group z-scores).
        w: [num_array, optional] Weights (length = observations).
        na_rm: [boolean, optional] Ignore NA (default True). Default ``True``.
        mean: [number, optional] Target mean (default 0). Default ``0``.
        sd: [number, optional] Target sd (default 1; a constant series -> NaN, honestly). Default
            ``1``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cll_scale: not implemented. The method card is in ./README.md."
    )


def cll_within(
    *,
    x: pd.Series,
    g: Sequence[str] | None = None,
    w: Sequence[float] | None = None,
    na_rm: bool | None = None,
    mean: float | None = None,
    theta: float | None = None,
) -> dict[str, Any]:
    """Node ``cll_within`` -- METHOD-SELECTION card #103.

    Fast (grouped/panel) data transformation
    (fgrowth/fdiff/flag/fcumsum/fscale/fwithin/collap/qsu/TRA).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a series.
        g: [series_codes, optional] Panel grouping labels (within/demean).
        w: [num_array, optional] Weights.
        na_rm: [boolean, optional] Ignore NA (default True). Default ``True``.
        mean: [number, optional] Value added back after centering (default 0). Default ``0``.
        theta: [number, optional] theta=1 plain within, 0<theta<1 quasi-demean (RE-style). Default
            ``1``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cll_within: not implemented. The method card is in ./README.md."
    )


def cll_collap(
    *,
    X: pd.DataFrame,
    by: Sequence[str],
    FUN: (
        Literal[
            "mean",
            "sum",
            "median",
            "min",
            "max",
            "sd",
            "first",
            "last",
            "prod",
            "nobs",
        ]
        | None
    ) = None,
    cols: Sequence[str] | None = None,
    w: Sequence[float] | None = None,
) -> dict[str, Any]:
    """Node ``cll_collap`` -- METHOD-SELECTION card #103.

    Fast (grouped/panel) data transformation
    (fgrowth/fdiff/flag/fcumsum/fscale/fwithin/collap/qsu/TRA).

    Category 00-data-utilities; memory class ``light``.

    Args:
        X: [df_handle, required] Handle to a (panel) DataFrame to aggregate.
        by: [series_codes, required] Grouping columns (names).
        FUN: [enum, optional] Fast statistical function per numeric column (default mean).
        cols: [series_codes, optional] Subset of columns to aggregate.
        w: [num_array, optional] Weights; ONLY the weighted fast-stat funcs
            (mean/sum/median/sd/prod) use them — first/last/min/max/nobs ignore them (warning).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cll_collap: not implemented. The method card is in ./README.md."
    )


def cll_qsu(
    *,
    x: pd.DataFrame,
    g: Sequence[str] | None = None,
    w: Sequence[float] | None = None,
    higher: bool | None = None,
) -> dict[str, Any]:
    """Node ``cll_qsu`` -- METHOD-SELECTION card #103.

    Fast (grouped/panel) data transformation
    (fgrowth/fdiff/flag/fcumsum/fscale/fwithin/collap/qsu/TRA).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [df_handle, required] Handle to a DataFrame (per-column summary).
        g: [series_codes, optional] Grouping labels (routed as 'by' for a DataFrame — otherwise
            SILENTLY IGNORED).
        w: [num_array, optional] Weights.
        higher: [boolean, optional] Add Skew & Kurt (default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cll_qsu: not implemented. The method card is in ./README.md."
    )


def cll_transform(
    *,
    x: pd.Series,
    STATS: Sequence[float],
    FUN: (
        Literal[
            "-",
            "replace_na",
            "replace_fill",
            "replace",
            "-+",
            "/",
            "%",
            "+",
            "*",
            "%%",
            "-%%",
        ]
        | None
    ) = None,
    g: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Node ``cll_transform`` -- METHOD-SELECTION card #103.

    Fast (grouped/panel) data transformation
    (fgrowth/fdiff/flag/fcumsum/fscale/fwithin/collap/qsu/TRA).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a series.
        STATS: [num_array, required] Statistics (atomic if g=None; one per group if grouped).
        FUN: [enum, optional] Sweep-out operation (default '-' center); '-+' requires groups.
        g: [series_codes, optional] Panel grouping labels.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cll_transform: not implemented. The method card is in ./README.md."
    )
