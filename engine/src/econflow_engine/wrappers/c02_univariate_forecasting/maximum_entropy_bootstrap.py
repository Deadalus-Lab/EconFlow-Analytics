# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``maximum_entropy_bootstrap`` -- method card #138.

#138 Maximum Entropy Bootstrap for time series (dependence/non-stationarity preserved)

Category 02-univariate-forecasting; module ``maximum_entropy_bootstrap``.

Reference implementation: 10.1016/j.asieco.2006.09.001.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c02_univariate_forecasting import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "meb_ensemble",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def meb_ensemble(
    *,
    x: pd.Series,
    seed: int,
    reps: int | None = None,
    trim: float | None = None,
    reachbnd: bool | None = None,
    expand_sd: bool | None = None,
    force_clt: bool | None = None,
    scl_adjustment: bool | None = None,
    sym: bool | None = None,
) -> dict[str, Any]:
    """Node ``meb_ensemble`` -- method card #138.

    Maximum Entropy Bootstrap for time series (dependence/non-stationarity preserved).

    Category 02-univariate-forecasting; memory class ``light``.

    Registers its result under ``ensemble``, so a later node can consume it as a handle.

    Args:
        x: [series_handle, required] Handle to a univariate series (numeric/ts; fully finite,
            length>=2).
        seed: [integer, required] Seed (REQUIRED; stochastic — seeded before the draw;
            reproducibility/caching).
        reps: [integer, optional] Number of bootstrap replicates (default 999; gate reps>=10).
        trim: [number, optional] Trimming proportion of the tails (default 0.10; gate 0<=trim<0.5).
        reachbnd: [boolean, optional] Reached-bounds draws at the 0/1 edges (default True).
        expand_sd: [boolean, optional] Widening of the ensemble's SD (default True).
        force_clt: [boolean, optional] Forcing of CLT on the ensemble mean (default True).
        scl_adjustment: [boolean, optional] Scale adjustment so that var(ensemble)=var(x) (default
            False).
        sym: [boolean, optional] Symmetric ME density adjustment (default False).

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
        "meb_ensemble: not implemented."
    )
