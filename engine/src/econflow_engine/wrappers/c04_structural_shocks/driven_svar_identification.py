# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``driven_svar_identification`` -- method card #20.

#20 Data-driven SVAR identification (Cholesky / changes-in-vol / distance-cov / non-Gaussian ML) +
    HD + counterfactual + wild/mb bootstrap

Category 04-structural-shocks; module ``driven_svar_identification``.

Reference implementation: 10.18637/jss.v097.i05.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

from econflow_engine.generated.args.c04_structural_shocks import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "svar_cf",
    "svar_fevd",
    "svar_hd",
    "svar_id_cholesky",
    "svar_id_distance_covariance",
    "svar_id_non_gaussian_ml",
    "svar_id_volatility_change",
    "svar_irf",
    "svar_mb_boot",
    "svar_wild_boot",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def svar_id_cholesky(
    *,
    model: Any,
) -> dict[str, Any]:
    """Node ``svar_id_cholesky`` -- method card #20.

    Data-driven SVAR identification (Cholesky / changes-in-vol / distance-cov / non-Gaussian ML) +
    HD + counterfactual + wild/mb bootstrap.

    Category 04-structural-shocks; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        model: [raw_handle, required] Handle to a reduced-form 'varest' (recursive/Cholesky ID).

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
        "svar_id_cholesky: not implemented."
    )


def svar_id_volatility_change(
    *,
    model: Any,
    SB: int,
    max_iter: int | None = None,
    crit: float | None = None,
) -> dict[str, Any]:
    """Node ``svar_id_volatility_change`` -- method card #20.

    Data-driven SVAR identification (Cholesky / changes-in-vol / distance-cov / non-Gaussian ML) +
    HD + counterfactual + wild/mb bootstrap.

    Category 04-structural-shocks; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        model: [raw_handle, required] Handle to a reduced-form 'varest' (changes-in-volatility,
            Rigobon).
        SB: [integer, required] Structural break: number of pre-break observations (integer).
        max_iter: [integer, optional] Maximum EM iterations (default 50). Default ``50``.
        crit: [number, optional] Convergence criterion (default 0.001). Default ``0.001``.

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
        "svar_id_volatility_change: not implemented."
    )


def svar_id_distance_covariance(
    *,
    model: Any,
    PIT: bool | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``svar_id_distance_covariance`` -- method card #20.

    Data-driven SVAR identification (Cholesky / changes-in-vol / distance-cov / non-Gaussian ML) +
    HD + counterfactual + wild/mb bootstrap.

    Category 04-structural-shocks; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        model: [raw_handle, required] Handle to a reduced-form 'varest' (distance-covariance ID).
        PIT: [boolean, optional] Probability integral transform of the residuals (default False).
            Default ``False``.
        seed: [integer, optional] Reproducibility seed (stochastic steadyICA, default 2025). Default
            ``2025``.

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
        "svar_id_distance_covariance: not implemented."
    )


def svar_id_non_gaussian_ml(
    *,
    model: Any,
    stage3: bool | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``svar_id_non_gaussian_ml`` -- method card #20.

    Data-driven SVAR identification (Cholesky / changes-in-vol / distance-cov / non-Gaussian ML) +
    HD + counterfactual + wild/mb bootstrap.

    Category 04-structural-shocks; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        model: [raw_handle, required] Handle to a reduced-form 'varest' (non-Gaussian ML, Lanne et
            al.).
        stage3: [boolean, optional] Stage-3 GLS refinement (default False). Default ``False``.
        seed: [integer, optional] Reproducibility seed (default 2025). Default ``2025``.

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
        "svar_id_non_gaussian_ml: not implemented."
    )


def svar_irf(
    *,
    x: Any,
    n_ahead: int | None = None,
) -> dict[str, Any]:
    """Node ``svar_irf`` -- method card #20.

    Data-driven SVAR identification (Cholesky / changes-in-vol / distance-cov / non-Gaussian ML) +
    HD + counterfactual + wild/mb bootstrap.

    Category 04-structural-shocks; memory class ``light``.

    Args:
        x: [raw_handle, required] Handle to an identified 'svars' (from svar_id_*).
        n_ahead: [integer, optional] IRF horizon (positive integer, default 10). Default ``10``.

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
        "svar_irf: not implemented."
    )


def svar_fevd(
    *,
    x: Any,
    n_ahead: int | None = None,
) -> dict[str, Any]:
    """Node ``svar_fevd`` -- method card #20.

    Data-driven SVAR identification (Cholesky / changes-in-vol / distance-cov / non-Gaussian ML) +
    HD + counterfactual + wild/mb bootstrap.

    Category 04-structural-shocks; memory class ``light``.

    Args:
        x: [raw_handle, required] Handle to an identified 'svars' (from svar_id_*).
        n_ahead: [integer, optional] FEVD horizon (positive integer, default 10). Default ``10``.

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
        "svar_fevd: not implemented."
    )


