# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 2 for category 26-text-as-data -- 13 nodes. No descriptions."""

from functools import cache

from pydantic import BaseModel

from econflow_engine.kinds import (
    NodeArgMeta,
    NodeExecutabilityMeta,
    NodeMeta,
    build_authoring_model,
    build_wire_model,
)

NODE_META: dict[str, NodeMeta] = {
    'snt_corpus': NodeMeta(
        fn='snt_corpus',
        category='26-text-as-data',
        card_id=234,
        contract_hash='c2-08f41258e3b2403b68601bfddc4b26b562241994b082469c592ad2a79f31d9bf',
        register_field='corpus',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='df', kind='df_handle', required=True),
        NodeArgMeta(name='do_clean', kind='boolean', required=False),
        ),
        defaults={'do_clean': False},
    ),
    'snt_measures': NodeMeta(
        fn='snt_measures',
        category='26-text-as-data',
        card_id=234,
        contract_hash='c2-5deff1f37637befe13b11b75253c08a8a5613f1c7be7bf41c40f315696d5e33e',
        register_field='measures',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='sentiment', kind='raw_handle', required=True),
        NodeArgMeta(name='by', kind='enum', required=False, enum=('year', 'month', 'week', 'day', )),
        NodeArgMeta(name='lag', kind='integer', required=False),
        NodeArgMeta(name='how_time', kind='series_codes', required=False),
        NodeArgMeta(name='how_docs', kind='enum', required=False, enum=('equal_weight', 'proportional', 'inverseProportional', 'exponential', 'inverseExponential', )),
        NodeArgMeta(name='fill', kind='enum', required=False, enum=('zero', 'latest', 'none', )),
        NodeArgMeta(name='do_ignore_zeros', kind='boolean', required=False),
        ),
        defaults={'lag': 1, 'do_ignore_zeros': True},
    ),
    'snt_model': NodeMeta(
        fn='snt_model',
        category='26-text-as-data',
        card_id=234,
        contract_hash='c2-2c1699a57630fe809be61ca9d6e039b81d9c3bcd38f6b003fc1a06b510aac146',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='measures', kind='raw_handle', required=True),
        NodeArgMeta(name='y', kind='num_array', required=True),
        NodeArgMeta(name='model', kind='enum', required=False, enum=('gaussian', 'binomial', 'multinomial', )),
        NodeArgMeta(name='type', kind='enum', required=False, enum=('BIC', 'AIC', 'Cp', 'cv', )),
        NodeArgMeta(name='alphas', kind='num_array', required=False),
        NodeArgMeta(name='h', kind='integer', required=False),
        NodeArgMeta(name='do_intercept', kind='boolean', required=False),
        NodeArgMeta(name='train_window', kind='integer', required=False),
        NodeArgMeta(name='test_window', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=False),
        ),
        defaults={'h': 0, 'do_intercept': True, 'seed': 1},
    ),
    'snt_sentiment': NodeMeta(
        fn='snt_sentiment',
        category='26-text-as-data',
        card_id=234,
        contract_hash='c2-f3f821e5bc2a1964345038b213637e75743e88007d03acf7413555e5653cf07c',
        register_field='sentiment',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='corpus', kind='raw_handle', required=True),
        NodeArgMeta(name='lexicons', kind='series_codes', required=False),
        NodeArgMeta(name='how', kind='enum', required=False, enum=('proportional', 'counts', 'proportionalPol', 'proportionalSquareRoot', 'UShaped', 'inverseUShaped', 'exponential', 'inverseExponential', 'TFIDF', )),
        ),
        defaults={},
    ),
    'tx_preprocess': NodeMeta(
        fn='tx_preprocess',
        category='26-text-as-data',
        card_id=579,
        contract_hash='c2-01981f38da9ed3ef9bc54b47abf3d8ff27fba66256243bb7ef8a6140a7c673ee',
        register_field='dtm',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='documents', kind='df_handle', required=True),
        NodeArgMeta(name='text', kind='string', required=True),
        NodeArgMeta(name='normalise', kind='enum', required=False, enum=('none', 'stem', 'lemmatise', )),
        NodeArgMeta(name='stop_words', kind='series_codes', required=False),
        NodeArgMeta(name='ngram_range', kind='int_array', required=False),
        NodeArgMeta(name='min_df', kind='number', required=False),
        NodeArgMeta(name='max_df', kind='number', required=False),
        NodeArgMeta(name='weighting', kind='enum', required=False, enum=('count', 'tfidf', 'binary', 'log_count', )),
        ),
        defaults={'normalise': 'lemmatise', 'ngram_range': [1, 2], 'min_df': 0.01, 'max_df': 0.95, 'weighting': 'tfidf'},
    ),
    'tx_topic_model': NodeMeta(
        fn='tx_topic_model',
        category='26-text-as-data',
        card_id=580,
        contract_hash='c2-bc68e44e0435f047138cbab3066ae02baf02bb76ec6537c13fdbf2626e561d5b',
        register_field='fit',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='dtm', kind='raw_handle', required=True),
        NodeArgMeta(name='n_topics', kind='integer', required=False),
        NodeArgMeta(name='model', kind='enum', required=False, enum=('lda', 'ctm', 'dmr', 'dtm', 'hdp', )),
        NodeArgMeta(name='time', kind='series_handle', required=False),
        NodeArgMeta(name='iterations', kind='integer', required=False),
        NodeArgMeta(name='n_seeds', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=True),
        ),
        defaults={'n_topics': 20, 'model': 'lda', 'iterations': 1000, 'n_seeds': 1},
    ),
    'tx_topic_coherence': NodeMeta(
        fn='tx_topic_coherence',
        category='26-text-as-data',
        card_id=580,
        contract_hash='c2-02d363f5ccd520edbcdba62fa808874341c0099568ce5bd6bb4900058d5b4898',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='dtm', kind='raw_handle', required=True),
        NodeArgMeta(name='topic_range', kind='int_array', required=False),
        NodeArgMeta(name='measure', kind='enum', required=False, enum=('c_v', 'u_mass', 'c_npmi', 'perplexity', )),
        NodeArgMeta(name='seed', kind='integer', required=True),
        ),
        defaults={'topic_range': [5, 10, 20, 30, 50], 'measure': 'c_v'},
    ),
    'tx_matrix_topics': NodeMeta(
        fn='tx_matrix_topics',
        category='26-text-as-data',
        card_id=581,
        contract_hash='c2-371137c07802fbd496428cee57fbc916055a1e3d9f70c17ff0aab48e74c4bcd3',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='dtm', kind='raw_handle', required=True),
        NodeArgMeta(name='n_components', kind='integer', required=False),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('nmf', 'lsa', 'pca', )),
        NodeArgMeta(name='init', kind='enum', required=False, enum=('random', 'nndsvd', 'nndsvda', )),
        NodeArgMeta(name='seed', kind='integer', required=True),
        ),
        defaults={'n_components': 20, 'method': 'nmf', 'init': 'nndsvd'},
    ),
    'tx_embeddings': NodeMeta(
        fn='tx_embeddings',
        category='26-text-as-data',
        card_id=582,
        contract_hash='c2-a0a03885d176f831b59b922b76ae125b7350b39ae0923b3de99a433c2266d2b9',
        register_field='model',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='documents', kind='df_handle', required=True),
        NodeArgMeta(name='text', kind='string', required=True),
        NodeArgMeta(name='model', kind='enum', required=False, enum=('word2vec', 'fasttext', 'doc2vec', )),
        NodeArgMeta(name='dimensions', kind='integer', required=False),
        NodeArgMeta(name='window', kind='integer', required=False),
        NodeArgMeta(name='min_count', kind='integer', required=False),
        NodeArgMeta(name='epochs', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=True),
        ),
        defaults={'model': 'word2vec', 'dimensions': 100, 'window': 5, 'min_count': 5, 'epochs': 10},
    ),
    'tx_similarity': NodeMeta(
        fn='tx_similarity',
        category='26-text-as-data',
        card_id=582,
        contract_hash='c2-110eb68a450dd59f400a8b30d8be1957877765594d98719f167643a33f52a305',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='model', kind='raw_handle', required=True),
        NodeArgMeta(name='terms', kind='series_codes', required=True),
        NodeArgMeta(name='top_n', kind='integer', required=False),
        ),
        defaults={'top_n': 10},
    ),
    'tx_news_index': NodeMeta(
        fn='tx_news_index',
        category='26-text-as-data',
        card_id=583,
        contract_hash='c2-9e2f5c1d7d1ecbc87de67425cc2792e9eede1cf968ff764be54e35199728ad5d',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='documents', kind='df_handle', required=True),
        NodeArgMeta(name='text', kind='string', required=True),
        NodeArgMeta(name='date', kind='string', required=True),
        NodeArgMeta(name='terms', kind='raw', required=True),
        NodeArgMeta(name='normalise_by', kind='enum', required=False, enum=('none', 'article_count', 'word_count', )),
        NodeArgMeta(name='frequency', kind='enum', required=False, enum=('daily', 'weekly', 'monthly', 'quarterly', )),
        NodeArgMeta(name='standardise', kind='boolean', required=False),
        ),
        defaults={'normalise_by': 'article_count', 'frequency': 'monthly', 'standardise': True},
    ),
    'tx_lexicon_sentiment': NodeMeta(
        fn='tx_lexicon_sentiment',
        category='26-text-as-data',
        card_id=584,
        contract_hash='c2-0219bf595b57b8ed058e87833ee396222988c379bc3f37a123bda287b6c99e08',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='documents', kind='df_handle', required=True),
        NodeArgMeta(name='text', kind='string', required=True),
        NodeArgMeta(name='lexicon', kind='enum', required=False, enum=('loughran_mcdonald', 'vader', 'harvard_iv', 'custom', )),
        NodeArgMeta(name='custom_lexicon', kind='df_handle', required=False),
        NodeArgMeta(name='negation', kind='boolean', required=False),
        NodeArgMeta(name='normalise', kind='enum', required=False, enum=('none', 'word_count', 'sentence_count', )),
        ),
        defaults={'lexicon': 'loughran_mcdonald', 'negation': True, 'normalise': 'word_count'},
    ),
    'tx_readability': NodeMeta(
        fn='tx_readability',
        category='26-text-as-data',
        card_id=585,
        contract_hash='c2-df9d763fc8b706c02eefdc70f7b2683267c83886052f344934d8029e4b6c1ba8',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='documents', kind='df_handle', required=True),
        NodeArgMeta(name='text', kind='string', required=True),
        NodeArgMeta(name='indices', kind='series_codes', required=False),
        NodeArgMeta(name='standardise_length', kind='boolean', required=False),
        ),
        defaults={'standardise_length': True},
    ),
}

