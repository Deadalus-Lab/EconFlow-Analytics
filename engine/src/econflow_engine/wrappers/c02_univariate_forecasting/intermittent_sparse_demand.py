# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``intermittent_sparse_demand`` -- method card #135.

#135 Intermittent / sparse-demand forecasting (Croston + SBA/SBJ variants, TSB, iMAPA
    auto-selection, Croston decomposition)

Category 02-univariate-forecasting; module ``intermittent_sparse_demand``.

Reference implementation: statsforecast.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c02_univariate_forecasting import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "tsi_croston",
    "tsi_decomp",
    "tsi_imapa",
    "tsi_tsb",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def tsi_croston(
    *,
    data: pd.Series,
    h: int | None = None,
    type: Literal["croston", "sba", "sbj"] | None = None,
    init: Literal["mean", "naive"] | None = None,
    cost: Literal["mar", "msr", "mae", "mse"] | None = None,
    nop: int | None = None,
    w: Any | None = None,
    init_opt: bool | None = None,
    na_rm: bool | None = None,
) -> dict[str, Any]:
    """Node ``tsi_croston`` -- method card #135.

    Intermittent / sparse-demand forecasting (Croston + SBA/SBJ variants, TSB, iMAPA auto-selection,
    Croston decomposition).

    Category 02-univariate-forecasting; memory class ``light``.

    Args:
        data: [series_handle, required] Handle to a univariate intermittent-demand series
            (non-negative, with zeros).
        h: [integer, optional] Forecast horizon (positive integer; default 10).
        type: [enum, optional] Croston variant (default croston; sba/sbj = bias-corrected).
        init: [enum, optional] Initial demand/interval values (default mean).
        cost: [enum, optional] Optimization cost function (default mar).
        nop: [integer, optional] Number of parameters: 1 (shared) or 2 (default, separate
            demand/interval).
        w: [raw, optional] Smoothing parameters (None -> optimise; 1 or 2 values).
        init_opt: [boolean, optional] Optimization of initial values (default True).
        na_rm: [boolean, optional] Removal of NA before the fit (default False).

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
        "tsi_croston: not implemented."
    )


def tsi_tsb(
    *,
    data: pd.Series,
    h: int | None = None,
    init: Literal["mean", "naive"] | None = None,
    cost: Literal["mar", "msr", "mae", "mse"] | None = None,
    w: Any | None = None,
    init_opt: bool | None = None,
    na_rm: bool | None = None,
) -> dict[str, Any]:
    """Node ``tsi_tsb`` -- method card #135.

    Intermittent / sparse-demand forecasting (Croston + SBA/SBJ variants, TSB, iMAPA auto-selection,
    Croston decomposition).

    Category 02-univariate-forecasting; memory class ``light``.

    Args:
        data: [series_handle, required] Handle to a univariate intermittent-demand series.
        h: [integer, optional] Forecast horizon (positive integer; default 10).
        init: [enum, optional] Initial values (default mean).
        cost: [enum, optional] Cost function (default mar).
        w: [raw, optional] Smoothing (demand, demand-probability)· None -> optimise.
        init_opt: [boolean, optional] Optimization of initial values (default True).
        na_rm: [boolean, optional] Removal of NA (default False).

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
        "tsi_tsb: not implemented."
    )


def tsi_imapa(
    *,
    data: pd.Series,
    h: int | None = None,
    comb: Literal["mean", "median"] | None = None,
    minimumAL: int | None = None,
    maximumAL: int | None = None,
    w: Any | None = None,
    init_opt: bool | None = None,
    na_rm: bool | None = None,
) -> dict[str, Any]:
    """Node ``tsi_imapa`` -- method card #135.

    Intermittent / sparse-demand forecasting (Croston + SBA/SBJ variants, TSB, iMAPA auto-selection,
    Croston decomposition).

    Category 02-univariate-forecasting; memory class ``light``.

    Args:
        data: [series_handle, required] Handle to a univariate intermittent-demand series.
        h: [integer, optional] Forecast horizon (positive integer; default 10).
        comb: [enum, optional] Combination operator over the aggregation levels (default mean).
        minimumAL: [integer, optional] Lowest aggregation level (default 1).
        maximumAL: [integer, optional] Highest aggregation level (None -> maximum interval).
        w: [raw, optional] Smoothing parameters (None -> optimise).
        init_opt: [boolean, optional] Optimization of Croston/SBA initial values (default True).
        na_rm: [boolean, optional] Removal of NA (default False).

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
        "tsi_imapa: not implemented."
    )


def tsi_decomp(
    *,
    data: pd.Series,
    init: Literal["naive", "mean"] | None = None,
) -> dict[str, Any]:
    """Node ``tsi_decomp`` -- method card #135.

    Intermittent / sparse-demand forecasting (Croston + SBA/SBJ variants, TSB, iMAPA auto-selection,
    Croston decomposition).

    Category 02-univariate-forecasting; memory class ``light``.

    Args:
        data: [series_handle, required] Handle to a univariate intermittent-demand series.
        init: [enum, optional] Initial interval value (default naive — CAUTION: reverse order from
            crost/tsb).

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
        "tsi_decomp: not implemented."
    )
