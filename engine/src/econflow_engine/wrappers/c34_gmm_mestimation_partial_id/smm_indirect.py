# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``smm_indirect`` -- method card #297.

#297 Simulated method of moments and indirect inference

Category 34-gmm-mestimation-partial-id; module ``smm_indirect``.

Reference implementation: optimagic.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c34_gmm_mestimation_partial_id import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "gme_indirect_inference",
    "gme_smm",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def gme_smm(
    *,
    data: pd.DataFrame,
    simulator: str,
    moments: Sequence[str],
    n_sim: int | None = None,
    seed: int,
    weighting: Literal["identity", "diagonal", "efficient"] | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``gme_smm`` -- method card #297.

    Simulated method of moments and indirect inference.

    Category 34-gmm-mestimation-partial-id; memory class ``heavy``.

    Args:
        data: [df_handle, required] Observed data whose moments are matched.
        simulator: [formula, required] Specification of the simulation model.
        moments: [series_codes, required] Names of the moments to match.
        n_sim: [integer, optional] Simulation draws per evaluation. Default ``100``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.
        weighting: [enum, optional] Weighting matrix. Default ``'efficient'``.
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
        "gme_smm: not implemented."
    )


def gme_indirect_inference(
    *,
    data: pd.DataFrame,
    simulator: str,
    auxiliary: str,
    n_sim: int | None = None,
    seed: int,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``gme_indirect_inference`` -- method card #297.

    Simulated method of moments and indirect inference.

    Category 34-gmm-mestimation-partial-id; memory class ``heavy``.

    Args:
        data: [df_handle, required] Observed data.
        simulator: [formula, required] Specification of the simulation model.
        auxiliary: [formula, required] Auxiliary model whose parameters are matched.
        n_sim: [integer, optional] Simulation draws per evaluation. Default ``100``.
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
        "gme_indirect_inference: not implemented."
    )
