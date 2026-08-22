# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 2 for category 17-forecast-combination -- 10 nodes. No descriptions."""

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
    'reconcile_grouped': NodeMeta(
        fn='reconcile_grouped',
        category='17-forecast-combination',
        card_id=209,
        contract_hash='c2-c06a74ef592ca2d75824bac736cbd1979ff13b05e98f4e3962940f5f8806197b',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='index', kind='string', required=True),
        NodeArgMeta(name='keys', kind='series_codes', required=True),
        NodeArgMeta(name='value', kind='string', required=True),
        NodeArgMeta(name='structure', kind='enum', required=False, enum=('nested', 'grouped', )),
        NodeArgMeta(name='base_model', kind='enum', required=False, enum=('arima', 'ets', 'snaive', )),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('wls_struct', 'ols', 'wls_var', 'mint_shrink', 'mint_cov', 'bottom_up', )),
        NodeArgMeta(name='h', kind='integer', required=False),
        ),
        defaults={'h': 8},
    ),
    'reconcile_cross_temporal': NodeMeta(
        fn='reconcile_cross_temporal',
        category='17-forecast-combination',
        card_id=208,
        contract_hash='c2-537a6e015e1ed6823a7902ade3cfc236432655744c802ee21451ef29ca5b429e',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='type', kind='enum', required=True, enum=('cs', 'te', 'ct', )),
        NodeArgMeta(name='base', kind='matrix_handle', required=True),
        NodeArgMeta(name='agg_mat', kind='matrix_handle', required=False),
        NodeArgMeta(name='agg_order', kind='int_array', required=False),
        NodeArgMeta(name='comb', kind='string', required=False),
        NodeArgMeta(name='tew', kind='enum', required=False, enum=('sum', 'avg', 'first', 'last', )),
        NodeArgMeta(name='approach', kind='enum', required=False, enum=('proj', 'strc', 'proj_osqp', 'strc_osqp', )),
        NodeArgMeta(name='res', kind='matrix_handle', required=False),
        NodeArgMeta(name='nn', kind='enum', required=False, enum=('none', 'osqp', 'sntz', 'bpv', 'nfca', 'nnic', )),
        ),
        defaults={'comb': 'ols'},
    ),
    'crps_learning': NodeMeta(
        fn='crps_learning',
        category='17-forecast-combination',
        card_id=207,
        contract_hash='c2-540b49d887713b8a73cfa1de66bfb9a13e68619838c2c33d0921cc0d51dfcd6f',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='y', kind='matrix_handle', required=True),
        NodeArgMeta(name='experts', kind='raw_handle', required=True),
        NodeArgMeta(name='tau', kind='num_array', required=True),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('bewa', 'boa', 'ml_poly', 'ewa', )),
        NodeArgMeta(name='loss_function', kind='enum', required=False, enum=('quantile', 'expectile', 'percentage', )),
        NodeArgMeta(name='loss_parameter', kind='number', required=False),
        NodeArgMeta(name='loss_gradient', kind='boolean', required=False),
        NodeArgMeta(name='lead_time', kind='integer', required=False),
        NodeArgMeta(name='forget_regret', kind='number', required=False),
        NodeArgMeta(name='fixed_share', kind='number', required=False),
        NodeArgMeta(name='gamma', kind='number', required=False),
        NodeArgMeta(name='soft_threshold', kind='number', required=False),
        NodeArgMeta(name='hard_threshold', kind='number', required=False),
        NodeArgMeta(name='allow_quantile_crossing', kind='boolean', required=False),
        NodeArgMeta(name='seed', kind='integer', required=False),
        ),
        defaults={'loss_parameter': 1, 'loss_gradient': True, 'lead_time': 0, 'forget_regret': 0, 'fixed_share': 0, 'gamma': 1, 'soft_threshold': None, 'hard_threshold': None, 'allow_quantile_crossing': False, 'seed': 2025},
    ),
    'run_hybrid': NodeMeta(
        fn='run_hybrid',
        category='17-forecast-combination',
        card_id=85,
        contract_hash='c2-0b7963c5eaee512816af8d31eca6c0273829d94572de33957c887acd71295120',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='y', kind='series_handle', required=True),
        NodeArgMeta(name='models', kind='string', required=False),
        NodeArgMeta(name='weights', kind='enum', required=False, enum=('equal', 'insample.errors', 'cv.errors', )),
        NodeArgMeta(name='errorMethod', kind='enum', required=False, enum=('RMSE', 'MAE', 'MASE', )),
        NodeArgMeta(name='h', kind='integer', required=False),
        NodeArgMeta(name='PI_combination', kind='enum', required=False, enum=('extreme', 'mean', )),
        NodeArgMeta(name='cvHorizon', kind='integer', required=False),
        NodeArgMeta(name='windowSize', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=False),
        ),
        defaults={'models': 'aefnst', 'windowSize': 84, 'seed': 42},
    ),
    'fc_combination_weights': NodeMeta(
        fn='fc_combination_weights',
        category='17-forecast-combination',
        card_id=530,
        contract_hash='c2-d06352704eb170dddce6961d72030bb9b55d322df490424287254c4abcf029d4',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='actual', kind='series_handle', required=True),
        NodeArgMeta(name='forecasts', kind='df_handle', required=True),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('equal', 'inverse_mse', 'granger_ramanathan', 'constrained_ls', 'trimmed_mean', )),
        NodeArgMeta(name='window', kind='integer', required=False),
        NodeArgMeta(name='constrain', kind='boolean', required=False),
        ),
        defaults={'method': 'inverse_mse', 'constrain': True},
    ),
    'fc_density_combination': NodeMeta(
        fn='fc_density_combination',
        category='17-forecast-combination',
        card_id=531,
        contract_hash='c2-b085af22fc626288539bff9e824e146a95401f04cb8034e8928594ef2f6083ca',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='densities', kind='matrix_handle', required=True),
        NodeArgMeta(name='weights', kind='num_array', required=False),
        NodeArgMeta(name='pool', kind='enum', required=False, enum=('linear', 'logarithmic', 'beta_transformed', )),
        NodeArgMeta(name='grid', kind='num_array', required=False),
        ),
        defaults={'pool': 'linear'},
    ),
    'fc_score_driven_weights': NodeMeta(
        fn='fc_score_driven_weights',
        category='17-forecast-combination',
        card_id=531,
        contract_hash='c2-12b6f32452abd1d7bd605c0cdf854440327e90e6abfb1893d0b611aa33f549f1',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='actual', kind='series_handle', required=True),
        NodeArgMeta(name='densities', kind='matrix_handle', required=True),
        NodeArgMeta(name='forgetting', kind='number', required=False),
        ),
        defaults={'forgetting': 0.95},
    ),
    'fc_dynamic_model_averaging': NodeMeta(
        fn='fc_dynamic_model_averaging',
        category='17-forecast-combination',
        card_id=532,
        contract_hash='c2-59bc6079fdc42ace25760a000c9e7846dde43614e083dd44ede635c27f0ff5bc',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='actual', kind='series_handle', required=True),
        NodeArgMeta(name='forecasts', kind='df_handle', required=True),
        NodeArgMeta(name='forgetting_weights', kind='number', required=False),
        NodeArgMeta(name='forgetting_variance', kind='number', required=False),
        NodeArgMeta(name='mode', kind='enum', required=False, enum=('averaging', 'selection', )),
        ),
        defaults={'forgetting_weights': 0.99, 'forgetting_variance': 0.95, 'mode': 'averaging'},
    ),
    'fc_stacking': NodeMeta(
        fn='fc_stacking',
        category='17-forecast-combination',
        card_id=533,
        contract_hash='c2-f9fc474416860492e61334058dd1b6d249f5e7443e80dd7e2fe9132eb521e0c2',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='actual', kind='series_handle', required=True),
        NodeArgMeta(name='forecasts', kind='df_handle', required=True),
        NodeArgMeta(name='meta_learner', kind='enum', required=False, enum=('linear', 'ridge', 'constrained_ls', 'gradient_boosting', )),
        NodeArgMeta(name='n_folds', kind='integer', required=False),
        ),
        defaults={'meta_learner': 'constrained_ls', 'n_folds': 5},
    ),
    'fc_temporal_hierarchy': NodeMeta(
        fn='fc_temporal_hierarchy',
        category='17-forecast-combination',
        card_id=534,
        contract_hash='c2-40eb509d28c5e802952ddb0f2462a947033cc886f35863dab25d6f47d23260f2',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='y', kind='series_handle', required=True),
        NodeArgMeta(name='h', kind='integer', required=True),
        NodeArgMeta(name='levels', kind='int_array', required=False),
        NodeArgMeta(name='base_model', kind='enum', required=False, enum=('auto_arima', 'auto_ets', 'theta', 'naive', )),
        NodeArgMeta(name='reconciliation', kind='enum', required=False, enum=('ols', 'wls_struct', 'wls_var', 'mint_shrink', )),
        ),
        defaults={'base_model': 'auto_ets', 'reconciliation': 'wls_struct'},
    ),
}

