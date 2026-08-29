# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``variational_inference`` -- method card #509.

#509 Variational inference, Pathfinder and Laplace approximation

Category 14-bayesian-toolkit; module ``variational_inference``.

Reference implementation: pymc.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c14_bayesian_toolkit import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "bt_variational",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def bt_variational(
    *,
    model: Any,
    data: pd.DataFrame,
    method: Literal["advi", "fullrank_advi", "pathfinder", "laplace", "map"] | None = None,
    n_iterations: int | None = None,
    draws: int | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``bt_variational`` -- method card #509.

    Variational inference, Pathfinder and Laplace approximation.

    Category 14-bayesian-toolkit; memory class ``mcmc``.

    Registers its result under ``approximation``, so a later node can consume it as a handle.

    Args:
        model: [raw, required] Model specification.
        data: [df_handle, required] Data.
        method: [enum, optional] Approximation method. Default ``'pathfinder'``.
        n_iterations: [integer, optional] Optimiser iterations. Default ``20000``.
        draws: [integer, optional] Draws from the approximation. Default ``1000``.
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
        "bt_variational: not implemented."
    )
