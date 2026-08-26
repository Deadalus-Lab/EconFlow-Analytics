# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``esda`` -- method card #471.

#471 Exploratory spatial data analysis: Moran, Geary, Getis-Ord and LISA

Category 09-cross-section-networks; module ``esda``.

Reference implementation: esda.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c09_cross_section_networks import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "cs_esda",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def cs_esda(
    *,
    y: pd.Series,
    weights: np.ndarray,
    statistic: Literal["moran", "geary", "getis_ord", "join_count"] | None = None,
    local: bool | None = None,
    n_permutations: int | None = None,
    adjust: Literal["none", "bonferroni", "fdr"] | None = None,
    seed: int,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``cs_esda`` -- method card #471.

    Exploratory spatial data analysis: Moran, Geary, Getis-Ord and LISA.

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        y: [series_handle, required] Variable to test.
        weights: [matrix_handle, required] Spatial weights matrix.
        statistic: [enum, optional] Statistic family. Default ``'moran'``.
        local: [boolean, optional] Compute local indicators as well. Default ``True``.
        n_permutations: [integer, optional] Permutations for inference. Default ``999``.
        adjust: [enum, optional] Multiplicity adjustment for local tests. Default ``'fdr'``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.
        alpha: [number, optional] Significance level. Default ``0.05``.

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
        "cs_esda: not implemented."
    )
