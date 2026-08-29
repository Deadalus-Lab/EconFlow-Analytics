# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``breusch_godfrey_breusch`` -- method card #76.

#76 Breusch-Godfrey / Breusch-Pagan / Ramsey RESET

Category 15-model-evaluation; module ``breusch_godfrey_breusch``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c15_model_evaluation import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "run_bg_test",
    "run_bp_test",
    "run_reset_test",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def run_bg_test(
    *,
    formula: str,
    order: int | None = None,
    type: Literal["Chisq", "F"] | None = None,
    data: pd.DataFrame | None = None,
) -> dict[str, Any]:
    """Node ``run_bg_test`` -- method card #76.

    Breusch-Godfrey / Breusch-Pagan / Ramsey RESET.

    Category 15-model-evaluation; memory class ``light``.

    Args:
        formula: [formula, required] Model formula (e.g. 'y ~ x1 + x2') for Breusch-Godfrey
            serial-correlation.
        order: [integer, optional] Order of serial correlation to test (positive integer, default
            1). Default ``1``.
        type: [enum, optional] Statistic type (default Chisq).
        data: [df_handle, optional] Handle to a DataFrame with the formula variables.

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
        "run_bg_test: not implemented."
    )


def run_bp_test(
    *,
    formula: str,
    studentize: bool | None = None,
    data: pd.DataFrame | None = None,
) -> dict[str, Any]:
    """Node ``run_bp_test`` -- method card #76.

    Breusch-Godfrey / Breusch-Pagan / Ramsey RESET.

    Category 15-model-evaluation; memory class ``light``.

    Args:
        formula: [formula, required] Model formula for Breusch-Pagan heteroskedasticity.
        studentize: [boolean, optional] Koenker studentized version (robust to non-normality,
            default True). Default ``True``.
        data: [df_handle, optional] Handle to a DataFrame with the formula variables.

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
        "run_bp_test: not implemented."
    )


def run_reset_test(
    *,
    formula: str,
    power: int | None = None,
    type: Literal["fitted", "regressor", "princomp"] | None = None,
    data: pd.DataFrame | None = None,
) -> dict[str, Any]:
    """Node ``run_reset_test`` -- method card #76.

    Breusch-Godfrey / Breusch-Pagan / Ramsey RESET.

    Category 15-model-evaluation; memory class ``light``.

    Args:
        formula: [formula, required] Model formula for Ramsey RESET functional-form
            misspecification.
        power: [integer, optional] Power of the fitted values in the auxiliary regression (integer
            >= 2· default 2:3).
        type: [enum, optional] Source of the non-linear terms (default fitted).
        data: [df_handle, optional] Handle to a DataFrame with the formula variables.

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
        "run_reset_test: not implemented."
    )
