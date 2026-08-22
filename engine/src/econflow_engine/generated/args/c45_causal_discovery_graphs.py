# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 2 for category 45-causal-discovery-graphs -- 13 nodes. No descriptions."""

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
    'cd_pc': NodeMeta(
        fn='cd_pc',
        category='45-causal-discovery-graphs',
        card_id=374,
        contract_hash='c2-04f0df81da729bff1e72249d0eafb716f8dce358584667683a7e376941a21e3d',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='independence_test', kind='enum', required=False, enum=('fisherz', 'chisq', 'gsq', 'kci', 'mv_fisherz', )),
        NodeArgMeta(name='stable', kind='boolean', required=False),
        NodeArgMeta(name='max_conditioning_set', kind='integer', required=False),
        NodeArgMeta(name='alpha', kind='number', required=False),
        ),
        defaults={'independence_test': 'fisherz', 'stable': True, 'alpha': 0.05},
    ),
    'cd_fci': NodeMeta(
        fn='cd_fci',
        category='45-causal-discovery-graphs',
        card_id=374,
        contract_hash='c2-1b0c18b36990689924c273a382d50a7a1aea5391422d8bf7d7207374fca4783d',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='independence_test', kind='enum', required=False, enum=('fisherz', 'chisq', 'gsq', 'kci', )),
        NodeArgMeta(name='max_conditioning_set', kind='integer', required=False),
        NodeArgMeta(name='alpha', kind='number', required=False),
        ),
        defaults={'independence_test': 'fisherz', 'alpha': 0.05},
    ),
    'cd_ges': NodeMeta(
        fn='cd_ges',
        category='45-causal-discovery-graphs',
        card_id=375,
        contract_hash='c2-461dceb9324d6837af287083ad259e9cdcbea92d18261ed86b8a5f0931f28aac',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='score', kind='enum', required=False, enum=('bic', 'bdeu', 'generalised_score', 'marginal_likelihood', )),
        NodeArgMeta(name='max_parents', kind='integer', required=False),
        ),
        defaults={'score': 'bic'},
    ),
    'cd_exact_search': NodeMeta(
        fn='cd_exact_search',
        category='45-causal-discovery-graphs',
        card_id=375,
        contract_hash='c2-4cd3c4e5d6e3532594c62dae70be864592333bc38c96107e0b2590fadb1ceeb2',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='score', kind='enum', required=False, enum=('bic', 'bdeu', )),
        NodeArgMeta(name='max_parents', kind='integer', required=False),
        ),
        defaults={'score': 'bic', 'max_parents': 3},
    ),
    'cd_lingam': NodeMeta(
        fn='cd_lingam',
        category='45-causal-discovery-graphs',
        card_id=376,
        contract_hash='c2-187ddc35a0b0edea433f9e5615d2aa2637c440abd5c9c6a517c124e53e25ad42',
        register_field='fit',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='heavy',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='variant', kind='enum', required=False, enum=('ica', 'direct', 'var', 'rcd', )),
        NodeArgMeta(name='lags', kind='integer', required=False),
        NodeArgMeta(name='nboot', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=False),
        ),
        defaults={'variant': 'direct', 'lags': 1, 'nboot': 0},
    ),
    'cd_nongaussianity_check': NodeMeta(
        fn='cd_nongaussianity_check',
        category='45-causal-discovery-graphs',
        card_id=376,
        contract_hash='c2-37960fa3b5bd9c313317c90250ae5d87b692774f16c1ff97652139a6fd59799c',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='test', kind='enum', required=False, enum=('jarque_bera', 'shapiro', 'anderson', 'dagostino', )),
        NodeArgMeta(name='alpha', kind='number', required=False),
        ),
        defaults={'test': 'jarque_bera', 'alpha': 0.05},
    ),
    'cd_identify_effect': NodeMeta(
        fn='cd_identify_effect',
        category='45-causal-discovery-graphs',
        card_id=377,
        contract_hash='c2-c3fc5f2a4821f6769413b850a58fbca3fcb52f7cfd6f16b69cd974e80094a107',
        register_field='estimand',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='graph', kind='string', required=True),
        NodeArgMeta(name='treatment', kind='string', required=True),
        NodeArgMeta(name='outcome', kind='string', required=True),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('auto', 'backdoor', 'frontdoor', 'iv', 'mediation', )),
        ),
        defaults={'method': 'auto'},
    ),
    'cd_adjustment_sets': NodeMeta(
        fn='cd_adjustment_sets',
        category='45-causal-discovery-graphs',
        card_id=377,
        contract_hash='c2-5fa21e4ec1e73209b037103cd33ed9dad09242463806c54828b8fdb5648c2ab8',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='graph', kind='string', required=True),
        NodeArgMeta(name='treatment', kind='string', required=True),
        NodeArgMeta(name='outcome', kind='string', required=True),
        NodeArgMeta(name='max_sets', kind='integer', required=False),
        ),
        defaults={'max_sets': 10},
    ),
    'cd_estimate_effect': NodeMeta(
        fn='cd_estimate_effect',
        category='45-causal-discovery-graphs',
        card_id=377,
        contract_hash='c2-533bcac81d44386e88456a1f8a5c23eb97beb9792cadf7ef1465136b14369570',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='estimand', kind='raw_handle', required=True),
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('linear_regression', 'propensity_matching', 'propensity_weighting', 'instrumental_variable', 'two_stage_regression', )),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'method': 'linear_regression', 'conf_level': 0.95},
    ),
    'cd_refute': NodeMeta(
        fn='cd_refute',
        category='45-causal-discovery-graphs',
        card_id=378,
        contract_hash='c2-46b4d23720b19408294e105345946004da4fccba06f799a9cb18aacf44013cc7',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='estimand', kind='raw_handle', required=True),
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='refuters', kind='series_codes', required=False),
        NodeArgMeta(name='n_simulations', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=True),
        ),
        defaults={'n_simulations': 100},
    ),
    'cd_sensitivity_confounder': NodeMeta(
        fn='cd_sensitivity_confounder',
        category='45-causal-discovery-graphs',
        card_id=378,
        contract_hash='c2-cb4a3884dc856799c515e7bfb5bf7387f8db5e1733eb9d8a2296e0ad6372bbf9',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='estimand', kind='raw_handle', required=True),
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='effect_strength_treatment', kind='num_array', required=False),
        NodeArgMeta(name='effect_strength_outcome', kind='num_array', required=False),
        ),
        defaults={},
    ),
    'cd_independence_test': NodeMeta(
        fn='cd_independence_test',
        category='45-causal-discovery-graphs',
        card_id=379,
        contract_hash='c2-b2c73342d765cd4586e02f147aaebe7d78fe11a9b6d1e10f3522cfcbef8c84d5',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='x', kind='multiseries_handle', required=True),
        NodeArgMeta(name='y', kind='multiseries_handle', required=True),
        NodeArgMeta(name='z', kind='multiseries_handle', required=False),
        NodeArgMeta(name='test', kind='enum', required=False, enum=('dcorr', 'hsic', 'kci', 'fisherz', 'mgc', 'hhg', )),
        NodeArgMeta(name='n_permutations', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=False),
        NodeArgMeta(name='alpha', kind='number', required=False),
        ),
        defaults={'test': 'dcorr', 'n_permutations': 1000, 'alpha': 0.05},
    ),
    'cd_distance_correlation': NodeMeta(
        fn='cd_distance_correlation',
        category='45-causal-discovery-graphs',
        card_id=379,
        contract_hash='c2-700dba4c14cd1c69f0e9c27ce7161d01ba2b8c3ba5609506a39416d5632e7ba4',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='x', kind='multiseries_handle', required=True),
        NodeArgMeta(name='y', kind='multiseries_handle', required=True),
        NodeArgMeta(name='z', kind='multiseries_handle', required=False),
        ),
        defaults={},
    ),
}

