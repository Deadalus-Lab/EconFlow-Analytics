# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``non_parametric_trend`` -- method card #131.

#131 Non-parametric trend & change-point tests (Mann-Kendall / Theil-Sen slope / Pettitt / Seasonal
    MK)

Category 01-preparation-prechecks; module ``non_parametric_trend``.

Reference implementation: pymannkendall.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c01_preparation_prechecks import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "tr_mann_kendall",
    "tr_pettitt",
    "tr_seasonal_mann_kendall",
    "tr_theil_sen",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def tr_mann_kendall(
    *,
    x: pd.Series,
    alternative: Literal["two.sided", "greater", "less"] | None = None,
    continuity: bool | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``tr_mann_kendall`` -- method card #131.

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
        "tr_mann_kendall: not implemented."
    )


def tr_theil_sen(
    *,
    x: pd.Series,
    conf_level: float | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``tr_theil_sen`` -- method card #131.

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
        "tr_theil_sen: not implemented."
    )


def tr_pettitt(
    *,
    x: pd.Series,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``tr_pettitt`` -- method card #131.

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
        "tr_pettitt: not implemented."
    )


def tr_seasonal_mann_kendall(
    *,
    x: pd.Series,
    frequency: int | None = None,
    alternative: Literal["two.sided", "greater", "less"] | None = None,
    continuity: bool | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``tr_seasonal_mann_kendall`` -- method card #131.

    Non-parametric trend & change-point tests (Mann-Kendall / Theil-Sen slope / Pettitt / Seasonal
    MK).

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a seasonal ts with frequency>1 (or numeric +
            frequency)· no NA, non-constant.
        frequency: [integer, optional] Seasonal period >1· MANDATORY if x is not a series (e.g.
            12=monthly, 4=quarterly).
        alternative: [enum, optional] Alternative hypothesis (default two.sided).
        continuity: [boolean, optional] Continuity correction (default True). Default ``True``.
        alpha: [number, optional] Decision level (default 0.05). Default ``0.05``.

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
        "tr_seasonal_mann_kendall: not implemented."
    )
