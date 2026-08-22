# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``polarisation`` -- method card #563.

#563 Polarisation indices

Category 22-inequality; module ``polarisation``.

Reference implementation: ineqpy.

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
    "iq_polarisation",
    "NODE_META",
    "wire_model",
]


def iq_polarisation(
    *,
    income: pd.Series,
    weights: pd.Series | None = None,
    index: Literal["foster_wolfson", "wolfson", "esteban_ray", "duclos_esteban_ray"] | None = None,
    alpha: float | None = None,
    n_groups: int | None = None,
) -> dict[str, Any]:
    """Node ``iq_polarisation`` -- method card #563.

    Polarisation indices.

    Category 22-inequality; memory class ``light``.

    Args:
        income: [series_handle, required] Income.
        weights: [series_handle, optional] Survey weights.
        index: [enum, optional] Index. Default ``'foster_wolfson'``.
        alpha: [number, optional] Sensitivity parameter for the Esteban-Ray family. Default ``1.0``.
        n_groups: [integer, optional] Groups used for identification. Default ``10``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "iq_polarisation: not implemented."
    )
