# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``penalized_poisson_pml`` -- method card #238.

#238 Penalized Poisson PML gravity with high-dimensional fixed effects (an HDFE PPML baseline; a
    single-lambda lasso/ridge/plugin; a lasso/ridge path + a BIC-selected lambda)

Category 28-trade-gravity; module ``penalized_poisson_pml``.

Reference implementation: 10.1596/1813-9450-9629.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c28_trade_gravity import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "pp_hdfe",
    "pp_ml_fit",
    "pp_penalized_hdfe",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def pp_hdfe(
    *,
    data: pd.DataFrame,
    dep: str,
    indep: Sequence[str],
    fixed: Any,
    cluster: Sequence[str] | None = None,
    tol: float | None = None,
    hdfetol: float | None = None,
) -> dict[str, Any]:
    """Node ``pp_hdfe`` -- method card #238.

    Penalized Poisson PML gravity with high-dimensional fixed effects (an HDFE PPML baseline; a
    single-lambda lasso/ridge/plugin; a lasso/ridge path + a BIC-selected lambda).

    Category 28-trade-gravity; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to ONE long gravity DataFrame: one row per (exporter,
            importer, [time]) with a flow column (dep >= 0), regressors (indep) and fixed-effect
            factor columns.
        dep: [string, required] Column name of the dependent flow/count (bilateral trade flow,
            non-negative)· PPML models E[y]=exp(xbeta).
        indep: [series_codes, required] Names of numeric regressor columns (>= 1): e.g. dummies of
            trade provisions / policies· ALL numeric, WITHOUT NA.
        fixed: [raw, required] High-dimensional fixed effects: either a character vector of simple
            FE (e.g. ["exp","imp"]) or array-of-arrays for interaction FE (e.g.
            [["exp","time"],["imp","time"],["exp","imp"]] = exporter-time, importer-time, pair FE).
        cluster: [series_codes, optional] Column names for cluster-robust SE / penalty loadings
            (optional)· REQUIRED when plugin=True.
        tol: [number, optional] Convergence tolerance of the IRLS (positive· default 1e-8). Default
            ``1e-08``.
        hdfetol: [number, optional] Convergence tolerance of the HDFE partialling-out (positive·
            default 1e-4). Default ``0.0001``.

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
        "pp_hdfe: not implemented."
    )


def pp_penalized_hdfe(
    *,
    data: pd.DataFrame,
    dep: str,
    indep: Sequence[str],
    fixed: Any,
    lambda_: float,
    penalty: Literal["lasso", "ridge"] | None = None,
    plugin: bool | None = None,
    cluster: Sequence[str] | None = None,
    hdfetol: float | None = None,
) -> dict[str, Any]:
    """Node ``pp_penalized_hdfe`` -- method card #238.

    Penalized Poisson PML gravity with high-dimensional fixed effects (an HDFE PPML baseline; a
    single-lambda lasso/ridge/plugin; a lasso/ridge path + a BIC-selected lambda).

    Category 28-trade-gravity; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to ONE long gravity DataFrame: one row per (exporter,
            importer, [time]) with a flow column (dep >= 0), regressors (indep) and fixed-effect
            factor columns.
        dep: [string, required] Column name of the dependent flow/count (bilateral trade flow,
            non-negative)· PPML models E[y]=exp(xbeta).
        indep: [series_codes, required] Names of numeric regressor columns (>= 1): e.g. dummies of
            trade provisions / policies· ALL numeric, WITHOUT NA.
        fixed: [raw, required] High-dimensional fixed effects: either a character vector of simple
            FE (e.g. ["exp","imp"]) or array-of-arrays for interaction FE (e.g.
            [["exp","time"],["imp","time"],["exp","imp"]] = exporter-time, importer-time, pair FE).
        lambda_ (wire name ``lambda``): [number, required] Non-negative penalization parameter
            (lambda=0 => unpenalized)· larger lambda => stronger shrinkage (lasso: more zeros).
        penalty: [enum, optional] Penalty type (default lasso): lasso=L1 (variable selection, zeroes
            coefficients)· ridge=L2 (shrinkage without zeroing).
        plugin: [boolean, optional] plugin lasso (Breinlich et al. 2021): coefficient-specific
            data-driven penalty loadings (default False)· REQUIRES cluster. Default ``False``.
        cluster: [series_codes, optional] Column names for cluster-robust SE / penalty loadings
            (optional)· REQUIRED when plugin=True.
        hdfetol: [number, optional] Convergence tolerance of the HDFE partialling-out (positive·
            default 1e-4). Default ``0.0001``.

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
        "pp_penalized_hdfe: not implemented."
    )


def pp_ml_fit(
    *,
    data: pd.DataFrame,
    dep: str,
    indep: Sequence[str],
    fixed: Any,
    lambdas: Sequence[float] | None = None,
    penalty: Literal["lasso", "ridge"] | None = None,
    plugin: bool | None = None,
    post: bool | None = None,
    cluster: Sequence[str] | None = None,
    seed: int | None = None,
    hdfetol: float | None = None,
) -> dict[str, Any]:
    """Node ``pp_ml_fit`` -- method card #238.

    Penalized Poisson PML gravity with high-dimensional fixed effects (an HDFE PPML baseline; a
    single-lambda lasso/ridge/plugin; a lasso/ridge path + a BIC-selected lambda).

    Category 28-trade-gravity; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to ONE long gravity DataFrame: one row per (exporter,
            importer, [time]) with a flow column (dep >= 0), regressors (indep) and fixed-effect
            factor columns.
        dep: [string, required] Column name of the dependent flow/count (bilateral trade flow,
            non-negative)· PPML models E[y]=exp(xbeta).
        indep: [series_codes, required] Names of numeric regressor columns (>= 1): e.g. dummies of
            trade provisions / policies· ALL numeric, WITHOUT NA.
        fixed: [raw, required] High-dimensional fixed effects: either a character vector of simple
            FE (e.g. ["exp","imp"]) or array-of-arrays for interaction FE (e.g.
            [["exp","time"],["imp","time"],["exp","imp"]] = exporter-time, importer-time, pair FE).
        lambdas: [num_array, optional] Vector of non-negative lambda of the penalization path
            (REQUIRED when plugin=False)· the lambda that MINIMIZES the BIC is selected.
        penalty: [enum, optional] Penalty type (default lasso): lasso=L1 selection· ridge=L2.
        plugin: [boolean, optional] plugin lasso (default False): ignores lambdas & uses data-driven
            penalty loadings· REQUIRES cluster. Default ``False``.
        post: [boolean, optional] post-lasso: re-estimation (unpenalized PPML) on the selected
            regressors for de-biased coefficients (default False). Default ``False``.
        cluster: [series_codes, optional] Column names for cluster-robust SE / penalty loadings
            (optional)· REQUIRED when plugin=True.
        seed: [integer, optional] Seed before the fit (determinism· default 1). Default ``1``.
        hdfetol: [number, optional] Convergence tolerance of the HDFE partialling-out (positive·
            default 1e-4). Default ``0.0001``.

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
        "pp_ml_fit: not implemented."
    )
