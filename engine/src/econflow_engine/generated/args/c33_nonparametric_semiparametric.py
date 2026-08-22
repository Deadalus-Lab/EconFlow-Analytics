# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 2 for category 33-nonparametric-semiparametric -- 16 nodes. No descriptions."""

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
    'np_kernel_regress': NodeMeta(
        fn='np_kernel_regress',
        category='33-nonparametric-semiparametric',
        card_id=283,
        contract_hash='c2-476b3baf40aa864eacdc055b9d7b1e4885d0fe798576f04d30af07ac10285bc4',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='y', kind='series_handle', required=True),
        NodeArgMeta(name='x', kind='multiseries_handle', required=True),
        NodeArgMeta(name='var_type', kind='string', required=False),
        NodeArgMeta(name='estimator', kind='enum', required=False, enum=('lc', 'll', )),
        NodeArgMeta(name='bandwidth', kind='num_array', required=False),
        NodeArgMeta(name='grid', kind='num_array', required=False),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'estimator': 'll', 'conf_level': 0.95},
    ),
    'np_local_polynomial': NodeMeta(
        fn='np_local_polynomial',
        category='33-nonparametric-semiparametric',
        card_id=283,
        contract_hash='c2-8a783367d1c7a420c116a63708542849c73aa8e2dcdd63eb931cb2c4225a0023',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='y', kind='series_handle', required=True),
        NodeArgMeta(name='x', kind='series_handle', required=True),
        NodeArgMeta(name='degree', kind='integer', required=False),
        NodeArgMeta(name='deriv', kind='integer', required=False),
        NodeArgMeta(name='bandwidth', kind='number', required=False),
        NodeArgMeta(name='kernel', kind='enum', required=False, enum=('epanechnikov', 'gaussian', 'uniform', 'triangular', 'biweight', )),
        ),
        defaults={'degree': 1, 'deriv': 0, 'kernel': 'epanechnikov'},
    ),
    'np_bandwidth_select': NodeMeta(
        fn='np_bandwidth_select',
        category='33-nonparametric-semiparametric',
        card_id=284,
        contract_hash='c2-6542e30065e2fcd955a432d021c85b6b145d5203bea6ce8ba3001109f2df6c96',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='x', kind='multiseries_handle', required=True),
        NodeArgMeta(name='y', kind='series_handle', required=False),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('cv_ls', 'cv_ml', 'plug_in', 'silverman', 'scott', )),
        NodeArgMeta(name='var_type', kind='string', required=False),
        ),
        defaults={'method': 'cv_ls'},
    ),
    'np_kde': NodeMeta(
        fn='np_kde',
        category='33-nonparametric-semiparametric',
        card_id=285,
        contract_hash='c2-b8da8d4f19a7f9bb59f0f1a09b8a39342fc4470befd3fbfeb0ef3c685f3f2f95',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='x', kind='multiseries_handle', required=True),
        NodeArgMeta(name='var_type', kind='string', required=False),
        NodeArgMeta(name='bandwidth', kind='num_array', required=False),
        NodeArgMeta(name='grid_size', kind='integer', required=False),
        ),
        defaults={'grid_size': 50},
    ),
    'np_conditional_kde': NodeMeta(
        fn='np_conditional_kde',
        category='33-nonparametric-semiparametric',
        card_id=285,
        contract_hash='c2-46ab18517ff37fe5acca436c32c304a8aea157a306fe0814af3f288ad6d296c6',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='y', kind='multiseries_handle', required=True),
        NodeArgMeta(name='x', kind='multiseries_handle', required=True),
        NodeArgMeta(name='var_type_y', kind='string', required=False),
        NodeArgMeta(name='var_type_x', kind='string', required=False),
        NodeArgMeta(name='grid_size', kind='integer', required=False),
        ),
        defaults={'grid_size': 50},
    ),
    'np_ecdf_grid': NodeMeta(
        fn='np_ecdf_grid',
        category='33-nonparametric-semiparametric',
        card_id=285,
        contract_hash='c2-f81b86b01146e2955576d4dadae4685417769964bb35bea6f85837a29bd295e2',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='x', kind='series_handle', required=True),
        NodeArgMeta(name='grid', kind='num_array', required=False),
        ),
        defaults={},
    ),
    'np_quantile_forest': NodeMeta(
        fn='np_quantile_forest',
        category='33-nonparametric-semiparametric',
        card_id=286,
        contract_hash='c2-21f2f422b6306ef78c3d72ca3ff0e7677a8844985ec5c185474465f7ce41de7b',
        register_field='fit',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='y', kind='series_handle', required=True),
        NodeArgMeta(name='x', kind='df_handle', required=True),
        NodeArgMeta(name='quantiles', kind='num_array', required=False),
        NodeArgMeta(name='n_estimators', kind='integer', required=False),
        NodeArgMeta(name='min_samples_leaf', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=False),
        ),
        defaults={'quantiles': [0.1, 0.5, 0.9], 'n_estimators': 500, 'min_samples_leaf': 5},
    ),
    'np_quantile_predict': NodeMeta(
        fn='np_quantile_predict',
        category='33-nonparametric-semiparametric',
        card_id=286,
        contract_hash='c2-4446e84d7acb8b8c5e9c729ff886ed1c175412459f30ff7ca2de8e7f53988c8c',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='fit', kind='raw_handle', required=True),
        NodeArgMeta(name='newdata', kind='df_handle', required=True),
        NodeArgMeta(name='quantiles', kind='num_array', required=False),
        ),
        defaults={'quantiles': [0.1, 0.5, 0.9]},
    ),
    'np_basis': NodeMeta(
        fn='np_basis',
        category='33-nonparametric-semiparametric',
        card_id=287,
        contract_hash='c2-1cfd842777ee969b2e74738a71daa08d321b56796420e8eb939eff211020f28a',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='x', kind='series_handle', required=True),
        NodeArgMeta(name='basis', kind='enum', required=False, enum=('polynomial', 'bspline', 'natural_spline', 'fourier', 'legendre', )),
        NodeArgMeta(name='df', kind='integer', required=False),
        NodeArgMeta(name='degree', kind='integer', required=False),
        NodeArgMeta(name='knots', kind='num_array', required=False),
        ),
        defaults={'basis': 'bspline', 'df': 5, 'degree': 3},
    ),
    'np_series_regress': NodeMeta(
        fn='np_series_regress',
        category='33-nonparametric-semiparametric',
        card_id=287,
        contract_hash='c2-bfbacca785086ae7d34a5fbf978eb07b05c946fe2cf5754492d3de233c498c4c',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='y', kind='series_handle', required=True),
        NodeArgMeta(name='x', kind='multiseries_handle', required=True),
        NodeArgMeta(name='basis', kind='enum', required=False, enum=('polynomial', 'bspline', 'natural_spline', )),
        NodeArgMeta(name='k_max', kind='integer', required=False),
        NodeArgMeta(name='criterion', kind='enum', required=False, enum=('aic', 'bic', 'cv', )),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'basis': 'bspline', 'k_max': 10, 'criterion': 'aic', 'conf_level': 0.95},
    ),
    'np_partially_linear': NodeMeta(
        fn='np_partially_linear',
        category='33-nonparametric-semiparametric',
        card_id=288,
        contract_hash='c2-72830c92a22de0af4e0508be7f811c10b8ea86ed18120009003d48f5877539be',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='y', kind='string', required=True),
        NodeArgMeta(name='d', kind='string', required=True),
        NodeArgMeta(name='covariates', kind='series_codes', required=False),
        NodeArgMeta(name='learner', kind='enum', required=False, enum=('linear', 'lasso', 'random_forest', 'gradient_boosting', )),
        NodeArgMeta(name='n_folds', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=False),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'learner': 'random_forest', 'n_folds': 5, 'conf_level': 0.95},
    ),
    'np_single_index': NodeMeta(
        fn='np_single_index',
        category='33-nonparametric-semiparametric',
        card_id=289,
        contract_hash='c2-9a62fc96c7a67d48b43de3620c36fe9941eb937ee8f25456f92160b2a73a2214',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='y', kind='series_handle', required=True),
        NodeArgMeta(name='x', kind='multiseries_handle', required=True),
        NodeArgMeta(name='bandwidth', kind='number', required=False),
        NodeArgMeta(name='normalisation', kind='enum', required=False, enum=('first_unit', 'unit_norm', )),
        ),
        defaults={'normalisation': 'first_unit'},
    ),
    'np_varying_coefficient': NodeMeta(
        fn='np_varying_coefficient',
        category='33-nonparametric-semiparametric',
        card_id=289,
        contract_hash='c2-e11151b4defa3e97448c18d0c09a78e84cdd823c070e1955df33eedcb6b8bde8',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='y', kind='series_handle', required=True),
        NodeArgMeta(name='x', kind='multiseries_handle', required=True),
        NodeArgMeta(name='modifier', kind='series_handle', required=True),
        NodeArgMeta(name='bandwidth', kind='number', required=False),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'conf_level': 0.95},
    ),
    'np_gam_fit': NodeMeta(
        fn='np_gam_fit',
        category='33-nonparametric-semiparametric',
        card_id=290,
        contract_hash='c2-9f764b4b0ab7612a248e2147e8c89343bd4ac74c7d49c754877d9c7d181ba8b6',
        register_field='fit',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='y', kind='series_handle', required=True),
        NodeArgMeta(name='x', kind='df_handle', required=True),
        NodeArgMeta(name='distribution', kind='enum', required=False, enum=('normal', 'binomial', 'poisson', 'gamma', 'inv_gauss', )),
        NodeArgMeta(name='link', kind='enum', required=False, enum=('identity', 'logit', 'log', 'inverse', )),
        NodeArgMeta(name='n_splines', kind='integer', required=False),
        NodeArgMeta(name='lam', kind='number', required=False),
        ),
        defaults={'distribution': 'normal', 'link': 'identity', 'n_splines': 20},
    ),
    'np_gam_partial': NodeMeta(
        fn='np_gam_partial',
        category='33-nonparametric-semiparametric',
        card_id=290,
        contract_hash='c2-631c36316ef893d80fa17d1cb4bd2f9e219eeac08e6808aae53a2769fa14092e',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='fit', kind='raw_handle', required=True),
        NodeArgMeta(name='term', kind='integer', required=True),
        NodeArgMeta(name='grid_size', kind='integer', required=False),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'grid_size': 100, 'conf_level': 0.95},
    ),
    'np_specification_test': NodeMeta(
        fn='np_specification_test',
        category='33-nonparametric-semiparametric',
        card_id=291,
        contract_hash='c2-0cdd5fcd37db616e7eefef6d1fb4ce5ff2bd3f54dc9978144680d177c127d7e8',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='heavy',
        args=(
        NodeArgMeta(name='y', kind='series_handle', required=True),
        NodeArgMeta(name='x', kind='multiseries_handle', required=True),
        NodeArgMeta(name='parametric', kind='formula', required=True),
        NodeArgMeta(name='bandwidth', kind='number', required=False),
        NodeArgMeta(name='nboot', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=False),
        NodeArgMeta(name='alpha', kind='number', required=False),
        ),
        defaults={'nboot': 999, 'alpha': 0.05},
    ),
}

