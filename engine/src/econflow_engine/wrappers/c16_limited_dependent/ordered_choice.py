# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``ordered_choice`` -- method card #523.

#523 Ordered logit and probit

Category 16-limited-dependent; module ``ordered_choice``.

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
    "ld_ordered_choice",
    "ld_proportional_odds_test",
    "NODE_META",
    "wire_model",
]


def ld_ordered_choice(
    *,
    y: pd.Series,
    x: pd.DataFrame,
    link: Literal["logit", "probit", "cloglog"] | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``ld_ordered_choice`` -- method card #523.

    Ordered logit and probit.

    Category 16-limited-dependent; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Ordered categorical outcome.
        x: [df_handle, required] Covariate table.
        link: [enum, optional] Link function. Default ``'logit'``.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ld_ordered_choice: not implemented."
    )


def ld_proportional_odds_test(
    *,
    fit: Any,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``ld_proportional_odds_test`` -- method card #523.

    Ordered logit and probit.

    Category 16-limited-dependent; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a fitted ordered model.
        alpha: [number, optional] Significance level. Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ld_proportional_odds_test: not implemented."
    )
