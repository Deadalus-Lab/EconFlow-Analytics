# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``gmm_factor_pricing`` -- method card #319.

#319 Traded and non-traded linear factor models and GMM factor pricing

Category 37-asset-pricing-factors; module ``gmm_factor_pricing``.

Reference implementation: linearmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c37_asset_pricing_factors import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ap_pricing_errors",
    "ap_sdf_gmm",
    "NODE_META",
    "wire_model",
]


def ap_sdf_gmm(
    *,
    returns: pd.DataFrame,
    factors: pd.DataFrame,
    traded: bool | None = None,
    weighting: Literal["identity", "optimal", "hansen_jagannathan"] | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``ap_sdf_gmm`` -- method card #319.

    Traded and non-traded linear factor models and GMM factor pricing.

    Category 37-asset-pricing-factors; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        returns: [multiseries_handle, required] Excess returns of the test assets.
        factors: [multiseries_handle, required] Factor series, traded or not.
        traded: [boolean, optional] Whether the factors are traded excess returns. Default
            ``False``.
        weighting: [enum, optional] GMM weighting. Default ``'hansen_jagannathan'``.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ap_sdf_gmm: not implemented."
    )


def ap_pricing_errors(
    *,
    fit: Any,
) -> dict[str, Any]:
    """Node ``ap_pricing_errors`` -- method card #319.

    Traded and non-traded linear factor models and GMM factor pricing.

    Category 37-asset-pricing-factors; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a fitted factor-pricing model.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ap_pricing_errors: not implemented."
    )
