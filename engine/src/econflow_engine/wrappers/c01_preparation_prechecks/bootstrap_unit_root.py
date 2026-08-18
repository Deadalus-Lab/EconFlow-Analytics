# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``bootstrap_unit_root`` -- METHOD-SELECTION card #122.

#122 Bootstrap unit-root tests robust to heterogeneity/non-stationary volatility/missing data (boot
    ADF / union / panel GM / order of integration)

Category 01-preparation-prechecks; module ``bootstrap_unit_root``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c01_preparation_prechecks import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "bur_boot_adf",
    "bur_boot_panel",
    "bur_boot_union",
    "bur_order_integration",
    "NODE_META",
    "wire_model",
]


def bur_boot_adf(
    *,
    data: pd.Series,
    seed: int,
    bootstrap: Literal["AWB", "MBB", "BWB", "DWB", "SB", "SWB"] | None = None,
    B: int | None = None,
    deterministics: Literal["intercept", "none", "trend"] | None = None,
    detrend: Literal["OLS", "QD"] | None = None,
    min_lag: int | None = None,
    max_lag: int | None = None,
    criterion: Literal["MAIC", "AIC", "BIC", "MBIC"] | None = None,
    criterion_scale: bool | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``bur_boot_adf`` -- METHOD-SELECTION card #122.

    Bootstrap unit-root tests robust to heterogeneity/non-stationary volatility/missing data (boot
    ADF / union / panel GM / order of integration).

    Category 01-preparation-prechecks; memory class ``heavy``.

    Args:
        data: [series_handle, required] Handle to a univariate ts/series (no NA, >=20 obs).
        seed: [integer, required] Bootstrap seed (MANDATORY — determinism/caching).
        bootstrap: [enum, optional] Bootstrap method (default AWB).
        B: [integer, optional] Bootstrap replications (>=99, default 1999). Default ``1999``.
        deterministics: [enum, optional] ADF deterministic terms (default intercept).
        detrend: [enum, optional] Detrending: OLS (ADF) or QD/GLS (DF-GLS) (default OLS).
        min_lag: [integer, optional] Minimum ADF lag (default 0). Default ``0``.
        max_lag: [integer, optional] Maximum ADF lag (default data-driven 12(T/100)^0.25).
        criterion: [enum, optional] Lag selection criterion (default MAIC).
        criterion_scale: [boolean, optional] Rescaled IC (Cavaliere et al. 2015) (default True).
            Default ``True``.
        alpha: [number, optional] Decision level· H0=unit root, p<alpha ⇒ STATIONARY (default 0.05).
            Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bur_boot_adf: not implemented. The method card is in ./README.md."
    )


def bur_boot_union(
    *,
    data: pd.Series,
    seed: int,
    bootstrap: Literal["AWB", "MBB", "BWB", "DWB", "SB", "SWB"] | None = None,
    B: int | None = None,
    min_lag: int | None = None,
    max_lag: int | None = None,
    criterion: Literal["MAIC", "AIC", "BIC", "MBIC"] | None = None,
    criterion_scale: bool | None = None,
    union_quantile: float | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``bur_boot_union`` -- METHOD-SELECTION card #122.

    Bootstrap unit-root tests robust to heterogeneity/non-stationary volatility/missing data (boot
    ADF / union / panel GM / order of integration).

    Category 01-preparation-prechecks; memory class ``heavy``.

    Args:
        data: [series_handle, required] Handle to a univariate ts/series (no NA, >=20 obs).
        seed: [integer, required] Bootstrap seed (MANDATORY — determinism/caching).
        bootstrap: [enum, optional] Bootstrap method (default AWB).
        B: [integer, optional] Bootstrap replications (>=99, default 1999). Default ``1999``.
        min_lag: [integer, optional] Minimum ADF lag (default 0). Default ``0``.
        max_lag: [integer, optional] Maximum ADF lag (default data-driven).
        criterion: [enum, optional] Lag selection criterion (default MAIC).
        criterion_scale: [boolean, optional] Rescaled IC (default True). Default ``True``.
        union_quantile: [number, optional] Quantile scaling of the individual statistics (= the
            level, default 0.05). Default ``0.05``.
        alpha: [number, optional] Decision level· p<alpha ⇒ STATIONARY (default 0.05). Default
            ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bur_boot_union: not implemented. The method card is in ./README.md."
    )


