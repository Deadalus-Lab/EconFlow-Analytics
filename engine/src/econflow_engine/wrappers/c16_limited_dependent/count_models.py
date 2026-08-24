# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``count_models`` -- method card #524.

#524 Count models: Poisson, negative binomial, generalised Poisson, zero-inflated and hurdle

Category 16-limited-dependent; module ``count_models``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c16_limited_dependent import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ld_count_model",
    "ld_overdispersion_test",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def ld_count_model(
    *,
    y: pd.Series,
    x: pd.DataFrame,
    family: Literal["poisson", "negative_binomial", "generalised_poisson"] | None = None,
    zeros: Literal["none", "zero_inflated", "hurdle", "truncated"] | None = None,
    exposure: pd.Series | None = None,
    inflation_covariates: Sequence[str] | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``ld_count_model`` -- method card #524.

    Count models: Poisson, negative binomial, generalised Poisson, zero-inflated and hurdle.

    Category 16-limited-dependent; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Count outcome.
        x: [df_handle, required] Covariate table.
        family: [enum, optional] Count family. Default ``'negative_binomial'``.
        zeros: [enum, optional] Zero handling. Default ``'none'``.
        exposure: [series_handle, optional] Exposure entering as an offset.
        inflation_covariates: [series_codes, optional] Covariates in the inflation equation.
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
        "ld_count_model: not implemented."
    )


def ld_overdispersion_test(
    *,
    fit: Any,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``ld_overdispersion_test`` -- method card #524.

    Count models: Poisson, negative binomial, generalised Poisson, zero-inflated and hurdle.

    Category 16-limited-dependent; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a fitted count model.
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
        "ld_overdispersion_test: not implemented."
    )
