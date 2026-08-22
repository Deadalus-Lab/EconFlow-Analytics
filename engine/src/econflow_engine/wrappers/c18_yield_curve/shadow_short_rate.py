# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``shadow_short_rate`` -- method card #538.

#538 Shadow short rate at the effective lower bound

Category 18-yield-curve; module ``shadow_short_rate``.

Reference implementation: srvar-toolkit.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c18_yield_curve import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "yc_shadow_short_rate",
    "NODE_META",
    "wire_model",
]


def yc_shadow_short_rate(
    *,
    yields: pd.DataFrame,
    maturities: Sequence[float],
    lower_bound: float | None = None,
    n_factors: int | None = None,
    model: Literal["wu_xia", "krippner"] | None = None,
) -> dict[str, Any]:
    """Node ``yc_shadow_short_rate`` -- method card #538.

    Shadow short rate at the effective lower bound.

    Category 18-yield-curve; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        yields: [df_handle, required] Yield panel.
        maturities: [num_array, required] Maturities in years.
        lower_bound: [number, optional] Effective lower bound. Default ``0.0``.
        n_factors: [integer, optional] Factors in the term-structure model. Default ``3``.
        model: [enum, optional] Construction. Default ``'wu_xia'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "yc_shadow_short_rate: not implemented."
    )
