# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``fiscal_reaction`` -- method card #357.

#357 Fiscal reaction functions with nonlinearity and regime tests

Category 42-fiscal-debt-sustainability; module ``fiscal_reaction``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c42_fiscal_debt_sustainability import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "fis_reaction_function",
    "fis_reaction_nonlinear",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def fis_reaction_function(
    *,
    primary_balance: pd.Series,
    debt_ratio: pd.Series,
    output_gap: pd.Series | None = None,
    controls: Sequence[str] | None = None,
    cov_type: Literal["nonrobust", "robust", "hac"] | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``fis_reaction_function`` -- method card #357.

    Fiscal reaction functions with nonlinearity and regime tests.

    Category 42-fiscal-debt-sustainability; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        primary_balance: [series_handle, required] Primary balance as a share of output.
        debt_ratio: [series_handle, required] Lagged debt ratio.
        output_gap: [series_handle, optional] Output gap.
        controls: [series_codes, optional] Additional control columns.
        cov_type: [enum, optional] Covariance estimator. Default ``'hac'``.
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
        "fis_reaction_function: not implemented."
    )


def fis_reaction_nonlinear(
    *,
    primary_balance: pd.Series,
    debt_ratio: pd.Series,
    output_gap: pd.Series | None = None,
    model: Literal["threshold", "markov_switching", "quadratic", "spline"] | None = None,
    n_regimes: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``fis_reaction_nonlinear`` -- method card #357.

    Fiscal reaction functions with nonlinearity and regime tests.

    Category 42-fiscal-debt-sustainability; memory class ``light``.

    Args:
        primary_balance: [series_handle, required] Primary balance as a share of output.
        debt_ratio: [series_handle, required] Lagged debt ratio.
        output_gap: [series_handle, optional] Output gap.
        model: [enum, optional] Nonlinear form. Default ``'threshold'``.
        n_regimes: [integer, optional] Regimes for the switching form. Default ``2``.
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
        "fis_reaction_nonlinear: not implemented."
    )
