# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.v1.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 26-text-as-data: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'snt_corpus': {
        'fn': 'snt_corpus',
        'description': 'snt_corpus -- category 26-text-as-data, METHOD-SELECTION card #234.',
        'args': {'df': 'Handle to a DataFrame {id(char), date(YYYY-MM-DD), texts(char, non-empty)} + optional numeric feature columns (dummies/weights e.g. wsj/wapo). >=1 document.', 'do_clean': 'Text cleaning (removal of extra whitespace/HTML/characters) (default False).'},
        'input_example': {'df': '<df_handle>', 'do_clean': False},
    },
    'snt_measures': {
        'fn': 'snt_measures',
        'description': 'snt_measures -- category 26-text-as-data, METHOD-SELECTION card #234.',
        'args': {'sentiment': 'Handle to sentiment (from snt_sentiment).', 'by': 'Aggregation time frequency (default month).', 'lag': 'Number of time periods in the smoothing window (positive integer; default 1 = no time aggregation).', 'how_time': "One or more time-weighting schemes (ALL are tried; default equal_weight). Valid: equal_weight, linear, almon, beta, exponential ('own' is not supported).", 'how_docs': 'Weighting of documents within a period (default equal_weight).', 'fill': 'Filling of periods without documents (default zero).', 'do_ignore_zeros': 'Ignore zero sentiment values in document weighting (default True).'},
        'input_example': {'sentiment': '<raw_handle>', 'lag': 1, 'do_ignore_zeros': True},
    },
    'snt_model': {
        'fn': 'snt_model',
        'description': 'snt_model -- category 26-text-as-data, METHOD-SELECTION card #234.',
        'args': {'measures': 'Handle to sento_measures (from snt_measures).', 'y': 'Target (dependent) ALIGNED with the dates of the measures (length == n_dates). gaussian: numeric; binomial: 2 values; multinomial: >=3 values.', 'model': 'Family (default gaussian=linear; binomial/multinomial=classification).', 'type': 'Selection of (alpha,lambda) (default BIC): information criterion BIC/AIC/Cp (gaussian ONLY) or cv=out-of-sample cross-validation (required also for binomial/multinomial; needs train/test_window).', 'alphas': 'Elastic-net mixing grid in [0,1] (0=ridge,1=lasso; ALL are tried; default 0,0.5,1).', 'h': 'Forecast horizon/lead (non-negative integer; default 0; h<n_dates).', 'do_intercept': 'Inclusion of intercept (default True).', 'train_window': "type='cv': training window size (positive integer; train+test < n_dates).", 'test_window': "type='cv': test window size (positive integer).", 'seed': 'Seed before the fit (locks the cv fold-RNG; default 1).'},
        'input_example': {'measures': '<raw_handle>', 'y': [0.5, 0.5], 'h': 0, 'do_intercept': True, 'seed': 1},
    },
    'snt_sentiment': {
        'fn': 'snt_sentiment',
        'description': 'snt_sentiment -- category 26-text-as-data, METHOD-SELECTION card #234.',
        'args': {'corpus': 'Handle to a sento_corpus (from snt_corpus).', 'lexicons': 'One or more built-in lexicons (default LM_en). Valid: LM_en, HENRY_en, GI_en, FEEL_en_tr, GI_fr_tr, LM_fr_tr, HENRY_fr_tr, FEEL_fr, GI_nl_tr, LM_nl_tr, HENRY_nl_tr, FEEL_nl_tr.', 'how': 'Within-document word weighting (default proportional): counts=sum of polarities; proportional=/word_count; TFIDF=tf-idf; U/inverseU/exponential=position-in-text.'},
        'input_example': {'corpus': '<raw_handle>'},
    },
}
