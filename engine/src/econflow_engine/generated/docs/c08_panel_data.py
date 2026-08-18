# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.v1.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 08-panel-data: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'feis_bstest': {
        'fn': 'feis_bstest',
        'description': 'feis_bstest -- category 08-panel-data, METHOD-SELECTION card #173.',
        'args': {'object': "Handle to a 'feis' model (from feis_fit).", 'type': 'bs1=FEIS vs FE, bs2=FE vs RE, bs3=FEIS vs RE (default all).', 'rep': 'Pairs-cluster bootstrap replications (default 500).', 'seed': 'Reproducibility seed of the bootstrap (default 2025).', 'terms': 'Optional character vector of coefficients for a joint Wald test (default: all).'},
        'input_example': {'object': '<raw_handle>', 'rep': 500, 'seed': 2025},
    },
    'feis_fit': {
        'fn': 'feis_fit',
        'description': 'feis_fit -- category 08-panel-data, METHOD-SELECTION card #173.',
        'args': {'formula': "Two-part FEIS formula 'y ~ x1 + x2 | slope1 + slope2' (the '|' is required· for conventional FE: 'y ~ x | 1').", 'data': 'Handle to a panel DataFrame (long format) with the id column + the variables.', 'id': 'Column name (string) of the unique group/person identifier.', 'robust': 'True -> panel/cluster-robust SE (default False).', 'intercept': 'True -> estimation with intercept (default False).', 'dropgroups': 'True -> drop groups without within-variance in the slope var (default False: omit per group).'},
        'input_example': {'formula': 'y ~ x', 'data': '<df_handle>', 'id': '...', 'robust': False, 'intercept': False, 'dropgroups': False},
    },
    'feis_slopes': {
        'fn': 'feis_slopes',
        'description': 'feis_slopes -- category 08-panel-data, METHOD-SELECTION card #173.',
        'args': {'object': "Handle to a 'feis' model (from feis_fit)· returns the N x J matrix of alpha_i."},
        'input_example': {'object': '<raw_handle>'},
    },
    'feis_test': {
        'fn': 'feis_test',
        'description': 'feis_test -- category 08-panel-data, METHOD-SELECTION card #173.',
        'args': {'object': "Handle to a 'feis' model (from feis_fit).", 'type': 'art1=FEIS vs FE, art2=FE vs RE, art3=FEIS vs RE (default all).', 'robust': 'True -> cluster-robust SE in the artificial regression (default False).', 'terms': 'Optional character vector of coefficients for a joint Wald test (default: all).'},
        'input_example': {'object': '<raw_handle>', 'robust': False},
    },
    'lme_glmer': {
        'fn': 'lme_glmer',
        'description': 'lme_glmer -- category 08-panel-data, METHOD-SELECTION card #175.',
        'args': {'formula': "GLMM formula with a random-effects term, e.g. 'y ~ x + (1 | group)'.", 'data': 'Handle to a DataFrame (variables of the formula + grouping factor).', 'family': 'Response distribution (closed set· default binomial). NOT gaussian (use lme_lmer).', 'nAGQ': 'Adaptive Gauss-Hermite quadrature points (default 1· >1 = more accurate likelihood, only single scalar RE).'},
        'input_example': {'formula': 'y ~ x', 'data': '<df_handle>', 'nAGQ': 1},
    },
    'lme_lmer': {
        'fn': 'lme_lmer',
        'description': 'lme_lmer -- category 08-panel-data, METHOD-SELECTION card #175.',
        'args': {'formula': "Mixed-model formula with a random-effects term, e.g. 'y ~ x + (1 | group)'.", 'data': 'Handle to a DataFrame (variables of the formula + grouping factor).', 'REML': 'True=REML (default, unbiased variance components), False=ML (for comparing fixed effects).'},
        'input_example': {'formula': 'y ~ x', 'data': '<df_handle>', 'REML': True},
    },
    'lme_ranef': {
        'fn': 'lme_ranef',
        'description': 'lme_ranef -- category 08-panel-data, METHOD-SELECTION card #175.',
        'args': {'object': 'Handle to a merMod model (from lme_lmer/lme_glmer).', 'condVar': 'Computation of conditional variances -> condsd in the records (default True).'},
        'input_example': {'object': '<raw_handle>', 'condVar': True},
    },
    'lme_varcorr': {
        'fn': 'lme_varcorr',
        'description': 'lme_varcorr -- category 08-panel-data, METHOD-SELECTION card #175.',
        'args': {'object': 'Handle to a merMod model (from lme_lmer/lme_glmer).'},
        'input_example': {'object': '<raw_handle>'},
    },
    'pcse_fit': {
        'fn': 'pcse_fit',
        'description': 'pcse_fit -- category 08-panel-data, METHOD-SELECTION card #174.',
        'args': {'formula': "Pooled TSCS formula, e.g. 'y ~ x1 + x2' (OLS is estimated internally).", 'data': 'Handle to a pooled panel DataFrame (one row per unit-time).', 'groupN': 'Column name of the cross-section (unit) index.', 'groupT': 'Column name of the time index.', 'pairwise': 'False=casewise (balanced rectangle), True=pairwise (unbalanced).'},
        'input_example': {'formula': 'y ~ x', 'data': '<df_handle>', 'groupN': '...', 'groupT': '...', 'pairwise': False},
    },
    'pcse_summary': {
        'fn': 'pcse_summary',
        'description': 'pcse_summary -- category 08-panel-data, METHOD-SELECTION card #174.',
        'args': {'object': "Handle to a 'pcse' object (from pcse_fit/pcse_vcov $object)."},
        'input_example': {'object': '<raw_handle>'},
    },
    'pcse_vcov': {
        'fn': 'pcse_vcov',
        'description': 'pcse_vcov -- category 08-panel-data, METHOD-SELECTION card #174.',
        'args': {'object': "Handle to an already-estimated 'lm' (pooled OLS) for PCSE correction.", 'groupN': 'Numeric vector of the cross-section (unit) index, of length nobs.', 'groupT': 'Numeric vector of the time index, of length nobs.', 'pairwise': 'False=casewise, True=pairwise (unbalanced panels).'},
        'input_example': {'object': '<raw_handle>', 'groupN': [0.5, 0.5], 'groupT': [0.5, 0.5], 'pairwise': False},
    },
    'pd_effects_ftest': {
        'fn': 'pd_effects_ftest',
        'description': 'pd_effects_ftest -- category 08-panel-data, METHOD-SELECTION card #46.',
        'args': {'x': 'Model formula (F-test for significance of the fixed effects).', 'data': 'Panel data handle.', 'effect': 'Effect dimension.'},
        'input_example': {'x': 'y ~ x', 'data': '<df_handle>'},
    },
    'pd_fit': {
        'fn': 'pd_fit',
        'description': 'pd_fit -- category 08-panel-data, METHOD-SELECTION card #46.',
        'args': {'formula': "Panel model formula, e.g. 'inv ~ value + capital'.", 'data': 'Handle to a panel DataFrame (first 2 columns = index individual/time).', 'effect': 'Effect dimension (default individual).', 'model': 'Estimator (default within = fixed effects).'},
        'input_example': {'formula': 'y ~ x', 'data': '<df_handle>'},
    },
    'pd_fixed_effects': {
        'fn': 'pd_fixed_effects',
        'description': 'pd_fixed_effects -- category 08-panel-data, METHOD-SELECTION card #46.',
        'args': {'object': "Handle to a 'within' plm model (from pd_fit with model='within').", 'type': 'Effects coding (default level).'},
        'input_example': {'object': '<raw_handle>'},
    },
    'pd_gmm_autocorr_test': {
        'fn': 'pd_gmm_autocorr_test',
        'description': 'pd_gmm_autocorr_test -- category 08-panel-data, METHOD-SELECTION card #47.',
        'args': {'object': 'Handle to a pgmm model (from pd_gmm_fit).', 'order': 'AR order of the residual autocorrelation test (default 1).'},
        'input_example': {'object': '<raw_handle>', 'order': 1},
    },
    'pd_gmm_fit': {
        'fn': 'pd_gmm_fit',
        'description': 'pd_gmm_fit -- category 08-panel-data, METHOD-SELECTION card #47.',
        'args': {'formula': 'Dynamic panel GMM formula (Arellano-Bond, e.g. with lag & instruments).', 'data': 'Panel data handle.', 'effect': 'Effect dimension (default twoways).', 'model': 'GMM steps (default onestep).', 'transformation': 'd=first-diff GMM, ld=system GMM (default d).'},
        'input_example': {'formula': 'y ~ x', 'data': '<df_handle>'},
    },
    'pd_gmm_sargan_test': {
        'fn': 'pd_gmm_sargan_test',
        'description': 'pd_gmm_sargan_test -- category 08-panel-data, METHOD-SELECTION card #47.',
        'args': {'object': 'Handle to a pgmm model (from pd_gmm_fit).', 'weights': 'Weighting for the Sargan/Hansen test.'},
        'input_example': {'object': '<raw_handle>'},
    },
    'pd_hausman_test': {
        'fn': 'pd_hausman_test',
        'description': 'pd_hausman_test -- category 08-panel-data, METHOD-SELECTION card #46.',
        'args': {'x': 'Model formula· the test runs within vs random internally.', 'data': 'Panel data handle.', 'effect': 'Effect dimension.', 'method': 'Test flavour (default chisq).'},
        'input_example': {'x': 'y ~ x', 'data': '<df_handle>'},
    },
    'pd_poolability_test': {
        'fn': 'pd_poolability_test',
        'description': 'pd_poolability_test -- category 08-panel-data, METHOD-SELECTION card #46.',
        'args': {'x': 'Model formula (LM poolability / random-effects test).', 'data': 'Panel data handle.', 'effect': 'Effect dimension.', 'type': 'LM statistic variant (default honda).'},
        'input_example': {'x': 'y ~ x', 'data': '<df_handle>'},
    },
    'pd_random_effects': {
        'fn': 'pd_random_effects',
        'description': 'pd_random_effects -- category 08-panel-data, METHOD-SELECTION card #46.',
        'args': {'object': "Handle to a 'random' plm model (from pd_fit with model='random')."},
        'input_example': {'object': '<raw_handle>'},
    },
}
