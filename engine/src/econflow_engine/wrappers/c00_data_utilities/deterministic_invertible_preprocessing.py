# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``deterministic_invertible_preprocessing`` -- METHOD-SELECTION card #104.

#104 Deterministic invertible preprocessing transforms
    (diff/standardize/normalize/box_cox/auto_lambda + tk_augment_lags/differences + pad_by_time)

Category 00-data-utilities; module ``deterministic_invertible_preprocessing``.

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
    "ttk_augment_differences",
    "ttk_augment_lags",
    "ttk_auto_lambda",
    "ttk_box_cox",
    "ttk_diff",
    "ttk_diff_inv",
    "ttk_normalize",
    "ttk_pad_by_time",
    "ttk_standardize",
    "NODE_META",
    "wire_model",
]


def ttk_diff(
    *,
    x: pd.Series,
    lag: int | None = None,
    difference: int | None = None,
    log: bool | None = None,
) -> dict[str, Any]:
    """Node ``ttk_diff`` -- METHOD-SELECTION card #104.

    Deterministic invertible preprocessing transforms
    (diff/standardize/normalize/box_cox/auto_lambda + tk_augment_lags/differences + pad_by_time).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a numeric series.
        lag: [integer, optional] Lag order >=1 (default 1). Default ``1``.
        difference: [integer, optional] Differencing order >=1 (lag*difference < length). Default
            ``1``.
        log: [boolean, optional] Log-difference (default False; requires x>0). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ttk_diff: not implemented. The method card is in ./README.md."
    )


def ttk_diff_inv(
    *,
    x: pd.Series,
    initial_values: Sequence[float] | None = None,
    lag: int | None = None,
    difference: int | None = None,
    log: bool | None = None,
) -> dict[str, Any]:
    """Node ``ttk_diff_inv`` -- METHOD-SELECTION card #104.

    Deterministic invertible preprocessing transforms
    (diff/standardize/normalize/box_cox/auto_lambda + tk_augment_lags/differences + pad_by_time).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a DIFFERENCED series (with leading NA).
        initial_values: [num_array, optional] The first lag*difference elements of the original
            series (for a full inversion).
        lag: [integer, optional] Same lag as the differencing. Default ``1``.
        difference: [integer, optional] Same difference. Default ``1``.
        log: [boolean, optional] Log-difference inversion (default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ttk_diff_inv: not implemented. The method card is in ./README.md."
    )


def ttk_standardize(
    *,
    x: pd.Series,
) -> dict[str, Any]:
    """Node ``ttk_standardize`` -- METHOD-SELECTION card #104.

    Deterministic invertible preprocessing transforms
    (diff/standardize/normalize/box_cox/auto_lambda + tk_augment_lags/differences + pad_by_time).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a series (n>=2, sd>0; no NA/Inf).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ttk_standardize: not implemented. The method card is in ./README.md."
    )


def ttk_normalize(
    *,
    x: pd.Series,
) -> dict[str, Any]:
    """Node ``ttk_normalize`` -- METHOD-SELECTION card #104.

    Deterministic invertible preprocessing transforms
    (diff/standardize/normalize/box_cox/auto_lambda + tk_augment_lags/differences + pad_by_time).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a series (min!=max; no NA/Inf).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ttk_normalize: not implemented. The method card is in ./README.md."
    )


