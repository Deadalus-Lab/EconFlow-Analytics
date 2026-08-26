# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``clustering_rule_choice`` -- method card #244.

#244 Model-based clustering (a finite gaussian mixture): a RULE-BASED choice of BOTH the number of
    groups G AND the geometric covariance shape through BIC/ICL + out-of-sample assignment

Category 29-unsupervised-clustering; module ``clustering_rule_choice``.

Reference implementation: scikit-learn.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c29_unsupervised_clustering import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "mb_bic",
    "mb_fit",
    "mb_icl",
    "mb_predict",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def mb_fit(
    *,
    x: np.ndarray,
    G: Sequence[int] | None = None,
    model_names: Sequence[str] | None = None,
    transform: Literal["none", "center", "scale", "log"] | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``mb_fit`` -- method card #244.

    Model-based clustering (a finite gaussian mixture): a RULE-BASED choice of BOTH the number of
    groups G AND the geometric covariance shape through BIC/ICL + out-of-sample assignment.

    Category 29-unsupervised-clustering; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a NUMERIC observations×features matrix (rows =
            observations/countries, columns = variables). NO NA/NaN/Inf (the model-based clusterer
            SILENTLY DROPS rows with NA). n > p IS REQUIRED (p >= n => singular covariances, the
            model-based clusterer does NOT error). sliding-window IS REJECTED subsequence matrix
            (Keogh gate).
        G: [int_array, optional] Range of the number of components to examine (default 1:9).
            Positive integers with max(G) <= n — the model-based clusterer does NOT error on a
            larger G: it SILENTLY truncates the range.
        model_names: [series_codes, optional] Geometric covariance shapes to try (default None = all
            the allowed ones). Multivariate (p>1): EII VII EEI VEI EVI VVI EEE VEE EVE VVE EEV VEV
            EVV VVV (volume-shape-orientation: E=equal, V=variable, I=identity). Univariate (p=1): E
            (equal variance) / V (unequal).
        transform: [enum, optional] EXPLICIT transformation BEFORE the clustering (default 'none' —
            NO silent standardization/detrending): center (mean removal per column)· scale (z-score·
            forbidden on a zero-variance column)· log (requires > 0). The fitted params are returned
            (transform_center/transform_scale) and are applied VERBATIM to mb_predict's newdata.
        seed: [integer, optional] Reproducibility seed (default 1234). For n <= the initialisation
            threshold (=2000) the initialization is deterministic (model-based hierarchical)· ABOVE
            that the model-based clusterer initialises on a RANDOM subset => the seed DETERMINES the
            result (field 'subset_init'). Default ``1234``.

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
        "mb_fit: not implemented."
    )


def mb_bic(
    *,
    x: np.ndarray,
    G: Sequence[int] | None = None,
    model_names: Sequence[str] | None = None,
    transform: Literal["none", "center", "scale", "log"] | None = None,
    top: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``mb_bic`` -- method card #244.

    Model-based clustering (a finite gaussian mixture): a RULE-BASED choice of BOTH the number of
    groups G AND the geometric covariance shape through BIC/ICL + out-of-sample assignment.

    Category 29-unsupervised-clustering; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a NUMERIC observations×features matrix (rows =
            observations/countries, columns = variables). NO NA/NaN/Inf (the model-based clusterer
            SILENTLY DROPS rows with NA). n > p IS REQUIRED (p >= n => singular covariances, the
            model-based clusterer does NOT error). sliding-window IS REJECTED subsequence matrix
            (Keogh gate).
        G: [int_array, optional] Range of the number of components to examine (default 1:9).
            Positive integers with max(G) <= n — the model-based clusterer does NOT error on a
            larger G: it SILENTLY truncates the range.
        model_names: [series_codes, optional] Geometric covariance shapes to try (default None = all
            the allowed ones). Multivariate (p>1): EII VII EEI VEI EVI VVI EEE VEE EVE VVE EEV VEV
            EVV VVV (volume-shape-orientation: E=equal, V=variable, I=identity). Univariate (p=1): E
            (equal variance) / V (unequal).
        transform: [enum, optional] EXPLICIT transformation BEFORE the clustering (default 'none' —
            NO silent standardization/detrending): center (mean removal per column)· scale (z-score·
            forbidden on a zero-variance column)· log (requires > 0). The fitted params are returned
            (transform_center/transform_scale) and are applied VERBATIM to mb_predict's newdata.
        top: [integer, optional] Number of top candidates (model, G) returned (default 3). Default
            ``3``.
        seed: [integer, optional] Reproducibility seed (default 1234). For n <= the initialisation
            threshold (=2000) the initialization is deterministic (model-based hierarchical)· ABOVE
            that the model-based clusterer initialises on a RANDOM subset => the seed DETERMINES the
            result (field 'subset_init'). Default ``1234``.

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
        "mb_bic: not implemented."
    )