#: Argument defaults, for FORM PREFILL ONLY. A default must never be sent
#: explicitly on the wire: adapt_args assigns it RAW, bypassing coercion.
DEFAULTS: dict[str, dict[str, object]] = {
    'snt_corpus': {'do_clean': False},
    'snt_measures': {'lag': 1, 'do_ignore_zeros': True},
    'snt_model': {'h': 0, 'do_intercept': True, 'seed': 1},
    'snt_sentiment': {},
    'tx_preprocess': {'normalise': 'lemmatise', 'ngram_range': [1, 2], 'min_df': 0.01, 'max_df': 0.95, 'weighting': 'tfidf'},
    'tx_topic_model': {'n_topics': 20, 'model': 'lda', 'iterations': 1000, 'n_seeds': 1},
    'tx_topic_coherence': {'topic_range': [5, 10, 20, 30, 50], 'measure': 'c_v'},
    'tx_matrix_topics': {'n_components': 20, 'method': 'nmf', 'init': 'nndsvd'},
    'tx_embeddings': {'model': 'word2vec', 'dimensions': 100, 'window': 5, 'min_count': 5, 'epochs': 10},
    'tx_similarity': {'top_n': 10},
    'tx_news_index': {'normalise_by': 'article_count', 'frequency': 'monthly', 'standardise': True},
    'tx_lexicon_sentiment': {'lexicon': 'loughran_mcdonald', 'negation': True, 'normalise': 'word_count'},
    'tx_readability': {'standardise_length': True},
}


@cache
def wire_model(fn: str) -> type[BaseModel]:
    """The model the ENGINE validates. Built on first use and cached."""
    return build_wire_model(NODE_META[fn])


@cache
def authoring_model(fn: str) -> type[BaseModel]:
    """The model a GRAPH EDITOR edits. Built on first use and cached."""
    return build_authoring_model(NODE_META[fn])