#: Argument defaults, for FORM PREFILL ONLY. A default must never be sent
#: explicitly on the wire: adapt_args assigns it RAW, bypassing coercion.
DEFAULTS: dict[str, dict[str, object]] = {
    'reconcile_grouped': {'h': 8},
    'reconcile_cross_temporal': {'comb': 'ols'},
    'crps_learning': {'loss_parameter': 1, 'loss_gradient': True, 'lead_time': 0, 'forget_regret': 0, 'fixed_share': 0, 'gamma': 1, 'soft_threshold': None, 'hard_threshold': None, 'allow_quantile_crossing': False, 'seed': 2025},
    'run_hybrid': {'models': 'aefnst', 'windowSize': 84, 'seed': 42},
    'fc_combination_weights': {'method': 'inverse_mse', 'constrain': True},
    'fc_density_combination': {'pool': 'linear'},
    'fc_score_driven_weights': {'forgetting': 0.95},
    'fc_dynamic_model_averaging': {'forgetting_weights': 0.99, 'forgetting_variance': 0.95, 'mode': 'averaging'},
    'fc_stacking': {'meta_learner': 'constrained_ls', 'n_folds': 5},
    'fc_temporal_hierarchy': {'base_model': 'auto_ets', 'reconciliation': 'wls_struct'},
}


@cache
def wire_model(fn: str) -> type[BaseModel]:
    """The model the ENGINE validates. Built on first use and cached."""
    return build_wire_model(NODE_META[fn])


@cache
def authoring_model(fn: str) -> type[BaseModel]:
    """The model a GRAPH EDITOR edits. Built on first use and cached."""
    return build_authoring_model(NODE_META[fn])
