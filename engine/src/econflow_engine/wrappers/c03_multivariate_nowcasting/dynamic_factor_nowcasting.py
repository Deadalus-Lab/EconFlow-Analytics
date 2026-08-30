# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``dynamic_factor_nowcasting`` -- method card #15.

#15 Dynamic Factor Model / nowcasting

Category 03-multivariate-nowcasting; module ``dynamic_factor_nowcasting``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c03_multivariate_nowcasting import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "df_fit",
    "df_predict",
    "df_select_factors",
    "df_summary",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def df_select_factors(
    *,
    X: pd.DataFrame,
    max_r: int | None = None,
) -> dict[str, Any]:
    """Node ``df_select_factors`` -- method card #15.

    Dynamic Factor Model / nowcasting.

    Category 03-multivariate-nowcasting; memory class ``light``.

    Args:
        X: [multiseries_handle, required] Handle to panel data (T x n, >=2 columns, no NA).
        max_r: [integer, optional] Maximum number of factors to evaluate (default min(20, n-1)).

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
        "df_select_factors: not implemented."
    )


def df_fit(
    *,
    X: pd.DataFrame,
    r: int | None = None,
    p: int | None = None,
    idio_ar1: bool | None = None,
    rQ: Literal["none", "diagonal", "identity"] | None = None,
    rR: Literal["diagonal", "none"] | None = None,
) -> dict[str, Any]:
    """Node ``df_fit`` -- method card #15.

    Dynamic Factor Model / nowcasting.

    Category 03-multivariate-nowcasting; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        X: [multiseries_handle, required] Handle to panel data (T x n, >=2 columns, T>=10).
        r: [integer, optional] Number of factors· None -> automatic IC2 selection (requires no NA).
        p: [integer, optional] VAR lag order of the factors (default 1). Default ``1``.
        idio_ar1: [boolean, optional] AR(1) idiosyncratic components (default False). Default
            ``False``.
        rQ: [enum, optional] Restriction on the state covariance Q (default none).
        rR: [enum, optional] Restriction on the observation covariance the reference (default
            diagonal).

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
        "df_fit: not implemented."
    )


def df_predict(
    *,
    model: Any,
    h: int | None = None,
    standardized: bool | None = None,
) -> dict[str, Any]:
    """Node ``df_predict`` -- method card #15.

    Dynamic Factor Model / nowcasting.

    Category 03-multivariate-nowcasting; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a dfm model (from df_fit).
        h: [integer, optional] Forecast horizon for factors + variables (default 10). Default
            ``10``.
        standardized: [boolean, optional] Output in standardised units (default False = original
            units). Default ``False``.

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
        "df_predict: not implemented."
    )


def df_summary(
    *,
    model: Any,
) -> dict[str, Any]:
    """Node ``df_summary`` -- method card #15.

    Dynamic Factor Model / nowcasting.

    Category 03-multivariate-nowcasting; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a dfm model (loadings/R2/explained variance).

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
        "df_summary: not implemented."
    )
