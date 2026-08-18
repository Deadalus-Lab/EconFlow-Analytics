# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.v1.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 2 for category 21-systemic-risk -- 8 nodes. No descriptions."""

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
        contract_hash='c-6e74d36a90283ad2cea198b26739c4831cfb0a0f348ae86d0df29cf24c4ad492',
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
        contract_hash='c-490a4d768c10381ea5e17908099e5ecfdd676fd451d9fa97b231e9de8dac022c',
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
        contract_hash='c-c2fe4c92687a2b695547c5af3f318dff8cf09dd0a9175bc184ce15e3d2ba5133',
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
        contract_hash='c-702afce08261da844a2614bcf86a1c9da6fa1fca8329a40a8f7ace88c1a39da5',
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
    'syr_correlation_network_measures': NodeMeta(
        fn='syr_correlation_network_measures',
        category='21-systemic-risk',
        card_id=221,
        contract_hash='c-86b98d375a3ce89b0924f1c51099f3b119945283dfa3d612b0fd63311b793e9d',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='returns', kind='matrix_handle', required=True),
        NodeArgMeta(name='seed', kind='integer', required=False),
        ),
        defaults={},
    ),
    'syr_covar_delta_covar': NodeMeta(
        fn='syr_covar_delta_covar',
        category='21-systemic-risk',
        card_id=221,
        contract_hash='c-8af4615363ecb6bd54b93cca1ff8073578f6d2bc1a92ea1bb8f1157debde073c',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='returns', kind='matrix_handle', required=True),
        ),
        defaults={},
    ),
    'syr_covar_delta_covar_t': NodeMeta(
        fn='syr_covar_delta_covar_t',
        category='21-systemic-risk',
        card_id=221,
        contract_hash='c-e0254f37209b07dfbbc26d10e686823fe53189bdf55d8a3484ba523a024d5310',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='returns', kind='matrix_handle', required=True),
        NodeArgMeta(name='state_variables', kind='matrix_handle', required=True),
        ),
        defaults={},
    ),
    'syr_scale': NodeMeta(
        fn='syr_scale',
        category='21-systemic-risk',
        card_id=221,
        contract_hash='c-c599f258b42da83272ed49908bdb0ab8f37916d4ef254f9b37b7c57ae9575edc',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='x', kind='matrix_handle', required=True),
        ),
        defaults={},
    ),
}

#: Argument defaults, for FORM PREFILL ONLY. A default must never be sent
#: explicitly on the wire: adapt_args assigns it RAW, bypassing coercion.
DEFAULTS: dict[str, dict[str, object]] = {
    'build_er_model': {},
    'nrm_contagion': {},
    'nrm_reconstruct_matrix': {},
    'sample_interbank_network': {},
    'syr_correlation_network_measures': {},
    'syr_covar_delta_covar': {},
    'syr_covar_delta_covar_t': {},
    'syr_scale': {},
}


@cache
def wire_model(fn: str) -> type[BaseModel]:
    """The model the ENGINE validates. Built on first use and cached."""
    return build_wire_model(NODE_META[fn])


@cache
def authoring_model(fn: str) -> type[BaseModel]:
    """The model a GRAPH EDITOR edits. Built on first use and cached."""
    return build_authoring_model(NODE_META[fn])
