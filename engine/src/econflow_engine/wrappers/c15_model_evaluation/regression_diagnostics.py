# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``regression_diagnostics`` -- method card #520.

#520 Regression diagnostic battery

Category 15-model-evaluation; module ``regression_diagnostics``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from econflow_engine.generated.args.c15_model_evaluation import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "me_regression_diagnostics",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def me_regression_diagnostics(
    *,
    fit: Any,
    tests: Sequence[str] | None = None,
    influence: bool | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``me_regression_diagnostics`` -- method card #520.

    Regression diagnostic battery.

    Category 15-model-evaluation; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a fitted regression.
        tests: [series_codes, optional] Tests to run; omitted = the standard set.
        influence: [boolean, optional] Compute influence measures. Default ``True``.
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
        "me_regression_diagnostics: not implemented."
    )
