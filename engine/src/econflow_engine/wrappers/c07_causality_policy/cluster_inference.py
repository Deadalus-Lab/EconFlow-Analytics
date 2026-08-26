# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``cluster_inference`` -- method card #449.

#449 Wild cluster bootstrap and randomisation inference for policy designs

Category 07-causality-policy; module ``cluster_inference``.

Reference implementation: wildboottest.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c07_causality_policy import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "cp_cluster_inference",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def cp_cluster_inference(
    *,
    fit: Any,
    cluster: pd.Series,
    restriction: str,
    method: Literal["wild_cluster", "randomisation", "cluster_robust"] | None = None,
    weights: Literal["rademacher", "mammen", "webb", "normal"] | None = None,
    nboot: int | None = None,
    seed: int,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``cp_cluster_inference`` -- method card #449.

    Wild cluster bootstrap and randomisation inference for policy designs.

    Category 07-causality-policy; memory class ``heavy``.

    Args:
        fit: [raw_handle, required] Handle to a fitted regression.
        cluster: [series_handle, required] Cluster identifier.
        restriction: [formula, required] Restriction tested.
        method: [enum, optional] Inference method. Default ``'wild_cluster'``.
        weights: [enum, optional] Bootstrap weights. Default ``'webb'``.
        nboot: [integer, optional] Number of bootstrap replications. Default ``999``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

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
        "cp_cluster_inference: not implemented."
    )
