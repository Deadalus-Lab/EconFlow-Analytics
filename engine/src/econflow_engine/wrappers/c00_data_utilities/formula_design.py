# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``formula_design`` -- method card #389.

#389 Formula parsing and the design-matrix contract

Category 00-data-utilities; module ``formula_design``.

Reference implementation: formulaic.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c00_data_utilities import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "du_apply_design",
    "du_design_matrix",
    "NODE_META",
    "wire_model",
]


def du_design_matrix(
    *,
    data: pd.DataFrame,
    formula: str,
    contrasts: Literal["treatment", "sum", "helmert", "poly", "backward_difference"] | None = None,
    na_action: Literal["drop", "raise", "keep"] | None = None,
) -> dict[str, Any]:
    """Node ``du_design_matrix`` -- method card #389.

    Formula parsing and the design-matrix contract.

    Category 00-data-utilities; memory class ``light``.

    Registers its result under ``design``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] Source table.
        formula: [formula, required] Model formula.
        contrasts: [enum, optional] Factor coding. Default ``'treatment'``.
        na_action: [enum, optional] Missing-value handling. Default ``'drop'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "du_design_matrix: not implemented."
    )


def du_apply_design(
    *,
    design: Any,
    data: pd.DataFrame,
) -> dict[str, Any]:
    """Node ``du_apply_design`` -- method card #389.

    Formula parsing and the design-matrix contract.

    Category 00-data-utilities; memory class ``light``.

    Args:
        design: [raw_handle, required] Handle to a stored design contract.
        data: [df_handle, required] New data to transform.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "du_apply_design: not implemented."
    )
