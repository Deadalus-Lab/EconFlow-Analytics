# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``stock_flow_consistent`` -- METHOD-SELECTION card #203.

#203 Stock-Flow-Consistent (Godley-Lavoie) macro simulation — a baseline steady-state solve, policy
    scenarios (shocks), balance-sheet/transactions-flow accounting validation

Category 13-dsge-general-equilibrium; module ``stock_flow_consistent``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

from econflow_engine.generated.args.c13_dsge_general_equilibrium import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "sfcr_balance_check",
    "sfcr_scenario_run",
    "sfcr_simulate",
    "NODE_META",
    "wire_model",
]


def sfcr_simulate(
    *,
    equations: Sequence[str],
    external: Sequence[str],
    periods: int,
    initial: Sequence[str] | None = None,
    hidden: Any | None = None,
    method: Literal["Broyden", "Gauss", "Newton"] | None = None,
    max_iter: int | None = None,
    tol: float | None = None,
    rhtol: bool | None = None,
    hidden_tol: float | None = None,
) -> dict[str, Any]:
    """Node ``sfcr_simulate`` -- METHOD-SELECTION card #203.

    Stock-Flow-Consistent (Godley-Lavoie) macro simulation — a baseline steady-state solve, policy
    scenarios (shocks), balance-sheet/transactions-flow accounting validation.

    Category 13-dsge-general-equilibrium; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        equations: [series_codes, required] Model equations as a list of strings in Wilkinson
            formula syntax ('Y ~ Cs + Gs'· lag=x[-1]· difference=d(x)).
        external: [series_codes, required] Exogenous variables/parameters as formula-strings ('Gd ~
            20').
        periods: [integer, required] Number of simulation periods (>=2· steady-state needs ~50+).
        initial: [series_codes, optional] Optional initial values as formula-strings.
        hidden: [raw, optional] Named 1-pair mapping of the hidden/redundant identity (e.g.
            {'Hh':'Hs'})· if given, accounting consistency is checked.
        method: [enum, optional] Solution algorithm (default Broyden· Gauss=Gauss-Seidel·
            Newton=Newton-Raphson).
        max_iter: [integer, optional] Maximum iterations per period (default 350). Default ``350``.
        tol: [number, optional] Convergence tolerance (default 1e-8). Default ``1e-08``.
        rhtol: [boolean, optional] Relative-hidden tolerance for growth models (default
            False=absolute). Default ``False``.
        hidden_tol: [number, optional] Tolerance of the hidden-equation check (default 0.1). Default
            ``0.1``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "sfcr_simulate: not implemented. The method card is in ./README.md."
    )


def sfcr_scenario_run(
    *,
    baseline: Any,
    shock_variables: Sequence[str],
    shock_start: int,
    shock_end: int,
    periods: int,
    method: Literal["Broyden", "Gauss", "Newton"] | None = None,
    max_iter: int | None = None,
    tol: float | None = None,
) -> dict[str, Any]:
    """Node ``sfcr_scenario_run`` -- METHOD-SELECTION card #203.

    Stock-Flow-Consistent (Godley-Lavoie) macro simulation — a baseline steady-state solve, policy
    scenarios (shocks), balance-sheet/transactions-flow accounting validation.

    Category 13-dsge-general-equilibrium; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        baseline: [raw_handle, required] Handle to a baseline sfcr_tbl (sfcr_simulate$object)· the
            scenario REQUIRES a baseline.
        shock_variables: [series_codes, required] Shock variables as formula-strings ('Gd ~ 30'· or
            a series of length end-start).
        shock_start: [integer, required] Shock start period (>=1).
        shock_end: [integer, required] Shock end period (shock_start<=shock_end<=periods).
        periods: [integer, required] Total scenario periods (>=2).
        method: [enum, optional] Solution algorithm (default Broyden).
        max_iter: [integer, optional] Maximum iterations per period (default 350). Default ``350``.
        tol: [number, optional] Scenario convergence tolerance (default 1e-10). Default ``1e-10``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "sfcr_scenario_run: not implemented. The method card is in ./README.md."
    )


def sfcr_balance_check(
    *,
    baseline: Any,
    matrix_type: Literal["tfm", "bs"] | None = None,
    columns: Sequence[str],
    codes: Sequence[str],
    rows: Any,
    tol: float | None = None,
    rtol: bool | None = None,
) -> dict[str, Any]:
    """Node ``sfcr_balance_check`` -- METHOD-SELECTION card #203.

    Stock-Flow-Consistent (Godley-Lavoie) macro simulation — a baseline steady-state solve, policy
    scenarios (shocks), balance-sheet/transactions-flow accounting validation.

    Category 13-dsge-general-equilibrium; memory class ``light``.

    Args:
        baseline: [raw_handle, required] Handle to a solved sfcr_tbl (baseline OR scenario $object).
        matrix_type: [enum, optional] tfm=transactions-flow· bs=balance-sheet (default tfm).
        columns: [series_codes, required] Sector column names of the matrix.
        codes: [series_codes, required] Column abbreviations (same length & order as columns·
            unique).
        rows: [raw, required] List of rows· each row {name, <code>:formula-string,...} (e.g.
            {'name':'Consumption','h':'-Cd','f':'+Cs'}).
        tol: [number, optional] Absolute validation tolerance (default 1). Default ``1``.
        rtol: [boolean, optional] Relative discrepancy for growth models (default False). Default
            ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "sfcr_balance_check: not implemented. The method card is in ./README.md."
    )
