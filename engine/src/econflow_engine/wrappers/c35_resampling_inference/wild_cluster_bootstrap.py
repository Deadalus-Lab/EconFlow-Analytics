# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``wild_cluster_bootstrap`` -- method card #305.

#305 Wild cluster bootstrap with few clusters

Category 35-resampling-inference; module ``wild_cluster_bootstrap``.

Reference implementation: wildboottest.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c35_resampling_inference import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "rs_wild_cluster_bootstrap",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def rs_wild_cluster_bootstrap(
    *,
    fit: Any,
    cluster: pd.Series,
    restriction: str,
    weights: Literal["rademacher", "mammen", "webb", "normal"] | None = None,
    nboot: int | None = None,
    seed: int,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``rs_wild_cluster_bootstrap`` -- method card #305.

    Wild cluster bootstrap with few clusters.

    Category 35-resampling-inference; memory class ``heavy``.

    Args:
        fit: [raw_handle, required] Handle to a fitted regression.
        cluster: [series_handle, required] Cluster identifier.
        restriction: [formula, required] Restriction tested under the null.
        weights: [enum, optional] Auxiliary weight distribution. Default ``'webb'``.
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
        "rs_wild_cluster_bootstrap: not implemented."
    )
