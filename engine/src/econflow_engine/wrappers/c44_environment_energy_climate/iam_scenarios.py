# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``iam_scenarios`` -- method card #369.

#369 Integrated-assessment scenario handling, harmonisation and aggregation

Category 44-environment-energy-climate; module ``iam_scenarios``.

Reference implementation: pyam-iamc.

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
    "env_scenario_aggregate",
    "env_scenario_filter",
    "env_scenario_harmonise",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def env_scenario_filter(
    *,
    data: pd.DataFrame,
    model: Sequence[str] | None = None,
    scenario: Sequence[str] | None = None,
    variable: Sequence[str] | None = None,
    region: Sequence[str] | None = None,
    year: Sequence[int] | None = None,
) -> dict[str, Any]:
    """Node ``env_scenario_filter`` -- method card #369.

    Integrated-assessment scenario handling, harmonisation and aggregation.

    Category 44-environment-energy-climate; memory class ``light``.

    Args:
        data: [df_handle, required] Scenario data in the standard long format.
        model: [series_codes, optional] Models to keep.
        scenario: [series_codes, optional] Scenarios to keep.
        variable: [series_codes, optional] Variables to keep.
        region: [series_codes, optional] Regions to keep.
        year: [int_array, optional] Years to keep.

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
        "env_scenario_filter: not implemented."
    )


def env_scenario_harmonise(
    *,
    data: pd.DataFrame,
    history: pd.DataFrame,
    base_year: int,
    method: Literal["ratio", "offset", "reduce_ratio", "reduce_offset"] | None = None,
    convergence_year: int | None = None,
) -> dict[str, Any]:
    """Node ``env_scenario_harmonise`` -- method card #369.

    Integrated-assessment scenario handling, harmonisation and aggregation.

    Category 44-environment-energy-climate; memory class ``light``.

    Args:
        data: [df_handle, required] Scenario data.
        history: [df_handle, required] Historical values to harmonise to.
        base_year: [integer, required] Year to harmonise on.
        method: [enum, optional] Harmonisation method. Default ``'ratio'``.
        convergence_year: [integer, optional] Year the adjustment converges to zero. Default
            ``2050``.

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
        "env_scenario_harmonise: not implemented."
    )


def env_scenario_aggregate(
    *,
    data: pd.DataFrame,
    mapping: pd.DataFrame,
    dimension: Literal["region", "variable"] | None = None,
    method: Literal["sum", "mean", "weighted"] | None = None,
) -> dict[str, Any]:
    """Node ``env_scenario_aggregate`` -- method card #369.

    Integrated-assessment scenario handling, harmonisation and aggregation.

    Category 44-environment-energy-climate; memory class ``light``.

    Args:
        data: [df_handle, required] Scenario data.
        mapping: [df_handle, required] Aggregation mapping.
        dimension: [enum, optional] Dimension to aggregate. Default ``'region'``.
        method: [enum, optional] Aggregation function. Default ``'sum'``.

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
        "env_scenario_aggregate: not implemented."
    )
