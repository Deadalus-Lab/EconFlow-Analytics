# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``spatial_interaction`` -- method card #470.

#470 Spatial interaction and gravity-type flow models

Category 09-cross-section-networks; module ``spatial_interaction``.

Reference implementation: spint.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c09_cross_section_networks import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "cs_spatial_interaction",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def cs_spatial_interaction(
    *,
    flows: pd.Series,
    origin: pd.Series,
    destination: pd.Series,
    distance: pd.Series,
    covariates: Sequence[str] | None = None,
    constraint: Literal["unconstrained", "production", "attraction", "doubly"] | None = None,
    family: Literal["poisson", "negative_binomial", "gaussian"] | None = None,
) -> dict[str, Any]:
    """Node ``cs_spatial_interaction`` -- method card #470.

    Spatial interaction and gravity-type flow models.

    Category 09-cross-section-networks; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        flows: [series_handle, required] Observed flows.
        origin: [series_handle, required] Origin identifier.
        destination: [series_handle, required] Destination identifier.
        distance: [series_handle, required] Origin-destination distance.
        covariates: [series_codes, optional] Additional flow covariates.
        constraint: [enum, optional] Constraint type. Default ``'doubly'``.
        family: [enum, optional] Estimation family. Default ``'poisson'``.

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
        "cs_spatial_interaction: not implemented."
    )
