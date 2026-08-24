# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``scorecards`` -- method card #349.

#349 Credit scorecards: optimal binning, weight of evidence and monotonic constraints

Category 41-credit-risk-default; module ``scorecards``.

Reference implementation: optbinning.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c41_credit_risk_default import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "cr_optimal_binning",
    "cr_scorecard",
    "cr_woe_transform",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def cr_optimal_binning(
    *,
    x: pd.Series,
    y: pd.Series,
    monotonic_trend: (
        Literal[
            "auto",
            "ascending",
            "descending",
            "convex",
            "concave",
            "none",
        ]
        | None
    ) = None,
    max_bins: int | None = None,
    min_bin_size: float | None = None,
) -> dict[str, Any]:
    """Node ``cr_optimal_binning`` -- method card #349.

    Credit scorecards: optimal binning, weight of evidence and monotonic constraints.

    Category 41-credit-risk-default; memory class ``light``.

    Args:
        x: [series_handle, required] Characteristic to bin.
        y: [series_handle, required] Binary default indicator.
        monotonic_trend: [enum, optional] Required trend of the default rate. Default ``'auto'``.
        max_bins: [integer, optional] Maximum number of bins. Default ``10``.
        min_bin_size: [number, optional] Minimum share of observations per bin. Default ``0.05``.

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
        "cr_optimal_binning: not implemented."
    )


def cr_woe_transform(
    *,
    x: pd.Series,
    y: pd.Series,
    bins: Sequence[float] | None = None,
    smoothing: float | None = None,
) -> dict[str, Any]:
    """Node ``cr_woe_transform`` -- method card #349.

    Credit scorecards: optimal binning, weight of evidence and monotonic constraints.

    Category 41-credit-risk-default; memory class ``light``.

    Args:
        x: [series_handle, required] Characteristic to transform.
        y: [series_handle, required] Binary default indicator.
        bins: [num_array, optional] Bin edges; omitted = fitted here.
        smoothing: [number, optional] Laplace smoothing for empty cells. Default ``0.5``.

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
        "cr_woe_transform: not implemented."
    )


def cr_scorecard(
    *,
    data: pd.DataFrame,
    y: str,
    covariates: Sequence[str] | None = None,
    base_points: float | None = None,
    pdo: float | None = None,
) -> dict[str, Any]:
    """Node ``cr_scorecard`` -- method card #349.

    Credit scorecards: optimal binning, weight of evidence and monotonic constraints.

    Category 41-credit-risk-default; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] Training table.
        y: [string, required] Binary default indicator column.
        covariates: [series_codes, optional] Characteristic columns.
        base_points: [number, optional] Score at the base odds. Default ``600.0``.
        pdo: [number, optional] Points to double the odds. Default ``20.0``.

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
        "cr_scorecard: not implemented."
    )
