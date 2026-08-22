# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``weather_normalisation`` -- method card #371.

#371 Weather normalisation of energy demand with heating and cooling degree days

Category 44-environment-energy-climate; module ``weather_normalisation``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c44_environment_energy_climate import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "env_degree_days",
    "env_weather_normalise",
    "NODE_META",
    "wire_model",
]


def env_degree_days(
    *,
    temperature: pd.Series,
    base_heating: float | None = None,
    base_cooling: float | None = None,
    frequency: Literal["daily", "weekly", "monthly", "annual"] | None = None,
) -> dict[str, Any]:
    """Node ``env_degree_days`` -- method card #371.

    Weather normalisation of energy demand with heating and cooling degree days.

    Category 44-environment-energy-climate; memory class ``light``.

    Args:
        temperature: [series_handle, required] Temperature series.
        base_heating: [number, optional] Heating base temperature. Default ``15.5``.
        base_cooling: [number, optional] Cooling base temperature. Default ``22.0``.
        frequency: [enum, optional] Aggregation frequency. Default ``'monthly'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "env_degree_days: not implemented."
    )


def env_weather_normalise(
    *,
    demand: pd.Series,
    hdd: pd.Series,
    cdd: pd.Series,
    controls: Sequence[str] | None = None,
    estimate_base: bool | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``env_weather_normalise`` -- method card #371.

    Weather normalisation of energy demand with heating and cooling degree days.

    Category 44-environment-energy-climate; memory class ``light``.

    Args:
        demand: [series_handle, required] Energy demand series.
        hdd: [series_handle, required] Heating degree days.
        cdd: [series_handle, required] Cooling degree days.
        controls: [series_codes, optional] Additional control columns.
        estimate_base: [boolean, optional] Estimate the balance point instead of assuming it.
            Default ``False``.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "env_weather_normalise: not implemented."
    )
