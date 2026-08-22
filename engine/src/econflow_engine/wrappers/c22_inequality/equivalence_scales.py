# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``equivalence_scales`` -- method card #564.

#564 Equivalence scales and household-to-individual welfare aggregation

Category 22-inequality; module ``equivalence_scales``.

Reference implementation: pandas.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c22_inequality import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "iq_equivalise",
    "NODE_META",
    "wire_model",
]


def iq_equivalise(
    *,
    income: pd.Series,
    n_adults: pd.Series,
    n_children: pd.Series | None = None,
    scale: (
        Literal[
            "per_capita",
            "household",
            "oecd",
            "oecd_modified",
            "square_root",
            "custom",
        ]
        | None
    ) = None,
    elasticity: float | None = None,
    sensitivity: bool | None = None,
) -> dict[str, Any]:
    """Node ``iq_equivalise`` -- method card #564.

    Equivalence scales and household-to-individual welfare aggregation.

    Category 22-inequality; memory class ``light``.

    Args:
        income: [series_handle, required] Household income.
        n_adults: [series_handle, required] Adults per household.
        n_children: [series_handle, optional] Children per household.
        scale: [enum, optional] Equivalence scale. Default ``'oecd_modified'``.
        elasticity: [number, optional] Elasticity for a custom scale. Default ``0.5``.
        sensitivity: [boolean, optional] Report results across the standard scales. Default
            ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "iq_equivalise: not implemented."
    )
