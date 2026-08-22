# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``general_bugs_style`` -- method card #70.

#70 General BUGS-style Bayesian MCMC (injection-safe)

Category 14-bayesian-toolkit; module ``general_bugs_style``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from econflow_engine.generated.args.c14_bayesian_toolkit import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "bugs_style_mcmc",
    "NODE_META",
    "wire_model",
]


def bugs_style_mcmc(
    *,
    code: str,
    inits: Any,
    monitors: Sequence[str],
    constants: Any | None = None,
    data: Any | None = None,
    niter: int | None = None,
    nburnin: int | None = None,
    nchains: int | None = None,
    seed: int,
    thin: int | None = None,
    rhat_threshold: float | None = None,
    ess_min: float | None = None,
    allow_nonconvergence: bool | None = None,
) -> dict[str, Any]:
    """Node ``bugs_style_mcmc`` -- method card #70.

    General BUGS-style Bayesian MCMC (injection-safe).

    Category 14-bayesian-toolkit; memory class ``mcmc``.

    Args:
        code: [string, required] BUGS-style model definition AS A STRING (parse ONLY, injection-safe
            — no eval).
        inits: [raw_handle, required] Handle to a named list of initial values (covers ALL the
            top-level stochastic parameters).
        monitors: [series_codes, required] Non-empty character vector of nodes to monitor (e.g.
            ['mu','sigma']).
        constants: [raw_handle, optional] Handle to a named list of constants/dimensions (e.g. N)·
            optional.
        data: [raw_handle, optional] Handle to a named list of observations (WITHOUT NA -> silent
            MISSING-node imputation).
        niter: [integer, optional] Total MCMC iterations (default 2000). Default ``2000``.
        nburnin: [integer, optional] Burn-in (default 1000· nburnin < niter required). Default
            ``1000``.
        nchains: [integer, optional] Number of chains (>=2 for gelman.diag· default 2). Default
            ``2``.
        seed: [integer, required] REQUIRED single integer seed (reproducibility· setSeed vector).
        thin: [integer, optional] Thinning (default 1). Default ``1``.
        rhat_threshold: [number, optional] Gelman R-hat threshold (default 1.1, looser BUGS).
            Default ``1.1``.
        ess_min: [number, optional] Minimum effective sample size (default 100). Default ``100``.
        allow_nonconvergence: [boolean, optional] True -> converged=False instead of stop. Default
            ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bugs_style_mcmc: not implemented."
    )
