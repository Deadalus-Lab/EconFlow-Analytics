# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``poverty_measures`` -- method card #558.

#558 Poverty measures with design-based inference

Category 22-inequality; module ``poverty_measures``.

Reference implementation: svy.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c22_inequality import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "iq_poverty_measures",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def iq_poverty_measures(
    *,
    income: pd.Series,
    weights: pd.Series | None = None,
    strata: pd.Series | None = None,
    cluster: pd.Series | None = None,
    line: float | None = None,
    relative: float | None = None,
    by: Sequence[str] | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``iq_poverty_measures`` -- method card #558.

    Poverty measures with design-based inference.

    Category 22-inequality; memory class ``light``.

    Args:
        income: [series_handle, required] Equivalised income.
        weights: [series_handle, optional] Survey weights.
        strata: [series_handle, optional] Design strata.
        cluster: [series_handle, optional] Primary sampling units.
        line: [number, optional] Absolute poverty line.
        relative: [number, optional] Relative line as a share of the median. Default ``0.6``.
        by: [series_codes, optional] Subgroup columns.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

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
        "iq_poverty_measures: not implemented."
    )
