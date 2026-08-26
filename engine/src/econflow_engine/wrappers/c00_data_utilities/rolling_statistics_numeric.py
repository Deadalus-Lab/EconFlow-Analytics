# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``rolling_statistics_numeric`` -- method card #110.

#110 Rolling O(n) statistics (mean/sd/min/max/quantile/mad) on a numeric vector/matrix

Category 00-data-utilities; module ``rolling_statistics_numeric``.

Reference implementation: pandas.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c00_data_utilities import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "roll_mad",
    "roll_max",
    "roll_mean",
    "roll_min",
    "roll_quantile",
    "roll_sd",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def roll_mean(
    *,
    x: np.ndarray,
    k: int,
    endrule: Literal["mean", "NA", "trim", "keep", "constant"] | None = None,
    align: Literal["center", "left", "right"] | None = None,
) -> dict[str, Any]:
    """Node ``roll_mean`` -- method card #110.

    Rolling O(n) statistics (mean/sd/min/max/quantile/mad) on a numeric vector/matrix.

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a numeric vector/matrix (matrix: rolling column by
            column).
        k: [integer, required] Rolling window width; finite integer in [1, nobs]. align='center'
            requires an ODD k.
        endrule: [enum, optional] Edge handling: mean=fill with the statistic (default), NA,
            trim=cut, keep, constant.
        align: [enum, optional] Window alignment: center (default), left, right (trailing).

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
        "roll_mean: not implemented."
    )


def roll_sd(
    *,
    x: np.ndarray,
    k: int,
    center: Sequence[float] | None = None,
    endrule: Literal["sd", "NA", "trim", "keep", "constant"] | None = None,
    align: Literal["center", "left", "right"] | None = None,
) -> dict[str, Any]:
    """Node ``roll_sd`` -- method card #110.

    Rolling O(n) statistics (mean/sd/min/max/quantile/mad) on a numeric vector/matrix.

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a numeric vector/matrix.
        k: [integer, required] Rolling window width in [1, nobs]; align='center' => odd k.
        center: [num_array, optional] Optional per-window center of length nobs (one per
            observation); empty=rolling mean. Wrong length => silent recycling => gate.
        endrule: [enum, optional] Edge handling (default sd).
        align: [enum, optional] Window alignment (default center).

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
        "roll_sd: not implemented."
    )


def roll_min(
    *,
    x: np.ndarray,
    k: int,
    endrule: Literal["min", "NA", "trim", "keep", "constant"] | None = None,
    align: Literal["center", "left", "right"] | None = None,
) -> dict[str, Any]:
    """Node ``roll_min`` -- method card #110.

    Rolling O(n) statistics (mean/sd/min/max/quantile/mad) on a numeric vector/matrix.

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a numeric vector/matrix.
        k: [integer, required] Rolling window width in [1, nobs]; align='center' => odd k.
        endrule: [enum, optional] Edge handling (default min).
        align: [enum, optional] Window alignment (default center).

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
        "roll_min: not implemented."
    )


def roll_max(
    *,
    x: np.ndarray,
    k: int,
    endrule: Literal["max", "NA", "trim", "keep", "constant"] | None = None,
    align: Literal["center", "left", "right"] | None = None,
) -> dict[str, Any]:
    """Node ``roll_max`` -- method card #110.

    Rolling O(n) statistics (mean/sd/min/max/quantile/mad) on a numeric vector/matrix.

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a numeric vector/matrix.
        k: [integer, required] Rolling window width in [1, nobs]; align='center' => odd k.
        endrule: [enum, optional] Edge handling (default max).
        align: [enum, optional] Window alignment (default center).

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
        "roll_max: not implemented."
    )


def roll_quantile(
    *,
    x: np.ndarray,
    k: int,
    probs: Sequence[float],
    type: int | None = None,
    endrule: Literal["quantile", "NA", "trim", "keep", "constant"] | None = None,
    align: Literal["center", "left", "right"] | None = None,
) -> dict[str, Any]:
    """Node ``roll_quantile`` -- method card #110.

    Rolling O(n) statistics (mean/sd/min/max/quantile/mad) on a numeric vector/matrix.

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a numeric vector/matrix.
        k: [integer, required] Rolling window width in [1, nobs]; align='center' => odd k.
        probs: [num_array, required] Non-empty vector of probabilities in [0,1] (passed WHOLE, not a
            single-choice match).
        type: [integer, optional] Quantile algorithm, integer in [1,9] (as the quantile estimator;
            default 7). Default ``7``.
        endrule: [enum, optional] Edge handling (default quantile).
        align: [enum, optional] Window alignment (default center).

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
        "roll_quantile: not implemented."
    )


def roll_mad(
    *,
    x: np.ndarray,
    k: int,
    center: Sequence[float] | None = None,
    constant: float | None = None,
    endrule: Literal["mad", "NA", "trim", "keep", "constant"] | None = None,
    align: Literal["center", "left", "right"] | None = None,
) -> dict[str, Any]:
    """Node ``roll_mad`` -- method card #110.

    Rolling O(n) statistics (mean/sd/min/max/quantile/mad) on a numeric vector/matrix.

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a numeric vector/matrix.
        k: [integer, required] Rolling window width in [1, nobs]; align='center' => odd k.
        center: [num_array, optional] Optional per-window center of length nobs; empty=rolling
            median. Wrong length => silent recycling => gate.
        constant: [number, optional] Positive consistency factor for Gaussian data (default 1.4826).
            Default ``1.4826``.
        endrule: [enum, optional] Edge handling (default mad).
        align: [enum, optional] Window alignment (default center).

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
        "roll_mad: not implemented."
    )
