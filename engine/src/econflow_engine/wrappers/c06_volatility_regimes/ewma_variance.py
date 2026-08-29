# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``ewma_variance`` -- method card #438.

#438 EWMA and RiskMetrics variance

Category 06-volatility-regimes; module ``ewma_variance``.

Reference implementation: arch.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c06_volatility_regimes import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "vr_ewma",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def vr_ewma(
    *,
    y: pd.Series,
    lambda_: float | None = None,
    initial: Literal["sample_variance", "first_observation", "backcast"] | None = None,
) -> dict[str, Any]:
    """Node ``vr_ewma`` -- method card #438.

    EWMA and RiskMetrics variance.

    Category 06-volatility-regimes; memory class ``light``.

    Args:
        y: [series_handle, required] Return series.
        lambda_: [number, optional] Decay factor. Default ``0.94``.
        initial: [enum, optional] Initialisation of the recursion. Default ``'sample_variance'``.

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
        "vr_ewma: not implemented."
    )
