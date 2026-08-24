# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``specification_tests_np`` -- method card #291.

#291 Specification tests of a parametric null against a nonparametric alternative

Category 33-nonparametric-semiparametric; module ``specification_tests_np``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c33_nonparametric_semiparametric import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "np_specification_test",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def np_specification_test(
    *,
    y: pd.Series,
    x: pd.DataFrame,
    parametric: str,
    bandwidth: float | None = None,
    nboot: int | None = None,
    seed: int | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``np_specification_test`` -- method card #291.

    Specification tests of a parametric null against a nonparametric alternative.

    Category 33-nonparametric-semiparametric; memory class ``heavy``.

    Args:
        y: [series_handle, required] Dependent variable.
        x: [multiseries_handle, required] Covariates.
        parametric: [formula, required] Formula for the parametric null.
        bandwidth: [number, optional] Bandwidth for the nonparametric alternative.
        nboot: [integer, optional] Number of bootstrap replications. Default ``999``.
        seed: [integer, optional] Seed for the random number generator.
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
        "np_specification_test: not implemented."
    )
