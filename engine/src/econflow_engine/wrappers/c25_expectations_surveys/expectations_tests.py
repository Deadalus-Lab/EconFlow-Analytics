# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``expectations_tests`` -- method card #576.

#576 Rational-expectations tests: Mincer-Zarnowitz and Coibion-Gorodnichenko

Category 25-expectations-surveys; module ``expectations_tests``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c25_expectations_surveys import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "es_expectations_tests",
    "NODE_META",
    "wire_model",
]


def es_expectations_tests(
    *,
    actual: pd.Series,
    forecast: pd.Series,
    revision: pd.Series | None = None,
    level: Literal["consensus", "individual"] | None = None,
    horizon: int | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``es_expectations_tests`` -- method card #576.

    Rational-expectations tests: Mincer-Zarnowitz and Coibion-Gorodnichenko.

    Category 25-expectations-surveys; memory class ``light``.

    Args:
        actual: [series_handle, required] Realised values.
        forecast: [series_handle, required] Survey forecast.
        revision: [series_handle, optional] Forecast revision for the rigidity test.
        level: [enum, optional] Analysis level. Default ``'consensus'``.
        horizon: [integer, optional] Forecast horizon, for the HAC lag. Default ``4``.
        alpha: [number, optional] Significance level. Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "es_expectations_tests: not implemented."
    )
