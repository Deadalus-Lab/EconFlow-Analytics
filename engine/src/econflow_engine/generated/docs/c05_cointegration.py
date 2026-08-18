# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.v1.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 05-cointegration: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'ardl_auto': {
        'fn': 'ardl_auto',
        'description': 'ardl_auto -- category 05-cointegration, METHOD-SELECTION card #25.',
        'args': {'formula': "ARDL formula (e.g. 'y ~ x1 + x2').", 'data': "Handle to a DataFrame or series handle carrying the formula's variables.", 'max_order': 'Maximum lag for the search; positive integer (or vector).', 'selection': 'Selection criterion (AIC/BIC/R2/adjR2/...) (default AIC).', 'selection_minmax': 'Optimization direction of the criterion (default min).', 'grid': 'True = exhaustive grid search (default False).'},
        'input_example': {'formula': 'y ~ x', 'data': '<df_handle>', 'max_order': 1, 'selection': 'AIC', 'grid': False},
    },
    'ardl_bounds_f': {
        'fn': 'ardl_bounds_f',
        'description': 'ardl_bounds_f -- category 05-cointegration, METHOD-SELECTION card #25.',
        'args': {'object': "Handle to an 'ardl'/'uecm' model (from ardl_fit/ardl_auto).", 'case': 'PSS case of deterministic terms; integer 1..5.', 'test': 'Bounds statistic (default F).', 'n_replications': 'Simulation replications of the p-value (default 40000).'},
        'input_example': {'object': '<raw_handle>', 'case': 1, 'n_replications': 40000},
    },
    'ardl_bounds_t': {
        'fn': 'ardl_bounds_t',
        'description': 'ardl_bounds_t -- category 05-cointegration, METHOD-SELECTION card #25.',
        'args': {'object': "Handle to an 'ardl'/'uecm' model (from ardl_fit/ardl_auto).", 'case': 'PSS case of deterministic terms; integer 1..5.', 'n_replications': 'Simulation replications of the p-value (default 40000).'},
        'input_example': {'object': '<raw_handle>', 'case': 1, 'n_replications': 40000},
    },
    'ardl_coint_eq': {
        'fn': 'ardl_coint_eq',
        'description': 'ardl_coint_eq -- category 05-cointegration, METHOD-SELECTION card #25.',
        'args': {'object': "Handle to an 'ardl'/'uecm' model (from ardl_fit/ardl_auto).", 'case': 'PSS case of deterministic terms; integer 1..5.'},
        'input_example': {'object': '<raw_handle>', 'case': 1},
    },
    'ardl_fit': {
        'fn': 'ardl_fit',
        'description': 'ardl_fit -- category 05-cointegration, METHOD-SELECTION card #25.',
        'args': {'formula': "ARDL formula (e.g. 'y ~ x1 + x2').", 'data': "Handle to a DataFrame or series handle carrying the formula's variables.", 'order': 'Lag orders per variable; vector of non-negative integers of length #vars.'},
        'input_example': {'formula': 'y ~ x', 'data': '<df_handle>', 'order': 1},
    },
    'ardl_multipliers': {
        'fn': 'ardl_multipliers',
        'description': 'ardl_multipliers -- category 05-cointegration, METHOD-SELECTION card #25.',
        'args': {'object': "Handle to an 'ardl'/'uecm' model (from ardl_fit/ardl_auto).", 'type': "'lr' (long-run, default), 'sr' (short-run), or a non-negative integer (interim).", 'se': 'True = return standard errors (default False).'},
        'input_example': {'object': '<raw_handle>', 'type': 'lr', 'se': False},
    },
    'ardl_recm': {
        'fn': 'ardl_recm',
        'description': 'ardl_recm -- category 05-cointegration, METHOD-SELECTION card #25.',
        'args': {'object': "Handle to an 'ardl'/'uecm' model (from ardl_fit/ardl_auto).", 'case': 'PSS case of deterministic terms; integer 1..5.'},
        'input_example': {'object': '<raw_handle>', 'case': 1},
    },
    'cmo_cointegration': {
        'fn': 'cmo_cointegration',
        'description': 'cmo_cointegration -- category 05-cointegration, METHOD-SELECTION card #141.',
        'args': {'x': 'Handle to RHS regressors (numeric matrix/vector, I(1), WITHOUT NA).', 'y': 'Handle to the LHS response (one-dimensional, length==the row count of x, WITHOUT NA).', 'm': 'Calibration period fraction ∈ [0.1, 0.9] (default 0.25).', 'model': 'Modified-OLS: FM-OLS (default), D-OLS (=DOLS), IM-OLS.', 'trend': 'True = intercept + linear trend; False (default) = intercept only.', 'kernel': 'Kernel long-run variance (default ba = Bartlett).', 'bandwidth': 'Automatic bandwidth selection (default and = Andrews 1991).', 'signif_level': 'Significance level ∈ [0.01, 0.1] (default 0.05).', 'D_options': "Only for model='D': list(n.lead,n.lag,kmax,info.crit) for D-OLS; None = cointRegD's defaults."},
        'input_example': {'x': '<matrix_handle>', 'y': '<series_handle>', 'm': 0.25, 'trend': False, 'signif_level': 0.05},
    },
    'cmo_stationarity': {
        'fn': 'cmo_stationarity',
        'description': 'cmo_stationarity -- category 05-cointegration, METHOD-SELECTION card #141.',
        'args': {'x': 'Handle to a one-dimensional series under monitoring (numeric ts/vector, WITHOUT NA).', 'm': 'Calibration period fraction ∈ [0.1, 0.9] (default 0.25); parameters are estimated only on [1..floor(m*N)].', 'trend': 'True = intercept + linear trend; False (default) = intercept only.', 'kernel': 'Kernel long-run variance (default ba = Bartlett).', 'bandwidth': 'Automatic bandwidth selection (default and = Andrews 1991).', 'signif_level': 'Significance level ∈ [0.01, 0.1] (default 0.05); detection time only if p < signif_level.'},
        'input_example': {'x': '<series_handle>', 'm': 0.25, 'trend': False, 'signif_level': 0.05},
    },
    'creg_dols': {
        'fn': 'creg_dols',
        'description': 'creg_dols -- category 05-cointegration, METHOD-SELECTION card #27.',
        'args': {'x': 'Handle to regressors (matrix/vector, I(1)).', 'y': 'Handle to a response series (one-dimensional, I(1)).', 'deter': 'Deterministic terms (default const).', 'kernel': 'Kernel long-run variance (default ba).', 'bandwidth': 'Bandwidth selection (default and).', 'kmax': 'Upper bound of lead/lag for automatic selection (default k4).', 'info_crit': 'Lead/lag selection criterion (default AIC).', 'demeaning': 'True = demeaning (default False).'},
        'input_example': {'x': '<matrix_handle>', 'y': '<series_handle>', 'demeaning': False},
    },
    'creg_fmols': {
        'fn': 'creg_fmols',
        'description': 'creg_fmols -- category 05-cointegration, METHOD-SELECTION card #27.',
        'args': {'x': 'Handle to regressors (matrix/vector, I(1)).', 'y': 'Handle to a response series (one-dimensional, I(1)).', 'deter': 'Deterministic terms (default const).', 'kernel': 'Kernel long-run variance (default ba = Bartlett).', 'bandwidth': 'Bandwidth selection (default and = Andrews).', 'demeaning': 'True = demeaning before the estimation (default False).'},
        'input_example': {'x': '<matrix_handle>', 'y': '<series_handle>', 'demeaning': False},
    },
    'creg_imols': {
        'fn': 'creg_imols',
        'description': 'creg_imols -- category 05-cointegration, METHOD-SELECTION card #27.',
        'args': {'x': 'Handle to regressors (matrix/vector, I(1)).', 'y': 'Handle to a response series (one-dimensional, I(1)).', 'deter': 'Deterministic terms (default const).', 'kernel': 'Kernel long-run variance (default ba).', 'bandwidth': 'Bandwidth selection (default and).'},
        'input_example': {'x': '<matrix_handle>', 'y': '<series_handle>'},
    },
    'dmac_ardl': {
        'fn': 'dmac_ardl',
        'description': 'dmac_ardl -- category 05-cointegration, METHOD-SELECTION card #26.',
        'args': {'formula': "ARDL/ECM formula (e.g. 'y ~ x1 + x2').", 'data': 'Handle to a DataFrame (NOT ts; dynardl builds lags/diffs on its own).', 'diffs': 'Variable names in first differences (array of strings).', 'levels': 'Variable names in levels (array of strings).', 'ec': 'True = error-correction parameterization (required for dmac_pssbounds).', 'trend': 'True = deterministic trend (default False).', 'constant': 'True = constant term (default True).', 'simulate': 'True = stochastic simulation of the counterfactual response (chart-data).', 'shockvar': 'Variable to shock (required when simulate=True; one of the RHS).', 'sims': 'Monte Carlo replications of the simulation (default 1000).', 'range': 'Horizon of the response path (default 20).'},
        'input_example': {'formula': 'y ~ x', 'data': '<df_handle>', 'ec': False, 'trend': False, 'constant': True, 'simulate': False, 'sims': 1000, 'range': 20},
    },
    'dmac_autocorr': {
        'fn': 'dmac_autocorr',
        'description': 'dmac_autocorr -- category 05-cointegration, METHOD-SELECTION card #26.',
        'args': {'object': "Handle to a 'dynardl' model (from dmac_ardl).", 'bg_type': 'Breusch-Godfrey statistic (default Chisq).', 'order': 'AR order of the autocorrelation test (default 1).'},
        'input_example': {'object': '<raw_handle>', 'order': 1},
    },
    'dmac_pssbounds': {
        'fn': 'dmac_pssbounds',
        'description': 'dmac_pssbounds -- category 05-cointegration, METHOD-SELECTION card #26.',
        'args': {'object': "Handle to a 'dynardl' estimated with ec=True (from dmac_ardl)."},
        'input_example': {'object': '<raw_handle>'},
    },
    'fcv_boot_rank': {
        'fn': 'fcv_boot_rank',
        'description': 'fcv_boot_rank -- category 05-cointegration, METHOD-SELECTION card #139.',
        'args': {'x': 'Handle to a multivariate system (matrix/mts, >=2 columns).', 'k': 'Number of lags; integer >=0 (default 1).', 'r1': 'Rank under H0; integer 0..p (default 0).', 'r2': 'Rank under H1; integer 0..p, r2>r1 (default 1).', 'B': 'Number of bootstrap samples; integer >=1 (default 99).', 'seed': 'Seed (REQUIRED — wild bootstrap, stochastic).', 'grid_search': 'Grid search for d,b (default False).'},
        'input_example': {'x': '<matrix_handle>', 'k': 1, 'r1': 0, 'r2': 1, 'B': 99, 'seed': 1, 'grid_search': False},
    },
    'fcv_estimate': {
        'fn': 'fcv_estimate',
        'description': 'fcv_estimate -- category 05-cointegration, METHOD-SELECTION card #139.',
        'args': {'x': 'Handle to a multivariate system (matrix/mts, >=2 columns, fractionally integrated).', 'k': 'Number of lags in the system; integer >=0 (default 1).', 'r': 'Cointegration rank; integer 0..p (default 1).', 'db_min': 'Lower bound for (d,b); scalar or length-2 (default 0.01).', 'db_max': 'Upper bound for (d,b); scalar or length-2 (default 2.0).', 'restrict_db': 'Enforcement of the d=b constraint (default True).', 'constrained': 'Enforcement of dbMax>=d>=b>=dbMin (default False).', 'level_param': 'Inclusion of a level parameter (default True).', 'r_constant': 'Restricted constant in the cointegrating relation (default False).', 'unr_constant': 'Unrestricted constant (default False).', 'grid_search': 'Grid search for d,b (expensive accuracy-refinement; default False).'},
        'input_example': {'x': '<matrix_handle>', 'k': 1, 'r': 1, 'restrict_db': True, 'constrained': False, 'level_param': True, 'r_constant': False, 'unr_constant': False, 'grid_search': False},
    },
    'fcv_lag_select': {
        'fn': 'fcv_lag_select',
        'description': 'fcv_lag_select -- category 05-cointegration, METHOD-SELECTION card #139.',
        'args': {'x': 'Handle to a multivariate system (matrix/mts, >=2 columns).', 'kmax': 'Maximum number of lags; integer >=1 (default 2).', 'r': 'Cointegration rank; integer 0..p (default p — over-specify).', 'order': 'Serial correlation order for the white-noise tests; >=1 (default 2).', 'grid_search': 'Grid search for d,b (default False).'},
        'input_example': {'x': '<matrix_handle>', 'kmax': 2, 'order': 2, 'grid_search': False},
    },
    'fcv_rank_test': {
        'fn': 'fcv_rank_test',
        'description': 'fcv_rank_test -- category 05-cointegration, METHOD-SELECTION card #139.',
        'args': {'x': 'Handle to a multivariate system (matrix/mts, >=2 columns).', 'k': 'Number of lags; integer >=0 (default 1).', 'restrict_db': 'Enforcement of d=b (default True).', 'constrained': 'Enforcement of dbMax>=d>=b>=dbMin (default False).', 'grid_search': 'Grid search for d,b (default False).'},
        'input_example': {'x': '<matrix_handle>', 'k': 1, 'restrict_db': True, 'constrained': False, 'grid_search': False},
    },
    'nar_bounds': {
        'fn': 'nar_bounds',
        'description': 'nar_bounds -- category 05-cointegration, METHOD-SELECTION card #140.',
        'args': {'object': "Handle to a 'nardl' model (from nar_fit)."},
        'input_example': {'object': '<raw_handle>'},
    },
    'nar_fit': {
        'fn': 'nar_fit',
        'description': 'nar_fit -- category 05-cointegration, METHOD-SELECTION card #140.',
        'args': {'data': 'Handle to a DataFrame with the y & x columns.', 'y': 'Dependent-variable column name (closed; NOT a free formula).', 'x': 'Column name of the decomposed regressor (positive/negative partial sums); EXACTLY one.', 'ic': 'Lag selection criterion (default aic).', 'maxlag': 'Maximum lag for the search; positive integer (default 4).', 'case': 'PSS case of deterministic terms; ONLY 3 (unrestricted intercept) or 5 (+trend).'},
        'input_example': {'data': '<df_handle>', 'y': '...', 'x': '...', 'maxlag': 4, 'case': 3},
    },
    'nar_stability': {
        'fn': 'nar_stability',
        'description': 'nar_stability -- category 05-cointegration, METHOD-SELECTION card #140.',
        'args': {'object': "Handle to a 'nardl' model (from nar_fit)."},
        'input_example': {'object': '<raw_handle>'},
    },
    'vecm_estimate': {
        'fn': 'vecm_estimate',
        'description': 'vecm_estimate -- category 05-cointegration, METHOD-SELECTION card #24.',
        'args': {'data': 'Handle to a multivariate system (matrix/mts, >=2 columns I(1)).', 'lag': 'Lag order (in differences); positive integer.', 'r': 'Cointegration rank; integer 1..(ncol-1) (default 1).', 'include': 'Deterministic terms (default const).', 'estim': 'Estimator; ML is required for vecm_rank_test (default 2OLS).', 'LRinclude': 'Deterministics in the long-run relation (default none).'},
        'input_example': {'data': '<matrix_handle>', 'lag': 1, 'r': 1},
    },
    'vecm_predict': {
        'fn': 'vecm_predict',
        'description': 'vecm_predict -- category 05-cointegration, METHOD-SELECTION card #24.',
        'args': {'vecm': "Handle to a 'VECM' (from vecm_estimate).", 'n_ahead': 'Forecast horizon; positive integer (default 5).'},
        'input_example': {'vecm': '<raw_handle>', 'n_ahead': 5},
    },
    'vecm_rank_select': {
        'fn': 'vecm_rank_select',
        'description': 'vecm_rank_select -- category 05-cointegration, METHOD-SELECTION card #24.',
        'args': {'data': 'Handle to a multivariate system (matrix/mts, >=2 columns).', 'lag_max': 'Maximum lag for the search; positive integer.', 'include': 'Deterministic terms (default const).'},
        'input_example': {'data': '<matrix_handle>', 'lag_max': 1},
    },
    'vecm_rank_test': {
        'fn': 'vecm_rank_test',
        'description': 'vecm_rank_test -- category 05-cointegration, METHOD-SELECTION card #24.',
        'args': {'vecm': "Handle to a 'VECM' estimated with estim='ML' (from vecm_estimate).", 'type': 'Johansen statistic (default eigen).', 'cval': 'Significance level in (0,1) (default 0.05).'},
        'input_example': {'vecm': '<raw_handle>', 'cval': 0.05},
    },
    'wrap_ca_jo': {
        'fn': 'wrap_ca_jo',
        'description': 'wrap_ca_jo -- category 05-cointegration, METHOD-SELECTION card #23.',
        'args': {'x': 'Handle to a multivariate system (matrix/mts, >=2 columns I(1)).', 'type': 'Johansen statistic (default eigen = max-eigenvalue).', 'ecdet': 'Deterministic term in the cointegrating relation (default none).', 'K': 'Lag order in levels (VAR); integer >=2 (default 2).', 'spec': 'VECM parameterization (default longrun).'},
        'input_example': {'x': '<matrix_handle>', 'K': 2},
    },
    'wrap_ca_po': {
        'fn': 'wrap_ca_po',
        'description': 'wrap_ca_po -- category 05-cointegration, METHOD-SELECTION card #23.',
        'args': {'z': 'Handle to a multivariate system (matrix/mts, >=2 columns).', 'demean': 'Deterministic terms in the regression (default none).', 'lag': 'Long-run variance lag selection (default short).', 'type': 'Phillips-Ouliaris statistic (default Pu).'},
        'input_example': {'z': '<matrix_handle>'},
    },
    'wrap_cajorls': {
        'fn': 'wrap_cajorls',
        'description': 'wrap_cajorls -- category 05-cointegration, METHOD-SELECTION card #23.',
        'args': {'z': "Handle to a 'ca.jo' object (from wrap_ca_jo).", 'r': 'Cointegration rank; integer 1..(P-1) (default 1).'},
        'input_example': {'z': '<raw_handle>', 'r': 1},
    },
}
