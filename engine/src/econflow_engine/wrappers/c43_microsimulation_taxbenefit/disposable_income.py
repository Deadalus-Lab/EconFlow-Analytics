# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``disposable_income`` -- method card #362.

#362 Disposable income, net-of-tax income and budget constraints

Category 43-microsimulation-taxbenefit; module ``disposable_income``.

Reference implementation: OpenFisca-Core.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

import pandas as pd

from econflow_engine.generated.args.c43_microsimulation_taxbenefit import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "tb_budget_constraint",
    "tb_disposable_income",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def tb_disposable_income(
    *,
    population: pd.DataFrame,
    period: str,
    include_housing: bool | None = None,
) -> dict[str, Any]:
    """Node ``tb_disposable_income`` -- method card #362.

    Disposable income, net-of-tax income and budget constraints.

    Category 43-microsimulation-taxbenefit; memory class ``light``.

    Args:
        population: [df_handle, required] Household microdata.
        period: [string, required] Period the calculation refers to.
        include_housing: [boolean, optional] Net off housing costs. Default ``False``.

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
        "tb_disposable_income: not implemented."
    )


def tb_budget_constraint(
    *,
    household: pd.DataFrame,
    earnings_grid: Sequence[float],
    period: str,
) -> dict[str, Any]:
    """Node ``tb_budget_constraint`` -- method card #362.

    Disposable income, net-of-tax income and budget constraints.

    Category 43-microsimulation-taxbenefit; memory class ``light``.

    Args:
        household: [df_handle, required] A single household specification.
        earnings_grid: [num_array, required] Earnings values to evaluate.
        period: [string, required] Period the calculation refers to.

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
        "tb_budget_constraint: not implemented."
    )
