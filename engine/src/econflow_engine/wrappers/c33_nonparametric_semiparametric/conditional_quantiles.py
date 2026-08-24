# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``conditional_quantiles`` -- method card #286.

#286 Nonparametric conditional quantiles

Category 33-nonparametric-semiparametric; module ``conditional_quantiles``.

Reference implementation: quantile-forest.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c33_nonparametric_semiparametric import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "np_quantile_forest",
    "np_quantile_predict",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def np_quantile_forest(
    *,
    y: pd.Series,
    x: pd.DataFrame,
    quantiles: Sequence[float] | None = None,
    n_estimators: int | None = None,
    min_samples_leaf: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``np_quantile_forest`` -- method card #286.

    Nonparametric conditional quantiles.

    Category 33-nonparametric-semiparametric; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Dependent variable.
        x: [df_handle, required] Covariate table.
        quantiles: [num_array, optional] Quantile levels to return. Default ``[0.1, 0.5, 0.9]``.
        n_estimators: [integer, optional] Number of trees. Default ``500``.
        min_samples_leaf: [integer, optional] Minimum observations per leaf. Default ``5``.
        seed: [integer, optional] Seed for the random number generator.

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
        "np_quantile_forest: not implemented."
    )


def np_quantile_predict(
    *,
    fit: Any,
    newdata: pd.DataFrame,
    quantiles: Sequence[float] | None = None,
) -> dict[str, Any]:
    """Node ``np_quantile_predict`` -- method card #286.

    Nonparametric conditional quantiles.

    Category 33-nonparametric-semiparametric; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a fitted quantile forest.
        newdata: [df_handle, required] Covariate rows to predict for.
        quantiles: [num_array, optional] Quantile levels to return. Default ``[0.1, 0.5, 0.9]``.

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
        "np_quantile_predict: not implemented."
    )
