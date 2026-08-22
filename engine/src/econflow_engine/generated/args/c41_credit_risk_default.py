# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 2 for category 41-credit-risk-default -- 18 nodes. No descriptions."""

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
    'cr_distance_to_default': NodeMeta(
        fn='cr_distance_to_default',
        category='41-credit-risk-default',
        card_id=347,
        contract_hash='c2-065a8bef85ba5a4096a7456e60681c3738083d285f089adb50ea7c42603c5c34',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='equity_value', kind='series_handle', required=True),
        NodeArgMeta(name='equity_volatility', kind='series_handle', required=True),
        NodeArgMeta(name='debt', kind='series_handle', required=True),
        NodeArgMeta(name='rate', kind='series_handle', required=True),
        NodeArgMeta(name='horizon', kind='number', required=False),
        NodeArgMeta(name='barrier', kind='enum', required=False, enum=('total_debt', 'short_plus_half_long', 'short_term', )),
        ),
        defaults={'horizon': 1.0, 'barrier': 'short_plus_half_long'},
    ),
    'cr_merton_pd': NodeMeta(
        fn='cr_merton_pd',
        category='41-credit-risk-default',
        card_id=347,
        contract_hash='c2-c3611463125605972e965d154fa6454f2ee69502158bd4697302652467533f43',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='distance_to_default', kind='series_handle', required=True),
        NodeArgMeta(name='mapping', kind='enum', required=False, enum=('normal', 'empirical', )),
        NodeArgMeta(name='empirical_map', kind='df_handle', required=False),
        ),
        defaults={'mapping': 'normal'},
    ),
    'cr_transition_matrix': NodeMeta(
        fn='cr_transition_matrix',
        category='41-credit-risk-default',
        card_id=348,
        contract_hash='c2-a3577ebde0e5f89f4e983b6b53a2ef86b634e0712d29b01af66d5dc39cec7b22',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='id', kind='string', required=True),
        NodeArgMeta(name='state', kind='string', required=True),
        NodeArgMeta(name='date', kind='string', required=True),
        NodeArgMeta(name='estimator', kind='enum', required=False, enum=('cohort', 'duration', )),
        NodeArgMeta(name='horizon', kind='number', required=False),
        ),
        defaults={'estimator': 'duration', 'horizon': 1.0},
    ),
    'cr_generator': NodeMeta(
        fn='cr_generator',
        category='41-credit-risk-default',
        card_id=348,
        contract_hash='c2-08c46cc3c64f8ebbeebfdc6df466a994c24408079e2e32fc6025a32d73fff413',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='transition_matrix', kind='matrix_handle', required=True),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('log', 'qo', 'wa', 'dae', )),
        ),
        defaults={'method': 'qo'},
    ),
    'cr_stationary_distribution': NodeMeta(
        fn='cr_stationary_distribution',
        category='41-credit-risk-default',
        card_id=348,
        contract_hash='c2-66405c1f7c1d4fd0c4f5440e01296d1da2bd32ca3f415e9de946838471e1081a',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='transition_matrix', kind='matrix_handle', required=True),
        ),
        defaults={},
    ),
    'cr_optimal_binning': NodeMeta(
        fn='cr_optimal_binning',
        category='41-credit-risk-default',
        card_id=349,
        contract_hash='c2-e8ceaa9047e9384c196865353f47c64ec1a9afffc55c0cae66e79d74aabc90f9',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='x', kind='series_handle', required=True),
        NodeArgMeta(name='y', kind='series_handle', required=True),
        NodeArgMeta(name='monotonic_trend', kind='enum', required=False, enum=('auto', 'ascending', 'descending', 'convex', 'concave', 'none', )),
        NodeArgMeta(name='max_bins', kind='integer', required=False),
        NodeArgMeta(name='min_bin_size', kind='number', required=False),
        ),
        defaults={'monotonic_trend': 'auto', 'max_bins': 10, 'min_bin_size': 0.05},
    ),
    'cr_woe_transform': NodeMeta(
        fn='cr_woe_transform',
        category='41-credit-risk-default',
        card_id=349,
        contract_hash='c2-2e3d03312c59c3ca9bed1050f8f82084425949fe8d9a6784191b210ee37a1508',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='x', kind='series_handle', required=True),
        NodeArgMeta(name='y', kind='series_handle', required=True),
        NodeArgMeta(name='bins', kind='num_array', required=False),
        NodeArgMeta(name='smoothing', kind='number', required=False),
        ),
        defaults={'smoothing': 0.5},
    ),
    'cr_scorecard': NodeMeta(
        fn='cr_scorecard',
        category='41-credit-risk-default',
        card_id=349,
        contract_hash='c2-5a736fcabfdcc1705f1f69fd68a95d38e7f00c15e1feb9df2a19ee70e7acb842',
        register_field='fit',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='y', kind='string', required=True),
        NodeArgMeta(name='covariates', kind='series_codes', required=False),
        NodeArgMeta(name='base_points', kind='number', required=False),
        NodeArgMeta(name='pdo', kind='number', required=False),
        ),
        defaults={'base_points': 600.0, 'pdo': 20.0},
    ),
    'cr_discrimination': NodeMeta(
        fn='cr_discrimination',
        category='41-credit-risk-default',
        card_id=350,
        contract_hash='c2-cfb68f974eb0c8f93dda1ec9ee35433982f16462d2157330382bad07d72ea583',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='y', kind='series_handle', required=True),
        NodeArgMeta(name='score', kind='series_handle', required=True),
        ),
        defaults={},
    ),
    'cr_calibration': NodeMeta(
        fn='cr_calibration',
        category='41-credit-risk-default',
        card_id=350,
        contract_hash='c2-f44291d977ddac6fc9ab28ad9b00f2a8c4525fca616134d17881a759cfc7bbf2',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='y', kind='series_handle', required=True),
        NodeArgMeta(name='pd', kind='series_handle', required=True),
        NodeArgMeta(name='n_bins', kind='integer', required=False),
        NodeArgMeta(name='strategy', kind='enum', required=False, enum=('quantile', 'uniform', )),
        ),
        defaults={'n_bins': 10, 'strategy': 'quantile'},
    ),
    'cr_grade_test': NodeMeta(
        fn='cr_grade_test',
        category='41-credit-risk-default',
        card_id=350,
        contract_hash='c2-cde168682bb04769003fe218d46772febbd5d066d503c7d99087558a2f1a0ea9',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='y', kind='series_handle', required=True),
        NodeArgMeta(name='grade', kind='series_handle', required=True),
        NodeArgMeta(name='grade_pd', kind='series_handle', required=True),
        NodeArgMeta(name='alpha', kind='number', required=False),
        ),
        defaults={'alpha': 0.05},
    ),
    'cr_lgd_model': NodeMeta(
        fn='cr_lgd_model',
        category='41-credit-risk-default',
        card_id=351,
        contract_hash='c2-67f67d41dc8a5529d5635f53e9d6c6e317e9ad1e5a61c2b98f57945313fe5df6',
        register_field='fit',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='lgd', kind='string', required=True),
        NodeArgMeta(name='covariates', kind='series_codes', required=False),
        NodeArgMeta(name='model', kind='enum', required=False, enum=('beta', 'fractional', 'two_part', 'tobit', 'linear', )),
        NodeArgMeta(name='downturn', kind='string', required=False),
        ),
        defaults={'model': 'fractional'},
    ),
    'cr_ead_model': NodeMeta(
        fn='cr_ead_model',
        category='41-credit-risk-default',
        card_id=351,
        contract_hash='c2-163539e9c1a4c9307ef482e165eb52c771bcd2f09c0500303af3fd444e146480',
        register_field='fit',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='ccf', kind='string', required=True),
        NodeArgMeta(name='covariates', kind='series_codes', required=False),
        NodeArgMeta(name='model', kind='enum', required=False, enum=('beta', 'fractional', 'two_part', 'linear', )),
        ),
        defaults={'model': 'fractional'},
    ),
    'cr_lifetime_pd': NodeMeta(
        fn='cr_lifetime_pd',
        category='41-credit-risk-default',
        card_id=352,
        contract_hash='c2-dc5b8547fb7c9b3a5d4f12f67373e3f1876e29fc5d70465a1d6ab9244aa0c238',
        register_field='fit',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='time', kind='string', required=True),
        NodeArgMeta(name='event', kind='string', required=True),
        NodeArgMeta(name='covariates', kind='series_codes', required=False),
        NodeArgMeta(name='horizon', kind='integer', required=False),
        NodeArgMeta(name='model', kind='enum', required=False, enum=('cox', 'discrete_cloglog', 'weibull', 'piecewise', )),
        ),
        defaults={'horizon': 10, 'model': 'cox'},
    ),
    'cr_pd_scenario': NodeMeta(
        fn='cr_pd_scenario',
        category='41-credit-risk-default',
        card_id=352,
        contract_hash='c2-2e2ac7cbec7598aa8a5e0c0021751954888e315044c66899e945a011d6c5c173',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='fit', kind='raw_handle', required=True),
        NodeArgMeta(name='scenarios', kind='df_handle', required=True),
        NodeArgMeta(name='weights', kind='num_array', required=False),
        ),
        defaults={},
    ),
    'cr_vasicek_loss': NodeMeta(
        fn='cr_vasicek_loss',
        category='41-credit-risk-default',
        card_id=353,
        contract_hash='c2-a9ad5054666b9ab8408871b16a3af451b1a29f22c381057a40df06a32edc0afc',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='pd', kind='series_handle', required=True),
        NodeArgMeta(name='lgd', kind='series_handle', required=True),
        NodeArgMeta(name='exposure', kind='series_handle', required=True),
        NodeArgMeta(name='asset_correlation', kind='number', required=True),
        NodeArgMeta(name='confidence', kind='number', required=False),
        ),
        defaults={'confidence': 0.999},
    ),
    'cr_credit_monte_carlo': NodeMeta(
        fn='cr_credit_monte_carlo',
        category='41-credit-risk-default',
        card_id=353,
        contract_hash='c2-9893b18ca7ba1368f0c5525674b1903c531391a0df7aa2178eed926e05e556c7',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='pd', kind='series_handle', required=True),
        NodeArgMeta(name='lgd', kind='series_handle', required=True),
        NodeArgMeta(name='exposure', kind='series_handle', required=True),
        NodeArgMeta(name='factor_loadings', kind='matrix_handle', required=True),
        NodeArgMeta(name='n_simulations', kind='integer', required=False),
        NodeArgMeta(name='confidence', kind='number', required=False),
        NodeArgMeta(name='seed', kind='integer', required=True),
        ),
        defaults={'n_simulations': 100000, 'confidence': 0.999},
    ),
    'cr_concentration': NodeMeta(
        fn='cr_concentration',
        category='41-credit-risk-default',
        card_id=353,
        contract_hash='c2-4c05eff56d10125af108c2d2b4dc57fea80c4d6da64f64972edf378a0875ce38',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='exposure', kind='series_handle', required=True),
        NodeArgMeta(name='pd', kind='series_handle', required=False),
        NodeArgMeta(name='sector', kind='series_handle', required=False),
        ),
        defaults={},
    ),
}

