# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``gravity_bilateral_trade`` -- METHOD-SELECTION card #237.

#237 Gravity models of bilateral trade (OLS / PPML / importer-exporter fixed effects / Bonus vetus
    OLS / Head-Mayer-Ries tetrads)

Category 28-trade-gravity; module ``gravity_bilateral_trade``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c28_trade_gravity import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "gr_bvu",
    "gr_fixed_effects",
    "gr_ols",
    "gr_ppml",
    "gr_tetrads",
    "NODE_META",
    "wire_model",
]


def gr_ppml(
    *,
    df: pd.DataFrame,
    dependent_variable: str,
    distance: str,
    additional_regressors: Sequence[str] | None = None,
    robust: bool | None = None,
) -> dict[str, Any]:
    """Node ``gr_ppml`` -- METHOD-SELECTION card #237.

    Gravity models of bilateral trade (OLS / PPML / importer-exporter fixed effects / Bonus vetus
    OLS / Head-Mayer-Ries tetrads).

    Category 28-trade-gravity; memory class ``light``.

    Args:
        df: [df_handle, required] Handle to a bilateral trade DataFrame {origin, destination, flow,
            distance, (incomes), (dummies)}· >= 3 rows (bilateral pairs). The data NEVER inline —
            only column names.
        dependent_variable: [string, required] Column name of the trade flow (dependent). Poisson
            PML => NON-NEGATIVE (>=0· accepts zeros).
        distance: [string, required] Distance column name (distance). Log-transformed automatically
            => STRICTLY POSITIVE (>0· non-positive => silent row-drop => gate).
        additional_regressors: [series_codes, optional] Array of names of ADDITIONAL dyadic
            regressors (e.g. rta, contig, comlang)· for PPML pass the incomes ALREADY
            log-transformed here. Optional.
        robust: [boolean, optional] robust=True => a robust linear fit robust SEs (without p-value)·
            False => lm/glm (default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "gr_ppml: not implemented. The method card is in ./README.md."
    )


def gr_ols(
    *,
    df: pd.DataFrame,
    dependent_variable: str,
    distance: str,
    income_origin: str,
    income_destination: str,
    code_origin: str,
    code_destination: str,
    additional_regressors: Sequence[str] | None = None,
    uie: bool | None = None,
    robust: bool | None = None,
) -> dict[str, Any]:
    """Node ``gr_ols`` -- METHOD-SELECTION card #237.

    Gravity models of bilateral trade (OLS / PPML / importer-exporter fixed effects / Bonus vetus
    OLS / Head-Mayer-Ries tetrads).

    Category 28-trade-gravity; memory class ``light``.

    Args:
        df: [df_handle, required] Handle to a bilateral trade DataFrame {origin, destination, flow,
            distance, (incomes), (dummies)}· >= 3 rows (bilateral pairs). The data NEVER inline —
            only column names.
        dependent_variable: [string, required] Column name of the trade flow (dependent).
            Log-transformed => STRICTLY POSITIVE (>0· zeros/negatives are dropped silently => gate).
        distance: [string, required] Distance column name (distance). Log-transformed automatically
            => STRICTLY POSITIVE (>0· non-positive => silent row-drop => gate).
        income_origin: [string, required] Origin income column name (exporter GDP)· log-transformed
            => >0.
        income_destination: [string, required] Destination income column name (importer GDP)·
            log-transformed => >0.
        code_origin: [string, required] Origin country code column name (exporter id, e.g. iso_o).
        code_destination: [string, required] Destination country code column name (importer id, e.g.
            iso_d).
        additional_regressors: [series_codes, optional] Array of names of ADDITIONAL dyadic
            regressors (e.g. rta, contig, comlang)· for PPML pass the incomes ALREADY
            log-transformed here. Optional.
        uie: [boolean, optional] uie=True => unitary income elasticities (dependent/(inc_o*inc_d)
            before the log)· False => incomes explicit regressors (default False). Default
            ``False``.
        robust: [boolean, optional] robust=True => a robust linear fit robust SEs (without p-value)·
            False => lm/glm (default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "gr_ols: not implemented. The method card is in ./README.md."
    )


