# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``dynamic_time_warping`` -- method card #243.

#243 Dynamic Time Warping (DTW): a shape-based distance with NON-LINEAR alignment in time — a
    query/reference pair + a cross-distance matrix (`dist`) for downstream clustering

Category 29-unsupervised-clustering; module ``dynamic_time_warping``.

Reference implementation: dtaidistance.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import numpy as np
import pandas as pd

from econflow_engine.generated.args.c29_unsupervised_clustering import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "dw_align",
    "dw_dist_matrix",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def dw_align(
    *,
    query: pd.Series,
    reference: pd.Series,
    window_type: Literal["none", "sakoechiba", "slantedband", "itakura"],
    window_size: int | None = None,
    step_pattern: (
        Literal[
            "symmetric2",
            "symmetric1",
            "asymmetric",
            "symmetricP0",
            "symmetricP05",
            "symmetricP1",
            "symmetricP2",
            "asymmetricP0",
            "asymmetricP05",
            "asymmetricP1",
            "asymmetricP2",
        ]
        | None
    ) = None,
    transform: Literal["none", "zscore"] | None = None,
    distance_only: bool | None = None,
) -> dict[str, Any]:
    """Node ``dw_align`` -- method card #243.

    Dynamic Time Warping (DTW): a shape-based distance with NON-LINEAR alignment in time — a
    query/reference pair + a cross-distance matrix (`dist`) for downstream clustering.

    Category 29-unsupervised-clustering; memory class ``light``.

    Args:
        query: [series_handle, required] Handle to the QUERY SERIES (numeric/ts, >= 2 observations,
            WITHOUT NA/NaN/Inf). It may have a DIFFERENT length from the reference — that is the
            point of DTW.
        reference: [series_handle, required] Handle to the REFERENCE SERIES (numeric/ts, >= 2
            observations, WITHOUT NA/NaN/Inf).
        window_type: [enum, required] REQUIRED, never guessed: global constraint on the warping
            path. 'none' = no band (allows PATHOLOGICAL alignments — one point matching dozens)·
            'sakoechiba' = band ±window.size around the MAIN diagonal (requires window.size >=
            |N-M|)· 'slantedband' = band around the SLANTED diagonal [1,1]->[N,M] (correct choice
            for UNEQUAL-LENGTH series)· 'itakura' = Itakura parallelogram (slope [1/2,2] => requires
            0.5 <= M/N < 2, WITHOUT window.size).
        window_size: [integer, optional] Band width in cells (NON-negative integer). REQUIRED for
            window.type='sakoechiba'/'slantedband'· FORBIDDEN for 'none'/'itakura' (would be ignored
            silently -> hard gate). For 'sakoechiba' requires window.size >= |query_length -
            ref_length| otherwise "No warping path exists that is allowed by costraints".
        step_pattern: [enum, optional] Local transition rules (default 'symmetric2' = the default of
            dtw· normalizable by N+M). 'symmetric1' is NOT normalized (normalizedDistance = NA)·
            'asymmetric*' match every point of the query EXACTLY ONCE (norm = N) but d(a,b) !=
            d(b,a)· '*P0/P05/P1/P2' = increasing slope constraints Sakoe-Chiba (P2 = strictest· a
            path may not exist for series of very unequal length).
        transform: [enum, optional] EXPLICIT (gated) transformation per series — default 'none' =
            RAW data· NO silent detrending/differencing (normative gate). 'zscore' = (x-mean)/sd:
            comparison of SHAPE independent of level/scale (the standard of the DTW literature)· on
            a CONSTANT series (sd=0) -> hard gate (would give NaN silently).
        distance_only: [boolean, optional] True = distance only (faster, WITHOUT backtrack =>
            index1/index2 = null). False (default) = also returns the warping path as numeric
            chart-data for drawing in the frontend.

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
        "dw_align: not implemented."
    )


def dw_dist_matrix(
    *,
    x: np.ndarray,
    window_type: Literal["none", "sakoechiba", "slantedband", "itakura"],
    window_size: int | None = None,
    step_pattern: (
        Literal[
            "symmetric2",
            "symmetric1",
            "symmetricP0",
            "symmetricP05",
            "symmetricP1",
            "symmetricP2",
        ]
        | None
    ) = None,
    transform: Literal["none", "zscore"] | None = None,
    normalize: bool | None = None,
    orientation: Literal["rows_are_objects", "columns_are_objects"],
) -> dict[str, Any]:
    """Node ``dw_dist_matrix`` -- method card #243.

    Dynamic Time Warping (DTW): a shape-based distance with NON-LINEAR alignment in time — a
    query/reference pair + a cross-distance matrix (`dist`) for downstream clustering.

    Category 29-unsupervised-clustering; memory class ``light``.

    Registers its result under ``dist_object``, so a later node can consume it as a handle.

    Args:
        x: [matrix_handle, required] Handle to a NUMERIC matrix/DataFrame with ONE series per object
            (country/indicator). NO NA/NaN/Inf· >= 2 series· >= 2 observations· UNIQUE names.
            sliding-window subsequence input is explicitly rejected (Keogh gate).
        window_type: [enum, required] REQUIRED, never guessed: global constraint on the warping
            path. 'none' = no band (allows PATHOLOGICAL alignments — one point matching dozens)·
            'sakoechiba' = band ±window.size around the MAIN diagonal (requires window.size >=
            |N-M|)· 'slantedband' = band around the SLANTED diagonal [1,1]->[N,M] (correct choice
            for UNEQUAL-LENGTH series)· 'itakura' = Itakura parallelogram (slope [1/2,2] => requires
            0.5 <= M/N < 2, WITHOUT window.size).
        window_size: [integer, optional] Band width in cells (NON-negative integer). REQUIRED for
            window.type='sakoechiba'/'slantedband'· FORBIDDEN for 'none'/'itakura' (would be ignored
            silently -> hard gate). For 'sakoechiba' requires window.size >= |query_length -
            ref_length| otherwise "No warping path exists that is allowed by costraints".
        step_pattern: [enum, optional] ONLY SYMMETRIC patterns (default 'symmetric2'): the
            cross-distance matrix is computed on the LOWER triangle, so an asymmetric pattern
            (asymmetric*) would SILENTLY give a wrong 'symmetric' matrix -> hard gate. 'symmetric1'
            is NOT normalized (incompatible with normalize=True).
        transform: [enum, optional] EXPLICIT (gated) transformation per series — default 'none' =
            RAW data· NO silent detrending/differencing (normative gate). 'zscore' = (x-mean)/sd:
            comparison of SHAPE independent of level/scale (the standard of the DTW literature)· on
            a CONSTANT series (sd=0) -> hard gate (would give NaN silently).
        normalize: [boolean, optional] True = use normalizedDistance (distance / length constant,
            e.g. N+M) instead of the raw one — NECESSARY when comparing series of different length.
            Default False. With step.pattern='symmetric1' (norm = NA) -> hard gate.
        orientation: [enum, required] REQUIRED, never guessed: which dimension holds the SERIES.
            'rows_are_objects' = one series per ROW (time in the columns)· 'columns_are_objects' =
            series in the COLUMNS, time in the rows (typical macro panel).

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
        "dw_dist_matrix: not implemented."
    )
