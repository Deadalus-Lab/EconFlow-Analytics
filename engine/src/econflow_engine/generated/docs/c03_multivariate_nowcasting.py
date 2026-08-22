# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 03-multivariate-nowcasting: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'bt_fevd': {
        'fn': 'bt_fevd',
        'description': 'bt_fevd -- category 03-multivariate-nowcasting, method card #13.',
        'args': {'model': 'Handle to a bvar model (from bt_var).', 'response': 'Name of the response variable for the FEVD.', 'n_ahead': 'FEVD horizon (default 5).', 'type': 'Decomposition type (default oir = orthogonalised).'},
        'input_example': {'model': '<raw_handle>', 'response': '...', 'n_ahead': 5},
    },
    'bt_irf': {
        'fn': 'bt_irf',
        'description': 'bt_irf -- category 03-multivariate-nowcasting, method card #13.',
        'args': {'model': 'Handle to a bvar model (from bt_var).', 'impulse': 'Name of the shock variable (impulse).', 'response': 'Name of the response variable (response).', 'n_ahead': 'IRF horizon (default 5).', 'ci': 'Confidence level in (0,1) (default 0.95).', 'type': 'IRF type (default feir = forecast error impulse response).', 'cumulative': 'Cumulative IRF (default False).'},
        'input_example': {'model': '<raw_handle>', 'impulse': '...', 'response': '...', 'n_ahead': 5, 'ci': 0.95, 'cumulative': False},
    },
    'bt_predict': {
        'fn': 'bt_predict',
        'description': 'bt_predict -- category 03-multivariate-nowcasting, method card #13.',
        'args': {'model': 'Handle to a bvar model (from bt_var).', 'n_ahead': 'Forecast horizon (default 10).', 'ci': 'Confidence level in (0,1) (default 0.95).', 'seed': 'Seed for reproducibility (optional).'},
        'input_example': {'model': '<raw_handle>', 'n_ahead': 10, 'ci': 0.95},
    },
    'bt_summary': {
        'fn': 'bt_summary',
        'description': 'bt_summary -- category 03-multivariate-nowcasting, method card #13.',
        'args': {'model': 'Handle to a bvar model (posterior coefficients/sigma).', 'ci': 'Confidence level of the credible intervals (default 0.95).'},
        'input_example': {'model': '<raw_handle>', 'ci': 0.95},
    },
    'bt_var': {
        'fn': 'bt_var',
        'description': 'bt_var -- category 03-multivariate-nowcasting, method card #13.',
        'args': {'data': 'Handle to series/panel data (>=2 columns, no NA).', 'p': 'VAR(p) lag order (default 2).', 'deterministic': 'Deterministic terms (default const).', 'iterations': 'MCMC iterations (default 10000).', 'burnin': 'Burn-in draws (default 5000, < iterations).', 'seed': 'Seed for reproducibility (optional).'},
        'input_example': {'data': '<multiseries_handle>', 'p': 2, 'iterations': 10000, 'burnin': 5000},
    },
    'bvar_companion': {
        'fn': 'bvar_companion',
        'description': 'bvar_companion -- category 03-multivariate-nowcasting, method card #12.',
        'args': {'model': 'Handle to a bvar model (companion matrix + stability check).'},
        'input_example': {'model': '<raw_handle>'},
    },
    'bvar_estimate': {
        'fn': 'bvar_estimate',
        'description': 'bvar_estimate -- category 03-multivariate-nowcasting, method card #12.',
        'args': {'data': 'Handle to multivariate data (>=2 columns, no NA).', 'lags': 'VAR lag order (default 1).', 'n_draw': 'Total MCMC draws (default 10000).', 'n_burn': 'Burn-in draws (default 5000, < n_draw).', 'n_thin': 'Thinning step (default 1).', 'lambda': 'Minnesota tightness (mode) > 0 (default 0.2).', 'seed': 'Seed for reproducibility (optional).'},
        'input_example': {'data': '<multiseries_handle>', 'lags': 1, 'n_draw': 10000, 'n_burn': 5000, 'n_thin': 1, 'lambda': 0.2},
    },
    'bvar_fevd': {
        'fn': 'bvar_fevd',
        'description': 'bvar_fevd -- category 03-multivariate-nowcasting, method card #12.',
        'args': {'model': 'Handle to a bvar model (from bvar_estimate).', 'horizon': 'FEVD horizon (default 12).'},
        'input_example': {'model': '<raw_handle>', 'horizon': 12},
    },
    'bvar_irf': {
        'fn': 'bvar_irf',
        'description': 'bvar_irf -- category 03-multivariate-nowcasting, method card #12.',
        'args': {'model': 'Handle to a bvar model (from bvar_estimate).', 'horizon': 'Impulse response horizon (default 12).', 'identification': 'Cholesky identification (default True).', 'fevd': 'Compute the FEVD together with the IRF (default False).'},
        'input_example': {'model': '<raw_handle>', 'horizon': 12, 'identification': True, 'fevd': False},
    },
    'bvar_predict': {
        'fn': 'bvar_predict',
        'description': 'bvar_predict -- category 03-multivariate-nowcasting, method card #12.',
        'args': {'model': 'Handle to a bvar model (from bvar_estimate).', 'horizon': 'Forecast horizon (default 12).', 'conf_bands': 'Confidence band in (0,0.5) (default 0.16).'},
        'input_example': {'model': '<raw_handle>', 'horizon': 12, 'conf_bands': 0.16},
    },
    'bvar_summary': {
        'fn': 'bvar_summary',
        'description': 'bvar_summary -- category 03-multivariate-nowcasting, method card #12.',
        'args': {'model': 'Handle to a bvar model (posterior coef/vcov/logLik/acceptance).'},
        'input_example': {'model': '<raw_handle>'},
    },
    'bvh_predict': {
        'fn': 'bvh_predict',
        'description': 'bvh_predict -- category 03-multivariate-nowcasting, method card #147.',
        'args': {'model': 'Handle to a bvhar model (from bvh_var/bvh_vhar).', 'n_ahead': 'Forecast horizon (default 8).', 'level': 'Significance level ∈ (0,1)· 0.05 -> 95% interval (default 0.05).', 'sparse': 'True -> sparsified (SAVS) coefficients (MCMC only· default False).'},
        'input_example': {'model': '<raw_handle>', 'n_ahead': 8, 'level': 0.05, 'sparse': False},
    },
    'bvh_var': {
        'fn': 'bvh_var',
        'description': 'bvh_var -- category 03-multivariate-nowcasting, method card #147.',
        'args': {'y': 'Handle to multivariate data (>=2 columns, finite).', 'p': 'VAR lag order (default 1).', 'prior': 'Prior: minnesota=conjugate/analytic· ssvs/horseshoe=MCMC (seed mandatory + convergence gate).', 'lambda': 'Minnesota tightness > 0 (default 0.1).', 'num_chains': 'MCMC chains (>=2 for a valid Rhat· default 2).', 'num_iter': 'MCMC iterations (default 200· small).', 'num_burn': 'Burn-in (< num_iter· default 100).', 'thinning': 'Thinning step (default 1).', 'include_mean': 'Include a constant term (default True).', 'seed': 'Seed· MANDATORY for ssvs/horseshoe (MCMC).', 'rhat_max': 'Maximum acceptable Rhat convergence gate (default 1.1).', 'ess_min': 'Minimum acceptable Bulk-ESS (default 100).', 'allow_nonconvergence': 'True -> return draws with converged=False instead of stop (default False).'},
        'input_example': {'y': '<multiseries_handle>', 'p': 1, 'prior': 'minnesota', 'lambda': 0.1, 'num_chains': 2, 'num_iter': 200, 'num_burn': 100, 'thinning': 1, 'include_mean': True, 'rhat_max': 1.1, 'ess_min': 100, 'allow_nonconvergence': False},
    },
    'bvh_vhar': {
        'fn': 'bvh_vhar',
        'description': 'bvh_vhar -- category 03-multivariate-nowcasting, method card #147.',
        'args': {'y': 'Handle to multivariate data (>=2 columns, finite).', 'har': 'VHAR thresholds (week, month)· 2 increasing positive integers (default [5,22]).', 'prior': 'Prior: minnesota=conjugate/analytic· ssvs/horseshoe=MCMC.', 'lambda': 'Minnesota tightness > 0 (default 0.1).', 'num_chains': 'MCMC chains (>=2· default 2).', 'num_iter': 'MCMC iterations (default 200).', 'num_burn': 'Burn-in (< num_iter· default 100).', 'thinning': 'Thinning step (default 1).', 'include_mean': 'Include a constant term (default True).', 'seed': 'Seed· MANDATORY for ssvs/horseshoe.', 'rhat_max': 'Maximum Rhat gate (default 1.1).', 'ess_min': 'Minimum Bulk-ESS (default 100).', 'allow_nonconvergence': 'True -> converged=False instead of stop (default False).'},
        'input_example': {'y': '<multiseries_handle>', 'har': [1, 1], 'prior': 'minnesota', 'lambda': 0.1, 'num_chains': 2, 'num_iter': 200, 'num_burn': 100, 'thinning': 1, 'include_mean': True, 'rhat_max': 1.1, 'ess_min': 100, 'allow_nonconvergence': False},
    },
    'bvr_coef': {
        'fn': 'bvr_coef',
        'description': 'bvr_coef -- category 03-multivariate-nowcasting, method card #142.',
        'args': {'model': 'Handle to a BigVAR.results model (sparse coefficient matrix k x kp+1).'},
        'input_example': {'model': '<raw_handle>'},
    },
    'bvr_fit': {
        'fn': 'bvr_fit',
        'description': 'bvr_fit -- category 03-multivariate-nowcasting, method card #142.',
        'args': {'Y': 'Handle to a multivariate series (panel, T x k, k>=2, no NA).', 'p': 'Maximum VAR lag order (positive integer, default 1).', 'struct': 'Penalty structure (default Basic· HLAG*/Tapered VAR-only· EFX VARX-only).', 'gran': '[penalty_grid_depth, n_lambda] — two positive integers (default [50,10]).', 'h': 'Forecast horizon for the CV (positive integer, default 1).', 'cv': 'Cross-validation: Rolling (default) or LOO leave-one-out.', 'T1': 'CV start index (default floor(T/3)· requires p < T1 < T2).', 'T2': 'Forecast-evaluation start index (default floor(2T/3)· T1 < T2 <= T).', 'IC': 'Include AIC/BIC benchmarks (default True).', 'ONESE': 'One-Standard-Error heuristic for lambda selection (default False).'},
        'input_example': {'Y': '<multiseries_handle>', 'p': 1, 'h': 1, 'IC': True, 'ONESE': False},
    },
    'bvr_predict': {
        'fn': 'bvr_predict',
        'description': 'bvr_predict -- category 03-multivariate-nowcasting, method card #142.',
        'args': {'model': 'Handle to a BigVAR.results model (from bvr_fit).', 'n_ahead': 'Horizon· returns a forecast path n.ahead x k (default 1).', 'confint': 'Return the 95% CI (lower/upper) in addition to the point forecast (default False).'},
        'input_example': {'model': '<raw_handle>', 'n_ahead': 1, 'confint': False},
    },
    'bvs_estimate': {
        'fn': 'bvs_estimate',
        'description': 'bvs_estimate -- category 03-multivariate-nowcasting, method card #143.',
        'args': {'data': 'Handle to a numeric matrix with >=2 columns (multivariate VAR)· no NA/Inf· nrow>lags+1.', 'lags': 'VAR order (positive integer· default 1).', 'prior': 'Global-local shrinkage prior on Phi (default HS = Horseshoe)· specify_prior_phi.', 'draws': 'Retained posterior draws (positive integer· TINY default 200).', 'burnin': 'Burn-in draws (non-negative integer· default 100).', 'thin': 'Thinning factor (positive integer <= draws· default 1).', 'sv_keep': 'Which log-variance draws to keep (default last).', 'seed': 'MANDATORY seed (seeded before the MCMC· cache key· bvar is stochastic).', 'min_draws': 'Minimum retained draws for convergence (non-negative· default 100).', 'ess_min': 'Minimum effective sample size of Phi (positive· default 1).', 'allow_nonconvergence': 'True = return the posterior with converged=False instead of stop when the gate fires .'},
        'input_example': {'data': '<matrix_handle>', 'lags': 1, 'draws': 200, 'burnin': 100, 'thin': 1, 'seed': 1, 'min_draws': 100, 'ess_min': 1, 'allow_nonconvergence': False},
    },
    'bvs_irf': {
        'fn': 'bvs_irf',
        'description': 'bvs_irf -- category 03-multivariate-nowcasting, method card #143.',
        'args': {'model': "Handle to a 'bayesianVARs_bvar' model (bvs_estimate.model).", 'ahead': 'Impulse response horizon 0..ahead (positive integer· default 8).', 'quantiles': 'Quantile bands of the IRF ∈ (0,1) (default 0.05/0.5/0.95).'},
        'input_example': {'model': '<raw_handle>', 'ahead': 8},
    },
    'bvs_predict': {
        'fn': 'bvs_predict',
        'description': 'bvs_predict -- category 03-multivariate-nowcasting, method card #143.',
        'args': {'model': "Handle to a 'bayesianVARs_bvar' model (bvs_estimate.model).", 'ahead': 'Forecast horizon· horizons 1..ahead (positive integer· default 4).', 'stable': 'Discard non-stable draws before forecasting (stable_bvar· default True).', 'quantiles': 'Quantiles of the predictive fan chart ∈ (0,1) (default 0.05/0.25/0.5/0.75/0.95).', 'LPL': 'True = compute the log predictive likelihood (requires Y_obs).', 'Y_obs': 'Realised values [ahead x M] for LPL (only when LPL=True).', 'seed': 'MANDATORY seed (predict is stochastic· simulate_predictive).'},
        'input_example': {'model': '<raw_handle>', 'ahead': 4, 'stable': True, 'LPL': False, 'seed': 1},
    },
    'df_fit': {
        'fn': 'df_fit',
        'description': 'df_fit -- category 03-multivariate-nowcasting, method card #15.',
        'args': {'X': 'Handle to panel data (T x n, >=2 columns, T>=10).', 'r': 'Number of factors· None -> automatic IC2 selection (requires no NA).', 'p': 'VAR lag order of the factors (default 1).', 'idio_ar1': 'AR(1) idiosyncratic components (default False).', 'rQ': 'Restriction on the state covariance Q (default none).', 'rR': 'Restriction on the observation covariance the reference (default diagonal).'},
        'input_example': {'X': '<multiseries_handle>', 'p': 1, 'idio_ar1': False},
    },
    'df_select_factors': {
        'fn': 'df_select_factors',
        'description': 'df_select_factors -- category 03-multivariate-nowcasting, method card #15.',
        'args': {'X': 'Handle to panel data (T x n, >=2 columns, no NA).', 'max_r': 'Maximum number of factors to evaluate (default min(20, n-1)).'},
        'input_example': {'X': '<multiseries_handle>'},
    },
    'df_predict': {
        'fn': 'df_predict',
        'description': 'df_predict -- category 03-multivariate-nowcasting, method card #15.',
        'args': {'model': 'Handle to a dfm model (from df_fit).', 'h': 'Forecast horizon for factors + variables (default 10).', 'standardized': 'Output in standardised units (default False = original units).'},
        'input_example': {'model': '<raw_handle>', 'h': 10, 'standardized': False},
    },
    'df_summary': {
        'fn': 'df_summary',
        'description': 'df_summary -- category 03-multivariate-nowcasting, method card #15.',
        'args': {'model': 'Handle to a dfm model (loadings/R2/explained variance).'},
        'input_example': {'model': '<raw_handle>'},
    },
    'md_forecast': {
        'fn': 'md_forecast',
        'description': 'md_forecast -- category 03-multivariate-nowcasting, method card #18.',
        'args': {'model': 'Handle to a midas_r model (from md_fit).', 'newx': 'Handle to future high-freq values (length = h*m).', 'm': 'Frequency ratio (same as the fit).'},
        'input_example': {'model': '<raw_handle>', 'newx': '<raw_handle>', 'm': 1},
    },
    'md_adequacy_test': {
        'fn': 'md_adequacy_test',
        'description': 'md_adequacy_test -- category 03-multivariate-nowcasting, method card #18.',
        'args': {'model': 'Handle to a midas_r model (from md_fit).', 'robust': 'HAC-robust hAhr_test instead of hAh_test (default False).'},
        'input_example': {'model': '<raw_handle>', 'robust': False},
    },
    'md_fit': {
        'fn': 'md_fit',
        'description': 'md_fit -- category 03-multivariate-nowcasting, method card #18.',
        'args': {'y': 'Handle to a low-freq numeric vector (dependent).', 'x': 'Handle to a high-freq numeric vector (length = m*length(y)).', 'm': 'Frequency ratio (high:low, e.g. 3 for monthly->quarterly).', 'k': 'Maximum high-freq lag (default 7).', 'weight': 'MIDAS weight scheme (default nealmon = exponential Almon).', 'poly_degree': "Polynomial degree for weight='almonp' (default 2).", 'trend': 'Include a linear trend (default False).'},
        'input_example': {'y': '<raw_handle>', 'x': '<raw_handle>', 'm': 1, 'k': 7, 'poly_degree': 2, 'trend': False},
    },
    'md_select': {
        'fn': 'md_select',
        'description': 'md_select -- category 03-multivariate-nowcasting, method card #18.',
        'args': {'y': 'Handle to a low-freq numeric vector (dependent).', 'x': 'Handle to a high-freq numeric vector (length = m*length(y)).', 'm': 'Frequency ratio (high:low).', 'k': 'Maximum high-freq lag (default 7).', 'ic': 'Selection criterion for the weight scheme (default AIC).', 'poly_degree': 'Polynomial degree for almonp (default 2).', 'trend': 'Include a linear trend (default False).'},
        'input_example': {'y': '<raw_handle>', 'x': '<raw_handle>', 'm': 1, 'k': 7, 'poly_degree': 2, 'trend': False},
    },
    'mf_estimate': {
        'fn': 'mf_estimate',
        'description': 'mf_estimate -- category 03-multivariate-nowcasting, method card #17.',
        'args': {'Y': 'Handle to a list of >=2 ts of different frequencies (monthly before quarterly).', 'n_lags': "VAR lag order (with aggregation='average' >=3).", 'n_reps': 'MCMC replications (default 10000).', 'n_burnin': 'Burn-in draws· None -> n_reps/2 (< n_reps).', 'n_fcst': 'Forecast/nowcast horizon (>0 for mf_predict) (default 0).', 'prior': 'Prior: Minnesota or steady-state (default minn).', 'variance': 'Variance structure (default iw· mf_mdd requires iw).', 'aggregation': 'Low-to-high frequency relation (default average).', 'seed': 'Seed for reproducibility (optional).'},
        'input_example': {'Y': '<raw_handle>', 'n_lags': 1, 'n_reps': 10000, 'n_fcst': 0},
    },
    'mf_mdd': {
        'fn': 'mf_mdd',
        'description': 'mf_mdd -- category 03-multivariate-nowcasting, method card #17.',
        'args': {'model': "Handle to an mfbvar model with variance='iw' (model comparison).", 'p_trunc': 'Truncation prob for the minn prior in (0,1) (default 0.5).', 'method': 'mdd method (1 or 2) for the steady-state prior (default 1).'},
        'input_example': {'model': '<raw_handle>', 'p_trunc': 0.5, 'method': 1},
    },
    'mf_predict': {
        'fn': 'mf_predict',
        'description': 'mf_predict -- category 03-multivariate-nowcasting, method card #17.',
        'args': {'model': 'Handle to an mfbvar model (from mf_estimate with n_fcst>0).', 'pred_bands': 'Prediction band in (0,1) (default 0.8).', 'aggregate_fcst': 'Aggregate high -> low frequency (default True).'},
        'input_example': {'model': '<raw_handle>', 'pred_bands': 0.8, 'aggregate_fcst': True},
    },
    'mml_cv': {
        'fn': 'mml_cv',
        'description': 'mml_cv -- category 03-multivariate-nowcasting, method card #145.',
        'args': {'y': 'Low-frequency target (T x 1, aligned with X).', 'X': 'High-frequency predictor block (T x p· columns per predictor).', 'group': 'Predictor label per column of X (length==the column count of X).', 'degree': 'Degree of the polynomial basis (default 3).', 'weight': 'MIDAS weighting basis (default legendre).', 'gb_alpha': 'Gegenbauer alpha (only for weight=gegenbauer).', 'gamma': 'sg-LASSO mixing in [0,1] (default 0.5).', 'lambda': 'Optional sequence of positive lambda values (otherwise an automatic path).', 'nfolds': 'Number of CV folds (3..nrow, default 10).', 'intercept': 'Fit an intercept (default True).', 'standardize': 'Standardise the regressors (default False).', 'seed': 'Seed for a reproducible fold partition (CV resampling -> determinism/cache).'},
        'input_example': {'y': [0.5, 0.5], 'X': '<matrix_handle>', 'group': [1, 1], 'degree': 3, 'gb_alpha': 1, 'gamma': 0.5, 'nfolds': 10, 'intercept': True, 'standardize': False},
    },
    'mml_fit': {
        'fn': 'mml_fit',
        'description': 'mml_fit -- category 03-multivariate-nowcasting, method card #145.',
        'args': {'y': 'Low-frequency target (T x 1 numeric vector, aligned with X).', 'X': 'High-frequency predictor block (T x p)· columns grouped per predictor (jmax lags each).', 'group': 'Predictor label per column of X (length==the column count of X)· defines the MIDAS blocks.', 'degree': 'Degree of the polynomial basis (degree+1 basis functions per predictor· default 3).', 'weight': 'MIDAS weighting basis (default legendre· none = no lag compression).', 'gb_alpha': 'Gegenbauer alpha parameter (only for weight=gegenbauer· alpha=0 -> Legendre).', 'gamma': 'sg-LASSO mixing in [0,1] (0 = group LASSO, 1 = LASSO· default 0.5).', 'lambda': 'Optional sequence of positive lambda values (otherwise an automatic lambda path).', 'nlambda': 'Length of the automatic lambda path (default 100).', 'intercept': 'Fit an intercept (default True).', 'standardize': 'Standardise the regressors (default False· the MIDAS basis is already orthonormal).'},
        'input_example': {'y': [0.5, 0.5], 'X': '<matrix_handle>', 'group': [1, 1], 'degree': 3, 'gb_alpha': 1, 'gamma': 0.5, 'nlambda': 100, 'intercept': True, 'standardize': False},
    },
    'mml_predict': {
        'fn': 'mml_predict',
        'description': 'mml_predict -- category 03-multivariate-nowcasting, method card #145.',
        'args': {'model': "Handle to an 'mml_model' (from mml_fit or mml_cv).", 'newx': 'New high-frequency block· ncol == length(group) of the fit (same lag structure).', 's': 'lambda selection for a CV model (lam.min default)· for a path model leave it empty (uses the default lambda).'},
        'input_example': {'model': '<raw_handle>', 'newx': '<matrix_handle>'},
    },
    'pn_cyclical_components': {
        'fn': 'pn_cyclical_components',
        'description': 'pn_cyclical_components -- category 03-multivariate-nowcasting, method card #256.',
        'args': {'x': 'Handle to a NUMERIC matrix ROWS = TIME, COLUMNS = VARIABLES (>= 2 series). You do NOT need to know which series are I(0) and which are I(1) — that IS the point of the method; do NOT difference and do NOT detrend first. Balanced sample: NOT NA/NaN/Inf. NO constant series and no DETERMINISTIC one (y_t = a + b·t) — its lags are collinear. Take logs upstream of whatever is described in growth rates (output/prices); rates enter as is.', 'h': "Forecast horizon h of eq. (7) — POSITIVE INTEGER. Default 24 = TWO YEARS on MONTHLY data (the paper's recommendation; maximum agreement of 99% with NBER recessions at h=25, 98% at h=24). For QUARTERLY data use h=8. Every h >= 1 produces a stationary cyclical component; larger h => fewer outliers but more autocorrelation (risk of a spurious factor in SMALL samples: with < 50 years prefer h=12 or h=1).", 'p': 'Number of own lags p of eq. (7) — POSITIVE INTEGER. Default 12 = ONE YEAR on MONTHLY data (4 for quarterly): the paper recommends p = observations per year so that lingering seasonal components are covered. p is ALSO the maximum integration order d_i <= p that is neutralized. T >= h + 2p + 1 IS REQUIRED.'},
        'input_example': {'x': '<matrix_handle>', 'h': 24, 'p': 12},
    },
    'pn_pca_nonstationary': {
        'fn': 'pn_pca_nonstationary',
        'description': 'pn_pca_nonstationary -- category 03-multivariate-nowcasting, method card #256.',
        'args': {'x': 'Handle to a NUMERIC matrix ROWS = TIME, COLUMNS = VARIABLES (>= 2 series). You do NOT need to know which series are I(0) and which are I(1) — that IS the point of the method; do NOT difference and do NOT detrend first. Balanced sample: NOT NA/NaN/Inf. NO constant series and no DETERMINISTIC one (y_t = a + b·t) — its lags are collinear. Take logs upstream of whatever is described in growth rates (output/prices); rates enter as is.', 'h': "Forecast horizon h of eq. (7) — POSITIVE INTEGER. Default 24 = TWO YEARS on MONTHLY data (the paper's recommendation; maximum agreement of 99% with NBER recessions at h=25, 98% at h=24). For QUARTERLY data use h=8. Every h >= 1 produces a stationary cyclical component; larger h => fewer outliers but more autocorrelation (risk of a spurious factor in SMALL samples: with < 50 years prefer h=12 or h=1).", 'p': 'Number of own lags p of eq. (7) — POSITIVE INTEGER. Default 12 = ONE YEAR on MONTHLY data (4 for quarterly): the paper recommends p = observations per year so that lingering seasonal components are covered. p is ALSO the maximum integration order d_i <= p that is neutralized. T >= h + 2p + 1 IS REQUIRED.', 'scale_residuals': 'Scaling OF THE RESIDUALS (NEVER of the raw series — this is the INVALID step on non-stationary data; the sample sd of an I(1) series DIVERGES with T, while that of the residuals CONVERGES). \'unit_variance\' (DEFAULT) = each residual series is divided by its sd => PCA on the CORRELATION MATRIX; this IS the paper\'s procedure (§6.3 "Since ĉ_it is normalized to have unit variance" and eqs. 18-19 defined over the correlation matrix). \'none\' = the COVARIANCE matrix — only for series ALREADY of common scale; then var_explained does NOT coincide with r2_eigen (see pca_matrix). The fitted scale params are returned (residual_scale) => reproducible out-of-sample apply.', 'r_max': 'Maximum number of factors for the Bai-Ng IC_p2 criterion (eq. 19; the paper uses r0 = 10). Automatically capped at min(N-1, T_eff-1) and the EFFECTIVE value is returned as r_max_effective. IC_p2 is VALID HERE (on the residuals) while it is CORRUPTED on non-stationary levels.'},
        'input_example': {'x': '<matrix_handle>', 'h': 24, 'p': 12, 'r_max': 10},
    },
    'sdf_factors': {
        'fn': 'sdf_factors',
        'description': 'sdf_factors -- category 03-multivariate-nowcasting, method card #144.',
        'args': {'model': 'Handle to a sparseDFM model (extracts factor paths + covariances).'},
        'input_example': {'model': '<raw_handle>'},
    },
    'sdf_fit': {
        'fn': 'sdf_fit',
        'description': 'sdf_fit -- category 03-multivariate-nowcasting, method card #144.',
        'args': {'X': 'Handle to panel data (T x p, >=2 columns, T>=10· NA allowed).', 'r': 'Number of factors· positive integer with 1 <= r < the column count of X.', 'method': 'Estimation algorithm (default EM-sparse = LASSO sparse loadings).', 'err': 'Idiosyncratic errors (default IID· AR1 does NOT support sdf_predict).', 'q': 'The first q series are NOT made sparse (default 0· 0 <= q < the column count of X).', 'alpha': 'Grid LASSO penalties (>=0)· None -> logspace(-2,3,100) default (EM-sparse).', 'standardize': 'Standardise the data before estimation (default True).', 'max_iter': 'Maximum EM iterations (default 100).', 'threshold': 'Convergence tolerance of the EM iterates (default 1e-4).'},
        'input_example': {'X': '<multiseries_handle>', 'r': 1, 'q': 0, 'standardize': True, 'max_iter': 100, 'threshold': 0.0001},
    },
    'sdf_predict': {
        'fn': 'sdf_predict',
        'description': 'sdf_predict -- category 03-multivariate-nowcasting, method card #144.',
        'args': {'model': "Handle to a sparseDFM model (from sdf_fit· requires err='IID').", 'h': 'Forecast/nowcast horizon (default 1).', 'standardize': 'Output in standardised units (default False = original units).'},
        'input_example': {'model': '<raw_handle>', 'h': 1, 'standardize': False},
    },
    'stv_estimate': {
        'fn': 'stv_estimate',
        'description': 'stv_estimate -- category 03-multivariate-nowcasting, method card #146.',
        'args': {'y': 'Handle to a multivariate series (panel, T x k, k>=2, no NA/Inf, nrow>p+1).', 'p': 'VAR lag order (positive integer, default 1).', 'mod_type': 'Prior shrinkage: double gamma (default) / triple gamma / ridge.', 'const': 'Include a time-varying intercept (default True).', 'niter': 'MCMC iterations including burn-in (positive integer, default 200).', 'nburn': 'Burn-in draws (non-negative, <= niter-2, default 100).', 'nthin': 'Thinning: every nthin-th draw is kept (default 1).', 'seed': 'MANDATORY seed (integer) — MCMC· seeded before sampling.', 'ess_min': 'Minimum acceptable min-ESS (convergence gate· production >=200).', 'min_draws': 'Minimum retained draws for the convergence assessment (default 20).', 'allow_nonconvergence': 'If True, return a non-converged result (converged=False) instead of stop.'},
        'input_example': {'y': '<multiseries_handle>', 'p': 1, 'const': True, 'niter': 200, 'nburn': 100, 'nthin': 1, 'seed': 1, 'ess_min': 10, 'min_draws': 20, 'allow_nonconvergence': False},
    },
    'stv_forecast': {
        'fn': 'stv_forecast',
        'description': 'stv_forecast -- category 03-multivariate-nowcasting, method card #146.',
        'args': {'model': "Handle to a 'shrinkTVPVAR' model (from stv_estimate).", 'n_ahead': 'Posterior predictive horizon (positive integer, default 1).', 'probs': 'Quantiles ∈ (0,1) for the fan grid (default 0.05/0.25/0.5/0.75/0.95).'},
        'input_example': {'model': '<raw_handle>', 'n_ahead': 1},
    },
    'stv_tvp': {
        'fn': 'stv_tvp',
        'description': 'stv_tvp -- category 03-multivariate-nowcasting, method card #146.',
        'args': {'model': "Handle to a 'shrinkTVPVAR' model (from stv_estimate).", 'equation': 'Equation/variable index 1..m for extracting coefficient paths (default 1).', 'probs': 'Quantiles ∈ (0,1) for the posterior bands over time (default 0.05/0.5/0.95).', 'include_intercept': 'Include the time-varying intercept path (if const, default True).'},
        'input_example': {'model': '<raw_handle>', 'equation': 1, 'include_intercept': True},
    },
    'sv_estimate': {
        'fn': 'sv_estimate',
        'description': 'sv_estimate -- category 03-multivariate-nowcasting, method card #14.',
        'args': {'Y': 'Handle to multivariate data (>=2 columns, finite).', 'p': 'VAR lag order (default 1).', 'tau': 'Training sample size for the LS prior (>= ncol*p+1, default 40).', 'nf': 'Forecast horizon that is stored (default 10).', 'nrep': 'MCMC replications after burn-in (default 50000).', 'nburn': 'Burn-in draws (default 5000).', 'thinfac': 'Thinning factor (default 10).', 'seed': 'Seed for reproducibility (optional).'},
        'input_example': {'Y': '<multiseries_handle>', 'p': 1, 'tau': 40, 'nf': 10, 'nrep': 50000, 'nburn': 5000, 'thinfac': 10},
    },
    'sv_irf': {
        'fn': 'sv_irf',
        'description': 'sv_irf -- category 03-multivariate-nowcasting, method card #14.',
        'args': {'model': 'Handle to a TVP-VAR-SV fit (from sv_estimate, save.parameters).', 'impulse': 'Shock variable index (1..M) (default 1).', 'response': 'Response variable index (1..M) (default 2).', 'horizon': 'IRF horizon (default 20).', 'scenario': '1=no orthogonalization, 2=Cholesky, 3=DNP (default 2).'},
        'input_example': {'model': '<raw_handle>', 'impulse': 1, 'response': 2, 'horizon': 20, 'scenario': 2},
    },
    'sv_parameter_draws': {
        'fn': 'sv_parameter_draws',
        'description': 'sv_parameter_draws -- category 03-multivariate-nowcasting, method card #14.',
        'args': {'model': 'Handle to a TVP-VAR-SV fit (from sv_estimate, save.parameters).', 'type': "Parameter: 'intercept', 'lag1'..'lagP' or 'vcv' (default 'lag1').", 'row': 'Row of the coefficient matrix (default 1).', 'col': 'Column of the coefficient matrix (default 1).'},
        'input_example': {'model': '<raw_handle>', 'type': 'lag1', 'row': 1, 'col': 1},
    },
    'sv_predict_density': {
        'fn': 'sv_predict_density',
        'description': 'sv_predict_density -- category 03-multivariate-nowcasting, method card #14.',
        'args': {'model': 'Handle to a TVP-VAR-SV fit (from sv_estimate).', 'variable': 'Variable index (1..M) (default 1).', 'horizon': 'Forecast horizon (1..nf) (default 1).', 'n_grid': 'Number of grid points at which the density is evaluated (default 101).', 'cdf': 'Return the CDF instead of the PDF (default False).'},
        'input_example': {'model': '<raw_handle>', 'variable': 1, 'horizon': 1, 'n_grid': 101, 'cdf': False},
    },
    'sv_predict_draws': {
        'fn': 'sv_predict_draws',
        'description': 'sv_predict_draws -- category 03-multivariate-nowcasting, method card #14.',
        'args': {'model': 'Handle to a TVP-VAR-SV fit (from sv_estimate).', 'variable': 'Variable index (1..M) (default 1).', 'horizon': 'Forecast horizon (1..nf) (default 1).'},
        'input_example': {'model': '<raw_handle>', 'variable': 1, 'horizon': 1},
    },
    'vr_arch_test': {
        'fn': 'vr_arch_test',
        'description': 'vr_arch_test -- category 03-multivariate-nowcasting, method card #11.',
        'args': {'model': 'Handle to a varest/vec2var model.', 'lags_single': 'Univariate ARCH-LM lags (default 16).', 'lags_multi': 'Multivariate ARCH-LM lags (default 5).', 'multivariate_only': 'Multivariate test only (default True).'},
        'input_example': {'model': '<raw_handle>', 'lags_single': 16, 'lags_multi': 5, 'multivariate_only': True},
    },
    'vr_causality': {
        'fn': 'vr_causality',
        'description': 'vr_causality -- category 03-multivariate-nowcasting, method card #11.',
        'args': {'model': 'Handle to a varest model (from vr_fit).', 'cause': 'Name of the causing variable (a subset of the VAR variables).', 'boot': 'Bootstrap p-values (default False).', 'boot_runs': 'Number of bootstrap replications (default 100).'},
        'input_example': {'model': '<raw_handle>', 'cause': '...', 'boot': False, 'boot_runs': 100},
    },
    'vr_normality_test': {
        'fn': 'vr_normality_test',
        'description': 'vr_normality_test -- category 03-multivariate-nowcasting, method card #11.',
        'args': {'model': 'Handle to a varest/vec2var model.', 'multivariate_only': 'Multivariate Jarque-Bera only (default True).'},
        'input_example': {'model': '<raw_handle>', 'multivariate_only': True},
    },
    'vr_predict': {
        'fn': 'vr_predict',
        'description': 'vr_predict -- category 03-multivariate-nowcasting, method card #11.',
        'args': {'model': 'Handle to a varest/vec2var model (from vr_fit/vr_vecm_to_var).', 'n_ahead': 'Forecast horizon (default 10).', 'ci': 'Fan chart confidence level in (0,1) (default 0.95).'},
        'input_example': {'model': '<raw_handle>', 'n_ahead': 10, 'ci': 0.95},
    },
    'vr_serial_test': {
        'fn': 'vr_serial_test',
        'description': 'vr_serial_test -- category 03-multivariate-nowcasting, method card #11.',
        'args': {'model': 'Handle to a varest/vec2var model.', 'lags_pt': 'Portmanteau lags (default 16).', 'lags_bg': 'Breusch-Godfrey lags (default 5).', 'type': 'Test variant (default PT.asymptotic).'},
        'input_example': {'model': '<raw_handle>', 'lags_pt': 16, 'lags_bg': 5},
    },
    'vr_fit': {
        'fn': 'vr_fit',
        'description': 'vr_fit -- category 03-multivariate-nowcasting, method card #11.',
        'args': {'y': 'Handle to a multivariate series (panel, K>=2 columns, no NA).', 'p': 'VAR(p) lag order (default 1).', 'type': 'Deterministic part (default const).'},
        'input_example': {'y': '<multiseries_handle>', 'p': 1},
    },
    'vr_lag_select': {
        'fn': 'vr_lag_select',
        'description': 'vr_lag_select -- category 03-multivariate-nowcasting, method card #11.',
        'args': {'y': 'Handle to a multivariate series (panel, K>=2 columns).', 'lag_max': 'Maximum lag order to evaluate (default 10).', 'type': 'Deterministic part (default const).'},
        'input_example': {'y': '<multiseries_handle>', 'lag_max': 10},
    },
    'vr_vecm_to_var': {
        'fn': 'vr_vecm_to_var',
        'description': 'vr_vecm_to_var -- category 03-multivariate-nowcasting, method card #11.',
        'args': {'z': 'Handle to a Johansen Johansen object .', 'r': 'Cointegration rank r (1..K) (default 1).'},
        'input_example': {'z': '<raw_handle>', 'r': 1},
    },
    'mn_nowcast_news': {
        'fn': 'mn_nowcast_news',
        'description': 'mn_nowcast_news -- category 03-multivariate-nowcasting, method card #416.',
        'args': {'fit': 'Handle to a fitted dynamic factor model.', 'vintage_old': 'Earlier data vintage.', 'vintage_new': 'Later data vintage.', 'target': 'Variable being nowcast.', 'period': 'Target period.'},
        'input_example': {'fit': '<raw_handle>', 'vintage_old': '<df_handle>', 'vintage_new': '<df_handle>', 'target': '...', 'period': '...'},
    },
    'mn_nowcast_weights': {
        'fn': 'mn_nowcast_weights',
        'description': 'mn_nowcast_weights -- category 03-multivariate-nowcasting, method card #416.',
        'args': {'fit': 'Handle to a fitted dynamic factor model.', 'target': 'Variable being nowcast.'},
        'input_example': {'fit': '<raw_handle>', 'target': '...'},
    },
    'mn_conditional_forecast': {
        'fn': 'mn_conditional_forecast',
        'description': 'mn_conditional_forecast -- category 03-multivariate-nowcasting, method card #417.',
        'args': {'fit': 'Handle to a fitted multivariate model.', 'conditions': 'Conditioning paths, one column per constrained variable.', 'h': 'Forecast horizon.', 'method': 'Conditioning scheme.', 'shocks': 'Shocks used to achieve the conditioning.', 'levels': 'Prediction interval levels.'},
        'input_example': {'fit': '<raw_handle>', 'conditions': '<df_handle>', 'h': 1, 'method': 'hard', 'levels': [0.68, 0.9]},
    },
    'mn_favar': {
        'fn': 'mn_favar',
        'description': 'mn_favar -- category 03-multivariate-nowcasting, method card #418.',
        'args': {'panel': 'Large panel of indicators.', 'observed': 'Observed variables entering the VAR directly.', 'n_factors': 'Number of factors; omitted = selected by criterion.', 'lags': 'VAR lag order.', 'standardise': 'Standardise the panel before extraction.'},
        'input_example': {'panel': '<df_handle>', 'observed': '<multiseries_handle>', 'lags': 4, 'standardise': True},
    },
    'mn_varmax': {
        'fn': 'mn_varmax',
        'description': 'mn_varmax -- category 03-multivariate-nowcasting, method card #419.',
        'args': {'y': 'Endogenous variables.', 'exog': 'Exogenous variables.', 'order': 'Autoregressive and moving-average orders.', 'trend': 'Deterministic terms.', 'error_cov_type': 'Error covariance structure.'},
        'input_example': {'y': '<multiseries_handle>', 'order': [1, 0], 'trend': 'c', 'error_cov_type': 'unstructured'},
    },
    'mn_bridge_equation': {
        'fn': 'mn_bridge_equation',
        'description': 'mn_bridge_equation -- category 03-multivariate-nowcasting, method card #420.',
        'args': {'target': 'Low-frequency target.', 'indicator': 'High-frequency indicator.', 'aggregation': 'How the indicator is aggregated.', 'fill': 'Ragged-edge handling.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'target': '<series_handle>', 'indicator': '<series_handle>', 'aggregation': 'mean', 'fill': 'arima', 'conf_level': 0.95},
    },
    'mn_umidas': {
        'fn': 'mn_umidas',
        'description': 'mn_umidas -- category 03-multivariate-nowcasting, method card #420.',
        'args': {'target': 'Low-frequency target.', 'indicator': 'High-frequency indicator.', 'n_lags': 'High-frequency lags included.', 'frequency_ratio': 'High- to low-frequency ratio.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'target': '<series_handle>', 'indicator': '<series_handle>', 'n_lags': 6, 'frequency_ratio': 1, 'conf_level': 0.95},
    },
    'mn_large_bvar': {
        'fn': 'mn_large_bvar',
        'description': 'mn_large_bvar -- category 03-multivariate-nowcasting, method card #421.',
        'args': {'y': 'Endogenous variables.', 'lags': 'Lag order.', 'prior': 'Prior family.', 'lambda_': 'Overall shrinkage; omitted = chosen by marginal likelihood.', 'sum_of_coefficients': 'Add the sum-of-coefficients dummy observations.', 'co_persistence': 'Add the co-persistence dummy observation.', 'draws': 'Posterior draws.', 'seed': 'Seed for the random number generator; required for reproducibility.'},
        'input_example': {'y': '<multiseries_handle>', 'lags': 13, 'prior': 'minnesota', 'sum_of_coefficients': True, 'co_persistence': True, 'draws': 2000, 'seed': 1},
    },
    'mn_shadow_rate_var': {
        'fn': 'mn_shadow_rate_var',
        'description': 'mn_shadow_rate_var -- category 03-multivariate-nowcasting, method card #422.',
        'args': {'y': 'Endogenous variables including the policy rate.', 'policy_rate': 'Column holding the policy rate.', 'lower_bound': 'Effective lower bound.', 'lags': 'Lag order.', 'draws': 'Posterior draws.', 'seed': 'Seed for the random number generator; required for reproducibility.'},
        'input_example': {'y': '<multiseries_handle>', 'policy_rate': '...', 'lower_bound': 0.0, 'lags': 4, 'draws': 2000, 'seed': 1},
    },
    'mn_sparse_var': {
        'fn': 'mn_sparse_var',
        'description': 'mn_sparse_var -- category 03-multivariate-nowcasting, method card #423.',
        'args': {'y': 'Endogenous variables.', 'lags': 'Maximum lag order.', 'penalty': 'Penalty family.', 'lambda_': 'Penalty strength; omitted = cross-validated.', 'n_folds': 'Time-series cross-validation folds.', 'own_lag_penalty': 'Relative penalty on own lags.'},
        'input_example': {'y': '<multiseries_handle>', 'lags': 12, 'penalty': 'lasso', 'n_folds': 5, 'own_lag_penalty': 0.5},
    },
}
