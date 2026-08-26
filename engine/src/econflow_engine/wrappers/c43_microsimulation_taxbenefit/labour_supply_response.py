# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``labour_supply_response`` -- method card #365.

#365 Behavioural labour-supply response

Category 43-microsimulation-taxbenefit; module ``labour_supply_response``.

Reference implementation: policyengine-core.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from econflow_engine.generated.args.c43_microsimulation_taxbenefit import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "tb_labour_supply",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def tb_labour_supply(
    *,
    baseline: Any,
    reform: Any,
    intensive_elasticity: float | None = None,
    extensive_elasticity: float | None = None,
    by_group: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Node ``tb_labour_supply`` -- method card #365.

    Behavioural labour-supply response.

    Category 43-microsimulation-taxbenefit; memory class ``light``.

    Args:
        baseline: [raw_handle, required] Handle to a baseline simulation.
        reform: [raw_handle, required] Handle to a reform simulation.
        intensive_elasticity: [number, optional] Hours elasticity to the net wage. Default ``0.2``.
        extensive_elasticity: [number, optional] Participation elasticity. Default ``0.3``.
        by_group: [series_codes, optional] Columns defining groups with distinct elasticities.

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
        "tb_labour_supply: not implemented."
    )
