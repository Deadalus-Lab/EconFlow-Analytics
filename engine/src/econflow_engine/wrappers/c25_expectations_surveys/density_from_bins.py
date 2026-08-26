# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``density_from_bins`` -- method card #574.

#574 Fitting continuous densities to probability bins

Category 25-expectations-surveys; module ``density_from_bins``.

Reference implementation: scipy.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c25_expectations_surveys import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "es_fit_bin_density",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def es_fit_bin_density(
    *,
    bins: pd.DataFrame,
    family: (
        Literal[
            "generalised_beta",
            "normal",
            "triangular",
            "uniform",
            "nonparametric",
        ]
        | None
    ) = None,
    open_ended_width: float | None = None,
    min_bins: int | None = None,
) -> dict[str, Any]:
    """Node ``es_fit_bin_density`` -- method card #574.

    Fitting continuous densities to probability bins.

    Category 25-expectations-surveys; memory class ``light``.

    Args:
        bins: [df_handle, required] Bin edges and reported probabilities per respondent.
        family: [enum, optional] Distribution family. Default ``'generalised_beta'``.
        open_ended_width: [number, optional] Assumed width of open-ended end bins. Default ``1.0``.
        min_bins: [integer, optional] Minimum bins required for a parametric fit. Default ``3``.

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
        "es_fit_bin_density: not implemented."
    )
