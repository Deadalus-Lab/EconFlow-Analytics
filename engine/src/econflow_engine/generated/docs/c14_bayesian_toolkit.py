# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 14-bayesian-toolkit: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'bviz_mcmc_areas_data': {
        'fn': 'bviz_mcmc_areas_data',
        'description': 'bviz_mcmc_areas_data -- category 14-bayesian-toolkit, method card #73.',
        'args': {'x': 'Handle to draws· density areas grid· WITHOUT NA.', 'pars': 'Parameter names AS a character vector (empty = all).', 'prob': 'Inner interval probability, strictly (0,1) (default 0.5).', 'prob_outer': 'Outer probability (default 1 = full density, <=1).', 'point_est': 'Point estimate (default median).'},
        'input_example': {'x': '<raw_handle>', 'prob': 0.5, 'prob_outer': 1},
    },
    'bviz_mcmc_intervals_data': {
        'fn': 'bviz_mcmc_intervals_data',
        'description': 'bviz_mcmc_intervals_data -- category 14-bayesian-toolkit, method card #73.',
        'args': {'x': 'Handle to draws (3D array / matrix / DataFrame / list of chain matrices)· WITHOUT NA.', 'pars': 'Parameter names AS a character vector (empty = all).', 'prob': 'Inner interval probability, strictly (0,1) (default 0.5· prob<=prob_outer).', 'prob_outer': 'Outer interval probability (default 0.9, <=1).', 'point_est': 'Point estimate (default median).'},
        'input_example': {'x': '<raw_handle>', 'prob': 0.5, 'prob_outer': 0.9},
    },
    'bviz_mcmc_neff_data': {
        'fn': 'bviz_mcmc_neff_data',
        'description': 'bviz_mcmc_neff_data -- category 14-bayesian-toolkit, method card #73.',
        'args': {'ratio': 'Handle to a PRECOMPUTED numeric N_eff/N ratio vector (ess-derived)· WITHOUT NA, >0.'},
        'input_example': {'ratio': '<raw_handle>'},
    },
    'bviz_mcmc_rhat_data': {
        'fn': 'bviz_mcmc_rhat_data',
        'description': 'bviz_mcmc_rhat_data -- category 14-bayesian-toolkit, method card #73.',
        'args': {'rhat': 'Handle to a PRECOMPUTED numeric R-hat vector (the convergence-diagnostic routine)· NOT a fitted model· WITHOUT NA, >0.'},
        'input_example': {'rhat': '<raw_handle>'},
    },
    'bviz_mcmc_trace_data': {
        'fn': 'bviz_mcmc_trace_data',
        'description': 'bviz_mcmc_trace_data -- category 14-bayesian-toolkit, method card #73.',
        'args': {'x': 'Handle to draws· trace value per iteration/chain· WITHOUT NA.', 'pars': 'Parameter names AS a character vector (empty = all).'},
        'input_example': {'x': '<raw_handle>'},
    },
    'bviz_ppc_intervals_data': {
        'fn': 'bviz_ppc_intervals_data',
        'description': 'bviz_ppc_intervals_data -- category 14-bayesian-toolkit, method card #73.',
        'args': {'y': 'Handle to an observed numeric VECTOR y.', 'yrep': 'Handle to a posterior-predictive MATRIX yrep (draws x obs)· ncol==length(y).', 'x': 'Handle to an optional x-axis (length==length(y)).', 'group': 'Handle to an optional group per observation (length==length(y)).', 'prob': 'Inner interval probability (default 0.5).', 'prob_outer': 'Outer interval probability (default 0.9).'},
        'input_example': {'y': '<raw_handle>', 'yrep': '<matrix_handle>', 'prob': 0.5, 'prob_outer': 0.9},
    },
    'bviz_ppc_ribbon_data': {
        'fn': 'bviz_ppc_ribbon_data',
        'description': 'bviz_ppc_ribbon_data -- category 14-bayesian-toolkit, method card #73.',
        'args': {'y': 'Handle to an observed numeric VECTOR y.', 'yrep': 'Handle to a posterior-predictive MATRIX yrep (draws x obs)· ncol==length(y).', 'x': 'Handle to an optional x-axis (length==length(y)).', 'group': 'Handle to an optional group (length==length(y)).', 'prob': 'Inner ribbon probability (default 0.5).', 'prob_outer': 'Outer ribbon probability (default 0.9).'},
        'input_example': {'y': '<raw_handle>', 'yrep': '<matrix_handle>', 'prob': 0.5, 'prob_outer': 0.9},
    },
    'bviz_ppc_stat_data': {
        'fn': 'bviz_ppc_stat_data',
        'description': 'bviz_ppc_stat_data -- category 14-bayesian-toolkit, method card #73.',
        'args': {'y': 'Handle to an observed numeric VECTOR y.', 'yrep': 'Handle to a posterior-predictive MATRIX yrep (draws x obs)· ncol==length(y).', 'stat': "Statistic name AS A STRING (e.g. 'mean','sd','median')· of length 1.", 'group': 'Handle to an optional group per observation (length==length(y)).'},
        'input_example': {'y': '<raw_handle>', 'yrep': '<matrix_handle>', 'stat': '...'},
    },
    'breg_fit': {
        'fn': 'breg_fit',
        'description': 'breg_fit -- category 14-bayesian-toolkit, method card #69.',
        'args': {'formula': "Regression formula AS A STRING (ACE-sanitized), e.g. 'y ~ x1 + x2'.", 'data': 'Handle to a DataFrame with columns matching the formula (WITHOUT NA in the model columns).', 'family': 'Family AS A STRING (default gaussian· Gamma uses the LOG link, not INVERSE).', 'prior': "Handle to a 'brmsprior' (from breg_set_prior)· optional.", 'seed': 'REQUIRED seed (Stan RNG· default RANDOM).', 'chains': 'Number of chains (default 2).', 'iter': 'Iterations per chain (default 1000, warmup=iter/2).', 'rhat_threshold': 'Threshold of the rank-normalized R-hat (default 1.01).', 'neff_ratio_threshold': 'Minimum neff_ratio (default 0.1).', 'allow_nonconvergence': 'True -> converged=False instead of stop on non-convergence.'},
        'input_example': {'formula': 'y ~ x', 'data': '<df_handle>', 'seed': 1, 'chains': 2, 'iter': 1000, 'rhat_threshold': 1.01, 'neff_ratio_threshold': 0.1, 'allow_nonconvergence': False},
    },
    'breg_make_formula': {
        'fn': 'breg_make_formula',
        'description': 'breg_make_formula -- category 14-bayesian-toolkit, method card #69.',
        'args': {'formula': "Regression formula AS A STRING (e.g. 'y ~ x1 + x2') -> brmsformula (ACE-sanitized)."},
        'input_example': {'formula': 'y ~ x'},
    },
    'breg_set_prior': {
        'fn': 'breg_set_prior',
        'description': 'breg_set_prior -- category 14-bayesian-toolkit, method card #69.',
        'args': {'prior': "Stan prior distribution AS A STRING (e.g. 'normal(0, 5)')· it is parsed by Stan and never evaluated as code here.", 'class': "Prior class (e.g. 'b' coefficients, 'Intercept', 'sigma'· default 'b')."},
        'input_example': {'prior': '...', 'class': 'b'},
    },
    'bsts_components': {
        'fn': 'bsts_components',
        'description': 'bsts_components -- category 14-bayesian-toolkit, method card #204.',
        'args': {'object': 'Handle to a fitted BSTS model (from bsts_fit).', 'burn': 'Burn-in draws (default None = SuggestBurn(0.1)).', 'quantile_lower': 'Lower quantile per component (default 0.025).', 'quantile_upper': 'Upper quantile per component (default 0.975).'},
        'input_example': {'object': '<raw_handle>', 'quantile_lower': 0.025, 'quantile_upper': 0.975},
    },
    'bsts_fit': {
        'fn': 'bsts_fit',
        'description': 'bsts_fit -- category 14-bayesian-toolkit, method card #204.',
        'args': {'y': 'Handle to a response ts (pure structural mode)· give ONE of y or formula+data.', 'formula': "Regression formula 'y ~ x1 + x2' (spike-and-slab mode)· requires data.", 'data': 'Handle to a DataFrame with response + regressors (regression mode).', 'family': 'Observation family (default gaussian· student = heavy tails).', 'local_linear_trend': 'AddLocalLinearTrend (default True)· mutually exclusive with semilocal.', 'semilocal_linear_trend': 'AddSemilocalLinearTrend (mean-reverting slope· better at long horizons).', 'seasonal_nseasons': 'AddSeasonal nseasons (0 = off· otherwise >=2, e.g. 12 monthly).', 'season_duration': 'Duration of each season in steps (default 1).', 'ar_lags': 'AddAr lags (0 = off· otherwise >=1).', 'niter': 'Number of MCMC iterations (default 1000).', 'burn': 'Burn-in draws to discard (default None = SuggestBurn(0.1)).', 'expected_model_size': 'Prior expected number of regressors (spike-and-slab)· ONLY in regression mode.', 'seed': 'REQUIRED seed (MCMC determinism· seeded + BSTS C++ RNG).'},
        'input_example': {'local_linear_trend': True, 'semilocal_linear_trend': False, 'seasonal_nseasons': 0, 'season_duration': 1, 'ar_lags': 0, 'niter': 1000, 'seed': 1},
    },
    'bsts_predict': {
        'fn': 'bsts_predict',
        'description': 'bsts_predict -- category 14-bayesian-toolkit, method card #204.',
        'args': {'object': 'Handle to a fitted BSTS model (from bsts_fit).', 'horizon': 'Forecast horizon (>=1· default 12).', 'newdata': 'Handle to future regressors (REQUIRED in regression models· nrow==horizon).', 'quantile_lower': 'Lower quantile of the forecast band (default 0.025).', 'quantile_upper': 'Upper quantile of the forecast band (default 0.975).', 'burn': 'Burn-in draws (default None = SuggestBurn(0.1)).', 'seed': 'REQUIRED seed (posterior sampling determinism).'},
        'input_example': {'object': '<raw_handle>', 'horizon': 12, 'quantile_lower': 0.025, 'quantile_upper': 0.975, 'seed': 1},
    },
    'mcmc_autocorr': {
        'fn': 'mcmc_autocorr',
        'description': 'mcmc_autocorr -- category 14-bayesian-toolkit, method card #72.',
        'args': {'chains': 'Handle to a list of per-chain matrices· autocorrelation per lag (default lags 0/1/5/10/50, all < niter).'},
        'input_example': {'chains': '<raw_handle>'},
    },
    'mcmc_diagnostics': {
        'fn': 'mcmc_diagnostics',
        'description': 'mcmc_diagnostics -- category 14-bayesian-toolkit, method card #72.',
        'args': {'chains': 'Handle to a list of per-chain numeric matrices (iter x var)· >=2 chains, niter>=10.', 'confidence': 'Gelman-Rubin confidence level, strictly (0,1) (default 0.95).', 'prob': 'HPD credible-interval probability, strictly (0,1) (default 0.95).'},
        'input_example': {'chains': '<raw_handle>', 'confidence': 0.95, 'prob': 0.95},
    },
    'mcmc_effective_size': {
        'fn': 'mcmc_effective_size',
        'description': 'mcmc_effective_size -- category 14-bayesian-toolkit, method card #72.',
        'args': {'chains': 'Handle to a list of per-chain matrices· ESS (POOLED = sum of the chains).'},
        'input_example': {'chains': '<raw_handle>'},
    },
    'mcmc_gelman': {
        'fn': 'mcmc_gelman',
        'description': 'mcmc_gelman -- category 14-bayesian-toolkit, method card #72.',
        'args': {'chains': 'Handle to a list of per-chain matrices (>=2 chains· Gelman-Rubin PSRF/MPSRF).', 'confidence': 'Confidence level, strictly (0,1) (default 0.95).'},
        'input_example': {'chains': '<raw_handle>', 'confidence': 0.95},
    },
    'mcmc_geweke': {
        'fn': 'mcmc_geweke',
        'description': 'mcmc_geweke -- category 14-bayesian-toolkit, method card #72.',
        'args': {'chains': 'Handle to a list of per-chain matrices (Geweke z-score per chain).', 'frac1': 'Fraction of the initial window (default 0.1· frac1+frac2<1).', 'frac2': 'Fraction of the final window (default 0.5).'},
        'input_example': {'chains': '<raw_handle>', 'frac1': 0.1, 'frac2': 0.5},
    },
    'mcmc_heidel': {
        'fn': 'mcmc_heidel',
        'description': 'mcmc_heidel -- category 14-bayesian-toolkit, method card #72.',
        'args': {'chain': 'Handle to ONE chain· Heidelberger-Welch stationarity + halfwidth.', 'eps': 'Halfwidth target accuracy (>0, default 0.1).', 'pvalue': 'Stationarity test p-value, strictly (0,1) (default 0.05).'},
        'input_example': {'chain': '<raw_handle>', 'eps': 0.1, 'pvalue': 0.05},
    },
    'mcmc_hpd_interval': {
        'fn': 'mcmc_hpd_interval',
        'description': 'mcmc_hpd_interval -- category 14-bayesian-toolkit, method card #72.',
        'args': {'chains': 'Handle to a list of per-chain matrices· HPD on the pooled draws.', 'prob': 'HPD probability, strictly (0,1) (default 0.95· 0/1 -> degenerate/full-range).'},
        'input_example': {'chains': '<raw_handle>', 'prob': 0.95},
    },
    'mcmc_raftery': {
        'fn': 'mcmc_raftery',
        'description': 'mcmc_raftery -- category 14-bayesian-toolkit, method card #72.',
        'args': {'chain': 'Handle to ONE chain (numeric matrix iter x var)· Raftery-Lewis run-length.', 'q': 'Quantile to estimate, strictly (0,1) (default 0.025).', 'r': 'Accuracy r, strictly (0,1) (default 0.005).', 's': 'Probability within r, strictly (0,1) (default 0.95).'},
        'input_example': {'chain': '<raw_handle>', 'q': 0.025, 'r': 0.005, 's': 0.95},
    },
    'bugs_style_mcmc': {
        'fn': 'bugs_style_mcmc',
        'description': 'bugs_style_mcmc -- category 14-bayesian-toolkit, method card #70.',
        'args': {'code': 'BUGS-style model definition AS A STRING (parse ONLY, injection-safe — no eval).', 'inits': 'Handle to a named list of initial values (covers ALL the top-level stochastic parameters).', 'monitors': "Non-empty character vector of nodes to monitor (e.g. ['mu','sigma']).", 'constants': 'Handle to a named list of constants/dimensions (e.g. N)· optional.', 'data': 'Handle to a named list of observations (WITHOUT NA -> silent MISSING-node imputation).', 'niter': 'Total MCMC iterations (default 2000).', 'nburnin': 'Burn-in (default 1000· nburnin < niter required).', 'nchains': 'Number of chains (>=2 for gelman.diag· default 2).', 'seed': 'REQUIRED single integer seed (reproducibility· setSeed vector).', 'thin': 'Thinning (default 1).', 'rhat_threshold': 'Gelman R-hat threshold (default 1.1, looser BUGS).', 'ess_min': 'Minimum effective sample size (default 100).', 'allow_nonconvergence': 'True -> converged=False instead of stop.'},
        'input_example': {'code': '...', 'inits': '<raw_handle>', 'monitors': ['PROVIDER/DATASET/SERIES'], 'niter': 2000, 'nburnin': 1000, 'nchains': 2, 'seed': 1, 'thin': 1, 'rhat_threshold': 1.1, 'ess_min': 100, 'allow_nonconvergence': False},
    },
    'post_draw_summary': {
        'fn': 'post_draw_summary',
        'description': 'post_draw_summary -- category 14-bayesian-toolkit, method card #71.',
        'args': {'x': "Handle to a 3D draws array (iter x chain x var), an MCMC draws list, or 'draws' object (nchains>=2).", 'include_mcse': 'True -> adds an mcse_mean column (Monte-Carlo SE of the mean).'},
        'input_example': {'x': '<raw_handle>', 'include_mcse': False},
    },
    'stan_compile': {
        'fn': 'stan_compile',
        'description': 'stan_compile -- category 14-bayesian-toolkit, method card #68.',
        'args': {'model_code': 'Stan model AS A STRING· stan_model compile (~40s) -> compiled stanmodel handle.', 'model_name': 'Model name (default anon_model).'},
        'input_example': {'model_code': '...', 'model_name': 'anon_model'},
    },
    'stan_fit': {
        'fn': 'stan_fit',
        'description': 'stan_fit -- category 14-bayesian-toolkit, method card #68.',
        'args': {'model_code': 'Stan model AS A STRING· one-shot compile + sample.', 'data': 'Handle to a named data list (Stan data block).', 'model_name': 'Model name (default anon_model).', 'seed': 'REQUIRED seed (reproducibility of the Stan RNG).', 'chains': 'Number of chains (>=2).', 'iter': 'Iterations per chain.', 'allow_nonconvergence': 'True -> converged=False instead of stop.'},
        'input_example': {'model_code': '...', 'data': '<raw_handle>', 'model_name': 'anon_model', 'seed': 1, 'chains': 2, 'iter': 1000, 'allow_nonconvergence': False},
    },
    'stan_sample': {
        'fn': 'stan_sample',
        'description': 'stan_sample -- category 14-bayesian-toolkit, method card #68.',
        'args': {'model': 'Handle to a compiled stanmodel (from stan_compile).', 'data': 'Handle to a GENUINE named data list matching the Stan data block (numeric, finite).', 'seed': 'REQUIRED seed (the Stan RNG is not affected by seeded· default RANDOM).', 'chains': 'Number of chains (>=2 required: the split-R-hat of one chain does not detect non-convergence).', 'iter': 'Iterations per chain (default 1000, warmup=iter/2).', 'algorithm': 'Sampler (only NUTS).', 'rhat_max': 'Threshold of the rank-normalized split-R-hat (hard gate, default 1.01).', 'ess_min': 'Minimum Bulk/Tail ESS (hard gate, default 400).', 'allow_nonconvergence': 'True -> returns draws with converged=False instead of stopping on non-convergence.'},
        'input_example': {'model': '<raw_handle>', 'data': '<raw_handle>', 'seed': 1, 'chains': 2, 'iter': 1000, 'rhat_max': 1.01, 'ess_min': 400, 'allow_nonconvergence': False},
    },
    'stan_syntax_check': {
        'fn': 'stan_syntax_check',
        'description': 'stan_syntax_check -- category 14-bayesian-toolkit, method card #68.',
        'args': {'model_code': 'Stan model AS A STRING (sandboxed DSL, never evaluated as code here)· cheap stanc syntax pre-gate.', 'model_name': 'Model name (default anon_model).'},
        'input_example': {'model_code': '...', 'model_name': 'anon_model'},
    },
    'smc_filter': {
        'fn': 'smc_filter',
        'description': 'smc_filter -- category 14-bayesian-toolkit, method card #205.',
        'args': {'code': 'BUGS-style state-space model definition AS A STRING (parse ONLY, injection-safe — no eval).', 'inits': 'Handle to a named list of initial values (covers ALL the top-level stochastic parameters).', 'latentNodes': "Non-empty character vector of stochastic latent nodes in time order (e.g. ['x'] or ['x[1:10]']).", 'seed': 'REQUIRED single integer seed (reproducibility· seeded before the run).', 'constants': 'Handle to a named list of constants/dimensions (e.g. Tn)· optional.', 'data': 'Handle to a named list of observations (WITHOUT NA -> silent MISSING-node imputation).', 'method': 'Particle filter· default bootstrap. Only bootstrap/auxiliary return logLik+ESS.', 'nParticles': 'Number of particles m for run(m) (integer >= 1· default 1000).', 'params': '(liuWest ONLY) top-level parameters to estimate· empty -> auto (top-level except latent).', 'thresh': '(ONLY bootstrap) resampling threshold· MUST be == 1 (resample at every step => equally weighted mvEWSamples => correct per-time summaries)· thresh<1 is blocked.', 'lookahead': '(auxiliary ONLY) lookahead for the auxiliary weights· default simulate.', 'd': '(liuWest ONLY) discount factor in (0,1) — close to but NOT above 1 (default 0.99).', 'probs': 'Quantiles for the per-time filtered summaries (default 0.025/0.25/0.5/0.75/0.975).'},
        'input_example': {'code': '...', 'inits': '<raw_handle>', 'latentNodes': ['PROVIDER/DATASET/SERIES'], 'seed': 1, 'nParticles': 1000, 'thresh': 1, 'd': 0.99},
    },
    'bt_loo_compare': {
        'fn': 'bt_loo_compare',
        'description': 'bt_loo_compare -- category 14-bayesian-toolkit, method card #507.',
        'args': {'fits': 'Handles to fitted Bayesian models.', 'method': 'Criterion.', 'pointwise': 'Return pointwise contributions.', 'scale': 'Reporting scale.'},
        'input_example': {'fits': ['<raw_handle>'], 'method': 'loo', 'pointwise': True, 'scale': 'log'},
    },
    'bt_stacking_weights': {
        'fn': 'bt_stacking_weights',
        'description': 'bt_stacking_weights -- category 14-bayesian-toolkit, method card #507.',
        'args': {'fits': 'Handles to fitted Bayesian models.', 'method': 'Weighting method.', 'nboot': 'Number of bootstrap replications.', 'seed': 'Seed for the random number generator.'},
        'input_example': {'fits': ['<raw_handle>'], 'method': 'stacking', 'nboot': 1000},
    },
    'bt_bayes_factor': {
        'fn': 'bt_bayes_factor',
        'description': 'bt_bayes_factor -- category 14-bayesian-toolkit, method card #508.',
        'args': {'fit': 'Handle to a fitted Bayesian model.', 'parameter': 'Parameter tested.', 'null_value': 'Null value.', 'method': 'Method.'},
        'input_example': {'fit': '<raw_handle>', 'parameter': '...', 'null_value': 0.0, 'method': 'savage_dickey'},
    },
    'bt_rope': {
        'fn': 'bt_rope',
        'description': 'bt_rope -- category 14-bayesian-toolkit, method card #508.',
        'args': {'fit': 'Handle to a fitted Bayesian model.', 'parameter': 'Parameter assessed.', 'rope': 'Bounds of the region of practical equivalence.', 'hdi_prob': 'Credible interval mass.'},
        'input_example': {'fit': '<raw_handle>', 'parameter': '...', 'rope': [1.0, 2.0], 'hdi_prob': 0.94},
    },
    'bt_variational': {
        'fn': 'bt_variational',
        'description': 'bt_variational -- category 14-bayesian-toolkit, method card #509.',
        'args': {'model': 'Model specification.', 'data': 'Data.', 'method': 'Approximation method.', 'n_iterations': 'Optimiser iterations.', 'draws': 'Draws from the approximation.', 'seed': 'Seed for the random number generator; required for reproducibility.'},
        'input_example': {'model': '...', 'data': '<df_handle>', 'method': 'pathfinder', 'n_iterations': 20000, 'draws': 1000, 'seed': 1},
    },
    'bt_prior_predictive': {
        'fn': 'bt_prior_predictive',
        'description': 'bt_prior_predictive -- category 14-bayesian-toolkit, method card #510.',
        'args': {'model': 'Model specification.', 'draws': 'Prior draws.', 'checks': 'Summaries to compute on the simulated data.', 'seed': 'Seed for the random number generator; required for reproducibility.'},
        'input_example': {'model': '...', 'draws': 1000, 'seed': 1},
    },
    'bt_elicit_prior': {
        'fn': 'bt_elicit_prior',
        'description': 'bt_elicit_prior -- category 14-bayesian-toolkit, method card #510.',
        'args': {'quantiles': 'Quantile levels.', 'values': 'Values at those quantiles.', 'family': 'Distribution family.', 'lower': 'Hard lower bound.', 'upper': 'Hard upper bound.'},
        'input_example': {'quantiles': [1.0, 2.0], 'values': [1.0, 2.0], 'family': 'auto'},
    },
    'bt_bart': {
        'fn': 'bt_bart',
        'description': 'bt_bart -- category 14-bayesian-toolkit, method card #511.',
        'args': {'y': 'Outcome.', 'x': 'Covariate table.', 'n_trees': 'Number of trees.', 'draws': 'Posterior draws.', 'warmup': 'Warm-up draws.', 'response': 'Response type.', 'seed': 'Seed for the random number generator; required for reproducibility.'},
        'input_example': {'y': '<series_handle>', 'x': '<df_handle>', 'n_trees': 50, 'draws': 2000, 'warmup': 1000, 'response': 'continuous', 'seed': 1},
    },
    'bt_gaussian_process': {
        'fn': 'bt_gaussian_process',
        'description': 'bt_gaussian_process -- category 14-bayesian-toolkit, method card #512.',
        'args': {'y': 'Outcome.', 'x': 'Inputs.', 'kernel': 'Covariance kernel.', 'approximation': 'Approximation for large samples.', 'n_inducing': 'Inducing points for a sparse fit.', 'draws': 'Posterior draws.', 'seed': 'Seed for the random number generator; required for reproducibility.'},
        'input_example': {'y': '<series_handle>', 'x': '<multiseries_handle>', 'kernel': 'matern52', 'approximation': 'none', 'n_inducing': 100, 'draws': 1000, 'seed': 1},
    },
}
