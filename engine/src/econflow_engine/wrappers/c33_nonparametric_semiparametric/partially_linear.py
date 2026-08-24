# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``partially_linear`` -- method card #288.

#288 Partially linear models by the Robinson double-residual method

Category 33-nonparametric-semiparametric; module ``partially_linear``.

Reference implementation: doubleml.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c33_nonparametric_semiparametric import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "np_partially_linear",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def np_partially_linear(
    *,
    data: pd.DataFrame,
    y: str,
    d: str,
    covariates: Sequence[str] | None = None,
    learner: Literal["linear", "lasso", "random_forest", "gradient_boosting"] | None = None,
    n_folds: int | None = None,
    seed: int | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``np_partially_linear`` -- method card #288.

    Partially linear models by the Robinson double-residual method.

    Category 33-nonparametric-semiparametric; memory class ``light``.

    Args:
        data: [df_handle, required] One row per unit.
        y: [string, required] Outcome column.
        d: [string, required] Column holding the variable of interest.
        covariates: [series_codes, optional] Nuisance covariate columns.
        learner: [enum, optional] Learner for both nuisance regressions. Default
            ``'random_forest'``.
        n_folds: [integer, optional] Cross-fitting folds. Default ``5``.
        seed: [integer, optional] Seed for the random number generator.
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
        "np_partially_linear: not implemented."
    )
