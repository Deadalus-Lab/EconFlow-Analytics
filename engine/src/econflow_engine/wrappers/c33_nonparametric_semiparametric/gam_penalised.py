# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``gam_penalised`` -- method card #290.

#290 Generalised additive models with penalised splines

Category 33-nonparametric-semiparametric; module ``gam_penalised``.

Reference implementation: pygam.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c33_nonparametric_semiparametric import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "np_gam_fit",
    "np_gam_partial",
    "NODE_META",
    "wire_model",
]


def np_gam_fit(
    *,
    y: pd.Series,
    x: pd.DataFrame,
    distribution: Literal["normal", "binomial", "poisson", "gamma", "inv_gauss"] | None = None,
    link: Literal["identity", "logit", "log", "inverse"] | None = None,
    n_splines: int | None = None,
    lam: float | None = None,
) -> dict[str, Any]:
    """Node ``np_gam_fit`` -- method card #290.

    Generalised additive models with penalised splines.

    Category 33-nonparametric-semiparametric; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Dependent variable.
        x: [df_handle, required] Covariate table.
        distribution: [enum, optional] Response distribution. Default ``'normal'``.
        link: [enum, optional] Link function. Default ``'identity'``.
        n_splines: [integer, optional] Basis functions per smooth term. Default ``20``.
        lam: [number, optional] Penalty; omitted = selected by grid search.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "np_gam_fit: not implemented."
    )


def np_gam_partial(
    *,
    fit: Any,
    term: int,
    grid_size: int | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``np_gam_partial`` -- method card #290.

    Generalised additive models with penalised splines.

    Category 33-nonparametric-semiparametric; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a fitted additive model.
        term: [integer, required] Index of the term to extract.
        grid_size: [integer, optional] Grid points for the curve. Default ``100``.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "np_gam_partial: not implemented."
    )
