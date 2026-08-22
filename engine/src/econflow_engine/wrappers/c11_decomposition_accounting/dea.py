# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``dea`` -- method card #486.

#486 Data envelopment analysis with scale and technical decomposition

Category 11-decomposition-accounting; module ``dea``.

Reference implementation: Pyfrontier.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c11_decomposition_accounting import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "da_dea",
    "NODE_META",
    "wire_model",
]


def da_dea(
    *,
    inputs: pd.DataFrame,
    outputs: pd.DataFrame,
    returns: Literal["crs", "vrs", "nirs", "ndrs"] | None = None,
    orientation: Literal["input", "output"] | None = None,
    decompose: bool | None = None,
) -> dict[str, Any]:
    """Node ``da_dea`` -- method card #486.

    Data envelopment analysis with scale and technical decomposition.

    Category 11-decomposition-accounting; memory class ``light``.

    Args:
        inputs: [df_handle, required] Input table.
        outputs: [df_handle, required] Output table.
        returns: [enum, optional] Returns to scale. Default ``'vrs'``.
        orientation: [enum, optional] Orientation. Default ``'input'``.
        decompose: [boolean, optional] Separate technical and scale efficiency. Default ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "da_dea: not implemented."
    )
