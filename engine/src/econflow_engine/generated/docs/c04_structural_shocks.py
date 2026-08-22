# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 04-structural-shocks: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'bss_estimate': {
        'fn': 'bss_estimate',
        'description': 'bss_estimate -- category 04-structural-shocks, method card #149.',
        'args': {'data': 'Handle to a multivariate series (matrix/series/panel, (T+p) x N, N>=2, no NA/Inf).', 'p': 'VAR lag order (positive integer, default 1).', 'sign_irf': 'NxN (horizon-0) matrix restrictions on the IRF: 1/-1 sign, 0 ZERO restriction, NA unrestricted. (For an NxNxH array see the L1 wrapper.)', 'sign_structural': 'NxN matrix {-1,1,NA} — sign restrictions on the contemporaneous relation B (BE=U).', 'S': 'Number of posterior draws (positive integer· default 100 — TINY· production raises it).', 'thin': 'MCMC thinning frequency (positive integer, default 1).', 'max_tries': 'Maximum attempts to find a valid rotation Q per iteration (finite -> prevents a hang on infeasible restrictions· L1 default Inf).', 'ess_min_ratio': 'Degeneracy threshold for the importance weights: ess/n_draws < this -> STOP (unreliable posterior). In (0,1], default 0.01.', 'allow_nonconvergence': 'True -> return with converged=False instead of STOP on degenerate weights (default False).', 'seed': 'MANDATORY seed (integer) — the Gibbs sampler is stochastic· seeded beforehand.'},
        'input_example': {'data': '<multiseries_handle>', 'p': 1, 'S': 100, 'thin': 1, 'max_tries': 10000, 'ess_min_ratio': 0.01, 'allow_nonconvergence': False, 'seed': 1},
    },
    'bss_fevd': {
        'fn': 'bss_fevd',
        'description': 'bss_fevd -- category 04-structural-shocks, method card #149.',
        'args': {'model': "Handle to a posterior 'PosteriorBSVARSIGN' (from bss_estimate).", 'horizon': 'FEVD horizon (positive integer, default 8).', 'lower_q': 'Lower quantile of the credible band in (0,1), < upper_q (default 0.16).', 'upper_q': 'Upper quantile of the credible band in (0,1), > lower_q (default 0.84).'},
        'input_example': {'model': '<raw_handle>', 'horizon': 8, 'lower_q': 0.16, 'upper_q': 0.84},
    },
    'bss_forecast': {
        'fn': 'bss_forecast',
        'description': 'bss_forecast -- category 04-structural-shocks, method card #149.',
        'args': {'model': "Handle to a posterior 'PosteriorBSVARSIGN' (from bss_estimate).", 'horizon': 'Forecast horizon (positive integer, default 4).', 'conditional_forecast': 'horizon x N matrix with numeric/NA — conditional forecast on the non-NA future values.', 'exogenous_forecast': 'horizon x d matrix of forecast exogenous variables (only if the model has exogenous).', 'lower_q': 'Lower quantile of the predictive band in (0,1), < upper_q (default 0.16).', 'upper_q': 'Upper quantile of the predictive band in (0,1), > lower_q (default 0.84).', 'seed': 'MANDATORY seed (integer) — the predictive-density sampling is stochastic· seeded beforehand.'},
        'input_example': {'model': '<raw_handle>', 'horizon': 4, 'lower_q': 0.16, 'upper_q': 0.84, 'seed': 1},
    },
    'bss_irf': {
        'fn': 'bss_irf',
        'description': 'bss_irf -- category 04-structural-shocks, method card #149.',
        'args': {'model': "Handle to a posterior 'PosteriorBSVARSIGN' (from bss_estimate).", 'horizon': 'IRF horizon (positive integer, default 8).', 'standardise': 'True -> standardise so that the own-shock response at horizon 0 = 1 (default False).', 'lower_q': 'Lower quantile of the credible band in (0,1), < upper_q (default 0.16).', 'upper_q': 'Upper quantile of the credible band in (0,1), > lower_q (default 0.84).'},
        'input_example': {'model': '<raw_handle>', 'horizon': 8, 'standardise': False, 'lower_q': 0.16, 'upper_q': 0.84},
    },
    'bsv_estimate': {
        'fn': 'bsv_estimate',
        'description': 'bsv_estimate -- category 04-structural-shocks, method card #148.',
        'args': {'data': 'Handle to a multivariate system (matrix/panel, K>=2, >=3 rows, no NA/Inf).', 'model': 'Identification through statistical structure: sv=stochastic volatility, msh=Markov-switching heteroskedasticity, t=Student-t (default sv).', 'p': 'VAR order (positive integer, default 1).', 'S': 'Retained posterior draws (TINY default 100· production raises it).', 'burnin': 'Burn-in draws (non-negative, default 50).', 'thin': 'Thinning factor (positive integer, default 1).', 'M': "Number of variance regimes (model='msh' only, >=2, default 2).", 'stationary': 'Impose the stationarity prior on the AR coefficients (default False).', 'seed': 'MANDATORY seed (the MCMC is stochastic· cache key).', 'allow_nonconvergence': 'True = return the posterior with converged=False instead of stop on degenerate draws .'},
        'input_example': {'data': '<matrix_handle>', 'p': 1, 'S': 100, 'burnin': 50, 'thin': 1, 'M': 2, 'stationary': False, 'seed': 1, 'allow_nonconvergence': False},
    },
    'bsv_fevd': {
        'fn': 'bsv_fevd',
        'description': 'bsv_fevd -- category 04-structural-shocks, method card #148.',
        'args': {'model': "Handle to a 'PosteriorBSVAR*' model.", 'horizon': 'FEVD horizon (positive integer, default 12).', 'probs': 'Quantile bands ∈ (0,1) (default 0.16/0.84).'},
        'input_example': {'model': '<raw_handle>', 'horizon': 12},
    },
    'bsv_hd': {
        'fn': 'bsv_hd',
        'description': 'bsv_hd -- category 04-structural-shocks, method card #148.',
        'args': {'model': "Handle to a 'PosteriorBSVAR*' model.", 'probs': 'Quantile bands ∈ (0,1) (default 0.16/0.84).'},
        'input_example': {'model': '<raw_handle>'},
    },
    'bsv_irf': {
        'fn': 'bsv_irf',
        'description': 'bsv_irf -- category 04-structural-shocks, method card #148.',
        'args': {'model': "Handle to a 'PosteriorBSVAR*' model (bsv_estimate.model).", 'horizon': 'Impulse-response horizon 0..horizon (positive integer, default 12).', 'standardise': 'Standardise the IRF in standard-deviation units (default False).', 'probs': 'Quantile bands of the posterior IRF ∈ (0,1) (default 0.16/0.84).'},
        'input_example': {'model': '<raw_handle>', 'horizon': 12, 'standardise': False},
    },
    'bsv_shocks': {
        'fn': 'bsv_shocks',
        'description': 'bsv_shocks -- category 04-structural-shocks, method card #148.',
        'args': {'model': "Handle to a 'PosteriorBSVAR*' model.", 'probs': 'Quantile bands ∈ (0,1) (default 0.16/0.84).'},
        'input_example': {'model': '<raw_handle>'},
    },
    'bsv_verify': {
        'fn': 'bsv_verify',
        'description': 'bsv_verify -- category 04-structural-shocks, method card #148.',
        'args': {'model': "Handle to a 'PosteriorBSVAR*' model (SDDR identification check).", 'allow_nonconvergence': 'True = return a degenerate SDDR instead of stop (default False).'},
        'input_example': {'model': '<raw_handle>', 'allow_nonconvergence': False},
    },
    'dlasso_inference': {
        'fn': 'dlasso_inference',
        'description': 'dlasso_inference -- category 04-structural-shocks, method card #152.',
        'args': {'X': 'Handle to a numeric matrix of regressors T x N (no NA/Inf· N>=T allowed — high-dim).', 'y': 'Dependent variable, numeric vector of length T (aligned with X).', 'H': 'Integer column indices of X in [1,N] that are tested (target coefficients).', 'seed': 'MANDATORY seed (integer) — the lasso lambda selection uses random CV folds· seeded beforehand.', 'alphas': 'Significance levels ∈ (0,1) for the CIs (default 0.05).', 'penalize_H': 'Penalise the H variables in the initial lasso (default True).', 'restriction': 'Matrix for testing H0: the reference*beta = q (default: identity -> joint significance of all H).', 'q': 'Right-hand-side vector for H0: the reference*beta = q (default: zeros). Activates row_tests.', 'demean': 'Demean X/y before estimation (recommended· default True).', 'scale': 'Scale X/y by the column-wise SD (penalty scale-sensitive· default True).'},
        'input_example': {'X': '<matrix_handle>', 'y': [0.5, 0.5], 'H': [1, 1], 'seed': 1, 'penalize_H': True, 'demean': True, 'scale': True},
    },
    'dlasso_local_projection': {
        'fn': 'dlasso_local_projection',
        'description': 'dlasso_local_projection -- category 04-structural-shocks, method card #152.',
        'args': {'x': 'Shock variable, numeric vector of length T (Plagborg-Moller & Wolf notation).', 'y': 'Response variable, numeric vector of length T (aligned with x).', 'seed': 'MANDATORY seed (integer) — lasso CV· seeded beforehand.', 'r': "'Slow' variables (do not react within the same period), T rows.", 'q': "'Fast' variables/controls (react within the same period), T rows — the high-dim space.", 'state_variables': 'State variables (categorical or binary indicators), T rows -> state-dependent IRF.', 'y_predetermined': 'True if y is predetermined with respect to x (IRF at horizon 0 = 0· default False).', 'cumulate_y': 'True for a cumulative IRF (uses cumsum of y· default False).', 'hmax': 'Maximum IRF horizon· positive integer with hmax+lags < T (default 10).', 'lags': 'Number of lags in the local projection· positive integer with hmax+lags < T (default 4).', 'alphas': 'Significance levels ∈ (0,1) for the CI bands (default 0.05).', 'penalize_x': 'Penalise the parameter of interest (default False).', 'OLS': 'Estimate with OLS instead of debiased lasso· ONLY for low-dimensional regressions (default False).'},
        'input_example': {'x': [0.5, 0.5], 'y': [0.5, 0.5], 'seed': 1, 'y_predetermined': False, 'cumulate_y': False, 'hmax': 10, 'lags': 4, 'penalize_x': False, 'OLS': False},
    },
    'gmv_fit': {
        'fn': 'gmv_fit',
        'description': 'gmv_fit -- category 04-structural-shocks, method card #151.',
        'args': {'data': 'Handle to a multivariate series (matrix/ts, T x d, d>=2, no NA/Inf).', 'p': 'VAR lag order (positive integer, default 1).', 'M': 'Number of regimes· positive integer (GMVAR/StMVAR) or a length-2 vector [M1,M2] for G-StMVAR (default 2).', 'model': "Mixture type: Gaussian (GMVAR), Student's-t (StMVAR), or mixed G-StMVAR (default GMVAR).", 'conditional': 'Conditional (True) or exact (False) log-likelihood (default True).', 'parametrization': 'Intercept or mean parametrization (default intercept).', 'structural_W': 'Optional d x d constraint matrix W for structural identification through conditional heteroskedasticity (NA=free, +/-=sign, 0=zero)· requires M>=2. None => reduced-form (recursive Cholesky).', 'ncalls': 'Number of GA estimation rounds (default 2 — TINY· production raises it to (M+1)^5).', 'ncores': 'CPU cores (default 1· use_parallel only when >1).', 'maxit': 'Maximum variable-metric optim iterations per round (default 100).', 'seed': 'MANDATORY seed (integer) — stochastic GA· seeded + reproducible seeds vector.', 'allow_nonconvergence': 'True to bypass the convergence gate (degenerate estimates· the IRF/FEVD will be UNRELIABLE· default False).'},
        'input_example': {'data': '<multiseries_handle>', 'p': 1, 'M': [1, 1], 'conditional': True, 'ncalls': 2, 'ncores': 1, 'maxit': 100, 'seed': 1, 'allow_nonconvergence': False},
    },
    'gmv_gfevd': {
        'fn': 'gmv_gfevd',
        'description': 'gmv_gfevd -- category 04-structural-shocks, method card #151.',
        'args': {'model': "Handle to a fitted 'gsmvar' model (from gmv_fit).", 'N': 'GFEVD horizon (positive integer, default 10).', 'n_iterations': 'MC iterations per initial value (default 50 — TINY).', 'n_initial_values': "Number of random initial values when initval_type='random' (default 50 — TINY).", 'initval_type': "Initial values of the GIRFs: all p-histories of the data ('data') or random draws from the stationary distribution ('random') (default data).", 'shock_size': 'Size/sign of the shocks· non-zero (default 1).', 'include_mixweights': 'GFEVD for the mixing weights as well (default False).', 'ncores': 'CPU cores (default 1).', 'seed': 'MANDATORY seed — simulation-based· seeded for reproducibility.'},
        'input_example': {'model': '<raw_handle>', 'N': 10, 'n_iterations': 50, 'n_initial_values': 50, 'shock_size': 1, 'include_mixweights': False, 'ncores': 1, 'seed': 1},
    },
    'gmv_girf': {
        'fn': 'gmv_girf',
        'description': 'gmv_girf -- category 04-structural-shocks, method card #151.',
        'args': {'model': "Handle to a fitted 'gsmvar' model (from gmv_fit).", 'which_shocks': 'Indices of the structural shocks in [1, d] (default 1).', 'N': 'GIRF horizon (positive integer, default 10).', 'n_iterations': 'MC iterations per initial value (default 50 — TINY).', 'n_initial_values': 'Number of initial values from the stationary distribution (default 50 — TINY).', 'shock_size': 'Size/sign of the shock· non-zero (default 1).', 'ci': 'Confidence levels of the bands in (0,1) (default [0.95, 0.8]).', 'include_mixweights': 'GIRF for the mixing weights as well (default False).', 'ncores': 'CPU cores (default 1).', 'seed': 'MANDATORY seed — simulation-based· seeded for reproducibility.'},
        'input_example': {'model': '<raw_handle>', 'which_shocks': [1, 1], 'N': 10, 'n_iterations': 50, 'n_initial_values': 50, 'shock_size': 1, 'include_mixweights': False, 'ncores': 1, 'seed': 1},
    },
    'gmv_linear_irf': {
        'fn': 'gmv_linear_irf',
        'description': 'gmv_linear_irf -- category 04-structural-shocks, method card #151.',
        'args': {'model': "Handle to a fitted 'gsmvar' model (structural W or reduced-form -> recursive Cholesky).", 'N': 'Linear-IRF horizon (positive integer, default 10).', 'regime': 'Regime 1..sum(M) on which the linear IRF is computed (default 1).', 'ci': 'Confidence level of the wild-bootstrap bands in (0,1)· only for linear-AR models (default None = no bands).', 'bootstrap_reps': 'Bootstrap replications when ci != None (default 100).', 'ncores': 'CPU cores (default 1).', 'seed': 'MANDATORY seed — stochastic bootstrap· seeded for reproducibility.'},
        'input_example': {'model': '<raw_handle>', 'N': 10, 'regime': 1, 'bootstrap_reps': 100, 'ncores': 1, 'seed': 1},
    },
    'lp_linear': {
        'fn': 'lp_linear',
        'description': 'lp_linear -- category 04-structural-shocks, method card #22.',
        'args': {'endog_data': 'Handle to a multivariate numeric DataFrame/ts (T x K, no NA).', 'lags_endog_lin': 'Endogenous lags (default 2).', 'trend': '0=none, 1=trend, 2=trend+quadratic (default 0).', 'shock_type': '0=1sd shock, 1=unit shock (default 1).', 'confint': 'CI multiplier (68%=1, 90%=1.65, 95%=1.96· default 1.96).', 'hor': 'IRF horizon (positive integer, default 10).'},
        'input_example': {'endog_data': '<df_handle>', 'lags_endog_lin': 2, 'trend': 0, 'shock_type': 1, 'confint': 1.96, 'hor': 10},
    },
    'lp_linear_iv': {
        'fn': 'lp_linear_iv',
        'description': 'lp_linear_iv -- category 04-structural-shocks, method card #22.',
        'args': {'endog_data': 'Handle to a multivariate numeric DataFrame/ts (T x K).', 'shock': 'Handle to an identified shock/instrument (single-column series, same rows).', 'lags_endog_lin': 'Endogenous lags (default 2).', 'trend': '0=none, 1=trend, 2=trend+quadratic (default 0).', 'confint': 'CI multiplier (default 1.96).', 'hor': 'IRF horizon (default 10).', 'cumul_mult': 'Cumulative multipliers (default False).', 'use_twosls': '2SLS (requires instrum) (default False).'},
        'input_example': {'endog_data': '<df_handle>', 'shock': '<series_handle>', 'lags_endog_lin': 2, 'trend': 0, 'confint': 1.96, 'hor': 10, 'cumul_mult': False, 'use_twosls': False},
    },
    'lp_nonlinear': {
        'fn': 'lp_nonlinear',
        'description': 'lp_nonlinear -- category 04-structural-shocks, method card #22.',
        'args': {'endog_data': 'Handle to a multivariate numeric DataFrame/ts (T x K).', 'switching': 'Handle to the state-separating variable (numeric, length = rows).', 'lags_endog_lin': 'Linear-part lags (default 2).', 'lags_endog_nl': 'Non-linear-part lags (default 2).', 'trend': '0=none, 1=trend, 2=trend+quadratic (default 0).', 'shock_type': '0=1sd shock, 1=unit shock (default 1).', 'confint': 'CI multiplier (default 1.96).', 'hor': 'IRF horizon (default 10).', 'use_logistic': 'Logistic transition (Auerbach-Gorodnichenko) (default True).', 'use_hp': 'HP-filter the switching variable (requires lambda) (default False).', 'lambda': 'HP lambda (e.g. 1600 quarterly)· required if use_hp=True.', 'gamma': 'Logistic steepness gamma (default 3).'},
        'input_example': {'endog_data': '<df_handle>', 'switching': '<series_handle>', 'lags_endog_lin': 2, 'lags_endog_nl': 2, 'trend': 0, 'shock_type': 1, 'confint': 1.96, 'hor': 10, 'use_logistic': True, 'use_hp': False, 'gamma': 3},
    },
    'lp_nonlinear_iv': {
        'fn': 'lp_nonlinear_iv',
        'description': 'lp_nonlinear_iv -- category 04-structural-shocks, method card #22.',
        'args': {'endog_data': 'Handle to a multivariate numeric DataFrame/ts (T x K).', 'shock': 'Handle to an identified shock/instrument (single-column series).', 'switching': 'Handle to the state-separating variable (numeric).', 'lags_endog_nl': 'Non-linear-part lags (default 2).', 'trend': '0=none, 1=trend, 2=trend+quadratic (default 0).', 'confint': 'CI multiplier (default 1.96).', 'hor': 'IRF horizon (default 10).', 'cumul_mult': 'Cumulative multipliers (default False).', 'use_logistic': 'Logistic transition (default True).', 'use_hp': 'HP-filter the switching variable (requires lambda) (default False).', 'lambda': 'HP lambda· required if use_hp=True.', 'gamma': 'Logistic steepness gamma (default 3).'},
        'input_example': {'endog_data': '<df_handle>', 'shock': '<series_handle>', 'switching': '<series_handle>', 'lags_endog_nl': 2, 'trend': 0, 'confint': 1.96, 'hor': 10, 'cumul_mult': False, 'use_logistic': True, 'use_hp': False, 'gamma': 3},
    },
    'lp_panel': {
        'fn': 'lp_panel',
        'description': 'lp_panel -- category 04-structural-shocks, method card #22.',
        'args': {'data_set': 'Handle to a panel DataFrame (1st column cross-section, 2nd time, >=3 columns).', 'endog_data': 'NAME of the dependent-variable column (not the data).', 'shock': 'NAME of the shock column (not the data).', 'hor': 'IRF horizon (default 10).', 'confint': 'CI multiplier (default 1.96).', 'panel_model': 'panel estimator (default within = fixed effects).', 'panel_effect': 'panel effect dimension (default individual).', 'iv_reg': 'IV/GMM (requires instrum) (default False).', 'cumul_mult': 'Cumulative multipliers (default True).', 'diff_shock': 'First-difference the shock (default True).'},
        'input_example': {'data_set': '<df_handle>', 'endog_data': '...', 'shock': '...', 'hor': 10, 'confint': 1.96, 'panel_model': 'within', 'panel_effect': 'individual', 'iv_reg': False, 'cumul_mult': True, 'diff_shock': True},
    },
    'lp_panel_nl': {
        'fn': 'lp_panel_nl',
        'description': 'lp_panel_nl -- category 04-structural-shocks, method card #22.',
        'args': {'data_set': 'Handle to a panel DataFrame (cross-section, time, >=3 columns).', 'endog_data': 'NAME of the dependent-variable column.', 'shock': 'NAME of the shock column.', 'switching': 'NAME of the regime-variable column.', 'hor': 'IRF horizon (default 10).', 'confint': 'CI multiplier (default 1.96).', 'panel_model': 'panel estimator (default within).', 'panel_effect': 'panel effect dimension (default individual).', 'cumul_mult': 'Cumulative multipliers (default True).', 'diff_shock': 'First-difference the shock (default True).', 'use_logistic': 'Logistic transition (default True).', 'use_hp': 'HP-filter the switching variable (requires lambda) (default False).', 'lambda': 'HP lambda· required if use_hp=True.', 'gamma': 'Logistic steepness gamma (default 3).'},
        'input_example': {'data_set': '<df_handle>', 'endog_data': '...', 'shock': '...', 'switching': '...', 'hor': 10, 'confint': 1.96, 'panel_model': 'within', 'panel_effect': 'individual', 'cumul_mult': True, 'diff_shock': True, 'use_logistic': True, 'use_hp': False, 'gamma': 3},
    },
    'sst_fit': {
        'fn': 'sst_fit',
        'description': 'sst_fit -- category 04-structural-shocks, method card #150.',
        'args': {'data': 'Handle to a multivariate series (matrix/ts, T x d, d>=2, no NA/Inf).', 'p': 'VAR lag order (positive integer, default 1).', 'M': 'Number of regimes (positive integer, default 2).', 'weight_function': 'Transition-weight function (default relative_dens — Gaussian ONLY).', 'cond_dist': 'Conditional error distribution (default Gaussian).', 'parametrization': 'Intercept or mean parametrization (default intercept).', 'weightfun_pars': 'Weight-function parameters· [switch_var, lag] for logistic/exponential/threshold (mandatory when weight_function != relative_dens).', 'nrounds': 'Number of GA estimation rounds (default 2 — TINY· production raises it).', 'ngen': 'Genetic-algorithm generations per round (default 30 — TINY).', 'maxit': 'Maximum variable-metric optim iterations (default 300).', 'seed': 'MANDATORY seed (integer) — stochastic GA· seeded + seeds vector.'},
        'input_example': {'data': '<multiseries_handle>', 'p': 1, 'M': 2, 'nrounds': 2, 'ngen': 30, 'maxit': 300, 'seed': 1},
    },
    'sst_gfevd': {
        'fn': 'sst_gfevd',
        'description': 'sst_gfevd -- category 04-structural-shocks, method card #150.',
        'args': {'model': "Handle to a fitted 'stvar' model (from sst_fit).", 'N': 'GFEVD horizon (positive integer, default 16).', 'shock_size': 'Size/sign of the shocks (default 1).', 'initval_type': 'Type of initial values for the GIRFs (default random).', 'n_iterations': 'MC iterations per initial value (default 50 — TINY).', 'n_initial_values': 'Number of initial values (random/fixed) (default 50 — TINY).', 'init_regime': 'Regime of the initial values 1..M (default 1).', 'burn_in': 'Simulation burn-in (default 200).', 'seed': 'MANDATORY seed — simulation-based· seeded for reproducibility.'},
        'input_example': {'model': '<raw_handle>', 'N': 16, 'shock_size': 1, 'n_iterations': 50, 'n_initial_values': 50, 'init_regime': 1, 'burn_in': 200, 'seed': 1},
    },
    'sst_girf': {
        'fn': 'sst_girf',
        'description': 'sst_girf -- category 04-structural-shocks, method card #150.',
        'args': {'model': "Handle to a fitted 'stvar' model (from sst_fit).", 'which_shocks': 'Indices of the structural shocks in [1, d] (default 1).', 'N': 'GIRF horizon (positive integer, default 16).', 'shock_size': 'Size/sign of the shock (default 1).', 'n_iterations': 'MC iterations per initial value (default 50 — TINY).', 'n_initial_values': 'Number of initial values from init_regime (default 50 — TINY).', 'init_regime': 'Regime generating the initial values 1..M (default 1).', 'ci': 'Confidence levels of the bands (default [0.95, 0.8]).', 'burn_in': 'Simulation burn-in (default 200).', 'seed': 'MANDATORY seed — simulation-based· seeded for reproducibility.'},
        'input_example': {'model': '<raw_handle>', 'N': 16, 'shock_size': 1, 'n_iterations': 50, 'n_initial_values': 50, 'init_regime': 1, 'burn_in': 200, 'seed': 1},
    },
    'sst_linear_irf': {
        'fn': 'sst_linear_irf',
        'description': 'sst_linear_irf -- category 04-structural-shocks, method card #150.',
        'args': {'model': "Handle to a fitted 'stvar' model (reduced-form -> recursive ID).", 'N': 'Linear-IRF horizon (positive integer, default 16).', 'regime': 'Regime 1..M on which the linear IRF is computed (default 1).', 'ci': 'Confidence level of the wild-bootstrap bands in (0,1)· only for linear-AR models (default None = no bands).', 'bootstrap_reps': 'Bootstrap replications when ci != None (default 100).', 'seed': 'Seed for the ci bootstrap (default None· deterministic when ci=None).'},
        'input_example': {'model': '<raw_handle>', 'N': 16, 'regime': 1, 'bootstrap_reps': 100},
    },
    'svar_cf': {
        'fn': 'svar_cf',
        'description': 'svar_cf -- category 04-structural-shocks, method card #20.',
        'args': {'x': "Handle to an identified 'svars' (counterfactual).", 'series': 'Variable index 1..K (default 1).', 'transition': 'Transition-period share in [0,1) (default 0).'},
        'input_example': {'x': '<raw_handle>', 'series': 1, 'transition': 0},
    },
    'svar_fevd': {
        'fn': 'svar_fevd',
        'description': 'svar_fevd -- category 04-structural-shocks, method card #20.',
        'args': {'x': "Handle to an identified 'svars' (from svar_id_*).", 'n_ahead': 'FEVD horizon (positive integer, default 10).'},
        'input_example': {'x': '<raw_handle>', 'n_ahead': 10},
    },
    'svar_hd': {
        'fn': 'svar_hd',
        'description': 'svar_hd -- category 04-structural-shocks, method card #20.',
        'args': {'x': "Handle to an identified 'svars' (historical decomposition).", 'series': 'Variable index 1..K (default 1).', 'transition': 'Transition-period share in [0,1) (default 0).'},
        'input_example': {'x': '<raw_handle>', 'series': 1, 'transition': 0},
    },
    'svar_id_cholesky': {
        'fn': 'svar_id_cholesky',
        'description': 'svar_id_cholesky -- category 04-structural-shocks, method card #20.',
        'args': {'model': "Handle to a reduced-form 'varest' (recursive/Cholesky ID)."},
        'input_example': {'model': '<raw_handle>'},
    },
    'svar_id_volatility_change': {
        'fn': 'svar_id_volatility_change',
        'description': 'svar_id_volatility_change -- category 04-structural-shocks, method card #20.',
        'args': {'model': "Handle to a reduced-form 'varest' (changes-in-volatility, Rigobon).", 'SB': 'Structural break: number of pre-break observations (integer).', 'max_iter': 'Maximum EM iterations (default 50).', 'crit': 'Convergence criterion (default 0.001).'},
        'input_example': {'model': '<raw_handle>', 'SB': 1, 'max_iter': 50, 'crit': 0.001},
    },
    'svar_id_distance_covariance': {
        'fn': 'svar_id_distance_covariance',
        'description': 'svar_id_distance_covariance -- category 04-structural-shocks, method card #20.',
        'args': {'model': "Handle to a reduced-form 'varest' (distance-covariance ID).", 'PIT': 'Probability integral transform of the residuals (default False).', 'seed': 'Reproducibility seed (stochastic steadyICA, default 2025).'},
        'input_example': {'model': '<raw_handle>', 'PIT': False, 'seed': 2025},
    },
    'svar_id_non_gaussian_ml': {
        'fn': 'svar_id_non_gaussian_ml',
        'description': 'svar_id_non_gaussian_ml -- category 04-structural-shocks, method card #20.',
        'args': {'model': "Handle to a reduced-form 'varest' (non-Gaussian ML, Lanne et al.).", 'stage3': 'Stage-3 GLS refinement (default False).', 'seed': 'Reproducibility seed (default 2025).'},
        'input_example': {'model': '<raw_handle>', 'stage3': False, 'seed': 2025},
    },
    'svar_irf': {
        'fn': 'svar_irf',
        'description': 'svar_irf -- category 04-structural-shocks, method card #20.',
        'args': {'x': "Handle to an identified 'svars' (from svar_id_*).", 'n_ahead': 'IRF horizon (positive integer, default 10).'},
        'input_example': {'x': '<raw_handle>', 'n_ahead': 10},
    },
    'svar_mb_boot': {
        'fn': 'svar_mb_boot',
        'description': 'svar_mb_boot -- category 04-structural-shocks, method card #20.',
        'args': {'x': "Handle to an identified 'svars' (moving-block bootstrap, Brüggemann et al.).", 'n_ahead': 'IRF horizon (default 20).', 'nboot': 'Number of bootstrap draws (default 500).', 'b_length': 'Block length (default 15).', 'design': 'Bootstrap design (default recursive).', 'lower_q': 'Lower quantile of the band (default 0.16).', 'upper_q': 'Upper quantile of the band (default 0.84).'},
        'input_example': {'x': '<raw_handle>', 'n_ahead': 20, 'nboot': 500, 'b_length': 15, 'lower_q': 0.16, 'upper_q': 0.84},
    },
    'svar_wild_boot': {
        'fn': 'svar_wild_boot',
        'description': 'svar_wild_boot -- category 04-structural-shocks, method card #20.',
        'args': {'x': "Handle to an identified 'svars' (wild bootstrap, Gonçalves-Kilian).", 'n_ahead': 'IRF horizon (default 20).', 'nboot': 'Number of bootstrap draws (default 500).', 'design': 'Bootstrap design (default fixed).', 'distr': 'Distribution of the wild multiplier (default rademacher).', 'lower_q': 'Lower quantile of the band (default 0.16).', 'upper_q': 'Upper quantile of the band (default 0.84).'},
        'input_example': {'x': '<raw_handle>', 'n_ahead': 20, 'nboot': 500, 'lower_q': 0.16, 'upper_q': 0.84},
    },
    'vr_bq': {
        'fn': 'vr_bq',
        'description': 'vr_bq -- category 04-structural-shocks, method card #19.',
        'args': {'model': "Handle to a reduced-form 'varest' (BQ long-run restrictions)."},
        'input_example': {'model': '<raw_handle>'},
    },
    'vr_fevd': {
        'fn': 'vr_fevd',
        'description': 'vr_fevd -- category 04-structural-shocks, method card #19.',
        'args': {'model': "Handle to a 'varest'/'svarest'/'vec2var'.", 'n_ahead': 'FEVD horizon (positive integer, default 10).'},
        'input_example': {'model': '<raw_handle>', 'n_ahead': 10},
    },
    'vr_irf': {
        'fn': 'vr_irf',
        'description': 'vr_irf -- category 04-structural-shocks, method card #19.',
        'args': {'model': "Handle to a 'varest'/'svarest'/'vec2var' (reduced or structural).", 'impulse': 'Name of the shock variable (default: all).', 'response': 'Name of the response variable (default: all).', 'n_ahead': 'IRF horizon (positive integer, default 10).', 'ortho': 'Orthogonalised (Cholesky) IRF (default True).', 'cumulative': 'Cumulative responses (default False).', 'boot': 'Bootstrap CI bands (default True).', 'ci': 'Confidence level in (0,1) (default 0.95).', 'runs': 'Bootstrap runs (positive integer, default 100).'},
        'input_example': {'model': '<raw_handle>', 'n_ahead': 10, 'ortho': True, 'cumulative': False, 'boot': True, 'ci': 0.95, 'runs': 100},
    },
    'vr_svar': {
        'fn': 'vr_svar',
        'description': 'vr_svar -- category 04-structural-shocks, method card #19.',
        'args': {'model': "Handle to a reduced-form 'varest' (from vr_fit, button #11).", 'estmethod': 'Estimation method (default scoring).', 'Amat': 'Handle to a K x K A-model matrix (NA = free parameter).', 'Bmat': 'Handle to a K x K B-model matrix (NA = free parameter).', 'lrtest': 'LR test overidentifying restrictions (default True).'},
        'input_example': {'model': '<raw_handle>', 'lrtest': True},
    },
    'sgn_rwz_reject': {
        'fn': 'sgn_rwz_reject',
        'description': 'sgn_rwz_reject -- category 04-structural-shocks, method card #21.',
        'args': {'Y': 'Handle to a multivariate ts (>=2 columns, no NA).', 'constrained': 'Signed sign-restriction indices (Rubio-Ramirez/Waggoner/Zha).', 'nlags': 'VAR lags (default 4).', 'draws': 'MCMC draws (default 200).', 'subdraws': 'Sub-draws per draw (default 200).', 'nkeep': 'Accepted draws (default 1000).', 'KMIN': 'First horizon at which they are imposed (default 1).', 'KMAX': 'Last horizon at which they are imposed (default 4).', 'steps': 'IRF horizon (default 24).', 'type': 'Central measure of the posterior bands (default median).'},
        'input_example': {'Y': '<multiseries_handle>', 'constrained': [4, -3, -2, -5], 'nlags': 4, 'draws': 200, 'subdraws': 200, 'nkeep': 1000, 'KMIN': 1, 'KMAX': 4, 'steps': 24},
    },
    'sgn_uhlig_penalty': {
        'fn': 'sgn_uhlig_penalty',
        'description': 'sgn_uhlig_penalty -- category 04-structural-shocks, method card #21.',
        'args': {'Y': 'Handle to a multivariate ts (>=2 columns, no NA).', 'constrained': 'Signed sign-restriction indices (1st = shock of interest).', 'nlags': 'VAR lags (default 4).', 'draws': 'MCMC draws (default 1000).', 'subdraws': 'Sub-draws per draw (default 1000).', 'nkeep': 'Accepted draws (default 1000).', 'KMIN': 'First horizon at which they are imposed (default 1).', 'KMAX': 'Last horizon at which they are imposed (default 4).', 'steps': 'IRF horizon (default 24).', 'penalty': 'Penalty function weight (>=0, default 100).', 'type': 'Central measure of the posterior bands (default median).'},
        'input_example': {'Y': '<multiseries_handle>', 'constrained': [4, -3, -2, -5], 'nlags': 4, 'draws': 1000, 'subdraws': 1000, 'nkeep': 1000, 'KMIN': 1, 'KMAX': 4, 'steps': 24, 'penalty': 100},
    },
    'sgn_uhlig_reject': {
        'fn': 'sgn_uhlig_reject',
        'description': 'sgn_uhlig_reject -- category 04-structural-shocks, method card #21.',
        'args': {'Y': 'Handle to a multivariate ts (>=2 columns, no NA).', 'constrained': 'Signed sign-restriction indices (1st = shock of interest, e.g. [4,-3,-2,-5]).', 'nlags': 'VAR lags (default 4).', 'draws': 'MCMC draws (default 200).', 'subdraws': 'Sub-draws per draw (default 200).', 'nkeep': 'Accepted draws to keep (default 1000).', 'KMIN': 'First horizon at which the restrictions are imposed (default 1).', 'KMAX': 'Last horizon at which they are imposed (default 4).', 'steps': 'IRF horizon (default 24).', 'type': 'Central measure of the posterior bands (default median).'},
        'input_example': {'Y': '<multiseries_handle>', 'constrained': [4, -3, -2, -5], 'nlags': 4, 'draws': 200, 'subdraws': 200, 'nkeep': 1000, 'KMIN': 1, 'KMAX': 4, 'steps': 24},
    },
    'vtt_arch': {
        'fn': 'vtt_arch',
        'description': 'vtt_arch -- category 04-structural-shocks, method card #153.',
        'args': {'fit': "Handle to a fitted VAR ('VARfit'/'varest').", 'h': 'Order h of the ARCH alternative (positive integer· default 2).', 'B': 'Number of bootstrap simulations (positive integer· default 499).', 'seed': 'MANDATORY seed (seeded before the bootstrap· cache key· without it uncacheable).', 'ET': 'Eklund-Terasvirta CCC-ARCH test (default True). The CA (Catani-Ahlgren) test ALWAYS runs.', 'MARCH': 'Multivariate LM ARCH test (Lutkepohl 2006, sect. 16.5· default True).', 'dist': 'Bootstrap error distribution (default norm· skT=skew-t with skT.param).', 'skT_param': "Skew-t parameters [xi,Omega,alpha,nu] when dist='skT' (default [0,1,0,5]).", 'alpha': 'Decision significance level ∈ (0,1) (default 0.05).'},
        'input_example': {'fit': '<raw_handle>', 'h': 2, 'B': 499, 'seed': 1, 'ET': True, 'MARCH': True, 'alpha': 0.05},
    },
    'vtt_fit': {
        'fn': 'vtt_fit',
        'description': 'vtt_fit -- category 04-structural-shocks, method card #153.',
        'args': {'y': 'Handle to a multivariate series (series/panel/matrix, T x K) — the data of the reduced-form VAR.', 'p': 'VAR lag order (positive integer· default 1).', 'const': 'Constant term (default True).', 'trend': 'Linear trend (default False).', 'exogen': 'Optional exogenous regressors (matrix, nrow==the row count of y).'},
        'input_example': {'y': '<multiseries_handle>', 'p': 1, 'const': True, 'trend': False},
    },
    'vtt_portmanteau': {
        'fn': 'vtt_portmanteau',
        'description': 'vtt_portmanteau -- category 04-structural-shocks, method card #153.',
        'args': {'fit': "Handle to a fitted VAR: 'VARfit' (from vtt_fit) or 'varest' (from vr_fit, button #11).", 'h': 'Order h of the alternative VAR(h) for the errors (positive integer· default 4).', 'HCtype': 'Character-vector subset of {LM,HC0,HC1,HC2,HC3}: LM=homoskedastic, HC*=heteroskedasticity-consistent (default all).', 'univariate': "Additional per-equation (univariate) test (default False· 'only' is NOT supported).", 'alpha': 'Decision significance level ∈ (0,1) (default 0.05).'},
        'input_example': {'fit': '<raw_handle>', 'h': 4, 'univariate': False, 'alpha': 0.05},
    },
    'vtt_wildboot': {
        'fn': 'vtt_wildboot',
        'description': 'vtt_wildboot -- category 04-structural-shocks, method card #153.',
        'args': {'fit': "Handle to a fitted VAR ('VARfit'/'varest').", 'h': 'Order h of the AC alternative (positive integer· default 4).', 'HCtype': 'Character-vector subset of {LM,HC0,HC1,HC2,HC3} (default all).', 'WBtype': 'Wild-bootstrap scheme (Algorithm 1/2 Ahlgren-Catani· default recursive).', 'B': 'Number of bootstrap simulations (positive integer· default 199).', 'WBdist': 'Distribution of the wild-bootstrap weights (default rademacher).', 'univariate': 'Additional per-equation test (default False).', 'seed': 'MANDATORY seed (seeded before the bootstrap· cache key).', 'alpha': 'Decision significance level ∈ (0,1) (default 0.05).'},
        'input_example': {'fit': '<raw_handle>', 'h': 4, 'B': 199, 'univariate': False, 'seed': 1, 'alpha': 0.05},
    },
    'ss_proxy_svar': {
        'fn': 'ss_proxy_svar',
        'description': 'ss_proxy_svar -- category 04-structural-shocks, method card #424.',
        'args': {'y': 'Endogenous variables.', 'instrument': 'External instrument for the shock.', 'target': 'Variable the shock is normalised on.', 'lags': 'VAR lag order.', 'horizons': 'Impulse-response horizon.', 'nboot': 'Number of bootstrap replications.', 'seed': 'Seed for the random number generator; required for reproducibility.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'y': '<multiseries_handle>', 'instrument': '<series_handle>', 'target': '...', 'lags': 4, 'horizons': 20, 'nboot': 999, 'seed': 1, 'conf_level': 0.95},
    },
    'ss_instrument_strength': {
        'fn': 'ss_instrument_strength',
        'description': 'ss_instrument_strength -- category 04-structural-shocks, method card #424.',
        'args': {'fit': 'Handle to a fitted proxy SVAR.'},
        'input_example': {'fit': '<raw_handle>'},
    },
    'ss_nongaussian_svar': {
        'fn': 'ss_nongaussian_svar',
        'description': 'ss_nongaussian_svar -- category 04-structural-shocks, method card #425.',
        'args': {'y': 'Endogenous variables.', 'lags': 'VAR lag order.', 'moments': 'Moments used for identification.', 'horizons': 'Impulse-response horizon.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'y': '<multiseries_handle>', 'lags': 4, 'moments': 'third_and_fourth', 'horizons': 20, 'conf_level': 0.95},
    },
    'ss_nongaussianity_diagnostics': {
        'fn': 'ss_nongaussianity_diagnostics',
        'description': 'ss_nongaussianity_diagnostics -- category 04-structural-shocks, method card #425.',
        'args': {'y': 'Endogenous variables.', 'lags': 'VAR lag order.', 'alpha': 'Significance level.'},
        'input_example': {'y': '<multiseries_handle>', 'lags': 4, 'alpha': 0.05},
    },
    'ss_irf_bands': {
        'fn': 'ss_irf_bands',
        'description': 'ss_irf_bands -- category 04-structural-shocks, method card #426.',
        'args': {'fit': 'Handle to a fitted VAR or SVAR.', 'horizons': 'Impulse-response horizon.', 'method': 'Bootstrap scheme.', 'nboot': 'Number of bootstrap replications.', 'joint': 'Report joint rather than pointwise bands.', 'seed': 'Seed for the random number generator; required for reproducibility.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'fit': '<raw_handle>', 'horizons': 20, 'method': 'kilian', 'nboot': 999, 'joint': False, 'seed': 1, 'conf_level': 0.95},
    },
    'ss_lag_augmented_lp': {
        'fn': 'ss_lag_augmented_lp',
        'description': 'ss_lag_augmented_lp -- category 04-structural-shocks, method card #427.',
        'args': {'y': 'Response variable.', 'shock': 'Shock or impulse variable.', 'controls': 'Control columns.', 'horizons': 'Maximum horizon.', 'lags': 'Lags included.', 'cov_type': 'Covariance estimator.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'y': '<series_handle>', 'shock': '<series_handle>', 'horizons': 20, 'lags': 4, 'cov_type': 'hac', 'conf_level': 0.95},
    },
    'ss_ms_var': {
        'fn': 'ss_ms_var',
        'description': 'ss_ms_var -- category 04-structural-shocks, method card #428.',
        'args': {'y': 'Endogenous variables.', 'k_regimes': 'Number of regimes.', 'lags': 'Lag order.', 'switching_variance': 'Allow the covariance to switch.', 'switching_coefficients': 'Allow the coefficients to switch.', 'n_starts': 'Random restarts of the optimiser.', 'seed': 'Seed for the random number generator.'},
        'input_example': {'y': '<multiseries_handle>', 'k_regimes': 2, 'lags': 1, 'switching_variance': True, 'switching_coefficients': True, 'n_starts': 10},
    },
    'ss_max_share': {
        'fn': 'ss_max_share',
        'description': 'ss_max_share -- category 04-structural-shocks, method card #429.',
        'args': {'y': 'Endogenous variables.', 'target': 'Variable whose variance is maximised.', 'lags': 'VAR lag order.', 'horizon_range': 'Horizons the share is maximised over.', 'frequency_band': 'Frequency band for spectral identification.', 'horizons': 'Impulse-response horizon.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'y': '<multiseries_handle>', 'target': '...', 'lags': 4, 'horizon_range': [0, 40], 'horizons': 40, 'conf_level': 0.95},
    },
    'ss_combined_restrictions': {
        'fn': 'ss_combined_restrictions',
        'description': 'ss_combined_restrictions -- category 04-structural-shocks, method card #430.',
        'args': {'y': 'Endogenous variables.', 'short_run': 'Short-run restriction pattern.', 'long_run': 'Long-run restriction pattern.', 'lags': 'VAR lag order.', 'horizons': 'Impulse-response horizon.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'y': '<multiseries_handle>', 'lags': 4, 'horizons': 40, 'conf_level': 0.95},
    },
    'ss_panel_lp': {
        'fn': 'ss_panel_lp',
        'description': 'ss_panel_lp -- category 04-structural-shocks, method card #431.',
        'args': {'data': 'Panel data.', 'y': 'Response column.', 'shock': 'Shock column.', 'unit': 'Unit identifier.', 'time': 'Time identifier.', 'controls': 'Control columns.', 'horizons': 'Maximum horizon.', 'lags': 'Lags included.', 'cov_type': 'Covariance estimator.', 'group': 'Column defining groups for separate responses.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'data': '<df_handle>', 'y': '...', 'shock': '...', 'unit': '...', 'time': '...', 'horizons': 20, 'lags': 4, 'cov_type': 'driscoll_kraay', 'conf_level': 0.95},
    },
}
