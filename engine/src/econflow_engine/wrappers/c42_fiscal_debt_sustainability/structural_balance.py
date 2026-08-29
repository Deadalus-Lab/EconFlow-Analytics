# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``structural_balance`` -- method card #359.

#359 Structural and cyclically-adjusted balances with output-gap elasticities

Category 42-fiscal-debt-sustainability; module ``structural_balance``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any

import pandas as pd

from econflow_engine.generated.args.c42_fiscal_debt_sustainability import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "fis_budget_elasticity",
    "fis_cyclically_adjusted",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def fis_cyclically_adjusted(
    *,
    balance: pd.Series,
    output_gap: pd.Series,
    elasticity: float | None = None,
    one_offs: pd.Series | None = None,
) -> dict[str, Any]:
    """Node ``fis_cyclically_adjusted`` -- method card #359.

    Structural and cyclically-adjusted balances with output-gap elasticities.

    Category 42-fiscal-debt-sustainability; memory class ``light``.

    Args:
        balance: [series_handle, required] Headline balance as a share of output.
        output_gap: [series_handle, required] Output gap as a share of potential.
        elasticity: [number, optional] Budget semi-elasticity to the gap. Default ``0.5``.
        one_offs: [series_handle, optional] One-off measures to remove for the structural balance.

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
        "fis_cyclically_adjusted: not implemented."
    )


def fis_budget_elasticity(
    *,
    revenue: pd.Series,
    expenditure: pd.Series,
    output_gap: pd.Series,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``fis_budget_elasticity`` -- method card #359.

    Structural and cyclically-adjusted balances with output-gap elasticities.

    Category 42-fiscal-debt-sustainability; memory class ``light``.

    Args:
        revenue: [series_handle, required] Revenue as a share of output.
        expenditure: [series_handle, required] Expenditure as a share of output.
        output_gap: [series_handle, required] Output gap.
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
        "fis_budget_elasticity: not implemented."
    )
