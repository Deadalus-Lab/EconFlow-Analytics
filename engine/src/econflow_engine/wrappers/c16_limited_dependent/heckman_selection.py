# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``heckman_selection`` -- method card #526.

#526 Heckman sample selection, two-step and full information

Category 16-limited-dependent; module ``heckman_selection``.

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
    "ld_heckman",
    "NODE_META",
    "wire_model",
]


def ld_heckman(
    *,
    y: pd.Series,
    x: pd.DataFrame,
    selection: pd.Series,
    z: pd.DataFrame,
    method: Literal["two_step", "mle"] | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``ld_heckman`` -- method card #526.

    Heckman sample selection, two-step and full information.

    Category 16-limited-dependent; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Outcome, observed for the selected subsample.
        x: [df_handle, required] Outcome-equation covariates.
        selection: [series_handle, required] Selection indicator.
        z: [df_handle, required] Selection-equation covariates, including the exclusion.
        method: [enum, optional] Estimator. Default ``'two_step'``.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ld_heckman: not implemented."
    )
