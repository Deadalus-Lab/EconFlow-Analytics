# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``financial_stress_index`` -- method card #556.

#556 Composite financial-stress index

Category 21-systemic-risk; module ``financial_stress_index``.

Reference implementation: scipy.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c21_systemic_risk import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "sr_stress_index",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def sr_stress_index(
    *,
    indicators: pd.DataFrame,
    segments: Sequence[str] | None = None,
    transform: Literal["empirical_cdf", "standardise", "rank"] | None = None,
    recursive: bool | None = None,
    correlation_window: int | None = None,
) -> dict[str, Any]:
    """Node ``sr_stress_index`` -- method card #556.

    Composite financial-stress index.

    Category 21-systemic-risk; memory class ``light``.

    Args:
        indicators: [df_handle, required] Stress indicators, one column each.
        segments: [series_codes, optional] Segment label per indicator.
        transform: [enum, optional] Transformation to a common scale. Default ``'empirical_cdf'``.
        recursive: [boolean, optional] Use recursive rather than full-sample transformation. Default
            ``True``.
        correlation_window: [integer, optional] Window for the time-varying correlation. Default
            ``250``.

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
        "sr_stress_index: not implemented."
    )
