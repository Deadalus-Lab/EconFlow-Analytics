# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``merton_structural`` -- method card #347.

#347 Merton structural model: distance to default and implied default probability

Category 41-credit-risk-default; module ``merton_structural``.

Reference implementation: frds.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c41_credit_risk_default import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "cr_distance_to_default",
    "cr_merton_pd",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def cr_distance_to_default(
    *,
    equity_value: pd.Series,
    equity_volatility: pd.Series,
    debt: pd.Series,
    rate: pd.Series,
    horizon: float | None = None,
    barrier: Literal["total_debt", "short_plus_half_long", "short_term"] | None = None,
) -> dict[str, Any]:
    """Node ``cr_distance_to_default`` -- method card #347.

    Merton structural model: distance to default and implied default probability.

    Category 41-credit-risk-default; memory class ``light``.

    Args:
        equity_value: [series_handle, required] Market value of equity.
        equity_volatility: [series_handle, required] Equity volatility.
        debt: [series_handle, required] Face value of debt at the horizon.
        rate: [series_handle, required] Risk-free rate.
        horizon: [number, optional] Horizon in years. Default ``1.0``.
        barrier: [enum, optional] Default barrier definition. Default ``'short_plus_half_long'``.

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
        "cr_distance_to_default: not implemented."
    )


def cr_merton_pd(
    *,
    distance_to_default: pd.Series,
    mapping: Literal["normal", "empirical"] | None = None,
    empirical_map: pd.DataFrame | None = None,
) -> dict[str, Any]:
    """Node ``cr_merton_pd`` -- method card #347.

    Merton structural model: distance to default and implied default probability.

    Category 41-credit-risk-default; memory class ``light``.

    Args:
        distance_to_default: [series_handle, required] Distance to default.
        mapping: [enum, optional] Mapping to a probability. Default ``'normal'``.
        empirical_map: [df_handle, optional] Empirical default frequency table when mapping is
            empirical.

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
        "cr_merton_pd: not implemented."
    )
