# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.v1.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 2 for category 08-panel-data -- 20 nodes. No descriptions."""

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
    'feis_bstest': NodeMeta(
        fn='feis_bstest',
        category='08-panel-data',
        card_id=173,
        contract_hash='c-489fdd0b3cc004a20cd410d17499f7e2aad6cb320879a971317f05c6da0a2bbf',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='object', kind='raw_handle', required=True),
        NodeArgMeta(name='type', kind='enum', required=False, enum=('all', 'bs1', 'bs2', 'bs3', )),
        NodeArgMeta(name='rep', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=False),
        NodeArgMeta(name='terms', kind='raw', required=False),
        ),
        defaults={'rep': 500, 'seed': 2025},
    ),
    'feis_fit': NodeMeta(
        fn='feis_fit',
        category='08-panel-data',
        card_id=173,
        contract_hash='c-6a085b3f0bd3872ac73cc8c1339f076f1d581e5c9f165218a1f44b21f914c0a5',
        register_field='object',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='formula', kind='formula', required=True),
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='id', kind='string', required=True),
        NodeArgMeta(name='robust', kind='boolean', required=False),
        NodeArgMeta(name='intercept', kind='boolean', required=False),
        NodeArgMeta(name='dropgroups', kind='boolean', required=False),
        ),
        defaults={'robust': False, 'intercept': False, 'dropgroups': False},
    ),
    'feis_slopes': NodeMeta(
        fn='feis_slopes',
        category='08-panel-data',
        card_id=173,
        contract_hash='c-2a9d8a9428811e26adf28f58aceaff1a6fc5270ccfdbb75c292ba631c69a694a',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='object', kind='raw_handle', required=True),
        ),
        defaults={},
    ),
    'feis_test': NodeMeta(
        fn='feis_test',
        category='08-panel-data',
        card_id=173,
        contract_hash='c-76d3827243e4850b9a72a33ad7878d2852b11ad5db5f11e6601d37e8468a719a',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='object', kind='raw_handle', required=True),
        NodeArgMeta(name='type', kind='enum', required=False, enum=('all', 'art1', 'art2', 'art3', )),
        NodeArgMeta(name='robust', kind='boolean', required=False),
        NodeArgMeta(name='terms', kind='raw', required=False),
        ),
        defaults={'robust': False},
    ),
    'lme_glmer': NodeMeta(
        fn='lme_glmer',
        category='08-panel-data',
        card_id=175,
        contract_hash='c-2dcf63da3bb5cb1b9fc1b1204d76b90c4ac77d4d50389a9c1183cc6da1f40575',
        register_field='object',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='formula', kind='formula', required=True),
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='family', kind='enum', required=False, enum=('binomial', 'poisson', 'Gamma', 'inverse.gaussian', )),
        NodeArgMeta(name='nAGQ', kind='integer', required=False),
        ),
        defaults={'nAGQ': 1},
    ),
    'lme_lmer': NodeMeta(
        fn='lme_lmer',
        category='08-panel-data',
        card_id=175,
        contract_hash='c-0c41cdda72267f49667ba11d5a40d858492a213291b1defdfce87153961dfb74',
        register_field='object',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='formula', kind='formula', required=True),
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='REML', kind='boolean', required=False),
        ),
        defaults={'REML': True},
    ),
    'lme_ranef': NodeMeta(
        fn='lme_ranef',
        category='08-panel-data',
        card_id=175,
        contract_hash='c-3f726c82e45b225308eb81724b486df2e5d49bc931bdbfa01c001611e1613b75',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='object', kind='raw_handle', required=True),
        NodeArgMeta(name='condVar', kind='boolean', required=False),
        ),
        defaults={'condVar': True},
    ),
    'lme_varcorr': NodeMeta(
        fn='lme_varcorr',
        category='08-panel-data',
        card_id=175,
        contract_hash='c-9b42f9a02c910f7ce25df5a2326f0c4b3d51864766fdfc19c777a57b9ab86c45',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='object', kind='raw_handle', required=True),
        ),
        defaults={},
    ),
    'pcse_fit': NodeMeta(
        fn='pcse_fit',
        category='08-panel-data',
        card_id=174,
        contract_hash='c-c45dfa5d837c3660d465983da949f8a05b63454dea0794c2881718af8e3a741a',
        register_field='object',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='formula', kind='formula', required=True),
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='groupN', kind='string', required=True),
        NodeArgMeta(name='groupT', kind='string', required=True),
        NodeArgMeta(name='pairwise', kind='boolean', required=False),
        ),
        defaults={'pairwise': False},
    ),
    'pcse_summary': NodeMeta(
        fn='pcse_summary',
        category='08-panel-data',
        card_id=174,
        contract_hash='c-c8984a900d7359dc560d6de39a12480797eef1584911293923b5512f70924b30',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='object', kind='raw_handle', required=True),
        ),
        defaults={},
    ),
    'pcse_vcov': NodeMeta(
        fn='pcse_vcov',
        category='08-panel-data',
        card_id=174,
        contract_hash='c-46dfe31fba4127674f3a9f317f35016727e6079a2a9aa2bd59c9c882b52d83bf',
        register_field='object',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='object', kind='raw_handle', required=True),
        NodeArgMeta(name='groupN', kind='num_array', required=True),
        NodeArgMeta(name='groupT', kind='num_array', required=True),
        NodeArgMeta(name='pairwise', kind='boolean', required=False),
        ),
        defaults={'pairwise': False},
    ),
    'pd_effects_ftest': NodeMeta(
        fn='pd_effects_ftest',
        category='08-panel-data',
        card_id=46,
        contract_hash='c-5110f8adcb7df4698b9c559650800b32c855cbd3e01a8aa612b6e1c60631f074',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='x', kind='formula', required=True),
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='effect', kind='enum', required=False, enum=('individual', 'time', 'twoways', )),
        ),
        defaults={},
    ),
    'pd_fit': NodeMeta(
        fn='pd_fit',
        category='08-panel-data',
        card_id=46,
        contract_hash='c-f9082990ec600f29178512dba9b8a9f01dc78f0e499dc1371c3c3ecb50ce5d1b',
        register_field='object',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='formula', kind='formula', required=True),
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='effect', kind='enum', required=False, enum=('individual', 'time', 'twoways', 'nested', )),
        NodeArgMeta(name='model', kind='enum', required=False, enum=('within', 'random', 'ht', 'between', 'pooling', 'fd', )),
        ),
        defaults={},
    ),
    'pd_fixed_effects': NodeMeta(
        fn='pd_fixed_effects',
        category='08-panel-data',
        card_id=46,
        contract_hash='c-ff980be3f9d7e524478379d47d0bdfed31509979db985ef496e296a55b7e6554',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='object', kind='raw_handle', required=True),
        NodeArgMeta(name='type', kind='enum', required=False, enum=('level', 'dfirst', 'dmean', )),
        ),
        defaults={},
    ),
    'pd_gmm_autocorr_test': NodeMeta(
        fn='pd_gmm_autocorr_test',
        category='08-panel-data',
        card_id=47,
        contract_hash='c-d05eceeb0c23f452e70bd112d5bd361357ac7fc8517b6dff042cea4ab222c880',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='object', kind='raw_handle', required=True),
        NodeArgMeta(name='order', kind='integer', required=False),
        ),
        defaults={'order': 1},
    ),
    'pd_gmm_fit': NodeMeta(
        fn='pd_gmm_fit',
        category='08-panel-data',
        card_id=47,
        contract_hash='c-0cabb837406b79e60e5b307bad47d38e982962dcf42171c3cecfb18ff59ba568',
        register_field='object',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='formula', kind='formula', required=True),
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='effect', kind='enum', required=False, enum=('twoways', 'individual', )),
        NodeArgMeta(name='model', kind='enum', required=False, enum=('onestep', 'twosteps', )),
        NodeArgMeta(name='transformation', kind='enum', required=False, enum=('d', 'ld', )),
        ),
        defaults={},
    ),
    'pd_gmm_sargan_test': NodeMeta(
        fn='pd_gmm_sargan_test',
        category='08-panel-data',
        card_id=47,
        contract_hash='c-b1da4c92cac0727969e83ff9981c8e6187ed1f3981166189f80c8f5587429207',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='object', kind='raw_handle', required=True),
        NodeArgMeta(name='weights', kind='enum', required=False, enum=('twosteps', 'onestep', )),
        ),
        defaults={},
    ),
    'pd_hausman_test': NodeMeta(
        fn='pd_hausman_test',
        category='08-panel-data',
        card_id=46,
        contract_hash='c-5c6a56d236bfb5e30c94de96b0d83c732594ea2e0ed4ab9bd45f53c15c72fcb6',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='x', kind='formula', required=True),
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='effect', kind='enum', required=False, enum=('individual', 'time', 'twoways', )),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('chisq', 'aux', )),
        ),
        defaults={},
    ),
    'pd_poolability_test': NodeMeta(
        fn='pd_poolability_test',
        category='08-panel-data',
        card_id=46,
        contract_hash='c-9557744b36feebca97de4dd01dc2ac57b1e4d82ce049fc7f51fa7efeaed8aaa5',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='x', kind='formula', required=True),
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='effect', kind='enum', required=False, enum=('individual', 'time', 'twoways', )),
        NodeArgMeta(name='type', kind='enum', required=False, enum=('honda', 'bp', 'ghm', 'kw', )),
        ),
        defaults={},
    ),
    'pd_random_effects': NodeMeta(
        fn='pd_random_effects',
        category='08-panel-data',
        card_id=46,
        contract_hash='c-4ed6819a68a43f5668e2e33e4c5a4b89b90508ec28ecacaff935249cbd9b8a20',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='object', kind='raw_handle', required=True),
        ),
        defaults={},
    ),
}

