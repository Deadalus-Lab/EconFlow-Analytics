# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``seasonality`` -- method card #125.

#125 Seasonality tests (combined/QS/Friedman/Kruskal-Wallis/seasonal-dummies/Welch/OCSB)

Category 01-preparation-prechecks; module ``seasonality``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c01_preparation_prechecks import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "friedman_test",
    "kw_test",
    "ocsb_test",
    "qs_test",
    "run_seasonality_test",
    "seasonal_dummy_test",
    "welch_test",
    "NODE_META",
    "wire_model",
]


def run_seasonality_test(
    *,
    x: pd.Series,
    test: Literal["combined", "qs", "fried", "kw", "seasdum", "welch", "ocsb"] | None = None,
    freq: int | None = None,
    alpha: float | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``run_seasonality_test`` -- method card #125.

    Seasonality tests (combined/QS/Friedman/Kruskal-Wallis/seasonal-dummies/Welch/OCSB).

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a univariate ts (frequency>1, no NA, >=3 seasonal
            cycles).
        test: [enum, optional] Seasonality test (default combined). 'ocsb' has INVERTED polarity
            (seasonal unit root).
        freq: [integer, optional] Optional frequency override (integer >1)· default = frequency(x).
        alpha: [number, optional] p-value threshold (default 0.01, as in isSeasonal). Ignored for
            test='combined'. Default ``0.01``.
        seed: [integer, optional] Monte-Carlo seed· used ONLY for test='ocsb'. Default ``123``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "run_seasonality_test: not implemented."
    )


def qs_test(
    *,
    x: pd.Series,
    freq: int | None = None,
    diff: bool | None = None,
    residuals: bool | None = None,
    autoarima: bool | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``qs_test`` -- method card #125.

    Seasonality tests (combined/QS/Friedman/Kruskal-Wallis/seasonal-dummies/Welch/OCSB).

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a univariate ts (frequency>1, no NA, >=3 seasonal
            cycles).
        freq: [integer, optional] Optional frequency override (integer >1).
        diff: [boolean, optional] Test the differenced series (default True). Default ``True``.
        residuals: [boolean, optional] Test the residuals of an ARIMA (default False). Default
            ``False``.
        autoarima: [boolean, optional] Auto ARIMA instead of (0,1,1) when residuals=True (default
            True). Default ``True``.
        alpha: [number, optional] Decision significance level (default 0.05). Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "qs_test: not implemented."
    )


def friedman_test(
    *,
    x: pd.Series,
    freq: int | None = None,
    diff: bool | None = None,
    residuals: bool | None = None,
    autoarima: bool | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``friedman_test`` -- method card #125.

    Seasonality tests (combined/QS/Friedman/Kruskal-Wallis/seasonal-dummies/Welch/OCSB).

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a univariate ts (frequency>1, no NA, >=3 seasonal
            cycles).
        freq: [integer, optional] Optional frequency override (integer >1).
        diff: [boolean, optional] Test the differenced series (default True). Default ``True``.
        residuals: [boolean, optional] Test the residuals of an ARIMA (default False). Default
            ``False``.
        autoarima: [boolean, optional] Auto ARIMA instead of (0,1,1) when residuals=True (default
            True). Default ``True``.
        alpha: [number, optional] Decision significance level (default 0.05). Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "friedman_test: not implemented."
    )


def kw_test(
    *,
    x: pd.Series,
    freq: int | None = None,
    diff: bool | None = None,
    residuals: bool | None = None,
    autoarima: bool | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``kw_test`` -- method card #125.

    Seasonality tests (combined/QS/Friedman/Kruskal-Wallis/seasonal-dummies/Welch/OCSB).

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a univariate ts (frequency>1, no NA, >=3 seasonal
            cycles).
        freq: [integer, optional] Optional frequency override (integer >1).
        diff: [boolean, optional] Test the differenced series (default True). Default ``True``.
        residuals: [boolean, optional] Test the residuals of an ARIMA (default False). Default
            ``False``.
        autoarima: [boolean, optional] Auto ARIMA instead of (0,1,1) when residuals=True (default
            True). Default ``True``.
        alpha: [number, optional] Decision significance level (default 0.05). Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "kw_test: not implemented."
    )


def seasonal_dummy_test(
    *,
    x: pd.Series,
    freq: int | None = None,
    autoarima: bool | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``seasonal_dummy_test`` -- method card #125.

    Seasonality tests (combined/QS/Friedman/Kruskal-Wallis/seasonal-dummies/Welch/OCSB).

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a univariate ts (frequency>1, no NA, >=3 seasonal
            cycles).
        freq: [integer, optional] Optional frequency override (integer >1).
        autoarima: [boolean, optional] Auto ARIMA (p,d,q)+seasonal dummies instead of (0,1,1)
            (default False). Default ``False``.
        alpha: [number, optional] Decision significance level (default 0.05). Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "seasonal_dummy_test: not implemented."
    )


def welch_test(
    *,
    x: pd.Series,
    freq: int | None = None,
    diff: bool | None = None,
    residuals: bool | None = None,
    autoarima: bool | None = None,
    rank: bool | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``welch_test`` -- method card #125.

    Seasonality tests (combined/QS/Friedman/Kruskal-Wallis/seasonal-dummies/Welch/OCSB).

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a univariate ts (frequency>1, no NA, >=3 seasonal
            cycles).
        freq: [integer, optional] Optional frequency override (integer >1).
        diff: [boolean, optional] Test the differenced series (default True). Default ``True``.
        residuals: [boolean, optional] Test the residuals of an ARIMA (default False). Default
            ``False``.
        autoarima: [boolean, optional] Auto ARIMA instead of (0,1,1) when residuals=True (default
            True). Default ``True``.
        rank: [boolean, optional] Use the rank-based variant (default False). Default ``False``.
        alpha: [number, optional] Decision significance level (default 0.05). Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "welch_test: not implemented."
    )


def ocsb_test(
    *,
    x: pd.Series,
    seed: int,
    method: Literal["OLS", "ML"] | None = None,
    augmentations: Sequence[int] | None = None,
    freq: int | None = None,
    nrun: int | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``ocsb_test`` -- method card #125.

    Seasonality tests (combined/QS/Friedman/Kruskal-Wallis/seasonal-dummies/Welch/OCSB).

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a univariate ts (frequency>1, no NA, >=3 seasonal
            cycles).
        seed: [integer, required] MANDATORY Monte-Carlo seed (determinism· same seed => same
            p-value).
        method: [enum, optional] OLS (default) or ML seasonal AR test regression.
        augmentations: [int_array, optional] [regular, seasonal] non-negative augmentation orders
            (default [3,0]). Default ``[3, 0]``.
        freq: [integer, optional] Optional frequency override (integer >1).
        nrun: [integer, optional] Number of runs in the Monte-Carlo simulation (default 1000).
            Default ``1000``.
        alpha: [number, optional] p-value threshold (H0 = seasonal unit root· fail-to-reject =>
            seasonal). Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ocsb_test: not implemented."
    )
