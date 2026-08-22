# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 2 for category 35-resampling-inference -- 14 nodes. No descriptions."""

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
    'rs_bootstrap_iid': NodeMeta(
        fn='rs_bootstrap_iid',
        category='35-resampling-inference',
        card_id=300,
        contract_hash='c2-ca48399d50efa37681b4512931195fae481449879a38242fcfdd9e578bf737a7',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='heavy',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='statistic', kind='formula', required=True),
        NodeArgMeta(name='nboot', kind='integer', required=False),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('percentile', 'basic', 'bca', 'percentile_t', 'studentized', )),
        NodeArgMeta(name='seed', kind='integer', required=True),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'nboot': 999, 'method': 'bca', 'conf_level': 0.95},
    ),
    'rs_bootstrap_residual': NodeMeta(
        fn='rs_bootstrap_residual',
        category='35-resampling-inference',
        card_id=300,
        contract_hash='c2-fb294910dfcaf89eb031887bae8daba9dd6191341b3c10b5adf73adb80d812e2',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='heavy',
        args=(
        NodeArgMeta(name='fit', kind='raw_handle', required=True),
        NodeArgMeta(name='nboot', kind='integer', required=False),
        NodeArgMeta(name='wild', kind='boolean', required=False),
        NodeArgMeta(name='seed', kind='integer', required=True),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'nboot': 999, 'wild': False, 'conf_level': 0.95},
    ),
    'rs_block_bootstrap': NodeMeta(
        fn='rs_block_bootstrap',
        category='35-resampling-inference',
        card_id=301,
        contract_hash='c2-8bcdf78ebadca3728d6a747d0b9341e3c9263451355a43e1a38be805d76a46d4',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='heavy',
        args=(
        NodeArgMeta(name='data', kind='multiseries_handle', required=True),
        NodeArgMeta(name='statistic', kind='formula', required=True),
        NodeArgMeta(name='block_length', kind='integer', required=False),
        NodeArgMeta(name='circular', kind='boolean', required=False),
        NodeArgMeta(name='nboot', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=True),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'circular': True, 'nboot': 999, 'conf_level': 0.95},
    ),
    'rs_optimal_block_length': NodeMeta(
        fn='rs_optimal_block_length',
        category='35-resampling-inference',
        card_id=301,
        contract_hash='c2-39ebc5ef9ea5b4d431586233a0211ac87d7d39ed7b90b8844c81d1e792b28300',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='x', kind='series_handle', required=True),
        ),
        defaults={},
    ),
    'rs_stationary_bootstrap': NodeMeta(
        fn='rs_stationary_bootstrap',
        category='35-resampling-inference',
        card_id=302,
        contract_hash='c2-71e7683e39630f3321141ea3c7516000948c52931033bc22ba9d53fcef060df5',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='heavy',
        args=(
        NodeArgMeta(name='data', kind='multiseries_handle', required=True),
        NodeArgMeta(name='statistic', kind='formula', required=True),
        NodeArgMeta(name='expected_block_length', kind='number', required=False),
        NodeArgMeta(name='nboot', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=True),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'nboot': 999, 'conf_level': 0.95},
    ),
    'rs_sieve_bootstrap': NodeMeta(
        fn='rs_sieve_bootstrap',
        category='35-resampling-inference',
        card_id=303,
        contract_hash='c2-1ff6467db47dcd037049f215fec3a3ea66605f38ecf5d3c046504172a7462e11',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='heavy',
        args=(
        NodeArgMeta(name='x', kind='series_handle', required=True),
        NodeArgMeta(name='statistic', kind='formula', required=True),
        NodeArgMeta(name='ar_order', kind='integer', required=False),
        NodeArgMeta(name='criterion', kind='enum', required=False, enum=('aic', 'bic', 'hqic', )),
        NodeArgMeta(name='nboot', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=True),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'criterion': 'aic', 'nboot': 999, 'conf_level': 0.95},
    ),
    'rs_wild_bootstrap': NodeMeta(
        fn='rs_wild_bootstrap',
        category='35-resampling-inference',
        card_id=304,
        contract_hash='c2-3ade6e6e721b3e1d8e21746bcb390dc1d4856278b4de6fd909399325b914eddc',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='heavy',
        args=(
        NodeArgMeta(name='fit', kind='raw_handle', required=True),
        NodeArgMeta(name='restriction', kind='formula', required=True),
        NodeArgMeta(name='weights', kind='enum', required=False, enum=('rademacher', 'mammen', 'webb', 'normal', )),
        NodeArgMeta(name='impose_null', kind='boolean', required=False),
        NodeArgMeta(name='nboot', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=True),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'weights': 'rademacher', 'impose_null': True, 'nboot': 999, 'conf_level': 0.95},
    ),
    'rs_wild_cluster_bootstrap': NodeMeta(
        fn='rs_wild_cluster_bootstrap',
        category='35-resampling-inference',
        card_id=305,
        contract_hash='c2-6cf250b8e7d41572974907d6b35deb1920ce35b795af47fcc0a44420cfd52f5b',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='heavy',
        args=(
        NodeArgMeta(name='fit', kind='raw_handle', required=True),
        NodeArgMeta(name='cluster', kind='series_handle', required=True),
        NodeArgMeta(name='restriction', kind='formula', required=True),
        NodeArgMeta(name='weights', kind='enum', required=False, enum=('rademacher', 'mammen', 'webb', 'normal', )),
        NodeArgMeta(name='nboot', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=True),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'weights': 'webb', 'nboot': 999, 'conf_level': 0.95},
    ),
    'rs_permutation_test': NodeMeta(
        fn='rs_permutation_test',
        category='35-resampling-inference',
        card_id=306,
        contract_hash='c2-b557caa6ce8bac62afcc201eaf41cb2ea9e8865ad25f615dce79e3a2e8c71c28',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='outcome', kind='series_handle', required=True),
        NodeArgMeta(name='treatment', kind='series_handle', required=True),
        NodeArgMeta(name='block', kind='series_handle', required=False),
        NodeArgMeta(name='cluster', kind='series_handle', required=False),
        NodeArgMeta(name='statistic', kind='enum', required=False, enum=('mean_difference', 'rank_sum', 't', 'regression_coef', )),
        NodeArgMeta(name='n_permutations', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=True),
        NodeArgMeta(name='alpha', kind='number', required=False),
        ),
        defaults={'statistic': 'mean_difference', 'n_permutations': 10000, 'alpha': 0.05},
    ),
    'rs_randomisation_ci': NodeMeta(
        fn='rs_randomisation_ci',
        category='35-resampling-inference',
        card_id=306,
        contract_hash='c2-1514e750ebdfa6d114023b4a36d90318763c6212345097281a54fd4ead44f866',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='outcome', kind='series_handle', required=True),
        NodeArgMeta(name='treatment', kind='series_handle', required=True),
        NodeArgMeta(name='grid', kind='num_array', required=False),
        NodeArgMeta(name='n_permutations', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=True),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'n_permutations': 1000, 'conf_level': 0.95},
    ),
    'rs_subsampling': NodeMeta(
        fn='rs_subsampling',
        category='35-resampling-inference',
        card_id=307,
        contract_hash='c2-442a2a3c86b61c5e04a6d7d7f4dde7e44f6ac548321af8881e0308c63bb469cf',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='statistic', kind='formula', required=True),
        NodeArgMeta(name='subsample_size', kind='integer', required=False),
        NodeArgMeta(name='n_subsamples', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=True),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'n_subsamples': 1000, 'conf_level': 0.95},
    ),
    'rs_jackknife': NodeMeta(
        fn='rs_jackknife',
        category='35-resampling-inference',
        card_id=307,
        contract_hash='c2-b1d5790bc6f05c445d18896f836975285edfebde85b4326905e1011c358a5d03',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='statistic', kind='formula', required=True),
        NodeArgMeta(name='kind', kind='enum', required=False, enum=('delete1', 'deleted', 'cluster', )),
        NodeArgMeta(name='d', kind='integer', required=False),
        NodeArgMeta(name='cluster', kind='series_handle', required=False),
        ),
        defaults={'kind': 'delete1', 'd': 1},
    ),
    'rs_multiple_testing': NodeMeta(
        fn='rs_multiple_testing',
        category='35-resampling-inference',
        card_id=308,
        contract_hash='c2-48cc4a74ec303e434103d4230a8ae4d3ff2687d28fec38ac6d332814faaa1db3',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='p_values', kind='num_array', required=True),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('bonferroni', 'holm', 'hochberg', 'bh', 'by', 'sidak', )),
        NodeArgMeta(name='alpha', kind='number', required=False),
        ),
        defaults={'method': 'holm', 'alpha': 0.05},
    ),
    'rs_romano_wolf': NodeMeta(
        fn='rs_romano_wolf',
        category='35-resampling-inference',
        card_id=308,
        contract_hash='c2-de66ab0f6fcd5bdc95505165f3e2f4be73c6a4aae8e84fc93a37f3c510b29a65',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='statistics', kind='num_array', required=True),
        NodeArgMeta(name='bootstrap_draws', kind='matrix_handle', required=True),
        NodeArgMeta(name='alpha', kind='number', required=False),
        ),
        defaults={'alpha': 0.05},
    ),
}