#: Argument defaults, for FORM PREFILL ONLY. A default must never be sent
#: explicitly on the wire: adapt_args assigns it RAW, bypassing coercion.
DEFAULTS: dict[str, dict[str, object]] = {
    'feis_bstest': {'rep': 500, 'seed': 2025},
    'feis_fit': {'robust': False, 'intercept': False, 'dropgroups': False},
    'feis_slopes': {},
    'feis_test': {'robust': False},
    'lme_glmer': {'nAGQ': 1},
    'lme_lmer': {'REML': True},
    'lme_ranef': {'condVar': True},
    'lme_varcorr': {},
    'pcse_fit': {'pairwise': False},
    'pcse_summary': {},
    'pcse_vcov': {'pairwise': False},
    'pd_effects_ftest': {},
    'pd_fit': {},
    'pd_fixed_effects': {},
    'pd_gmm_autocorr_test': {'order': 1},
    'pd_gmm_fit': {},
    'pd_gmm_sargan_test': {},
    'pd_hausman_test': {},
    'pd_poolability_test': {},
    'pd_random_effects': {},
}


@cache
def wire_model(fn: str) -> type[BaseModel]:
    """The model the ENGINE validates. Built on first use and cached."""
    return build_wire_model(NODE_META[fn])


@cache
def authoring_model(fn: str) -> type[BaseModel]:
    """The model a GRAPH EDITOR edits. Built on first use and cached."""
    return build_authoring_model(NODE_META[fn])
