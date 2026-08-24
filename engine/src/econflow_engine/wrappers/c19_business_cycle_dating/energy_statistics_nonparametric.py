# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``energy_statistics_nonparametric`` -- method card #215.

#215 Energy-statistics nonparametric multivariate change-point detection (E-divisive /
    E-agglomerative)

Category 19-business-cycle-dating; module ``energy_statistics_nonparametric``.

Reference implementation: 10.1080/01621459.2013.849605.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c19_business_cycle_dating import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "detect_changepoints_agglo",
    "detect_changepoints_divisive",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def detect_changepoints_divisive(
    *,
    X: np.ndarray,
    sig_lvl: float | None = None,
    n_permutations: int | None = None,
    min_size: int | None = None,
    alpha: float | None = None,
    k: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``detect_changepoints_divisive`` -- method card #215.

    Energy-statistics nonparametric multivariate change-point detection (E-divisive /
    E-agglomerative).

    Category 19-business-cycle-dating; memory class ``light``.

    Args:
        X: [matrix_handle, required] Handle to an n×d numeric matrix (multivariate series; without
            NA/Inf; nrow>=2*min.size).
        sig_lvl: [number, optional] Significance level of the permutation test in the open interval
            (0,1) (default 0.05). Default ``0.05``.
        n_permutations: [integer, optional] Number of permutations of the significance test
            (positive integer; default 199). Default ``199``.
        min_size: [integer, optional] Minimum segment size (integer >=2; default 30; requires
            nrow>=2*min.size). Default ``30``.
        alpha: [number, optional] Moment index of the energy distance in (0,2] (default 1). Default
            ``1``.
        k: [integer, optional] Optional: fixed requested number of change points (None=data-driven
            via permutation).
        seed: [integer, optional] Seed for reproducibility (e.divisive is stochastic; default
            20240101). Default ``20240101``.

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
        "detect_changepoints_divisive: not implemented."
    )


def detect_changepoints_agglo(
    *,
    X: np.ndarray,
    member: Sequence[int] | None = None,
    alpha: float | None = None,
    penalty: Literal["none", "num_cp"] | None = None,
) -> dict[str, Any]:
    """Node ``detect_changepoints_agglo`` -- method card #215.

    Energy-statistics nonparametric multivariate change-point detection (E-divisive /
    E-agglomerative).

    Category 19-business-cycle-dating; memory class ``light``.

    Args:
        X: [matrix_handle, required] Handle to an n×d numeric matrix (multivariate series; without
            NA/Inf).
        member: [int_array, optional] Optional initial segmentation vector of length the row count
            of X (default: each obs its own segment).
        alpha: [number, optional] Moment index of the energy distance in (0,2] (default 1). Default
            ``1``.
        penalty: [enum, optional] Penalized GOF penalty: 'none' (none, default) or 'num_cp' (penalty
            on the number of change points).

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
        "detect_changepoints_agglo: not implemented."
    )
