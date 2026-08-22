# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``taxbenefit_engine`` -- method card #361.

#361 Tax-benefit rule engine: parameters, entities, periods and reform overlays

Category 43-microsimulation-taxbenefit; module ``taxbenefit_engine``.

Reference implementation: OpenFisca-Core.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c43_microsimulation_taxbenefit import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "tb_compute",
    "tb_parameters",
    "tb_reform",
    "NODE_META",
    "wire_model",
]


def tb_compute(
    *,
    population: pd.DataFrame,
    variables: Sequence[str],
    period: str,
    country: Literal["generic", "uk", "fr", "us", "eu"] | None = None,
) -> dict[str, Any]:
    """Node ``tb_compute`` -- method card #361.

    Tax-benefit rule engine: parameters, entities, periods and reform overlays.

    Category 43-microsimulation-taxbenefit; memory class ``light``.

    Registers its result under ``simulation``, so a later node can consume it as a handle.

    Args:
        population: [df_handle, required] Household microdata.
        variables: [series_codes, required] Variables to compute.
        period: [string, required] Period the calculation refers to.
        country: [enum, optional] Rule set to apply. Default ``'generic'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "tb_compute: not implemented."
    )


def tb_reform(
    *,
    simulation: Any,
    reform: pd.DataFrame,
    variables: Sequence[str],
) -> dict[str, Any]:
    """Node ``tb_reform`` -- method card #361.

    Tax-benefit rule engine: parameters, entities, periods and reform overlays.

    Category 43-microsimulation-taxbenefit; memory class ``light``.

    Args:
        simulation: [raw_handle, required] Handle to a baseline simulation.
        reform: [df_handle, required] Parameter changes defining the reform.
        variables: [series_codes, required] Variables to compare.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "tb_reform: not implemented."
    )


def tb_parameters(
    *,
    period: str,
    path: str | None = None,
) -> dict[str, Any]:
    """Node ``tb_parameters`` -- method card #361.

    Tax-benefit rule engine: parameters, entities, periods and reform overlays.

    Category 43-microsimulation-taxbenefit; memory class ``light``.

    Args:
        period: [string, required] Date to read the parameters at.
        path: [string, optional] Parameter subtree to return.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "tb_parameters: not implemented."
    )
