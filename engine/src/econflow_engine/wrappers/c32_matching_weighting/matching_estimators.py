# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``matching_estimators`` -- method card #275.

#275 Nearest-neighbour, caliper, kernel and radius matching

Category 32-matching-weighting; module ``matching_estimators``.

Reference implementation: psmpy.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c32_matching_weighting import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "mw_match",
    "mw_match_effect",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def mw_match(
    *,
    data: pd.DataFrame,
    treatment: str,
    pscore: str | None = None,
    covariates: Sequence[str] | None = None,
    method: Literal["nearest", "caliper", "kernel", "radius", "mahalanobis"] | None = None,
    n_neighbors: int | None = None,
    caliper: float | None = None,
    replace: bool | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``mw_match`` -- method card #275.

    Nearest-neighbour, caliper, kernel and radius matching.

    Category 32-matching-weighting; memory class ``light``.

    Registers its result under ``matched``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] One row per unit.
        treatment: [string, required] Binary treatment column.
        pscore: [string, optional] Column holding a pre-computed propensity score.
        covariates: [series_codes, optional] Covariates used when matching directly.
        method: [enum, optional] Matching rule. Default ``'nearest'``.
        n_neighbors: [integer, optional] Controls matched per treated unit. Default ``1``.
        caliper: [number, optional] Maximum admissible distance.
        replace: [boolean, optional] Match with replacement. Default ``True``.
        seed: [integer, optional] Seed for the random number generator.

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
        "mw_match: not implemented."
    )


def mw_match_effect(
    *,
    matched: Any,
    outcome: pd.Series,
    estimand: Literal["att", "atc", "ate"] | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``mw_match_effect`` -- method card #275.

    Nearest-neighbour, caliper, kernel and radius matching.

    Category 32-matching-weighting; memory class ``light``.

    Args:
        matched: [raw_handle, required] Handle to a completed matching.
        outcome: [series_handle, required] Outcome per unit.
        estimand: [enum, optional] Estimand to report. Default ``'att'``.
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
        "mw_match_effect: not implemented."
    )
