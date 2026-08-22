# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``favar`` -- method card #418.

#418 Factor-augmented vector autoregression

Category 03-multivariate-nowcasting; module ``favar``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c03_multivariate_nowcasting import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "mn_favar",
    "NODE_META",
    "wire_model",
]


def mn_favar(
    *,
    panel: pd.DataFrame,
    observed: pd.DataFrame,
    n_factors: int | None = None,
    lags: int | None = None,
    standardise: bool | None = None,
) -> dict[str, Any]:
    """Node ``mn_favar`` -- method card #418.

    Factor-augmented vector autoregression.

    Category 03-multivariate-nowcasting; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        panel: [df_handle, required] Large panel of indicators.
        observed: [multiseries_handle, required] Observed variables entering the VAR directly.
        n_factors: [integer, optional] Number of factors; omitted = selected by criterion.
        lags: [integer, optional] VAR lag order. Default ``4``.
        standardise: [boolean, optional] Standardise the panel before extraction. Default ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mn_favar: not implemented."
    )
