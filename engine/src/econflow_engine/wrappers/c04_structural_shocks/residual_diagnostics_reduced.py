# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``residual_diagnostics_reduced`` -- METHOD-SELECTION card #153.

#153 Residual diagnostics for a reduced-form VAR: a multivariate LM autocorrelation test
    (+HC-robust/univariate) + a combined bootstrap ARCH test (CA/ET/MARCH) + a wild-bootstrap AC
    test

Category 04-structural-shocks; module ``residual_diagnostics_reduced``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c04_structural_shocks import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np
    import pandas as pd

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


def vtt_fit(
    *,
    y: pd.DataFrame,
    p: int | None = None,
    const: bool | None = None,
    trend: bool | None = None,
    exogen: np.ndarray | None = None,
) -> dict[str, Any]:
    """Node ``vtt_fit`` -- METHOD-SELECTION card #153.

    Residual diagnostics for a reduced-form VAR: a multivariate LM autocorrelation test
    (+HC-robust/univariate) + a combined bootstrap ARCH test (CA/ET/MARCH) + a wild-bootstrap AC
    test.

    Category 04-structural-shocks; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        y: [multiseries_handle, required] Handle to a multivariate series (ts/mts/matrix, T x K) —
            the data of the reduced-form VAR.
        p: [integer, optional] VAR lag order (positive integer· default 1). Default ``1``.
        const: [boolean, optional] Constant term (default True). Default ``True``.
        trend: [boolean, optional] Linear trend (default False). Default ``False``.
        exogen: [exog_handle, optional] Optional exogenous regressors (matrix, nrow==the row count
            of y).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "vtt_fit: not implemented. The method card is in ./README.md."
    )


def vtt_portmanteau(
    *,
    fit: Any,
    h: int | None = None,
    HCtype: Any | None = None,
    univariate: bool | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``vtt_portmanteau`` -- METHOD-SELECTION card #153.

    Residual diagnostics for a reduced-form VAR: a multivariate LM autocorrelation test
    (+HC-robust/univariate) + a combined bootstrap ARCH test (CA/ET/MARCH) + a wild-bootstrap AC
    test.

    Category 04-structural-shocks; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a fitted VAR: 'VARfit' (from vtt_fit) or 'varest'
            (from vr_var, button #11).
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
    """
    raise NotImplementedError(
        "vtt_portmanteau: not implemented. The method card is in ./README.md."
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
    """Node ``vtt_arch`` -- METHOD-SELECTION card #153.

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
        seed: [integer, required] MANDATORY seed (set.seed before the bootstrap· cache key· without
            it uncacheable).
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
    """
    raise NotImplementedError(
        "vtt_arch: not implemented. The method card is in ./README.md."
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
    """Node ``vtt_wildboot`` -- METHOD-SELECTION card #153.

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
        seed: [integer, required] MANDATORY seed (set.seed before the bootstrap· cache key).
        alpha: [number, optional] Decision significance level ∈ (0,1) (default 0.05). Default
            ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "vtt_wildboot: not implemented. The method card is in ./README.md."
    )