#: Argument defaults, for FORM PREFILL ONLY. A default must never be sent
#: explicitly on the wire: adapt_args assigns it RAW, bypassing coercion.
DEFAULTS: dict[str, dict[str, object]] = {
    'np_kernel_regress': {'estimator': 'll', 'conf_level': 0.95},
    'np_local_polynomial': {'degree': 1, 'deriv': 0, 'kernel': 'epanechnikov'},
    'np_bandwidth_select': {'method': 'cv_ls'},
    'np_kde': {'grid_size': 50},
    'np_conditional_kde': {'grid_size': 50},
    'np_ecdf_grid': {},
    'np_quantile_forest': {'quantiles': [0.1, 0.5, 0.9], 'n_estimators': 500, 'min_samples_leaf': 5},
    'np_quantile_predict': {'quantiles': [0.1, 0.5, 0.9]},
    'np_basis': {'basis': 'bspline', 'df': 5, 'degree': 3},
    'np_series_regress': {'basis': 'bspline', 'k_max': 10, 'criterion': 'aic', 'conf_level': 0.95},
    'np_partially_linear': {'learner': 'random_forest', 'n_folds': 5, 'conf_level': 0.95},
    'np_single_index': {'normalisation': 'first_unit'},
    'np_varying_coefficient': {'conf_level': 0.95},
    'np_gam_fit': {'distribution': 'normal', 'link': 'identity', 'n_splines': 20},
    'np_gam_partial': {'grid_size': 100, 'conf_level': 0.95},
    'np_specification_test': {'nboot': 999, 'alpha': 0.05},
}


@cache
def wire_model(fn: str) -> type[BaseModel]:
    """The model the ENGINE validates. Built on first use and cached."""
    return build_wire_model(NODE_META[fn])


@cache
def authoring_model(fn: str) -> type[BaseModel]:
    """The model a GRAPH EDITOR edits. Built on first use and cached."""
    return build_authoring_model(NODE_META[fn])
