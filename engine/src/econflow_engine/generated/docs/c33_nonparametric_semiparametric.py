# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 33-nonparametric-semiparametric: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'np_kernel_regress': {
        'fn': 'np_kernel_regress',
        'description': 'np_kernel_regress -- category 33-nonparametric-semiparametric, method card #283.',
        'args': {'y': 'Dependent variable.', 'x': 'Covariates, one column each.', 'var_type': 'One character per covariate: c continuous, o ordered, u unordered.', 'estimator': 'Local estimator.', 'bandwidth': 'Bandwidth per covariate; omitted = data-driven.', 'grid': 'Evaluation points; omitted = the observed covariates.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'y': '<series_handle>', 'x': '<multiseries_handle>', 'estimator': 'll', 'conf_level': 0.95},
    },
    'np_local_polynomial': {
        'fn': 'np_local_polynomial',
        'description': 'np_local_polynomial -- category 33-nonparametric-semiparametric, method card #283.',
        'args': {'y': 'Dependent variable.', 'x': 'Single continuous covariate.', 'degree': 'Polynomial degree fitted locally.', 'deriv': 'Order of the derivative to return.', 'bandwidth': 'Bandwidth; omitted = plug-in.', 'kernel': 'Kernel function.'},
        'input_example': {'y': '<series_handle>', 'x': '<series_handle>', 'degree': 1, 'deriv': 0, 'kernel': 'epanechnikov'},
    },
    'np_bandwidth_select': {
        'fn': 'np_bandwidth_select',
        'description': 'np_bandwidth_select -- category 33-nonparametric-semiparametric, method card #284.',
        'args': {'x': 'Data the bandwidth is chosen for.', 'y': 'Dependent variable when the target is a regression.', 'method': 'Selection rule.', 'var_type': 'One character per covariate: c, o or u.'},
        'input_example': {'x': '<multiseries_handle>', 'method': 'cv_ls'},
    },
    'np_kde': {
        'fn': 'np_kde',
        'description': 'np_kde -- category 33-nonparametric-semiparametric, method card #285.',
        'args': {'x': 'Data, one column per dimension.', 'var_type': 'One character per dimension: c, o or u.', 'bandwidth': 'Bandwidth per dimension; omitted = data-driven.', 'grid_size': 'Points per dimension in the evaluation grid.'},
        'input_example': {'x': '<multiseries_handle>', 'grid_size': 50},
    },
    'np_conditional_kde': {
        'fn': 'np_conditional_kde',
        'description': 'np_conditional_kde -- category 33-nonparametric-semiparametric, method card #285.',
        'args': {'y': 'Dependent variables.', 'x': 'Conditioning variables.', 'var_type_y': 'Kind characters for y.', 'var_type_x': 'Kind characters for x.', 'grid_size': 'Points per dimension in the evaluation grid.'},
        'input_example': {'y': '<multiseries_handle>', 'x': '<multiseries_handle>', 'grid_size': 50},
    },
    'np_ecdf_grid': {
        'fn': 'np_ecdf_grid',
        'description': 'np_ecdf_grid -- category 33-nonparametric-semiparametric, method card #285.',
        'args': {'x': 'Data.', 'grid': 'Evaluation points; omitted = the sorted data.'},
        'input_example': {'x': '<series_handle>'},
    },
    'np_quantile_forest': {
        'fn': 'np_quantile_forest',
        'description': 'np_quantile_forest -- category 33-nonparametric-semiparametric, method card #286.',
        'args': {'y': 'Dependent variable.', 'x': 'Covariate table.', 'quantiles': 'Quantile levels to return.', 'n_estimators': 'Number of trees.', 'min_samples_leaf': 'Minimum observations per leaf.', 'seed': 'Seed for the random number generator.'},
        'input_example': {'y': '<series_handle>', 'x': '<df_handle>', 'quantiles': [0.1, 0.5, 0.9], 'n_estimators': 500, 'min_samples_leaf': 5},
    },
    'np_quantile_predict': {
        'fn': 'np_quantile_predict',
        'description': 'np_quantile_predict -- category 33-nonparametric-semiparametric, method card #286.',
        'args': {'fit': 'Handle to a fitted quantile forest.', 'newdata': 'Covariate rows to predict for.', 'quantiles': 'Quantile levels to return.'},
        'input_example': {'fit': '<raw_handle>', 'newdata': '<df_handle>', 'quantiles': [0.1, 0.5, 0.9]},
    },
    'np_basis': {
        'fn': 'np_basis',
        'description': 'np_basis -- category 33-nonparametric-semiparametric, method card #287.',
        'args': {'x': 'Covariate to expand.', 'basis': 'Basis family.', 'df': 'Basis dimension.', 'degree': 'Spline degree.', 'knots': 'Interior knots; omitted = quantile-spaced.'},
        'input_example': {'x': '<series_handle>', 'basis': 'bspline', 'df': 5, 'degree': 3},
    },
    'np_series_regress': {
        'fn': 'np_series_regress',
        'description': 'np_series_regress -- category 33-nonparametric-semiparametric, method card #287.',
        'args': {'y': 'Dependent variable.', 'x': 'Covariates to expand.', 'basis': 'Basis family.', 'k_max': 'Largest basis dimension searched.', 'criterion': 'Selection criterion.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'y': '<series_handle>', 'x': '<multiseries_handle>', 'basis': 'bspline', 'k_max': 10, 'criterion': 'aic', 'conf_level': 0.95},
    },
    'np_partially_linear': {
        'fn': 'np_partially_linear',
        'description': 'np_partially_linear -- category 33-nonparametric-semiparametric, method card #288.',
        'args': {'data': 'One row per unit.', 'y': 'Outcome column.', 'd': 'Column holding the variable of interest.', 'covariates': 'Nuisance covariate columns.', 'learner': 'Learner for both nuisance regressions.', 'n_folds': 'Cross-fitting folds.', 'seed': 'Seed for the random number generator.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'data': '<df_handle>', 'y': '...', 'd': '...', 'learner': 'random_forest', 'n_folds': 5, 'conf_level': 0.95},
    },
    'np_single_index': {
        'fn': 'np_single_index',
        'description': 'np_single_index -- category 33-nonparametric-semiparametric, method card #289.',
        'args': {'y': 'Dependent variable.', 'x': 'Covariates entering the index.', 'bandwidth': 'Smoothing bandwidth for the link.', 'normalisation': 'Identifying normalisation.'},
        'input_example': {'y': '<series_handle>', 'x': '<multiseries_handle>', 'normalisation': 'first_unit'},
    },
    'np_varying_coefficient': {
        'fn': 'np_varying_coefficient',
        'description': 'np_varying_coefficient -- category 33-nonparametric-semiparametric, method card #289.',
        'args': {'y': 'Dependent variable.', 'x': 'Covariates whose coefficients vary.', 'modifier': 'Variable the coefficients vary with.', 'bandwidth': 'Smoothing bandwidth.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'y': '<series_handle>', 'x': '<multiseries_handle>', 'modifier': '<series_handle>', 'conf_level': 0.95},
    },
    'np_gam_fit': {
        'fn': 'np_gam_fit',
        'description': 'np_gam_fit -- category 33-nonparametric-semiparametric, method card #290.',
        'args': {'y': 'Dependent variable.', 'x': 'Covariate table.', 'distribution': 'Response distribution.', 'link': 'Link function.', 'n_splines': 'Basis functions per smooth term.', 'lam': 'Penalty; omitted = selected by grid search.'},
        'input_example': {'y': '<series_handle>', 'x': '<df_handle>', 'distribution': 'normal', 'link': 'identity', 'n_splines': 20},
    },
    'np_gam_partial': {
        'fn': 'np_gam_partial',
        'description': 'np_gam_partial -- category 33-nonparametric-semiparametric, method card #290.',
        'args': {'fit': 'Handle to a fitted additive model.', 'term': 'Index of the term to extract.', 'grid_size': 'Grid points for the curve.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'fit': '<raw_handle>', 'term': 1, 'grid_size': 100, 'conf_level': 0.95},
    },
    'np_specification_test': {
        'fn': 'np_specification_test',
        'description': 'np_specification_test -- category 33-nonparametric-semiparametric, method card #291.',
        'args': {'y': 'Dependent variable.', 'x': 'Covariates.', 'parametric': 'Formula for the parametric null.', 'bandwidth': 'Bandwidth for the nonparametric alternative.', 'nboot': 'Number of bootstrap replications.', 'seed': 'Seed for the random number generator.', 'alpha': 'Significance level.'},
        'input_example': {'y': '<series_handle>', 'x': '<multiseries_handle>', 'parametric': 'y ~ x', 'nboot': 999, 'alpha': 0.05},
    },
}
