# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``pca_mixed_variables`` -- method card #256.

#256 PCA for MIXED I(0)/I(1) variables: an h-step-ahead OLS regression per series (a constant + p
    own lags) -> PCA on the RESIDUALS (Hamilton-Ma-Xi)

Category 03-multivariate-nowcasting; module ``pca_mixed_variables``.

Reference implementation: 10.3386/w32068.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import numpy as np

from econflow_engine.generated.args.c03_multivariate_nowcasting import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "pn_cyclical_components",
    "pn_pca_nonstationary",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def pn_cyclical_components(
    *,
    x: np.ndarray,
    h: int | None = None,
    p: int | None = None,
) -> dict[str, Any]:
    """Node ``pn_cyclical_components`` -- method card #256.

    PCA for MIXED I(0)/I(1) variables: an h-step-ahead OLS regression per series (a constant + p own
    lags) -> PCA on the RESIDUALS (Hamilton-Ma-Xi).

    Category 03-multivariate-nowcasting; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a NUMERIC matrix ROWS = TIME, COLUMNS = VARIABLES (>=
            2 series). You do NOT need to know which series are I(0) and which are I(1) — that IS
            the point of the method; do NOT difference and do NOT detrend first. Balanced sample:
            NOT NA/NaN/Inf. NO constant series and no DETERMINISTIC one (y_t = a + b·t) — its lags
            are collinear. Take logs upstream of whatever is described in growth rates
            (output/prices); rates enter as is.
        h: [integer, optional] Forecast horizon h of eq. (7) — POSITIVE INTEGER. Default 24 = TWO
            YEARS on MONTHLY data (the paper's recommendation; maximum agreement of 99% with NBER
            recessions at h=25, 98% at h=24). For QUARTERLY data use h=8. Every h >= 1 produces a
            stationary cyclical component; larger h => fewer outliers but more autocorrelation (risk
            of a spurious factor in SMALL samples: with < 50 years prefer h=12 or h=1). Default
            ``24``.
        p: [integer, optional] Number of own lags p of eq. (7) — POSITIVE INTEGER. Default 12 = ONE
            YEAR on MONTHLY data (4 for quarterly): the paper recommends p = observations per year
            so that lingering seasonal components are covered. p is ALSO the maximum integration
            order d_i <= p that is neutralized. T >= h + 2p + 1 IS REQUIRED. Default ``12``.

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
        "pn_cyclical_components: not implemented."
    )


def pn_pca_nonstationary(
    *,
    x: np.ndarray,
    h: int | None = None,
    p: int | None = None,
    scale_residuals: Literal["unit_variance", "none"] | None = None,
    r_max: int | None = None,
) -> dict[str, Any]:
    """Node ``pn_pca_nonstationary`` -- method card #256.

    PCA for MIXED I(0)/I(1) variables: an h-step-ahead OLS regression per series (a constant + p own
    lags) -> PCA on the RESIDUALS (Hamilton-Ma-Xi).

    Category 03-multivariate-nowcasting; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a NUMERIC matrix ROWS = TIME, COLUMNS = VARIABLES (>=
            2 series). You do NOT need to know which series are I(0) and which are I(1) — that IS
            the point of the method; do NOT difference and do NOT detrend first. Balanced sample:
            NOT NA/NaN/Inf. NO constant series and no DETERMINISTIC one (y_t = a + b·t) — its lags
            are collinear. Take logs upstream of whatever is described in growth rates
            (output/prices); rates enter as is.
        h: [integer, optional] Forecast horizon h of eq. (7) — POSITIVE INTEGER. Default 24 = TWO
            YEARS on MONTHLY data (the paper's recommendation; maximum agreement of 99% with NBER
            recessions at h=25, 98% at h=24). For QUARTERLY data use h=8. Every h >= 1 produces a
            stationary cyclical component; larger h => fewer outliers but more autocorrelation (risk
            of a spurious factor in SMALL samples: with < 50 years prefer h=12 or h=1). Default
            ``24``.
        p: [integer, optional] Number of own lags p of eq. (7) — POSITIVE INTEGER. Default 12 = ONE
            YEAR on MONTHLY data (4 for quarterly): the paper recommends p = observations per year
            so that lingering seasonal components are covered. p is ALSO the maximum integration
            order d_i <= p that is neutralized. T >= h + 2p + 1 IS REQUIRED. Default ``12``.
        scale_residuals: [enum, optional] Scaling OF THE RESIDUALS (NEVER of the raw series — this
            is the INVALID step on non-stationary data; the sample sd of an I(1) series DIVERGES
            with T, while that of the residuals CONVERGES). 'unit_variance' (DEFAULT) = each
            residual series is divided by its sd => PCA on the CORRELATION MATRIX; this IS the
            paper's procedure (§6.3 "Since ĉ_it is normalized to have unit variance" and eqs. 18-19
            defined over the correlation matrix). 'none' = the COVARIANCE matrix — only for series
            ALREADY of common scale; then var_explained does NOT coincide with r2_eigen (see
            pca_matrix). The fitted scale params are returned (residual_scale) => reproducible
            out-of-sample apply.
        r_max: [integer, optional] Maximum number of factors for the Bai-Ng IC_p2 criterion (eq. 19;
            the paper uses r0 = 10). Automatically capped at min(N-1, T_eff-1) and the EFFECTIVE
            value is returned as r_max_effective. IC_p2 is VALID HERE (on the residuals) while it is
            CORRUPTED on non-stationary levels. Default ``10``.

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
        "pn_pca_nonstationary: not implemented."
    )
