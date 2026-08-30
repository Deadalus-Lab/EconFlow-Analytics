# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``bart`` -- method card #511.

#511 Bayesian additive regression trees

Category 14-bayesian-toolkit; module ``bart``.

Reference implementation: pymc-bart.

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
    "bt_bart",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def bt_bart(
    *,
    y: pd.Series,
    x: pd.DataFrame,
    n_trees: int | None = None,
    draws: int | None = None,
    warmup: int | None = None,
    response: Literal["continuous", "binary", "count"] | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``bt_bart`` -- method card #511.

    Bayesian additive regression trees.

    Category 14-bayesian-toolkit; memory class ``mcmc``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Outcome.
        x: [df_handle, required] Covariate table.
        n_trees: [integer, optional] Number of trees. Default ``50``.
        draws: [integer, optional] Posterior draws. Default ``2000``.
        warmup: [integer, optional] Warm-up draws. Default ``1000``.
        response: [enum, optional] Response type. Default ``'continuous'``.
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
        "bt_bart: not implemented."
    )
