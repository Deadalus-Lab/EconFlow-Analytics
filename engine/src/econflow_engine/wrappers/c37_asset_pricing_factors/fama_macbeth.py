# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``fama_macbeth`` -- method card #318.

#318 Fama-MacBeth two-pass regression with the Shanken correction

Category 37-asset-pricing-factors; module ``fama_macbeth``.

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
    "ap_fama_macbeth",
    "NODE_META",
    "wire_model",
]


def ap_fama_macbeth(
    *,
    returns: pd.DataFrame,
    factors: pd.DataFrame,
    shanken: bool | None = None,
    intercept: bool | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``ap_fama_macbeth`` -- method card #318.

    Fama-MacBeth two-pass regression with the Shanken correction.

    Category 37-asset-pricing-factors; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        returns: [multiseries_handle, required] Excess returns of the test assets.
        factors: [multiseries_handle, required] Factor returns.
        shanken: [boolean, optional] Apply the errors-in-variables correction. Default ``True``.
        intercept: [boolean, optional] Include a cross-sectional intercept. Default ``True``.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ap_fama_macbeth: not implemented."
    )
