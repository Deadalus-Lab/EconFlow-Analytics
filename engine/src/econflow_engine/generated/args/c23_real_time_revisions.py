# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.v1.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 2 for category 23-real-time-revisions -- 5 nodes. No descriptions."""

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
        contract_hash='c-828d258ab255cecb989e3392f46896c4108790c1a456393c50a8b95e99214306',
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
        contract_hash='c-e1ef2e8b5f9b8aad28954e337524734264539cdf83edc3330f7d04f0fe6503d1',
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
        contract_hash='c-18e1433893ecfe8dd9ec7860002d757a8ad87fbc0bb5b9a7e43164762eb613c6',
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
        contract_hash='c-a59af88c5f09a4b08ae453a01122def346cfb087cf49b0a2d286d52c51ea4d5a',
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
        contract_hash='c-7038b36e8f7d24d3a281989557af556315fc5e08266862ceff85e6f601da5973',
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
}

#: Argument defaults, for FORM PREFILL ONLY. A default must never be sent
#: explicitly on the wire: adapt_args assigns it RAW, bypassing coercion.
DEFAULTS: dict[str, dict[str, object]] = {
    'analyze_revisions': {'n_releases': 3, 'degree': 5},
    'build_revision_triangle': {},
    'compute_revisions': {'interval': 1},
    'first_efficient_release': {'n_releases': 5, 'significance': 0.05, 'robust': True, 'test_all': False},
    'nowcast_revisions': {'n_releases': 6, 'h': 0, 'seed': 1},
}


@cache
def wire_model(fn: str) -> type[BaseModel]:
    """The model the ENGINE validates. Built on first use and cached."""
    return build_wire_model(NODE_META[fn])


@cache
def authoring_model(fn: str) -> type[BaseModel]:
    """The model a GRAPH EDITOR edits. Built on first use and cached."""
    return build_authoring_model(NODE_META[fn])
