# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.v1.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 2 for category 28-trade-gravity -- 11 nodes. No descriptions."""

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
    'ec_balassa': NodeMeta(
        fn='ec_balassa',
        category='28-trade-gravity',
        card_id=239,
        contract_hash='c-8d0c07e8630b490130082f2a69d8fd3f532669ee35425ecf974fd144592a44e8',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='df', kind='df_handle', required=True),
        NodeArgMeta(name='discrete', kind='boolean', required=False),
        NodeArgMeta(name='cutoff', kind='number', required=False),
        NodeArgMeta(name='country', kind='string', required=False),
        NodeArgMeta(name='product', kind='string', required=False),
        NodeArgMeta(name='value', kind='string', required=False),
        ),
        defaults={'discrete': True, 'cutoff': 1},
    ),
    'ec_complexity': NodeMeta(
        fn='ec_complexity',
        category='28-trade-gravity',
        card_id=239,
        contract_hash='c-963c4f1937346a8859f15414e15b25b1d5cdb86945e555c5651aa68215dafda6',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='df', kind='df_handle', required=True),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('fitness', 'reflections', 'eigenvalues', )),
        NodeArgMeta(name='iterations', kind='integer', required=False),
        NodeArgMeta(name='extremality', kind='number', required=False),
        NodeArgMeta(name='discrete', kind='boolean', required=False),
        NodeArgMeta(name='cutoff', kind='number', required=False),
        NodeArgMeta(name='country', kind='string', required=False),
        NodeArgMeta(name='product', kind='string', required=False),
        NodeArgMeta(name='value', kind='string', required=False),
        ),
        defaults={'iterations': 20, 'extremality': 1, 'discrete': True, 'cutoff': 1},
    ),
    'ec_proximity': NodeMeta(
        fn='ec_proximity',
        category='28-trade-gravity',
        card_id=239,
        contract_hash='c-a214667c13ea3490520a01e3c9af938b3f44d2bd3c10245b87ccdfb5abd537fc',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='df', kind='df_handle', required=True),
        NodeArgMeta(name='compute', kind='enum', required=False, enum=('both', 'country', 'product', )),
        NodeArgMeta(name='discrete', kind='boolean', required=False),
        NodeArgMeta(name='cutoff', kind='number', required=False),
        NodeArgMeta(name='country', kind='string', required=False),
        NodeArgMeta(name='product', kind='string', required=False),
        NodeArgMeta(name='value', kind='string', required=False),
        ),
        defaults={'discrete': True, 'cutoff': 1},
    ),
    'gr_bvu': NodeMeta(
        fn='gr_bvu',
        category='28-trade-gravity',
        card_id=237,
        contract_hash='c-1469ec8399ec6a30cfb6e7913c030a66a98a65d031eb9389fa344db6d22017a7',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='df', kind='df_handle', required=True),
        NodeArgMeta(name='dependent_variable', kind='string', required=True),
        NodeArgMeta(name='distance', kind='string', required=True),
        NodeArgMeta(name='income_origin', kind='string', required=True),
        NodeArgMeta(name='income_destination', kind='string', required=True),
        NodeArgMeta(name='code_origin', kind='string', required=True),
        NodeArgMeta(name='code_destination', kind='string', required=True),
        NodeArgMeta(name='additional_regressors', kind='series_codes', required=False),
        NodeArgMeta(name='robust', kind='boolean', required=False),
        ),
        defaults={'robust': False},
    ),
    'gr_fixed_effects': NodeMeta(
        fn='gr_fixed_effects',
        category='28-trade-gravity',
        card_id=237,
        contract_hash='c-f4a8276e01959db4d30f3642311dc35b3cbb1dd123ecfff1f3d3446566e23d7b',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='df', kind='df_handle', required=True),
        NodeArgMeta(name='dependent_variable', kind='string', required=True),
        NodeArgMeta(name='distance', kind='string', required=True),
        NodeArgMeta(name='code_origin', kind='string', required=True),
        NodeArgMeta(name='code_destination', kind='string', required=True),
        NodeArgMeta(name='additional_regressors', kind='series_codes', required=False),
        NodeArgMeta(name='robust', kind='boolean', required=False),
        ),
        defaults={'robust': False},
    ),
    'gr_ols': NodeMeta(
        fn='gr_ols',
        category='28-trade-gravity',
        card_id=237,
        contract_hash='c-5bb434b839642001de7711770b13ff154556f13b4b3603eecd852ee64d2a824d',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='df', kind='df_handle', required=True),
        NodeArgMeta(name='dependent_variable', kind='string', required=True),
        NodeArgMeta(name='distance', kind='string', required=True),
        NodeArgMeta(name='income_origin', kind='string', required=True),
        NodeArgMeta(name='income_destination', kind='string', required=True),
        NodeArgMeta(name='code_origin', kind='string', required=True),
        NodeArgMeta(name='code_destination', kind='string', required=True),
        NodeArgMeta(name='additional_regressors', kind='series_codes', required=False),
        NodeArgMeta(name='uie', kind='boolean', required=False),
        NodeArgMeta(name='robust', kind='boolean', required=False),
        ),
        defaults={'uie': False, 'robust': False},
    ),
    'gr_ppml': NodeMeta(
        fn='gr_ppml',
        category='28-trade-gravity',
        card_id=237,
        contract_hash='c-64b0a7461ef35ab932d95fa545a83ad116274dd568127bbbc3e60a05b0332daa',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='df', kind='df_handle', required=True),
        NodeArgMeta(name='dependent_variable', kind='string', required=True),
        NodeArgMeta(name='distance', kind='string', required=True),
        NodeArgMeta(name='additional_regressors', kind='series_codes', required=False),
        NodeArgMeta(name='robust', kind='boolean', required=False),
        ),
        defaults={'robust': False},
    ),
    'gr_tetrads': NodeMeta(
        fn='gr_tetrads',
        category='28-trade-gravity',
        card_id=237,
        contract_hash='c-36373a3736a587aa9719748993354d5795bee9a49d3ce8a3b40902227464c61b',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='df', kind='df_handle', required=True),
        NodeArgMeta(name='dependent_variable', kind='string', required=True),
        NodeArgMeta(name='distance', kind='string', required=True),
        NodeArgMeta(name='code_origin', kind='string', required=True),
        NodeArgMeta(name='code_destination', kind='string', required=True),
        NodeArgMeta(name='filter_origin', kind='string', required=True),
        NodeArgMeta(name='filter_destination', kind='string', required=True),
        NodeArgMeta(name='additional_regressors', kind='series_codes', required=True),
        NodeArgMeta(name='multiway', kind='boolean', required=False),
        ),
        defaults={'multiway': False},
    ),
    'pp_hdfeppml': NodeMeta(
        fn='pp_hdfeppml',
        category='28-trade-gravity',
        card_id=238,
        contract_hash='c-2425c112ded745b5a1b7e7935fbf05bdceda67fd86f91a9395103bcd18fa0240',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='dep', kind='string', required=True),
        NodeArgMeta(name='indep', kind='series_codes', required=True),
        NodeArgMeta(name='fixed', kind='raw', required=True),
        NodeArgMeta(name='cluster', kind='series_codes', required=False),
        NodeArgMeta(name='tol', kind='number', required=False),
        NodeArgMeta(name='hdfetol', kind='number', required=False),
        ),
        defaults={'tol': 1e-08, 'hdfetol': 0.0001},
    ),
    'pp_mlfitppml': NodeMeta(
        fn='pp_mlfitppml',
        category='28-trade-gravity',
        card_id=238,
        contract_hash='c-841d4a9ffe0aa82a6cd2ca3a880b9615a4e7faa19ef1bd0294e687797b1e2602',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='dep', kind='string', required=True),
        NodeArgMeta(name='indep', kind='series_codes', required=True),
        NodeArgMeta(name='fixed', kind='raw', required=True),
        NodeArgMeta(name='lambdas', kind='num_array', required=False),
        NodeArgMeta(name='penalty', kind='enum', required=False, enum=('lasso', 'ridge', )),
        NodeArgMeta(name='plugin', kind='boolean', required=False),
        NodeArgMeta(name='post', kind='boolean', required=False),
        NodeArgMeta(name='cluster', kind='series_codes', required=False),
        NodeArgMeta(name='seed', kind='integer', required=False),
        NodeArgMeta(name='hdfetol', kind='number', required=False),
        ),
        defaults={'plugin': False, 'post': False, 'seed': 1, 'hdfetol': 0.0001},
    ),
    'pp_penhdfeppml': NodeMeta(
        fn='pp_penhdfeppml',
        category='28-trade-gravity',
        card_id=238,
        contract_hash='c-95f259663a053797129c24560f322a5cce7bf5e107d00636728e22ba2758358d',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='dep', kind='string', required=True),
        NodeArgMeta(name='indep', kind='series_codes', required=True),
        NodeArgMeta(name='fixed', kind='raw', required=True),
        NodeArgMeta(name='lambda', kind='number', required=True),
        NodeArgMeta(name='penalty', kind='enum', required=False, enum=('lasso', 'ridge', )),
        NodeArgMeta(name='plugin', kind='boolean', required=False),
        NodeArgMeta(name='cluster', kind='series_codes', required=False),
        NodeArgMeta(name='hdfetol', kind='number', required=False),
        ),
        defaults={'plugin': False, 'hdfetol': 0.0001},
    ),
}

