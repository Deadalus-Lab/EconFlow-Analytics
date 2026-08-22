# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 08-panel-data: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'feis_bootstrap_test': {
        'fn': 'feis_bootstrap_test',
        'description': 'feis_bootstrap_test -- category 08-panel-data, method card #173.',
        'args': {'object': "Handle to a 'feis' model (from feis_fit).", 'type': 'bs1=FEIS vs FE, bs2=FE vs RE, bs3=FEIS vs RE (default all).', 'rep': 'Pairs-cluster bootstrap replications (default 500).', 'seed': 'Reproducibility seed of the bootstrap (default 2025).', 'terms': 'Optional character vector of coefficients for a joint Wald test (default: all).'},
        'input_example': {'object': '<raw_handle>', 'rep': 500, 'seed': 2025},
    },
    'feis_fit': {
        'fn': 'feis_fit',
        'description': 'feis_fit -- category 08-panel-data, method card #173.',
        'args': {'formula': "Two-part FEIS formula 'y ~ x1 + x2 | slope1 + slope2' (the '|' is required· for conventional FE: 'y ~ x | 1').", 'data': 'Handle to a panel DataFrame (long format) with the id column + the variables.', 'id': 'Column name (string) of the unique group/person identifier.', 'robust': 'True -> panel/cluster-robust SE (default False).', 'intercept': 'True -> estimation with intercept (default False).', 'dropgroups': 'True -> drop groups without within-variance in the slope var (default False: omit per group).'},
        'input_example': {'formula': 'y ~ x', 'data': '<df_handle>', 'id': '...', 'robust': False, 'intercept': False, 'dropgroups': False},
    },
    'feis_slopes': {
        'fn': 'feis_slopes',
        'description': 'feis_slopes -- category 08-panel-data, method card #173.',
        'args': {'object': "Handle to a 'feis' model (from feis_fit)· returns the N x J matrix of alpha_i."},
        'input_example': {'object': '<raw_handle>'},
    },
    'feis_test': {
        'fn': 'feis_test',
        'description': 'feis_test -- category 08-panel-data, method card #173.',
        'args': {'object': "Handle to a 'feis' model (from feis_fit).", 'type': 'art1=FEIS vs FE, art2=FE vs RE, art3=FEIS vs RE (default all).', 'robust': 'True -> cluster-robust SE in the artificial regression (default False).', 'terms': 'Optional character vector of coefficients for a joint Wald test (default: all).'},
        'input_example': {'object': '<raw_handle>', 'robust': False},
    },
    'lme_fit_glm': {
        'fn': 'lme_fit_glm',
        'description': 'lme_fit_glm -- category 08-panel-data, method card #175.',
        'args': {'formula': "GLMM formula with a random-effects term, e.g. 'y ~ x + (1 | group)'.", 'data': 'Handle to a DataFrame (variables of the formula + grouping factor).', 'family': 'Response distribution (closed set· default binomial). NOT gaussian (use lme_fit).', 'nAGQ': 'Adaptive Gauss-Hermite quadrature points (default 1· >1 = more accurate likelihood, only single scalar RE).'},
        'input_example': {'formula': 'y ~ x', 'data': '<df_handle>', 'nAGQ': 1},
    },
    'lme_fit': {
        'fn': 'lme_fit',
        'description': 'lme_fit -- category 08-panel-data, method card #175.',
        'args': {'formula': "Mixed-model formula with a random-effects term, e.g. 'y ~ x + (1 | group)'.", 'data': 'Handle to a DataFrame (variables of the formula + grouping factor).', 'REML': 'True=REML (default, unbiased variance components), False=ML (for comparing fixed effects).'},
        'input_example': {'formula': 'y ~ x', 'data': '<df_handle>', 'REML': True},
    },
    'lme_random_effects': {
        'fn': 'lme_random_effects',
        'description': 'lme_random_effects -- category 08-panel-data, method card #175.',
        'args': {'object': 'Handle to a merMod model (from lme_fit/lme_fit_glm).', 'condVar': 'Computation of conditional variances -> condsd in the records (default True).'},
        'input_example': {'object': '<raw_handle>', 'condVar': True},
    },
    'lme_variance_components': {
        'fn': 'lme_variance_components',
        'description': 'lme_variance_components -- category 08-panel-data, method card #175.',
        'args': {'object': 'Handle to a merMod model (from lme_fit/lme_fit_glm).'},
        'input_example': {'object': '<raw_handle>'},
    },
    'pcse_fit': {
        'fn': 'pcse_fit',
        'description': 'pcse_fit -- category 08-panel-data, method card #174.',
        'args': {'formula': "Pooled TSCS formula, e.g. 'y ~ x1 + x2' (OLS is estimated internally).", 'data': 'Handle to a pooled panel DataFrame (one row per unit-time).', 'groupN': 'Column name of the cross-section (unit) index.', 'groupT': 'Column name of the time index.', 'pairwise': 'False=casewise (balanced rectangle), True=pairwise (unbalanced).'},
        'input_example': {'formula': 'y ~ x', 'data': '<df_handle>', 'groupN': '...', 'groupT': '...', 'pairwise': False},
    },
    'pcse_summary': {
        'fn': 'pcse_summary',
        'description': 'pcse_summary -- category 08-panel-data, method card #174.',
        'args': {'object': "Handle to a 'pcse' object (from pcse_fit/pcse_vcov $object)."},
        'input_example': {'object': '<raw_handle>'},
    },
    'pcse_vcov': {
        'fn': 'pcse_vcov',
        'description': 'pcse_vcov -- category 08-panel-data, method card #174.',
        'args': {'object': "Handle to an already-estimated 'lm' (pooled OLS) for PCSE correction.", 'groupN': 'Numeric vector of the cross-section (unit) index, of length nobs.', 'groupT': 'Numeric vector of the time index, of length nobs.', 'pairwise': 'False=casewise, True=pairwise (unbalanced panels).'},
        'input_example': {'object': '<raw_handle>', 'groupN': [0.5, 0.5], 'groupT': [0.5, 0.5], 'pairwise': False},
    },
    'pd_effects_ftest': {
        'fn': 'pd_effects_ftest',
        'description': 'pd_effects_ftest -- category 08-panel-data, method card #46.',
        'args': {'x': 'Model formula (F-test for significance of the fixed effects).', 'data': 'Panel data handle.', 'effect': 'Effect dimension.'},
        'input_example': {'x': 'y ~ x', 'data': '<df_handle>'},
    },
    'pd_fit': {
        'fn': 'pd_fit',
        'description': 'pd_fit -- category 08-panel-data, method card #46.',
        'args': {'formula': "Panel model formula, e.g. 'inv ~ value + capital'.", 'data': 'Handle to a panel DataFrame (first 2 columns = index individual/time).', 'effect': 'Effect dimension (default individual).', 'model': 'Estimator (default within = fixed effects).'},
        'input_example': {'formula': 'y ~ x', 'data': '<df_handle>'},
    },
    'pd_fixed_effects': {
        'fn': 'pd_fixed_effects',
        'description': 'pd_fixed_effects -- category 08-panel-data, method card #46.',
        'args': {'object': "Handle to a 'within' panel model (from pd_fit with model='within').", 'type': 'Effects coding (default level).'},
        'input_example': {'object': '<raw_handle>'},
    },
    'pd_gmm_autocorr_test': {
        'fn': 'pd_gmm_autocorr_test',
        'description': 'pd_gmm_autocorr_test -- category 08-panel-data, method card #47.',
        'args': {'object': 'Handle to a pgmm model (from pd_gmm_fit).', 'order': 'AR order of the residual autocorrelation test (default 1).'},
        'input_example': {'object': '<raw_handle>', 'order': 1},
    },
    'pd_gmm_fit': {
        'fn': 'pd_gmm_fit',
        'description': 'pd_gmm_fit -- category 08-panel-data, method card #47.',
        'args': {'formula': 'Dynamic panel GMM formula (Arellano-Bond, e.g. with lag & instruments).', 'data': 'Panel data handle.', 'effect': 'Effect dimension (default twoways).', 'model': 'GMM steps (default onestep).', 'transformation': 'd=first-diff GMM, ld=system GMM (default d).'},
        'input_example': {'formula': 'y ~ x', 'data': '<df_handle>'},
    },
    'pd_gmm_sargan_test': {
        'fn': 'pd_gmm_sargan_test',
        'description': 'pd_gmm_sargan_test -- category 08-panel-data, method card #47.',
        'args': {'object': 'Handle to a pgmm model (from pd_gmm_fit).', 'weights': 'Weighting for the Sargan/Hansen test.'},
        'input_example': {'object': '<raw_handle>'},
    },
    'pd_hausman_test': {
        'fn': 'pd_hausman_test',
        'description': 'pd_hausman_test -- category 08-panel-data, method card #46.',
        'args': {'x': 'Model formula· the test runs within vs random internally.', 'data': 'Panel data handle.', 'effect': 'Effect dimension.', 'method': 'Test flavour (default chisq).'},
        'input_example': {'x': 'y ~ x', 'data': '<df_handle>'},
    },
    'pd_poolability_test': {
        'fn': 'pd_poolability_test',
        'description': 'pd_poolability_test -- category 08-panel-data, method card #46.',
        'args': {'x': 'Model formula (LM poolability / random-effects test).', 'data': 'Panel data handle.', 'effect': 'Effect dimension.', 'type': 'LM statistic variant (default honda).'},
        'input_example': {'x': 'y ~ x', 'data': '<df_handle>'},
    },
    'pd_random_effects': {
        'fn': 'pd_random_effects',
        'description': 'pd_random_effects -- category 08-panel-data, method card #46.',
        'args': {'object': "Handle to a 'random' panel model (from pd_fit with model='random')."},
        'input_example': {'object': '<raw_handle>'},
    },
    'pd_correlated_random_effects': {
        'fn': 'pd_correlated_random_effects',
        'description': 'pd_correlated_random_effects -- category 08-panel-data, method card #458.',
        'args': {'data': 'Panel data.', 'formula': 'Model formula.', 'unit': 'Unit identifier.', 'time': 'Time identifier.', 'estimator': 'Estimator.', 'exogenous': 'Regressors assumed exogenous for Hausman-Taylor.', 'time_invariant': 'Time-invariant regressors.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'data': '<df_handle>', 'formula': 'y ~ x', 'unit': '...', 'time': '...', 'estimator': 'mundlak', 'conf_level': 0.95},
    },
    'pd_heterogeneous_panel': {
        'fn': 'pd_heterogeneous_panel',
        'description': 'pd_heterogeneous_panel -- category 08-panel-data, method card #459.',
        'args': {'data': 'Panel data.', 'formula': 'Model formula.', 'unit': 'Unit identifier.', 'time': 'Time identifier.', 'estimator': 'Estimator.', 'trim': 'Trimming of outlying unit estimates.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'data': '<df_handle>', 'formula': 'y ~ x', 'unit': '...', 'time': '...', 'estimator': 'mean_group', 'trim': 0.0, 'conf_level': 0.95},
    },
    'pd_fama_macbeth': {
        'fn': 'pd_fama_macbeth',
        'description': 'pd_fama_macbeth -- category 08-panel-data, method card #460.',
        'args': {'data': 'Panel data.', 'formula': 'Model formula.', 'unit': 'Unit identifier.', 'time': 'Time identifier.', 'newey_west_lags': 'Lags for the autocorrelation correction.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'data': '<df_handle>', 'formula': 'y ~ x', 'unit': '...', 'time': '...', 'newey_west_lags': 0, 'conf_level': 0.95},
    },
    'pd_sur': {
        'fn': 'pd_sur',
        'description': 'pd_sur -- category 08-panel-data, method card #461.',
        'args': {'data': 'Data.', 'equations': 'Equation specifications.', 'estimator': 'Estimator.', 'instruments': 'Instruments for the three-stage estimator.', 'iterate': 'Iterate the covariance to convergence.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'data': '<df_handle>', 'equations': '...', 'estimator': 'sur', 'iterate': False, 'conf_level': 0.95},
    },
    'pd_panel_quantile': {
        'fn': 'pd_panel_quantile',
        'description': 'pd_panel_quantile -- category 08-panel-data, method card #462.',
        'args': {'data': 'Panel data.', 'formula': 'Model formula.', 'unit': 'Unit identifier.', 'time': 'Time identifier.', 'quantiles': 'Quantile levels.', 'estimator': 'Estimator.', 'nboot': 'Number of bootstrap replications.', 'seed': 'Seed for the random number generator; required for reproducibility.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'data': '<df_handle>', 'formula': 'y ~ x', 'unit': '...', 'time': '...', 'quantiles': [0.1, 0.25, 0.5, 0.75, 0.9], 'estimator': 'canay', 'nboot': 999, 'seed': 1, 'conf_level': 0.95},
    },
    'pd_panel_iv': {
        'fn': 'pd_panel_iv',
        'description': 'pd_panel_iv -- category 08-panel-data, method card #463.',
        'args': {'data': 'Panel data.', 'formula': 'Model formula with the instrument block.', 'absorb': 'Columns whose fixed effects are absorbed.', 'cluster': 'Clustering variables.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'data': '<df_handle>', 'formula': 'y ~ x', 'absorb': ['a', 'b'], 'conf_level': 0.95},
    },
    'pd_panel_vcov': {
        'fn': 'pd_panel_vcov',
        'description': 'pd_panel_vcov -- category 08-panel-data, method card #464.',
        'args': {'fit': 'Handle to a fitted panel model.', 'estimators': 'Estimators to compute; omitted = the standard set.', 'cluster': 'Clustering variables.', 'bandwidth': 'Lag truncation for Driscoll-Kraay.'},
        'input_example': {'fit': '<raw_handle>'},
    },
    'pd_panel_count': {
        'fn': 'pd_panel_count',
        'description': 'pd_panel_count -- category 08-panel-data, method card #465.',
        'args': {'data': 'Panel data.', 'formula': 'Model formula.', 'absorb': 'Columns whose fixed effects are absorbed.', 'family': 'Distribution family.', 'cluster': 'Clustering variables.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'data': '<df_handle>', 'formula': 'y ~ x', 'absorb': ['a', 'b'], 'family': 'poisson', 'conf_level': 0.95},
    },
    'pd_variance_decomposition': {
        'fn': 'pd_variance_decomposition',
        'description': 'pd_variance_decomposition -- category 08-panel-data, method card #466.',
        'args': {'data': 'Panel data.', 'variables': 'Variables to decompose.', 'unit': 'Unit identifier.', 'time': 'Time identifier.', 'threshold': 'Within-share below which a variable is flagged.'},
        'input_example': {'data': '<df_handle>', 'unit': '...', 'time': '...', 'threshold': 0.05},
    },
    'pd_slope_homogeneity_test': {
        'fn': 'pd_slope_homogeneity_test',
        'description': 'pd_slope_homogeneity_test -- category 08-panel-data, method card #466.',
        'args': {'data': 'Panel data.', 'formula': 'Model formula.', 'unit': 'Unit identifier.', 'alpha': 'Significance level.'},
        'input_example': {'data': '<df_handle>', 'formula': 'y ~ x', 'unit': '...', 'alpha': 0.05},
    },
    'pd_attrition_test': {
        'fn': 'pd_attrition_test',
        'description': 'pd_attrition_test -- category 08-panel-data, method card #467.',
        'args': {'data': 'Panel data.', 'outcome': 'Outcome column.', 'unit': 'Unit identifier.', 'time': 'Time identifier.', 'covariates': 'Covariates entering the retention model.', 'alpha': 'Significance level.'},
        'input_example': {'data': '<df_handle>', 'outcome': '...', 'unit': '...', 'time': '...', 'alpha': 0.05},
    },
    'pd_attrition_weights': {
        'fn': 'pd_attrition_weights',
        'description': 'pd_attrition_weights -- category 08-panel-data, method card #467.',
        'args': {'data': 'Panel data.', 'unit': 'Unit identifier.', 'time': 'Time identifier.', 'covariates': 'Covariates entering the retention model.', 'stabilised': 'Use stabilised weights.'},
        'input_example': {'data': '<df_handle>', 'unit': '...', 'time': '...', 'stabilised': True},
    },
    'pd_akm': {
        'fn': 'pd_akm',
        'description': 'pd_akm -- category 08-panel-data, method card #468.',
        'args': {'data': 'Matched employer-employee panel.', 'outcome': 'Outcome column, usually log pay.', 'worker': 'Worker identifier.', 'firm': 'Firm identifier.', 'time': 'Time identifier.', 'controls': 'Additional control columns.', 'bias_correction': 'Limited-mobility bias correction.'},
        'input_example': {'data': '<df_handle>', 'outcome': '...', 'worker': '...', 'firm': '...', 'time': '...', 'bias_correction': 'none'},
    },
}
