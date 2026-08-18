# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.v1.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 2 for category 11-decomposition-accounting -- 7 nodes. No descriptions."""

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
    'ox_decompose': NodeMeta(
        fn='ox_decompose',
        category='11-decomposition-accounting',
        card_id=63,
        contract_hash='c-b0bb19e426dc5c6a03ca89491fd6b214edd13c90a11bcd8ae13fd4b8b3d3ab49',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='formula', kind='formula', required=True),
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='n_bootstrap', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=False),
        ),
        defaults={'n_bootstrap': 100, 'seed': 42},
    ),
    'pi_bilateral': NodeMeta(
        fn='pi_bilateral',
        category='11-decomposition-accounting',
        card_id=190,
        contract_hash='c-35f082e37d32ca0ebba16c4d86234a000d00a44524fda6d0f70cffa1eea0a84e',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='start', kind='string', required=True),
        NodeArgMeta(name='end', kind='string', required=True),
        NodeArgMeta(name='formula', kind='enum', required=False, enum=('jevons', 'dutot', 'carli', 'laspeyres', 'paasche', 'fisher', 'tornqvist', 'walsh', )),
        NodeArgMeta(name='interval', kind='boolean', required=False),
        ),
        defaults={'interval': False},
    ),
    'pi_contributions': NodeMeta(
        fn='pi_contributions',
        category='11-decomposition-accounting',
        card_id=190,
        contract_hash='c-323ec0439e80ec178115f7ddf97c2124382be95c0c1184ee506b9fe33956ea78',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='start', kind='string', required=True),
        NodeArgMeta(name='end', kind='string', required=True),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('bennet', 'montgomery', )),
        NodeArgMeta(name='matched', kind='boolean', required=False),
        NodeArgMeta(name='interval', kind='boolean', required=False),
        NodeArgMeta(name='prec', kind='integer', required=False),
        ),
        defaults={'matched': False, 'interval': False, 'prec': 2},
    ),
    'pi_multilateral': NodeMeta(
        fn='pi_multilateral',
        category='11-decomposition-accounting',
        card_id=190,
        contract_hash='c-61ae108282dc4fb4428c174813fa193394197b6446e449ff61cb077846728bdf',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='start', kind='string', required=True),
        NodeArgMeta(name='end', kind='string', required=True),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('geks', 'ccdi', 'gk', 'tpd', )),
        NodeArgMeta(name='window', kind='integer', required=False),
        NodeArgMeta(name='wstart', kind='string', required=False),
        ),
        defaults={'window': 13},
    ),
    'pi_splice': NodeMeta(
        fn='pi_splice',
        category='11-decomposition-accounting',
        card_id=190,
        contract_hash='c-b61b674c0ab3dce3554435093146c6c4b91632413946d28fdd879df2c3875620',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='start', kind='string', required=True),
        NodeArgMeta(name='end', kind='string', required=True),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('geks', 'ccdi', 'gk', 'tpd', )),
        NodeArgMeta(name='window', kind='integer', required=False),
        NodeArgMeta(name='splice', kind='enum', required=False, enum=('movement', 'window', 'half', 'mean', 'window_published', 'half_published', 'mean_published', )),
        NodeArgMeta(name='interval', kind='boolean', required=False),
        ),
        defaults={'window': 13, 'interval': False},
    ),
    'prod_fareprim': NodeMeta(
        fn='prod_fareprim',
        category='11-decomposition-accounting',
        card_id=62,
        contract_hash='c-39c49cf3208e8e671dd9c19ccd6c26acce55922c4789a48e62f646e929c3eade',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='id_var', kind='string', required=True),
        NodeArgMeta(name='time_var', kind='string', required=True),
        NodeArgMeta(name='x_vars', kind='series_codes', required=True),
        NodeArgMeta(name='y_vars', kind='series_codes', required=True),
        NodeArgMeta(name='w_vars', kind='series_codes', required=False),
        NodeArgMeta(name='p_vars', kind='series_codes', required=False),
        NodeArgMeta(name='tech_change', kind='boolean', required=False),
        NodeArgMeta(name='tech_reg', kind='boolean', required=False),
        NodeArgMeta(name='rts', kind='enum', required=False, enum=('vrs', 'crs', 'nirs', 'ndrs', )),
        NodeArgMeta(name='orientation', kind='enum', required=False, enum=('out', 'in', 'in-out', )),
        NodeArgMeta(name='scaled', kind='boolean', required=False),
        NodeArgMeta(name='shadow', kind='boolean', required=False),
        ),
        defaults={'tech_change': True, 'tech_reg': True, 'scaled': True, 'shadow': False},
    ),
    'prod_malmquist': NodeMeta(
        fn='prod_malmquist',
        category='11-decomposition-accounting',
        card_id=62,
        contract_hash='c-ac698516b399c8dc2e4d6a36e2e736724131376f47fecc01663477926d10f892',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='id_var', kind='string', required=True),
        NodeArgMeta(name='time_var', kind='string', required=True),
        NodeArgMeta(name='x_vars', kind='series_codes', required=True),
        NodeArgMeta(name='y_vars', kind='series_codes', required=True),
        NodeArgMeta(name='rts', kind='enum', required=False, enum=('vrs', 'crs', 'nirs', 'ndrs', )),
        NodeArgMeta(name='orientation', kind='enum', required=False, enum=('out', 'in', )),
        NodeArgMeta(name='tech_reg', kind='boolean', required=False),
        NodeArgMeta(name='scaled', kind='boolean', required=False),
        ),
        defaults={'tech_reg': True, 'scaled': True},
    ),
}

#: Argument defaults, for FORM PREFILL ONLY. A default must never be sent
#: explicitly on the wire: adapt_args assigns it RAW, bypassing coercion.
DEFAULTS: dict[str, dict[str, object]] = {
    'ox_decompose': {'n_bootstrap': 100, 'seed': 42},
    'pi_bilateral': {'interval': False},
    'pi_contributions': {'matched': False, 'interval': False, 'prec': 2},
    'pi_multilateral': {'window': 13},
    'pi_splice': {'window': 13, 'interval': False},
    'prod_fareprim': {'tech_change': True, 'tech_reg': True, 'scaled': True, 'shadow': False},
    'prod_malmquist': {'tech_reg': True, 'scaled': True},
}


@cache
def wire_model(fn: str) -> type[BaseModel]:
    """The model the ENGINE validates. Built on first use and cached."""
    return build_wire_model(NODE_META[fn])


@cache
def authoring_model(fn: str) -> type[BaseModel]:
    """The model a GRAPH EDITOR edits. Built on first use and cached."""
    return build_authoring_model(NODE_META[fn])
