# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``bayesian_var`` -- method card #12.

#12 Bayesian VAR (Minnesota prior)

Category 03-multivariate-nowcasting; module ``bayesian_var``.

Reference implementation: 10.1162/REST_a_00483.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any

import pandas as pd

from econflow_engine.generated.args.c03_multivariate_nowcasting import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "bvar_companion",
    "bvar_estimate",
    "bvar_fevd",
    "bvar_irf",
    "bvar_predict",
    "bvar_summary",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def bvar_estimate(
    *,
    data: pd.DataFrame,
    lags: int | None = None,
    n_draw: int | None = None,
    n_burn: int | None = None,
    n_thin: int | None = None,
    lambda_: float | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``bvar_estimate`` -- method card #12.

    Bayesian VAR (Minnesota prior).

    Category 03-multivariate-nowcasting; memory class ``mcmc``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        data: [multiseries_handle, required] Handle to multivariate data (>=2 columns, no NA).
        lags: [integer, optional] VAR lag order (default 1). Default ``1``.
        n_draw: [integer, optional] Total MCMC draws (default 10000). Default ``10000``.
        n_burn: [integer, optional] Burn-in draws (default 5000, < n_draw). Default ``5000``.
        n_thin: [integer, optional] Thinning step (default 1). Default ``1``.
        lambda_ (wire name ``lambda``): [number, optional] Minnesota tightness (mode) > 0 (default
            0.2). Default ``0.2``.
        seed: [integer, optional] Seed for reproducibility (optional).

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
        "bvar_estimate: not implemented."
    )


def bvar_predict(
    *,
    model: Any,
    horizon: int | None = None,
    conf_bands: float | None = None,
) -> dict[str, Any]:
    """Node ``bvar_predict`` -- method card #12.

    Bayesian VAR (Minnesota prior).

    Category 03-multivariate-nowcasting; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a bvar model (from bvar_estimate).
        horizon: [integer, optional] Forecast horizon (default 12). Default ``12``.
        conf_bands: [number, optional] Confidence band in (0,0.5) (default 0.16). Default ``0.16``.

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
        "bvar_predict: not implemented."
    )


def bvar_irf(
    *,
    model: Any,
    horizon: int | None = None,
    identification: bool | None = None,
    fevd: bool | None = None,
) -> dict[str, Any]:
    """Node ``bvar_irf`` -- method card #12.

    Bayesian VAR (Minnesota prior).

    Category 03-multivariate-nowcasting; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a bvar model (from bvar_estimate).
        horizon: [integer, optional] Impulse response horizon (default 12). Default ``12``.
        identification: [boolean, optional] Cholesky identification (default True). Default
            ``True``.
        fevd: [boolean, optional] Compute the FEVD together with the IRF (default False). Default
            ``False``.

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
        "bvar_irf: not implemented."
    )


def bvar_fevd(
    *,
    model: Any,
    horizon: int | None = None,
) -> dict[str, Any]:
    """Node ``bvar_fevd`` -- method card #12.

    Bayesian VAR (Minnesota prior).

    Category 03-multivariate-nowcasting; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a bvar model (from bvar_estimate).
        horizon: [integer, optional] FEVD horizon (default 12). Default ``12``.

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
        "bvar_fevd: not implemented."
    )


def bvar_companion(
    *,
    model: Any,
) -> dict[str, Any]:
    """Node ``bvar_companion`` -- method card #12.

    Bayesian VAR (Minnesota prior).

    Category 03-multivariate-nowcasting; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a bvar model (companion matrix + stability check).

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
        "bvar_companion: not implemented."
    )


def bvar_summary(
    *,
    model: Any,
) -> dict[str, Any]:
    """Node ``bvar_summary`` -- method card #12.

    Bayesian VAR (Minnesota prior).

    Category 03-multivariate-nowcasting; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a bvar model (posterior
            coef/vcov/logLik/acceptance).

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
        "bvar_summary: not implemented."
    )
