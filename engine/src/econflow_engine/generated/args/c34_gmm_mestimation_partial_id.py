# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 2 for category 34-gmm-mestimation-partial-id -- 15 nodes. No descriptions."""

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
    'gme_fit': NodeMeta(
        fn='gme_fit',
        category='34-gmm-mestimation-partial-id',
        card_id=292,
        contract_hash='c2-46ddfb94d38fd5c6e76b4c4efdcc02440abf156c84a3705f30317643262dcf4c',
        register_field='fit',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='moments', kind='formula', required=True),
        NodeArgMeta(name='instruments', kind='series_codes', required=False),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('onestep', 'twostep', 'iterated', 'cue', )),
        NodeArgMeta(name='weighting', kind='enum', required=False, enum=('identity', 'robust', 'hac', 'cluster', )),
        NodeArgMeta(name='max_iter', kind='integer', required=False),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'method': 'twostep', 'weighting': 'robust', 'max_iter': 100, 'conf_level': 0.95},
    ),
    'gme_j_test': NodeMeta(
        fn='gme_j_test',
        category='34-gmm-mestimation-partial-id',
        card_id=292,
        contract_hash='c2-f10204ccbf8922fcfc0ef775c67926330dd8f0f479c78f77831b153ee27ce311',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='fit', kind='raw_handle', required=True),
        NodeArgMeta(name='alpha', kind='number', required=False),
        ),
        defaults={'alpha': 0.05},
    ),
    'gme_weighting_matrix': NodeMeta(
        fn='gme_weighting_matrix',
        category='34-gmm-mestimation-partial-id',
        card_id=293,
        contract_hash='c2-fb014ef75056937d02bb44fa4e55c316a010f91163e0fc67a7ecf9b600dcadf2',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='moments', kind='matrix_handle', required=True),
        NodeArgMeta(name='kind', kind='enum', required=False, enum=('homoskedastic', 'robust', 'hac', 'cluster', )),
        NodeArgMeta(name='kernel', kind='enum', required=False, enum=('bartlett', 'parzen', 'quadratic_spectral', 'truncated', )),
        NodeArgMeta(name='bandwidth', kind='integer', required=False),
        NodeArgMeta(name='cluster', kind='series_handle', required=False),
        ),
        defaults={'kind': 'hac', 'kernel': 'bartlett'},
    ),
    'gme_c_test': NodeMeta(
        fn='gme_c_test',
        category='34-gmm-mestimation-partial-id',
        card_id=294,
        contract_hash='c2-3c464ef29d1e1ae33505a6ca916ee2e535900d545c2a0e6938c468964d13fcee',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='fit', kind='raw_handle', required=True),
        NodeArgMeta(name='subset', kind='series_codes', required=True),
        NodeArgMeta(name='alpha', kind='number', required=False),
        ),
        defaults={'alpha': 0.05},
    ),
    'gme_moment_selection': NodeMeta(
        fn='gme_moment_selection',
        category='34-gmm-mestimation-partial-id',
        card_id=294,
        contract_hash='c2-b3b3bb5cf085ab57b1c532ea68ebfcbc4a33d1961184ed385de09d629aaafc31',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='moments', kind='formula', required=True),
        NodeArgMeta(name='candidates', kind='series_codes', required=False),
        NodeArgMeta(name='criterion', kind='enum', required=False, enum=('aic', 'bic', 'hqic', )),
        ),
        defaults={'criterion': 'bic'},
    ),
    'gme_minimum_distance': NodeMeta(
        fn='gme_minimum_distance',
        category='34-gmm-mestimation-partial-id',
        card_id=295,
        contract_hash='c2-e1ab265b2181a1ecce175db2a589a4e1e737b2cc46225d5401be0c4777f384ca',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='reduced_form', kind='num_array', required=True),
        NodeArgMeta(name='vcov', kind='matrix_handle', required=True),
        NodeArgMeta(name='mapping', kind='formula', required=True),
        NodeArgMeta(name='weighting', kind='enum', required=False, enum=('efficient', 'identity', 'diagonal', )),
        NodeArgMeta(name='start', kind='num_array', required=False),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'weighting': 'efficient', 'conf_level': 0.95},
    ),
    'gme_empirical_likelihood': NodeMeta(
        fn='gme_empirical_likelihood',
        category='34-gmm-mestimation-partial-id',
        card_id=296,
        contract_hash='c2-b9ca449b604ddec22a003eac4ae229d5f3ff6cf14aad9e5374580d2ed0f67869',
        register_field='fit',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='moments', kind='formula', required=True),
        NodeArgMeta(name='family', kind='enum', required=False, enum=('el', 'et', 'cue', 'hd', )),
        NodeArgMeta(name='max_iter', kind='integer', required=False),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'family': 'el', 'max_iter': 100, 'conf_level': 0.95},
    ),
    'gme_el_test': NodeMeta(
        fn='gme_el_test',
        category='34-gmm-mestimation-partial-id',
        card_id=296,
        contract_hash='c2-b41edb72df878b33f70c801f0461b1fcc252bbc075ece7713e2b198d129fcf45',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='fit', kind='raw_handle', required=True),
        NodeArgMeta(name='restriction', kind='formula', required=True),
        NodeArgMeta(name='alpha', kind='number', required=False),
        ),
        defaults={'alpha': 0.05},
    ),
    'gme_smm': NodeMeta(
        fn='gme_smm',
        category='34-gmm-mestimation-partial-id',
        card_id=297,
        contract_hash='c2-76726dc1492bcdea49f81bc5e10d21ad83a329f60ba3e1c573cc81cc525cce32',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='heavy',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='simulator', kind='formula', required=True),
        NodeArgMeta(name='moments', kind='series_codes', required=True),
        NodeArgMeta(name='n_sim', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=True),
        NodeArgMeta(name='weighting', kind='enum', required=False, enum=('identity', 'diagonal', 'efficient', )),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'n_sim': 100, 'weighting': 'efficient', 'conf_level': 0.95},
    ),
    'gme_indirect_inference': NodeMeta(
        fn='gme_indirect_inference',
        category='34-gmm-mestimation-partial-id',
        card_id=297,
        contract_hash='c2-77053764539afd33f3d53cef3f6ccccd5aa30c5290c5dafc5497c22f43bd526a',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='heavy',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='simulator', kind='formula', required=True),
        NodeArgMeta(name='auxiliary', kind='formula', required=True),
        NodeArgMeta(name='n_sim', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=True),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'n_sim': 100, 'conf_level': 0.95},
    ),
    'gme_optimise': NodeMeta(
        fn='gme_optimise',
        category='34-gmm-mestimation-partial-id',
        card_id=298,
        contract_hash='c2-fdadcbc6d9ba8b30e24f7292b042a8eab6f8cf1791ceea02de88c5e130d39c75',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='objective', kind='formula', required=True),
        NodeArgMeta(name='start', kind='num_array', required=True),
        NodeArgMeta(name='lower', kind='num_array', required=False),
        NodeArgMeta(name='upper', kind='num_array', required=False),
        NodeArgMeta(name='algorithm', kind='enum', required=False, enum=('lbfgsb', 'nelder_mead', 'slsqp', 'trust_constr', 'differential_evolution', )),
        NodeArgMeta(name='n_starts', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=False),
        ),
        defaults={'algorithm': 'lbfgsb', 'n_starts': 1},
    ),
    'gme_numerical_derivatives': NodeMeta(
        fn='gme_numerical_derivatives',
        category='34-gmm-mestimation-partial-id',
        card_id=298,
        contract_hash='c2-c30294c0e16d2880dcd9458391e2d5df69a5eddf4b90ef5530d486f3b9855253',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='objective', kind='formula', required=True),
        NodeArgMeta(name='at', kind='num_array', required=True),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('forward', 'backward', 'central', 'richardson', )),
        NodeArgMeta(name='step', kind='number', required=False),
        ),
        defaults={'method': 'central'},
    ),
    'gme_manski_bounds': NodeMeta(
        fn='gme_manski_bounds',
        category='34-gmm-mestimation-partial-id',
        card_id=299,
        contract_hash='c2-e0dd03817c40b7c38f01c65db8f1e845fd983d61c264fc7cedf95f5381742e3a',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='outcome', kind='series_handle', required=True),
        NodeArgMeta(name='selection', kind='series_handle', required=True),
        NodeArgMeta(name='treatment', kind='series_handle', required=False),
        NodeArgMeta(name='y_min', kind='number', required=False),
        NodeArgMeta(name='y_max', kind='number', required=False),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'conf_level': 0.95},
    ),
    'gme_lee_bounds': NodeMeta(
        fn='gme_lee_bounds',
        category='34-gmm-mestimation-partial-id',
        card_id=299,
        contract_hash='c2-7eb91ccb918c4888a8185efa9ea43b677b2eb9b11d98bd871270a60592290eff',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='outcome', kind='series_handle', required=True),
        NodeArgMeta(name='treatment', kind='series_handle', required=True),
        NodeArgMeta(name='selection', kind='series_handle', required=True),
        NodeArgMeta(name='covariates', kind='series_codes', required=False),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'conf_level': 0.95},
    ),
    'gme_moment_inequality_set': NodeMeta(
        fn='gme_moment_inequality_set',
        category='34-gmm-mestimation-partial-id',
        card_id=299,
        contract_hash='c2-ead29356ce7621492c3d4e1064460a522ae0ed41d46178e9c6b8029f4768f642',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='heavy',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='inequalities', kind='formula', required=True),
        NodeArgMeta(name='grid', kind='num_array', required=False),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('subsampling', 'bootstrap', 'self_normalised', )),
        NodeArgMeta(name='nboot', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=False),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'method': 'subsampling', 'nboot': 999, 'conf_level': 0.95},
    ),
}

