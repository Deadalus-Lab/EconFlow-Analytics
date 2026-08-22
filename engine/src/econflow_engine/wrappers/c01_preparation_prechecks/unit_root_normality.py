# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``unit_root_normality`` -- method card #1.

#1 Unit-root & normality prechecks (ADF/KPSS/PP/Jarque-Bera)

Category 01-preparation-prechecks; module ``unit_root_normality``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c01_preparation_prechecks import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "run_adf_test",
    "run_jarque_bera_test",
    "run_kpss_test",
    "run_pp_test",
    "NODE_META",
    "wire_model",
]


def run_adf_test(
    *,
    x: pd.Series,
    alternative: Literal["stationary", "explosive"] | None = None,
    k: int | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``run_adf_test`` -- method card #1.

    Unit-root & normality prechecks (ADF/KPSS/PP/Jarque-Bera).

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a univariate ts/series to test (no NA).
        alternative: [enum, optional] Alternative hypothesis (default stationary).
        k: [integer, optional] Lag order· default trunc((n-1)^(1/3)).
        alpha: [number, optional] Decision significance level (default 0.05). Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "run_adf_test: not implemented."
    )


def run_kpss_test(
    *,
    x: pd.Series,
    null: Literal["Level", "Trend"] | None = None,
    lshort: bool | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``run_kpss_test`` -- method card #1.

    Unit-root & normality prechecks (ADF/KPSS/PP/Jarque-Bera).

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a univariate ts/series (no NA).
        null: [enum, optional] H0 stationarity around Level or Trend (default Level).
        lshort: [boolean, optional] Short truncation lag (True) or long (False). Default ``True``.
        alpha: [number, optional] Significance level (default 0.05). Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "run_kpss_test: not implemented."
    )


def run_pp_test(
    *,
    x: pd.Series,
    alternative: Literal["stationary", "explosive"] | None = None,
    type: Literal["Z(alpha)", "Z(t_alpha)"] | None = None,
    lshort: bool | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``run_pp_test`` -- method card #1.

    Unit-root & normality prechecks (ADF/KPSS/PP/Jarque-Bera).

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a univariate ts/series (no NA).
        alternative: [enum, optional] Alternative hypothesis (default stationary).
        type: [enum, optional] PP statistic (default Z(alpha)).
        lshort: [boolean, optional] Short truncation lag (True) or long (False). Default ``True``.
        alpha: [number, optional] Significance level (default 0.05). Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "run_pp_test: not implemented."
    )


def run_jarque_bera_test(
    *,
    x: pd.Series,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``run_jarque_bera_test`` -- method card #1.

    Unit-root & normality prechecks (ADF/KPSS/PP/Jarque-Bera).

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a univariate ts/series for a normality test.
        alpha: [number, optional] Significance level (default 0.05). Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "run_jarque_bera_test: not implemented."
    )
