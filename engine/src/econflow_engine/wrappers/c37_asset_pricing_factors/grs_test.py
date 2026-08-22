# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``grs_test`` -- method card #317.

#317 The GRS joint test of zero alphas

Category 37-asset-pricing-factors; module ``grs_test``.

Reference implementation: linearmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c37_asset_pricing_factors import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ap_grs_test",
    "NODE_META",
    "wire_model",
]


def ap_grs_test(
    *,
    returns: pd.DataFrame,
    factors: pd.DataFrame,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``ap_grs_test`` -- method card #317.

    The GRS joint test of zero alphas.

    Category 37-asset-pricing-factors; memory class ``light``.

    Args:
        returns: [multiseries_handle, required] Excess returns of the test assets.
        factors: [multiseries_handle, required] Factor returns.
        alpha: [number, optional] Significance level. Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ap_grs_test: not implemented."
    )
