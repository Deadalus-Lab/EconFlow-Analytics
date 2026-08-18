# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.v1.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 2 for category 16-limited-dependent -- 4 nodes. No descriptions."""

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
    'alpaca_apes': NodeMeta(
        fn='alpaca_apes',
        category='16-limited-dependent',
        card_id=206,
        contract_hash='c-add714cf81a005a371d623c9c791e87fb4be672e36c727edc3f7d7c4f09a95f7',
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
    'alpaca_feglm': NodeMeta(
        fn='alpaca_feglm',
        category='16-limited-dependent',
        card_id=206,
        contract_hash='c-9275ca2881b04fc57d14e6cd039dd0852470352c0cec2a366f93ac0b9db6355b',
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
    'run_feglm_binom': NodeMeta(
        fn='run_feglm_binom',
        category='16-limited-dependent',
        card_id=83,
        contract_hash='c-15e947b6a21d64b760f98902986cc2f2b4fe67ae4268d8ad519f017becee0b6d',
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
        contract_hash='c-baa572eca1d5ff254730d6d6beedb7b3f934600b589db8d278df0acbffa5b1dd',
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
}

#: Argument defaults, for FORM PREFILL ONLY. A default must never be sent
#: explicitly on the wire: adapt_args assigns it RAW, bypassing coercion.
DEFAULTS: dict[str, dict[str, object]] = {
    'alpaca_apes': {'weak_exo': False},
    'alpaca_feglm': {'bias_correct': False, 'L': 0},
    'run_feglm_binom': {},
    'run_roc': {'ci': True, 'conf_level': 0.95},
}


@cache
def wire_model(fn: str) -> type[BaseModel]:
    """The model the ENGINE validates. Built on first use and cached."""
    return build_wire_model(NODE_META[fn])


@cache
def authoring_model(fn: str) -> type[BaseModel]:
    """The model a GRAPH EDITOR edits. Built on first use and cached."""
    return build_authoring_model(NODE_META[fn])