def bur_boot_panel(
    *,
    data: pd.DataFrame,
    seed: int,
    bootstrap: Literal["AWB", "MBB", "BWB", "DWB", "SB", "SWB"] | None = None,
    B: int | None = None,
    union: bool | None = None,
    union_quantile: float | None = None,
    deterministics: Literal["intercept", "none", "trend"] | None = None,
    detrend: Literal["OLS", "QD"] | None = None,
    min_lag: int | None = None,
    max_lag: int | None = None,
    criterion: Literal["MAIC", "AIC", "BIC", "MBIC"] | None = None,
    criterion_scale: bool | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``bur_boot_panel`` -- METHOD-SELECTION card #122.

    Bootstrap unit-root tests robust to heterogeneity/non-stationary volatility/missing data (boot
    ADF / union / panel GM / order of integration).

    Category 01-preparation-prechecks; memory class ``heavy``.

    Args:
        data: [multiseries_handle, required] Handle to a (T x N) matrix/mts of >=2 series (no NA,
            >=20 obs).
        seed: [integer, required] Bootstrap seed (MANDATORY — determinism/caching).
        bootstrap: [enum, optional] Bootstrap method (default AWB).
        B: [integer, optional] Bootstrap replications (>=99, default 1999). Default ``1999``.
        union: [boolean, optional] Use the union test per series (default True). Default ``True``.
        union_quantile: [number, optional] Quantile scaling union (default 0.05). Default ``0.05``.
        deterministics: [enum, optional] Deterministic terms· ONLY if union=False (default
            intercept).
        detrend: [enum, optional] Detrending· ONLY if union=False (default OLS).
        min_lag: [integer, optional] Minimum ADF lag (default 0). Default ``0``.
        max_lag: [integer, optional] Maximum ADF lag (default data-driven).
        criterion: [enum, optional] Lag selection criterion (default MAIC).
        criterion_scale: [boolean, optional] Rescaled IC (default True). Default ``True``.
        alpha: [number, optional] Decision level· H0=ALL series have a unit root, p<alpha ⇒ SOME are
            stationary (default 0.05). Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bur_boot_panel: not implemented. The method card is in ./README.md."
    )


def bur_order_integration(
    *,
    data: pd.DataFrame,
    seed: int,
    method: Literal["boot_ur", "boot_sqt", "boot_fdr"] | None = None,
    max_order: int | None = None,
    level: float | None = None,
    bootstrap: Literal["AWB", "MBB", "BWB", "DWB", "SB", "SWB"] | None = None,
    B: int | None = None,
    min_lag: int | None = None,
    max_lag: int | None = None,
    criterion: Literal["MAIC", "AIC", "BIC", "MBIC"] | None = None,
) -> dict[str, Any]:
    """Node ``bur_order_integration`` -- METHOD-SELECTION card #122.

    Bootstrap unit-root tests robust to heterogeneity/non-stationary volatility/missing data (boot
    ADF / union / panel GM / order of integration).

    Category 01-preparation-prechecks; memory class ``heavy``.

    Registers its result under ``diff_data``, so a later node can consume it as a handle.

    Args:
        data: [multiseries_handle, required] Handle to a (T x N) matrix/mts of >=2 series (no NA,
            >=20 obs).
        seed: [integer, required] Bootstrap seed (MANDATORY — determinism/caching).
        method: [enum, optional] Multivariate test per step (default boot_ur).
        max_order: [integer, optional] Maximum order of integration (default 2). Default ``2``.
        level: [number, optional] Significance level of the unit-root tests (default 0.05). Default
            ``0.05``.
        bootstrap: [enum, optional] Bootstrap method (default AWB).
        B: [integer, optional] Bootstrap replications (>=99, default 1999). Default ``1999``.
        min_lag: [integer, optional] Minimum ADF lag (default 0). Default ``0``.
        max_lag: [integer, optional] Maximum ADF lag (default data-driven).
        criterion: [enum, optional] Lag selection criterion (default MAIC).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bur_order_integration: not implemented. The method card is in ./README.md."
    )
