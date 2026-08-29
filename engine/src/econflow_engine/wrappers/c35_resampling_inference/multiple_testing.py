# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``multiple_testing`` -- method card #308.

#308 Multiple testing: Holm, Benjamini-Hochberg and Romano-Wolf stepdown

Category 35-resampling-inference; module ``multiple_testing``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import numpy as np

from econflow_engine.generated.args.c35_resampling_inference import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "rs_multiple_testing",
    "rs_romano_wolf",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def rs_multiple_testing(
    *,
    p_values: Sequence[float],
    method: Literal["bonferroni", "holm", "hochberg", "bh", "by", "sidak"] | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``rs_multiple_testing`` -- method card #308.

    Multiple testing: Holm, Benjamini-Hochberg and Romano-Wolf stepdown.

    Category 35-resampling-inference; memory class ``light``.

    Args:
        p_values: [num_array, required] Unadjusted p-values.
        method: [enum, optional] Adjustment procedure. Default ``'holm'``.
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
        "rs_multiple_testing: not implemented."
    )


def rs_romano_wolf(
    *,
    statistics: Sequence[float],
    bootstrap_draws: np.ndarray,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``rs_romano_wolf`` -- method card #308.

    Multiple testing: Holm, Benjamini-Hochberg and Romano-Wolf stepdown.

    Category 35-resampling-inference; memory class ``light``.

    Args:
        statistics: [num_array, required] Test statistics.
        bootstrap_draws: [matrix_handle, required] Bootstrap draws of the statistics under the null.
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
        "rs_romano_wolf: not implemented."
    )
