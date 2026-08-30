# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``deterministic_terms`` -- method card #385.

#385 Deterministic-term generator: seasonal dummies, Fourier harmonics and trends

Category 00-data-utilities; module ``deterministic_terms``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any

import pandas as pd

from econflow_engine.generated.args.c00_data_utilities import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "du_deterministic_terms",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


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
        "du_deterministic_terms: not implemented."
    )
