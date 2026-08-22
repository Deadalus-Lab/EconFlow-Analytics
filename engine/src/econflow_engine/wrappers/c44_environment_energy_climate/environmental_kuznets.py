# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``environmental_kuznets`` -- method card #370.

#370 Environmental Kuznets curve and emissions-income panels

Category 44-environment-energy-climate; module ``environmental_kuznets``.

Reference implementation: pyfixest.

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
    "env_ekc",
    "NODE_META",
    "wire_model",
]


def env_ekc(
    *,
    data: pd.DataFrame,
    emissions: str,
    income: str,
    controls: Sequence[str] | None = None,
    unit: str,
    time: str,
    form: Literal["linear", "quadratic", "cubic", "semiparametric"] | None = None,
    cluster: str | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``env_ekc`` -- method card #370.

    Environmental Kuznets curve and emissions-income panels.

    Category 44-environment-energy-climate; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] Country-year panel.
        emissions: [string, required] Emissions column.
        income: [string, required] Income column.
        controls: [series_codes, optional] Control columns.
        unit: [string, required] Column identifying the country.
        time: [string, required] Column identifying the period.
        form: [enum, optional] Functional form. Default ``'quadratic'``.
        cluster: [string, optional] Clustering variable for standard errors.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "env_ekc: not implemented."
    )
