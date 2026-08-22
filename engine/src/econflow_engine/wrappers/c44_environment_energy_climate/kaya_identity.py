# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``kaya_identity`` -- method card #373.

#373 Kaya identity and energy-balance accounting

Category 44-environment-energy-climate; module ``kaya_identity``.

Reference implementation: pandas.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c44_environment_energy_climate import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "env_energy_balance",
    "env_kaya",
    "NODE_META",
    "wire_model",
]


def env_kaya(
    *,
    emissions: pd.Series,
    population: pd.Series,
    output: pd.Series,
    energy: pd.Series,
    method: Literal["lmdi", "laspeyres", "simple"] | None = None,
) -> dict[str, Any]:
    """Node ``env_kaya`` -- method card #373.

    Kaya identity and energy-balance accounting.

    Category 44-environment-energy-climate; memory class ``light``.

    Args:
        emissions: [series_handle, required] Emissions.
        population: [series_handle, required] Population.
        output: [series_handle, required] Output.
        energy: [series_handle, required] Primary energy.
        method: [enum, optional] Attribution method. Default ``'lmdi'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "env_kaya: not implemented."
    )


def env_energy_balance(
    *,
    data: pd.DataFrame,
    carrier: str,
    stage: str,
    value: str,
) -> dict[str, Any]:
    """Node ``env_energy_balance`` -- method card #373.

    Kaya identity and energy-balance accounting.

    Category 44-environment-energy-climate; memory class ``light``.

    Args:
        data: [df_handle, required] Energy flows by carrier and stage.
        carrier: [string, required] Column identifying the energy carrier.
        stage: [string, required] Column identifying the balance stage.
        value: [string, required] Column holding the flow.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "env_energy_balance: not implemented."
    )
