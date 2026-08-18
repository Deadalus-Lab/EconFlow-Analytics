# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``seasonal_adjustment_13arima`` -- METHOD-SELECTION card #4.

#4 Seasonal adjustment with X-13ARIMA-SEATS

Category 01-preparation-prechecks; module ``seasonal_adjustment_13arima``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c01_preparation_prechecks import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "check_x13",
    "get_series",
    "run_seas",
    "NODE_META",
    "wire_model",
]


def run_seas(
    *,
    x: pd.Series,
    exog: np.ndarray | None = None,
    out: bool | None = None,
) -> dict[str, Any]:
    """Node ``run_seas`` -- METHOD-SELECTION card #4.

    Seasonal adjustment with X-13ARIMA-SEATS.

    Category 01-preparation-prechecks; memory class ``light``.

    Registers its result under ``seas_object``, so a later node can consume it as a handle.

    Args:
        x: [series_handle, required] Handle to a seasonal ts to be seasonally adjusted (X-13/SEATS).
        exog: [exog_handle, optional] Optional exogenous regressors (regARIMA).
        out: [boolean, optional] Store the full X-13 output (default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "run_seas: not implemented. The method card is in ./README.md."
    )


def get_series(
    *,
    seas_object: Any,
    series: str,
    reeval: bool | None = None,
    verbose: bool | None = None,
) -> dict[str, Any]:
    """Node ``get_series`` -- METHOD-SELECTION card #4.

    Seasonal adjustment with X-13ARIMA-SEATS.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        seas_object: [raw_handle, required] Handle to a 'seas' object (from run_seas).
        series: [string, required] Name of the X-13 table to extract (e.g. 'fct', 'seats.seasonal').
        reeval: [boolean, optional] Re-estimate if the table had not been requested (default True).
            Default ``True``.
        verbose: [boolean, optional] Message when a spec is added during re-estimation (default
            True). Default ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "get_series: not implemented. The method card is in ./README.md."
    )


def check_x13(
    *,
    fail: bool | None = None,
    fullcheck: bool | None = None,
    htmlcheck: bool | None = None,
) -> dict[str, Any]:
    """Node ``check_x13`` -- METHOD-SELECTION card #4.

    Seasonal adjustment with X-13ARIMA-SEATS.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        fail: [boolean, optional] If True an error aborts· otherwise a message is returned (default
            False). Default ``False``.
        fullcheck: [boolean, optional] Full check (runs Testairline.spc, default True). Default
            ``True``.
        htmlcheck: [boolean, optional] Check for the HTML version of X-13 (default True). Default
            ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "check_x13: not implemented. The method card is in ./README.md."
    )
