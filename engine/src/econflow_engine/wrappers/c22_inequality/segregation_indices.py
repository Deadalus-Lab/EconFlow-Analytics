# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``segregation_indices`` -- method card #560.

#560 Segregation and dissimilarity indices

Category 22-inequality; module ``segregation_indices``.

Reference implementation: segregation.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c22_inequality import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "iq_segregation",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def iq_segregation(
    *,
    data: pd.DataFrame,
    group: Sequence[str],
    total: str | None = None,
    index: (
        Literal[
            "dissimilarity",
            "gini",
            "entropy",
            "isolation",
            "exposure",
            "atkinson",
        ]
        | None
    ) = None,
    bias_correct: bool | None = None,
    region: str | None = None,
    nboot: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``iq_segregation`` -- method card #560.

    Segregation and dissimilarity indices.

    Category 22-inequality; memory class ``heavy``.

    Args:
        data: [df_handle, required] Area-by-group counts.
        group: [series_codes, required] Group count columns.
        total: [string, optional] Column holding the area total.
        index: [enum, optional] Index. Default ``'dissimilarity'``.
        bias_correct: [boolean, optional] Apply the small-unit bias correction. Default ``True``.
        region: [string, optional] Larger region for decomposition.
        nboot: [integer, optional] Number of bootstrap replications. Default ``500``.
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
        "iq_segregation: not implemented."
    )
