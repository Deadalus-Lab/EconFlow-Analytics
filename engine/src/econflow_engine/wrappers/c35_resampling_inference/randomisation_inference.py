# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``randomisation_inference`` -- method card #306.

#306 Randomisation and permutation inference

Category 35-resampling-inference; module ``randomisation_inference``.

Reference implementation: scipy.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c35_resampling_inference import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "rs_permutation_test",
    "rs_randomisation_ci",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def rs_permutation_test(
    *,
    outcome: pd.Series,
    treatment: pd.Series,
    block: pd.Series | None = None,
    cluster: pd.Series | None = None,
    statistic: Literal["mean_difference", "rank_sum", "t", "regression_coef"] | None = None,
    n_permutations: int | None = None,
    seed: int,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``rs_permutation_test`` -- method card #306.

    Randomisation and permutation inference.

    Category 35-resampling-inference; memory class ``light``.

    Args:
        outcome: [series_handle, required] Outcome per unit.
        treatment: [series_handle, required] Treatment assignment.
        block: [series_handle, optional] Blocking variable the randomisation respected.
        cluster: [series_handle, optional] Cluster the randomisation was applied at.
        statistic: [enum, optional] Test statistic. Default ``'mean_difference'``.
        n_permutations: [integer, optional] Sampled permutations; 0 = exhaustive. Default ``10000``.
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
        "rs_permutation_test: not implemented."
    )


def rs_randomisation_ci(
    *,
    outcome: pd.Series,
    treatment: pd.Series,
    grid: Sequence[float] | None = None,
    n_permutations: int | None = None,
    seed: int,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``rs_randomisation_ci`` -- method card #306.

    Randomisation and permutation inference.

    Category 35-resampling-inference; memory class ``light``.

    Args:
        outcome: [series_handle, required] Outcome per unit.
        treatment: [series_handle, required] Treatment assignment.
        grid: [num_array, optional] Effect grid to invert over.
        n_permutations: [integer, optional] Sampled permutations. Default ``1000``.
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
        "rs_randomisation_ci: not implemented."
    )
