# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``optimiser_layer`` -- method card #298.

#298 Constrained estimation, numerical derivatives and the optimiser layer

Category 34-gmm-mestimation-partial-id; module ``optimiser_layer``.

Reference implementation: optimagic.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

from econflow_engine.generated.args.c34_gmm_mestimation_partial_id import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "gme_numerical_derivatives",
    "gme_optimise",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def gme_optimise(
    *,
    objective: str,
    start: Sequence[float],
    lower: Sequence[float] | None = None,
    upper: Sequence[float] | None = None,
    algorithm: (
        Literal[
            "lbfgsb",
            "nelder_mead",
            "slsqp",
            "trust_constr",
            "differential_evolution",
        ]
        | None
    ) = None,
    n_starts: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``gme_optimise`` -- method card #298.

    Constrained estimation, numerical derivatives and the optimiser layer.

    Category 34-gmm-mestimation-partial-id; memory class ``light``.

    Args:
        objective: [formula, required] Objective specification.
        start: [num_array, required] Starting values.
        lower: [num_array, optional] Lower bounds.
        upper: [num_array, optional] Upper bounds.
        algorithm: [enum, optional] Optimiser. Default ``'lbfgsb'``.
        n_starts: [integer, optional] Multi-start restarts. Default ``1``.
        seed: [integer, optional] Seed for the random number generator.

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
        "gme_optimise: not implemented."
    )


def gme_numerical_derivatives(
    *,
    objective: str,
    at: Sequence[float],
    method: Literal["forward", "backward", "central", "richardson"] | None = None,
    step: float | None = None,
) -> dict[str, Any]:
    """Node ``gme_numerical_derivatives`` -- method card #298.

    Constrained estimation, numerical derivatives and the optimiser layer.

    Category 34-gmm-mestimation-partial-id; memory class ``light``.

    Args:
        objective: [formula, required] Objective specification.
        at: [num_array, required] Point to differentiate at.
        method: [enum, optional] Difference scheme. Default ``'central'``.
        step: [number, optional] Step size; omitted = scaled automatically.

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
        "gme_numerical_derivatives: not implemented."
    )
