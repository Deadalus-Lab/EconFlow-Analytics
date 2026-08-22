# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``bubble_tests`` -- method card #395.

#395 SADF and GSADF explosive-bubble tests with date stamping

Category 01-preparation-prechecks; module ``bubble_tests``.

Reference implementation: arch.

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
    "pp_bubble_dates",
    "pp_bubble_test",
    "NODE_META",
    "wire_model",
]


def pp_bubble_test(
    *,
    x: pd.Series,
    test: Literal["adf", "sadf", "gsadf"] | None = None,
    min_window: float | None = None,
    lags: int | None = None,
    n_simulations: int | None = None,
    seed: int,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``pp_bubble_test`` -- method card #395.

    SADF and GSADF explosive-bubble tests with date stamping.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [series_handle, required] Series, usually a price or price-to-fundamental ratio.
        test: [enum, optional] Test variant. Default ``'gsadf'``.
        min_window: [number, optional] Minimum window as a fraction of the sample.
        lags: [integer, optional] Lag order for the ADF regressions. Default ``0``.
        n_simulations: [integer, optional] Draws for the simulated critical values. Default
            ``1000``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.
        alpha: [number, optional] Significance level. Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "pp_bubble_test: not implemented."
    )


def pp_bubble_dates(
    *,
    x: pd.Series,
    min_duration: int | None = None,
    min_window: float | None = None,
    n_simulations: int | None = None,
    seed: int,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``pp_bubble_dates`` -- method card #395.

    SADF and GSADF explosive-bubble tests with date stamping.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [series_handle, required] Series.
        min_duration: [integer, optional] Minimum episode length in periods. Default ``5``.
        min_window: [number, optional] Minimum window as a fraction of the sample.
        n_simulations: [integer, optional] Draws for the simulated critical values. Default
            ``1000``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.
        alpha: [number, optional] Significance level. Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "pp_bubble_dates: not implemented."
    )
