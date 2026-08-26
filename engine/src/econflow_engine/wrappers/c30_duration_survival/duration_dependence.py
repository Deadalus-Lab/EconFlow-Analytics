# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``duration_dependence`` -- method card #265.

#265 Spell duration dependence and hazard-shape estimation

Category 30-duration-survival; module ``duration_dependence``.

Reference implementation: lifelines.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c30_duration_survival import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "srv_hazard_shape",
    "srv_piecewise_hazard",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def srv_piecewise_hazard(
    *,
    time: pd.Series,
    event: pd.Series,
    breaks: Sequence[float] | None = None,
    n_intervals: int | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``srv_piecewise_hazard`` -- method card #265.

    Spell duration dependence and hazard-shape estimation.

    Category 30-duration-survival; memory class ``light``.

    Args:
        time: [series_handle, required] Observed duration.
        event: [series_handle, required] Event indicator.
        breaks: [num_array, optional] Interval boundaries; empty = equal-count intervals.
        n_intervals: [integer, optional] Number of equal-count intervals when breaks is empty.
            Default ``6``.
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
        "srv_piecewise_hazard: not implemented."
    )


def srv_hazard_shape(
    *,
    time: pd.Series,
    event: pd.Series,
    bandwidth: float | None = None,
) -> dict[str, Any]:
    """Node ``srv_hazard_shape`` -- method card #265.

    Spell duration dependence and hazard-shape estimation.

    Category 30-duration-survival; memory class ``light``.

    Args:
        time: [series_handle, required] Observed duration.
        event: [series_handle, required] Event indicator.
        bandwidth: [number, optional] Smoothing bandwidth; omitted = plug-in rule.

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
        "srv_hazard_shape: not implemented."
    )
