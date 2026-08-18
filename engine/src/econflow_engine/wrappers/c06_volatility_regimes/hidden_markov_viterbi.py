# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``hidden_markov_viterbi`` -- METHOD-SELECTION card #161.

#161 (Hierarchical) Hidden Markov Models + Viterbi global decoding + forecasting

Category 06-volatility-regimes; module ``hidden_markov_viterbi``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

from econflow_engine.generated.args.c06_volatility_regimes import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "hmm_decode",
    "hmm_fit",
    "hmm_predict",
    "NODE_META",
    "wire_model",
]


def hmm_fit(
    *,
    data: Sequence[float],
    nstates: int | None = None,
    sdd: Literal["normal", "lognormal", "t", "gamma", "poisson"] | None = None,
    runs: int | None = None,
    iterlim: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``hmm_fit`` -- METHOD-SELECTION card #161.

    (Hierarchical) Hidden Markov Models + Viterbi global decoding + forecasting.

    Category 06-volatility-regimes; memory class ``heavy``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        data: [num_array, required] Numeric vector of observations/returns (>=20 obs, without
            NA/Inf, non-constant).
        nstates: [integer, optional] Number of hidden states of the Markov chain (>=2, default 2).
            Default ``2``.
        sdd: [enum, optional] State-dependent distribution (default normal·
            gamma/lognormal->positive, poisson->non-negative integers).
        runs: [integer, optional] Number of randomly initialised optimization runs (default 5).
            Default ``5``.
        iterlim: [integer, optional] Iteration limit per nlm run (default 100). Default ``100``.
        seed: [integer, optional] Reproducibility seed (ncluster=1, single-core· default 2025).
            Default ``2025``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "hmm_fit: not implemented. The method card is in ./README.md."
    )


def hmm_decode(
    *,
    object: Any,
) -> dict[str, Any]:
    """Node ``hmm_decode`` -- METHOD-SELECTION card #161.

    (Hierarchical) Hidden Markov Models + Viterbi global decoding + forecasting.

    Category 06-volatility-regimes; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to an 'fHMM_model' (from hmm_fit).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "hmm_decode: not implemented. The method card is in ./README.md."
    )


def hmm_predict(
    *,
    object: Any,
    ahead: int | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``hmm_predict`` -- METHOD-SELECTION card #161.

    (Hierarchical) Hidden Markov Models + Viterbi global decoding + forecasting.

    Category 06-volatility-regimes; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to an 'fHMM_model' (from hmm_fit).
        ahead: [integer, optional] Forecast horizon (positive integer, default 5). Default ``5``.
        alpha: [number, optional] Significance level of the prediction interval in (0,1) (default
            0.05). Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "hmm_predict: not implemented. The method card is in ./README.md."
    )
