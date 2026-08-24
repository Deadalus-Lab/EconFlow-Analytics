# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``walk_forward_backtest`` -- method card #331.

#331 Walk-forward backtesting with turnover and transaction costs

Category 38-portfolio-allocation; module ``walk_forward_backtest``.

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
    "pf_backtest_summary",
    "pf_walk_forward",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def pf_walk_forward(
    *,
    returns: pd.DataFrame,
    rule: str,
    train_window: int | None = None,
    rebalance_every: int | None = None,
    cost_bps: float | None = None,
    expanding: bool | None = None,
) -> dict[str, Any]:
    """Node ``pf_walk_forward`` -- method card #331.

    Walk-forward backtesting with turnover and transaction costs.

    Category 38-portfolio-allocation; memory class ``light``.

    Args:
        returns: [df_handle, required] Asset return panel.
        rule: [formula, required] Allocation rule to apply at each rebalance.
        train_window: [integer, optional] Estimation window in periods. Default ``252``.
        rebalance_every: [integer, optional] Periods between rebalances. Default ``21``.
        cost_bps: [number, optional] Round-trip cost in basis points. Default ``10.0``.
        expanding: [boolean, optional] Use an expanding rather than rolling window. Default
            ``False``.

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
        "pf_walk_forward: not implemented."
    )


def pf_backtest_summary(
    *,
    backtest: Any,
    frequency: Literal["daily", "weekly", "monthly"] | None = None,
) -> dict[str, Any]:
    """Node ``pf_backtest_summary`` -- method card #331.

    Walk-forward backtesting with turnover and transaction costs.

    Category 38-portfolio-allocation; memory class ``light``.

    Args:
        backtest: [raw_handle, required] Handle to a completed backtest.
        frequency: [enum, optional] Return frequency for annualisation. Default ``'daily'``.

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
        "pf_backtest_summary: not implemented."
    )
