# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``favar`` -- method card #418.

#418 Factor-augmented vector autoregression

Category 03-multivariate-nowcasting; module ``favar``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any

import pandas as pd

from econflow_engine.generated.args.c03_multivariate_nowcasting import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "mn_favar",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


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
        "mn_favar: not implemented."
    )
