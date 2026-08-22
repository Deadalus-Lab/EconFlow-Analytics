# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``complex_survey_aware`` -- method card #226.

#226 Complex-survey-aware inequality & poverty with design-based linearized SE (Gini/QSR/Zenga +
    FGT/ARPR)

Category 22-inequality; module ``complex_survey_aware``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c22_inequality import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "svy_inequality",
    "svy_poverty",
    "NODE_META",
    "wire_model",
]


def svy_inequality(
    *,
    data: pd.DataFrame,
    income: str,
    ids: str,
    weights: str,
    strata: str | None = None,
    fpc: str | None = None,
    nest: bool | None = None,
    subset_var: str | None = None,
    subset_level: str | None = None,
    na_rm: bool | None = None,
    level: float | None = None,
    measure: Literal["gini", "qsr", "zenga"] | None = None,
    alpha1: float | None = None,
    alpha2: float | None = None,
) -> dict[str, Any]:
    """Node ``svy_inequality`` -- method card #226.

    Complex-survey-aware inequality & poverty with design-based linearized SE (Gini/QSR/Zenga +
    FGT/ARPR).

    Category 22-inequality; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a MICRODATA DataFrame; contains the
            income/weights/design columns. the survey design is built internally.
        income: [string, required] Income column name (numeric, non-negative).
        ids: [string, required] PSU/cluster ID column name; give "1" for no clustering (ids=~1).
        weights: [string, required] Sampling weights column name (positive, > 0).
        strata: [string, optional] Strata column name (optional).
        fpc: [string, optional] Finite population correction column name (optional).
        nest: [boolean, optional] PSU IDs nested within strata (default False).
        subset_var: [string, optional] Column name for domain estimation (optional).
        subset_level: [string, optional] Value of subset_var that defines the domain.
        na_rm: [boolean, optional] Removal of income NA (default False; NA + False => hard gate).
        level: [number, optional] CI confidence level in (0,1) (default 0.95).
        measure: [enum, optional] Inequality index (default gini).
        alpha1: [number, optional] QSR: lower quantile in (0,1) (default 0.2 => S80/S20).
        alpha2: [number, optional] QSR: upper quantile in (0,1) (default 1-alpha1); alpha1<alpha2.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "svy_inequality: not implemented."
    )


def svy_poverty(
    *,
    data: pd.DataFrame,
    income: str,
    ids: str,
    weights: str,
    strata: str | None = None,
    fpc: str | None = None,
    nest: bool | None = None,
    subset_var: str | None = None,
    subset_level: str | None = None,
    na_rm: bool | None = None,
    level: float | None = None,
    measure: Literal["fgt", "arpr"] | None = None,
    g: float | None = None,
    type_thresh: Literal["abs", "relq", "relm"] | None = None,
    abs_thresh: float | None = None,
    percent: float | None = None,
    quantiles: float | None = None,
) -> dict[str, Any]:
    """Node ``svy_poverty`` -- method card #226.

    Complex-survey-aware inequality & poverty with design-based linearized SE (Gini/QSR/Zenga +
    FGT/ARPR).

    Category 22-inequality; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a MICRODATA DataFrame; contains the
            income/weights/design columns. the survey design is built internally.
        income: [string, required] Income column name (numeric, non-negative).
        ids: [string, required] PSU/cluster ID column name; give "1" for no clustering (ids=~1).
        weights: [string, required] Sampling weights column name (positive, > 0).
        strata: [string, optional] Strata column name (optional).
        fpc: [string, optional] Finite population correction column name (optional).
        nest: [boolean, optional] PSU IDs nested within strata (default False).
        subset_var: [string, optional] Column name for domain estimation (optional).
        subset_level: [string, optional] Value of subset_var that defines the domain.
        na_rm: [boolean, optional] Removal of income NA (default False; NA + False => hard gate).
        level: [number, optional] CI confidence level in (0,1) (default 0.95).
        measure: [enum, optional] Poverty index (default fgt).
        g: [number, optional] FGT: integer >=0 (0 headcount, 1 gap, 2 severity; default 0).
        type_thresh: [enum, optional] FGT threshold: abs (absolute) | relq (relative-to-quantile) |
            relm (relative-to-mean). Default abs.
        abs_thresh: [number, optional] FGT: absolute poverty line (>0); ONLY when type_thresh='abs'.
        percent: [number, optional] Percentage of the threshold for relative/ARPR (default 0.6).
        quantiles: [number, optional] Base threshold quantile (default 0.5 = median).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "svy_poverty: not implemented."
    )
