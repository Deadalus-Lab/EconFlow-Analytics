# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 2 for category 21-systemic-risk -- 14 nodes. No descriptions."""

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
    'build_er_model': NodeMeta(
        fn='build_er_model',
        category='21-systemic-risk',
        card_id=223,
        contract_hash='c2-a054850cbc1239ba54dbca0b22196e9bb2fb3c561598023eb522b578458eee45',
        register_field='model',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='l', kind='matrix_handle', required=True),
        NodeArgMeta(name='a', kind='matrix_handle', required=True),
        NodeArgMeta(name='targetdensity', kind='number', required=False),
        NodeArgMeta(name='seed', kind='integer', required=False),
        NodeArgMeta(name='nsamples_calib', kind='integer', required=False),
        NodeArgMeta(name='thin_calib', kind='integer', required=False),
        NodeArgMeta(name='tol', kind='number', required=False),
        ),
        defaults={},
    ),
    'nrm_contagion': NodeMeta(
        fn='nrm_contagion',
        category='21-systemic-risk',
        card_id=222,
        contract_hash='c2-71e09e90c87e4b4297ef4e299c524c02c69a0826e61f7af678d71e239c794ddf',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='exposures', kind='matrix_handle', required=True),
        NodeArgMeta(name='buffer', kind='matrix_handle', required=True),
        NodeArgMeta(name='weights', kind='matrix_handle', required=False),
        NodeArgMeta(name='shock', kind='raw', required=False),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('debtrank', 'threshold', )),
        NodeArgMeta(name='exposure_type', kind='enum', required=False, enum=('assets', 'liabilities', )),
        NodeArgMeta(name='max_it', kind='integer', required=False),
        NodeArgMeta(name='single_hit', kind='boolean', required=False),
        ),
        defaults={},
    ),
    'nrm_reconstruct_matrix': NodeMeta(
        fn='nrm_reconstruct_matrix',
        category='21-systemic-risk',
        card_id=222,
        contract_hash='c2-cb885d0bfa41e123656d578260caabda475b5ab8dddba2650fb7d0ef3187c0de',
        register_field='exposure_matrix',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='rowsums', kind='matrix_handle', required=True),
        NodeArgMeta(name='colsums', kind='matrix_handle', required=True),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('me', 'md', )),
        NodeArgMeta(name='seed', kind='integer', required=False),
        NodeArgMeta(name='max_it', kind='integer', required=False),
        NodeArgMeta(name='abs_tol', kind='number', required=False),
        NodeArgMeta(name='md_c', kind='number', required=False),
        NodeArgMeta(name='md_lambda', kind='number', required=False),
        NodeArgMeta(name='md_k', kind='integer', required=False),
        NodeArgMeta(name='md_theta', kind='number', required=False),
        NodeArgMeta(name='md_remove_prob', kind='number', required=False),
        ),
        defaults={},
    ),
    'sample_interbank_network': NodeMeta(
        fn='sample_interbank_network',
        category='21-systemic-risk',
        card_id=223,
        contract_hash='c2-cebf83aa48bc3b8315368238b5b7573a5b6d6655ad476628b89380dc8318ecdd',
        register_field='samples',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='mcmc',
        args=(
        NodeArgMeta(name='l', kind='matrix_handle', required=True),
        NodeArgMeta(name='a', kind='matrix_handle', required=True),
        NodeArgMeta(name='model', kind='raw_handle', required=True),
        NodeArgMeta(name='nsamples', kind='integer', required=False),
        NodeArgMeta(name='thin', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=False),
        NodeArgMeta(name='matrpertheta', kind='integer', required=False),
        NodeArgMeta(name='burnin', kind='integer', required=False),
        NodeArgMeta(name='probs', kind='num_array', required=False),
        NodeArgMeta(name='tol', kind='number', required=False),
        ),
        defaults={},
    ),
    'sys_correlation_network_measures': NodeMeta(
        fn='sys_correlation_network_measures',
        category='21-systemic-risk',
        card_id=221,
        contract_hash='c2-392d0c02067091f1af894de246734689b6ef9c14dacd493e4e29b42d62383e6f',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='returns', kind='matrix_handle', required=True),
        NodeArgMeta(name='seed', kind='integer', required=False),
        ),
        defaults={},
    ),
    'sys_covar_delta_covar': NodeMeta(
        fn='sys_covar_delta_covar',
        category='21-systemic-risk',
        card_id=221,
        contract_hash='c2-d2b43e9e0348a60bbcfcf03487911b5eb91058f49bcd574758d366474ac98c20',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='returns', kind='matrix_handle', required=True),
        ),
        defaults={},
    ),
    'sys_covar_delta_covar_t': NodeMeta(
        fn='sys_covar_delta_covar_t',
        category='21-systemic-risk',
        card_id=221,
        contract_hash='c2-5356af0c2e97647ea5fa9e9e93a4bfcc4b7a0087fb3a80a3367ef1c8f14f14fe',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='returns', kind='matrix_handle', required=True),
        NodeArgMeta(name='state_variables', kind='matrix_handle', required=True),
        ),
        defaults={},
    ),
    'sys_scale': NodeMeta(
        fn='sys_scale',
        category='21-systemic-risk',
        card_id=221,
        contract_hash='c2-0a70ec6600c01923ca54df8e0eaae198a94bc84032546c983e23eb71dfadb0e9',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='x', kind='matrix_handle', required=True),
        ),
        defaults={},
    ),
    'sr_mes_srisk': NodeMeta(
        fn='sr_mes_srisk',
        category='21-systemic-risk',
        card_id=553,
        contract_hash='c2-85e262de8e2c998f91c89c457aac68f3639d10e7f3a2c760eae795ecafb939d3',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='returns', kind='df_handle', required=True),
        NodeArgMeta(name='market', kind='series_handle', required=True),
        NodeArgMeta(name='liabilities', kind='series_handle', required=False),
        NodeArgMeta(name='market_cap', kind='series_handle', required=False),
        NodeArgMeta(name='crisis_decline', kind='number', required=False),
        NodeArgMeta(name='prudential_ratio', kind='number', required=False),
        NodeArgMeta(name='horizon', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=True),
        ),
        defaults={'crisis_decline': 0.4, 'prudential_ratio': 0.08, 'horizon': 126},
    ),
    'sr_absorption_ratio': NodeMeta(
        fn='sr_absorption_ratio',
        category='21-systemic-risk',
        card_id=554,
        contract_hash='c2-1ca8ccc2920aa3f168aa2d94cbe9903899a5905005a121cb939308380bb39f0e',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='returns', kind='df_handle', required=True),
        NodeArgMeta(name='n_components', kind='integer', required=False),
        NodeArgMeta(name='window', kind='integer', required=False),
        NodeArgMeta(name='short_window', kind='integer', required=False),
        ),
        defaults={'window': 500, 'short_window': 15},
    ),
    'sr_granger_network': NodeMeta(
        fn='sr_granger_network',
        category='21-systemic-risk',
        card_id=555,
        contract_hash='c2-243547f1a450e09c8ee981996ab6227f7d4040e6768e51d9761f392c07ca64ae',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='returns', kind='df_handle', required=True),
        NodeArgMeta(name='lags', kind='integer', required=False),
        NodeArgMeta(name='adjust', kind='enum', required=False, enum=('none', 'bonferroni', 'holm', 'fdr', )),
        NodeArgMeta(name='window', kind='integer', required=False),
        NodeArgMeta(name='alpha', kind='number', required=False),
        ),
        defaults={'lags': 1, 'adjust': 'fdr', 'alpha': 0.05},
    ),
    'sr_network_topology': NodeMeta(
        fn='sr_network_topology',
        category='21-systemic-risk',
        card_id=555,
        contract_hash='c2-e5882203d9fc1fb55a7b2ac970c79024baba8a03c4d15bf461570f7ac5879731',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='adjacency', kind='matrix_handle', required=True),
        NodeArgMeta(name='measures', kind='series_codes', required=False),
        ),
        defaults={},
    ),
    'sr_stress_index': NodeMeta(
        fn='sr_stress_index',
        category='21-systemic-risk',
        card_id=556,
        contract_hash='c2-55f1e713956d0e93f44b6906039e86ca96738d4ae559d091bd978fe108a16fdf',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='indicators', kind='df_handle', required=True),
        NodeArgMeta(name='segments', kind='series_codes', required=False),
        NodeArgMeta(name='transform', kind='enum', required=False, enum=('empirical_cdf', 'standardise', 'rank', )),
        NodeArgMeta(name='recursive', kind='boolean', required=False),
        NodeArgMeta(name='correlation_window', kind='integer', required=False),
        ),
        defaults={'transform': 'empirical_cdf', 'recursive': True, 'correlation_window': 250},
    ),
    'sr_correlation_filter': NodeMeta(
        fn='sr_correlation_filter',
        category='21-systemic-risk',
        card_id=557,
        contract_hash='c2-68692349c70c6e6f5a20cf6843abc7e8cc0f8d5f59f94c8d86db5da190bec5ee',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='correlation', kind='matrix_handle', required=True),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('mst', 'pmfg', 'threshold', 'knn', )),
        NodeArgMeta(name='threshold', kind='number', required=False),
        NodeArgMeta(name='metric', kind='enum', required=False, enum=('sqrt_2_1_minus_rho', 'one_minus_abs', 'angular', )),
        ),
        defaults={'method': 'mst', 'threshold': 0.5, 'metric': 'sqrt_2_1_minus_rho'},
    ),
}

