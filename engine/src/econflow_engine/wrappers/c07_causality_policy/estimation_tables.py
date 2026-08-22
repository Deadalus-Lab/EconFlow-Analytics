# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``estimation_tables`` -- method card #457.

#457 Publication-ready estimation tables

Category 07-causality-policy; module ``estimation_tables``.

Reference implementation: pyfixest.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

from econflow_engine.generated.args.c07_causality_policy import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "cp_estimation_table",
    "NODE_META",
    "wire_model",
]


def cp_estimation_table(
    *,
    fits: Sequence[Any],
    keep: Sequence[str] | None = None,
    format: Literal["markdown", "latex", "html", "text"] | None = None,
    stars: bool | None = None,
    digits: int | None = None,
) -> dict[str, Any]:
    """Node ``cp_estimation_table`` -- method card #457.

    Publication-ready estimation tables.

    Category 07-causality-policy; memory class ``light``.

    Args:
        fits: [raw_handle_array, required] Handles to the fitted models.
        keep: [series_codes, optional] Coefficients to display.
        format: [enum, optional] Output format. Default ``'markdown'``.
        stars: [boolean, optional] Include significance stars. Default ``False``.
        digits: [integer, optional] Digits displayed. Default ``3``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cp_estimation_table: not implemented."
    )
