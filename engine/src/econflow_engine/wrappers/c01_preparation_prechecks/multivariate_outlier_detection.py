# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``multivariate_outlier_detection`` -- METHOD-SELECTION card #246.

#246 MULTIVARIATE outlier detection: CLASSICAL Mahalanobis distances vs the ROBUST MCD
    (Deterministic MCD) at the SAME chi-square(p) cutoff + a MASKING / SWAMPING diagnostic

Category 01-preparation-prechecks; module ``multivariate_outlier_detection``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c01_preparation_prechecks import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "mv_covmcd",
    "mv_mahalanobis",
    "mv_outliers",
    "NODE_META",
    "wire_model",
]


def mv_mahalanobis(
    *,
    x: np.ndarray,
    quantile: float | None = None,
    center: Sequence[float] | None = None,
    cov: np.ndarray | None = None,
) -> dict[str, Any]:
    """Node ``mv_mahalanobis`` -- METHOD-SELECTION card #246.

    MULTIVARIATE outlier detection: CLASSICAL Mahalanobis distances vs the ROBUST MCD (Deterministic
    MCD) at the SAME chi-square(p) cutoff + a MASKING / SWAMPING diagnostic.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a NUMERIC observations×variables matrix (rows =
            observations/countries/periods, columns = variables). p >= 2 columns are required
            (MULTIVARIATE test), NO zero-variance column, NO collinearity, NOT NA/NaN/Inf (covMcd
            SILENTLY drops the incomplete rows). CROSS-SECTION/PANEL: on LEVELS of non-stationary
            time series the Mahalanobis distance is uninterpretable — give DIFFERENCES
            (Hamilton-Ma-Xi).
        quantile: [number, optional] Chi-square quantile of the threshold: cutoff = qchisq(quantile,
            df = p) (default 0.975). STRICTLY within (0,1). Larger quantile => stricter threshold =>
            fewer flags. Default ``0.975``.
        center: [num_array, optional] OPTIONAL center of length p (fit/apply externalization): pass
            the 'center' of a previous mv_covmcd node for OUT-OF-SAMPLE scoring of new observations.
            Omitting it the sample mean is used.
        cov: [matrix_handle, optional] OPTIONAL handle to a p×p covariance matrix (fit/apply
            externalization): typically the ROBUST 'cov' of a mv_covmcd node => robust distances on
            NEW data. It must be symmetric, positive definite and invertible. When BOTH 'center' AND
            'cov' are given, ONE observation suffices.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mv_mahalanobis: not implemented. The method card is in ./README.md."
    )


def mv_covmcd(
    *,
    x: np.ndarray,
    alpha: float | None = None,
    quantile: float | None = None,
    use_correction: bool | None = None,
    robust_cor: bool | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``mv_covmcd`` -- METHOD-SELECTION card #246.

    MULTIVARIATE outlier detection: CLASSICAL Mahalanobis distances vs the ROBUST MCD (Deterministic
    MCD) at the SAME chi-square(p) cutoff + a MASKING / SWAMPING diagnostic.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a NUMERIC observations×variables matrix (rows =
            observations/countries/periods, columns = variables). p >= 2 columns are required
            (MULTIVARIATE test), NO zero-variance column, NO collinearity, NOT NA/NaN/Inf (covMcd
            SILENTLY drops the incomplete rows). CROSS-SECTION/PANEL: on LEVELS of non-stationary
            time series the Mahalanobis distance is uninterpretable — give DIFFERENCES
            (Hamilton-Ma-Xi).
        alpha: [number, optional] Size of the "clean" subset of the MCD: h = h.alpha.n(alpha, n, p)
            ~ alpha*n (default 0.5 = maximum robustness). Permitted [0.5, 1) — covMcd does NOT error
            below 0.5 (only a warning; breakdown > 50%) and alpha = 1 DEGENERATES the MCD into the
            classical estimator. Values 0.75 give greater efficiency with less robustness. Default
            ``0.5``.
        quantile: [number, optional] Chi-square quantile of the threshold: cutoff = qchisq(quantile,
            df = p) (default 0.975). STRICTLY within (0,1). Larger quantile => stricter threshold =>
            fewer flags. Default ``0.975``.
        use_correction: [boolean, optional] Finite-sample correction factors (Pison et al. 2002·
            default True). False = only the consistency factor. Default ``True``.
        robust_cor: [boolean, optional] Whether to also return the ROBUST correlation matrix (covMcd
            cor=; default False). Default ``False``.
        seed: [integer, optional] Seed (default 1234). nsamp='deterministic' is PINNED, so the
            result is IDENTICAL regardless of seed; the seed is a safety net for n > nmini*kmini
            (=1500) where covMcd subsamples in the initial search. Default ``1234``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mv_covmcd: not implemented. The method card is in ./README.md."
    )


def mv_outliers(
    *,
    x: np.ndarray,
    alpha: float | None = None,
    quantile: float | None = None,
    use_correction: bool | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``mv_outliers`` -- METHOD-SELECTION card #246.

    MULTIVARIATE outlier detection: CLASSICAL Mahalanobis distances vs the ROBUST MCD (Deterministic
    MCD) at the SAME chi-square(p) cutoff + a MASKING / SWAMPING diagnostic.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a NUMERIC observations×variables matrix (rows =
            observations/countries/periods, columns = variables). p >= 2 columns are required
            (MULTIVARIATE test), NO zero-variance column, NO collinearity, NOT NA/NaN/Inf (covMcd
            SILENTLY drops the incomplete rows). CROSS-SECTION/PANEL: on LEVELS of non-stationary
            time series the Mahalanobis distance is uninterpretable — give DIFFERENCES
            (Hamilton-Ma-Xi).
        alpha: [number, optional] Size of the "clean" subset of the MCD: h = h.alpha.n(alpha, n, p)
            ~ alpha*n (default 0.5 = maximum robustness). Permitted [0.5, 1) — covMcd does NOT error
            below 0.5 (only a warning; breakdown > 50%) and alpha = 1 DEGENERATES the MCD into the
            classical estimator. Values 0.75 give greater efficiency with less robustness. Default
            ``0.5``.
        quantile: [number, optional] Chi-square quantile of the threshold: cutoff = qchisq(quantile,
            df = p) (default 0.975). STRICTLY within (0,1). Larger quantile => stricter threshold =>
            fewer flags. Default ``0.975``.
        use_correction: [boolean, optional] Finite-sample correction factors (Pison et al. 2002·
            default True). False = only the consistency factor. Default ``True``.
        seed: [integer, optional] Seed (default 1234). nsamp='deterministic' is PINNED, so the
            result is IDENTICAL regardless of seed; the seed is a safety net for n > nmini*kmini
            (=1500) where covMcd subsamples in the initial search. Default ``1234``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mv_outliers: not implemented. The method card is in ./README.md."
    )
