# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``power_analysis`` -- method card #314.

#314 Power analysis and minimum detectable effect for randomised and cluster designs

Category 36-monte-carlo-design; module ``power_analysis``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

from econflow_engine.generated.args.c36_monte_carlo_design import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "mc_power",
    "mc_power_cluster",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def mc_power(
    *,
    solve_for: Literal["n", "power", "effect"] | None = None,
    effect_size: float | None = None,
    n: int | None = None,
    power: float | None = None,
    ratio: float | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``mc_power`` -- method card #314.

    Power analysis and minimum detectable effect for randomised and cluster designs.

    Category 36-monte-carlo-design; memory class ``light``.

    Args:
        solve_for: [enum, optional] Quantity to solve for. Default ``'n'``.
        effect_size: [number, optional] Standardised effect size.
        n: [integer, optional] Sample size per arm.
        power: [number, optional] Target power. Default ``0.8``.
        ratio: [number, optional] Allocation ratio between arms. Default ``1.0``.
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
        "mc_power: not implemented."
    )


def mc_power_cluster(
    *,
    n_clusters: int | None = None,
    cluster_size: int,
    icc: float,
    effect_size: float | None = None,
    power: float | None = None,
    solve_for: Literal["n_clusters", "power", "effect"] | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``mc_power_cluster`` -- method card #314.

    Power analysis and minimum detectable effect for randomised and cluster designs.

    Category 36-monte-carlo-design; memory class ``light``.

    Args:
        n_clusters: [integer, optional] Number of clusters.
        cluster_size: [integer, required] Units per cluster.
        icc: [number, required] Intra-cluster correlation.
        effect_size: [number, optional] Standardised effect size.
        power: [number, optional] Target power. Default ``0.8``.
        solve_for: [enum, optional] Quantity to solve for. Default ``'n_clusters'``.
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
        "mc_power_cluster: not implemented."
    )
