# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``tobit_censored`` -- method card #525.

#525 Truncated and censored regression: Tobit and variants

Category 16-limited-dependent; module ``tobit_censored``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c16_limited_dependent import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ld_tobit",
    "NODE_META",
    "wire_model",
]


def ld_tobit(
    *,
    y: pd.Series,
    x: pd.DataFrame,
    left: float | None = None,
    right: float | None = None,
    model: Literal["censored", "truncated", "two_part"] | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``ld_tobit`` -- method card #525.

    Truncated and censored regression: Tobit and variants.

    Category 16-limited-dependent; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Outcome.
        x: [df_handle, required] Covariate table.
        left: [number, optional] Left censoring or truncation limit.
        right: [number, optional] Right censoring or truncation limit.
        model: [enum, optional] Model. Default ``'censored'``.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ld_tobit: not implemented."
    )
