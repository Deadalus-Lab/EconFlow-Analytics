# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``experimental_designs`` -- method card #313.

#313 Experimental designs: Latin hypercube, factorial, Box-Behnken and Plackett-Burman

Category 36-monte-carlo-design; module ``experimental_designs``.

Reference implementation: pyDOE3.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

from econflow_engine.generated.args.c36_monte_carlo_design import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "mc_design_generate",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def mc_design_generate(
    *,
    n_factors: int,
    design: (
        Literal[
            "lhs",
            "full_factorial",
            "fractional_factorial",
            "box_behnken",
            "central_composite",
            "plackett_burman",
        ]
        | None
    ) = None,
    n_samples: int | None = None,
    levels: Sequence[int] | None = None,
    criterion: Literal["maximin", "centermaximin", "correlation", "none"] | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``mc_design_generate`` -- method card #313.

    Experimental designs: Latin hypercube, factorial, Box-Behnken and Plackett-Burman.

    Category 36-monte-carlo-design; memory class ``light``.

    Args:
        n_factors: [integer, required] Number of factors.
        design: [enum, optional] Design family. Default ``'lhs'``.
        n_samples: [integer, optional] Runs for the sampling designs. Default ``100``.
        levels: [int_array, optional] Levels per factor for factorial designs.
        criterion: [enum, optional] Optimality criterion for Latin hypercube. Default ``'maximin'``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.

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
        "mc_design_generate: not implemented."
    )
