# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 2 for category 31-discrete-choice-demand -- 21 nodes. No descriptions."""

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
    'dcd_blp_problem': NodeMeta(
        fn='dcd_blp_problem',
        category='31-discrete-choice-demand',
        card_id=266,
        contract_hash='c2-b6d8dbdba437b8ad26e853653fa6b04b8100ed03d73fbcfa0cebe36d3f8d8bb5',
        register_field='problem',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='product_data', kind='df_handle', required=True),
        NodeArgMeta(name='market_ids', kind='string', required=True),
        NodeArgMeta(name='shares', kind='string', required=True),
        NodeArgMeta(name='prices', kind='string', required=True),
        NodeArgMeta(name='characteristics', kind='series_codes', required=False),
        NodeArgMeta(name='random_coefficients', kind='series_codes', required=False),
        NodeArgMeta(name='instruments', kind='series_codes', required=False),
        ),
        defaults={},
    ),
    'dcd_blp_solve': NodeMeta(
        fn='dcd_blp_solve',
        category='31-discrete-choice-demand',
        card_id=266,
        contract_hash='c2-50ee6dc1e55b37b45a53656789e8097b554894c5d7235bcea5ebb64cfea3e481',
        register_field='results',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='problem', kind='raw_handle', required=True),
        NodeArgMeta(name='sigma_init', kind='num_array', required=False),
        NodeArgMeta(name='inner_tol', kind='number', required=False),
        NodeArgMeta(name='outer_tol', kind='number', required=False),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('1s', '2s', )),
        ),
        defaults={'inner_tol': 1e-14, 'outer_tol': 1e-08, 'method': '2s'},
    ),
    'dcd_blp_shares': NodeMeta(
        fn='dcd_blp_shares',
        category='31-discrete-choice-demand',
        card_id=266,
        contract_hash='c2-7c5cbb0d100f60ab47a4377d49b6633d26f3ea9c5947737aa0691c8d35c35bba',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='results', kind='raw_handle', required=True),
        NodeArgMeta(name='prices', kind='series_handle', required=False),
        ),
        defaults={},
    ),
    'dcd_blp_instruments': NodeMeta(
        fn='dcd_blp_instruments',
        category='31-discrete-choice-demand',
        card_id=267,
        contract_hash='c2-8b18b1d201c147d330c7e8101566f7a1e1495561aac8ccf8d375fd83b3eba9cb',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='product_data', kind='df_handle', required=True),
        NodeArgMeta(name='market_ids', kind='string', required=True),
        NodeArgMeta(name='characteristics', kind='series_codes', required=False),
        NodeArgMeta(name='kind', kind='enum', required=False, enum=('blp', 'differentiation', 'local', 'quadratic', )),
        ),
        defaults={'kind': 'differentiation'},
    ),
    'dcd_optimal_instruments': NodeMeta(
        fn='dcd_optimal_instruments',
        category='31-discrete-choice-demand',
        card_id=267,
        contract_hash='c2-70765e32432959553291c2b21f6d3dcc8607b9cbc2d10385a6ab2ba7667a05bb',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='results', kind='raw_handle', required=True),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('approximate', 'monte_carlo', )),
        NodeArgMeta(name='seed', kind='integer', required=False),
        ),
        defaults={'method': 'approximate'},
    ),
    'dcd_elasticities': NodeMeta(
        fn='dcd_elasticities',
        category='31-discrete-choice-demand',
        card_id=268,
        contract_hash='c2-1dfb9ec50c3321912ed1170eb8517113b3c1e521413cbd72c5617eae10af20ff',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='results', kind='raw_handle', required=True),
        NodeArgMeta(name='market_id', kind='string', required=False),
        NodeArgMeta(name='variable', kind='string', required=False),
        ),
        defaults={'variable': 'prices'},
    ),
    'dcd_diversion': NodeMeta(
        fn='dcd_diversion',
        category='31-discrete-choice-demand',
        card_id=268,
        contract_hash='c2-d0cc1106e4a12fe10360ca5ca32704ff7e0bfb1b26f3038193ed24ab4cd15ee3',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='results', kind='raw_handle', required=True),
        NodeArgMeta(name='market_id', kind='string', required=False),
        NodeArgMeta(name='include_outside', kind='boolean', required=False),
        ),
        defaults={'include_outside': True},
    ),
    'dcd_markups': NodeMeta(
        fn='dcd_markups',
        category='31-discrete-choice-demand',
        card_id=268,
        contract_hash='c2-b833d35fbad575c6099133d5cb823ea04b3fc0e2c50f413ef2dcc301e64457d0',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='results', kind='raw_handle', required=True),
        NodeArgMeta(name='conduct', kind='enum', required=False, enum=('bertrand', 'monopoly', 'cournot', )),
        NodeArgMeta(name='ownership', kind='matrix_handle', required=False),
        ),
        defaults={'conduct': 'bertrand'},
    ),
    'dcd_merger_simulate': NodeMeta(
        fn='dcd_merger_simulate',
        category='31-discrete-choice-demand',
        card_id=269,
        contract_hash='c2-7ba4be4f025d077927693be57a9bc527f6385ced1b527d91b4b77081c481bcf7',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='results', kind='raw_handle', required=True),
        NodeArgMeta(name='ownership_post', kind='matrix_handle', required=True),
        NodeArgMeta(name='cost_change', kind='series_handle', required=False),
        NodeArgMeta(name='tol', kind='number', required=False),
        NodeArgMeta(name='max_iter', kind='integer', required=False),
        ),
        defaults={'tol': 1e-12, 'max_iter': 1000},
    ),
    'dcd_upp': NodeMeta(
        fn='dcd_upp',
        category='31-discrete-choice-demand',
        card_id=269,
        contract_hash='c2-eb3158f2b298fd3d44ceae6862b0c247d0f5b4cb58d1f15a63b43114bbb06f88',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='results', kind='raw_handle', required=True),
        NodeArgMeta(name='merging', kind='series_codes', required=True),
        NodeArgMeta(name='efficiency', kind='number', required=False),
        ),
        defaults={'efficiency': 0.0},
    ),
    'dcd_welfare_change': NodeMeta(
        fn='dcd_welfare_change',
        category='31-discrete-choice-demand',
        card_id=269,
        contract_hash='c2-67b791815e8c94e1171c4adc2e72f5eb3adbbdcc0b7be170f6b94fcffe329bef',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='results', kind='raw_handle', required=True),
        NodeArgMeta(name='prices_post', kind='series_handle', required=True),
        ),
        defaults={},
    ),
    'dcd_nested_logit_fit': NodeMeta(
        fn='dcd_nested_logit_fit',
        category='31-discrete-choice-demand',
        card_id=270,
        contract_hash='c2-3fdde90c9b238de04bfb5a06cd00b3674752c1abc209ced197cd87456ed5332d',
        register_field='results',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='product_data', kind='df_handle', required=True),
        NodeArgMeta(name='market_ids', kind='string', required=True),
        NodeArgMeta(name='shares', kind='string', required=True),
        NodeArgMeta(name='nesting_ids', kind='string', required=True),
        NodeArgMeta(name='characteristics', kind='series_codes', required=False),
        NodeArgMeta(name='instruments', kind='series_codes', required=False),
        ),
        defaults={},
    ),
    'dcd_nested_logit_elasticities': NodeMeta(
        fn='dcd_nested_logit_elasticities',
        category='31-discrete-choice-demand',
        card_id=270,
        contract_hash='c2-5f7a3e3a15deadb83d373c5beea5900d121c0006665274897a94a4682db084c7',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='results', kind='raw_handle', required=True),
        NodeArgMeta(name='market_id', kind='string', required=False),
        ),
        defaults={},
    ),
    'dcd_mnlogit_fit': NodeMeta(
        fn='dcd_mnlogit_fit',
        category='31-discrete-choice-demand',
        card_id=271,
        contract_hash='c2-94d7e905e10be22aeccc5fbe2c6d48c9efce9174d978ec507909f6fc0a956be2',
        register_field='fit',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='choice', kind='string', required=True),
        NodeArgMeta(name='covariates', kind='series_codes', required=False),
        NodeArgMeta(name='base', kind='string', required=False),
        ),
        defaults={},
    ),
    'dcd_clogit_fit': NodeMeta(
        fn='dcd_clogit_fit',
        category='31-discrete-choice-demand',
        card_id=271,
        contract_hash='c2-d6dd4a1f3f073a8d36276520c62b09c5f8ea851ef19e621807cf5de150cab779',
        register_field='fit',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='chooser', kind='string', required=True),
        NodeArgMeta(name='chosen', kind='string', required=True),
        NodeArgMeta(name='covariates', kind='series_codes', required=False),
        ),
        defaults={},
    ),
    'dcd_iia_test': NodeMeta(
        fn='dcd_iia_test',
        category='31-discrete-choice-demand',
        card_id=271,
        contract_hash='c2-4387d4532e055b234815496be4be3db70fc30e231b3339f46c14244232254b3d',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='fit', kind='raw_handle', required=True),
        NodeArgMeta(name='drop', kind='series_codes', required=True),
        ),
        defaults={},
    ),
    'dcd_mixed_logit_fit': NodeMeta(
        fn='dcd_mixed_logit_fit',
        category='31-discrete-choice-demand',
        card_id=272,
        contract_hash='c2-3a1720ca74fce751d3d65ad6e1f826714770ba31585f2940eb80c7c33f128fbd',
        register_field='fit',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='chooser', kind='string', required=True),
        NodeArgMeta(name='chosen', kind='string', required=True),
        NodeArgMeta(name='covariates', kind='series_codes', required=False),
        NodeArgMeta(name='random', kind='series_codes', required=False),
        NodeArgMeta(name='distributions', kind='series_codes', required=False),
        NodeArgMeta(name='n_draws', kind='integer', required=False),
        NodeArgMeta(name='panel', kind='string', required=False),
        NodeArgMeta(name='seed', kind='integer', required=True),
        ),
        defaults={'n_draws': 600},
    ),
    'dcd_mixed_logit_individual': NodeMeta(
        fn='dcd_mixed_logit_individual',
        category='31-discrete-choice-demand',
        card_id=272,
        contract_hash='c2-f0ac0401f83516088ece5cd5af9aa95e94c89398fb3ab9c689c1e25e29478e51',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='fit', kind='raw_handle', required=True),
        ),
        defaults={},
    ),
    'dcd_wtp': NodeMeta(
        fn='dcd_wtp',
        category='31-discrete-choice-demand',
        card_id=273,
        contract_hash='c2-787f60a1c7675e38cecebb39a822a57c1318ee56e1c6d9cc57da24ef68e67ed7',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='results', kind='raw_handle', required=True),
        NodeArgMeta(name='price_variable', kind='string', required=False),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'price_variable': 'prices', 'conf_level': 0.95},
    ),
    'dcd_compensating_variation': NodeMeta(
        fn='dcd_compensating_variation',
        category='31-discrete-choice-demand',
        card_id=273,
        contract_hash='c2-104c1e9151857528fddc041c9ce6af20212f66dcaa630ea63d422b5a6737a58b',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='results', kind='raw_handle', required=True),
        NodeArgMeta(name='prices_post', kind='series_handle', required=False),
        NodeArgMeta(name='available_post', kind='series_handle', required=False),
        ),
        defaults={},
    ),
    'dcd_consumer_surplus': NodeMeta(
        fn='dcd_consumer_surplus',
        category='31-discrete-choice-demand',
        card_id=273,
        contract_hash='c2-9144c53c1477a2cfeadc0b18ea511e93612e002ffe979933b418aaf7236995ba',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='results', kind='raw_handle', required=True),
        NodeArgMeta(name='market_id', kind='string', required=False),
        ),
        defaults={},
    ),
}

