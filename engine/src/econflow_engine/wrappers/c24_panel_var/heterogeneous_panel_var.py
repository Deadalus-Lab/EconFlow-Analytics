# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``heterogeneous_panel_var`` -- method card #230.

#230 Heterogeneous-panel VAR/SVAR: (P)MG estimation, panel cointegration rank tests, structural
    identification (+MG-IRF/MG-FEVD), bootstrap IRF confidence bands

Category 24-panel-var; module ``heterogeneous_panel_var``.

Reference implementation: 10.1016/0304-4076(94)01644-F.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c24_panel_var import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "pv_bootstrap",
    "pv_cointegration",
    "pv_estimate",
    "pv_identify",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def pv_estimate(
    *,
    df: pd.DataFrame,
    variables: Sequence[str],
    lags: int,
    id_col: str | None = None,
    model: Literal["VAR", "VEC"] | None = None,
    type: str | None = None,
    dim_r: int | None = None,
    n_factors: int | None = None,
    n_iterations: int | None = None,
) -> dict[str, Any]:
    """Node ``pv_estimate`` -- method card #230.

    Heterogeneous-panel VAR/SVAR: (P)MG estimation, panel cointegration rank tests, structural
    identification (+MG-IRF/MG-FEVD), bootstrap IRF confidence bands.

    Category 24-panel-var; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        df: [df_handle, required] Handle to a long panel DataFrame: identity column `id_col` + K
            numeric variable columns (same order k=1..K in each individual); >= 2 individuals,
            without NA.
        variables: [series_codes, required] Names of the K (>=2) endogenous columns in system order.
        lags: [integer, required] Common lag order p (positive integer) of the VAR in levels.
        id_col: [string, optional] Individual identity column name (default 'id'). Default ``'id'``.
        model: [enum, optional] VAR = mean-group VAR in levels (default); VEC = (pooled) mean-group
            rank-restricted VECM.
        type: [string, optional] Deterministic term. VAR: const/trend/both/none (default const)·
            VEC: Case1..Case5 (default Case4).
        dim_r: [integer, optional] model='VEC': common cointegration rank r (1..K-1); required for
            VEC.
        n_factors: [integer, optional] Number of common factors for SUR (default inactive).
        n_iterations: [integer, optional] Maximum iterations of SUR/pooled cointegrating vectors
            (default inactive).

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
        "pv_estimate: not implemented."
    )


def pv_cointegration(
    *,
    df: pd.DataFrame,
    variables: Sequence[str],
    lags: int,
    test: Literal["JO", "SL", "BR", "CAIN"] | None = None,
    id_col: str | None = None,
    det_case: Literal["Case1", "Case2", "Case3", "Case4"] | None = None,
    n_factors: int | None = None,
) -> dict[str, Any]:
    """Node ``pv_cointegration`` -- method card #230.

    Heterogeneous-panel VAR/SVAR: (P)MG estimation, panel cointegration rank tests, structural
    identification (+MG-IRF/MG-FEVD), bootstrap IRF confidence bands.

    Category 24-panel-var; memory class ``light``.

    Args:
        df: [df_handle, required] Handle to a long panel DataFrame {id_col + K variables}, as in
            pv_estimate.
        variables: [series_codes, required] Names of the K (>=2) endogenous columns in system order.
        lags: [integer, required] Common lag order p (positive integer) of the VAR in levels.
        test: [enum, optional] Procedure (default JO): JO=Johansen trace (panel); BR=Breitung
            two-step pooled· SL=Saikkonen-Luetkepohl· CAIN=Arsova-Oersal.
        id_col: [string, optional] Individual identity column name (default 'id'). Default ``'id'``.
        det_case: [enum, optional] Deterministic term for JO/BR (default Case1); SL/CAIN ignore it
            and use 'SL_trend'.
        n_factors: [integer, optional] PANIC common factors (Arsova-Oersal) for JO/SL (default
            inactive).

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
        "pv_cointegration: not implemented."
    )