def svar_hd(
    *,
    x: Any,
    series: int | None = None,
    transition: float | None = None,
) -> dict[str, Any]:
    """Node ``svar_hd`` -- method card #20.

    Data-driven SVAR identification (Cholesky / changes-in-vol / distance-cov / non-Gaussian ML) +
    HD + counterfactual + wild/mb bootstrap.

    Category 04-structural-shocks; memory class ``light``.

    Args:
        x: [raw_handle, required] Handle to an identified 'svars' (historical decomposition).
        series: [integer, optional] Variable index 1..K (default 1). Default ``1``.
        transition: [number, optional] Transition-period share in [0,1) (default 0). Default ``0``.

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
        "svar_hd: not implemented."
    )


def svar_cf(
    *,
    x: Any,
    series: int | None = None,
    transition: float | None = None,
) -> dict[str, Any]:
    """Node ``svar_cf`` -- method card #20.

    Data-driven SVAR identification (Cholesky / changes-in-vol / distance-cov / non-Gaussian ML) +
    HD + counterfactual + wild/mb bootstrap.

    Category 04-structural-shocks; memory class ``light``.

    Args:
        x: [raw_handle, required] Handle to an identified 'svars' (counterfactual).
        series: [integer, optional] Variable index 1..K (default 1). Default ``1``.
        transition: [number, optional] Transition-period share in [0,1) (default 0). Default ``0``.

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
        "svar_cf: not implemented."
    )


def svar_wild_boot(
    *,
    x: Any,
    n_ahead: int | None = None,
    nboot: int | None = None,
    design: Literal["fixed", "recursive"] | None = None,
    distr: Literal["rademacher", "mammen", "gaussian"] | None = None,
    lower_q: float | None = None,
    upper_q: float | None = None,
) -> dict[str, Any]:
    """Node ``svar_wild_boot`` -- method card #20.

    Data-driven SVAR identification (Cholesky / changes-in-vol / distance-cov / non-Gaussian ML) +
    HD + counterfactual + wild/mb bootstrap.

    Category 04-structural-shocks; memory class ``heavy``.

    Args:
        x: [raw_handle, required] Handle to an identified 'svars' (wild bootstrap,
            Gonçalves-Kilian).
        n_ahead: [integer, optional] IRF horizon (default 20). Default ``20``.
        nboot: [integer, optional] Number of bootstrap draws (default 500). Default ``500``.
        design: [enum, optional] Bootstrap design (default fixed).
        distr: [enum, optional] Distribution of the wild multiplier (default rademacher).
        lower_q: [number, optional] Lower quantile of the band (default 0.16). Default ``0.16``.
        upper_q: [number, optional] Upper quantile of the band (default 0.84). Default ``0.84``.

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
        "svar_wild_boot: not implemented."
    )


def svar_mb_boot(
    *,
    x: Any,
    n_ahead: int | None = None,
    nboot: int | None = None,
    b_length: int | None = None,
    design: Literal["recursive", "fixed"] | None = None,
    lower_q: float | None = None,
    upper_q: float | None = None,
) -> dict[str, Any]:
    """Node ``svar_mb_boot`` -- method card #20.

    Data-driven SVAR identification (Cholesky / changes-in-vol / distance-cov / non-Gaussian ML) +
    HD + counterfactual + wild/mb bootstrap.

    Category 04-structural-shocks; memory class ``heavy``.

    Args:
        x: [raw_handle, required] Handle to an identified 'svars' (moving-block bootstrap,
            Brüggemann et al.).
        n_ahead: [integer, optional] IRF horizon (default 20). Default ``20``.
        nboot: [integer, optional] Number of bootstrap draws (default 500). Default ``500``.
        b_length: [integer, optional] Block length (default 15). Default ``15``.
        design: [enum, optional] Bootstrap design (default recursive).
        lower_q: [number, optional] Lower quantile of the band (default 0.16). Default ``0.16``.
        upper_q: [number, optional] Upper quantile of the band (default 0.84). Default ``0.84``.

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
        "svar_mb_boot: not implemented."
    )
