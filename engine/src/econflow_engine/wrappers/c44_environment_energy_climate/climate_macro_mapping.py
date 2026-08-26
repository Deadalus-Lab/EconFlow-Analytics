# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``climate_macro_mapping`` -- method card #372.

#372 Mapping climate scenarios onto macroeconomic paths: transition and physical risk

Category 44-environment-energy-climate; module ``climate_macro_mapping``.

Reference implementation: 10.1038/nature15725.

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
    "env_climate_macro_map",
    "env_damage_function",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def env_climate_macro_map(
    *,
    scenario: pd.DataFrame,
    elasticities: pd.DataFrame,
    horizon: int | None = None,
    component: Literal["transition", "physical", "both"] | None = None,
) -> dict[str, Any]:
    """Node ``env_climate_macro_map`` -- method card #372.

    Mapping climate scenarios onto macroeconomic paths: transition and physical risk.

    Category 44-environment-energy-climate; memory class ``light``.

    Args:
        scenario: [df_handle, required] Climate scenario variables.
        elasticities: [df_handle, required] Mapping elasticities from scenario to macro variables.
        horizon: [integer, optional] Horizon in years. Default ``30``.
        component: [enum, optional] Risk component to map. Default ``'both'``.

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
        "env_climate_macro_map: not implemented."
    )


def env_damage_function(
    *,
    temperature: pd.Series,
    function: Literal["nordhaus", "weitzman", "howard_sterner", "burke", "linear"] | None = None,
    parameters: Sequence[float] | None = None,
) -> dict[str, Any]:
    """Node ``env_damage_function`` -- method card #372.

    Mapping climate scenarios onto macroeconomic paths: transition and physical risk.

    Category 44-environment-energy-climate; memory class ``light``.

    Args:
        temperature: [series_handle, required] Warming path in degrees.
        function: [enum, optional] Damage-function family. Default ``'nordhaus'``.
        parameters: [num_array, optional] Override the default parameters.

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
        "env_damage_function: not implemented."
    )
