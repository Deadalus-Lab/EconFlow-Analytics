# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``deterministic_invertible_preprocessing`` -- method card #104.

#104 Deterministic invertible preprocessing transforms
    (diff/standardize/normalize/box_cox/auto_lambda + lag/difference augmentation + pad_by_time)

Category 00-data-utilities; module ``deterministic_invertible_preprocessing``.

Reference implementation: scikit-learn.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
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
    "prep_augment_differences",
    "prep_augment_lags",
    "prep_auto_lambda",
    "prep_box_cox",
    "prep_diff",
    "prep_diff_inverse",
    "prep_normalize",
    "prep_pad_by_time",
    "prep_standardize",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def prep_diff(
    *,
    x: pd.Series,
    lag: int | None = None,
    difference: int | None = None,
    log: bool | None = None,
) -> dict[str, Any]:
    """Node ``prep_diff`` -- method card #104.

    Deterministic invertible preprocessing transforms
    (diff/standardize/normalize/box_cox/auto_lambda + lag/difference augmentation + pad_by_time).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a numeric series.
        lag: [integer, optional] Lag order >=1 (default 1). Default ``1``.
        difference: [integer, optional] Differencing order >=1 (lag*difference < length). Default
            ``1``.
        log: [boolean, optional] Log-difference (default False; requires x>0). Default ``False``.

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
        "prep_diff: not implemented."
    )


def prep_diff_inverse(
    *,
    x: pd.Series,
    initial_values: Sequence[float] | None = None,
    lag: int | None = None,
    difference: int | None = None,
    log: bool | None = None,
) -> dict[str, Any]:
    """Node ``prep_diff_inverse`` -- method card #104.

    Deterministic invertible preprocessing transforms
    (diff/standardize/normalize/box_cox/auto_lambda + lag/difference augmentation + pad_by_time).

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
        "prep_diff_inverse: not implemented."
    )


def prep_standardize(
    *,
    x: pd.Series,
) -> dict[str, Any]:
    """Node ``prep_standardize`` -- method card #104.

    Deterministic invertible preprocessing transforms
    (diff/standardize/normalize/box_cox/auto_lambda + lag/difference augmentation + pad_by_time).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a series (n>=2, sd>0; no NA/Inf).

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
        "prep_standardize: not implemented."
    )


def prep_normalize(
    *,
    x: pd.Series,
) -> dict[str, Any]:
    """Node ``prep_normalize`` -- method card #104.

    Deterministic invertible preprocessing transforms
    (diff/standardize/normalize/box_cox/auto_lambda + lag/difference augmentation + pad_by_time).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a series (min!=max; no NA/Inf).

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
        "prep_normalize: not implemented."
    )


def prep_box_cox(
    *,
    x: pd.Series,
    lambda_: float | None = None,
    method: Literal["guerrero", "loglik"] | None = None,
    lambda_lower: float | None = None,
    lambda_upper: float | None = None,
) -> dict[str, Any]:
    """Node ``prep_box_cox`` -- method card #104.

    Deterministic invertible preprocessing transforms
    (diff/standardize/normalize/box_cox/auto_lambda + lag/difference augmentation + pad_by_time).

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
        "prep_box_cox: not implemented."
    )


def prep_auto_lambda(
    *,
    x: pd.Series,
    method: Literal["guerrero", "loglik"] | None = None,
    lambda_lower: float | None = None,
    lambda_upper: float | None = None,
) -> dict[str, Any]:
    """Node ``prep_auto_lambda`` -- method card #104.

    Deterministic invertible preprocessing transforms
    (diff/standardize/normalize/box_cox/auto_lambda + lag/difference augmentation + pad_by_time).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a strictly positive series (x>0).
        method: [enum, optional] Method (default guerrero).
        lambda_lower: [number, optional] Lower bound (default -1). Default ``-1``.
        lambda_upper: [number, optional] Upper bound (default 2; > lower). Default ``2``.

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
        "prep_auto_lambda: not implemented."
    )


def prep_augment_lags(
    *,
    data: pd.DataFrame,
    value_col: Sequence[str],
    lags: Sequence[int] | None = None,
    new_names: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Node ``prep_augment_lags`` -- method card #104.

    Deterministic invertible preprocessing transforms
    (diff/standardize/normalize/box_cox/auto_lambda + lag/difference augmentation + pad_by_time).

    Category 00-data-utilities; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a long frame.
        value_col: [series_codes, required] Value column(s) to lag.
        lags: [int_array, optional] Integer lags (negative=lead accepted; default 1). Default ``1``.
        new_names: [series_codes, optional] New column names or 'auto' (default 'auto'). Default
            ``'auto'``.

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
        "prep_augment_lags: not implemented."
    )


def prep_augment_differences(
    *,
    data: pd.DataFrame,
    value_col: Sequence[str],
    lags: Sequence[int] | None = None,
    differences: int | None = None,
    log: bool | None = None,
    new_names: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Node ``prep_augment_differences`` -- method card #104.

    Deterministic invertible preprocessing transforms
    (diff/standardize/normalize/box_cox/auto_lambda + lag/difference augmentation + pad_by_time).

    Category 00-data-utilities; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a long frame.
        value_col: [series_codes, required] Value column(s) to difference.
        lags: [int_array, optional] Positive lags (>=1; default 1). Default ``1``.
        differences: [integer, optional] Differencing order >=1 (default 1). Default ``1``.
        log: [boolean, optional] Log-differences (default False; requires column>0). Default
            ``False``.
        new_names: [series_codes, optional] Names or 'auto'. Default ``'auto'``.

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
        "prep_augment_differences: not implemented."
    )


def prep_pad_by_time(
    *,
    data: pd.DataFrame,
    date_col: str,
    by: str | None = None,
    pad_value: float | None = None,
    fill_na_direction: Literal["none", "down", "up", "downup", "updown"] | None = None,
    start_date: str | None = None,
    end_date: str | None = None,
) -> dict[str, Any]:
    """Node ``prep_pad_by_time`` -- method card #104.

    Deterministic invertible preprocessing transforms
    (diff/standardize/normalize/box_cox/auto_lambda + lag/difference augmentation + pad_by_time).

    Category 00-data-utilities; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a frame with a Date/timestamp column.
        date_col: [string, required] Time column name (Date/timestamp).
        by: [string, optional] Padding step ('auto'/'month'/'5 min'/...; default 'auto'). Default
            ``'auto'``.
        pad_value: [number, optional] Fill value (default NA).
        fill_na_direction: [enum, optional] LOCF/NOCB after the padding (default none).
        start_date: [string, optional] Extend the start of the padding.
        end_date: [string, optional] Extend the end of the padding.

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
        "prep_pad_by_time: not implemented."
    )
