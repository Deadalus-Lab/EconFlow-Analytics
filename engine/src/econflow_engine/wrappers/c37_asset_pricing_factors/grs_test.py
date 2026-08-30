# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``grs_test`` -- method card #317.

#317 The GRS joint test of zero alphas

Category 37-asset-pricing-factors; module ``grs_test``.

Reference implementation: linearmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any

import pandas as pd

from econflow_engine.generated.args.c37_asset_pricing_factors import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ap_grs_test",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


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
        "ap_grs_test: not implemented."
    )
