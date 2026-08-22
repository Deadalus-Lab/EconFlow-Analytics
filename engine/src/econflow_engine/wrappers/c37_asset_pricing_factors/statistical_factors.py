# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``statistical_factors`` -- method card #321.

#321 Statistical factors: principal components, asymptotic PCA and risk-premium PCA

Category 37-asset-pricing-factors; module ``statistical_factors``.

Reference implementation: scikit-learn.

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
    "ap_n_factors_test",
    "ap_pca_factors",
    "NODE_META",
    "wire_model",
]


def ap_pca_factors(
    *,
    returns: pd.DataFrame,
    n_factors: int | None = None,
    method: Literal["pca", "asymptotic_pca", "rp_pca"] | None = None,
    criterion: (
        Literal[
            "bai_ng_icp1",
            "bai_ng_icp2",
            "bai_ng_icp3",
            "scree",
            "explained_variance",
        ]
        | None
    ) = None,
    standardise: bool | None = None,
) -> dict[str, Any]:
    """Node ``ap_pca_factors`` -- method card #321.

    Statistical factors: principal components, asymptotic PCA and risk-premium PCA.

    Category 37-asset-pricing-factors; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        returns: [df_handle, required] Panel of asset returns.
        n_factors: [integer, optional] Factors to extract; omitted = selected by criterion.
        method: [enum, optional] Extraction method. Default ``'pca'``.
        criterion: [enum, optional] Selection criterion when n_factors is omitted. Default
            ``'bai_ng_icp2'``.
        standardise: [boolean, optional] Standardise returns before extraction. Default ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ap_pca_factors: not implemented."
    )


def ap_n_factors_test(
    *,
    returns: pd.DataFrame,
    k_max: int | None = None,
) -> dict[str, Any]:
    """Node ``ap_n_factors_test`` -- method card #321.

    Statistical factors: principal components, asymptotic PCA and risk-premium PCA.

    Category 37-asset-pricing-factors; memory class ``light``.

    Args:
        returns: [df_handle, required] Panel of asset returns.
        k_max: [integer, optional] Largest number of factors considered. Default ``10``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ap_n_factors_test: not implemented."
    )
