# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``nongaussian_identification`` -- method card #425.

#425 Non-Gaussian higher-moment identification

Category 04-structural-shocks; module ``nongaussian_identification``.

Reference implementation: SVARpy.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c04_structural_shocks import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ss_nongaussian_svar",
    "ss_nongaussianity_diagnostics",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def ss_nongaussian_svar(
    *,
    y: pd.DataFrame,
    lags: int | None = None,
    moments: Literal["third", "fourth", "third_and_fourth"] | None = None,
    horizons: int | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``ss_nongaussian_svar`` -- method card #425.

    Non-Gaussian higher-moment identification.

    Category 04-structural-shocks; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        y: [multiseries_handle, required] Endogenous variables.
        lags: [integer, optional] VAR lag order. Default ``4``.
        moments: [enum, optional] Moments used for identification. Default ``'third_and_fourth'``.
        horizons: [integer, optional] Impulse-response horizon. Default ``20``.
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
        "ss_nongaussian_svar: not implemented."
    )


def ss_nongaussianity_diagnostics(
    *,
    y: pd.DataFrame,
    lags: int | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``ss_nongaussianity_diagnostics`` -- method card #425.

    Non-Gaussian higher-moment identification.

    Category 04-structural-shocks; memory class ``light``.

    Args:
        y: [multiseries_handle, required] Endogenous variables.
        lags: [integer, optional] VAR lag order. Default ``4``.
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
        "ss_nongaussianity_diagnostics: not implemented."
    )
