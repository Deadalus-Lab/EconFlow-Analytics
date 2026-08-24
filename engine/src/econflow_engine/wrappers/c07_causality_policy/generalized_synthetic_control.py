# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``generalized_synthetic_control`` -- method card #43.

#43 Generalized Synthetic Control (interactive FE)

Category 07-causality-policy; module ``generalized_synthetic_control``.

Reference implementation: 10.1017/pan.2016.2.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c07_causality_policy import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "gsc_fit",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def gsc_fit(
    *,
    formula: str | None = None,
    data: pd.DataFrame,
    Y: str | None = None,
    D: str | None = None,
    X: Sequence[str] | None = None,
    index: Sequence[str],
    force: Literal["two-way", "none", "unit", "time"] | None = None,
    estimator: Literal["gsynth", "ife", "mc"] | None = None,
    criterion: Literal["mspe", "pc"] | None = None,
    r: int | None = None,
    CV: bool | None = None,
    se: bool | None = None,
    nboots: int | None = None,
) -> dict[str, Any]:
    """Node ``gsc_fit`` -- method card #43.

    Generalized Synthetic Control (interactive FE).

    Category 07-causality-policy; memory class ``heavy``.

    Args:
        formula: [formula, optional] Formula 'y ~ D + x1' (D = 0/1 treatment); alternatively supply
            Y/D.
        data: [df_handle, required] Handle to a long-format panel DataFrame.
        Y: [string, optional] Outcome column name (when no formula is given).
        D: [string, optional] Treatment 0/1 column name (when Y is given).
        X: [series_codes, optional] Covariate column names (array of strings).
        index: [series_codes, required] Column names [unit, time] (exactly 2).
        force: [enum, optional] Fixed effects (default two-way).
        estimator: [enum, optional] Estimator: IFE / matrix completion (default gsynth).
        criterion: [enum, optional] CV criterion (default mspe).
        r: [integer, optional] Number of factors (default 0; CV selects it when CV=True). Default
            ``0``.
        CV: [boolean, optional] Cross-validation for r (default True). Default ``True``.
        se: [boolean, optional] Bootstrap standard errors (default False). Default ``False``.
        nboots: [integer, optional] Bootstrap iterations when se=True (default 200). Default
            ``200``.

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
        "gsc_fit: not implemented."
    )