#: Argument defaults, for FORM PREFILL ONLY. A default must never be sent
#: explicitly on the wire: adapt_args assigns it RAW, bypassing coercion.
DEFAULTS: dict[str, dict[str, object]] = {
    'cr_distance_to_default': {'horizon': 1.0, 'barrier': 'short_plus_half_long'},
    'cr_merton_pd': {'mapping': 'normal'},
    'cr_transition_matrix': {'estimator': 'duration', 'horizon': 1.0},
    'cr_generator': {'method': 'qo'},
    'cr_stationary_distribution': {},
    'cr_optimal_binning': {'monotonic_trend': 'auto', 'max_bins': 10, 'min_bin_size': 0.05},
    'cr_woe_transform': {'smoothing': 0.5},
    'cr_scorecard': {'base_points': 600.0, 'pdo': 20.0},
    'cr_discrimination': {},
    'cr_calibration': {'n_bins': 10, 'strategy': 'quantile'},
    'cr_grade_test': {'alpha': 0.05},
    'cr_lgd_model': {'model': 'fractional'},
    'cr_ead_model': {'model': 'fractional'},
    'cr_lifetime_pd': {'horizon': 10, 'model': 'cox'},
    'cr_pd_scenario': {},
    'cr_vasicek_loss': {'confidence': 0.999},
    'cr_credit_monte_carlo': {'n_simulations': 100000, 'confidence': 0.999},
    'cr_concentration': {},
}


@cache
def wire_model(fn: str) -> type[BaseModel]:
    """The model the ENGINE validates. Built on first use and cached."""
    return build_wire_model(NODE_META[fn])


@cache
def authoring_model(fn: str) -> type[BaseModel]:
    """The model a GRAPH EDITOR edits. Built on first use and cached."""
    return build_authoring_model(NODE_META[fn])