def mb_icl(
    *,
    x: np.ndarray,
    G: Sequence[int] | None = None,
    model_names: Sequence[str] | None = None,
    transform: Literal["none", "center", "scale", "log"] | None = None,
    top: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``mb_icl`` -- method card #244.

    Model-based clustering (a finite gaussian mixture): a RULE-BASED choice of BOTH the number of
    groups G AND the geometric covariance shape through BIC/ICL + out-of-sample assignment.

    Category 29-unsupervised-clustering; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a NUMERIC observations×features matrix (rows =
            observations/countries, columns = variables). NO NA/NaN/Inf (the model-based clusterer
            SILENTLY DROPS rows with NA). n > p IS REQUIRED (p >= n => singular covariances, the
            model-based clusterer does NOT error). sliding-window IS REJECTED subsequence matrix
            (Keogh gate).
        G: [int_array, optional] Range of the number of components to examine (default 1:9).
            Positive integers with max(G) <= n — the model-based clusterer does NOT error on a
            larger G: it SILENTLY truncates the range.
        model_names: [series_codes, optional] Geometric covariance shapes to try (default None = all
            the allowed ones). Multivariate (p>1): EII VII EEI VEI EVI VVI EEE VEE EVE VVE EEV VEV
            EVV VVV (volume-shape-orientation: E=equal, V=variable, I=identity). Univariate (p=1): E
            (equal variance) / V (unequal).
        transform: [enum, optional] EXPLICIT transformation BEFORE the clustering (default 'none' —
            NO silent standardization/detrending): center (mean removal per column)· scale (z-score·
            forbidden on a zero-variance column)· log (requires > 0). The fitted params are returned
            (transform_center/transform_scale) and are applied VERBATIM to mb_predict's newdata.
        top: [integer, optional] Number of top candidates (model, G) returned (default 3). Default
            ``3``.
        seed: [integer, optional] Reproducibility seed (default 1234). For n <= the initialisation
            threshold (=2000) the initialization is deterministic (model-based hierarchical)· ABOVE
            that the model-based clusterer initialises on a RANDOM subset => the seed DETERMINES the
            result (field 'subset_init'). Default ``1234``.

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
        "mb_icl: not implemented."
    )


def mb_predict(
    *,
    x: np.ndarray,
    newdata: np.ndarray,
    G: Sequence[int] | None = None,
    model_names: Sequence[str] | None = None,
    transform: Literal["none", "center", "scale", "log"] | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``mb_predict`` -- method card #244.

    Model-based clustering (a finite gaussian mixture): a RULE-BASED choice of BOTH the number of
    groups G AND the geometric covariance shape through BIC/ICL + out-of-sample assignment.

    Category 29-unsupervised-clustering; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a NUMERIC observations×features matrix (rows =
            observations/countries, columns = variables). NO NA/NaN/Inf (the model-based clusterer
            SILENTLY DROPS rows with NA). n > p IS REQUIRED (p >= n => singular covariances, the
            model-based clusterer does NOT error). sliding-window IS REJECTED subsequence matrix
            (Keogh gate).
        newdata: [matrix_handle, required] Handle to a NUMERIC matrix of new observations with
            EXACTLY the same columns (same count AND same names/order) as 'x'. predict.Mclust checks
            ONLY ncol => a shuffled column order would give WRONG assignments (silent-wrong) — it is
            blocked by a hard gate.
        G: [int_array, optional] Range of the number of components to examine (default 1:9).
            Positive integers with max(G) <= n — the model-based clusterer does NOT error on a
            larger G: it SILENTLY truncates the range.
        model_names: [series_codes, optional] Geometric covariance shapes to try (default None = all
            the allowed ones). Multivariate (p>1): EII VII EEI VEI EVI VVI EEE VEE EVE VVE EEV VEV
            EVV VVV (volume-shape-orientation: E=equal, V=variable, I=identity). Univariate (p=1): E
            (equal variance) / V (unequal).
        transform: [enum, optional] EXPLICIT transformation BEFORE the clustering (default 'none' —
            NO silent standardization/detrending): center (mean removal per column)· scale (z-score·
            forbidden on a zero-variance column)· log (requires > 0). The fitted params are returned
            (transform_center/transform_scale) and are applied VERBATIM to mb_predict's newdata.
        seed: [integer, optional] Reproducibility seed (default 1234). For n <= the initialisation
            threshold (=2000) the initialization is deterministic (model-based hierarchical)· ABOVE
            that the model-based clusterer initialises on a RANDOM subset => the seed DETERMINES the
            result (field 'subset_init'). Default ``1234``.

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
        "mb_predict: not implemented."
    )
