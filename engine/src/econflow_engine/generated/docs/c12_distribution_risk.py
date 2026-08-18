# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.v1.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 12-distribution-risk: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'cop_fit': {
        'fn': 'cop_fit',
        'description': 'cop_fit -- category 12-distribution-risk, METHOD-SELECTION card #197.',
        'args': {'data': 'Handle to a matrix of pseudo-observations in [0,1]^d (one column per dimension· apply the pseudo-observation transform to the raw data first).', 'family': 'Copula family (default normal)· clayton=lower-tail, gumbel=upper-tail, t=symmetric tail, normal/frank=without tail dependence.', 'dim': 'Copula dimension = the column count of data (default 2· tail dependence is defined only for dim==2).', 'method': 'Parameter estimator (default mpl = maximum pseudo-likelihood· itau/irho = inversion Kendall/Spearman without optim).'},
        'input_example': {'data': '<matrix_handle>', 'dim': 2},
    },
    'cop_gof': {
        'fn': 'cop_gof',
        'description': 'cop_gof -- category 12-distribution-risk, METHOD-SELECTION card #197.',
        'args': {'object': 'Handle to a fitCopula (from cop_fit)· gives the candidate family/structure for H0.', 'data': 'Handle to a matrix of pseudo-observations in [0,1]^d (same data as the fit).', 'N': 'Parametric bootstrap replications (default 200· STOCHASTIC p-value· keep small).', 'method': 'GoF statistic (default Sn = Cramer-von Mises, Genest-Remillard-Beaudoin 2009).', 'estim_method': 'Estimator re-applied to each bootstrap replicate (default mpl).', 'seed': 'Reproducibility seed of the parametric bootstrap (default 2025).'},
        'input_example': {'object': '<raw_handle>', 'data': '<matrix_handle>', 'N': 200, 'seed': 2025},
    },
    'cop_tail_index': {
        'fn': 'cop_tail_index',
        'description': 'cop_tail_index -- category 12-distribution-risk, METHOD-SELECTION card #197.',
        'args': {'object': 'Handle to a fitCopula (from cop_fit· ONLY bivariate)· returns lower/upper coefficients of tail dependence (the tail-dependence routine).'},
        'input_example': {'object': '<raw_handle>'},
    },
    'er_expectiles': {
        'fn': 'er_expectiles',
        'description': 'er_expectiles -- category 12-distribution-risk, METHOD-SELECTION card #192.',
        'args': {'data': 'Vector of returns/losses (>=20 obs, without NA/Inf, non-constant).', 'tau': 'Intermediate level tau_n in the open (0,1) (e.g. 0.95).', 'tau1': "Extreme level tau'_n in (0,1) & > tau· if given -> extreme expectile prediction, otherwise intermediate.", 'method': 'Estimator: LAWS (direct, default) or QB (quantile-based, depends on the tail index).', 'tailest': "Tail-index estimator when method='QB' (default Hill).", 'var': 'True (default) -> asymptotic variance + CI.', 'varType': 'Asymptotic variance type: asym-Ind (independent, default) or asym-Dep (serial dependence -> requires blocks).', 'bias': 'Bias correction (only extreme/predExpectiles· default False).', 'bigBlock': 'big-block size for the asym-Dep variance (< n).', 'smallBlock': 'small-block size for the asym-Dep variance (< bigBlock).', 'k': 'Intermediate sequence k_n in 1..n-1 (order statistics)· if None, it is driven by tau.', 'alpha': 'CI significance level (1-alpha)· default 0.05.'},
        'input_example': {'data': [0.5, 0.5], 'tau': 0.5, 'var': True, 'bias': False, 'alpha': 0.05},
    },
    'er_mes': {
        'fn': 'er_mes',
        'description': 'er_mes -- category 12-distribution-risk, METHOD-SELECTION card #192.',
        'args': {'data': 'series1 = the variable of interest (whose loss is measured).', 'data2': 'series2 = the condition· MES = E[series1 | series2 at an extreme level] (same length as data).', 'tau': 'Intermediate level tau_n in (0,1).', 'tau1': "Extreme level tau'_n in (0,1) & > tau (systemic event level).", 'estimator': 'quantile -> QuantMES (default)· expectile -> ExpectMES.', 'method': 'Estimator for ExpectMES (ignored in the quantile MES· default LAWS).', 'var': 'True (default) -> asymptotic variance + CI.', 'varType': 'asym-Ind (default) or asym-Dep (serial dependence -> requires blocks).', 'bias': 'Bias correction (default False).', 'bigBlock': 'big-block size for the asym-Dep variance (< n).', 'smallBlock': 'small-block size for the asym-Dep variance (< bigBlock).', 'k': 'Intermediate sequence k_n in 1..n-1· if None, it is driven by tau.', 'alpha': 'CI significance level (1-alpha)· default 0.05.'},
        'input_example': {'data': [0.5, 0.5], 'data2': [0.5, 0.5], 'tau': 0.5, 'tau1': 0.5, 'var': True, 'bias': False, 'alpha': 0.05},
    },
    'er_tail_index': {
        'fn': 'er_tail_index',
        'description': 'er_tail_index -- category 12-distribution-risk, METHOD-SELECTION card #192.',
        'args': {'data': 'Vector of returns/losses (>=20 obs, without NA/Inf, non-constant).', 'k': 'Intermediate sequence k_n for the Hill estimator in 1..n-1 (number of top order statistics).', 'tau': 'Intermediate level in (0,1) for the expectile-based estimator (EBTailIndex)· if None, only the Hill is returned.', 'var': 'True (default) -> asymptotic variance + CI of the Hill gamma.', 'varType': 'asym-Ind (default) or asym-Dep (serial dependence -> requires blocks).', 'bias': 'Bias-corrected Hill (default False).', 'bigBlock': 'big-block size for the asym-Dep variance (< n).', 'smallBlock': 'small-block size for the asym-Dep variance (< bigBlock).', 'alpha': 'CI significance level (1-alpha)· default 0.05.'},
        'input_example': {'data': [0.5, 0.5], 'k': 1, 'var': True, 'bias': False, 'alpha': 0.05},
    },
    'es_backtest': {
        'fn': 'es_backtest',
        'description': 'es_backtest -- category 12-distribution-risk, METHOD-SELECTION card #194.',
        'args': {'r': 'Vector of realized returns (without NA).', 'q': 'Vector of VaR forecasts of the same length as r (typically negative).', 'e': 'Vector of Expected Shortfall forecasts of the same length as r (typically negative, more extreme than q).', 'alpha': 'Probability level in the open (0,1), e.g. 0.025.', 'version': '1=Strict ESR (default)· 2=Auxiliary ESR (regress on q & e)· 3=Strict Intercept (+ one-sided p-values).', 'B': 'Number of bootstrap samples· 0 = without bootstrap (default). >0 -> fills the pvalue_*_bootstrap.', 'sparsity': 'Sparsity estimator in Lambda (cov_config, default nid).', 'sigma_est': 'Sigma estimator in the sandwich (cov_config, default scl_sp).', 'misspec': 'If True (default) the estimator accounts for possible misspecification (cov_config).', 'seed': 'Reproducibility seed for the bootstrap when B>0 (default 2025).'},
        'input_example': {'r': [0.5, 0.5], 'q': [0.5, 0.5], 'e': [0.5, 0.5], 'alpha': 0.5, 'B': 0, 'misspec': True, 'seed': 2025},
    },
    'es_joint_reg': {
        'fn': 'es_joint_reg',
        'description': 'es_joint_reg -- category 12-distribution-risk, METHOD-SELECTION card #194.',
        'args': {'formula': "Joint (VaR,ES) formula· supports two-part 'y ~ xq | xe' (1st part = quantile/VaR equation, 2nd = ES)· a single set -> shared by both.", 'data': 'Handle to a DataFrame with the response and the regressors (without NA in the variables).', 'alpha': 'Probability level in the open (0,1), e.g. 0.025 (2.5% VaR/ES).', 'g1': 'Specification function G1 of the quantile equation· 2=G1(z)=0 (default), 1=G1(z)=z.', 'g2': 'Specification function G2 of the ES equation (default 1)· types 1-3 require negative ES values.', 'early_stopping': 'Stop the iterated local search if there is no improvement within this many steps (default 10).', 'seed': 'Reproducibility seed for the ILS optimization (default 2025).'},
        'input_example': {'formula': 'y ~ x', 'data': '<df_handle>', 'alpha': 0.5, 'early_stopping': 10, 'seed': 2025},
    },
    'esg_martingale_test': {
        'fn': 'esg_martingale_test',
        'description': 'esg_martingale_test -- category 12-distribution-risk, METHOD-SELECTION card #199.',
        'args': {'object': 'Handle to esg_simdiff$object (list model/params/T/time/paths). Gate: model ∈ {vasicek,cir} (only these have a closed-form bond price).', 'conf_level': 'Confidence level of the MC interval for the within_ci check, in (0,1) (default 0.95).'},
        'input_example': {'object': '<raw_handle>', 'conf_level': 0.95},
    },
    'esg_simdiff': {
        'fn': 'esg_simdiff',
        'description': 'esg_simdiff -- category 12-distribution-risk, METHOD-SELECTION card #199.',
        'args': {'model': 'SDE model (CLOSED set· default vasicek): vasicek/ou short-rate mean-reverting, cir positive short-rate, gbm asset. drift/diffusion HARD-CODED (NEVER an eval string).', 'params': 'Named list of parameters per model: vasicek/ou {theta,mu,sigma,x0}· cir {kappa,theta,sigma,x0}· gbm {mu,sigma,x0}. sigma>0, speed>0, gbm x0>0, cir x0>=0 (gates).', 'T': 'Horizon (time) of the simulation, >0 (default 1).', 'n_steps': 'Number of grid steps, >=2· the paths matrix has n_steps+1 rows (default 100).', 'n_paths': 'Number of simulated paths, >=2 (columns of the matrix· default 200).', 'seed': 'Reproducibility seed (the simulation is stochastic· default 2025).'},
        'input_example': {'params': '...', 'T': 1, 'n_steps': 100, 'n_paths': 200, 'seed': 2025},
    },
    'evt_fevd': {
        'fn': 'evt_fevd',
        'description': 'evt_fevd -- category 12-distribution-risk, METHOD-SELECTION card #191.',
        'args': {'x': 'Numeric series: block maxima (GEV/Gumbel) or the whole series for threshold-exceedances (GP/PP/Exponential).', 'type': 'EVT family: GEV=block-maxima (default)· GP/PP/Exponential=threshold-exceedances (they require a threshold)· Gumbel=block-maxima with shape=0.', 'method': 'Estimator: MLE (default)· GMLE (Beta-prior/penalty on the shape)· Lmoments (ONLY GEV/GP). Bayesian is NOT exposed.', 'threshold': 'Single threshold u for GP/PP/Exponential (< max(x)· >=5 exceedances). Ignored for GEV/Gumbel.', 'time_units': "DETERMINES npy (e.g. 'days'->365.25, 'months'->12, '12/year') — i.e. the BASIS of the return periods in threshold models.", 'period_basis': "Return period unit (default 'year')."},
        'input_example': {'x': [0.5, 0.5], 'type': 'GEV', 'method': 'MLE', 'time_units': 'days', 'period_basis': 'year'},
    },
    'evt_return_level': {
        'fn': 'evt_return_level',
        'description': 'evt_return_level -- category 12-distribution-risk, METHOD-SELECTION card #191.',
        'args': {'object': 'Handle to an fevd fit (from evt_fevd$object).', 'return_periods': 'Vector of return periods in period_basis units· each value > 1 (default [10,50,100]).', 'do_ci': 'True (default) -> normal-approx (delta) CIs· False -> only point estimates.', 'conf_level': 'Confidence level in (0,1) for the CIs (default 0.95).'},
        'input_example': {'object': '<raw_handle>', 'do_ci': True, 'conf_level': 0.95},
    },
    'evt_threshold_diag': {
        'fn': 'evt_threshold_diag',
        'description': 'evt_threshold_diag -- category 12-distribution-risk, METHOD-SELECTION card #191.',
        'args': {'x': 'Numeric series for threshold-selection diagnostics (mean residual life + parameter stability).', 'type': 'Model for the parameter-stability grid (default GP).', 'nint': 'Number of points in the threshold grid (>=2· default 10).', 'alpha': 'Significance level for the pointwise CIs (default 0.05).', 'r': 'Threshold range [r1,r2] (r1<r2<max(x)) for the stability grid (default: quantiles 0.75..0.99 of x).'},
        'input_example': {'x': [0.5, 0.5], 'type': 'GP', 'nint': 10, 'alpha': 0.05},
    },
    'exr_expectile': {
        'fn': 'exr_expectile',
        'description': 'exr_expectile -- category 12-distribution-risk, METHOD-SELECTION card #193.',
        'args': {'x': 'Numeric vector (series of returns/losses) without NA.', 'probs': 'Vector of expectile levels in [0,1]· passed WHOLE (default [0.05,0.5,0.95]· 0.5 = the mean).', 'dec': 'Rounding decimals of the expectiles (default 4).'},
        'input_example': {'x': [0.5, 0.5], 'dec': 4},
    },
    'exr_expectile_reg': {
        'fn': 'exr_expectile_reg',
        'description': 'exr_expectile_reg -- category 12-distribution-risk, METHOD-SELECTION card #193.',
        'args': {'formula': "Expectile-regression formula, e.g. 'growth ~ fci + slack' (response ~ covariates).", 'data': 'Handle to a DataFrame (data-agnostic· time-sorted for the GaR interpretation).', 'estimate': 'Expectile estimation strategy (default laws· restricted/bundle/sheets forbid crossing).', 'smooth': "Selection of the smoothing penalty lambda (default schall· 'fixed' -> use lambda as is).", 'lambda': "Positive smoothing parameter· active when smooth='fixed' (default 1).", 'expectiles': 'Vector of expectile levels in the open (0,1)· passed WHOLE (e.g. [0.05,0.5,0.95]). If missing -> default set 0.01..0.99.', 'seed': 'Reproducibility seed (defensive· deterministic fit) (default 2025).'},
        'input_example': {'formula': 'y ~ x', 'data': '<df_handle>', 'lambda': 1, 'seed': 2025},
    },
    'fd_bootdist': {
        'fn': 'fd_bootdist',
        'description': 'fd_bootdist -- category 12-distribution-risk, METHOD-SELECTION card #196.',
        'args': {'object': 'Handle to a fitdist fit (from fd_fit)· bootstrap CIs of the parameters.', 'bootmethod': 'param (default· simulate from the fitted) or nonparam (resample of the data).', 'niter': 'Number of bootstrap replications (>=10· default 200).', 'seed': 'Reproducibility seed (default 2025).'},
        'input_example': {'object': '<raw_handle>', 'niter': 200, 'seed': 2025},
    },
    'fd_descdist': {
        'fn': 'fd_descdist',
        'description': 'fd_descdist -- category 12-distribution-risk, METHOD-SELECTION card #196.',
        'args': {'data': 'Vector of numbers· >=4 values, without NA/Inf. Returns Cullen-Frey descriptives (NUMBERS, no plot at all).', 'discrete': 'True if the data are discrete/counts (default False).', 'method': 'Estimator skewness/kurtosis (default unbiased).', 'boot': 'Number of bootstrap samples for the skewness/kurtosis cloud (chart-data· >=10 active· None/0 = without).', 'seed': 'Reproducibility seed for the bootstrap cloud (default 2025).'},
        'input_example': {'data': [0.5, 0.5], 'discrete': False, 'boot': 200, 'seed': 2025},
    },
    'fd_fit': {
        'fn': 'fd_fit',
        'description': 'fd_fit -- category 12-distribution-risk, METHOD-SELECTION card #196.',
        'args': {'data': 'Vector of numbers (returns/losses/counts)· >=4 values, without NA/Inf, with variance.', 'distr': 'Distribution family (closed set· default norm). The support is checked (positive>0· beta∈(0,1)· pois/nbinom non-negative integers).', 'method': 'Estimator: mle (default)· mme (moments)· qme (quantile matching — requires probs)· mge (max GOF distance).', 'probs': "Probabilities in (0,1) for method='qme' (e.g. [0.333,0.667])· ignored elsewhere.", 'gof': "GOF-distance measure for method='mge' (default CvM)· ignored elsewhere.", 'fix_arg': 'Optional named list of fixed parameters (e.g. {rate:1}) that are NOT estimated.'},
        'input_example': {'data': [0.5, 0.5]},
    },
    'fd_gof': {
        'fn': 'fd_gof',
        'description': 'fd_gof -- category 12-distribution-risk, METHOD-SELECTION card #196.',
        'args': {'object': 'Handle to a fitdist fit (from fd_fit). Continuous -> KS/CvM/AD· discrete -> chisq (KS/CvM/AD = NA).'},
        'input_example': {'object': '<raw_handle>'},
    },
    'pa_component_var': {
        'fn': 'pa_component_var',
        'description': 'pa_component_var -- category 12-distribution-risk, METHOD-SELECTION card #65.',
        'args': {'returns': 'Handle to a MULTIVARIATE returns matrix (>=2 assets).', 'weights': 'Vector of portfolio weights of length the column count of the reference, sum ~ 1 (e.g. [0.5,0.5]).', 'p': 'Confidence level in (0,1) (default 0.95).', 'method': 'Estimator with a CONSISTENT (additive) Euler decomposition (default gaussian).'},
        'input_example': {'returns': '<matrix_handle>', 'weights': 0.5, 'p': 0.95},
    },
    'pa_downside_risk': {
        'fn': 'pa_downside_risk',
        'description': 'pa_downside_risk -- category 12-distribution-risk, METHOD-SELECTION card #65.',
        'args': {'returns': 'Handle to a returns series/matrix (one column per asset).', 'MAR': 'Minimum acceptable return for downside/Sortino (default 0).', 'p': 'Confidence level for the historical VaR/ES of the summary (default 0.95).'},
        'input_example': {'returns': '<matrix_handle>', 'MAR': 0, 'p': 0.95},
    },
    'pa_expected_shortfall': {
        'fn': 'pa_expected_shortfall',
        'description': 'pa_expected_shortfall -- category 12-distribution-risk, METHOD-SELECTION card #65.',
        'args': {'returns': 'Handle to a returns series/matrix (one column per asset).', 'p': 'Confidence level in (0,1) (default 0.95).', 'method': 'Estimator ES/CVaR (default historical· modified = Cornish-Fisher).', 'clean': 'Outlier cleaning (default none).', 'invert': 'False (default) -> positive loss magnitude· True -> signed return-space quantile.'},
        'input_example': {'returns': '<matrix_handle>', 'p': 0.95, 'invert': False},
    },
    'pa_returns_from_long': {
        'fn': 'pa_returns_from_long',
        'description': 'pa_returns_from_long -- category 12-distribution-risk, METHOD-SELECTION card #65.',
        'args': {'data': 'Handle to a long DataFrame (columns period/value).', 'period_col': "Date column name (default 'period').", 'value_col': "Value column name (default 'value')."},
        'input_example': {'data': '<df_handle>', 'period_col': 'period', 'value_col': 'value'},
    },
    'pa_var': {
        'fn': 'pa_var',
        'description': 'pa_var -- category 12-distribution-risk, METHOD-SELECTION card #65.',
        'args': {'returns': 'Handle to a returns series/matrix (one column per asset).', 'p': 'Confidence level in (0,1) (default 0.95).', 'method': 'Estimator VaR (default historical· modified = Cornish-Fisher).', 'clean': 'Outlier cleaning (default none).', 'invert': 'False (default) -> positive loss magnitude· True -> signed return-space quantile.'},
        'input_example': {'returns': '<matrix_handle>', 'p': 0.95, 'invert': False},
    },
    'qr_conditional_quantiles': {
        'fn': 'qr_conditional_quantiles',
        'description': 'qr_conditional_quantiles -- category 12-distribution-risk, METHOD-SELECTION card #64.',
        'args': {'object': 'Handle to an rq/rqs fit (from qr_regression / qr_growth_at_risk).', 'newdata': 'Optional handle to a DataFrame for prediction (default: training frame).'},
        'input_example': {'object': '<raw_handle>'},
    },
    'qr_growth_at_risk': {
        'fn': 'qr_growth_at_risk',
        'description': 'qr_growth_at_risk -- category 12-distribution-risk, METHOD-SELECTION card #64.',
        'args': {'formula': "GaR formula outcome ~ conditions, e.g. 'growth ~ fci'.", 'data': 'Handle to a DataFrame (time-sorted for h-lead alignment).', 'newdata': 'Optional forecast point (default: the last conditions x_T).', 'tau': 'Vector of quantile levels in (0,1)· passed WHOLE (must contain risk_tau).', 'risk_tau': 'Downside quantile = Growth-at-Risk (one of the tau· default 0.05).', 'h': 'Horizon of h steps· y_{t+h} ~ x_t (default 0 = contemporaneous).', 'method': 'rq solver (default br).', 'se': 'Inference for std errors (default nid).', 'boot_replications': "Bootstrap replications when se='boot' (default 200).", 'seed': 'Reproducibility seed (default 42).'},
        'input_example': {'formula': 'y ~ x', 'data': '<df_handle>', 'risk_tau': 0.05, 'h': 0, 'boot_replications': 200, 'seed': 42},
    },
    'qr_regression': {
        'fn': 'qr_regression',
        'description': 'qr_regression -- category 12-distribution-risk, METHOD-SELECTION card #64.',
        'args': {'formula': "Quantile-regression formula, e.g. 'growth ~ fci + slack'.", 'data': 'Handle to a DataFrame (data-agnostic· no column renaming).', 'tau': 'Vector of quantile levels in the open (0,1)· passed WHOLE (e.g. [0.05,0.25,0.5,0.75,0.95]).', 'method': 'rq solver (default br).', 'se': 'Inference for std errors (default nid).', 'boot_replications': "Bootstrap replications when se='boot' (default 200).", 'seed': "Reproducibility seed for se='boot' (default 42)."},
        'input_example': {'formula': 'y ~ x', 'data': '<df_handle>', 'boot_replications': 200, 'seed': 42},
    },
    'qr_slope_equality': {
        'fn': 'qr_slope_equality',
        'description': 'qr_slope_equality -- category 12-distribution-risk, METHOD-SELECTION card #64.',
        'args': {'object': 'Handle to an rqs fit with >=2 tau (anova.rq: equality of slopes across quantiles).'},
        'input_example': {'object': '<raw_handle>'},
    },
    'qrf_fit': {
        'fn': 'qrf_fit',
        'description': 'qrf_fit -- category 12-distribution-risk, METHOD-SELECTION card #195.',
        'args': {'x': 'Handle to a matrix/DataFrame of predictors (one column per covariate· without NA).', 'y': 'Numeric response vector of length the row count of x (e.g. growth)· NOT factor, without NA.', 'ntree': 'Number of trees in the forest (default 200· small/deterministic).', 'nodesize': 'Minimum terminal node size (default 5· randomForest regression).', 'mtry': 'Predictors tried per split (default floor(p/3))· must be <= the column count of x.', 'seed': 'Reproducibility seed for the stochastic fit (default 2025).'},
        'input_example': {'x': '<matrix_handle>', 'y': [0.5, 0.5], 'ntree': 200, 'nodesize': 5, 'seed': 2025},
    },
    'qrf_predict': {
        'fn': 'qrf_predict',
        'description': 'qrf_predict -- category 12-distribution-risk, METHOD-SELECTION card #195.',
        'args': {'object': 'Handle to a quantregForest fit (from qrf_fit).', 'newdata': 'Handle to a matrix/DataFrame of new predictors (same columns as the training· without NA).', 'quantiles': 'Vector of quantile levels in [0,1]· passed WHOLE (e.g. [0.05,0.5,0.95]).'},
        'input_example': {'object': '<raw_handle>', 'newdata': '<matrix_handle>', 'quantiles': [0.5, 0.5]},
    },
    'st_density': {
        'fn': 'st_density',
        'description': 'st_density -- category 12-distribution-risk, METHOD-SELECTION card #95.',
        'args': {'fit': 'Handle to a skew-t fit/dp (from st_fit_quantiles).', 'n': 'Number of pdf/cdf grid points (default 512).'},
        'input_example': {'fit': '<raw_handle>', 'n': 512},
    },
    'st_fit_quantiles': {
        'fn': 'st_fit_quantiles',
        'description': 'st_fit_quantiles -- category 12-distribution-risk, METHOD-SELECTION card #95.',
        'args': {'probs': 'Vector of probabilities in (0,1), strictly increasing (>=4 points).', 'quantiles': 'Vector of fitted quantiles (strictly increasing· same length as probs).', 'fix_nu': 'Optionally fix the degrees of freedom nu (>2).', 'weights': 'Optional positive weights of length length(probs) for the SSE.', 'method': 'optim method (default Nelder-Mead).', 'maxit': 'Maximum optim iterations (default 2000).'},
        'input_example': {'probs': 0.5, 'quantiles': 0.5, 'maxit': 2000},
    },
    'st_shortfall': {
        'fn': 'st_shortfall',
        'description': 'st_shortfall -- category 12-distribution-risk, METHOD-SELECTION card #95.',
        'args': {'fit': 'Handle to a skew-t fit/dp (from st_fit_quantiles).', 'prob': 'Tail probability for VaR/ES (default 0.05).', 'side': 'left = downside ES (default)· right = upside.'},
        'input_example': {'fit': '<raw_handle>', 'prob': 0.05},
    },
    'vine_loglik': {
        'fn': 'vine_loglik',
        'description': 'vine_loglik -- category 12-distribution-risk, METHOD-SELECTION card #198.',
        'args': {'object': 'Handle to an RVineMatrix (from vine_select).', 'data': 'Handle to a matrix of pseudo-observations of the SAME dimension as the vine (in [0,1], without NA).', 'separate': 'False (default) -> total loglik· True -> per-observation vector.'},
        'input_example': {'object': '<raw_handle>', 'data': '<matrix_handle>', 'separate': False},
    },
    'vine_select': {
        'fn': 'vine_select',
        'description': 'vine_select -- category 12-distribution-risk, METHOD-SELECTION card #198.',
        'args': {'data': 'Handle to a matrix of pseudo-observations (>=2 columns, ALL in [0,1], without NA· do the PIT/rank-transform first).', 'familyset': 'Permitted copula families (BiCop codes· default curated: 0/1/2/3/4/5/6 + rotations). Leave it unset for all.', 'type': 'Vine type: RVine (regular, default) or CVine (canonical).', 'selectioncrit': 'Pair-copula selection criterion (default AIC).', 'indeptest': 'Preliminary independence test per pair (default False).', 'level': 'Significance level of the indeptest in (0,1) (default 0.05).', 'trunclevel': 'Truncation: keep only the first k trees (NA = no truncation).', 'rotations': 'Include rotated versions (90/180/270) of the families (default True).', 'method': "Parameter estimation: mle (default) or itau (inversion of Kendall's tau)."},
        'input_example': {'data': '<matrix_handle>', 'indeptest': False, 'level': 0.05, 'rotations': True},
    },
    'vine_sim': {
        'fn': 'vine_sim',
        'description': 'vine_sim -- category 12-distribution-risk, METHOD-SELECTION card #198.',
        'args': {'object': 'Handle to an RVineMatrix (from vine_select).', 'N': 'Number of pseudo-observations to simulate (positive integer).', 'seed': 'Reproducibility seed (STOCHASTIC· default 2025).'},
        'input_example': {'object': '<raw_handle>', 'N': 1, 'seed': 2025},
    },
}
