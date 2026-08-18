# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``non_parametric_trend`` -- METHOD-SELECTION card #131.

#131 Non-parametric trend & change-point tests (Mann-Kendall / Theil-Sen slope / Pettitt / Seasonal
    MK)

Category 01-preparation-prechecks; module ``non_parametric_trend``.

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
    "tr_mk",
    "tr_pettitt",
    "tr_sens",
    "tr_smk",
    "NODE_META",
    "wire_model",
]


def tr_mk(
    *,
    x: pd.Series,
    alternative: Literal["two.sided", "greater", "less"] | None = None,
    continuity: bool | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``tr_mk`` -- METHOD-SELECTION card #131.

    Non-parametric trend & change-point tests (Mann-Kendall / Theil-Sen slope / Pettitt / Seasonal
    MK).

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a univariate ts/numeric series (no NA, >=3 obs,
            non-constant).
        alternative: [enum, optional] Alternative hypothesis (default two.sided).
        continuity: [boolean, optional] Continuity correction of the normal approximation (default
            True). Default ``True``.
        alpha: [number, optional] Decision level· H0=no trend, p<alpha ⇒ monotonic trend (default
            0.05). Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "tr_mk: not implemented. The method card is in ./README.md."
    )


def tr_sens(
    *,
    x: pd.Series,
    conf_level: float | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``tr_sens`` -- METHOD-SELECTION card #131.

    Non-parametric trend & change-point tests (Mann-Kendall / Theil-Sen slope / Pettitt / Seasonal
    MK).

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a univariate ts/numeric series (no NA, >=3 obs,
            non-constant).
        conf_level: [number, optional] Confidence level of the slope CI, ∈(0,1) (default 0.95).
            Default ``0.95``.
        alpha: [number, optional] Decision level on the Mann-Kendall p-value (default 0.05). Default
            ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "tr_sens: not implemented. The method card is in ./README.md."
    )


def tr_pettitt(
    *,
    x: pd.Series,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``tr_pettitt`` -- METHOD-SELECTION card #131.

    Non-parametric trend & change-point tests (Mann-Kendall / Theil-Sen slope / Pettitt / Seasonal
    MK).

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a univariate ts/numeric series (no NA, >=3 obs,
            non-constant).
        alpha: [number, optional] Decision level· H0=no change in central tendency (default 0.05).
            Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "tr_pettitt: not implemented. The method card is in ./README.md."
    )


def tr_smk(
    *,
    x: pd.Series,
    frequency: int | None = None,
    alternative: Literal["two.sided", "greater", "less"] | None = None,
    continuity: bool | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``tr_smk`` -- METHOD-SELECTION card #131.

    Non-parametric trend & change-point tests (Mann-Kendall / Theil-Sen slope / Pettitt / Seasonal
    MK).

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a seasonal ts with frequency>1 (or numeric +
            frequency)· no NA, non-constant.
        frequency: [integer, optional] Seasonal period >1· MANDATORY if x is not a ts (e.g.
            12=monthly, 4=quarterly).
        alternative: [enum, optional] Alternative hypothesis (default two.sided).
        continuity: [boolean, optional] Continuity correction (default True). Default ``True``.
        alpha: [number, optional] Decision level (default 0.05). Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "tr_smk: not implemented. The method card is in ./README.md."
    )
