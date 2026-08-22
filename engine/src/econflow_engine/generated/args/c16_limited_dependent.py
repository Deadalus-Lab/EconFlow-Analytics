# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 2 for category 16-limited-dependent -- 13 nodes. No descriptions."""

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
    'hdfe_average_partial_effects': NodeMeta(
        fn='hdfe_average_partial_effects',
        category='16-limited-dependent',
        card_id=206,
        contract_hash='c2-738c8ad485f451ae477fb3b92bc327bf58af1f3461596b2f018aa3044a7e52bf',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='object', kind='raw_handle', required=True),
        NodeArgMeta(name='n_pop', kind='integer', required=False),
        NodeArgMeta(name='sampling_fe', kind='enum', required=False, enum=('independence', 'unrestricted', )),
        NodeArgMeta(name='weak_exo', kind='boolean', required=False),
        ),
        defaults={'weak_exo': False},
    ),
    'hdfe_glm': NodeMeta(
        fn='hdfe_glm',
        category='16-limited-dependent',
        card_id=206,
        contract_hash='c2-5a9731a2c0661086030136bf490fdfc64b77f877b03faececd8e64d10200267b',
        register_field='object',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='formula', kind='formula', required=True),
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='family', kind='enum', required=False, enum=('logit', 'probit', 'poisson', )),
        NodeArgMeta(name='bias_correct', kind='boolean', required=False),
        NodeArgMeta(name='L', kind='integer', required=False),
        NodeArgMeta(name='panel_structure', kind='enum', required=False, enum=('classic', 'network', )),
        ),
        defaults={'bias_correct': False, 'L': 0},
    ),
    'run_binomial_fe_glm': NodeMeta(
        fn='run_binomial_fe_glm',
        category='16-limited-dependent',
        card_id=83,
        contract_hash='c2-c6630e2a7607079a05c51777084f7ff67f615f082d0201a54ad7b3120f6e983c',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='formula', kind='formula', required=True),
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='link', kind='enum', required=False, enum=('probit', 'logit', )),
        NodeArgMeta(name='fixef', kind='string', required=False),
        ),
        defaults={},
    ),
    'run_roc': NodeMeta(
        fn='run_roc',
        category='16-limited-dependent',
        card_id=84,
        contract_hash='c2-0665fd025eb1eac42b3394d2b4b7ee9c38f2378f3efa85873059c6d722d9fda1',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='response', kind='raw_handle', required=True),
        NodeArgMeta(name='predictor', kind='raw_handle', required=True),
        NodeArgMeta(name='direction', kind='enum', required=False, enum=('auto', '<', '>', )),
        NodeArgMeta(name='ci', kind='boolean', required=False),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'ci': True, 'conf_level': 0.95},
    ),
    'ld_ordered_choice': NodeMeta(
        fn='ld_ordered_choice',
        category='16-limited-dependent',
        card_id=523,
        contract_hash='c2-8a59b3306b9dd6933d304224e3030ffd1bf94f6984977f833fa148a4977b8a6a',
        register_field='fit',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='y', kind='series_handle', required=True),
        NodeArgMeta(name='x', kind='df_handle', required=True),
        NodeArgMeta(name='link', kind='enum', required=False, enum=('logit', 'probit', 'cloglog', )),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'link': 'logit', 'conf_level': 0.95},
    ),
    'ld_proportional_odds_test': NodeMeta(
        fn='ld_proportional_odds_test',
        category='16-limited-dependent',
        card_id=523,
        contract_hash='c2-9660abf20c86d664e288f73864029222c78723cf16139ebb51f62f3e792c072f',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='fit', kind='raw_handle', required=True),
        NodeArgMeta(name='alpha', kind='number', required=False),
        ),
        defaults={'alpha': 0.05},
    ),
    'ld_count_model': NodeMeta(
        fn='ld_count_model',
        category='16-limited-dependent',
        card_id=524,
        contract_hash='c2-bdcc39178be9117cc3aa8cf20f2174538f00ab3977617a95a4c484a670fc82ba',
        register_field='fit',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='y', kind='series_handle', required=True),
        NodeArgMeta(name='x', kind='df_handle', required=True),
        NodeArgMeta(name='family', kind='enum', required=False, enum=('poisson', 'negative_binomial', 'generalised_poisson', )),
        NodeArgMeta(name='zeros', kind='enum', required=False, enum=('none', 'zero_inflated', 'hurdle', 'truncated', )),
        NodeArgMeta(name='exposure', kind='series_handle', required=False),
        NodeArgMeta(name='inflation_covariates', kind='series_codes', required=False),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'family': 'negative_binomial', 'zeros': 'none', 'conf_level': 0.95},
    ),
    'ld_overdispersion_test': NodeMeta(
        fn='ld_overdispersion_test',
        category='16-limited-dependent',
        card_id=524,
        contract_hash='c2-b1a91aa5f1503404fe3b225fd858ece1b8870c368d15a092db8c000e61f3d6fb',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='fit', kind='raw_handle', required=True),
        NodeArgMeta(name='alpha', kind='number', required=False),
        ),
        defaults={'alpha': 0.05},
    ),
    'ld_tobit': NodeMeta(
        fn='ld_tobit',
        category='16-limited-dependent',
        card_id=525,
        contract_hash='c2-aa92c1b24a1b1c1f3693d31d80fabc446e799725d0fcf3203365b74ff1d2d895',
        register_field='fit',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='y', kind='series_handle', required=True),
        NodeArgMeta(name='x', kind='df_handle', required=True),
        NodeArgMeta(name='left', kind='number', required=False),
        NodeArgMeta(name='right', kind='number', required=False),
        NodeArgMeta(name='model', kind='enum', required=False, enum=('censored', 'truncated', 'two_part', )),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'model': 'censored', 'conf_level': 0.95},
    ),
    'ld_heckman': NodeMeta(
        fn='ld_heckman',
        category='16-limited-dependent',
        card_id=526,
        contract_hash='c2-7bb2d91d7b7cc72e700081602ea82b85233046ee207913efa64edda7f14a6830',
        register_field='fit',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='y', kind='series_handle', required=True),
        NodeArgMeta(name='x', kind='df_handle', required=True),
        NodeArgMeta(name='selection', kind='series_handle', required=True),
        NodeArgMeta(name='z', kind='df_handle', required=True),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('two_step', 'mle', )),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'method': 'two_step', 'conf_level': 0.95},
    ),
    'ld_fractional_response': NodeMeta(
        fn='ld_fractional_response',
        category='16-limited-dependent',
        card_id=527,
        contract_hash='c2-30c9dc20161288ae9d737019098e681860f71fae3d6dca1921fb1f190ce4994a',
        register_field='fit',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='y', kind='series_handle', required=True),
        NodeArgMeta(name='x', kind='df_handle', required=True),
        NodeArgMeta(name='model', kind='enum', required=False, enum=('fractional', 'beta', 'zero_one_inflated_beta', )),
        NodeArgMeta(name='link', kind='enum', required=False, enum=('logit', 'probit', 'cloglog', 'loglog', )),
        NodeArgMeta(name='precision_covariates', kind='series_codes', required=False),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'model': 'fractional', 'link': 'logit', 'conf_level': 0.95},
    ),
    'ld_unordered_choice': NodeMeta(
        fn='ld_unordered_choice',
        category='16-limited-dependent',
        card_id=528,
        contract_hash='c2-db711395f348a585a9fc3b28aa3a3192edcdbdaf037b4edd611dfc04ba5b45f6',
        register_field='fit',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='y', kind='series_handle', required=True),
        NodeArgMeta(name='x', kind='df_handle', required=True),
        NodeArgMeta(name='model', kind='enum', required=False, enum=('multinomial', 'conditional', 'multinomial_probit', )),
        NodeArgMeta(name='base', kind='string', required=False),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'model': 'multinomial', 'conf_level': 0.95},
    ),
    'ld_classification_evaluation': NodeMeta(
        fn='ld_classification_evaluation',
        category='16-limited-dependent',
        card_id=529,
        contract_hash='c2-610bda3a732f3e1ce291e32cbe036c7f3ce477fb7801d3cf8d37b156187543b9',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='y', kind='series_handle', required=True),
        NodeArgMeta(name='probability', kind='series_handle', required=True),
        NodeArgMeta(name='threshold', kind='number', required=False),
        NodeArgMeta(name='n_bins', kind='integer', required=False),
        NodeArgMeta(name='decompose', kind='boolean', required=False),
        ),
        defaults={'threshold': 0.5, 'n_bins': 10, 'decompose': True},
    ),
}