def gr_fixed_effects(
    *,
    df: pd.DataFrame,
    dependent_variable: str,
    distance: str,
    code_origin: str,
    code_destination: str,
    additional_regressors: Sequence[str] | None = None,
    robust: bool | None = None,
) -> dict[str, Any]:
    """Node ``gr_fixed_effects`` -- METHOD-SELECTION card #237.

    Gravity models of bilateral trade (OLS / PPML / importer-exporter fixed effects / Bonus vetus
    OLS / Head-Mayer-Ries tetrads).

    Category 28-trade-gravity; memory class ``light``.

    Args:
        df: [df_handle, required] Handle to a bilateral trade DataFrame {origin, destination, flow,
            distance, (incomes), (dummies)}· >= 3 rows (bilateral pairs). The data NEVER inline —
            only column names.
        dependent_variable: [string, required] Column name of the trade flow (dependent).
            Log-transformed => STRICTLY POSITIVE (>0· zeros/negatives are dropped silently => gate).
        distance: [string, required] Distance column name (distance). Log-transformed automatically
            => STRICTLY POSITIVE (>0· non-positive => silent row-drop => gate).
        code_origin: [string, required] Origin country code column name (exporter id, e.g. iso_o).
        code_destination: [string, required] Destination country code column name (importer id, e.g.
            iso_d).
        additional_regressors: [series_codes, optional] Array of names of ADDITIONAL dyadic
            regressors (e.g. rta, contig, comlang)· for PPML pass the incomes ALREADY
            log-transformed here. Optional.
        robust: [boolean, optional] robust=True => a robust linear fit robust SEs (without p-value)·
            False => lm/glm (default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "gr_fixed_effects: not implemented. The method card is in ./README.md."
    )


def gr_bvu(
    *,
    df: pd.DataFrame,
    dependent_variable: str,
    distance: str,
    income_origin: str,
    income_destination: str,
    code_origin: str,
    code_destination: str,
    additional_regressors: Sequence[str] | None = None,
    robust: bool | None = None,
) -> dict[str, Any]:
    """Node ``gr_bvu`` -- METHOD-SELECTION card #237.

    Gravity models of bilateral trade (OLS / PPML / importer-exporter fixed effects / Bonus vetus
    OLS / Head-Mayer-Ries tetrads).

    Category 28-trade-gravity; memory class ``light``.

    Args:
        df: [df_handle, required] Handle to a bilateral trade DataFrame {origin, destination, flow,
            distance, (incomes), (dummies)}· >= 3 rows (bilateral pairs). The data NEVER inline —
            only column names.
        dependent_variable: [string, required] Column name of the trade flow (dependent).
            Log-transformed => STRICTLY POSITIVE (>0· zeros/negatives are dropped silently => gate).
        distance: [string, required] Distance column name (distance). Log-transformed automatically
            => STRICTLY POSITIVE (>0· non-positive => silent row-drop => gate).
        income_origin: [string, required] Origin income column name (exporter GDP)· log-transformed
            => >0.
        income_destination: [string, required] Destination income column name (importer GDP)·
            log-transformed => >0.
        code_origin: [string, required] Origin country code column name (exporter id, e.g. iso_o).
        code_destination: [string, required] Destination country code column name (importer id, e.g.
            iso_d).
        additional_regressors: [series_codes, optional] Array of names of ADDITIONAL dyadic
            regressors (e.g. rta, contig, comlang)· for PPML pass the incomes ALREADY
            log-transformed here. Optional.
        robust: [boolean, optional] robust=True => a robust linear fit robust SEs (without p-value)·
            False => lm/glm (default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "gr_bvu: not implemented. The method card is in ./README.md."
    )


def gr_tetrads(
    *,
    df: pd.DataFrame,
    dependent_variable: str,
    distance: str,
    code_origin: str,
    code_destination: str,
    filter_origin: str,
    filter_destination: str,
    additional_regressors: Sequence[str],
    multiway: bool | None = None,
) -> dict[str, Any]:
    """Node ``gr_tetrads`` -- METHOD-SELECTION card #237.

    Gravity models of bilateral trade (OLS / PPML / importer-exporter fixed effects / Bonus vetus
    OLS / Head-Mayer-Ries tetrads).

    Category 28-trade-gravity; memory class ``light``.

    Args:
        df: [df_handle, required] Handle to a bilateral trade DataFrame {origin, destination, flow,
            distance, (incomes), (dummies)}· >= 3 rows (bilateral pairs). The data NEVER inline —
            only column names.
        dependent_variable: [string, required] Column name of the trade flow (dependent).
            Log-transformed => STRICTLY POSITIVE (>0· zeros/negatives are dropped silently => gate).
        distance: [string, required] Distance column name (distance). Log-transformed automatically
            => STRICTLY POSITIVE (>0· non-positive => silent row-drop => gate).
        code_origin: [string, required] Origin country code column name (exporter id, e.g. iso_o).
        code_destination: [string, required] Destination country code column name (importer id, e.g.
            iso_d).
        filter_origin: [string, required] Reference exporter code (must EXIST in the column
            code_origin)· eliminates monadic exporter effects.
        filter_destination: [string, required] Reference importer code (must EXIST in the column
            code_destination)· eliminates monadic importer effects.
        additional_regressors: [series_codes, required] Array of names of ADDITIONAL dyadic
            regressors (e.g. rta, contig, comlang)· for PPML pass the incomes ALREADY
            log-transformed here. REQUIRED for tetrads (>=1).
        multiway: [boolean, optional] multiway=True => multi-way clustered SEs
            (Cameron-Gelbach-Miller 2011· returns a coeftest matrix)· False => plain lm (default
            False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "gr_tetrads: not implemented. The method card is in ./README.md."
    )
