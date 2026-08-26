# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``factor_regressions`` -- method card #316.

#316 Time-series factor regressions with alphas: CAPM, Fama-French three and five factor, Carhart

Category 37-asset-pricing-factors; module ``factor_regressions``.

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
    "ap_alpha_table",
    "ap_factor_regression",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def ap_factor_regression(
    *,
    returns: pd.DataFrame,
    factors: pd.DataFrame,
    cov_type: Literal["nonrobust", "robust", "hac"] | None = None,
    bandwidth: int | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``ap_factor_regression`` -- method card #316.

    Time-series factor regressions with alphas: CAPM, Fama-French three and five factor, Carhart.

    Category 37-asset-pricing-factors; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        returns: [multiseries_handle, required] Excess returns, one column per test asset.
        factors: [multiseries_handle, required] Factor returns.
        cov_type: [enum, optional] Covariance estimator. Default ``'hac'``.
        bandwidth: [integer, optional] HAC lag truncation; omitted = automatic.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

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
        "ap_factor_regression: not implemented."
    )


def ap_alpha_table(
    *,
    fit: Any,
    annualise: bool | None = None,
) -> dict[str, Any]:
    """Node ``ap_alpha_table`` -- method card #316.

    Time-series factor regressions with alphas: CAPM, Fama-French three and five factor, Carhart.

    Category 37-asset-pricing-factors; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a fitted factor regression.
        annualise: [boolean, optional] Report alpha in annual units. Default ``True``.

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
        "ap_alpha_table: not implemented."
    )