#: Argument defaults, for FORM PREFILL ONLY. A default must never be sent
#: explicitly on the wire: adapt_args assigns it RAW, bypassing coercion.
DEFAULTS: dict[str, dict[str, object]] = {
    'dcd_blp_problem': {},
    'dcd_blp_solve': {'inner_tol': 1e-14, 'outer_tol': 1e-08, 'method': '2s'},
    'dcd_blp_shares': {},
    'dcd_blp_instruments': {'kind': 'differentiation'},
    'dcd_optimal_instruments': {'method': 'approximate'},
    'dcd_elasticities': {'variable': 'prices'},
    'dcd_diversion': {'include_outside': True},
    'dcd_markups': {'conduct': 'bertrand'},
    'dcd_merger_simulate': {'tol': 1e-12, 'max_iter': 1000},
    'dcd_upp': {'efficiency': 0.0},
    'dcd_welfare_change': {},
    'dcd_nested_logit_fit': {},
    'dcd_nested_logit_elasticities': {},
    'dcd_mnlogit_fit': {},
    'dcd_clogit_fit': {},
    'dcd_iia_test': {},
    'dcd_mixed_logit_fit': {'n_draws': 600},
    'dcd_mixed_logit_individual': {},
    'dcd_wtp': {'price_variable': 'prices', 'conf_level': 0.95},
    'dcd_compensating_variation': {},
    'dcd_consumer_surplus': {},
}


@cache
def wire_model(fn: str) -> type[BaseModel]:
    """The model the ENGINE validates. Built on first use and cached."""
    return build_wire_model(NODE_META[fn])


@cache
def authoring_model(fn: str) -> type[BaseModel]:
    """The model a GRAPH EDITOR edits. Built on first use and cached."""
    return build_authoring_model(NODE_META[fn])
