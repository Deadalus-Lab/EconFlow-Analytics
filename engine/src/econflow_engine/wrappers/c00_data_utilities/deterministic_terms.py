# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``deterministic_terms`` -- method card #385.

#385 Deterministic-term generator: seasonal dummies, Fourier harmonics and trends

Category 00-data-utilities; module ``deterministic_terms``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c00_data_utilities import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "du_deterministic_terms",
    "NODE_META",
    "wire_model",
]


def du_deterministic_terms(
    *,
    index: pd.Series,
    seasonal: bool | None = None,
    period: int | None = None,
    fourier: int | None = None,
    trend_order: int | None = None,
    constant: bool | None = None,
    steps: int | None = None,
) -> dict[str, Any]:
    """Node ``du_deterministic_terms`` -- method card #385.

    Deterministic-term generator: seasonal dummies, Fourier harmonics and trends.

    Category 00-data-utilities; memory class ``light``.

    Args:
        index: [series_handle, required] Date index for the estimation sample.
        seasonal: [boolean, optional] Include seasonal dummies. Default ``False``.
        period: [integer, optional] Seasonal period.
        fourier: [integer, optional] Number of Fourier harmonic pairs. Default ``0``.
        trend_order: [integer, optional] Polynomial trend order; 0 = none. Default ``0``.
        constant: [boolean, optional] Include an intercept. Default ``True``.
        steps: [integer, optional] Forecast horizon to extend the terms over. Default ``0``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "du_deterministic_terms: not implemented."
    )
