# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``textual_sentiment_pipeline`` -- method card #234.

#234 Textual sentiment pipeline (corpus -> lexicon sentiment -> time aggregation -> elastic-net
    sparse-regression forecasting)

Category 26-text-as-data; module ``textual_sentiment_pipeline``.

Reference implementation: nltk.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c26_text_as_data import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "snt_corpus",
    "snt_measures",
    "snt_model",
    "snt_sentiment",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def snt_corpus(
    *,
    df: pd.DataFrame,
    do_clean: bool | None = None,
) -> dict[str, Any]:
    """Node ``snt_corpus`` -- method card #234.

    Textual sentiment pipeline (corpus -> lexicon sentiment -> time aggregation -> elastic-net
    sparse-regression forecasting).

    Category 26-text-as-data; memory class ``light``.

    Registers its result under ``corpus``, so a later node can consume it as a handle.

    Args:
        df: [df_handle, required] Handle to a DataFrame {id(char), date(YYYY-MM-DD), texts(char,
            non-empty)} + optional numeric feature columns (dummies/weights e.g. wsj/wapo). >=1
            document.
        do_clean: [boolean, optional] Text cleaning (removal of extra whitespace/HTML/characters)
            (default False). Default ``False``.

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
        "snt_corpus: not implemented."
    )


def snt_sentiment(
    *,
    corpus: Any,
    lexicons: Sequence[str] | None = None,
    how: (
        Literal[
            "proportional",
            "counts",
            "proportionalPol",
            "proportionalSquareRoot",
            "UShaped",
            "inverseUShaped",
            "exponential",
            "inverseExponential",
            "TFIDF",
        ]
        | None
    ) = None,
) -> dict[str, Any]:
    """Node ``snt_sentiment`` -- method card #234.

    Textual sentiment pipeline (corpus -> lexicon sentiment -> time aggregation -> elastic-net
    sparse-regression forecasting).

    Category 26-text-as-data; memory class ``light``.

    Registers its result under ``sentiment``, so a later node can consume it as a handle.

    Args:
        corpus: [raw_handle, required] Handle to a sento_corpus (from snt_corpus).
        lexicons: [series_codes, optional] One or more built-in lexicons (default LM_en). Valid:
            LM_en, HENRY_en, GI_en, FEEL_en_tr, GI_fr_tr, LM_fr_tr, HENRY_fr_tr, FEEL_fr, GI_nl_tr,
            LM_nl_tr, HENRY_nl_tr, FEEL_nl_tr.
        how: [enum, optional] Within-document word weighting (default proportional): counts=sum of
            polarities; proportional=/word_count; TFIDF=tf-idf;
            U/inverseU/exponential=position-in-text.

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
        "snt_sentiment: not implemented."
    )


def snt_measures(
    *,
    sentiment: Any,
    by: Literal["year", "month", "week", "day"] | None = None,
    lag: int | None = None,
    how_time: Sequence[str] | None = None,
    how_docs: (
        Literal[
            "equal_weight",
            "proportional",
            "inverseProportional",
            "exponential",
            "inverseExponential",
        ]
        | None
    ) = None,
    fill: Literal["zero", "latest", "none"] | None = None,
    do_ignore_zeros: bool | None = None,
) -> dict[str, Any]:
    """Node ``snt_measures`` -- method card #234.

    Textual sentiment pipeline (corpus -> lexicon sentiment -> time aggregation -> elastic-net
    sparse-regression forecasting).

    Category 26-text-as-data; memory class ``light``.

    Registers its result under ``measures``, so a later node can consume it as a handle.

    Args:
        sentiment: [raw_handle, required] Handle to sentiment (from snt_sentiment).
        by: [enum, optional] Aggregation time frequency (default month).
        lag: [integer, optional] Number of time periods in the smoothing window (positive integer;
            default 1 = no time aggregation). Default ``1``.
        how_time: [series_codes, optional] One or more time-weighting schemes (ALL are tried;
            default equal_weight). Valid: equal_weight, linear, almon, beta, exponential ('own' is
            not supported).
        how_docs: [enum, optional] Weighting of documents within a period (default equal_weight).
        fill: [enum, optional] Filling of periods without documents (default zero).
        do_ignore_zeros: [boolean, optional] Ignore zero sentiment values in document weighting
            (default True). Default ``True``.

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
        "snt_measures: not implemented."
    )


def snt_model(
    *,
    measures: Any,
    y: Sequence[float],
    model: Literal["gaussian", "binomial", "multinomial"] | None = None,
    type: Literal["BIC", "AIC", "Cp", "cv"] | None = None,
    alphas: Sequence[float] | None = None,
    h: int | None = None,
    do_intercept: bool | None = None,
    train_window: int | None = None,
    test_window: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``snt_model`` -- method card #234.

    Textual sentiment pipeline (corpus -> lexicon sentiment -> time aggregation -> elastic-net
    sparse-regression forecasting).

    Category 26-text-as-data; memory class ``light``.

    Args:
        measures: [raw_handle, required] Handle to sento_measures (from snt_measures).
        y: [num_array, required] Target (dependent) ALIGNED with the dates of the measures (length
            == n_dates). gaussian: numeric; binomial: 2 values; multinomial: >=3 values.
        model: [enum, optional] Family (default gaussian=linear;
            binomial/multinomial=classification).
        type: [enum, optional] Selection of (alpha,lambda) (default BIC): information criterion
            BIC/AIC/Cp (gaussian ONLY) or cv=out-of-sample cross-validation (required also for
            binomial/multinomial; needs train/test_window).
        alphas: [num_array, optional] Elastic-net mixing grid in [0,1] (0=ridge,1=lasso; ALL are
            tried; default 0,0.5,1).
        h: [integer, optional] Forecast horizon/lead (non-negative integer; default 0; h<n_dates).
            Default ``0``.
        do_intercept: [boolean, optional] Inclusion of intercept (default True). Default ``True``.
        train_window: [integer, optional] type='cv': training window size (positive integer;
            train+test < n_dates).
        test_window: [integer, optional] type='cv': test window size (positive integer).
        seed: [integer, optional] Seed before the fit (locks the cv fold-RNG; default 1). Default
            ``1``.

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
        "snt_model: not implemented."
    )
