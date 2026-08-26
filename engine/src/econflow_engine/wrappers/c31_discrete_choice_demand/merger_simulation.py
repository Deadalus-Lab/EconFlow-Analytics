# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``merger_simulation`` -- method card #269.

#269 Merger simulation and counterfactual pricing

Category 31-discrete-choice-demand; module ``merger_simulation``.

Reference implementation: pyblp.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c31_discrete_choice_demand import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "dcd_merger_simulate",
    "dcd_upp",
    "dcd_welfare_change",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def dcd_merger_simulate(
    *,
    results: Any,
    ownership_post: np.ndarray,
    cost_change: pd.Series | None = None,
    tol: float | None = None,
    max_iter: int | None = None,
) -> dict[str, Any]:
    """Node ``dcd_merger_simulate`` -- method card #269.

    Merger simulation and counterfactual pricing.

    Category 31-discrete-choice-demand; memory class ``light``.

    Args:
        results: [raw_handle, required] Handle to fitted demand results.
        ownership_post: [matrix_handle, required] Post-merger ownership matrix.
        cost_change: [series_handle, optional] Proportional marginal-cost change per product.
        tol: [number, optional] Fixed-point tolerance. Default ``1e-12``.
        max_iter: [integer, optional] Maximum fixed-point iterations. Default ``1000``.

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
        "dcd_merger_simulate: not implemented."
    )


def dcd_upp(
    *,
    results: Any,
    merging: Sequence[str],
    efficiency: float | None = None,
) -> dict[str, Any]:
    """Node ``dcd_upp`` -- method card #269.

    Merger simulation and counterfactual pricing.

    Category 31-discrete-choice-demand; memory class ``light``.

    Args:
        results: [raw_handle, required] Handle to fitted demand results.
        merging: [series_codes, required] Product identifiers of the merging parties.
        efficiency: [number, optional] Assumed proportional marginal-cost saving. Default ``0.0``.

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
        "dcd_upp: not implemented."
    )


def dcd_welfare_change(
    *,
    results: Any,
    prices_post: pd.Series,
) -> dict[str, Any]:
    """Node ``dcd_welfare_change`` -- method card #269.

    Merger simulation and counterfactual pricing.

    Category 31-discrete-choice-demand; memory class ``light``.

    Args:
        results: [raw_handle, required] Handle to fitted demand results.
        prices_post: [series_handle, required] Counterfactual price vector.

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
        "dcd_welfare_change: not implemented."
    )
