# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``generalized_moments_hansen`` -- method card #172.

#172 Generalized Method of Moments (linear IV / moment conditions) + the Hansen-Sargan J test

Category 07-causality-policy; module ``generalized_moments_hansen``.

Reference implementation: linearmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c07_causality_policy import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "gmm_fit",
    "gmm_j_test",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def gmm_fit(
    *,
    formula: str,
    instruments: str,
    data: pd.DataFrame,
    type: Literal["twoStep", "cue", "iterative"] | None = None,
    wmatrix: Literal["optimal", "ident"] | None = None,
    vcov: Literal["HAC", "MDS", "iid", "TrueFixed"] | None = None,
) -> dict[str, Any]:
    """Node ``gmm_fit`` -- method card #172.

    Generalized Method of Moments (linear IV / moment conditions) + the Hansen-Sargan J test.

    Category 07-causality-policy; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        formula: [formula, required] Two-sided model formula 'y ~ x1 + x2' (the moment conditions
            are defined by the instruments; formula ONLY — no moment function).
        instruments: [formula, required] One-sided instruments formula '~ z1 + z2 + z3' (>= number
            of coefficients for identification).
        data: [df_handle, required] Handle to a DataFrame holding every formula+instruments
            variable, no NA.
        type: [enum, optional] GMM estimator: two-step efficient / continuous-updating / iterative
            (default twoStep).
        wmatrix: [enum, optional] Weighting matrix: efficient optimal or identity (2SLS-type)
            (default optimal).
        vcov: [enum, optional] Variance estimator of the moments: HAC (autocorrelation-robust) / MDS
            (mart. diff.) / iid / TrueFixed (default HAC).

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
        "gmm_fit: not implemented."
    )


def gmm_j_test(
    *,
    object: Any,
) -> dict[str, Any]:
    """Node ``gmm_j_test`` -- method card #172.

    Generalized Method of Moments (linear IV / moment conditions) + the Hansen-Sargan J test.

    Category 07-causality-policy; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a fitted gmm object (from gmm_fit.object) —
            Hansen-Sargan J of overidentification.

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
        "gmm_j_test: not implemented."
    )
