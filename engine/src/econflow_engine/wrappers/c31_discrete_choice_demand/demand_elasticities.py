# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``demand_elasticities`` -- method card #268.

#268 Own- and cross-price elasticities and diversion ratios

Category 31-discrete-choice-demand; module ``demand_elasticities``.

Reference implementation: pyblp.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c31_discrete_choice_demand import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "dcd_diversion",
    "dcd_elasticities",
    "dcd_markups",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def dcd_elasticities(
    *,
    results: Any,
    market_id: str | None = None,
    variable: str | None = None,
) -> dict[str, Any]:
    """Node ``dcd_elasticities`` -- method card #268.

    Own- and cross-price elasticities and diversion ratios.

    Category 31-discrete-choice-demand; memory class ``light``.

    Args:
        results: [raw_handle, required] Handle to fitted demand results.
        market_id: [string, optional] Restrict to one market; omitted = every market.
        variable: [string, optional] Characteristic to differentiate with respect to. Default
            ``'prices'``.

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
        "dcd_elasticities: not implemented."
    )


def dcd_diversion(
    *,
    results: Any,
    market_id: str | None = None,
    include_outside: bool | None = None,
) -> dict[str, Any]:
    """Node ``dcd_diversion`` -- method card #268.

    Own- and cross-price elasticities and diversion ratios.

    Category 31-discrete-choice-demand; memory class ``light``.

    Args:
        results: [raw_handle, required] Handle to fitted demand results.
        market_id: [string, optional] Restrict to one market.
        include_outside: [boolean, optional] Include the outside good as a destination. Default
            ``True``.

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
        "dcd_diversion: not implemented."
    )


def dcd_markups(
    *,
    results: Any,
    conduct: Literal["bertrand", "monopoly", "cournot"] | None = None,
    ownership: np.ndarray | None = None,
) -> dict[str, Any]:
    """Node ``dcd_markups`` -- method card #268.

    Own- and cross-price elasticities and diversion ratios.

    Category 31-discrete-choice-demand; memory class ``light``.

    Args:
        results: [raw_handle, required] Handle to fitted demand results.
        conduct: [enum, optional] Assumed firm conduct. Default ``'bertrand'``.
        ownership: [matrix_handle, optional] Ownership matrix; omitted = single-product firms.

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
        "dcd_markups: not implemented."
    )