#: Argument defaults, for FORM PREFILL ONLY. A default must never be sent
#: explicitly on the wire: adapt_args assigns it RAW, bypassing coercion.
DEFAULTS: dict[str, dict[str, object]] = {
    'build_er_model': {},
    'nrm_contagion': {},
    'nrm_reconstruct_matrix': {},
    'sample_interbank_network': {},
    'sys_correlation_network_measures': {},
    'sys_covar_delta_covar': {},
    'sys_covar_delta_covar_t': {},
    'sys_scale': {},
    'sr_mes_srisk': {'crisis_decline': 0.4, 'prudential_ratio': 0.08, 'horizon': 126},
    'sr_absorption_ratio': {'window': 500, 'short_window': 15},
    'sr_granger_network': {'lags': 1, 'adjust': 'fdr', 'alpha': 0.05},
    'sr_network_topology': {},
    'sr_stress_index': {'transform': 'empirical_cdf', 'recursive': True, 'correlation_window': 250},
    'sr_correlation_filter': {'method': 'mst', 'threshold': 0.5, 'metric': 'sqrt_2_1_minus_rho'},
}


@cache
def wire_model(fn: str) -> type[BaseModel]:
    """The model the ENGINE validates. Built on first use and cached."""
    return build_wire_model(NODE_META[fn])


@cache
def authoring_model(fn: str) -> type[BaseModel]:
    """The model a GRAPH EDITOR edits. Built on first use and cached."""
    return build_authoring_model(NODE_META[fn])