#: Argument defaults, for FORM PREFILL ONLY. A default must never be sent
#: explicitly on the wire: adapt_args assigns it RAW, bypassing coercion.
DEFAULTS: dict[str, dict[str, object]] = {
    'cd_pc': {'independence_test': 'fisherz', 'stable': True, 'alpha': 0.05},
    'cd_fci': {'independence_test': 'fisherz', 'alpha': 0.05},
    'cd_ges': {'score': 'bic'},
    'cd_exact_search': {'score': 'bic', 'max_parents': 3},
    'cd_lingam': {'variant': 'direct', 'lags': 1, 'nboot': 0},
    'cd_nongaussianity_check': {'test': 'jarque_bera', 'alpha': 0.05},
    'cd_identify_effect': {'method': 'auto'},
    'cd_adjustment_sets': {'max_sets': 10},
    'cd_estimate_effect': {'method': 'linear_regression', 'conf_level': 0.95},
    'cd_refute': {'n_simulations': 100},
    'cd_sensitivity_confounder': {},
    'cd_independence_test': {'test': 'dcorr', 'n_permutations': 1000, 'alpha': 0.05},
    'cd_distance_correlation': {},
}


@cache
def wire_model(fn: str) -> type[BaseModel]:
    """The model the ENGINE validates. Built on first use and cached."""
    return build_wire_model(NODE_META[fn])


@cache
def authoring_model(fn: str) -> type[BaseModel]:
    """The model a GRAPH EDITOR edits. Built on first use and cached."""
    return build_authoring_model(NODE_META[fn])
