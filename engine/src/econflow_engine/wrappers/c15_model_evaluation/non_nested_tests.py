# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``non_nested_tests`` -- method card #521.

#521 Non-nested model tests: Cox, Davidson-MacKinnon J and Vuong

Category 15-model-evaluation; module ``non_nested_tests``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

from econflow_engine.generated.args.c15_model_evaluation import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "me_non_nested_test",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def me_non_nested_test(
    *,
    fit_a: Any,
    fit_b: Any,
    test: Literal["j", "cox", "vuong", "encompassing"] | None = None,
    correction: Literal["none", "aic", "bic"] | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``me_non_nested_test`` -- method card #521.

    Non-nested model tests: Cox, Davidson-MacKinnon J and Vuong.

    Category 15-model-evaluation; memory class ``light``.

    Args:
        fit_a: [raw_handle, required] Handle to the first fitted model.
        fit_b: [raw_handle, required] Handle to the second fitted model.
        test: [enum, optional] Test. Default ``'j'``.
        correction: [enum, optional] Vuong correction. Default ``'bic'``.
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
        "me_non_nested_test: not implemented."
    )
