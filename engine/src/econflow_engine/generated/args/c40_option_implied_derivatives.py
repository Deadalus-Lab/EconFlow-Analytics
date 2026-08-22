# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 2 for category 40-option-implied-derivatives -- 14 nodes. No descriptions."""

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
    'opt_price': NodeMeta(
        fn='opt_price',
        category='40-option-implied-derivatives',
        card_id=340,
        contract_hash='c2-c4812ae478beba3feb33a9294da6b3e6da9f594d28b2454bb3c31a31fd45a9a2',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='spot', kind='number', required=True),
        NodeArgMeta(name='strike', kind='number', required=True),
        NodeArgMeta(name='time_to_expiry', kind='number', required=True),
        NodeArgMeta(name='rate', kind='number', required=True),
        NodeArgMeta(name='volatility', kind='number', required=True),
        NodeArgMeta(name='option_type', kind='enum', required=True, enum=('call', 'put', )),
        NodeArgMeta(name='model', kind='enum', required=False, enum=('black_scholes', 'bachelier', 'black76', )),
        NodeArgMeta(name='dividend', kind='number', required=False),
        ),
        defaults={'model': 'black_scholes', 'dividend': 0.0},
    ),
    'opt_implied_volatility': NodeMeta(
        fn='opt_implied_volatility',
        category='40-option-implied-derivatives',
        card_id=340,
        contract_hash='c2-67ff7af35582f8bae36c19f3eff2d6ccd29df2c92c18017be6e4e9446809940c',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='price', kind='series_handle', required=True),
        NodeArgMeta(name='spot', kind='series_handle', required=True),
        NodeArgMeta(name='strike', kind='series_handle', required=True),
        NodeArgMeta(name='time_to_expiry', kind='series_handle', required=True),
        NodeArgMeta(name='rate', kind='series_handle', required=True),
        NodeArgMeta(name='option_type', kind='series_handle', required=True),
        NodeArgMeta(name='model', kind='enum', required=False, enum=('black_scholes', 'bachelier', 'black76', )),
        ),
        defaults={'model': 'black_scholes'},
    ),
    'opt_fit_surface': NodeMeta(
        fn='opt_fit_surface',
        category='40-option-implied-derivatives',
        card_id=341,
        contract_hash='c2-6a9444a23f50b45bab4b570f685c8f964f892e6b08ae37f5913a8c1b2f93ce7b',
        register_field='surface',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='strikes', kind='series_handle', required=True),
        NodeArgMeta(name='expiries', kind='series_handle', required=True),
        NodeArgMeta(name='implied_vols', kind='series_handle', required=True),
        NodeArgMeta(name='forward', kind='series_handle', required=True),
        NodeArgMeta(name='model', kind='enum', required=False, enum=('svi', 'ssvi', 'sabr', 'cubic_spline', )),
        NodeArgMeta(name='enforce_no_arbitrage', kind='boolean', required=False),
        ),
        defaults={'model': 'svi', 'enforce_no_arbitrage': True},
    ),
    'opt_surface_evaluate': NodeMeta(
        fn='opt_surface_evaluate',
        category='40-option-implied-derivatives',
        card_id=341,
        contract_hash='c2-9e6a5bd123badd57e8d7f6516a13cf345f85885729d22607a607d30e3eeb21f7',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='surface', kind='raw_handle', required=True),
        NodeArgMeta(name='strikes', kind='num_array', required=True),
        NodeArgMeta(name='expiries', kind='num_array', required=True),
        ),
        defaults={},
    ),
    'opt_arbitrage_check': NodeMeta(
        fn='opt_arbitrage_check',
        category='40-option-implied-derivatives',
        card_id=341,
        contract_hash='c2-9f20ca956639772d8a61d008e10a66d1d9bcd72d2efb4ac8f9bc453d3a45ace4',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='surface', kind='raw_handle', required=True),
        NodeArgMeta(name='grid_size', kind='integer', required=False),
        ),
        defaults={'grid_size': 100},
    ),
    'opt_risk_neutral_density': NodeMeta(
        fn='opt_risk_neutral_density',
        category='40-option-implied-derivatives',
        card_id=342,
        contract_hash='c2-98f593a2f220c257918815f0f26726bb2acb179322789ccae29692a7f102735f',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='strikes', kind='series_handle', required=True),
        NodeArgMeta(name='prices', kind='series_handle', required=True),
        NodeArgMeta(name='forward', kind='number', required=True),
        NodeArgMeta(name='time_to_expiry', kind='number', required=True),
        NodeArgMeta(name='rate', kind='number', required=True),
        NodeArgMeta(name='smoothing', kind='enum', required=False, enum=('none', 'spline', 'svi', 'kernel', )),
        NodeArgMeta(name='grid_size', kind='integer', required=False),
        ),
        defaults={'smoothing': 'svi', 'grid_size': 500},
    ),
    'opt_model_free_variance': NodeMeta(
        fn='opt_model_free_variance',
        category='40-option-implied-derivatives',
        card_id=343,
        contract_hash='c2-7b95d4a43367dacc4311d4f37294aa4eb8ede4059da69a3d5b88a1fa96ac9407',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='strikes', kind='series_handle', required=True),
        NodeArgMeta(name='prices', kind='series_handle', required=True),
        NodeArgMeta(name='option_type', kind='series_handle', required=True),
        NodeArgMeta(name='forward', kind='number', required=True),
        NodeArgMeta(name='time_to_expiry', kind='number', required=True),
        NodeArgMeta(name='rate', kind='number', required=True),
        ),
        defaults={},
    ),
    'opt_variance_risk_premium': NodeMeta(
        fn='opt_variance_risk_premium',
        category='40-option-implied-derivatives',
        card_id=343,
        contract_hash='c2-19919b1aea3529b1948347b49e17ebfcd0587975a6afbdd68bc55d2cd74adf42',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='implied_variance', kind='series_handle', required=True),
        NodeArgMeta(name='realised_variance', kind='series_handle', required=True),
        NodeArgMeta(name='horizon', kind='integer', required=False),
        ),
        defaults={'horizon': 21},
    ),
    'opt_risk_neutral_moments': NodeMeta(
        fn='opt_risk_neutral_moments',
        category='40-option-implied-derivatives',
        card_id=344,
        contract_hash='c2-6771a1af9af942ca9b9aa10f4c982c951133de6c1e5f13bfadfde9a188c42d83',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='strikes', kind='series_handle', required=True),
        NodeArgMeta(name='prices', kind='series_handle', required=True),
        NodeArgMeta(name='option_type', kind='series_handle', required=True),
        NodeArgMeta(name='forward', kind='number', required=True),
        NodeArgMeta(name='time_to_expiry', kind='number', required=True),
        NodeArgMeta(name='rate', kind='number', required=True),
        ),
        defaults={},
    ),
    'opt_implied_term_structure': NodeMeta(
        fn='opt_implied_term_structure',
        category='40-option-implied-derivatives',
        card_id=345,
        contract_hash='c2-d82b56aee0e4d1a1c4208cc0a488dfc72fc7a306316cc3179819ea790072e5d1',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='maturities', kind='num_array', required=True),
        NodeArgMeta(name='implied_variance', kind='num_array', required=True),
        ),
        defaults={},
    ),
    'opt_density_fan': NodeMeta(
        fn='opt_density_fan',
        category='40-option-implied-derivatives',
        card_id=345,
        contract_hash='c2-659e46079a8dc5198cf11afa4c1b5e76d5f292881c824bd7f3339979c167ef70',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='densities', kind='matrix_handle', required=True),
        NodeArgMeta(name='grid', kind='num_array', required=True),
        NodeArgMeta(name='quantiles', kind='num_array', required=False),
        ),
        defaults={'quantiles': [0.05, 0.25, 0.5, 0.75, 0.95]},
    ),
    'opt_sv_calibrate': NodeMeta(
        fn='opt_sv_calibrate',
        category='40-option-implied-derivatives',
        card_id=346,
        contract_hash='c2-18fbad6f4ea9b068d701c9d1664a4accc99b901990ce737b92e4b423c612293f',
        register_field='model',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='strikes', kind='series_handle', required=True),
        NodeArgMeta(name='expiries', kind='series_handle', required=True),
        NodeArgMeta(name='implied_vols', kind='series_handle', required=True),
        NodeArgMeta(name='forward', kind='series_handle', required=True),
        NodeArgMeta(name='model', kind='enum', required=False, enum=('heston', 'lognormal_sv', 'rough_bergomi', 'sabr', )),
        NodeArgMeta(name='n_starts', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=False),
        ),
        defaults={'model': 'heston', 'n_starts': 5},
    ),
    'opt_sv_price': NodeMeta(
        fn='opt_sv_price',
        category='40-option-implied-derivatives',
        card_id=346,
        contract_hash='c2-9234e3e64acbdae3ff98ee916739e646f768619dc5729756152449dc18bef6e3',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='model', kind='raw_handle', required=True),
        NodeArgMeta(name='strikes', kind='num_array', required=True),
        NodeArgMeta(name='expiries', kind='num_array', required=True),
        ),
        defaults={},
    ),
    'opt_sv_simulate': NodeMeta(
        fn='opt_sv_simulate',
        category='40-option-implied-derivatives',
        card_id=346,
        contract_hash='c2-2eabd5ea476a47cef0a0a90b7c7ce404407ab6fb75edf8e180097c5128cfdba4',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='model', kind='raw_handle', required=True),
        NodeArgMeta(name='n_paths', kind='integer', required=False),
        NodeArgMeta(name='n_steps', kind='integer', required=False),
        NodeArgMeta(name='scheme', kind='enum', required=False, enum=('euler', 'milstein', 'qe', 'exact', )),
        NodeArgMeta(name='seed', kind='integer', required=True),
        ),
        defaults={'n_paths': 10000, 'n_steps': 252, 'scheme': 'qe'},
    ),
}

