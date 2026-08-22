# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``copula_diagnostics`` -- method card #496.

#496 Copula goodness of fit, tail dependence and dynamic copulas

Category 12-distribution-risk; module ``copula_diagnostics``.

Reference implementation: copulae.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c12_distribution_risk import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "dr_copula_fit",
    "dr_tail_dependence",
    "NODE_META",
    "wire_model",
]


def dr_copula_fit(
    *,
    u: pd.DataFrame,
    families: Sequence[str] | None = None,
    gof: bool | None = None,
    nboot: int | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``dr_copula_fit`` -- method card #496.

    Copula goodness of fit, tail dependence and dynamic copulas.

    Category 12-distribution-risk; memory class ``heavy``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        u: [df_handle, required] Pseudo-observations on the unit cube.
        families: [series_codes, optional] Copula families to compare.
        gof: [boolean, optional] Run the parametric-bootstrap goodness-of-fit test. Default
            ``True``.
        nboot: [integer, optional] Number of bootstrap replications. Default ``999``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "dr_copula_fit: not implemented."
    )


def dr_tail_dependence(
    *,
    u: pd.DataFrame,
    method: Literal["nonparametric", "parametric", "empirical"] | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``dr_tail_dependence`` -- method card #496.

    Copula goodness of fit, tail dependence and dynamic copulas.

    Category 12-distribution-risk; memory class ``light``.

    Args:
        u: [df_handle, required] Pseudo-observations on the unit cube.
        method: [enum, optional] Estimator. Default ``'nonparametric'``.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "dr_tail_dependence: not implemented."
    )
