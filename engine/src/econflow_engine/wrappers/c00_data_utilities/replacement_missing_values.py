# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``replacement_missing_values`` -- method card #80.

#80 Replacement of missing values in time series (Kalman / interpolation / seasonally-decomposed + a
    missingness report)

Category 00-data-utilities; module ``replacement_missing_values``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

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
    "impute_interpolation",
    "impute_kalman",
    "impute_missing_stats",
    "impute_seasonal_decomposed",
    "NODE_META",
    "wire_model",
]


def impute_kalman(
    *,
    x: pd.Series,
    model: Literal["structural", "auto_arima"] | None = None,
    smooth: bool | None = None,
    maxgap: float | None = None,
) -> dict[str, Any]:
    """Node ``impute_kalman`` -- method card #80.

    Replacement of missing values in time series (Kalman / interpolation / seasonally-decomposed + a
    missingness report).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a univariate series with NA (>=2 non-NA values).
        model: [enum, optional] State-space model (default structural).
        smooth: [boolean, optional] True=Kalman Smoothing, False=Kalman Run (default True). Default
            ``True``.
        maxgap: [number, optional] Maximum length of a consecutive NA run that is filled (default
            Inf = no limit).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "impute_kalman: not implemented."
    )


def impute_interpolation(
    *,
    x: pd.Series,
    option: Literal["linear", "spline", "stine"] | None = None,
    maxgap: float | None = None,
) -> dict[str, Any]:
    """Node ``impute_interpolation`` -- method card #80.

    Replacement of missing values in time series (Kalman / interpolation / seasonally-decomposed + a
    missingness report).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a univariate series with NA.
        option: [enum, optional] Interpolation type (default linear).
        maxgap: [number, optional] Maximum NA-gap length that is filled (default Inf).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "impute_interpolation: not implemented."
    )


def impute_seasonal_decomposed(
    *,
    x: pd.Series,
    algorithm: Literal["interpolation", "locf", "mean", "random", "kalman", "ma"] | None = None,
    find_frequency: bool | None = None,
    maxgap: float | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``impute_seasonal_decomposed`` -- method card #80.

    Replacement of missing values in time series (Kalman / interpolation / seasonally-decomposed + a
    missingness report).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a seasonal ts (freq>1, >=2 periods) with NA.
        algorithm: [enum, optional] Algorithm applied to the deseasonalized series (default
            interpolation).
        find_frequency: [boolean, optional] Automatic frequency estimation (default False). Default
            ``False``.
        maxgap: [number, optional] Maximum NA-gap length that is filled (default Inf).
        seed: [integer, optional] Seed for the stochastic algorithm='random' (reproducibility;
            default 42). Default ``42``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "impute_seasonal_decomposed: not implemented."
    )


def impute_missing_stats(
    *,
    x: pd.Series,
    bins: int | None = None,
) -> dict[str, Any]:
    """Node ``impute_missing_stats`` -- method card #80.

    Replacement of missing values in time series (Kalman / interpolation / seasonally-decomposed + a
    missingness report).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a series, for mapping the NA pattern (as data).
        bins: [integer, optional] Bins of the print-table (default 4; does NOT affect the UNBINNED
            gap_distribution). Default ``4``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "impute_missing_stats: not implemented."
    )
