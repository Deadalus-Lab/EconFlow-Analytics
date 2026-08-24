# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``fiscal_rules`` -- method card #360.

#360 Fiscal-rule compliance simulation and adjustment paths

Category 42-fiscal-debt-sustainability; module ``fiscal_rules``.

Reference implementation: scipy.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c42_fiscal_debt_sustainability import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "fis_adjustment_path",
    "fis_rule_compliance",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def fis_rule_compliance(
    *,
    debt_ratio: pd.Series,
    structural_balance: pd.Series | None = None,
    expenditure_growth: pd.Series | None = None,
    debt_limit: float | None = None,
    deficit_limit: float | None = None,
    mto: float | None = None,
) -> dict[str, Any]:
    """Node ``fis_rule_compliance`` -- method card #360.

    Fiscal-rule compliance simulation and adjustment paths.

    Category 42-fiscal-debt-sustainability; memory class ``light``.

    Args:
        debt_ratio: [series_handle, required] Projected debt ratio.
        structural_balance: [series_handle, optional] Projected structural balance.
        expenditure_growth: [series_handle, optional] Projected expenditure growth.
        debt_limit: [number, optional] Debt ratio limit. Default ``0.6``.
        deficit_limit: [number, optional] Headline deficit limit. Default ``0.03``.
        mto: [number, optional] Medium-term structural balance objective.

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
        "fis_rule_compliance: not implemented."
    )


def fis_adjustment_path(
    *,
    debt_ratio_initial: float,
    target: float,
    horizon: int | None = None,
    interest_rate: float,
    growth_rate: float,
    multiplier: float | None = None,
) -> dict[str, Any]:
    """Node ``fis_adjustment_path`` -- method card #360.

    Fiscal-rule compliance simulation and adjustment paths.

    Category 42-fiscal-debt-sustainability; memory class ``light``.

    Args:
        debt_ratio_initial: [number, required] Starting debt ratio.
        target: [number, required] Target debt ratio.
        horizon: [integer, optional] Years to reach the target. Default ``10``.
        interest_rate: [number, required] Effective interest rate.
        growth_rate: [number, required] Nominal growth rate.
        multiplier: [number, optional] Fiscal multiplier applied to the consolidation. Default
            ``0.0``.

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
        "fis_adjustment_path: not implemented."
    )
