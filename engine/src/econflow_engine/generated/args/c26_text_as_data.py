# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.v1.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 2 for category 26-text-as-data -- 4 nodes. No descriptions."""

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
        contract_hash='c-2b7fa928e5537c84583c29bdb447a3aef2ecf0eb865b4c2ad22b9f6d6b0e10eb',
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
        contract_hash='c-88943a2c5ffda4ef25f9d72df6c76b485d66110d905ce856b1a7cd067de0e457',
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
        contract_hash='c-28f034249260ca09c398a6519746c88c9db5399d7e7a0e8b7e4dc4883a704076',
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
        contract_hash='c-5a3f63bf8fa7c678496341542abe0070454f632b093dfd8a84dc10649409c4a9',
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
}

#: Argument defaults, for FORM PREFILL ONLY. A default must never be sent
#: explicitly on the wire: adapt_args assigns it RAW, bypassing coercion.
DEFAULTS: dict[str, dict[str, object]] = {
    'snt_corpus': {'do_clean': False},
    'snt_measures': {'lag': 1, 'do_ignore_zeros': True},
    'snt_model': {'h': 0, 'do_intercept': True, 'seed': 1},
    'snt_sentiment': {},
}


@cache
def wire_model(fn: str) -> type[BaseModel]:
    """The model the ENGINE validates. Built on first use and cached."""
    return build_wire_model(NODE_META[fn])


@cache
def authoring_model(fn: str) -> type[BaseModel]:
    """The model a GRAPH EDITOR edits. Built on first use and cached."""
    return build_authoring_model(NODE_META[fn])
