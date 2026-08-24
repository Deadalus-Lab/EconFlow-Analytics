# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``network_estimation_time`` -- method card #181.

#181 Network estimation for time series — a sparse VAR (Granger network) + a
    concentration/partial-correlation network via the NETS LASSO

Category 09-cross-section-networks; module ``network_estimation_time``.

Reference implementation: 10.1002/jae.2676.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c09_cross_section_networks import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "nets_fit",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def nets_fit(
    *,
    y: np.ndarray,
    p: int | None = None,
    lambda_: Sequence[float] | None = None,
    lambda_grid: Sequence[float] | None = None,
    ic: Literal["bic", "aic"] | None = None,
    GN: bool | None = None,
    CN: bool | None = None,
    algorithm: Literal["activeshooting", "shooting"] | None = None,
    weights: Literal["adaptive", "none"] | None = None,
    iter_in: int | None = None,
    iter_out: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``nets_fit`` -- method card #181.

    Network estimation for time series — a sparse VAR (Granger network) + a
    concentration/partial-correlation network via the NETS LASSO.

    Category 09-cross-section-networks; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        y: [matrix_handle, required] Multivariate matrix T x N (each column = one time series· N>=2,
            T>=3, no NA/Inf). Keep N small (~4-6).
        p: [integer, optional] VAR order (non-negative integer, default 1). Ignored when GN=False
            (space -> p=0). Default ``1``.
        lambda_ (wire name ``lambda``): [num_array, optional] Shrinkage LASSO: scalar (common
            penalty) or length-2 [AR, concentration] (GN&CN only). Positive. EXACTLY ONE of lambda /
            lambda_grid.
        lambda_grid: [num_array, optional] Candidate scalar lambdas· the best one is selected by
            information criterion (ic). EXACTLY ONE of lambda / lambda_grid.
        ic: [enum, optional] Criterion for selecting lambda within lambda_grid (default bic):
            T*log(rss)+npar*penalty.
        GN: [boolean, optional] Estimate the Granger (autoregressive) network (default True).
            Default ``True``.
        CN: [boolean, optional] Estimate the concentration (partial-correlation) network of the VAR
            innovations (default True). Default ``True``.
        algorithm: [enum, optional] LASSO optimizer (default activeshooting· faster on sparse
            models).
        weights: [enum, optional] LASSO weights: adaptive (default) or none (standard lasso).
        iter_in: [integer, optional] Maximum in iterations of the lasso (positive integer, default
            100). Default ``100``.
        iter_out: [integer, optional] Out iterations of the lasso (positive integer, default 2·
            relevant for space/nets). Default ``2``.
        seed: [integer, optional] Reproducibility seed (default 2025). Default ``2025``.

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
        "nets_fit: not implemented."
    )
