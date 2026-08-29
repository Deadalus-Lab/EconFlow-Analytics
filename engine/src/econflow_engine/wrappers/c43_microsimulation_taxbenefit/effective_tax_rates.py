# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``effective_tax_rates`` -- method card #363.

#363 Marginal and participation effective tax rates and work incentives

Category 43-microsimulation-taxbenefit; module ``effective_tax_rates``.

Reference implementation: OpenFisca-Core.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c43_microsimulation_taxbenefit import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "tb_metr",
    "tb_participation_tax_rate",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def tb_metr(
    *,
    population: pd.DataFrame,
    period: str,
    increment: float | None = None,
) -> dict[str, Any]:
    """Node ``tb_metr`` -- method card #363.

    Marginal and participation effective tax rates and work incentives.

    Category 43-microsimulation-taxbenefit; memory class ``light``.

    Args:
        population: [df_handle, required] Household microdata.
        period: [string, required] Period the calculation refers to.
        increment: [number, optional] Earnings increment used for the derivative. Default ``100.0``.

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
        "tb_metr: not implemented."
    )


def tb_participation_tax_rate(
    *,
    population: pd.DataFrame,
    period: str,
    transition: Literal["zero_to_full", "zero_to_part", "part_to_full"] | None = None,
) -> dict[str, Any]:
    """Node ``tb_participation_tax_rate`` -- method card #363.

    Marginal and participation effective tax rates and work incentives.

    Category 43-microsimulation-taxbenefit; memory class ``light``.

    Args:
        population: [df_handle, required] Household microdata.
        period: [string, required] Period the calculation refers to.
        transition: [enum, optional] Transition modelled. Default ``'zero_to_full'``.

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
        "tb_participation_tax_rate: not implemented."
    )