def ttk_box_cox(
    *,
    x: pd.Series,
    lambda_: float | None = None,
    method: Literal["guerrero", "loglik"] | None = None,
    lambda_lower: float | None = None,
    lambda_upper: float | None = None,
) -> dict[str, Any]:
    """Node ``ttk_box_cox`` -- METHOD-SELECTION card #104.

    Deterministic invertible preprocessing transforms
    (diff/standardize/normalize/box_cox/auto_lambda + tk_augment_lags/differences + pad_by_time).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a strictly positive series (x>0).
        lambda_ (wire name ``lambda``): [number, optional] Fixed lambda; OMIT for auto-selection
            (default 'auto').
        method: [enum, optional] Auto-lambda method (default guerrero).
        lambda_lower: [number, optional] Auto lower bound (default -1). Default ``-1``.
        lambda_upper: [number, optional] Auto upper bound (default 2; > lower). Default ``2``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ttk_box_cox: not implemented. The method card is in ./README.md."
    )


def ttk_auto_lambda(
    *,
    x: pd.Series,
    method: Literal["guerrero", "loglik"] | None = None,
    lambda_lower: float | None = None,
    lambda_upper: float | None = None,
) -> dict[str, Any]:
    """Node ``ttk_auto_lambda`` -- METHOD-SELECTION card #104.

    Deterministic invertible preprocessing transforms
    (diff/standardize/normalize/box_cox/auto_lambda + tk_augment_lags/differences + pad_by_time).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a strictly positive series (x>0).
        method: [enum, optional] Method (default guerrero).
        lambda_lower: [number, optional] Lower bound (default -1). Default ``-1``.
        lambda_upper: [number, optional] Upper bound (default 2; > lower). Default ``2``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ttk_auto_lambda: not implemented. The method card is in ./README.md."
    )


def ttk_augment_lags(
    *,
    data: pd.DataFrame,
    value_col: Sequence[str],
    lags: Sequence[int] | None = None,
    new_names: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Node ``ttk_augment_lags`` -- METHOD-SELECTION card #104.

    Deterministic invertible preprocessing transforms
    (diff/standardize/normalize/box_cox/auto_lambda + tk_augment_lags/differences + pad_by_time).

    Category 00-data-utilities; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a long tibble.
        value_col: [series_codes, required] Value column(s) to lag.
        lags: [int_array, optional] Integer lags (negative=lead accepted; default 1). Default ``1``.
        new_names: [series_codes, optional] New column names or 'auto' (default 'auto'). Default
            ``'auto'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ttk_augment_lags: not implemented. The method card is in ./README.md."
    )


def ttk_augment_differences(
    *,
    data: pd.DataFrame,
    value_col: Sequence[str],
    lags: Sequence[int] | None = None,
    differences: int | None = None,
    log: bool | None = None,
    new_names: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Node ``ttk_augment_differences`` -- METHOD-SELECTION card #104.

    Deterministic invertible preprocessing transforms
    (diff/standardize/normalize/box_cox/auto_lambda + tk_augment_lags/differences + pad_by_time).

    Category 00-data-utilities; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a long tibble.
        value_col: [series_codes, required] Value column(s) to difference.
        lags: [int_array, optional] Positive lags (>=1; default 1). Default ``1``.
        differences: [integer, optional] Differencing order >=1 (default 1). Default ``1``.
        log: [boolean, optional] Log-differences (default False; requires column>0). Default
            ``False``.
        new_names: [series_codes, optional] Names or 'auto'. Default ``'auto'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ttk_augment_differences: not implemented. The method card is in ./README.md."
    )


def ttk_pad_by_time(
    *,
    data: pd.DataFrame,
    date_col: str,
    by: str | None = None,
    pad_value: float | None = None,
    fill_na_direction: Literal["none", "down", "up", "downup", "updown"] | None = None,
    start_date: str | None = None,
    end_date: str | None = None,
) -> dict[str, Any]:
    """Node ``ttk_pad_by_time`` -- METHOD-SELECTION card #104.

    Deterministic invertible preprocessing transforms
    (diff/standardize/normalize/box_cox/auto_lambda + tk_augment_lags/differences + pad_by_time).

    Category 00-data-utilities; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a tibble with a Date/POSIXct column.
        date_col: [string, required] Time column name (Date/POSIXct).
        by: [string, optional] Padding step ('auto'/'month'/'5 min'/...; default 'auto'). Default
            ``'auto'``.
        pad_value: [number, optional] Fill value (default NA).
        fill_na_direction: [enum, optional] LOCF/NOCB after the padding (default none).
        start_date: [string, optional] Extend the start of the padding.
        end_date: [string, optional] Extend the end of the padding.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ttk_pad_by_time: not implemented. The method card is in ./README.md."
    )
