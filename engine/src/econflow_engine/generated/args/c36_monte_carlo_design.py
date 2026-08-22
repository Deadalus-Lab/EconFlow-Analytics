# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 2 for category 36-monte-carlo-design -- 16 nodes. No descriptions."""

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
    'mc_simulate_arma': NodeMeta(
        fn='mc_simulate_arma',
        category='36-monte-carlo-design',
        card_id=309,
        contract_hash='c2-8e8042a696fd4595367f00cfa9cd8741491490a91942155242d105425871a32f',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='mcmc',
        args=(
        NodeArgMeta(name='n', kind='integer', required=True),
        NodeArgMeta(name='ar', kind='num_array', required=False),
        NodeArgMeta(name='ma', kind='num_array', required=False),
        NodeArgMeta(name='d', kind='integer', required=False),
        NodeArgMeta(name='sigma', kind='number', required=False),
        NodeArgMeta(name='burnin', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=True),
        ),
        defaults={'d': 0, 'sigma': 1.0, 'burnin': 500},
    ),
    'mc_simulate_var': NodeMeta(
        fn='mc_simulate_var',
        category='36-monte-carlo-design',
        card_id=309,
        contract_hash='c2-a6866bdd91829bd96bed8371da535adb09f35117d893fae545dee602ecdae0d0',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='mcmc',
        args=(
        NodeArgMeta(name='n', kind='integer', required=True),
        NodeArgMeta(name='coefs', kind='matrix_handle', required=True),
        NodeArgMeta(name='sigma', kind='matrix_handle', required=True),
        NodeArgMeta(name='burnin', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=True),
        ),
        defaults={'burnin': 500},
    ),
    'mc_simulate_garch': NodeMeta(
        fn='mc_simulate_garch',
        category='36-monte-carlo-design',
        card_id=309,
        contract_hash='c2-4e1b3ed8f93d052154981c49798e9ac3b8ef71a3b7db11e10c2ca2dc9aa38902',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='n', kind='integer', required=True),
        NodeArgMeta(name='omega', kind='number', required=True),
        NodeArgMeta(name='alpha', kind='num_array', required=True),
        NodeArgMeta(name='beta', kind='num_array', required=True),
        NodeArgMeta(name='distribution', kind='enum', required=False, enum=('normal', 't', 'skewt', 'ged', )),
        NodeArgMeta(name='seed', kind='integer', required=True),
        ),
        defaults={'distribution': 'normal'},
    ),
    'mc_simulate_panel': NodeMeta(
        fn='mc_simulate_panel',
        category='36-monte-carlo-design',
        card_id=309,
        contract_hash='c2-a941870cf18d0fb685e865975059ed3fe7f4be10e167dc036c14ff249116f897',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='n_units', kind='integer', required=True),
        NodeArgMeta(name='n_periods', kind='integer', required=True),
        NodeArgMeta(name='beta', kind='num_array', required=True),
        NodeArgMeta(name='unit_sd', kind='number', required=False),
        NodeArgMeta(name='time_sd', kind='number', required=False),
        NodeArgMeta(name='seed', kind='integer', required=True),
        ),
        defaults={'unit_sd': 1.0, 'time_sd': 0.5},
    ),
    'mc_size_study': NodeMeta(
        fn='mc_size_study',
        category='36-monte-carlo-design',
        card_id=310,
        contract_hash='c2-cdaec6f3d382340e913083dc2975ccc5b1967fb023b08d3cf8340f63c48c5492',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='dgp', kind='formula', required=True),
        NodeArgMeta(name='test', kind='formula', required=True),
        NodeArgMeta(name='n_replications', kind='integer', required=False),
        NodeArgMeta(name='sample_sizes', kind='int_array', required=False),
        NodeArgMeta(name='seed', kind='integer', required=True),
        NodeArgMeta(name='alpha', kind='number', required=False),
        ),
        defaults={'n_replications': 1000, 'sample_sizes': [50, 100, 250, 500], 'alpha': 0.05},
    ),
    'mc_power_study': NodeMeta(
        fn='mc_power_study',
        category='36-monte-carlo-design',
        card_id=310,
        contract_hash='c2-fc57037aae8ef8c1202faaa40be601bd6005c0666127bb7183d8c1aea72fc496',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='dgp', kind='formula', required=True),
        NodeArgMeta(name='test', kind='formula', required=True),
        NodeArgMeta(name='effect_grid', kind='num_array', required=True),
        NodeArgMeta(name='n_replications', kind='integer', required=False),
        NodeArgMeta(name='size_correct', kind='boolean', required=False),
        NodeArgMeta(name='seed', kind='integer', required=True),
        NodeArgMeta(name='alpha', kind='number', required=False),
        ),
        defaults={'n_replications': 1000, 'size_correct': True, 'alpha': 0.05},
    ),
    'mc_coverage_study': NodeMeta(
        fn='mc_coverage_study',
        category='36-monte-carlo-design',
        card_id=311,
        contract_hash='c2-288ec55156fb8cdde98765cc6ab5f339b674d34f9e1d14a3545a0e8cbee04f00',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='dgp', kind='formula', required=True),
        NodeArgMeta(name='procedure', kind='formula', required=True),
        NodeArgMeta(name='levels', kind='num_array', required=False),
        NodeArgMeta(name='n_replications', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=True),
        ),
        defaults={'levels': [0.8, 0.9, 0.95], 'n_replications': 1000},
    ),
    'mc_pit': NodeMeta(
        fn='mc_pit',
        category='36-monte-carlo-design',
        card_id=311,
        contract_hash='c2-263fe0e964ec9b818073a9f18ead7a59c4a3093a77ad2a368e8ead2d5690d969',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='observed', kind='series_handle', required=True),
        NodeArgMeta(name='predictive_cdf', kind='matrix_handle', required=True),
        NodeArgMeta(name='test', kind='enum', required=False, enum=('ks', 'ad', 'cvm', 'berkowitz', )),
        ),
        defaults={'test': 'ks'},
    ),
    'mc_sobol': NodeMeta(
        fn='mc_sobol',
        category='36-monte-carlo-design',
        card_id=312,
        contract_hash='c2-a986ba0f78ea71d6d8700bffeb8d4eb93fad16c3529af8e45f01bbd9f0fc672e',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='problem', kind='df_handle', required=True),
        NodeArgMeta(name='outputs', kind='series_handle', required=True),
        NodeArgMeta(name='n_samples', kind='integer', required=False),
        NodeArgMeta(name='calc_second_order', kind='boolean', required=False),
        NodeArgMeta(name='seed', kind='integer', required=True),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'n_samples': 1024, 'calc_second_order': False, 'conf_level': 0.95},
    ),
    'mc_morris': NodeMeta(
        fn='mc_morris',
        category='36-monte-carlo-design',
        card_id=312,
        contract_hash='c2-753486e30c98a41d1e8a54021e70711542b1b073ef5539be30512228752ad9f0',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='problem', kind='df_handle', required=True),
        NodeArgMeta(name='outputs', kind='series_handle', required=True),
        NodeArgMeta(name='n_trajectories', kind='integer', required=False),
        NodeArgMeta(name='levels', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=True),
        ),
        defaults={'n_trajectories': 100, 'levels': 4},
    ),
    'mc_sample_design': NodeMeta(
        fn='mc_sample_design',
        category='36-monte-carlo-design',
        card_id=312,
        contract_hash='c2-77912920d8254964305624d7ef82d2fb719686be0095818a91cfb9971dba8c88',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='problem', kind='df_handle', required=True),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('sobol', 'morris', 'fast', 'latin_hypercube', 'finite_diff', )),
        NodeArgMeta(name='n_samples', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=True),
        ),
        defaults={'method': 'sobol', 'n_samples': 1024},
    ),
    'mc_design_generate': NodeMeta(
        fn='mc_design_generate',
        category='36-monte-carlo-design',
        card_id=313,
        contract_hash='c2-6f95fe2899be8fae1b5f29d75dfaa993872fee5c98fcc1b39cf280073b0ad761',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='n_factors', kind='integer', required=True),
        NodeArgMeta(name='design', kind='enum', required=False, enum=('lhs', 'full_factorial', 'fractional_factorial', 'box_behnken', 'central_composite', 'plackett_burman', )),
        NodeArgMeta(name='n_samples', kind='integer', required=False),
        NodeArgMeta(name='levels', kind='int_array', required=False),
        NodeArgMeta(name='criterion', kind='enum', required=False, enum=('maximin', 'centermaximin', 'correlation', 'none', )),
        NodeArgMeta(name='seed', kind='integer', required=True),
        ),
        defaults={'design': 'lhs', 'n_samples': 100, 'criterion': 'maximin'},
    ),
    'mc_power': NodeMeta(
        fn='mc_power',
        category='36-monte-carlo-design',
        card_id=314,
        contract_hash='c2-fe2729fc58c3988c1f195ed6f02c8aa8e7ea8b0ee22bf1b0a00fc92f1983ae04',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='solve_for', kind='enum', required=False, enum=('n', 'power', 'effect', )),
        NodeArgMeta(name='effect_size', kind='number', required=False),
        NodeArgMeta(name='n', kind='integer', required=False),
        NodeArgMeta(name='power', kind='number', required=False),
        NodeArgMeta(name='ratio', kind='number', required=False),
        NodeArgMeta(name='alpha', kind='number', required=False),
        ),
        defaults={'solve_for': 'n', 'power': 0.8, 'ratio': 1.0, 'alpha': 0.05},
    ),
    'mc_power_cluster': NodeMeta(
        fn='mc_power_cluster',
        category='36-monte-carlo-design',
        card_id=314,
        contract_hash='c2-cee8dc26116439e4776ab964dfc2ea9c24f87b04ac3113e2e47365188a2b8e91',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='n_clusters', kind='integer', required=False),
        NodeArgMeta(name='cluster_size', kind='integer', required=True),
        NodeArgMeta(name='icc', kind='number', required=True),
        NodeArgMeta(name='effect_size', kind='number', required=False),
        NodeArgMeta(name='power', kind='number', required=False),
        NodeArgMeta(name='solve_for', kind='enum', required=False, enum=('n_clusters', 'power', 'effect', )),
        NodeArgMeta(name='alpha', kind='number', required=False),
        ),
        defaults={'power': 0.8, 'solve_for': 'n_clusters', 'alpha': 0.05},
    ),
    'mc_qmc_sample': NodeMeta(
        fn='mc_qmc_sample',
        category='36-monte-carlo-design',
        card_id=315,
        contract_hash='c2-0c2377c5b28066424074ec66644d828515a5715b5ef5fb623b0a8ff029c18700',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='n_dimensions', kind='integer', required=True),
        NodeArgMeta(name='n_samples', kind='integer', required=True),
        NodeArgMeta(name='sequence', kind='enum', required=False, enum=('sobol', 'halton', 'latin_hypercube', 'poisson_disk', )),
        NodeArgMeta(name='scramble', kind='boolean', required=False),
        NodeArgMeta(name='seed', kind='integer', required=True),
        ),
        defaults={'sequence': 'sobol', 'scramble': True},
    ),
    'mc_discrepancy': NodeMeta(
        fn='mc_discrepancy',
        category='36-monte-carlo-design',
        card_id=315,
        contract_hash='c2-3394a4c67675fdb55e975f3825879d5b309f60adc2dbfca25b5e06f1c1c8c9f0',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='sample', kind='matrix_handle', required=True),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('cd', 'wd', 'md', 'l2_star', )),
        ),
        defaults={'method': 'cd'},
    ),
}