def pv_identify(
    *,
    fit: Any,
    method: Literal["chol", "cvm", "dc", "iv", "grt"] | None = None,
    n_ahead: int | None = None,
    fevd_ahead: int | None = None,
    order_k: Any | None = None,
    combine: str | None = None,
    iv: pd.DataFrame | None = None,
    S2: Literal["MR", "JL", "NQ"] | None = None,
    cov_u: Literal["OMEGA", "SIGMA"] | None = None,
    LR: Any | None = None,
    SR: Any | None = None,
    n_factors: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``pv_identify`` -- method card #230.

    Heterogeneous-panel VAR/SVAR: (P)MG estimation, panel cointegration rank tests, structural
    identification (+MG-IRF/MG-FEVD), bootstrap IRF confidence bands.

    Category 24-panel-var; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        fit: [raw_handle, required] Handle to an UNIDENTIFIED panel VAR/VEC (pv_estimate.fit).
        method: [enum, optional] Identification (default chol): chol=recursive/Cholesky;
            cvm=Cramer-von Mises ICA· dc=distance-covariance ICA· iv=proxy/IV; grt=SVEC
            long/short-run (REQUIRES a VEC fit).
        n_ahead: [integer, optional] IRF horizon (positive integer; default 20). Default ``20``.
        fevd_ahead: [integer, optional] FEVD horizon (positive integer; default 10). Default ``10``.
        order_k: [raw, optional] method='chol': causal ordering (variable names or integer
            positions).
        combine: [string, optional] cvm/dc: group/pool/indiv (default indiv)· iv: pool/indiv
            (default pool); combination of individuals.
        iv: [df_handle, optional] method='iv': handle to a proxy DataFrame (L columns, T-lags rows).
        S2: [enum, optional] method='iv' with multiple proxies: MR/JL/NQ (default MR; pool=>NQ).
        cov_u: [enum, optional] method='iv': residual covariance OMEGA (÷T) or SIGMA (÷T-n) (default
            OMEGA).
        LR: [raw, optional] method='grt': K×K long-run restriction matrix (NA=free, 0=zero).
        SR: [raw, optional] method='grt': K×K short-run restriction matrix (NA=free).
        n_factors: [integer, optional] cvm/dc combine='group': number of common structural shocks
            (default inactive).
        seed: [integer, optional] Seed for cvm/dc (DEoptim/steadyICA; determinism; default 1).
            Default ``1``.

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
        "pv_identify: not implemented."
    )


def pv_bootstrap(
    *,
    fit: Any,
    method: Literal["pmb", "mg", "mb"] | None = None,
    n_ahead: int | None = None,
    n_boot: int | None = None,
    b_length: int | None = None,
    b_dim: Sequence[int] | None = None,
    individual: str | None = None,
    level: float | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``pv_bootstrap`` -- method card #230.

    Heterogeneous-panel VAR/SVAR: (P)MG estimation, panel cointegration rank tests, structural
    identification (+MG-IRF/MG-FEVD), bootstrap IRF confidence bands.

    Category 24-panel-var; memory class ``heavy``.

    Args:
        fit: [raw_handle, required] Handle to an IDENTIFIED panel SVAR (pv_identify.fit).
        method: [enum, optional] Bands (default pmb): pmb=panel moving-block bootstrap·
            mg=mean-group inference (spread of N individuals); mb=individual moving-block bootstrap
            of one individual.
        n_ahead: [integer, optional] IRF horizon (positive integer; default 20). Default ``20``.
        n_boot: [integer, optional] Bootstrap iterations for pmb/mb (positive integer; default 100).
            Default ``100``.
        b_length: [integer, optional] method='mb': residual block length (positive integer; default
            1; ~T/10). Default ``1``.
        b_dim: [int_array, optional] method='pmb': block dimensions (temporal, cross-sectional);
            default [1,1] i.i.d. Default ``[1, 1]``.
        individual: [string, optional] method='mb': individual to bootstrap (name or position 1..N).
        level: [number, optional] Confidence level of the bands ∈ (0,1) (default 0.90). Default
            ``0.9``.
        seed: [integer, optional] Seed for pmb/mb (determinism; default 1). Default ``1``.

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
        "pv_bootstrap: not implemented."
    )
