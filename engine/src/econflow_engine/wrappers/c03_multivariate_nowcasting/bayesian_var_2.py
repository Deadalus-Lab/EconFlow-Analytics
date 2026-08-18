# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``bayesian_var_2`` -- METHOD-SELECTION card #13.

#13 Bayesian VAR (Gibbs sampler)

Category 03-multivariate-nowcasting; module ``bayesian_var_2``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c03_multivariate_nowcasting import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "bt_fevd",
    "bt_irf",
    "bt_predict",
    "bt_summary",
    "bt_var",
    "NODE_META",
    "wire_model",
]


def bt_var(
    *,
    data: pd.DataFrame,
    p: int | None = None,
    deterministic: Literal["const", "none", "trend", "both"] | None = None,
    iterations: int | None = None,
    burnin: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``bt_var`` -- METHOD-SELECTION card #13.

    Bayesian VAR (Gibbs sampler).

    Category 03-multivariate-nowcasting; memory class ``mcmc``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        data: [multiseries_handle, required] Handle to ts/mts data (>=2 columns, no NA).
        p: [integer, optional] VAR(p) lag order (default 2). Default ``2``.
        deterministic: [enum, optional] Deterministic terms (default const).
        iterations: [integer, optional] MCMC iterations (default 10000). Default ``10000``.
        burnin: [integer, optional] Burn-in draws (default 5000, < iterations). Default ``5000``.
        seed: [integer, optional] Seed for reproducibility (optional).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bt_var: not implemented. The method card is in ./README.md."
    )


def bt_predict(
    *,
    model: Any,
    n_ahead: int | None = None,
    ci: float | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``bt_predict`` -- METHOD-SELECTION card #13.

    Bayesian VAR (Gibbs sampler).

    Category 03-multivariate-nowcasting; memory class ``heavy``.

    Args:
        model: [raw_handle, required] Handle to a bvar model (from bt_var).
        n_ahead: [integer, optional] Forecast horizon (default 10). Default ``10``.
        ci: [number, optional] Confidence level in (0,1) (default 0.95). Default ``0.95``.
        seed: [integer, optional] Seed for reproducibility (optional).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bt_predict: not implemented. The method card is in ./README.md."
    )


def bt_irf(
    *,
    model: Any,
    impulse: str,
    response: str,
    n_ahead: int | None = None,
    ci: float | None = None,
    type: Literal["feir", "oir", "gir", "sir", "sgir"] | None = None,
    cumulative: bool | None = None,
) -> dict[str, Any]:
    """Node ``bt_irf`` -- METHOD-SELECTION card #13.

    Bayesian VAR (Gibbs sampler).

    Category 03-multivariate-nowcasting; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a bvar model (from bt_var).
        impulse: [string, required] Name of the shock variable (impulse).
        response: [string, required] Name of the response variable (response).
        n_ahead: [integer, optional] IRF horizon (default 5). Default ``5``.
        ci: [number, optional] Confidence level in (0,1) (default 0.95). Default ``0.95``.
        type: [enum, optional] IRF type (default feir = forecast error impulse response).
        cumulative: [boolean, optional] Cumulative IRF (default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bt_irf: not implemented. The method card is in ./README.md."
    )


def bt_fevd(
    *,
    model: Any,
    response: str,
    n_ahead: int | None = None,
    type: Literal["oir", "gir", "sir", "sgir"] | None = None,
) -> dict[str, Any]:
    """Node ``bt_fevd`` -- METHOD-SELECTION card #13.

    Bayesian VAR (Gibbs sampler).

    Category 03-multivariate-nowcasting; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a bvar model (from bt_var).
        response: [string, required] Name of the response variable for the FEVD.
        n_ahead: [integer, optional] FEVD horizon (default 5). Default ``5``.
        type: [enum, optional] Decomposition type (default oir = orthogonalised).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bt_fevd: not implemented. The method card is in ./README.md."
    )


def bt_summary(
    *,
    model: Any,
    ci: float | None = None,
) -> dict[str, Any]:
    """Node ``bt_summary`` -- METHOD-SELECTION card #13.

    Bayesian VAR (Gibbs sampler).

    Category 03-multivariate-nowcasting; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a bvar model (posterior coefficients/sigma).
        ci: [number, optional] Confidence level of the credible intervals (default 0.95). Default
            ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bt_summary: not implemented. The method card is in ./README.md."
    )
