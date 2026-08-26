# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``lingam`` -- method card #376.

#376 Functional causal models: ICA-LiNGAM, DirectLiNGAM and VAR-LiNGAM

Category 45-causal-discovery-graphs; module ``lingam``.

Reference implementation: lingam.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c45_causal_discovery_graphs import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "cd_lingam",
    "cd_nongaussianity_check",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def cd_lingam(
    *,
    data: pd.DataFrame,
    variant: Literal["ica", "direct", "var", "rcd"] | None = None,
    lags: int | None = None,
    nboot: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``cd_lingam`` -- method card #376.

    Functional causal models: ICA-LiNGAM, DirectLiNGAM and VAR-LiNGAM.

    Category 45-causal-discovery-graphs; memory class ``heavy``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] Observational data.
        variant: [enum, optional] Algorithm variant. Default ``'direct'``.
        lags: [integer, optional] Lag order for the time-series variant. Default ``1``.
        nboot: [integer, optional] Number of bootstrap replications. Default ``0``.
        seed: [integer, optional] Seed for the random number generator.

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
        "cd_lingam: not implemented."
    )


def cd_nongaussianity_check(
    *,
    data: pd.DataFrame,
    test: Literal["jarque_bera", "shapiro", "anderson", "dagostino"] | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``cd_nongaussianity_check`` -- method card #376.

    Functional causal models: ICA-LiNGAM, DirectLiNGAM and VAR-LiNGAM.

    Category 45-causal-discovery-graphs; memory class ``light``.

    Args:
        data: [df_handle, required] Observational data.
        test: [enum, optional] Normality test. Default ``'jarque_bera'``.
        alpha: [number, optional] Significance level. Default ``0.05``.

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
        "cd_nongaussianity_check: not implemented."
    )
