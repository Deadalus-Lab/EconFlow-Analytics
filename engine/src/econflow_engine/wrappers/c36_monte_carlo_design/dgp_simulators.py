# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``dgp_simulators`` -- method card #309.

#309 Data-generating-process simulators for ARMA, VAR, GARCH, panel and factor models

Category 36-monte-carlo-design; module ``dgp_simulators``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c36_monte_carlo_design import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "mc_simulate_arma",
    "mc_simulate_garch",
    "mc_simulate_panel",
    "mc_simulate_var",
    "NODE_META",
    "wire_model",
]


def mc_simulate_arma(
    *,
    n: int,
    ar: Sequence[float] | None = None,
    ma: Sequence[float] | None = None,
    d: int | None = None,
    sigma: float | None = None,
    burnin: int | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``mc_simulate_arma`` -- method card #309.

    Data-generating-process simulators for ARMA, VAR, GARCH, panel and factor models.

    Category 36-monte-carlo-design; memory class ``mcmc``.

    Args:
        n: [integer, required] Observations to generate.
        ar: [num_array, optional] Autoregressive coefficients.
        ma: [num_array, optional] Moving-average coefficients.
        d: [integer, optional] Order of integration. Default ``0``.
        sigma: [number, optional] Innovation standard deviation. Default ``1.0``.
        burnin: [integer, optional] Discarded initial observations. Default ``500``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mc_simulate_arma: not implemented."
    )


def mc_simulate_var(
    *,
    n: int,
    coefs: np.ndarray,
    sigma: np.ndarray,
    burnin: int | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``mc_simulate_var`` -- method card #309.

    Data-generating-process simulators for ARMA, VAR, GARCH, panel and factor models.

    Category 36-monte-carlo-design; memory class ``mcmc``.

    Args:
        n: [integer, required] Observations to generate.
        coefs: [matrix_handle, required] Stacked coefficient matrices.
        sigma: [matrix_handle, required] Innovation covariance.
        burnin: [integer, optional] Discarded initial observations. Default ``500``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mc_simulate_var: not implemented."
    )


def mc_simulate_garch(
    *,
    n: int,
    omega: float,
    alpha: Sequence[float],
    beta: Sequence[float],
    distribution: Literal["normal", "t", "skewt", "ged"] | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``mc_simulate_garch`` -- method card #309.

    Data-generating-process simulators for ARMA, VAR, GARCH, panel and factor models.

    Category 36-monte-carlo-design; memory class ``light``.

    Args:
        n: [integer, required] Observations to generate.
        omega: [number, required] Variance intercept.
        alpha: [num_array, required] ARCH coefficients.
        beta: [num_array, required] GARCH coefficients.
        distribution: [enum, optional] Innovation distribution. Default ``'normal'``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mc_simulate_garch: not implemented."
    )


def mc_simulate_panel(
    *,
    n_units: int,
    n_periods: int,
    beta: Sequence[float],
    unit_sd: float | None = None,
    time_sd: float | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``mc_simulate_panel`` -- method card #309.

    Data-generating-process simulators for ARMA, VAR, GARCH, panel and factor models.

    Category 36-monte-carlo-design; memory class ``light``.

    Args:
        n_units: [integer, required] Number of units.
        n_periods: [integer, required] Periods per unit.
        beta: [num_array, required] Slope coefficients.
        unit_sd: [number, optional] Standard deviation of unit effects. Default ``1.0``.
        time_sd: [number, optional] Standard deviation of time effects. Default ``0.5``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mc_simulate_panel: not implemented."
    )
