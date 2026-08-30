# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``rd_local_randomisation`` -- method card #447.

#447 Local-randomisation regression discontinuity

Category 07-causality-policy; module ``rd_local_randomisation``.

Reference implementation: rdlocrand.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

import pandas as pd

from econflow_engine.generated.args.c07_causality_policy import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "cp_rd_local_randomisation",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def cp_rd_local_randomisation(
    *,
    outcome: pd.Series,
    running: pd.Series,
    cutoff: float | None = None,
    covariates: Sequence[str] | None = None,
    window: Sequence[float] | None = None,
    n_permutations: int | None = None,
    seed: int,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``cp_rd_local_randomisation`` -- method card #447.

    Local-randomisation regression discontinuity.

    Category 07-causality-policy; memory class ``light``.

    Args:
        outcome: [series_handle, required] Outcome.
        running: [series_handle, required] Running variable.
        cutoff: [number, optional] Cut-off value. Default ``0.0``.
        covariates: [series_codes, optional] Covariates used for window selection and balance.
        window: [num_array, optional] Window bounds; omitted = selected by balance.
        n_permutations: [integer, optional] Randomisation draws. Default ``1000``.
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
        "cp_rd_local_randomisation: not implemented."
    )
