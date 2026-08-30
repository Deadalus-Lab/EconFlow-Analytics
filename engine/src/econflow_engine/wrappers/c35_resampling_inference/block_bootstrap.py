# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``block_bootstrap`` -- method card #301.

#301 Moving-block and circular-block bootstrap

Category 35-resampling-inference; module ``block_bootstrap``.

Reference implementation: arch.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any

import pandas as pd

from econflow_engine.generated.args.c35_resampling_inference import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "rs_block_bootstrap",
    "rs_optimal_block_length",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def rs_block_bootstrap(
    *,
    data: pd.DataFrame,
    statistic: str,
    block_length: int | None = None,
    circular: bool | None = None,
    nboot: int | None = None,
    seed: int,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``rs_block_bootstrap`` -- method card #301.

    Moving-block and circular-block bootstrap.

    Category 35-resampling-inference; memory class ``heavy``.

    Args:
        data: [multiseries_handle, required] Serially dependent data.
        statistic: [formula, required] Statistic to bootstrap.
        block_length: [integer, optional] Block length; omitted = automatic.
        circular: [boolean, optional] Wrap the series to remove end effects. Default ``True``.
        nboot: [integer, optional] Number of bootstrap replications. Default ``999``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.
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
        "rs_block_bootstrap: not implemented."
    )


def rs_optimal_block_length(
    *,
    x: pd.Series,
) -> dict[str, Any]:
    """Node ``rs_optimal_block_length`` -- method card #301.

    Moving-block and circular-block bootstrap.

    Category 35-resampling-inference; memory class ``light``.

    Args:
        x: [series_handle, required] Series whose dependence sets the block length.

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
        "rs_optimal_block_length: not implemented."
    )
