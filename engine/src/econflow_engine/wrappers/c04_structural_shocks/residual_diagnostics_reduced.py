# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``residual_diagnostics_reduced`` -- method card #153.

#153 Residual diagnostics for a reduced-form VAR: a multivariate LM autocorrelation test
    (+HC-robust/univariate) + a combined bootstrap ARCH test (CA/ET/MARCH) + a wild-bootstrap AC
    test

Category 04-structural-shocks; module ``residual_diagnostics_reduced``.

Reference implementation: 10.1007/s00362-016-0744-0.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import numpy as np
import pandas as pd

from econflow_engine.generated.args.c04_structural_shocks import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "vtt_arch",
    "vtt_fit",
    "vtt_portmanteau",
    "vtt_wildboot",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def vtt_fit(
    *,
    y: pd.DataFrame,
    p: int | None = None,
    const: bool | None = None,
    trend: bool | None = None,
    exogen: np.ndarray | None = None,
) -> dict[str, Any]:
    """Node ``vtt_fit`` -- method card #153.

    Residual diagnostics for a reduced-form VAR: a multivariate LM autocorrelation test
    (+HC-robust/univariate) + a combined bootstrap ARCH test (CA/ET/MARCH) + a wild-bootstrap AC
    test.

    Category 04-structural-shocks; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        y: [multiseries_handle, required] Handle to a multivariate series (series/panel/matrix, T x
            K) — the data of the reduced-form VAR.
        p: [integer, optional] VAR lag order (positive integer· default 1). Default ``1``.
        const: [boolean, optional] Constant term (default True). Default ``True``.
        trend: [boolean, optional] Linear trend (default False). Default ``False``.
        exogen: [exog_handle, optional] Optional exogenous regressors (matrix, nrow==the row count
            of y).

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
        "vtt_fit: not implemented."
    )


def vtt_portmanteau(
    *,
    fit: Any,
    h: int | None = None,
    HCtype: Any | None = None,
    univariate: bool | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``vtt_portmanteau`` -- method card #153.

    Residual diagnostics for a reduced-form VAR: a multivariate LM autocorrelation test
    (+HC-robust/univariate) + a combined bootstrap ARCH test (CA/ET/MARCH) + a wild-bootstrap AC
    test.

    Category 04-structural-shocks; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a fitted VAR: 'VARfit' (from vtt_fit) or 'varest'
            (from vr_fit, button #11).
        h: [integer, optional] Order h of the alternative VAR(h) for the errors (positive integer·
            default 4). Default ``4``.
        HCtype: [raw, optional] Character-vector subset of {LM,HC0,HC1,HC2,HC3}: LM=homoskedastic,
            HC*=heteroskedasticity-consistent (default all).
        univariate: [boolean, optional] Additional per-equation (univariate) test (default False·
            'only' is NOT supported). Default ``False``.
        alpha: [number, optional] Decision significance level ∈ (0,1) (default 0.05). Default
            ``0.05``.

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
        "vtt_portmanteau: not implemented."
    )


def vtt_arch(
    *,
    fit: Any,
    h: int | None = None,
    B: int | None = None,
    seed: int,
    ET: bool | None = None,
    MARCH: bool | None = None,
    dist: Literal["norm", "skT"] | None = None,
    skT_param: Sequence[float] | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``vtt_arch`` -- method card #153.

    Residual diagnostics for a reduced-form VAR: a multivariate LM autocorrelation test
    (+HC-robust/univariate) + a combined bootstrap ARCH test (CA/ET/MARCH) + a wild-bootstrap AC
    test.

    Category 04-structural-shocks; memory class ``heavy``.

    Args:
        fit: [raw_handle, required] Handle to a fitted VAR ('VARfit'/'varest').
        h: [integer, optional] Order h of the ARCH alternative (positive integer· default 2).
            Default ``2``.
        B: [integer, optional] Number of bootstrap simulations (positive integer· default 499).
            Default ``499``.
        seed: [integer, required] MANDATORY seed (seeded before the bootstrap· cache key· without it
            uncacheable).
        ET: [boolean, optional] Eklund-Terasvirta CCC-ARCH test (default True). The CA
            (Catani-Ahlgren) test ALWAYS runs. Default ``True``.
        MARCH: [boolean, optional] Multivariate LM ARCH test (Lutkepohl 2006, sect. 16.5· default
            True). Default ``True``.
        dist: [enum, optional] Bootstrap error distribution (default norm· skT=skew-t with
            skT.param).
        skT_param: [num_array, optional] Skew-t parameters [xi,Omega,alpha,nu] when dist='skT'
            (default [0,1,0,5]).
        alpha: [number, optional] Decision significance level ∈ (0,1) (default 0.05). Default
            ``0.05``.

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
        "vtt_arch: not implemented."
    )


def vtt_wildboot(
    *,
    fit: Any,
    h: int | None = None,
    HCtype: Any | None = None,
    WBtype: Literal["recursive", "fixed"] | None = None,
    B: int | None = None,
    WBdist: Literal["rademacher", "normal", "mammen"] | None = None,
    univariate: bool | None = None,
    seed: int,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``vtt_wildboot`` -- method card #153.

    Residual diagnostics for a reduced-form VAR: a multivariate LM autocorrelation test
    (+HC-robust/univariate) + a combined bootstrap ARCH test (CA/ET/MARCH) + a wild-bootstrap AC
    test.

    Category 04-structural-shocks; memory class ``heavy``.

    Args:
        fit: [raw_handle, required] Handle to a fitted VAR ('VARfit'/'varest').
        h: [integer, optional] Order h of the AC alternative (positive integer· default 4). Default
            ``4``.
        HCtype: [raw, optional] Character-vector subset of {LM,HC0,HC1,HC2,HC3} (default all).
        WBtype: [enum, optional] Wild-bootstrap scheme (Algorithm 1/2 Ahlgren-Catani· default
            recursive).
        B: [integer, optional] Number of bootstrap simulations (positive integer· default 199).
            Default ``199``.
        WBdist: [enum, optional] Distribution of the wild-bootstrap weights (default rademacher).
        univariate: [boolean, optional] Additional per-equation test (default False). Default
            ``False``.
        seed: [integer, required] MANDATORY seed (seeded before the bootstrap· cache key).
        alpha: [number, optional] Decision significance level ∈ (0,1) (default 0.05). Default
            ``0.05``.

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
        "vtt_wildboot: not implemented."
    )
