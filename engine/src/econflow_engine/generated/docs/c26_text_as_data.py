# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
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
        'description': 'snt_corpus -- category 26-text-as-data, method card #234.',
        'args': {'df': 'Handle to a DataFrame {id(char), date(YYYY-MM-DD), texts(char, non-empty)} + optional numeric feature columns (dummies/weights e.g. wsj/wapo). >=1 document.', 'do_clean': 'Text cleaning (removal of extra whitespace/HTML/characters) (default False).'},
        'input_example': {'df': '<df_handle>', 'do_clean': False},
    },
    'snt_measures': {
        'fn': 'snt_measures',
        'description': 'snt_measures -- category 26-text-as-data, method card #234.',
        'args': {'sentiment': 'Handle to sentiment (from snt_sentiment).', 'by': 'Aggregation time frequency (default month).', 'lag': 'Number of time periods in the smoothing window (positive integer; default 1 = no time aggregation).', 'how_time': "One or more time-weighting schemes (ALL are tried; default equal_weight). Valid: equal_weight, linear, almon, beta, exponential ('own' is not supported).", 'how_docs': 'Weighting of documents within a period (default equal_weight).', 'fill': 'Filling of periods without documents (default zero).', 'do_ignore_zeros': 'Ignore zero sentiment values in document weighting (default True).'},
        'input_example': {'sentiment': '<raw_handle>', 'lag': 1, 'do_ignore_zeros': True},
    },
    'snt_model': {
        'fn': 'snt_model',
        'description': 'snt_model -- category 26-text-as-data, method card #234.',
        'args': {'measures': 'Handle to sento_measures (from snt_measures).', 'y': 'Target (dependent) ALIGNED with the dates of the measures (length == n_dates). gaussian: numeric; binomial: 2 values; multinomial: >=3 values.', 'model': 'Family (default gaussian=linear; binomial/multinomial=classification).', 'type': 'Selection of (alpha,lambda) (default BIC): information criterion BIC/AIC/Cp (gaussian ONLY) or cv=out-of-sample cross-validation (required also for binomial/multinomial; needs train/test_window).', 'alphas': 'Elastic-net mixing grid in [0,1] (0=ridge,1=lasso; ALL are tried; default 0,0.5,1).', 'h': 'Forecast horizon/lead (non-negative integer; default 0; h<n_dates).', 'do_intercept': 'Inclusion of intercept (default True).', 'train_window': "type='cv': training window size (positive integer; train+test < n_dates).", 'test_window': "type='cv': test window size (positive integer).", 'seed': 'Seed before the fit (locks the cv fold-RNG; default 1).'},
        'input_example': {'measures': '<raw_handle>', 'y': [0.5, 0.5], 'h': 0, 'do_intercept': True, 'seed': 1},
    },
    'snt_sentiment': {
        'fn': 'snt_sentiment',
        'description': 'snt_sentiment -- category 26-text-as-data, method card #234.',
        'args': {'corpus': 'Handle to a sento_corpus (from snt_corpus).', 'lexicons': 'One or more built-in lexicons (default LM_en). Valid: LM_en, HENRY_en, GI_en, FEEL_en_tr, GI_fr_tr, LM_fr_tr, HENRY_fr_tr, FEEL_fr, GI_nl_tr, LM_nl_tr, HENRY_nl_tr, FEEL_nl_tr.', 'how': 'Within-document word weighting (default proportional): counts=sum of polarities; proportional=/word_count; TFIDF=tf-idf; U/inverseU/exponential=position-in-text.'},
        'input_example': {'corpus': '<raw_handle>'},
    },
    'tx_preprocess': {
        'fn': 'tx_preprocess',
        'description': 'tx_preprocess -- category 26-text-as-data, method card #579.',
        'args': {'documents': 'Documents with an identifier and text column.', 'text': 'Column holding the text.', 'normalise': 'Word normalisation.', 'stop_words': 'Stop-word list; omitted = a generic English list.', 'ngram_range': 'Minimum and maximum n-gram length.', 'min_df': 'Minimum document frequency.', 'max_df': 'Maximum document frequency.', 'weighting': 'Term weighting.'},
        'input_example': {'documents': '<df_handle>', 'text': '...', 'normalise': 'lemmatise', 'ngram_range': [1, 2], 'min_df': 0.01, 'max_df': 0.95, 'weighting': 'tfidf'},
    },
    'tx_topic_model': {
        'fn': 'tx_topic_model',
        'description': 'tx_topic_model -- category 26-text-as-data, method card #580.',
        'args': {'dtm': 'Handle to a document-term matrix.', 'n_topics': 'Number of topics; omitted = selected by coherence.', 'model': 'Model.', 'time': 'Document time index for the dynamic model.', 'iterations': 'Sampler iterations.', 'n_seeds': 'Seeds for a stability check.', 'seed': 'Seed for the random number generator; required for reproducibility.'},
        'input_example': {'dtm': '<raw_handle>', 'n_topics': 20, 'model': 'lda', 'iterations': 1000, 'n_seeds': 1, 'seed': 1},
    },
    'tx_topic_coherence': {
        'fn': 'tx_topic_coherence',
        'description': 'tx_topic_coherence -- category 26-text-as-data, method card #580.',
        'args': {'dtm': 'Handle to a document-term matrix.', 'topic_range': 'Topic counts to evaluate.', 'measure': 'Coherence measure.', 'seed': 'Seed for the random number generator; required for reproducibility.'},
        'input_example': {'dtm': '<raw_handle>', 'topic_range': [5, 10, 20, 30, 50], 'measure': 'c_v', 'seed': 1},
    },
    'tx_matrix_topics': {
        'fn': 'tx_matrix_topics',
        'description': 'tx_matrix_topics -- category 26-text-as-data, method card #581.',
        'args': {'dtm': 'Handle to a document-term matrix.', 'n_components': 'Number of components.', 'method': 'Factorisation.', 'init': 'Initialisation.', 'seed': 'Seed for the random number generator; required for reproducibility.'},
        'input_example': {'dtm': '<raw_handle>', 'n_components': 20, 'method': 'nmf', 'init': 'nndsvd', 'seed': 1},
    },
    'tx_embeddings': {
        'fn': 'tx_embeddings',
        'description': 'tx_embeddings -- category 26-text-as-data, method card #582.',
        'args': {'documents': 'Tokenised documents.', 'text': 'Column holding the tokens.', 'model': 'Embedding model.', 'dimensions': 'Vector dimension.', 'window': 'Context window.', 'min_count': 'Minimum token frequency.', 'epochs': 'Training epochs.', 'seed': 'Seed for the random number generator; required for reproducibility.'},
        'input_example': {'documents': '<df_handle>', 'text': '...', 'model': 'word2vec', 'dimensions': 100, 'window': 5, 'min_count': 5, 'epochs': 10, 'seed': 1},
    },
    'tx_similarity': {
        'fn': 'tx_similarity',
        'description': 'tx_similarity -- category 26-text-as-data, method card #582.',
        'args': {'model': 'Handle to trained embeddings.', 'terms': 'Terms or document ids to query.', 'top_n': 'Neighbours returned.'},
        'input_example': {'model': '<raw_handle>', 'terms': ['a', 'b'], 'top_n': 10},
    },
    'tx_news_index': {
        'fn': 'tx_news_index',
        'description': 'tx_news_index -- category 26-text-as-data, method card #583.',
        'args': {'documents': 'Documents with a date and text column.', 'text': 'Column holding the text.', 'date': 'Column holding the document date.', 'terms': 'Term groups that must co-occur.', 'normalise_by': 'Normalisation.', 'frequency': 'Aggregation frequency.', 'standardise': 'Standardise to unit variance.'},
        'input_example': {'documents': '<df_handle>', 'text': '...', 'date': '...', 'terms': '...', 'normalise_by': 'article_count', 'frequency': 'monthly', 'standardise': True},
    },
    'tx_lexicon_sentiment': {
        'fn': 'tx_lexicon_sentiment',
        'description': 'tx_lexicon_sentiment -- category 26-text-as-data, method card #584.',
        'args': {'documents': 'Documents with a text column.', 'text': 'Column holding the text.', 'lexicon': 'Lexicon.', 'custom_lexicon': 'Custom term-polarity table.', 'negation': 'Apply negation handling.', 'normalise': 'Score normalisation.'},
        'input_example': {'documents': '<df_handle>', 'text': '...', 'lexicon': 'loughran_mcdonald', 'negation': True, 'normalise': 'word_count'},
    },
    'tx_readability': {
        'fn': 'tx_readability',
        'description': 'tx_readability -- category 26-text-as-data, method card #585.',
        'args': {'documents': 'Documents with a text column.', 'text': 'Column holding the text.', 'indices': 'Indices to compute; omitted = the standard set.', 'standardise_length': 'Standardise length-dependent measures.'},
        'input_example': {'documents': '<df_handle>', 'text': '...', 'standardise_length': True},
    },
}
