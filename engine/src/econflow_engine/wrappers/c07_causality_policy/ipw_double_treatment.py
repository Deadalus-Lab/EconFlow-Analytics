# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``ipw_double_treatment`` -- METHOD-SELECTION card #171.

#171 IPW / double-ML treatment effects (ATE/ATET, IV-LATE/LATT, causal mediation)

Category 07-causality-policy; module ``ipw_double_treatment``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c07_causality_policy import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "cw_lateweight",
    "cw_medDML",
    "cw_treatDML",
    "cw_treatweight",
    "NODE_META",
    "wire_model",
]


def cw_treatDML(
    *,
    y: Any,
    d: Any,
    x: np.ndarray,
    dtreat: float | None = None,
    dcontrol: float | None = None,
    trim: float | None = None,
    MLmethod: (
        Literal[
            "lasso",
            "randomforest",
            "xgboost",
            "svm",
            "ensemble",
            "parametric",
        ]
        | None
    ) = None,
    k: int | None = None,
    normalized: bool | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``cw_treatDML`` -- METHOD-SELECTION card #171.

    IPW / double-ML treatment effects (ATE/ATET, IV-LATE/LATT, causal mediation).

    Category 07-causality-policy; memory class ``light``.

    Args:
        y: [raw_handle, required] Handle to an outcome vector (numeric, no NA/Inf).
        d: [raw_handle, required] Handle to a discrete treatment vector (binary or multiple; same
            length as y).
        x: [matrix_handle, required] Handle to a covariate/confounder matrix (n x p, numeric, no
            NA).
        dtreat: [number, optional] Value of d in the treated group (default 1). Default ``1``.
        dcontrol: [number, optional] Value of d in the control group (default 0; != dtreat, among
            the values of d). Default ``0``.
        trim: [number, optional] Trimming of propensity scores outside [trim, 1-trim] (default 0.01;
            [0,0.5)). Default ``0.01``.
        MLmethod: [enum, optional] ML engine for the nuisance parameters (default lasso).
        k: [integer, optional] Folds in the k-fold cross-fitting (default 3; >=2). Default ``3``.
        normalized: [boolean, optional] Normalize the IPW weights so they sum to 1 per group
            (default True). Default ``True``.
        seed: [integer, optional] Seed for the random cross-fitting partition (default 2025).
            Default ``2025``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cw_treatDML: not implemented. The method card is in ./README.md."
    )


def cw_treatweight(
    *,
    y: Any,
    d: Any,
    x: np.ndarray,
    ATET: bool | None = None,
    trim: float | None = None,
    logit: bool | None = None,
    boot: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``cw_treatweight`` -- METHOD-SELECTION card #171.

    IPW / double-ML treatment effects (ATE/ATET, IV-LATE/LATT, causal mediation).

    Category 07-causality-policy; memory class ``heavy``.

    Args:
        y: [raw_handle, required] Handle to an outcome vector (numeric).
        d: [raw_handle, required] Handle to a BINARY 0/1 treatment vector (same length as y).
        x: [matrix_handle, required] Handle to a confounder matrix (n x p, no NA).
        ATET: [boolean, optional] True -> ATET (effect on treated); False -> ATE (default). Default
            ``False``.
        trim: [number, optional] Trimming of extreme propensity scores (default 0.05; [0,0.5)).
            Default ``0.05``.
        logit: [boolean, optional] True=logit, False=probit for the propensity score (default
            False). Default ``False``.
        boot: [integer, optional] Bootstrap replications for the SE (default 1999; >=2). Default
            ``1999``.
        seed: [integer, optional] Seed for the bootstrap (default 2025). Default ``2025``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cw_treatweight: not implemented. The method card is in ./README.md."
    )


def cw_lateweight(
    *,
    y: Any,
    d: Any,
    z: Any,
    x: np.ndarray,
    LATT: bool | None = None,
    trim: float | None = None,
    logit: bool | None = None,
    boot: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``cw_lateweight`` -- METHOD-SELECTION card #171.

    IPW / double-ML treatment effects (ATE/ATET, IV-LATE/LATT, causal mediation).

    Category 07-causality-policy; memory class ``heavy``.

    Args:
        y: [raw_handle, required] Handle to an outcome vector (numeric).
        d: [raw_handle, required] Handle to a BINARY 0/1 (endogenous) treatment vector.
        z: [raw_handle, required] Handle to a BINARY 0/1 instrument vector (same length as y).
        x: [matrix_handle, required] Handle to a confounder matrix (confounders of z & y, no NA).
        LATT: [boolean, optional] True -> LATT (treated compliers); False -> LATE (default). Default
            ``False``.
        trim: [number, optional] Trimming of extreme instrument propensity scores (default 0.05;
            [0,0.5)). Default ``0.05``.
        logit: [boolean, optional] True=logit, False=probit (default False). Default ``False``.
        boot: [integer, optional] Bootstrap replications for the SE (default 1999; >=2). Default
            ``1999``.
        seed: [integer, optional] Seed for the bootstrap (default 2025). Default ``2025``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cw_lateweight: not implemented. The method card is in ./README.md."
    )


def cw_medDML(
    *,
    y: Any,
    d: Any,
    m: Any,
    x: np.ndarray,
    k: int | None = None,
    trim: float | None = None,
    multmed: bool | None = None,
    normalized: bool | None = None,
    MLmethod: (
        Literal[
            "lasso",
            "randomforest",
            "xgboost",
            "svm",
            "ensemble",
            "parametric",
        ]
        | None
    ) = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``cw_medDML`` -- METHOD-SELECTION card #171.

    IPW / double-ML treatment effects (ATE/ATET, IV-LATE/LATT, causal mediation).

    Category 07-causality-policy; memory class ``light``.

    Args:
        y: [raw_handle, required] Handle to an outcome vector (numeric).
        d: [raw_handle, required] Handle to a BINARY 0/1 treatment vector (same length as y).
        m: [raw_handle, required] Handle to the mediator(s): vector/matrix (multmed=True) or a
            binary scalar (multmed=False).
        x: [matrix_handle, required] Handle to a pre-treatment confounder matrix (no NA).
        k: [integer, optional] Cross-fitting folds when multmed=False (default 3; >=2). Default
            ``3``.
        trim: [number, optional] Trimming of extreme conditional probabilities (default 0.05;
            [0,0.5)). Default ``0.05``.
        multmed: [boolean, optional] True=Farbmacher et al. (multiple/continuous mediators);
            False=Tchetgen (binary scalar mediator). Default ``True``.
        normalized: [boolean, optional] Normalize the IPW weights (default True). Default ``True``.
        MLmethod: [enum, optional] ML engine for the nuisance parameters (default lasso).
        seed: [integer, optional] Seed for the random cross-fitting partition (default 2025).
            Default ``2025``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cw_medDML: not implemented. The method card is in ./README.md."
    )