#: Argument defaults, for FORM PREFILL ONLY. A default must never be sent
#: explicitly on the wire: adapt_args assigns it RAW, bypassing coercion.
DEFAULTS: dict[str, dict[str, object]] = {
    'mc_simulate_arma': {'d': 0, 'sigma': 1.0, 'burnin': 500},
    'mc_simulate_var': {'burnin': 500},
    'mc_simulate_garch': {'distribution': 'normal'},
    'mc_simulate_panel': {'unit_sd': 1.0, 'time_sd': 0.5},
    'mc_size_study': {'n_replications': 1000, 'sample_sizes': [50, 100, 250, 500], 'alpha': 0.05},
    'mc_power_study': {'n_replications': 1000, 'size_correct': True, 'alpha': 0.05},
    'mc_coverage_study': {'levels': [0.8, 0.9, 0.95], 'n_replications': 1000},
    'mc_pit': {'test': 'ks'},
    'mc_sobol': {'n_samples': 1024, 'calc_second_order': False, 'conf_level': 0.95},
    'mc_morris': {'n_trajectories': 100, 'levels': 4},
    'mc_sample_design': {'method': 'sobol', 'n_samples': 1024},
    'mc_design_generate': {'design': 'lhs', 'n_samples': 100, 'criterion': 'maximin'},
    'mc_power': {'solve_for': 'n', 'power': 0.8, 'ratio': 1.0, 'alpha': 0.05},
    'mc_power_cluster': {'power': 0.8, 'solve_for': 'n_clusters', 'alpha': 0.05},
    'mc_qmc_sample': {'sequence': 'sobol', 'scramble': True},
    'mc_discrepancy': {'method': 'cd'},
}


@cache
def wire_model(fn: str) -> type[BaseModel]:
    """The model the ENGINE validates. Built on first use and cached."""
    return build_wire_model(NODE_META[fn])


@cache
def authoring_model(fn: str) -> type[BaseModel]:
    """The model a GRAPH EDITOR edits. Built on first use and cached."""
    return build_authoring_model(NODE_META[fn])