#: Argument defaults, for FORM PREFILL ONLY. A default must never be sent
#: explicitly on the wire: adapt_args assigns it RAW, bypassing coercion.
DEFAULTS: dict[str, dict[str, object]] = {
    'opt_price': {'model': 'black_scholes', 'dividend': 0.0},
    'opt_implied_volatility': {'model': 'black_scholes'},
    'opt_fit_surface': {'model': 'svi', 'enforce_no_arbitrage': True},
    'opt_surface_evaluate': {},
    'opt_arbitrage_check': {'grid_size': 100},
    'opt_risk_neutral_density': {'smoothing': 'svi', 'grid_size': 500},
    'opt_model_free_variance': {},
    'opt_variance_risk_premium': {'horizon': 21},
    'opt_risk_neutral_moments': {},
    'opt_implied_term_structure': {},
    'opt_density_fan': {'quantiles': [0.05, 0.25, 0.5, 0.75, 0.95]},
    'opt_sv_calibrate': {'model': 'heston', 'n_starts': 5},
    'opt_sv_price': {},
    'opt_sv_simulate': {'n_paths': 10000, 'n_steps': 252, 'scheme': 'qe'},
}


@cache
def wire_model(fn: str) -> type[BaseModel]:
    """The model the ENGINE validates. Built on first use and cached."""
    return build_wire_model(NODE_META[fn])


@cache
def authoring_model(fn: str) -> type[BaseModel]:
    """The model a GRAPH EDITOR edits. Built on first use and cached."""
    return build_authoring_model(NODE_META[fn])
