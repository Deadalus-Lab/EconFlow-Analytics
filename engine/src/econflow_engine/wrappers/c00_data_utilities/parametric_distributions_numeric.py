# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``parametric_distributions_numeric`` -- method card #118.

#118 Parametric distributions (normal/student_t) as a numeric grid: quantile bands / cdf / density /
    moments (fan-chart data)

Category 00-data-utilities; module ``parametric_distributions_numeric``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

from econflow_engine.generated.args.c00_data_utilities import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "dist_density_grid",
    "dist_fan_quantiles",
    "dist_moments",
    "dist_prob_cdf",
    "NODE_META",
    "wire_model",
]


def dist_fan_quantiles(
    *,
    family: Literal["normal", "student_t"] | None = None,
    mu: Sequence[float],
    sigma: Sequence[float],
    df: Sequence[float] | None = None,
    probs: Sequence[float] | None = None,
) -> dict[str, Any]:
    """Node ``dist_fan_quantiles`` -- method card #118.

    Parametric distributions (normal/student_t) as a numeric grid: quantile bands / cdf / density /
    moments (fan-chart data).

    Category 00-data-utilities; memory class ``light``.

    Args:
        family: [enum, optional] Distribution family: normal (default) or student_t (location-scale,
            fat tails).
        mu: [num_array, required] Mean/location per distribution (e.g. per forecast horizon);
            recycled from length 1 or a common L.
        sigma: [num_array, required] Scale (strictly >0) per distribution; recycled from length 1 or
            L.
        df: [num_array, optional] Degrees of freedom (>0); MANDATORY for student_t, ignored for
            normal.
        probs: [num_array, optional] Quantile-band probabilities, strictly in (0,1) (default [0.1,
            0.25, 0.5, 0.75, 0.9]); outside => ±Inf/NaN (gated).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "dist_fan_quantiles: not implemented."
    )


def dist_prob_cdf(
    *,
    family: Literal["normal", "student_t"] | None = None,
    mu: Sequence[float],
    sigma: Sequence[float],
    df: Sequence[float] | None = None,
    at: Sequence[float],
) -> dict[str, Any]:
    """Node ``dist_prob_cdf`` -- method card #118.

    Parametric distributions (normal/student_t) as a numeric grid: quantile bands / cdf / density /
    moments (fan-chart data).

    Category 00-data-utilities; memory class ``light``.

    Args:
        family: [enum, optional] normal (default) or student_t.
        mu: [num_array, required] Mean/location per distribution; recycled from length 1 or L.
        sigma: [num_array, required] Scale (>0) per distribution; recycled from length 1 or L.
        df: [num_array, optional] df (>0); mandatory for student_t.
        at: [num_array, required] Points q at which P(X<=q) is evaluated (finite).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "dist_prob_cdf: not implemented."
    )


def dist_density_grid(
    *,
    family: Literal["normal", "student_t"] | None = None,
    mu: Sequence[float],
    sigma: Sequence[float],
    df: Sequence[float] | None = None,
    at: Sequence[float],
) -> dict[str, Any]:
    """Node ``dist_density_grid`` -- method card #118.

    Parametric distributions (normal/student_t) as a numeric grid: quantile bands / cdf / density /
    moments (fan-chart data).

    Category 00-data-utilities; memory class ``light``.

    Args:
        family: [enum, optional] normal (default) or student_t.
        mu: [num_array, required] Mean/location per distribution; recycled from length 1 or L.
        sigma: [num_array, required] Scale (>0) per distribution; recycled from length 1 or L.
        df: [num_array, optional] df (>0); mandatory for student_t.
        at: [num_array, required] Points x at which the density f(x) is evaluated (finite).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "dist_density_grid: not implemented."
    )


def dist_moments(
    *,
    family: Literal["normal", "student_t"] | None = None,
    mu: Sequence[float],
    sigma: Sequence[float],
    df: Sequence[float] | None = None,
) -> dict[str, Any]:
    """Node ``dist_moments`` -- method card #118.

    Parametric distributions (normal/student_t) as a numeric grid: quantile bands / cdf / density /
    moments (fan-chart data).

    Category 00-data-utilities; memory class ``light``.

    Args:
        family: [enum, optional] normal (default) or student_t.
        mu: [num_array, required] Mean/location per distribution; recycled from length 1 or L.
        sigma: [num_array, required] Scale (>0) per distribution; recycled from length 1 or L.
        df: [num_array, optional] df (>0); mandatory for student_t (variance is infinite for df<=2).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "dist_moments: not implemented."
    )
