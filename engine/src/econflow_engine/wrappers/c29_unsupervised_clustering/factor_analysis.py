# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``factor_analysis`` -- method card #600.

#600 Exploratory factor analysis with rotation and independent components

Category 29-unsupervised-clustering; module ``factor_analysis``.

Reference implementation: factor-analyzer.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c29_unsupervised_clustering import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "uc_factor_analysis",
    "uc_ica",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def uc_factor_analysis(
    *,
    x: pd.DataFrame,
    n_factors: int | None = None,
    rotation: Literal["none", "varimax", "promax", "oblimin", "quartimax"] | None = None,
    method: Literal["minres", "ml", "principal"] | None = None,
    criterion: Literal["kaiser", "scree", "parallel", "mean_eigenvalue"] | None = None,
) -> dict[str, Any]:
    """Node ``uc_factor_analysis`` -- method card #600.

    Exploratory factor analysis with rotation and independent components.

    Category 29-unsupervised-clustering; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        x: [df_handle, required] Observed variables.
        n_factors: [integer, optional] Number of factors; omitted = selected by criterion.
        rotation: [enum, optional] Rotation. Default ``'promax'``.
        method: [enum, optional] Extraction method. Default ``'minres'``.
        criterion: [enum, optional] Factor-count criterion. Default ``'parallel'``.

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
        "uc_factor_analysis: not implemented."
    )


def uc_ica(
    *,
    x: pd.DataFrame,
    n_components: int | None = None,
    algorithm: Literal["parallel", "deflation"] | None = None,
    whiten: bool | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``uc_ica`` -- method card #600.

    Exploratory factor analysis with rotation and independent components.

    Category 29-unsupervised-clustering; memory class ``light``.

    Args:
        x: [df_handle, required] Observed variables.
        n_components: [integer, optional] Components to extract.
        algorithm: [enum, optional] Algorithm. Default ``'parallel'``.
        whiten: [boolean, optional] Whiten the data first. Default ``True``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.

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
        "uc_ica: not implemented."
    )
