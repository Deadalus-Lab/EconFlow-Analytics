# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``covariance_shrinkage`` -- method card #325.

#325 Covariance and return estimation with shrinkage and denoising

Category 38-portfolio-allocation; module ``covariance_shrinkage``.

Reference implementation: skfolio.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c38_portfolio_allocation import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "pf_covariance",
    "pf_expected_returns",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def pf_covariance(
    *,
    returns: pd.DataFrame,
    method: (
        Literal[
            "sample",
            "ledoit_wolf",
            "oas",
            "shrunk",
            "exponential",
            "denoised",
            "detoned",
            "graphical_lasso",
        ]
        | None
    ) = None,
    halflife: int | None = None,
    shrinkage: float | None = None,
) -> dict[str, Any]:
    """Node ``pf_covariance`` -- method card #325.

    Covariance and return estimation with shrinkage and denoising.

    Category 38-portfolio-allocation; memory class ``light``.

    Args:
        returns: [df_handle, required] Asset return panel.
        method: [enum, optional] Estimator. Default ``'ledoit_wolf'``.
        halflife: [integer, optional] Half-life for the exponential estimator.
        shrinkage: [number, optional] Manual shrinkage intensity; omitted = analytic.

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
        "pf_covariance: not implemented."
    )


def pf_expected_returns(
    *,
    returns: pd.DataFrame,
    method: (
        Literal[
            "sample",
            "exponential",
            "james_stein",
            "bayes_stein",
            "capm",
            "equal",
        ]
        | None
    ) = None,
    halflife: int | None = None,
    market: pd.Series | None = None,
) -> dict[str, Any]:
    """Node ``pf_expected_returns`` -- method card #325.

    Covariance and return estimation with shrinkage and denoising.

    Category 38-portfolio-allocation; memory class ``light``.

    Args:
        returns: [df_handle, required] Asset return panel.
        method: [enum, optional] Estimator. Default ``'james_stein'``.
        halflife: [integer, optional] Half-life for the exponential estimator.
        market: [series_handle, optional] Market return for the CAPM estimator.

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
        "pf_expected_returns: not implemented."
    )
