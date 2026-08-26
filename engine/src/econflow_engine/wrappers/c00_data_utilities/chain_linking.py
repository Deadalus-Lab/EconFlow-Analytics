# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``chain_linking`` -- method card #381.

#381 Chain linking with an explicit non-additivity residual

Category 00-data-utilities; module ``chain_linking``.

Reference implementation: pandas.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c00_data_utilities import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "du_chain_link",
    "du_contributions",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def du_chain_link(
    *,
    components: pd.DataFrame,
    prices: pd.DataFrame,
    method: Literal["annual_overlap", "one_quarter_overlap", "over_the_year"] | None = None,
    reference_year: int | None = None,
) -> dict[str, Any]:
    """Node ``du_chain_link`` -- method card #381.

    Chain linking with an explicit non-additivity residual.

    Category 00-data-utilities; memory class ``light``.

    Args:
        components: [multiseries_handle, required] Component volume series.
        prices: [multiseries_handle, required] Corresponding price series.
        method: [enum, optional] Linking convention. Default ``'annual_overlap'``.
        reference_year: [integer, optional] Reference year for the level.

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
        "du_chain_link: not implemented."
    )


def du_contributions(
    *,
    aggregate: pd.Series,
    components: pd.DataFrame,
    nominal: pd.DataFrame,
) -> dict[str, Any]:
    """Node ``du_contributions`` -- method card #381.

    Chain linking with an explicit non-additivity residual.

    Category 00-data-utilities; memory class ``light``.

    Args:
        aggregate: [series_handle, required] Chain-linked aggregate.
        components: [multiseries_handle, required] Chain-linked components.
        nominal: [multiseries_handle, required] Nominal component values for the weights.

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
        "du_contributions: not implemented."
    )
