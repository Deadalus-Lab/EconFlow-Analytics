# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``topic_models`` -- method card #580.

#580 Topic models: LDA, correlated and dynamic

Category 26-text-as-data; module ``topic_models``.

Reference implementation: tomotopy.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c26_text_as_data import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "tx_topic_coherence",
    "tx_topic_model",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def tx_topic_model(
    *,
    dtm: Any,
    n_topics: int | None = None,
    model: Literal["lda", "ctm", "dmr", "dtm", "hdp"] | None = None,
    time: pd.Series | None = None,
    iterations: int | None = None,
    n_seeds: int | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``tx_topic_model`` -- method card #580.

    Topic models: LDA, correlated and dynamic.

    Category 26-text-as-data; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        dtm: [raw_handle, required] Handle to a document-term matrix.
        n_topics: [integer, optional] Number of topics; omitted = selected by coherence. Default
            ``20``.
        model: [enum, optional] Model. Default ``'lda'``.
        time: [series_handle, optional] Document time index for the dynamic model.
        iterations: [integer, optional] Sampler iterations. Default ``1000``.
        n_seeds: [integer, optional] Seeds for a stability check. Default ``1``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.

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
        "tx_topic_model: not implemented."
    )


def tx_topic_coherence(
    *,
    dtm: Any,
    topic_range: Sequence[int] | None = None,
    measure: Literal["c_v", "u_mass", "c_npmi", "perplexity"] | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``tx_topic_coherence`` -- method card #580.

    Topic models: LDA, correlated and dynamic.

    Category 26-text-as-data; memory class ``light``.

    Args:
        dtm: [raw_handle, required] Handle to a document-term matrix.
        topic_range: [int_array, optional] Topic counts to evaluate. Default ``[5, 10, 20, 30,
            50]``.
        measure: [enum, optional] Coherence measure. Default ``'c_v'``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.

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
        "tx_topic_coherence: not implemented."
    )
