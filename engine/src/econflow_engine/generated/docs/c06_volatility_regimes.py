# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.v1.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 06-volatility-regimes: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'bekk_estimate': {
        'fn': 'bekk_estimate',
        'description': 'bekk_estimate -- category 06-volatility-regimes, METHOD-SELECTION card #160.',
        'args': {'y': 'Handle to a T×N returns matrix (N>=2, without NA).', 'type': 'BEKK type (default bekk· dbekk=diagonal, sbekk=scalar).', 'asymmetric': 'Asymmetric (leverage) volatility structure.', 'signs': 'N-vector of {1,-1} for asymmetric effects (asymmetric=True only· default rep(-1,N)).', 'QML_t_ratios': 'QML (robust) t-ratios instead of asymptotic ones.', 'max_iter': 'Maximum BHHH iterations (default 50).', 'crit': 'BHHH convergence criterion (default 1e-9).', 'seed': 'Reproducibility seed (default 2025).'},
        'input_example': {'y': '<matrix_handle>', 'asymmetric': False, 'QML_t_ratios': False, 'max_iter': 50, 'crit': 1e-09, 'seed': 2025},
    },
    'bekk_var': {
        'fn': 'bekk_var',
        'description': 'bekk_var -- category 06-volatility-regimes, METHOD-SELECTION card #160.',
        'args': {'object': "Handle to a 'bekkFit' (from bekk_estimate).", 'p': 'VaR confidence level in (0,1) (default 0.99, Basel).', 'portfolio_weights': 'N-vector of portfolio weights (None -> per-series VaR).', 'distribution': 'Residual distribution (default normal· empirical requires >=1000 obs).'},
        'input_example': {'object': '<raw_handle>', 'p': 0.99},
    },
    'bekk_virf': {
        'fn': 'bekk_virf',
        'description': 'bekk_virf -- category 06-volatility-regimes, METHOD-SELECTION card #160.',
        'args': {'object': "Handle to a SYMMETRIC 'bekkFit' (from bekk_estimate· asymmetric=False).", 'time': 'Time point of the shock (1..T).', 'q': 'Quantile of the shock in (0,1) (default 0.05).', 'index_series': 'Series the shock is applied to (1..N).', 'n_ahead': 'VIRF horizon (>=1, default 10).', 'ci': 'Confidence band level in (0,1) (default 0.9).', 'time_shock': "Use the estimated residuals at 'time' as the shock."},
        'input_example': {'object': '<raw_handle>', 'time': 1, 'q': 0.05, 'index_series': 1, 'n_ahead': 10, 'ci': 0.9, 'time_shock': False},
    },
    'dcc_fit': {
        'fn': 'dcc_fit',
        'description': 'dcc_fit -- category 06-volatility-regimes, METHOD-SELECTION card #29.',
        'args': {'spec': "Handle to a 'DCCspec' (from dcc_spec).", 'data': 'Handle to a multivariate numeric matrix (>=2 columns, without NA).', 'out_sample': 'Out-of-sample observations (default 0).', 'solver': 'Optimizer (default solnp).'},
        'input_example': {'spec': '<raw_handle>', 'data': '<matrix_handle>', 'out_sample': 0},
    },
    'dcc_forecast': {
        'fn': 'dcc_forecast',
        'description': 'dcc_forecast -- category 06-volatility-regimes, METHOD-SELECTION card #29.',
        'args': {'fit': "Handle to a 'DCCfit' (from dcc_fit).", 'n_ahead': 'Forecast horizon for correlation/covariance (default 1).', 'n_roll': 'Rolling forecasts over out.sample (default 0).'},
        'input_example': {'fit': '<raw_handle>', 'n_ahead': 1, 'n_roll': 0},
    },
    'dcc_multispec': {
        'fn': 'dcc_multispec',
        'description': 'dcc_multispec -- category 06-volatility-regimes, METHOD-SELECTION card #29.',
        'args': {'specs': "Array of handles to 'uGARCHspec' objects (output of ga_spec$object) — one per asset, AT LEAST 2."},
        'input_example': {'specs': ['<raw_handle_1>', '<raw_handle_2>']},
    },
    'dcc_roll': {
        'fn': 'dcc_roll',
        'description': 'dcc_roll -- category 06-volatility-regimes, METHOD-SELECTION card #29.',
        'args': {'spec': "Handle to a 'DCCspec' (from dcc_spec).", 'data': 'Handle to a multivariate numeric matrix (>=2 columns).', 'forecast_length': 'Length of the rolling out-of-sample period (default 50).', 'refit_every': 'Re-estimate every n steps (default 25).', 'refit_window': 'Re-estimation window (default recursive).', 'solver': 'Optimizer (default solnp).'},
        'input_example': {'spec': '<raw_handle>', 'data': '<matrix_handle>', 'forecast_length': 50, 'refit_every': 25},
    },
    'dcc_sim': {
        'fn': 'dcc_sim',
        'description': 'dcc_sim -- category 06-volatility-regimes, METHOD-SELECTION card #29.',
        'args': {'fit': "Handle to a 'DCCfit' (from dcc_fit).", 'n_sim': 'Length of each simulated path (default 1000).', 'n_start': 'Burn-in observations (default 0).', 'm_sim': 'Number of independent paths (default 1· seeded).'},
        'input_example': {'fit': '<raw_handle>', 'n_sim': 1000, 'n_start': 0, 'm_sim': 1},
    },
    'dcc_spec': {
        'fn': 'dcc_spec',
        'description': 'dcc_spec -- category 06-volatility-regimes, METHOD-SELECTION card #29.',
        'args': {'uspec': "Handle to a 'uGARCHmultispec' (from dcc_multispec).", 'model': 'DCC model (default DCC· aDCC=asymmetric).', 'distribution': 'Multivariate distribution (default mvnorm).', 'VAR': 'VAR filter on the conditional mean (default False).', 'lag': 'VAR lag order when VAR=True (default 1).'},
        'input_example': {'uspec': '<raw_handle>', 'VAR': False, 'lag': 1},
    },
    'fsv_cov': {
        'fn': 'fsv_cov',
        'description': 'fsv_cov -- category 06-volatility-regimes, METHOD-SELECTION card #163.',
        'args': {'object': "Handle to an 'fsvdraws' (from fsv_sample)."},
        'input_example': {'object': '<raw_handle>'},
    },
    'fsv_predict': {
        'fn': 'fsv_predict',
        'description': 'fsv_predict -- category 06-volatility-regimes, METHOD-SELECTION card #163.',
        'args': {'object': "Handle to an 'fsvdraws' (from fsv_sample).", 'ahead': 'Forecast horizons (positive integers, e.g. [1,5,10]· default [1]).', 'each': 'Predictive draws per stored MCMC draw (default 1).'},
        'input_example': {'object': '<raw_handle>', 'ahead': [1, 1], 'each': 1},
    },
    'fsv_sample': {
        'fn': 'fsv_sample',
        'description': 'fsv_sample -- category 06-volatility-regimes, METHOD-SELECTION card #163.',
        'args': {'y': 'T×N returns matrix (>=2 columns, without NA/constant columns).', 'factors': 'Number of latent factors (integer 1..N· default 1).', 'draws': 'MCMC draws after burn-in (default 300).', 'burnin': 'Initial MCMC draws to discard (default 100).', 'restrict': "Factor loading restriction: 'none' (all estimated· preferred for cov/pred) or 'upper' (zeros above the diagonal· stabilises/identifies). Default none.", 'seed': 'MCMC reproducibility seed (default 2025).'},
        'input_example': {'y': '<matrix_handle>', 'factors': 1, 'draws': 300, 'burnin': 100, 'seed': 2025},
    },
    'ga_diagnostics': {
        'fn': 'ga_diagnostics',
        'description': 'ga_diagnostics -- category 06-volatility-regimes, METHOD-SELECTION card #28.',
        'args': {'fit': "Handle to a 'uGARCHfit' (from ga_fit).", 'gof_groups': 'Goodness-of-fit test groups (must be > parameters+1, default 20).'},
        'input_example': {'fit': '<raw_handle>', 'gof_groups': 20},
    },
    'ga_fit': {
        'fn': 'ga_fit',
        'description': 'ga_fit -- category 06-volatility-regimes, METHOD-SELECTION card #28.',
        'args': {'spec': "Handle to a 'uGARCHspec' (from ga_spec).", 'data': 'Handle to a univariate numeric series (returns, without NA).', 'out_sample': 'Out-of-sample observations for the backtest (default 0).', 'solver': 'ML optimizer (default hybrid).'},
        'input_example': {'spec': '<raw_handle>', 'data': '<series_handle>', 'out_sample': 0},
    },
    'ga_forecast': {
        'fn': 'ga_forecast',
        'description': 'ga_forecast -- category 06-volatility-regimes, METHOD-SELECTION card #28.',
        'args': {'fit': "Handle to a 'uGARCHfit' (from ga_fit).", 'n_ahead': 'Forecast horizon (>=1, default 10).', 'n_roll': 'Rolling forecasts over out.sample (default 0).'},
        'input_example': {'fit': '<raw_handle>', 'n_ahead': 10, 'n_roll': 0},
    },
    'ga_roll': {
        'fn': 'ga_roll',
        'description': 'ga_roll -- category 06-volatility-regimes, METHOD-SELECTION card #28.',
        'args': {'spec': "Handle to a 'uGARCHspec' (from ga_spec).", 'data': 'Handle to a univariate numeric series (returns).', 'forecast_length': 'Length of the rolling out-of-sample period (default 500).', 'refit_every': 'Re-estimate every n steps (default 25).', 'refit_window': 'Re-estimation window (default recursive).', 'solver': 'Optimizer (default hybrid).', 'calculate_VaR': 'Compute VaR + backtest on the rolling forecast.'},
        'input_example': {'spec': '<raw_handle>', 'data': '<series_handle>', 'forecast_length': 500, 'refit_every': 25, 'calculate_VaR': True},
    },
    'ga_sim': {
        'fn': 'ga_sim',
        'description': 'ga_sim -- category 06-volatility-regimes, METHOD-SELECTION card #28.',
        'args': {'fit': "Handle to a 'uGARCHfit' (from ga_fit).", 'n_sim': 'Length of each simulated path (default 1000).', 'n_start': 'Burn-in observations (default 0).', 'm_sim': 'Number of independent paths (default 1· seeded).'},
        'input_example': {'fit': '<raw_handle>', 'n_sim': 1000, 'n_start': 0, 'm_sim': 1},
    },
    'ga_spec': {
        'fn': 'ga_spec',
        'description': 'ga_spec -- category 06-volatility-regimes, METHOD-SELECTION card #28.',
        'args': {'model': 'Variance model type (default sGARCH· fGARCH requires a submodel).', 'garchOrder': 'GARCH order [p,q] (default [1,1]· e.g. [2,1]).', 'armaOrder': 'ARMA order of the mean model [AR,MA] (default [1,1]).', 'submodel': "Submodel for model='fGARCH' (e.g. 'GARCH','TGARCH','NGARCH').", 'distribution_model': 'Innovation distribution (default norm· std/sstd for fat tails).', 'include_mean': 'Include a constant term in the mean model.', 'archm': 'ARCH-in-mean (risk in the mean).', 'archpow': 'ARCH-in-mean power (1=st.dev, 2=variance).', 'variance_targeting': 'Variance targeting (omega from the sample uncond. variance).'},
        'input_example': {'include_mean': True, 'archm': False, 'archpow': 1, 'variance_targeting': False},
    },
    'gas_fit': {
        'fn': 'gas_fit',
        'description': 'gas_fit -- category 06-volatility-regimes, METHOD-SELECTION card #158.',
        'args': {'y': 'Univariate series (returns without NA· positive values for gamma/exp/weibull/lognorm/fisk/rayleigh).', 'distr': 'Conditional innovation distribution (default norm· t/ged for fat tails· gamma etc. for positive duration series).', 'scaling': 'Scaling of the score (default unit=fastest· fisher_* far heavier, numerical Fisher information).', 'param': "Parameterisation of the distribution (e.g. 'rate'/'scale' for gamma)· None=the distribution default.", 'p': 'Score order (non-negative integer, default 1).', 'q': 'Autoregressive order (non-negative integer, default 1).', 'par_static': '0/1 vector: which parameters are static· e.g. norm+[1,0] drives the VARIANCE (vol model) instead of the mean.', 'maxeval': 'Cap on ML iterations (default 10000 instead of 1e6)· guarantees finite runtime· non-convergence -> converged=False.'},
        'input_example': {'y': [0.5, 0.5], 'distr': 'norm', 'scaling': 'unit', 'p': 1, 'q': 1, 'maxeval': 10000},
    },
    'gas_forecast': {
        'fn': 'gas_forecast',
        'description': 'gas_forecast -- category 06-volatility-regimes, METHOD-SELECTION card #158.',
        'args': {'object': "Handle to a 'gas' object (from gas_fit).", 'method': 'mean_path=deterministic point path· simulated_paths=simulation + quantiles (STOCHASTIC, seeded).', 't_ahead': 'Forecast horizon (integer >=1, default 10).', 'rep_ahead': 'Number of simulated paths (simulated_paths only, default 1000).', 'quant': 'Quantile probabilities of the predictive distribution in (0,1) (simulated_paths only).'},
        'input_example': {'object': '<raw_handle>', 'method': 'mean_path', 't_ahead': 10, 'rep_ahead': 1000, 'quant': [0.5, 0.5]},
    },
    'gas_simulate': {
        'fn': 'gas_simulate',
        'description': 'gas_simulate -- category 06-volatility-regimes, METHOD-SELECTION card #158.',
        'args': {'object': "Handle to a 'gas' object (from gas_fit).", 't_sim': 'Length of the simulated path (integer >=1, default 10· seeded).'},
        'input_example': {'object': '<raw_handle>', 't_sim': 10},
    },
    'har_estimate': {
        'fn': 'har_estimate',
        'description': 'har_estimate -- category 06-volatility-regimes, METHOD-SELECTION card #157.',
        'args': {'RM': 'Realized measure of the integrated volatility (positive realized variance series, e.g. from hf_realized_var· without NA).', 'periods': 'Lags of the HAR components (Corsi 2009: [1,5,22] = daily/weekly/monthly).', 'type': 'HAR type: HAR (vanilla), HARJ (jump), HARQ (measurement-error corrected), HARQ-J.', 'BPV': 'Continuous/jump component (bipower variation)· REQUIRED for HARJ/HARQ-J (same length as RM).', 'RQ': 'Realized quarticity· REQUIRED for HARQ/HARQ-J (same length as RM).', 'periodsJ': 'Lags for the jump component (HARJ/HARQ-J).', 'periodsRQ': 'Lags for the realized quarticity component (HARQ/HARQ-J).', 'insanityFilter': 'Insanity filter on the fitted values (BPQ 2016 footnote 17).', 'h': 'Realized variance aggregation horizon (1=none, 5=weekly, 22=monthly).'},
        'input_example': {'RM': [0.5, 0.5], 'periods': [1, 1], 'type': 'HAR', 'insanityFilter': True, 'h': 1},
    },
    'har_forecast': {
        'fn': 'har_forecast',
        'description': 'har_forecast -- category 06-volatility-regimes, METHOD-SELECTION card #157.',
        'args': {'RM': 'Realized measure (positive realized variance series· without NA).', 'periods': 'Lags of the HAR components (default [1,5,22]).', 'nRoll': 'Number of rolling out-of-sample forecasts (>=1).', 'nAhead': 'Length of each rolling forecast (>=1)· must be 1 when h>1.', 'type': 'HAR model type to estimate and forecast.', 'windowType': 'Estimation window type: rolling/fixed or increasing/expanding.', 'BPV': 'Continuous/jump component· REQUIRED for HARJ/HARQ-J (same length as RM).', 'RQ': 'Realized quarticity· REQUIRED for HARQ/HARQ-J (same length as RM).', 'periodsJ': 'Lags jump component (HARJ/HARQ-J).', 'periodsRQ': 'Lags realized quarticity (HARQ/HARQ-J).', 'insanityFilter': 'Insanity filter on the forecasted values (BPQ 2016 footnote 17).', 'h': 'Aggregation horizon (1=none)· when h>1 then nAhead=1.'},
        'input_example': {'RM': [0.5, 0.5], 'periods': [1, 1], 'nRoll': 10, 'nAhead': 1, 'type': 'HAR', 'windowType': 'rolling', 'insanityFilter': True, 'h': 1},
    },
    'har_simulate': {
        'fn': 'har_simulate',
        'description': 'har_simulate -- category 06-volatility-regimes, METHOD-SELECTION card #157.',
        'args': {'len': 'Length of the simulated process (>=1).', 'periods': 'Lags used to build the HAR model (default [1,5,22]).', 'coef': 'Coefficients: length = length(periods)+1 (intercept + one per period).', 'errorTermSD': 'Standard deviation of the error term (>0).', 'seed': 'Reproducibility seed (stochastic process).'},
        'input_example': {'len': 1500, 'periods': [1, 1], 'coef': [0.5, 0.5], 'errorTermSD': 0.001, 'seed': 2025},
    },
    'hf_realized_cov': {
        'fn': 'hf_realized_cov',
        'description': 'hf_realized_cov -- category 06-volatility-regimes, METHOD-SELECTION card #156.',
        'args': {'data': 'T×N intraday matrix for ONE day (>=2 assets): prices or returns (see makeReturns), without NA.', 'measure': 'rCov=plain realized cov· rTSCov=noise-robust· rSemiCov=semivariance decomposition (default rCov).', 'makeReturns': 'True=data holds PRICES· False=already returns. rTSCov requires True.', 'cor': 'True=return the correlation matrix instead of the covariance (rCov/rTSCov).', 'K': 'rTSCov: slow time-scale (ticks)· default auto=floor(n/15)· requires n>=10*K.', 'J': 'rTSCov: fast time-scale (ticks, default 1).'},
        'input_example': {'data': '<matrix_handle>', 'makeReturns': True, 'cor': False, 'J': 1},
    },
    'hf_realized_var': {
        'fn': 'hf_realized_var',
        'description': 'hf_realized_var -- category 06-volatility-regimes, METHOD-SELECTION card #156.',
        'args': {'data': 'Intraday array for ONE day: prices (makeReturns=True) or returns (False), ordered, without NA.', 'measure': 'Realized measure (default rCov). rBPCov/medRV=jump-robust· rKernelCov/rTSCov=noise-robust.', 'makeReturns': 'True=data holds PRICES (log-returns taken internally)· False=already returns. rTSCov requires True.', 'kernelType': "Kernel for measure='rKernelCov' (default rectangular).", 'kernelParam': 'Lag order of the kernel (rKernelCov, default 1).', 'K': 'rTSCov: slow time-scale (ticks)· default auto=floor(n/15)· requires n>=10*K.', 'J': 'rTSCov: fast time-scale (ticks, default 1).'},
        'input_example': {'data': [0.5, 0.5], 'makeReturns': True, 'kernelParam': 1, 'J': 1},
    },
    'hf_spot_vol': {
        'fn': 'hf_spot_vol',
        'description': 'hf_spot_vol -- category 06-volatility-regimes, METHOD-SELECTION card #156.',
        'args': {'data': 'DataFrame with columns DT (POSIXct intraday timestamps, spanning several days) + price (levels).', 'method': 'Spot vol estimation method (default detPer=deterministic periodicity).', 'alignBy': 'Aggregation time scale (default minutes).', 'alignPeriod': 'Number of aggregation periods, positive integer (default 5).', 'marketOpen': 'Market open time in the tz zone (default 09:30:00).', 'marketClose': 'Market close time in the tz zone (default 16:00:00).', 'tz': 'Time zone of marketOpen/marketClose/DT (default GMT).'},
        'input_example': {'data': '<df_handle>', 'alignPeriod': 5, 'marketOpen': '09:30:00', 'marketClose': '16:00:00', 'tz': 'GMT'},
    },
    'hmm_decode': {
        'fn': 'hmm_decode',
        'description': 'hmm_decode -- category 06-volatility-regimes, METHOD-SELECTION card #161.',
        'args': {'object': "Handle to an 'fHMM_model' (from hmm_fit)."},
        'input_example': {'object': '<raw_handle>'},
    },
    'hmm_fit': {
        'fn': 'hmm_fit',
        'description': 'hmm_fit -- category 06-volatility-regimes, METHOD-SELECTION card #161.',
        'args': {'data': 'Numeric vector of observations/returns (>=20 obs, without NA/Inf, non-constant).', 'nstates': 'Number of hidden states of the Markov chain (>=2, default 2).', 'sdd': 'State-dependent distribution (default normal· gamma/lognormal->positive, poisson->non-negative integers).', 'runs': 'Number of randomly initialised optimization runs (default 5).', 'iterlim': 'Iteration limit per nlm run (default 100).', 'seed': 'Reproducibility seed (ncluster=1, single-core· default 2025).'},
        'input_example': {'data': [0.5, 0.5], 'nstates': 2, 'runs': 5, 'iterlim': 100, 'seed': 2025},
    },
    'hmm_predict': {
        'fn': 'hmm_predict',
        'description': 'hmm_predict -- category 06-volatility-regimes, METHOD-SELECTION card #161.',
        'args': {'object': "Handle to an 'fHMM_model' (from hmm_fit).", 'ahead': 'Forecast horizon (positive integer, default 5).', 'alpha': 'Significance level of the prediction interval in (0,1) (default 0.05).'},
        'input_example': {'object': '<raw_handle>', 'ahead': 5, 'alpha': 0.05},
    },
    'lstar_fit': {
        'fn': 'lstar_fit',
        'description': 'lstar_fit -- category 06-volatility-regimes, METHOD-SELECTION card #32.',
        'args': {'x': 'Handle to a univariate numeric series (without NA).', 'm': 'Embedding dimension / maximum lag (positive integer).', 'd': 'Time delay for the embedding (default 1).', 'thDelay': 'Lag of the threshold variable (default: internal selection).', 'gamma': 'Initial smoothness value (>0· default: internal estimate).', 'include': 'Deterministic terms (default const).'},
        'input_example': {'x': '<series_handle>', 'm': 1, 'd': 1},
    },
    'mc_analytics': {
        'fn': 'mc_analytics',
        'description': 'mc_analytics -- category 06-volatility-regimes, METHOD-SELECTION card #164.',
        'args': {'object': "Handle to a 'markovchain' object (from mc_fit)."},
        'input_example': {'object': '<raw_handle>'},
    },
    'mc_fit': {
        'fn': 'mc_fit',
        'description': 'mc_fit -- category 06-volatility-regimes, METHOD-SELECTION card #164.',
        'args': {'data': 'State sequence: character codes (or int_array). Length>=2, >=2 distinct, without NA.', 'method': 'Transition matrix estimator (default mle· bootstrap=STOCHASTIC CI).', 'laplacian': "Laplacian smoothing pseudo-count (>=0, default 0· effective for method='laplace').", 'confidencelevel': 'CI confidence level in (0,1) (default 0.95).', 'nboot': "Bootstrap replicates for method='bootstrap' (positive integer, default 10).", 'sanitize': 'Convert NaN rows to uniform (default False).', 'seed': "Reproducibility seed for method='bootstrap' (default 2025)."},
        'input_example': {'data': ['PROVIDER/DATASET/SERIES'], 'method': 'mle', 'laplacian': 0, 'confidencelevel': 0.95, 'nboot': 10, 'sanitize': False, 'seed': 2025},
    },
    'mfg_fit': {
        'fn': 'mfg_fit',
        'description': 'mfg_fit -- category 06-volatility-regimes, METHOD-SELECTION card #159.',
        'args': {'data': "Handle to a long-format DataFrame· REQUIRED column 'date' (Date), numeric y, numeric x constant per low.freq, low.freq column of class Date.", 'y': 'Name of the high-freq returns column (numeric, without NA).', 'x': 'Name of the low-freq macro variable column (MIDAS long-run· ONE value per low.freq period).', 'K': 'MIDAS lag-length (positive integer < number of low.freq periods).', 'low_freq': "Name of the low-freq index column of class Date (default 'date' = daily).", 'weighting': 'MIDAS beta weighting scheme (default beta.restricted, w1=1).', 'gamma': 'Asymmetric GJR-GARCH term in the short-run component (default True).', 'var_ratio_freq': 'Frequency column for the variance ratio (default: low.freq).'},
        'input_example': {'data': '<df_handle>', 'y': '...', 'x': '...', 'K': 1, 'low_freq': 'date', 'gamma': True},
    },
    'mfg_predict': {
        'fn': 'mfg_predict',
        'description': 'mfg_predict -- category 06-volatility-regimes, METHOD-SELECTION card #159.',
        'args': {'object': "Handle to an 'mfGARCH' model (from mfg_fit).", 'horizon': 'Forecast horizons for total volatility (positive integers, default 1:10).'},
        'input_example': {'object': '<raw_handle>'},
    },
    'mfg_simulate': {
        'fn': 'mfg_simulate',
        'description': 'mfg_simulate -- category 06-volatility-regimes, METHOD-SELECTION card #159.',
        'args': {'n_days': 'Number of days to simulate (positive integer).', 'mu': 'Mean of the returns.', 'alpha': 'GARCH ARCH coefficient (short-run).', 'beta': 'GARCH persistence coefficient (short-run).', 'gamma': 'Asymmetric (leverage) coefficient.', 'm': 'Constant term of the long-run component.', 'theta': 'Sensitivity of the long-run component to the MIDAS covariate.', 'w2': 'Beta weighting parameter w2.', 'K': 'MIDAS lag-length (positive integer < low.freq).', 'psi': 'AR(1) persistence of the simulated covariate.', 'sigma_psi': 'Standard deviation of the covariate innovations.', 'w1': 'Beta weighting parameter w1 (default 1, restricted).', 'low_freq': 'Length of the low-freq period in days (default 1).', 'n_intraday': 'Intraday observations per day (default 288).', 'corr': 'Returns-covariate correlation (leverage, default 0).'},
        'input_example': {'n_days': 1, 'mu': 0.5, 'alpha': 0.5, 'beta': 0.5, 'gamma': 0.5, 'm': 0.5, 'theta': 0.5, 'w2': 0.5, 'K': 1, 'psi': 0.5, 'sigma_psi': 0.5, 'w1': 1, 'low_freq': 1, 'n_intraday': 288, 'corr': 0},
    },
    'msg_fit_mcmc': {
        'fn': 'msg_fit_mcmc',
        'description': 'msg_fit_mcmc -- category 06-volatility-regimes, METHOD-SELECTION card #31.',
        'args': {'spec': "Handle to an 'MSGARCH_SPEC' (from msg_spec).", 'data': 'Handle to a univariate numeric series (returns, without NA).'},
        'input_example': {'spec': '<raw_handle>', 'data': '<series_handle>'},
    },
    'msg_fit_ml': {
        'fn': 'msg_fit_ml',
        'description': 'msg_fit_ml -- category 06-volatility-regimes, METHOD-SELECTION card #31.',
        'args': {'spec': "Handle to an 'MSGARCH_SPEC' (from msg_spec).", 'data': 'Handle to a univariate numeric series (returns, without NA).'},
        'input_example': {'spec': '<raw_handle>', 'data': '<series_handle>'},
    },
    'msg_predict': {
        'fn': 'msg_predict',
        'description': 'msg_predict -- category 06-volatility-regimes, METHOD-SELECTION card #31.',
        'args': {'fit': "Handle to an 'MSGARCH_ML_FIT'/'MSGARCH_MCMC_FIT' (from msg_fit_*).", 'nahead': 'Volatility forecast horizon (default 1).', 'do_cumulative': 'Cumulative (aggregated) volatility forecast.'},
        'input_example': {'fit': '<raw_handle>', 'nahead': 1, 'do_cumulative': False},
    },
    'msg_risk': {
        'fn': 'msg_risk',
        'description': 'msg_risk -- category 06-volatility-regimes, METHOD-SELECTION card #31.',
        'args': {'fit': "Handle to an 'MSGARCH_ML_FIT'/'MSGARCH_MCMC_FIT' (from msg_fit_*).", 'do_es': 'Compute Expected Shortfall in addition to VaR.', 'nahead': 'VaR/ES horizon (default 1).'},
        'input_example': {'fit': '<raw_handle>', 'do_es': True, 'nahead': 1},
    },
    'msg_sim': {
        'fn': 'msg_sim',
        'description': 'msg_sim -- category 06-volatility-regimes, METHOD-SELECTION card #31.',
        'args': {'fit': "Handle to an 'MSGARCH_ML_FIT'/'MSGARCH_MCMC_FIT' (from msg_fit_*).", 'nsim': 'Number of simulated paths (default 1· seeded).', 'nahead': 'Length of each path (default 1).', 'nburn': 'Burn-in observations (default 500).'},
        'input_example': {'fit': '<raw_handle>', 'nsim': 1, 'nahead': 1, 'nburn': 500},
    },
    'msg_spec': {
        'fn': 'msg_spec',
        'description': 'msg_spec -- category 06-volatility-regimes, METHOD-SELECTION card #31.',
        'args': {'model': 'Variance model per regime (recycled to K, default sGARCH).', 'distribution': 'Distribution per regime (recycled to K, default norm).', 'K': 'Number of regimes (default 2).', 'do_mix': 'Mixture (True) instead of Markov-switching (False, default).'},
        'input_example': {'K': 2, 'do_mix': False},
    },
    'msg_state': {
        'fn': 'msg_state',
        'description': 'msg_state -- category 06-volatility-regimes, METHOD-SELECTION card #31.',
        'args': {'fit': "Handle to an 'MSGARCH_ML_FIT'/'MSGARCH_MCMC_FIT' (from msg_fit_*)."},
        'input_example': {'fit': '<raw_handle>'},
    },
    'msw_fit': {
        'fn': 'msw_fit',
        'description': 'msw_fit -- category 06-volatility-regimes, METHOD-SELECTION card #30.',
        'args': {'formula': "Linear model formula, e.g. 'y ~ 1' or 'y ~ x1 + x2'.", 'data': 'Handle to a DataFrame holding the formula variables.', 'k': 'Number of regimes (>=2, default 2).', 'p': 'AR order of the residuals per regime (default 0).'},
        'input_example': {'formula': 'y ~ x', 'data': '<df_handle>', 'k': 2, 'p': 0},
    },
    'msw_intervals': {
        'fn': 'msw_intervals',
        'description': 'msw_intervals -- category 06-volatility-regimes, METHOD-SELECTION card #30.',
        'args': {'fit': "Handle to an 'MSM' model (from msw_fit).", 'level': 'Confidence level in (0,1) (default 0.95).'},
        'input_example': {'fit': '<raw_handle>', 'level': 0.95},
    },
    'msw_residuals': {
        'fn': 'msw_residuals',
        'description': 'msw_residuals -- category 06-volatility-regimes, METHOD-SELECTION card #30.',
        'args': {'fit': "Handle to an 'MSM' model (from msw_fit).", 'regime': 'Regime 1..k for conditional residuals (default: all).'},
        'input_example': {'fit': '<raw_handle>'},
    },
    'setar_fit': {
        'fn': 'setar_fit',
        'description': 'setar_fit -- category 06-volatility-regimes, METHOD-SELECTION card #32.',
        'args': {'x': 'Handle to a univariate numeric series (without NA).', 'm': 'Embedding dimension / maximum lag (positive integer).', 'd': 'Time delay for the embedding (default 1).', 'thDelay': 'Lag of the threshold variable, 0..(m-1) (default 0).', 'include': 'Deterministic terms (default const).', 'common': 'Common coefficients across regimes (default none).', 'model': 'TAR (levels) or MTAR (momentum, default TAR).', 'nthresh': 'Number of thresholds: 1 or 2 (default 1).', 'trim': 'Minimum share per regime in (0,0.5) (default 0.15).'},
        'input_example': {'x': '<series_handle>', 'm': 1, 'd': 1, 'thDelay': 0, 'nthresh': 1, 'trim': 0.15},
    },
    'setar_select': {
        'fn': 'setar_select',
        'description': 'setar_select -- category 06-volatility-regimes, METHOD-SELECTION card #32.',
        'args': {'x': 'Handle to a univariate numeric series (without NA).', 'm': 'Maximum lag / embedding dimension (positive integer).', 'thDelay': 'Threshold delay to test, 0..(m-1) (default 0).', 'nthresh': 'Number of thresholds: 1 or 2 (default 1).', 'trim': 'Minimum share per regime in (0,0.5) (default 0.15).', 'criterion': 'Selection criterion (default pooled-AIC).', 'include': 'Deterministic terms (default const).', 'model': 'TAR or MTAR (default TAR).'},
        'input_example': {'x': '<series_handle>', 'm': 1, 'thDelay': 0, 'nthresh': 1, 'trim': 0.15},
    },
    'setar_test': {
        'fn': 'setar_test',
        'description': 'setar_test -- category 06-volatility-regimes, METHOD-SELECTION card #32.',
        'args': {'x': 'Handle to a univariate numeric series (without NA).', 'm': 'Maximum lag / embedding dimension (positive integer).', 'thDelay': 'Threshold delay (default 0).', 'trim': 'Minimum share per regime in (0,0.5) (default 0.1).', 'include': 'Deterministic terms (default const).', 'nboot': 'Bootstrap replications (seeded, default 100).', 'test': '1vs=linear vs SETAR· 2vs3=1 vs 2 thresholds (default 1vs).', 'boot_scheme': 'Bootstrap scheme (default resample).'},
        'input_example': {'x': '<series_handle>', 'm': 1, 'thDelay': 0, 'trim': 0.1, 'nboot': 100},
    },
    'star_fit': {
        'fn': 'star_fit',
        'description': 'star_fit -- category 06-volatility-regimes, METHOD-SELECTION card #32.',
        'args': {'x': 'Handle to a univariate numeric series (without NA).', 'noRegimes': 'Maximum number of regimes to test (>=2).', 'm': 'Embedding dimension / maximum lag (default 2).', 'd': 'Time delay for the embedding (default 1).', 'sig': 'Significance level for adding a regime (default 0.05).'},
        'input_example': {'x': '<series_handle>', 'noRegimes': 1, 'm': 2, 'd': 1, 'sig': 0.05},
    },
    'sv_predict': {
        'fn': 'sv_predict',
        'description': 'sv_predict -- category 06-volatility-regimes, METHOD-SELECTION card #162.',
        'args': {'object': "Handle to an 'svdraws' (from sv_sample).", 'steps': 'Forecast horizon for future volatility (>=1, default 1).'},
        'input_example': {'object': '<raw_handle>', 'steps': 1},
    },
    'sv_sample': {
        'fn': 'sv_sample',
        'description': 'sv_sample -- category 06-volatility-regimes, METHOD-SELECTION card #162.',
        'args': {'y': 'Numeric vector of returns (without NA/Inf, length > 1).', 'model': 'SV variant: vanilla (Gaussian), t (Student-t errors), leverage (asymmetric)· default vanilla.', 'draws': 'MCMC draws after burnin (default 500· keep it small).', 'burnin': 'Burn-in draws (default 200).', 'priormu': 'Normal prior on mu: [mean, sd] (default [0,100]).', 'priorphi': 'Beta prior on (phi+1)/2: [a0,b0] positive (default [5,1.5]).', 'priorsigma': 'Scale of the Gamma prior on sigma (positive, default 1).', 'priornu': "Rate of the exp. prior on nu — model='t' only (default 0.1).", 'priorrho': "Beta prior on (rho+1)/2: [a,b] positive — model='leverage' only (default [4,4]).", 'keeptime': "'all'=full latent path (vol chart-data)· 'last'=last only (default all).", 'thin': 'Thinning interval draws (default 1).', 'ess_min': 'Minimum ESS threshold for the converged flag (default 20).'},
        'input_example': {'y': [0.5, 0.5], 'draws': 500, 'burnin': 200, 'priorsigma': 1, 'thin': 1, 'ess_min': 20},
    },
    'sv_simulate': {
        'fn': 'sv_simulate',
        'description': 'sv_simulate -- category 06-volatility-regimes, METHOD-SELECTION card #162.',
        'args': {'len': 'Length of the simulated series (>=2).', 'mu': 'Level of the log-variance (default -10).', 'phi': 'Persistence in (-1,1) (default 0.98).', 'sigma': 'Vol-of-vol, positive (default 0.2).', 'nu': 'Student-t degrees of freedom (>2· default Inf=Gaussian).', 'rho': 'Leverage correlation in (-1,1) (default 0=no leverage).'},
        'input_example': {'len': 1, 'mu': -10, 'phi': 0.98, 'sigma': 0.2, 'rho': 0},
    },
    'tg_backtest': {
        'fn': 'tg_backtest',
        'description': 'tg_backtest -- category 06-volatility-regimes, METHOD-SELECTION card #154.',
        'args': {'y': 'Numeric vector of returns (without NA/Inf, non-constant, >=40).', 'model': 'GARCH type (default garch).', 'constant': 'Estimate a constant (mean) term (default True).', 'order': 'GARCH order [p,q] (default [1,1]).', 'distribution': 'Innovation distribution (default norm).', 'start': 'Out-of-sample start index (>=10, default floor(n/2)).', 'end': 'End index (<=length(y), default length(y)).', 'h': 'Forecast horizon per step (default 1).', 'estimate_every': 'Re-estimate every n steps (default 1).', 'rolling': 'Rolling (True) vs expanding (False, default) window.', 'seed': 'Seed (default 2025).'},
        'input_example': {'y': [0.5, 0.5], 'constant': True, 'h': 1, 'estimate_every': 1, 'rolling': False, 'seed': 2025},
    },
    'tg_estimate': {
        'fn': 'tg_estimate',
        'description': 'tg_estimate -- category 06-volatility-regimes, METHOD-SELECTION card #154.',
        'args': {'y': 'Numeric vector of returns (without NA/Inf, non-constant, >=25).', 'model': 'GARCH type (default garch· egarch/gjrgarch/aparch=asymmetric, cgarch=component).', 'constant': 'Estimate a constant (mean) term for the returns (default True).', 'order': 'GARCH order [p,q] (default [1,1]).', 'distribution': 'Innovation distribution (default norm· std/ged for fat tails, s*=skew).', 'variance_targeting': 'Variance targeting (omega from the sample uncond. variance, default False).', 'solver': "ML optimizer (default 'nloptr').", 'seed': 'Seed (estimation is deterministic· default 2025).'},
        'input_example': {'y': [0.5, 0.5], 'constant': True, 'variance_targeting': False, 'solver': 'nloptr', 'seed': 2025},
    },
    'tg_predict': {
        'fn': 'tg_predict',
        'description': 'tg_predict -- category 06-volatility-regimes, METHOD-SELECTION card #154.',
        'args': {'object': "Handle to a 'tsgarch.estimate' (from tg_estimate).", 'h': 'Forecast horizon for conditional sigma/mean (>=1, default 1).', 'nsim': 'Simulated paths for the forecast distribution (0=point forecast, default 0· seeded).', 'sim_method': 'Simulation method when nsim>0 (default parametric).', 'seed': 'Seed for the stochastic simulation (default 2025).'},
        'input_example': {'object': '<raw_handle>', 'h': 1, 'nsim': 0, 'seed': 2025},
    },
    'thr_predict': {
        'fn': 'thr_predict',
        'description': 'thr_predict -- category 06-volatility-regimes, METHOD-SELECTION card #32.',
        'args': {'object': "Handle to an 'nlar' model (from setar_fit/lstar_fit/star_fit).", 'n_ahead': 'Forecast horizon (default 1).', 'type': 'naive=point· MC/bootstrap=distribution (seeded, default naive).', 'nboot': 'Replications for MC/bootstrap (default 100).', 'ci': 'Prediction interval level in (0,1) (default 0.95).'},
        'input_example': {'object': '<raw_handle>', 'n_ahead': 1, 'nboot': 100, 'ci': 0.95},
    },
    'thr_regime': {
        'fn': 'thr_regime',
        'description': 'thr_regime -- category 06-volatility-regimes, METHOD-SELECTION card #32.',
        'args': {'object': "Handle to a 'setar'/'lstar' model (from setar_fit/lstar_fit)."},
        'input_example': {'object': '<raw_handle>'},
    },
    'tm_cov': {
        'fn': 'tm_cov',
        'description': 'tm_cov -- category 06-volatility-regimes, METHOD-SELECTION card #155.',
        'args': {'object': "Handle to a 'dcc.estimate' (from tm_dcc_estimate).", 'correlation': 'True -> the `array` field becomes the conditional correlation instead of the covariance (default False).'},
        'input_example': {'object': '<raw_handle>', 'correlation': False},
    },
    'tm_dcc_estimate': {
        'fn': 'tm_dcc_estimate',
        'description': 'tm_dcc_estimate -- category 06-volatility-regimes, METHOD-SELECTION card #155.',
        'args': {'y': 'Handle to a numeric T×N returns matrix (N=2-3, without NA, no constant column).', 'dynamics': 'Correlation dynamics: constant=CCC (fixed), dcc=Engle DCC, adcc=asymmetric DCC (default constant).', 'distribution': 'Multivariate innovation distribution: mvn=normal, mvt=t (fat tails) (default mvn).', 'garch_model': 'Univariate variance model per series (shared, default garch).', 'garch_order': 'GARCH order [p,q] of the univariate models (default [1,1]).', 'garch_distribution': 'Univariate innovation distribution per series (default norm).', 'dcc_order': 'DCC order [a,b] of the correlation dynamics (default [1,1]· ignored when constant).', 'solver': 'Second-stage ML optimizer (default solnp).', 'seed': 'Reproducibility seed (ML is deterministic· default 2025).'},
        'input_example': {'y': '<matrix_handle>', 'garch_model': 'garch', 'garch_distribution': 'norm', 'seed': 2025},
    },
    'tm_predict': {
        'fn': 'tm_predict',
        'description': 'tm_predict -- category 06-volatility-regimes, METHOD-SELECTION card #155.',
        'args': {'object': "Handle to a 'dcc.estimate' (from tm_dcc_estimate).", 'h': 'Forecast horizon for conditional covariance/correlation (>=1, default 1).', 'nsim': 'Number of simulated paths for the forecast distribution (default 1000· seeded).', 'sim_method': 'parametric=draw from the assumed distribution· bootstrap=resample residuals (default parametric).', 'seed': 'Seed for the stochastic simulation (default 2025).'},
        'input_example': {'object': '<raw_handle>', 'h': 1, 'nsim': 1000, 'seed': 2025},
    },
}
