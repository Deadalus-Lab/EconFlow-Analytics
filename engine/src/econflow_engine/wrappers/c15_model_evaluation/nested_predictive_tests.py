# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``nested_predictive_tests`` -- method card #515.

#515 Clark-West and Giacomini-White conditional predictive ability

Category 15-model-evaluation; module ``nested_predictive_tests``.

Reference implementation: 10.1016/j.jeconom.2006.05.023.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c15_model_evaluation import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "me_nested_predictive_test",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def me_nested_predictive_test(
    *,
    actual: pd.Series,
    forecast_restricted: pd.Series,
    forecast_unrestricted: pd.Series,
    test: Literal["clark_west", "giacomini_white", "diebold_mariano", "fluctuation"] | None = None,
    state: pd.Series | None = None,
    horizon: int | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``me_nested_predictive_test`` -- method card #515.

    Clark-West and Giacomini-White conditional predictive ability.

    Category 15-model-evaluation; memory class ``light``.

    Args:
        actual: [series_handle, required] Realised values.
        forecast_restricted: [series_handle, required] Forecast from the nested model.
        forecast_unrestricted: [series_handle, required] Forecast from the larger model.
        test: [enum, optional] Test. Default ``'clark_west'``.
        state: [series_handle, optional] Conditioning variable for the conditional test.
        horizon: [integer, optional] Forecast horizon, for the HAC lag. Default ``1``.
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
        "me_nested_predictive_test: not implemented."
    )
