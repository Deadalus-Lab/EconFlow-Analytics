# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``distributed_lag_ardl`` -- METHOD-SELECTION card #137.

#137 Distributed-lag & ARDL regression (finite DL / Koyck geometric / autoregressive DL / Almon
    polynomial DL)

Category 02-univariate-forecasting; module ``distributed_lag_ardl``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c02_univariate_forecasting import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "dlm_ardl",
    "dlm_finite",
    "dlm_koyck",
    "dlm_poly",
    "NODE_META",
    "wire_model",
]


def dlm_finite(
    *,
    x: pd.Series | None = None,
    y: pd.Series | None = None,
    data: pd.DataFrame | None = None,
    y_col: str | None = None,
    x_cols: Sequence[str] | None = None,
    q: int,
    remove: Any | None = None,
) -> dict[str, Any]:
    """Node ``dlm_finite`` -- METHOD-SELECTION card #137.

    Distributed-lag & ARDL regression (finite DL / Koyck geometric / autoregressive DL / Almon
    polynomial DL).

    Category 02-univariate-forecasting; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        x: [series_handle, optional] Handle to predictor series X (vector mode; numeric >=3, without
            NA/Inf).
        y: [series_handle, optional] Handle to dependent series Y (vector mode; same length as x).
        data: [df_handle, optional] Handle to a DataFrame (closed formula mode; requires
            y_col+x_cols).
        y_col: [string, optional] Response column name (formula mode).
        x_cols: [series_codes, optional] Predictor column names >=1 (formula mode; closed, without a
            free formula string).
        q: [integer, required] Finite lag length (positive integer >=1, < nobs).
        remove: [raw, optional] list of lags to remove per predictor (optional).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "dlm_finite: not implemented. The method card is in ./README.md."
    )


def dlm_koyck(
    *,
    x: pd.Series,
    y: pd.Series,
    intercept: bool | None = None,
) -> dict[str, Any]:
    """Node ``dlm_koyck`` -- METHOD-SELECTION card #137.

    Distributed-lag & ARDL regression (finite DL / Koyck geometric / autoregressive DL / Almon
    polynomial DL).

    Category 02-univariate-forecasting; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        x: [series_handle, required] Handle to predictor series X (numeric >=3).
        y: [series_handle, required] Handle to dependent series Y (same length as x).
        intercept: [boolean, optional] Inclusion of intercept in the Koyck-transformed model
            (default True).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "dlm_koyck: not implemented. The method card is in ./README.md."
    )


def dlm_ardl(
    *,
    x: pd.Series | None = None,
    y: pd.Series | None = None,
    data: pd.DataFrame | None = None,
    y_col: str | None = None,
    x_cols: Sequence[str] | None = None,
    p: int | None = None,
    q: int | None = None,
    remove: Any | None = None,
) -> dict[str, Any]:
    """Node ``dlm_ardl`` -- METHOD-SELECTION card #137.

    Distributed-lag & ARDL regression (finite DL / Koyck geometric / autoregressive DL / Almon
    polynomial DL).

    Category 02-univariate-forecasting; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        x: [series_handle, optional] Handle to predictor series X (vector mode).
        y: [series_handle, optional] Handle to dependent series Y (vector mode).
        data: [df_handle, optional] Handle to a DataFrame (closed formula mode; requires
            y_col+x_cols).
        y_col: [string, optional] Response column name (formula mode).
        x_cols: [series_codes, optional] Predictor column names >=1 (formula mode).
        p: [integer, optional] Lag length of predictor X (positive integer >=1, < nobs). Default
            ``1``.
        q: [integer, optional] AR order of dependent Y (positive integer >=1, < nobs). Default
            ``1``.
        remove: [raw, optional] list(p=, q=) of lags to remove (optional).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "dlm_ardl: not implemented. The method card is in ./README.md."
    )


def dlm_poly(
    *,
    x: pd.Series,
    y: pd.Series,
    q: int,
    k: int,
    show_beta: bool | None = None,
) -> dict[str, Any]:
    """Node ``dlm_poly`` -- METHOD-SELECTION card #137.

    Distributed-lag & ARDL regression (finite DL / Koyck geometric / autoregressive DL / Almon
    polynomial DL).

    Category 02-univariate-forecasting; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        x: [series_handle, required] Handle to predictor series X (numeric >=3).
        y: [series_handle, required] Handle to dependent series Y (same length as x).
        q: [integer, required] Finite lag length (positive integer >=1, < nobs).
        k: [integer, required] Almon polynomial order (positive integer >=1, k <= q).
        show_beta: [boolean, optional] Return of original beta lag weights + t-tests (default True).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "dlm_poly: not implemented. The method card is in ./README.md."
    )
