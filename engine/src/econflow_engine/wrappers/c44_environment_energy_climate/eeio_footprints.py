# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``eeio_footprints`` -- method card #367.

#367 Environmentally-extended input-output footprints and consumption accounting

Category 44-environment-energy-climate; module ``eeio_footprints``.

Reference implementation: pymrio.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from econflow_engine.generated.args.c44_environment_energy_climate import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "env_embodied_trade",
    "env_footprint",
    "env_multipliers",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def env_footprint(
    *,
    io_table: Any,
    extension: str,
    final_demand: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Node ``env_footprint`` -- method card #367.

    Environmentally-extended input-output footprints and consumption accounting.

    Category 44-environment-energy-climate; memory class ``light``.

    Args:
        io_table: [raw_handle, required] Handle to a loaded multi-regional table.
        extension: [string, required] Environmental extension to attribute.
        final_demand: [series_codes, optional] Final-demand categories; omitted = all.

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
        "env_footprint: not implemented."
    )


def env_multipliers(
    *,
    io_table: Any,
    extension: str,
) -> dict[str, Any]:
    """Node ``env_multipliers`` -- method card #367.

    Environmentally-extended input-output footprints and consumption accounting.

    Category 44-environment-energy-climate; memory class ``light``.

    Args:
        io_table: [raw_handle, required] Handle to a loaded multi-regional table.
        extension: [string, required] Environmental extension.

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
        "env_multipliers: not implemented."
    )


def env_embodied_trade(
    *,
    io_table: Any,
    extension: str,
    region: str | None = None,
) -> dict[str, Any]:
    """Node ``env_embodied_trade`` -- method card #367.

    Environmentally-extended input-output footprints and consumption accounting.

    Category 44-environment-energy-climate; memory class ``light``.

    Args:
        io_table: [raw_handle, required] Handle to a loaded multi-regional table.
        extension: [string, required] Environmental extension.
        region: [string, optional] Region to report for; omitted = all.

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
        "env_embodied_trade: not implemented."
    )
