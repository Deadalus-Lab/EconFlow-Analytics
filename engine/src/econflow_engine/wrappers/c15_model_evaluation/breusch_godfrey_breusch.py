# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``breusch_godfrey_breusch`` -- method card #76.

#76 Breusch-Godfrey / Breusch-Pagan / Ramsey RESET

Category 15-model-evaluation; module ``breusch_godfrey_breusch``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c15_model_evaluation import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "run_bg_test",
    "run_bp_test",
    "run_reset_test",
    "NODE_META",
    "wire_model",
]


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
    """
    raise NotImplementedError(
        "run_reset_test: not implemented."
    )
