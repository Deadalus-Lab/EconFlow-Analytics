# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``implied_term_structure`` -- method card #345.

#345 Term structure of option-implied uncertainty and density fan charts

Category 40-option-implied-derivatives; module ``implied_term_structure``.

Reference implementation: QuantLib.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

import numpy as np

from econflow_engine.generated.args.c40_option_implied_derivatives import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "opt_density_fan",
    "opt_implied_term_structure",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def opt_implied_term_structure(
    *,
    maturities: Sequence[float],
    implied_variance: Sequence[float],
) -> dict[str, Any]:
    """Node ``opt_implied_term_structure`` -- method card #345.

    Term structure of option-implied uncertainty and density fan charts.

    Category 40-option-implied-derivatives; memory class ``light``.

    Args:
        maturities: [num_array, required] Times to expiry in years.
        implied_variance: [num_array, required] Model-free implied variance per maturity.

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
        "opt_implied_term_structure: not implemented."
    )


def opt_density_fan(
    *,
    densities: np.ndarray,
    grid: Sequence[float],
    quantiles: Sequence[float] | None = None,
) -> dict[str, Any]:
    """Node ``opt_density_fan`` -- method card #345.

    Term structure of option-implied uncertainty and density fan charts.

    Category 40-option-implied-derivatives; memory class ``light``.

    Args:
        densities: [matrix_handle, required] Implied density per horizon.
        grid: [num_array, required] Value grid the densities are defined on.
        quantiles: [num_array, optional] Quantile bands to report. Default ``[0.05, 0.25, 0.5, 0.75,
            0.95]``.

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
        "opt_density_fan: not implemented."
    )
