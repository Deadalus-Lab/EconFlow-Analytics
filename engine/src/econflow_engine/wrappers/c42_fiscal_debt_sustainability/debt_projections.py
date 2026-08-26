# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``debt_projections`` -- method card #355.

#355 Deterministic debt projections and standardised stress scenarios

Category 42-fiscal-debt-sustainability; module ``debt_projections``.

Reference implementation: pandas.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from econflow_engine.generated.args.c42_fiscal_debt_sustainability import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "fis_debt_stabilising_balance",
    "fis_project_debt",
    "fis_stress_scenarios",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def fis_project_debt(
    *,
    debt_ratio_initial: float,
    primary_balance: Sequence[float],
    interest_rate: Sequence[float],
    growth_rate: Sequence[float],
    horizon: int | None = None,
) -> dict[str, Any]:
    """Node ``fis_project_debt`` -- method card #355.

    Deterministic debt projections and standardised stress scenarios.

    Category 42-fiscal-debt-sustainability; memory class ``light``.

    Args:
        debt_ratio_initial: [number, required] Starting debt ratio.
        primary_balance: [num_array, required] Assumed primary balance path.
        interest_rate: [num_array, required] Assumed effective interest rate path.
        growth_rate: [num_array, required] Assumed nominal growth path.
        horizon: [integer, optional] Projection horizon in periods. Default ``10``.

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
        "fis_project_debt: not implemented."
    )


def fis_stress_scenarios(
    *,
    baseline: Any,
    shock_size: float | None = None,
    scenarios: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Node ``fis_stress_scenarios`` -- method card #355.

    Deterministic debt projections and standardised stress scenarios.

    Category 42-fiscal-debt-sustainability; memory class ``light``.

    Args:
        baseline: [raw_handle, required] Handle to a baseline projection.
        shock_size: [number, optional] Shock in historical standard deviations. Default ``1.0``.
        scenarios: [series_codes, optional] Scenarios to run; omitted = the standard set.

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
        "fis_stress_scenarios: not implemented."
    )


def fis_debt_stabilising_balance(
    *,
    debt_ratio: float,
    interest_rate: float,
    growth_rate: float,
) -> dict[str, Any]:
    """Node ``fis_debt_stabilising_balance`` -- method card #355.

    Deterministic debt projections and standardised stress scenarios.

    Category 42-fiscal-debt-sustainability; memory class ``light``.

    Args:
        debt_ratio: [number, required] Current debt ratio.
        interest_rate: [number, required] Effective interest rate.
        growth_rate: [number, required] Nominal growth rate.

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
        "fis_debt_stabilising_balance: not implemented."
    )
