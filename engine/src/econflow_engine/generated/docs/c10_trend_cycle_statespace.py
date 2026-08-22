# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 10-trend-cycle-statespace: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'beast_changepoints': {
        'fn': 'beast_changepoints',
        'description': 'beast_changepoints -- category 10-trend-cycle-statespace, method card #186.',
        'args': {'object': 'Handle to a fitted beast (output of beast_decompose.object).', 'component': "Which component's change-points to extract· 'season' only if the fit had seasonality.", 'threshold': 'Minimum posterior probability cpPr ∈ [0,1] for a change-point to be kept.'},
        'input_example': {'object': '<raw_handle>', 'component': 'trend', 'threshold': 0},
    },
    'beast_decompose': {
        'fn': 'beast_decompose',
        'description': 'beast_decompose -- category 10-trend-cycle-statespace, method card #186.',
        'args': {'y': 'Regular (equally spaced) numeric series· without NA/Inf (hard gate).', 'season': "Seasonality form· 'none' = trend-only (the period is ignored).", 'period': 'Seasonality period (>=2)· REQUIRED for harmonic/dummy· otherwise silent period-guess.', 'tcp_minmax': '[min,max] of the allowed number of trend change-points (non-negative integers, min<=max).', 'scp_minmax': '[min,max] of the allowed number of seasonal change-points (non-negative integers, min<=max).', 'mcmc_samples': 'MCMC samples per chain (keep it small, ~2000).', 'mcmc_burnin': 'MCMC burn-in samples (>=0).', 'mcmc_chains': 'Number of MCMC chains (>=1· 1 for speed/determinism).', 'seed': 'mcmc.seed for reproducibility (>=0)· same seed ⇒ identical trend.'},
        'input_example': {'y': [0.5, 0.5], 'season': 'harmonic', 'tcp_minmax': [1, 1], 'scp_minmax': [1, 1], 'mcmc_samples': 2000, 'mcmc_burnin': 200, 'mcmc_chains': 1, 'seed': 2025},
    },
    'bsp_ar1': {
        'fn': 'bsp_ar1',
        'description': 'bsp_ar1 -- category 10-trend-cycle-statespace, method card #60.',
        'args': {'y': 'Handle to a univariate ts· stationary AR(1) latent cycle (Bayesian gap).', 'rho': 'Handle to a prior for the AR(1) rho (e.g. uniform ∈ (-1,1)).', 'sigma': 'Handle to a prior for the state standard deviation.', 'mu': 'Handle to a prior for the stationary mean (REQUIRED).', 'sd_y': 'Handle to a prior for the obs standard deviation.'},
        'input_example': {'y': '<series_handle>', 'rho': '<raw_handle>', 'sigma': '<raw_handle>', 'mu': '<raw_handle>', 'sd_y': '<raw_handle>'},
    },
    'bsp_basic_structural': {
        'fn': 'bsp_basic_structural',
        'description': 'bsp_basic_structural -- category 10-trend-cycle-statespace, method card #60.',
        'args': {'y': 'Handle to a univariate ts· basic structural (level + optional slope/seasonal).', 'sd_y': 'Handle to a prior (bsp_prior) for the obs standard deviation.', 'sd_level': 'Handle to a prior for the level standard deviation.', 'sd_slope': 'Handle to a prior for the slope (None -> without a slope term).', 'sd_seasonal': 'Handle to a prior for the seasonality (None -> without a seasonal term).', 'period': 'Seasonal period (>=2, < n)· required with sd_seasonal.'},
        'input_example': {'y': '<series_handle>', 'sd_y': '<raw_handle>', 'sd_level': '<raw_handle>'},
    },
    'bsp_prior': {
        'fn': 'bsp_prior',
        'description': 'bsp_prior -- category 10-trend-cycle-statespace, method card #60.',
        'args': {'distribution': 'Prior family (default halfnormal).', 'init': 'Initial parameter value (within the support of the distribution).', 'sd': 'Standard deviation (halfnormal/normal/tnormal)· > 0.', 'mean': 'Mean (normal/tnormal).', 'min': 'Lower bound (uniform/tnormal).', 'max': 'Upper bound (uniform/tnormal).', 'shape': 'Shape parameter (gamma)· > 0.', 'rate': 'Rate parameter (gamma)· > 0.'},
        'input_example': {'init': 0.5},
    },
    'bsp_run_mcmc': {
        'fn': 'bsp_run_mcmc',
        'description': 'bsp_run_mcmc -- category 10-trend-cycle-statespace, method card #60.',
        'args': {'model': 'Handle to a lineargaussian model (from bsp_basic_structural/bsp_ar1).', 'iter': 'Number of MCMC iterations.', 'seed': 'Seed REQUIRED (determinism -- the bssm default is random).', 'burnin': 'Iterations burn-in ∈ [0, iter)· default floor(iter/2).', 'thin': 'Thinning interval (positive integer).', 'output_type': 'full -> states+theta· summary· theta only (default full).'},
        'input_example': {'model': '<raw_handle>', 'iter': 1, 'seed': 1, 'thin': 1},
    },
    'dl_forecast': {
        'fn': 'dl_forecast',
        'description': 'dl_forecast -- category 10-trend-cycle-statespace, method card #59.',
        'args': {'object': 'Handle to a dlmFiltered (the filtered_obj from dl_local_level/.../dl_trend_cycle).', 'n_ahead': 'Forecast horizon (positive integer).', 'level': 'Confidence level ∈ (0,1).'},
        'input_example': {'object': '<raw_handle>', 'n_ahead': 8, 'level': 0.95},
    },
    'dl_local_level': {
        'fn': 'dl_local_level',
        'description': 'dl_local_level -- category 10-trend-cycle-statespace, method card #59.',
        'args': {'y': 'Handle to a univariate ts· local level (dlmModPoly order=1).', 'seasonal': 'Add a dummy seasonal term.', 'seasonal_period': 'Seasonal period (>=2, <=n)· default frequency(y).'},
        'input_example': {'y': '<series_handle>', 'seasonal': False},
    },
    'dl_local_linear_trend': {
        'fn': 'dl_local_linear_trend',
        'description': 'dl_local_linear_trend -- category 10-trend-cycle-statespace, method card #59.',
        'args': {'y': 'Handle to a univariate ts· local linear trend (dlmModPoly order=2).', 'seasonal': 'Add a dummy seasonal term.', 'seasonal_period': 'Seasonal period (>=2, <=n)· default frequency(y).'},
        'input_example': {'y': '<series_handle>', 'seasonal': False},
    },
    'dl_trend_cycle': {
        'fn': 'dl_trend_cycle',
        'description': 'dl_trend_cycle -- category 10-trend-cycle-statespace, method card #59.',
        'args': {'y': 'Handle to a univariate ts· trend + rotation-form stochastic cycle (output gap).', 'cycle_period': 'Cycle length in periods (> 2)· default 8*frequency.', 'seasonal': 'Add a dummy seasonal term.', 'seasonal_period': 'Seasonal period (>=2, <=n)· default frequency(y).'},
        'input_example': {'y': '<series_handle>', 'seasonal': False},
    },
    'ham_filter': {
        'fn': 'ham_filter',
        'description': 'ham_filter -- category 10-trend-cycle-statespace, method card #57.',
        'args': {'x': 'Handle to an series from ham_frame_from_long (kept as series).', 'h': 'Regression horizon (default 2*periods_per_year).', 'p': 'Number of lags (>=2· default periods_per_year).'},
        'input_example': {'x': '<raw_handle>'},
    },
    'ham_regression': {
        'fn': 'ham_regression',
        'description': 'ham_regression -- category 10-trend-cycle-statespace, method card #57.',
        'args': {'x': 'Handle to an series from ham_frame_from_long (underlying Hamilton regression).', 'h': 'Regression horizon (default 2*periods_per_year).', 'p': 'Number of lags (>=2· default periods_per_year).'},
        'input_example': {'x': '<raw_handle>'},
    },
    'ham_frame_from_long': {
        'fn': 'ham_frame_from_long',
        'description': 'ham_frame_from_long -- category 10-trend-cycle-statespace, method card #57.',
        'args': {'df': 'Handle to a long DataFrame (one series, period/value).', 'series_name': 'Series name -> colname of the series (determines the output names).', 'transform': 'log100 = 100*log (Hamilton canonical for levels).', 'frequency': 'Frequency assertion (1/4/12)· None -> inferred.'},
        'input_example': {'df': '<df_handle>', 'series_name': '...'},
    },
    'hp_one_sided': {
        'fn': 'hp_one_sided',
        'description': 'hp_one_sided -- category 10-trend-cycle-statespace, method card #92.',
        'args': {'x': 'Handle to a univariate ts· one-sided (real-time) HP trend· cycle = gap.', 'lambda': 'Smoothing (default 1600 quarterly· Basel III credit-to-GDP = 400000).'},
        'input_example': {'x': '<series_handle>', 'lambda': 1600},
    },
    'kf_forecast': {
        'fn': 'kf_forecast',
        'description': 'kf_forecast -- category 10-trend-cycle-statespace, method card #58.',
        'args': {'object': 'Handle to a fitted SSModel (the model from kf_local_level/.../kf_trend_cycle).', 'n_ahead': 'Forecast horizon (positive integer).', 'interval': 'Interval type (default prediction).', 'level': 'Confidence level ∈ (0,1).'},
        'input_example': {'object': '<raw_handle>', 'n_ahead': 8, 'level': 0.95},
    },
    'kf_local_level': {
        'fn': 'kf_local_level',
        'description': 'kf_local_level -- category 10-trend-cycle-statespace, method card #58.',
        'args': {'y': 'Handle to a univariate ts· local level (level random walk).', 'seasonal': 'Add a dummy seasonal term.', 'seasonal_period': 'Seasonal period (>=2, <=n)· default frequency(y).'},
        'input_example': {'y': '<series_handle>', 'seasonal': False},
    },
    'kf_local_linear_trend': {
        'fn': 'kf_local_linear_trend',
        'description': 'kf_local_linear_trend -- category 10-trend-cycle-statespace, method card #58.',
        'args': {'y': 'Handle to a univariate ts· local linear trend (level + slope).', 'seasonal': 'Add a dummy seasonal term.', 'seasonal_period': 'Seasonal period (>=2, <=n)· default frequency(y).'},
        'input_example': {'y': '<series_handle>', 'seasonal': False},
    },
    'kf_trend_cycle': {
        'fn': 'kf_trend_cycle',
        'description': 'kf_trend_cycle -- category 10-trend-cycle-statespace, method card #58.',
        'args': {'y': 'Handle to a univariate ts· trend + stochastic cycle (output gap).', 'cycle_period': 'Cycle length in periods (> 2)· default 8*frequency.', 'seasonal': 'Add a dummy seasonal term.', 'seasonal_period': 'Seasonal period (>=2, <=n)· default frequency(y).'},
        'input_example': {'y': '<series_handle>', 'seasonal': False},
    },
    'mss_dfa': {
        'fn': 'mss_dfa',
        'description': 'mss_dfa -- category 10-trend-cycle-statespace, method card #61.',
        'args': {'data': 'Handle to a mss_prepare_data result (n x T matrix).', 'm': 'Number of common latent factors (<= n).', 'method': 'Optimizer (default kem EM).', 'maxit': 'Maximum iterations.', 'allow_nonconvergence': 'If True, allows a non-converged result (default False = hard gate).'},
        'input_example': {'data': '<raw_handle>', 'm': 1, 'maxit': 5000, 'allow_nonconvergence': False},
    },
    'mss_forecast': {
        'fn': 'mss_forecast',
        'description': 'mss_forecast -- category 10-trend-cycle-statespace, method card #61.',
        'args': {'object': 'Handle to a fitted marssMLE (from mss_dfa).', 'n_ahead': 'Forecast horizon (0 = only in-sample fitted).', 'level': 'Confidence level ∈ (0,1).', 'type': 'Requested quantity (default ytT = smoothed observations).', 'interval': 'Interval type (default prediction).'},
        'input_example': {'object': '<raw_handle>', 'n_ahead': 0, 'level': 0.95},
    },
    'mss_fit_summary': {
        'fn': 'mss_fit_summary',
        'description': 'mss_fit_summary -- category 10-trend-cycle-statespace, method card #61.',
        'args': {'object': 'Handle to a fitted marssMLE (from mss_dfa).', 'tidy': 'If True, adds a long-format parameter table.'},
        'input_example': {'object': '<raw_handle>', 'tidy': False},
    },
    'mss_param_cis': {
        'fn': 'mss_param_cis',
        'description': 'mss_param_cis -- category 10-trend-cycle-statespace, method card #61.',
        'args': {'object': 'Handle to a fitted marssMLE (from mss_dfa).', 'method': 'hessian (default, deterministic)· parametric/innovations = seeded bootstrap.', 'alpha': 'Significance level ∈ (0,1).', 'nboot': 'Bootstrap replications (only parametric/innovations).', 'seed': 'Seed REQUIRED for parametric/innovations bootstrap (determinism).'},
        'input_example': {'object': '<raw_handle>', 'alpha': 0.05, 'nboot': 1000},
    },
    'mss_prepare_data': {
        'fn': 'mss_prepare_data',
        'description': 'mss_prepare_data -- category 10-trend-cycle-statespace, method card #61.',
        'args': {'df': 'Handle to a long DataFrame (series/period/value)· owns the transpose.', 'series_col': 'Series identifier column· None -> auto (series_code/series_name/series).', 'standardize': 'z-score per series (recommended for DFA).'},
        'input_example': {'df': '<df_handle>', 'standardize': False},
    },
    'filt_baxter_king': {
        'fn': 'filt_baxter_king',
        'description': 'filt_baxter_king -- category 10-trend-cycle-statespace, method card #56.',
        'args': {'y': 'Handle to a univariate ts· band-pass Baxter-King (NA at each end).', 'pl': 'Lower cyclical period (>=2)· None -> frequency default.', 'pu': 'Upper cyclical period (> pl)· None -> frequency default.', 'nfix': 'Lead/lag length (NA at each end)· None -> frequency default.', 'type': 'Fixed vs variable length (default fixed).', 'drift': 'Removal of linear drift before the filter.'},
        'input_example': {'y': '<series_handle>', 'drift': False},
    },
    'filt_butterworth': {
        'fn': 'filt_butterworth',
        'description': 'filt_butterworth -- category 10-trend-cycle-statespace, method card #56.',
        'args': {'y': 'Handle to a univariate ts· Butterworth high-pass (full-length).', 'freq': 'Cut-off period (default 10).', 'nfix': 'Filter order (default 2).', 'drift': 'Removal of linear drift before the filter.'},
        'input_example': {'y': '<series_handle>', 'drift': False},
    },
    'filt_christiano_fitzgerald': {
        'fn': 'filt_christiano_fitzgerald',
        'description': 'filt_christiano_fitzgerald -- category 10-trend-cycle-statespace, method card #56.',
        'args': {'y': 'Handle to a univariate ts· Christiano-Fitzgerald band-pass.', 'pl': 'Lower cyclical period (>=2)· None -> frequency default.', 'pu': 'Upper cyclical period (> pl)· None -> frequency default.', 'root': 'Unit-root drift adjustment.', 'drift': 'Removal of linear drift before the filter.', 'type': 'asymmetric (default) = full-length real-time gap (no NA).', 'nfix': 'Fixed lag length (only fixed/baxter-king types).'},
        'input_example': {'y': '<series_handle>', 'root': False, 'drift': False},
    },
    'filt_hp': {
        'fn': 'filt_hp',
        'description': 'filt_hp -- category 10-trend-cycle-statespace, method card #56.',
        'args': {'y': 'Handle to a univariate ts (e.g. 100*log(GDP))· cycle = output gap.', 'freq': "lambda (type='lambda') or cut-off period (type='frequency')· None -> default from the frequency.", 'type': 'Interpretation of freq (default lambda).', 'drift': 'Removal of linear drift before the filter.'},
        'input_example': {'y': '<series_handle>', 'drift': False},
    },
    'filt_trigonometric': {
        'fn': 'filt_trigonometric',
        'description': 'filt_trigonometric -- category 10-trend-cycle-statespace, method card #56.',
        'args': {'y': 'Handle to a univariate ts (EVEN n)· trigonometric band-pass.', 'pl': 'Lower cyclical period (>=2)· None -> frequency default.', 'pu': 'Upper cyclical period (> pl)· None -> frequency default.', 'drift': 'Removal of linear drift before the filter.'},
        'input_example': {'y': '<series_handle>', 'drift': False},
    },
    'np_detrend': {
        'fn': 'np_detrend',
        'description': 'np_detrend -- category 10-trend-cycle-statespace, method card #189.',
        'args': {'y': 'The series (numeric vector, e.g. 100*log(GDP))· without NA, n>=4· cycle = y - trend.', 'x': 'Optional numeric index of the same length (None -> 1..n).', 'method': 'Non-parametric smoother (default loess): loess/smooth.spline/supsmu.', 'span': 'Smoothing fraction ∈ [0,1] for loess/supsmu (loess: >0)· default 0.75.', 'degree': 'loess local polynomial 0/1/2 (default 2).', 'spar': 'smooth.spline smoothing parameter ∈ (0,1.5]· None -> automatic GCV.', 'cv': 'smooth.spline: True -> LOOCV instead of GCV (ignored if spar is given).'},
        'input_example': {'y': [0.5, 0.5], 'span': 0.75, 'degree': 2, 'cv': False},
    },
    'np_output_gap': {
        'fn': 'np_output_gap',
        'description': 'np_output_gap -- category 10-trend-cycle-statespace, method card #189.',
        'args': {'y': 'The series (numeric vector)· without NA, n>=4· gap = deviation from the non-parametric trend.', 'x': 'Optional numeric index of the same length (None -> 1..n).', 'method': 'Non-parametric trend smoother (default loess).', 'mode': 'pct=100*(y-trend)/trend (default)· log=100*(log y - log trend), y&trend>0· level=y-trend.', 'span': 'Smoothing fraction ∈ [0,1] for loess/supsmu (loess: >0)· default 0.75.', 'degree': 'loess local polynomial 0/1/2 (default 2).', 'spar': 'smooth.spline smoothing parameter ∈ (0,1.5]· None -> automatic GCV.', 'cv': 'smooth.spline: True -> LOOCV instead of GCV (ignored if spar is given).'},
        'input_example': {'y': [0.5, 0.5], 'span': 0.75, 'degree': 2, 'cv': False},
    },
    'pf_iterated_filtering': {
        'fn': 'pf_iterated_filtering',
        'description': 'pf_iterated_filtering -- category 10-trend-cycle-statespace, method card #185.',
        'args': {'model': 'Built-in POMP template (same as pf_loglik). ONLY built-in — no user C-code.', 'params': 'Optional named list/vector of initial parameter values (starting point of IF2). Unknown names -> gate error.', 'estimate': 'Character vector of parameter names to estimate (rw.sd perturbation)· None -> the dynamic parameters of the template (the initial-value …_0 are excluded).', 'Nmif': 'Number of IF2 iterations (positive integer)· more = better MLE convergence.', 'Np': 'Number of particles per IF2 iteration (positive integer).', 'cooling_fraction_50': 'Reduction fraction of rw.sd over the first 50 iterations, in (0,1] (cooling schedule).', 'rw_sd_value': 'Random-walk perturbation standard deviation (>0), common to all the estimate parameters.', 'seed': 'Seed for the stochastic IF2 perturbations (reproducibility).'},
        'input_example': {'model': 'gompertz', 'Nmif': 10, 'Np': 500, 'cooling_fraction_50': 0.5, 'rw_sd_value': 0.02, 'seed': 2025},
    },
    'pf_loglik': {
        'fn': 'pf_loglik',
        'description': 'pf_loglik -- category 10-trend-cycle-statespace, method card #185.',
        'args': {'model': 'Built-in POMP template (gompertz=stochastic Gompertz· ricker=Ricker map· ou2=bivariate OU). ONLY built-in — no user C-code.', 'params': 'Optional named list/vector override of the template parameters (e.g. list(r=0.15)). Unknown names -> gate error.', 'Np': 'Number of particles (positive integer)· larger = more accurate loglik, heavier compute.', 'seed': 'Seed for the stochastic particle filter (reproducibility).'},
        'input_example': {'model': 'gompertz', 'Np': 500, 'seed': 2025},
    },
    'stl_tolerant_decompose': {
        'fn': 'stl_tolerant_decompose',
        'description': 'stl_tolerant_decompose -- category 10-trend-cycle-statespace, method card #188.',
        'args': {'x': 'Handle to a univariate ts (or num_array)· STL loess decomposition· tolerates NA.', 'n_p': 'Seasonality period (integer >= 2)· None -> frequency(x) if x is a seasonal ts.', 's_window': '"periodic" (default, constant seasonality) or a positive odd integer >= 7 (seasonal loess span).', 't_window': 'Trend loess span (positive odd integer >= 3)· None -> computed automatically.', 's_degree': 'Seasonal loess degree ∈ {0,1,2}.', 't_degree': 'Trend loess degree ∈ {0,1,2}.', 'inner': 'Inner-loop iterations (positive integer).', 'outer': 'Outer-loop (robustness) iterations (non-negative integer).'},
        'input_example': {'x': '<series_handle>', 's_window': 'periodic', 's_degree': 1, 't_degree': 1, 'inner': 2, 'outer': 1},
    },
    'regdec_decompose': {
        'fn': 'regdec_decompose',
        'description': 'regdec_decompose -- category 10-trend-cycle-statespace, method card #187.',
        'args': {'y': 'Handle to a univariate ts (or msts for multiple/complex seasonality)· the series to decompose.', 'frequency': 'Seasonal frequency (>=2) when y is a numeric vector· ignored for ts/msts.', 'robust': 'Robust STR (M-estimation) — True when outliers/level shifts are present.', 'gapCV': 'Gap length for the CV selection of lambdas· larger -> faster/coarser (None = package default).', 'confidence': 'Confidence level ∈ (0,1) for per-component CIs· None = without CIs (faster).', 'lambdas': 'Fixed smoothing parameters (they bypass the CV)· None = auto via gapCV.', 'seed': 'Determinism seed for the stochastic CV selection of lambdas.'},
        'input_example': {'y': '<series_handle>', 'robust': False, 'confidence': 0.95, 'seed': 2025},
    },
    'regdec_seasadj': {
        'fn': 'regdec_seasadj',
        'description': 'regdec_seasadj -- category 10-trend-cycle-statespace, method card #187.',
        'args': {'object': 'Handle to an STR object (regdec_decompose.object).', 'include': 'Names of the components that are summed (character vector)· None = ["Trend","Random"] = seasonally-adjusted.'},
        'input_example': {'object': '<raw_handle>'},
    },
    'stvp_fit': {
        'fn': 'stvp_fit',
        'description': 'stvp_fit -- category 10-trend-cycle-statespace, method card #183.',
        'args': {'formula': "Regression formula, e.g. 'y ~ x1 + x2' (Intercept is added automatically, as TVP).", 'data': 'Handle to a DataFrame· ALL the formula variables numeric, without NA.', 'mod_type': 'Shrinkage prior: triple (default, triple gamma) / double (NG horseshoe-like) / ridge (without shrinkage).', 'sv': 'Stochastic volatility in the observation variance (sigma2 -> time-varying path).', 'niter': 'Number of MCMC iterations (>=2)· keep SMALL.', 'nburn': 'Burn-in draws (0 <= nburn < niter)· None -> round(niter/2).', 'nthin': 'Thinning (>=1)· (niter-nburn) must be >= nthin.', 'seed': 'RNG seed (required for reproducibility in a stateless node).'},
        'input_example': {'formula': 'y ~ x', 'data': '<df_handle>', 'sv': False, 'niter': 2000, 'nthin': 1, 'seed': 2025},
    },
    'stvp_forecast': {
        'fn': 'stvp_forecast',
        'description': 'stvp_forecast -- category 10-trend-cycle-statespace, method card #183.',
        'args': {'object': "Handle to a fitted 'shrinkTVP' model (from stvp_fit).", 'newdata': 'DataFrame with the RHS covariates for the horizons (numeric, without NA)· nrow >= n.ahead.', 'n_ahead': 'Forecast horizon (integer >=1).'},
        'input_example': {'object': '<raw_handle>', 'newdata': '<df_handle>', 'n_ahead': 1},
    },
    'stvp_lpds': {
        'fn': 'stvp_lpds',
        'description': 'stvp_lpds -- category 10-trend-cycle-statespace, method card #183.',
        'args': {'object': "Handle to a fitted 'shrinkTVP' model (from stvp_fit).", 'data_test': 'DataFrame with EXACTLY one hold-out row (dependent + covariates, numeric).'},
        'input_example': {'object': '<raw_handle>', 'data_test': '<df_handle>'},
    },
    'tvreg_coef': {
        'fn': 'tvreg_coef',
        'description': 'tvreg_coef -- category 10-trend-cycle-statespace, method card #184.',
        'args': {'object': "Handle to a fitted 'tvreg_fit' object (from tvreg_fit.object).", 'exponentiate': 'exp on the coefficients (link-scale -> multiplicative· useful for poisson/binomial).'},
        'input_example': {'object': '<raw_handle>', 'exponentiate': False},
    },
    'tvreg_fit': {
        'fn': 'tvreg_fit',
        'description': 'tvreg_fit -- category 10-trend-cycle-statespace, method card #184.',
        'args': {'formula': "Regression formula AS A STRING (ACE-sanitized), e.g. 'y ~ x1 + x2'· the regressors become time-varying (wrapped automatically in rw1/rw2).", 'data': 'Handle to a TIME-SORTED DataFrame (row = time)· contains response + regressors, WITHOUT NA, >=5 rows.', 'family': 'gaussian -> walker· poisson/binomial -> walker_glm (counts).', 'rw_order': 'Random-walk order of the coefficients: rw1 (level) or rw2 (local linear, with slope).', 'beta_prior': '[mean, sd]: Gaussian prior of the INITIAL time-varying coefficients.', 'sigma_prior': '[shape, rate]: Gamma prior of the walk sd (>0).', 'nu_prior': "[mean, sd]: prior of the initial slope· ONLY for rw_order='rw2'.", 'sigma_y_prior': "[shape, rate]: Gamma prior of the observational sd (>0)· ONLY family='gaussian'.", 'u': 'poisson -> exposures (E(y)=u*exp(x*beta))· binomial -> number of trials· length 1 or n· ONLY glm (default 1).', 'chains': 'Number of HMC chains (SMALL· default 1).', 'iter': 'Iterations per chain (SMALL· default 400, warmup=iter/2).', 'seed': 'Reproducibility seed (seeded + Stan sampler seed).'},
        'input_example': {'formula': 'y ~ x', 'data': '<df_handle>', 'family': 'gaussian', 'rw_order': 'rw1', 'beta_prior': [0.5, 0.5], 'sigma_prior': [0.5, 0.5], 'nu_prior': [0.5, 0.5], 'sigma_y_prior': [0.5, 0.5], 'chains': 1, 'iter': 400, 'seed': 2025},
    },
    'tc_beveridge_nelson': {
        'fn': 'tc_beveridge_nelson',
        'description': 'tc_beveridge_nelson -- category 10-trend-cycle-statespace, method card #476.',
        'args': {'y': 'Series, usually in logs.', 'order': 'ARIMA order; omitted = selected.', 'filter': 'Use the BN filter with a persistence prior.', 'delta': 'Persistence prior for the BN filter.'},
        'input_example': {'y': '<series_handle>', 'filter': False, 'delta': 0.05},
    },
    'tc_uc_stochastic_volatility': {
        'fn': 'tc_uc_stochastic_volatility',
        'description': 'tc_uc_stochastic_volatility -- category 10-trend-cycle-statespace, method card #477.',
        'args': {'y': 'Series.', 'draws': 'Posterior draws.', 'warmup': 'Warm-up draws discarded.', 'trend': 'Trend specification.', 'seed': 'Seed for the random number generator; required for reproducibility.'},
        'input_example': {'y': '<series_handle>', 'draws': 5000, 'warmup': 1000, 'trend': 'local_level', 'seed': 1},
    },
    'tc_mstl': {
        'fn': 'tc_mstl',
        'description': 'tc_mstl -- category 10-trend-cycle-statespace, method card #478.',
        'args': {'y': 'Series.', 'periods': 'Seasonal periods to extract.', 'robust': 'Use outlier-resistant weights.', 'seasonal_smoother': 'Seasonal smoother length per period.', 'iterate': 'Outer iterations.'},
        'input_example': {'y': '<series_handle>', 'periods': [1, 2], 'robust': True, 'iterate': 2},
    },
    'tc_singular_spectrum': {
        'fn': 'tc_singular_spectrum',
        'description': 'tc_singular_spectrum -- category 10-trend-cycle-statespace, method card #479.',
        'args': {'y': 'Series.', 'window_length': 'Embedding window; omitted = a third of the sample.', 'n_components': 'Components to reconstruct.', 'grouping': 'Explicit grouping of singular triples.'},
        'input_example': {'y': '<series_handle>', 'n_components': 3},
    },
    'tc_boosted_hp': {
        'fn': 'tc_boosted_hp',
        'description': 'tc_boosted_hp -- category 10-trend-cycle-statespace, method card #480.',
        'args': {'y': 'Series.', 'lamb': 'Smoothing parameter.', 'stopping': 'Stopping rule.', 'max_iter': 'Maximum boosting rounds.'},
        'input_example': {'y': '<series_handle>', 'lamb': 1600.0, 'stopping': 'bic', 'max_iter': 100},
    },
    'tc_recursive_ls': {
        'fn': 'tc_recursive_ls',
        'description': 'tc_recursive_ls -- category 10-trend-cycle-statespace, method card #481.',
        'args': {'y': 'Dependent variable.', 'x': 'Regressors.', 'start': 'Observations before the first recursive estimate.', 'alpha': 'Significance level.'},
        'input_example': {'y': '<series_handle>', 'x': '<multiseries_handle>', 'alpha': 0.05},
    },
    'tc_uc_correlated': {
        'fn': 'tc_uc_correlated',
        'description': 'tc_uc_correlated -- category 10-trend-cycle-statespace, method card #482.',
        'args': {'y': 'Series.', 'cycle_order': 'Autoregressive order of the cycle.', 'restrict_correlation': 'Impose zero correlation.', 'profile_rho': 'Return the profile likelihood in rho.'},
        'input_example': {'y': '<series_handle>', 'cycle_order': 2, 'restrict_correlation': False, 'profile_rho': True},
    },
    'tc_ensemble_kalman': {
        'fn': 'tc_ensemble_kalman',
        'description': 'tc_ensemble_kalman -- category 10-trend-cycle-statespace, method card #483.',
        'args': {'y': 'Observations.', 'transition': 'State transition matrix.', 'observation': 'Observation matrix.', 'state_cov': 'State noise covariance.', 'obs_cov': 'Observation noise covariance.', 'filter_type': 'Filter variant.', 'ensemble_size': 'Ensemble members.', 'smooth': 'Also run the smoother.', 'seed': 'Seed for the random number generator.'},
        'input_example': {'y': '<multiseries_handle>', 'transition': '<matrix_handle>', 'observation': '<matrix_handle>', 'state_cov': '<matrix_handle>', 'obs_cov': '<matrix_handle>', 'filter_type': 'square_root', 'ensemble_size': 100, 'smooth': True},
    },
}
