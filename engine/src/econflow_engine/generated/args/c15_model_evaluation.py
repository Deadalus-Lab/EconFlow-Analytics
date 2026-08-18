# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.v1.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 2 for category 15-model-evaluation -- 15 nodes. No descriptions."""

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
    'compute_loss_level': NodeMeta(
        fn='compute_loss_level',
        category='15-model-evaluation',
        card_id=75,
        contract_hash='c-b667852cfba7e487d095771ad6c4b9ac0364a6f2c10fbc043d520d293343e722',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='realized', kind='series_handle', required=True),
        NodeArgMeta(name='evaluated', kind='matrix_handle', required=True),
        NodeArgMeta(name='which', kind='enum', required=False, enum=('SE', 'AE', )),
        ),
        defaults={},
    ),
    'compute_loss_vol': NodeMeta(
        fn='compute_loss_vol',
        category='15-model-evaluation',
        card_id=75,
        contract_hash='c-01185519174ef34e239ca3203cf96c5cf06682f63553fcb7fd12578ab545f09e',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='realized', kind='series_handle', required=True),
        NodeArgMeta(name='evaluated', kind='matrix_handle', required=True),
        NodeArgMeta(name='which', kind='enum', required=False, enum=('SE1', 'SE2', 'QLIKE', 'R2LOG', 'AE1', 'AE2', )),
        ),
        defaults={},
    ),
    'eval_dm_test': NodeMeta(
        fn='eval_dm_test',
        category='15-model-evaluation',
        card_id=74,
        contract_hash='c-5df9d31676a7a59a7ad0abad57ed8571070cce4c92d43106ebe9a148099ce803',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='e1', kind='series_handle', required=True),
        NodeArgMeta(name='e2', kind='series_handle', required=True),
        NodeArgMeta(name='alternative', kind='enum', required=False, enum=('two.sided', 'less', 'greater', )),
        NodeArgMeta(name='h', kind='integer', required=False),
        NodeArgMeta(name='power', kind='number', required=False),
        NodeArgMeta(name='varestimator', kind='enum', required=False, enum=('acf', 'bartlett', )),
        ),
        defaults={'h': 1, 'power': 2},
    ),
    'eval_tsCV': NodeMeta(
        fn='eval_tsCV',
        category='15-model-evaluation',
        card_id=74,
        contract_hash='c-5b11784643247577563a645d574fbbb3a6ae887ac6e675dbbd7c3a48cd0f0492',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='y', kind='series_handle', required=True),
        NodeArgMeta(name='forecastfunction', kind='forecastfn_enum', required=True, enum=('naive', 'snaive', 'drift', 'mean', 'ses', 'holt', 'ets', 'auto_arima', 'theta', )),
        NodeArgMeta(name='h', kind='integer', required=False),
        NodeArgMeta(name='window', kind='integer', required=False),
        NodeArgMeta(name='initial', kind='integer', required=False),
        ),
        defaults={'h': 1, 'initial': 0},
    ),
    'run_arch_test': NodeMeta(
        fn='run_arch_test',
        category='15-model-evaluation',
        card_id=77,
        contract_hash='c-b59d7d53691beff26395e58a9d0e9f759f928b54149637ec152d4bf1fefa086d',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='x', kind='series_handle', required=True),
        NodeArgMeta(name='lags', kind='integer', required=False),
        NodeArgMeta(name='demean', kind='boolean', required=False),
        ),
        defaults={'lags': 12, 'demean': False},
    ),
    'run_bg_test': NodeMeta(
        fn='run_bg_test',
        category='15-model-evaluation',
        card_id=76,
        contract_hash='c-177eeedcad2e56106c2fae31f9dc4a3e5c48031d1cfd42189b1129481a22f33f',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='formula', kind='formula', required=True),
        NodeArgMeta(name='order', kind='integer', required=False),
        NodeArgMeta(name='type', kind='enum', required=False, enum=('Chisq', 'F', )),
        NodeArgMeta(name='data', kind='df_handle', required=False),
        ),
        defaults={'order': 1},
    ),
    'run_bp_test': NodeMeta(
        fn='run_bp_test',
        category='15-model-evaluation',
        card_id=76,
        contract_hash='c-c10d6d811d22c1ded31548dee4c40c26f15dee3b3042cd36216f9ae9b63c0b5a',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='formula', kind='formula', required=True),
        NodeArgMeta(name='studentize', kind='boolean', required=False),
        NodeArgMeta(name='data', kind='df_handle', required=False),
        ),
        defaults={'studentize': True},
    ),
    'run_mcs_procedure': NodeMeta(
        fn='run_mcs_procedure',
        category='15-model-evaluation',
        card_id=75,
        contract_hash='c-856996b8c74c24b806e6bd0a481febc5d6c2a230576958498317812d3a53861f',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='heavy',
        args=(
        NodeArgMeta(name='Loss', kind='matrix_handle', required=True),
        NodeArgMeta(name='alpha', kind='number', required=False),
        NodeArgMeta(name='B', kind='integer', required=False),
        NodeArgMeta(name='statistic', kind='enum', required=False, enum=('Tmax', 'TR', )),
        NodeArgMeta(name='k', kind='integer', required=False),
        NodeArgMeta(name='min_k', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=False),
        ),
        defaults={'alpha': 0.15, 'B': 1000, 'min_k': 3},
    ),
    'run_reset_test': NodeMeta(
        fn='run_reset_test',
        category='15-model-evaluation',
        card_id=76,
        contract_hash='c-5f6e898c450ebd4c79adabbbabf127716f3d6b3fd3013b94c8df1ca82afe3f01',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='formula', kind='formula', required=True),
        NodeArgMeta(name='power', kind='integer', required=False),
        NodeArgMeta(name='type', kind='enum', required=False, enum=('fitted', 'regressor', 'princomp', )),
        NodeArgMeta(name='data', kind='df_handle', required=False),
        ),
        defaults={},
    ),
    'sr_crps_parametric': NodeMeta(
        fn='sr_crps_parametric',
        category='15-model-evaluation',
        card_id=94,
        contract_hash='c-ed4a7abb390730cc27aa71b175cd393d4dd15dffea946ef26dade1aec8555a23',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='y', kind='raw_handle', required=True),
        NodeArgMeta(name='family', kind='enum', required=False, enum=('normal', 't', 'mixnorm', )),
        NodeArgMeta(name='mean', kind='number', required=False),
        NodeArgMeta(name='sd', kind='number', required=False),
        NodeArgMeta(name='df', kind='number', required=False),
        NodeArgMeta(name='location', kind='number', required=False),
        NodeArgMeta(name='scale', kind='number', required=False),
        ),
        defaults={'mean': 0, 'sd': 1, 'location': 0, 'scale': 1},
    ),
    'sr_crps_sample': NodeMeta(
        fn='sr_crps_sample',
        category='15-model-evaluation',
        card_id=94,
        contract_hash='c-b2903ec6ba28e60235839ef709fe36dbb947982c1566db103bfe8bdfea410838',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='y', kind='raw_handle', required=True),
        NodeArgMeta(name='dat', kind='matrix_handle', required=True),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('edf', 'kde', )),
        NodeArgMeta(name='bw', kind='number', required=False),
        ),
        defaults={},
    ),
    'sr_crps_tailweighted': NodeMeta(
        fn='sr_crps_tailweighted',
        category='15-model-evaluation',
        card_id=94,
        contract_hash='c-06c693252da45ae0f47e64d347efdd4c318e64f275d73d8eab94b848010ca8ae',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='y', kind='raw_handle', required=True),
        NodeArgMeta(name='dat', kind='matrix_handle', required=True),
        NodeArgMeta(name='side', kind='enum', required=False, enum=('left', 'right', 'interval', )),
        NodeArgMeta(name='a', kind='number', required=False),
        NodeArgMeta(name='b', kind='number', required=False),
        NodeArgMeta(name='kind', kind='enum', required=False, enum=('threshold', 'outcome', )),
        ),
        defaults={},
    ),
    'sr_logs_parametric': NodeMeta(
        fn='sr_logs_parametric',
        category='15-model-evaluation',
        card_id=94,
        contract_hash='c-0ff23f36de2fadcd552005f38bbae500684424be5d4bd101a7d8cbab02d81eb8',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='y', kind='raw_handle', required=True),
        NodeArgMeta(name='family', kind='enum', required=False, enum=('normal', 't', 'mixnorm', )),
        NodeArgMeta(name='mean', kind='number', required=False),
        NodeArgMeta(name='sd', kind='number', required=False),
        NodeArgMeta(name='df', kind='number', required=False),
        NodeArgMeta(name='location', kind='number', required=False),
        NodeArgMeta(name='scale', kind='number', required=False),
        ),
        defaults={'mean': 0, 'sd': 1, 'location': 0, 'scale': 1},
    ),
    'sr_logs_sample': NodeMeta(
        fn='sr_logs_sample',
        category='15-model-evaluation',
        card_id=94,
        contract_hash='c-22cd97dafd3640464dfe247221f6e3d30a0a4b1cb75ac9e343cfddd12296dcff',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='y', kind='raw_handle', required=True),
        NodeArgMeta(name='dat', kind='matrix_handle', required=True),
        NodeArgMeta(name='bw', kind='number', required=False),
        ),
        defaults={},
    ),
    'sr_pit_sample': NodeMeta(
        fn='sr_pit_sample',
        category='15-model-evaluation',
        card_id=94,
        contract_hash='c-8cd6df3a4e6246087aa77de7c707168d2c179c3dc7e08e9e7e60de51129d3947',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='y', kind='raw_handle', required=True),
        NodeArgMeta(name='dat', kind='matrix_handle', required=True),
        ),
        defaults={},
    ),
}

