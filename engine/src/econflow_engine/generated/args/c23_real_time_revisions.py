# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 2 for category 23-real-time-revisions -- 9 nodes. No descriptions."""

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
    'analyze_revisions': NodeMeta(
        fn='analyze_revisions',
        category='23-real-time-revisions',
        card_id=229,
        contract_hash='c2-6f3454742755c3abeb7f8c1f676b0465a8eda63180e7eb81c63d653190278723',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='df', kind='df_handle', required=True),
        NodeArgMeta(name='n_releases', kind='integer', required=False),
        NodeArgMeta(name='final_release', kind='string', required=False),
        NodeArgMeta(name='degree', kind='integer', required=False),
        ),
        defaults={'n_releases': 3, 'degree': 5},
    ),
    'build_revision_triangle': NodeMeta(
        fn='build_revision_triangle',
        category='23-real-time-revisions',
        card_id=229,
        contract_hash='c2-488ae8912125c37bc1e8b2a19df00dbe203219684a7870f985805928355402be',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='df', kind='df_handle', required=True),
        ),
        defaults={},
    ),
    'compute_revisions': NodeMeta(
        fn='compute_revisions',
        category='23-real-time-revisions',
        card_id=229,
        contract_hash='c2-1476c084bb0bc1f63fd05552924de39195157d48b16ed7853cb95f0535033d6f',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='df', kind='df_handle', required=True),
        NodeArgMeta(name='mode', kind='enum', required=False, enum=('interval', 'nth_release', 'ref_date', )),
        NodeArgMeta(name='interval', kind='integer', required=False),
        NodeArgMeta(name='nth_release', kind='string', required=False),
        NodeArgMeta(name='ref_date', kind='string', required=False),
        ),
        defaults={'interval': 1},
    ),
    'first_efficient_release': NodeMeta(
        fn='first_efficient_release',
        category='23-real-time-revisions',
        card_id=229,
        contract_hash='c2-b610aaebb562fc782cb7534712ea49c2e8278a89b5137fa1d429cdc8f1fdf53e',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='df', kind='df_handle', required=True),
        NodeArgMeta(name='n_releases', kind='integer', required=False),
        NodeArgMeta(name='final_release', kind='string', required=False),
        NodeArgMeta(name='significance', kind='number', required=False),
        NodeArgMeta(name='robust', kind='boolean', required=False),
        NodeArgMeta(name='test_all', kind='boolean', required=False),
        ),
        defaults={'n_releases': 5, 'significance': 0.05, 'robust': True, 'test_all': False},
    ),
    'nowcast_revisions': NodeMeta(
        fn='nowcast_revisions',
        category='23-real-time-revisions',
        card_id=229,
        contract_hash='c2-7d6347afad3dc424bcbb8458d3a7cc5e29bfb7cd1e1a69c14818e455dd1c7062',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='df', kind='df_handle', required=True),
        NodeArgMeta(name='e', kind='integer', required=True),
        NodeArgMeta(name='n_releases', kind='integer', required=False),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('jvn', 'kk', )),
        NodeArgMeta(name='h', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=False),
        ),
        defaults={'n_releases': 6, 'h': 0, 'seed': 1},
    ),
    'rt_construct_vintages': NodeMeta(
        fn='rt_construct_vintages',
        category='23-real-time-revisions',
        card_id=565,
        contract_hash='c2-af70dfc7c76a7368a00ab1f59eb616d038ce23ebba17289a489c8d925b084423',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='publication_lags', kind='df_handle', required=True),
        NodeArgMeta(name='vintage_dates', kind='series_codes', required=False),
        NodeArgMeta(name='calendar', kind='df_handle', required=False),
        ),
        defaults={},
    ),
    'rt_realtime_evaluation': NodeMeta(
        fn='rt_realtime_evaluation',
        category='23-real-time-revisions',
        card_id=566,
        contract_hash='c2-910dd1e69e16dc1c9e5f6902b606d68b57b067f60e6aae9276640bac3ba7afdf',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='forecasts', kind='df_handle', required=True),
        NodeArgMeta(name='vintages', kind='df_handle', required=True),
        NodeArgMeta(name='conventions', kind='series_codes', required=False),
        NodeArgMeta(name='fixed_lag', kind='integer', required=False),
        NodeArgMeta(name='metrics', kind='series_codes', required=False),
        ),
        defaults={'fixed_lag': 12},
    ),
    'rt_revision_diagnostics': NodeMeta(
        fn='rt_revision_diagnostics',
        category='23-real-time-revisions',
        card_id=567,
        contract_hash='c2-40e984223f236a541ceddaeeb82c5bc4c4caecd38c7a9c4e0bb7099ecb1aa308',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='y', kind='series_handle', required=True),
        NodeArgMeta(name='n_spans', kind='integer', required=False),
        NodeArgMeta(name='span_length', kind='integer', required=False),
        NodeArgMeta(name='threshold', kind='number', required=False),
        ),
        defaults={'n_spans': 4, 'span_length': 8, 'threshold': 3.0},
    ),
    'rt_read_vintages': NodeMeta(
        fn='rt_read_vintages',
        category='23-real-time-revisions',
        card_id=568,
        contract_hash='c2-9b41082b9632fd3133eea656b6150b5a84fb2495c3af90e8c1b75a50f23e4b66',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='path', kind='path', required=True),
        NodeArgMeta(name='series', kind='series_codes', required=True),
        NodeArgMeta(name='vintage_dates', kind='series_codes', required=False),
        NodeArgMeta(name='format', kind='enum', required=False, enum=('long', 'wide', 'triangle', )),
        ),
        defaults={'format': 'long'},
    ),
}

#: Argument defaults, for FORM PREFILL ONLY. A default must never be sent
#: explicitly on the wire: adapt_args assigns it RAW, bypassing coercion.
DEFAULTS: dict[str, dict[str, object]] = {
    'analyze_revisions': {'n_releases': 3, 'degree': 5},
    'build_revision_triangle': {},
    'compute_revisions': {'interval': 1},
    'first_efficient_release': {'n_releases': 5, 'significance': 0.05, 'robust': True, 'test_all': False},
    'nowcast_revisions': {'n_releases': 6, 'h': 0, 'seed': 1},
    'rt_construct_vintages': {},
    'rt_realtime_evaluation': {'fixed_lag': 12},
    'rt_revision_diagnostics': {'n_spans': 4, 'span_length': 8, 'threshold': 3.0},
    'rt_read_vintages': {'format': 'long'},
}


@cache
def wire_model(fn: str) -> type[BaseModel]:
    """The model the ENGINE validates. Built on first use and cached."""
    return build_wire_model(NODE_META[fn])


@cache
def authoring_model(fn: str) -> type[BaseModel]:
    """The model a GRAPH EDITOR edits. Built on first use and cached."""
    return build_authoring_model(NODE_META[fn])
