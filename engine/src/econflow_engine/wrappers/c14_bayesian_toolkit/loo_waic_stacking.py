# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``loo_waic_stacking`` -- method card #507.

#507 LOO-CV, WAIC, model comparison and stacking weights

Category 14-bayesian-toolkit; module ``loo_waic_stacking``.

Reference implementation: arviz.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

from econflow_engine.generated.args.c14_bayesian_toolkit import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "bt_loo_compare",
    "bt_stacking_weights",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def bt_loo_compare(
    *,
    fits: Sequence[Any],
    method: Literal["loo", "waic"] | None = None,
    pointwise: bool | None = None,
    scale: Literal["log", "deviance", "negative_log"] | None = None,
) -> dict[str, Any]:
    """Node ``bt_loo_compare`` -- method card #507.

    LOO-CV, WAIC, model comparison and stacking weights.

    Category 14-bayesian-toolkit; memory class ``light``.

    Args:
        fits: [raw_handle_array, required] Handles to fitted Bayesian models.
        method: [enum, optional] Criterion. Default ``'loo'``.
        pointwise: [boolean, optional] Return pointwise contributions. Default ``True``.
        scale: [enum, optional] Reporting scale. Default ``'log'``.

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
        "bt_loo_compare: not implemented."
    )


def bt_stacking_weights(
    *,
    fits: Sequence[Any],
    method: Literal["stacking", "pseudo_bma", "pseudo_bma_bb"] | None = None,
    nboot: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``bt_stacking_weights`` -- method card #507.

    LOO-CV, WAIC, model comparison and stacking weights.

    Category 14-bayesian-toolkit; memory class ``heavy``.

    Args:
        fits: [raw_handle_array, required] Handles to fitted Bayesian models.
        method: [enum, optional] Weighting method. Default ``'stacking'``.
        nboot: [integer, optional] Number of bootstrap replications. Default ``1000``.
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
        "bt_stacking_weights: not implemented."
    )