#: Argument defaults, for FORM PREFILL ONLY. A default must never be sent
#: explicitly on the wire: adapt_args assigns it RAW, bypassing coercion.
DEFAULTS: dict[str, dict[str, object]] = {
    'compute_loss_level': {},
    'compute_loss_vol': {},
    'eval_dm_test': {'h': 1, 'power': 2},
    'eval_tsCV': {'h': 1, 'initial': 0},
    'run_arch_test': {'lags': 12, 'demean': False},
    'run_bg_test': {'order': 1},
    'run_bp_test': {'studentize': True},
    'run_mcs_procedure': {'alpha': 0.15, 'B': 1000, 'min_k': 3},
    'run_reset_test': {},
    'sr_crps_parametric': {'mean': 0, 'sd': 1, 'location': 0, 'scale': 1},
    'sr_crps_sample': {},
    'sr_crps_tailweighted': {},
    'sr_logs_parametric': {'mean': 0, 'sd': 1, 'location': 0, 'scale': 1},
    'sr_logs_sample': {},
    'sr_pit_sample': {},
}


@cache
def wire_model(fn: str) -> type[BaseModel]:
    """The model the ENGINE validates. Built on first use and cached."""
    return build_wire_model(NODE_META[fn])


@cache
def authoring_model(fn: str) -> type[BaseModel]:
    """The model a GRAPH EDITOR edits. Built on first use and cached."""
    return build_authoring_model(NODE_META[fn])