#: Argument defaults, for FORM PREFILL ONLY. A default must never be sent
#: explicitly on the wire: adapt_args assigns it RAW, bypassing coercion.
DEFAULTS: dict[str, dict[str, object]] = {
    'hdfe_average_partial_effects': {'weak_exo': False},
    'hdfe_glm': {'bias_correct': False, 'L': 0},
    'run_binomial_fe_glm': {},
    'run_roc': {'ci': True, 'conf_level': 0.95},
    'ld_ordered_choice': {'link': 'logit', 'conf_level': 0.95},
    'ld_proportional_odds_test': {'alpha': 0.05},
    'ld_count_model': {'family': 'negative_binomial', 'zeros': 'none', 'conf_level': 0.95},
    'ld_overdispersion_test': {'alpha': 0.05},
    'ld_tobit': {'model': 'censored', 'conf_level': 0.95},
    'ld_heckman': {'method': 'two_step', 'conf_level': 0.95},
    'ld_fractional_response': {'model': 'fractional', 'link': 'logit', 'conf_level': 0.95},
    'ld_unordered_choice': {'model': 'multinomial', 'conf_level': 0.95},
    'ld_classification_evaluation': {'threshold': 0.5, 'n_bins': 10, 'decompose': True},
}


@cache
def wire_model(fn: str) -> type[BaseModel]:
    """The model the ENGINE validates. Built on first use and cached."""
    return build_wire_model(NODE_META[fn])


@cache
def authoring_model(fn: str) -> type[BaseModel]:
    """The model a GRAPH EDITOR edits. Built on first use and cached."""
    return build_authoring_model(NODE_META[fn])