#: Argument defaults, for FORM PREFILL ONLY. A default must never be sent
#: explicitly on the wire: adapt_args assigns it RAW, bypassing coercion.
DEFAULTS: dict[str, dict[str, object]] = {
    'gme_fit': {'method': 'twostep', 'weighting': 'robust', 'max_iter': 100, 'conf_level': 0.95},
    'gme_j_test': {'alpha': 0.05},
    'gme_weighting_matrix': {'kind': 'hac', 'kernel': 'bartlett'},
    'gme_c_test': {'alpha': 0.05},
    'gme_moment_selection': {'criterion': 'bic'},
    'gme_minimum_distance': {'weighting': 'efficient', 'conf_level': 0.95},
    'gme_empirical_likelihood': {'family': 'el', 'max_iter': 100, 'conf_level': 0.95},
    'gme_el_test': {'alpha': 0.05},
    'gme_smm': {'n_sim': 100, 'weighting': 'efficient', 'conf_level': 0.95},
    'gme_indirect_inference': {'n_sim': 100, 'conf_level': 0.95},
    'gme_optimise': {'algorithm': 'lbfgsb', 'n_starts': 1},
    'gme_numerical_derivatives': {'method': 'central'},
    'gme_manski_bounds': {'conf_level': 0.95},
    'gme_lee_bounds': {'conf_level': 0.95},
    'gme_moment_inequality_set': {'method': 'subsampling', 'nboot': 999, 'conf_level': 0.95},
}


@cache
def wire_model(fn: str) -> type[BaseModel]:
    """The model the ENGINE validates. Built on first use and cached."""
    return build_wire_model(NODE_META[fn])


@cache
def authoring_model(fn: str) -> type[BaseModel]:
    """The model a GRAPH EDITOR edits. Built on first use and cached."""
    return build_authoring_model(NODE_META[fn])