#: Argument defaults, for FORM PREFILL ONLY. A default must never be sent
#: explicitly on the wire: adapt_args assigns it RAW, bypassing coercion.
DEFAULTS: dict[str, dict[str, object]] = {
    'rs_bootstrap_iid': {'nboot': 999, 'method': 'bca', 'conf_level': 0.95},
    'rs_bootstrap_residual': {'nboot': 999, 'wild': False, 'conf_level': 0.95},
    'rs_block_bootstrap': {'circular': True, 'nboot': 999, 'conf_level': 0.95},
    'rs_optimal_block_length': {},
    'rs_stationary_bootstrap': {'nboot': 999, 'conf_level': 0.95},
    'rs_sieve_bootstrap': {'criterion': 'aic', 'nboot': 999, 'conf_level': 0.95},
    'rs_wild_bootstrap': {'weights': 'rademacher', 'impose_null': True, 'nboot': 999, 'conf_level': 0.95},
    'rs_wild_cluster_bootstrap': {'weights': 'webb', 'nboot': 999, 'conf_level': 0.95},
    'rs_permutation_test': {'statistic': 'mean_difference', 'n_permutations': 10000, 'alpha': 0.05},
    'rs_randomisation_ci': {'n_permutations': 1000, 'conf_level': 0.95},
    'rs_subsampling': {'n_subsamples': 1000, 'conf_level': 0.95},
    'rs_jackknife': {'kind': 'delete1', 'd': 1},
    'rs_multiple_testing': {'method': 'holm', 'alpha': 0.05},
    'rs_romano_wolf': {'alpha': 0.05},
}


@cache
def wire_model(fn: str) -> type[BaseModel]:
    """The model the ENGINE validates. Built on first use and cached."""
    return build_wire_model(NODE_META[fn])


@cache
def authoring_model(fn: str) -> type[BaseModel]:
    """The model a GRAPH EDITOR edits. Built on first use and cached."""
    return build_authoring_model(NODE_META[fn])
