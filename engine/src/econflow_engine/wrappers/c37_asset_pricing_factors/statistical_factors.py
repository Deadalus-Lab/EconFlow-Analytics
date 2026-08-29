# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``statistical_factors`` -- method card #321.

#321 Statistical factors: principal components, asymptotic PCA and risk-premium PCA

Category 37-asset-pricing-factors; module ``statistical_factors``.

Reference implementation: scikit-learn.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c37_asset_pricing_factors import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ap_n_factors_test",
    "ap_pca_factors",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


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

    Gates:
        None declared. The ``precondition_gates`` field of this method card is empty; the checks a
        body must run are named here once the field carries them.

    .. gen_wrappers: end of generated docstring

    Examples:
        None yet. This node raises ``NotImplementedError``; its example is written with its body and
        belongs to whoever writes it.

    Note:
        The implementation note is written with the body: the library functions it calls and their
        versions, what the method leaves out, and every gate added with the source that requires it.
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

    Gates:
        None declared. The ``precondition_gates`` field of this method card is empty; the checks a
        body must run are named here once the field carries them.

    .. gen_wrappers: end of generated docstring

    Examples:
        None yet. This node raises ``NotImplementedError``; its example is written with its body and
        belongs to whoever writes it.

    Note:
        The implementation note is written with the body: the library functions it calls and their
        versions, what the method leaves out, and every gate added with the source that requires it.
    """
    raise NotImplementedError(
        "ap_n_factors_test: not implemented."
    )
