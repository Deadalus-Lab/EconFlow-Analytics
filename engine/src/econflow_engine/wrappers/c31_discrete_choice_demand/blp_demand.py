# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``blp_demand`` -- method card #266.

#266 BLP random-coefficients logit demand estimation

Category 31-discrete-choice-demand; module ``blp_demand``.

Reference implementation: pyblp.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c31_discrete_choice_demand import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "dcd_blp_problem",
    "dcd_blp_shares",
    "dcd_blp_solve",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def dcd_blp_problem(
    *,
    product_data: pd.DataFrame,
    market_ids: str,
    shares: str,
    prices: str,
    characteristics: Sequence[str] | None = None,
    random_coefficients: Sequence[str] | None = None,
    instruments: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Node ``dcd_blp_problem`` -- method card #266.

    BLP random-coefficients logit demand estimation.

    Category 31-discrete-choice-demand; memory class ``light``.

    Registers its result under ``problem``, so a later node can consume it as a handle.

    Args:
        product_data: [df_handle, required] One row per product per market: shares, prices,
            characteristics.
        market_ids: [string, required] Column identifying the market.
        shares: [string, required] Column holding observed market shares.
        prices: [string, required] Column holding prices.
        characteristics: [series_codes, optional] Product characteristic columns entering utility
            linearly.
        random_coefficients: [series_codes, optional] Characteristics carrying a random coefficient.
        instruments: [series_codes, optional] Excluded instrument columns.

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
        "dcd_blp_problem: not implemented."
    )


def dcd_blp_solve(
    *,
    problem: Any,
    sigma_init: Sequence[float] | None = None,
    inner_tol: float | None = None,
    outer_tol: float | None = None,
    method: Literal["1s", "2s"] | None = None,
) -> dict[str, Any]:
    """Node ``dcd_blp_solve`` -- method card #266.

    BLP random-coefficients logit demand estimation.

    Category 31-discrete-choice-demand; memory class ``light``.

    Registers its result under ``results``, so a later node can consume it as a handle.

    Args:
        problem: [raw_handle, required] Handle to an assembled BLP problem.
        sigma_init: [num_array, optional] Starting values for the random-coefficient dispersion.
        inner_tol: [number, optional] Contraction tolerance for the share inversion. Default
            ``1e-14``.
        outer_tol: [number, optional] Convergence tolerance for the outer GMM search. Default
            ``1e-08``.
        method: [enum, optional] One-step or two-step GMM. Default ``'2s'``.

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
        "dcd_blp_solve: not implemented."
    )


def dcd_blp_shares(
    *,
    results: Any,
    prices: pd.Series | None = None,
) -> dict[str, Any]:
    """Node ``dcd_blp_shares`` -- method card #266.

    BLP random-coefficients logit demand estimation.

    Category 31-discrete-choice-demand; memory class ``light``.

    Args:
        results: [raw_handle, required] Handle to fitted BLP results.
        prices: [series_handle, optional] Counterfactual prices; omitted = observed.

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
        "dcd_blp_shares: not implemented."
    )