#: Argument defaults, for FORM PREFILL ONLY. A default must never be sent
#: explicitly on the wire: adapt_args assigns it RAW, bypassing coercion.
DEFAULTS: dict[str, dict[str, object]] = {
    'ec_balassa': {'discrete': True, 'cutoff': 1},
    'ec_complexity': {'iterations': 20, 'extremality': 1, 'discrete': True, 'cutoff': 1},
    'ec_proximity': {'discrete': True, 'cutoff': 1},
    'gr_bvu': {'robust': False},
    'gr_fixed_effects': {'robust': False},
    'gr_ols': {'uie': False, 'robust': False},
    'gr_ppml': {'robust': False},
    'gr_tetrads': {'multiway': False},
    'pp_hdfeppml': {'tol': 1e-08, 'hdfetol': 0.0001},
    'pp_mlfitppml': {'plugin': False, 'post': False, 'seed': 1, 'hdfetol': 0.0001},
    'pp_penhdfeppml': {'plugin': False, 'hdfetol': 0.0001},
}


@cache
def wire_model(fn: str) -> type[BaseModel]:
    """The model the ENGINE validates. Built on first use and cached."""
    return build_wire_model(NODE_META[fn])


@cache
def authoring_model(fn: str) -> type[BaseModel]:
    """The model a GRAPH EDITOR edits. Built on first use and cached."""
    return build_authoring_model(NODE_META[fn])
