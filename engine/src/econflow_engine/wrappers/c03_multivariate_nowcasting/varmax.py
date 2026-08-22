# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``varmax`` -- method card #419.

#419 VARMA and VARMAX estimation in state-space form

Category 03-multivariate-nowcasting; module ``varmax``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c03_multivariate_nowcasting import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "mn_varmax",
    "NODE_META",
    "wire_model",
]


def mn_varmax(
    *,
    y: pd.DataFrame,
    exog: np.ndarray | None = None,
    order: Sequence[int] | None = None,
    trend: Literal["n", "c", "t", "ct"] | None = None,
    error_cov_type: Literal["diagonal", "unstructured"] | None = None,
) -> dict[str, Any]:
    """Node ``mn_varmax`` -- method card #419.

    VARMA and VARMAX estimation in state-space form.

    Category 03-multivariate-nowcasting; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        y: [multiseries_handle, required] Endogenous variables.
        exog: [exog_handle, optional] Exogenous variables.
        order: [int_array, optional] Autoregressive and moving-average orders. Default ``[1, 0]``.
        trend: [enum, optional] Deterministic terms. Default ``'c'``.
        error_cov_type: [enum, optional] Error covariance structure. Default ``'unstructured'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mn_varmax: not implemented."
    )
