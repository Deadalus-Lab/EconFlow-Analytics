# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``hidden_bias`` -- method card #281.

#281 Sensitivity to hidden bias: Rosenbaum bounds and the E-value

Category 32-matching-weighting; module ``hidden_bias``.

Reference implementation: 10.7326/M16-2607.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c32_matching_weighting import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "mw_e_value",
    "mw_rosenbaum_bounds",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def mw_rosenbaum_bounds(
    *,
    matched: Any,
    outcome: pd.Series,
    gamma_max: float | None = None,
    gamma_step: float | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``mw_rosenbaum_bounds`` -- method card #281.

    Sensitivity to hidden bias: Rosenbaum bounds and the E-value.

    Category 32-matching-weighting; memory class ``light``.

    Args:
        matched: [raw_handle, required] Handle to a completed matching.
        outcome: [series_handle, required] Outcome per unit.
        gamma_max: [number, optional] Largest hidden-bias odds ratio to scan. Default ``3.0``.
        gamma_step: [number, optional] Step of the gamma grid. Default ``0.1``.
        alpha: [number, optional] Significance level. Default ``0.05``.

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
        "mw_rosenbaum_bounds: not implemented."
    )


def mw_e_value(
    *,
    estimate: float,
    lower: float | None = None,
    upper: float | None = None,
    scale: Literal["risk_ratio", "odds_ratio", "hazard_ratio", "standardised_mean"] | None = None,
) -> dict[str, Any]:
    """Node ``mw_e_value`` -- method card #281.

    Sensitivity to hidden bias: Rosenbaum bounds and the E-value.

    Category 32-matching-weighting; memory class ``light``.

    Args:
        estimate: [number, required] The effect estimate, on the ratio scale.
        lower: [number, optional] Lower confidence limit.
        upper: [number, optional] Upper confidence limit.
        scale: [enum, optional] Scale the estimate is reported on. Default ``'risk_ratio'``.

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
        "mw_e_value: not implemented."
    )
