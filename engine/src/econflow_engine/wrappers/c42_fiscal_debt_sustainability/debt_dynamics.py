# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``debt_dynamics`` -- method card #354.

#354 Debt-dynamics accounting: the r-g snowball, primary balance and stock-flow adjustment

Category 42-fiscal-debt-sustainability; module ``debt_dynamics``.

Reference implementation: pandas.

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
    "fis_debt_decomposition",
    "fis_snowball",
    "NODE_META",
    "wire_model",
]


def fis_debt_decomposition(
    *,
    debt_ratio: pd.Series,
    primary_balance: pd.Series,
    interest_rate: pd.Series,
    growth_rate: pd.Series,
    inflation: pd.Series | None = None,
) -> dict[str, Any]:
    """Node ``fis_debt_decomposition`` -- method card #354.

    Debt-dynamics accounting: the r-g snowball, primary balance and stock-flow adjustment.

    Category 42-fiscal-debt-sustainability; memory class ``light``.

    Args:
        debt_ratio: [series_handle, required] Debt as a share of output.
        primary_balance: [series_handle, required] Primary balance as a share of output.
        interest_rate: [series_handle, required] Effective nominal interest rate.
        growth_rate: [series_handle, required] Nominal output growth rate.
        inflation: [series_handle, optional] Deflator growth, when a real decomposition is wanted.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fis_debt_decomposition: not implemented."
    )


def fis_snowball(
    *,
    debt_ratio: pd.Series,
    interest_rate: pd.Series,
    growth_rate: pd.Series,
) -> dict[str, Any]:
    """Node ``fis_snowball`` -- method card #354.

    Debt-dynamics accounting: the r-g snowball, primary balance and stock-flow adjustment.

    Category 42-fiscal-debt-sustainability; memory class ``light``.

    Args:
        debt_ratio: [series_handle, required] Debt as a share of output.
        interest_rate: [series_handle, required] Effective nominal interest rate.
        growth_rate: [series_handle, required] Nominal output growth rate.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fis_snowball: not implemented."
    )
