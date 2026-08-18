# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``desparsified_debiased_lasso`` -- METHOD-SELECTION card #152.

#152 Desparsified/debiased LASSO inference (high-dimensional time series) + high-dimensional local
    projections (HDLP) with valid CIs — Adamek-Smeekes-Wilms

Category 04-structural-shocks; module ``desparsified_debiased_lasso``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c04_structural_shocks import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "dsl_desla",
    "dsl_hdlp",
    "NODE_META",
    "wire_model",
]


def dsl_desla(
    *,
    X: np.ndarray,
    y: Sequence[float],
    H: Sequence[int],
    seed: int,
    alphas: Sequence[float] | None = None,
    penalize_H: bool | None = None,
    restriction: np.ndarray | None = None,
    q: Sequence[float] | None = None,
    demean: bool | None = None,
    scale: bool | None = None,
) -> dict[str, Any]:
    """Node ``dsl_desla`` -- METHOD-SELECTION card #152.

    Desparsified/debiased LASSO inference (high-dimensional time series) + high-dimensional local
    projections (HDLP) with valid CIs — Adamek-Smeekes-Wilms.

    Category 04-structural-shocks; memory class ``light``.

    Args:
        X: [matrix_handle, required] Handle to a numeric matrix of regressors T x N (no NA/Inf· N>=T
            allowed — high-dim).
        y: [num_array, required] Dependent variable, numeric vector of length T (aligned with X).
        H: [int_array, required] Integer column indices of X in [1,N] that are tested (target
            coefficients).
        seed: [integer, required] MANDATORY seed (integer) — the lasso lambda selection uses random
            CV folds· set.seed beforehand.
        alphas: [num_array, optional] Significance levels ∈ (0,1) for the CIs (default 0.05).
        penalize_H: [boolean, optional] Penalise the H variables in the initial lasso (default
            True). Default ``True``.
        restriction: [matrix_handle, optional] Matrix for testing H0: the reference*beta = q
            (default: identity -> joint significance of all H).
        q: [num_array, optional] Right-hand-side vector for H0: the reference*beta = q (default:
            zeros). Activates row_tests.
        demean: [boolean, optional] Demean X/y before estimation (recommended· default True).
            Default ``True``.
        scale: [boolean, optional] Scale X/y by the column-wise SD (penalty scale-sensitive· default
            True). Default ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "dsl_desla: not implemented. The method card is in ./README.md."
    )


def dsl_hdlp(
    *,
    x: Sequence[float],
    y: Sequence[float],
    seed: int,
    r: np.ndarray | None = None,
    q: np.ndarray | None = None,
    state_variables: np.ndarray | None = None,
    y_predetermined: bool | None = None,
    cumulate_y: bool | None = None,
    hmax: int | None = None,
    lags: int | None = None,
    alphas: Sequence[float] | None = None,
    penalize_x: bool | None = None,
    OLS: bool | None = None,
) -> dict[str, Any]:
    """Node ``dsl_hdlp`` -- METHOD-SELECTION card #152.

    Desparsified/debiased LASSO inference (high-dimensional time series) + high-dimensional local
    projections (HDLP) with valid CIs — Adamek-Smeekes-Wilms.

    Category 04-structural-shocks; memory class ``light``.

    Args:
        x: [num_array, required] Shock variable, numeric vector of length T (Plagborg-Moller & Wolf
            notation).
        y: [num_array, required] Response variable, numeric vector of length T (aligned with x).
        seed: [integer, required] MANDATORY seed (integer) — lasso CV· set.seed beforehand.
        r: [matrix_handle, optional] 'Slow' variables (do not react within the same period), T rows.
        q: [matrix_handle, optional] 'Fast' variables/controls (react within the same period), T
            rows — the high-dim space.
        state_variables: [matrix_handle, optional] State variables (categorical or binary
            indicators), T rows -> state-dependent IRF.
        y_predetermined: [boolean, optional] True if y is predetermined with respect to x (IRF at
            horizon 0 = 0· default False). Default ``False``.
        cumulate_y: [boolean, optional] True for a cumulative IRF (uses cumsum of y· default False).
            Default ``False``.
        hmax: [integer, optional] Maximum IRF horizon· positive integer with hmax+lags < T (default
            10). Default ``10``.
        lags: [integer, optional] Number of lags in the local projection· positive integer with
            hmax+lags < T (default 4). Default ``4``.
        alphas: [num_array, optional] Significance levels ∈ (0,1) for the CI bands (default 0.05).
        penalize_x: [boolean, optional] Penalise the parameter of interest (default False). Default
            ``False``.
        OLS: [boolean, optional] Estimate with OLS instead of debiased lasso· ONLY for
            low-dimensional regressions (default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "dsl_hdlp: not implemented. The method card is in ./README.md."
    )
