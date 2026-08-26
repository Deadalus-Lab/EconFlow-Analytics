# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``mcmc_convergence_diagnostics`` -- method card #72.

#72 MCMC convergence diagnostics (Gelman/Geweke/Raftery/Heidel/ESS/HPD/ACF)

Category 14-bayesian-toolkit; module ``mcmc_convergence_diagnostics``.

Reference implementation: arviz.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any

from econflow_engine.generated.args.c14_bayesian_toolkit import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "mcmc_autocorr",
    "mcmc_diagnostics",
    "mcmc_effective_size",
    "mcmc_gelman",
    "mcmc_geweke",
    "mcmc_heidel",
    "mcmc_hpd_interval",
    "mcmc_raftery",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def mcmc_diagnostics(
    *,
    chains: Any,
    confidence: float | None = None,
    prob: float | None = None,
) -> dict[str, Any]:
    """Node ``mcmc_diagnostics`` -- method card #72.

    MCMC convergence diagnostics (Gelman/Geweke/Raftery/Heidel/ESS/HPD/ACF).

    Category 14-bayesian-toolkit; memory class ``mcmc``.

    Args:
        chains: [raw_handle, required] Handle to a list of per-chain numeric matrices (iter x var)·
            >=2 chains, niter>=10.
        confidence: [number, optional] Gelman-Rubin confidence level, strictly (0,1) (default 0.95).
            Default ``0.95``.
        prob: [number, optional] HPD credible-interval probability, strictly (0,1) (default 0.95).
            Default ``0.95``.

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
        "mcmc_diagnostics: not implemented."
    )


def mcmc_gelman(
    *,
    chains: Any,
    confidence: float | None = None,
) -> dict[str, Any]:
    """Node ``mcmc_gelman`` -- method card #72.

    MCMC convergence diagnostics (Gelman/Geweke/Raftery/Heidel/ESS/HPD/ACF).

    Category 14-bayesian-toolkit; memory class ``mcmc``.

    Args:
        chains: [raw_handle, required] Handle to a list of per-chain matrices (>=2 chains·
            Gelman-Rubin PSRF/MPSRF).
        confidence: [number, optional] Confidence level, strictly (0,1) (default 0.95). Default
            ``0.95``.

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
        "mcmc_gelman: not implemented."
    )


def mcmc_geweke(
    *,
    chains: Any,
    frac1: float | None = None,
    frac2: float | None = None,
) -> dict[str, Any]:
    """Node ``mcmc_geweke`` -- method card #72.

    MCMC convergence diagnostics (Gelman/Geweke/Raftery/Heidel/ESS/HPD/ACF).

    Category 14-bayesian-toolkit; memory class ``mcmc``.

    Args:
        chains: [raw_handle, required] Handle to a list of per-chain matrices (Geweke z-score per
            chain).
        frac1: [number, optional] Fraction of the initial window (default 0.1· frac1+frac2<1).
            Default ``0.1``.
        frac2: [number, optional] Fraction of the final window (default 0.5). Default ``0.5``.

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
        "mcmc_geweke: not implemented."
    )


def mcmc_effective_size(
    *,
    chains: Any,
) -> dict[str, Any]:
    """Node ``mcmc_effective_size`` -- method card #72.

    MCMC convergence diagnostics (Gelman/Geweke/Raftery/Heidel/ESS/HPD/ACF).

    Category 14-bayesian-toolkit; memory class ``mcmc``.

    Args:
        chains: [raw_handle, required] Handle to a list of per-chain matrices· ESS (POOLED = sum of
            the chains).

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
        "mcmc_effective_size: not implemented."
    )


def mcmc_hpd_interval(
    *,
    chains: Any,
    prob: float | None = None,
) -> dict[str, Any]:
    """Node ``mcmc_hpd_interval`` -- method card #72.

    MCMC convergence diagnostics (Gelman/Geweke/Raftery/Heidel/ESS/HPD/ACF).

    Category 14-bayesian-toolkit; memory class ``mcmc``.

    Args:
        chains: [raw_handle, required] Handle to a list of per-chain matrices· HPD on the pooled
            draws.
        prob: [number, optional] HPD probability, strictly (0,1) (default 0.95· 0/1 ->
            degenerate/full-range). Default ``0.95``.

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
        "mcmc_hpd_interval: not implemented."
    )


def mcmc_raftery(
    *,
    chain: Any,
    q: float | None = None,
    r: float | None = None,
    s: float | None = None,
) -> dict[str, Any]:
    """Node ``mcmc_raftery`` -- method card #72.

    MCMC convergence diagnostics (Gelman/Geweke/Raftery/Heidel/ESS/HPD/ACF).

    Category 14-bayesian-toolkit; memory class ``light``.

    Args:
        chain: [raw_handle, required] Handle to ONE chain (numeric matrix iter x var)· Raftery-Lewis
            run-length.
        q: [number, optional] Quantile to estimate, strictly (0,1) (default 0.025). Default
            ``0.025``.
        r: [number, optional] Accuracy r, strictly (0,1) (default 0.005). Default ``0.005``.
        s: [number, optional] Probability within r, strictly (0,1) (default 0.95). Default ``0.95``.

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
        "mcmc_raftery: not implemented."
    )


def mcmc_heidel(
    *,
    chain: Any,
    eps: float | None = None,
    pvalue: float | None = None,
) -> dict[str, Any]:
    """Node ``mcmc_heidel`` -- method card #72.

    MCMC convergence diagnostics (Gelman/Geweke/Raftery/Heidel/ESS/HPD/ACF).

    Category 14-bayesian-toolkit; memory class ``light``.

    Args:
        chain: [raw_handle, required] Handle to ONE chain· Heidelberger-Welch stationarity +
            halfwidth.
        eps: [number, optional] Halfwidth target accuracy (>0, default 0.1). Default ``0.1``.
        pvalue: [number, optional] Stationarity test p-value, strictly (0,1) (default 0.05). Default
            ``0.05``.

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
        "mcmc_heidel: not implemented."
    )


def mcmc_autocorr(
    *,
    chains: Any,
) -> dict[str, Any]:
    """Node ``mcmc_autocorr`` -- method card #72.

    MCMC convergence diagnostics (Gelman/Geweke/Raftery/Heidel/ESS/HPD/ACF).

    Category 14-bayesian-toolkit; memory class ``mcmc``.

    Args:
        chains: [raw_handle, required] Handle to a list of per-chain matrices· autocorrelation per
            lag (default lags 0/1/5/10/50, all < niter).

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
        "mcmc_autocorr: not implemented."
    )
