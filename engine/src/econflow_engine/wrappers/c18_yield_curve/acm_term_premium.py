# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``acm_term_premium`` -- method card #535.

#535 ACM term-premium decomposition

Category 18-yield-curve; module ``acm_term_premium``.

Reference implementation: pyacm.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c18_yield_curve import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "yc_acm_decomposition",
    "NODE_META",
    "wire_model",
]


def yc_acm_decomposition(
    *,
    yields: pd.DataFrame,
    maturities: Sequence[float],
    n_factors: int | None = None,
    real: bool | None = None,
) -> dict[str, Any]:
    """Node ``yc_acm_decomposition`` -- method card #535.

    ACM term-premium decomposition.

    Category 18-yield-curve; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        yields: [df_handle, required] Yield panel, one column per maturity.
        maturities: [num_array, required] Maturities in years.
        n_factors: [integer, optional] Pricing factors extracted. Default ``5``.
        real: [boolean, optional] Decompose real rather than nominal yields. Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "yc_acm_decomposition: not implemented."
    )
