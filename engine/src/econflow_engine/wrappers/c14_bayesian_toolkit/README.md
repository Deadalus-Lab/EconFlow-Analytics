<!-- SPDX-License-Identifier: AGPL-3.0-only -->
# 14-bayesian-toolkit

8 METHOD-SELECTION cards, 8 modules, 29 nodes.

Every card below governs one wrapper module in this package. The cards are the
reason a method exists here at all: they record when it applies, what to reach
for instead, and the traps that make its output easy to misread.

## #68 — General Bayesian inference via Stan (NUTS-only + convergence gate)

**Module:** `general_bayesian_inference.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `rs_syntax_check` | `model_code` | `string`, `string` | `model_name='anon_model'` | `light` | — |
| `rs_compile` | `model_code` | `string`, `string` | `model_name='anon_model'` | `light` | `model` |
| `rs_sample` | `model`, `data`, `seed` | `raw_handle`, `raw_handle`, `integer`, `integer`, `integer`, `enum`, `number`, `number`, `boolean` | `chains=2`, `iter=1000`, `rhat_max=1.01`, `ess_min=400`, `allow_nonconvergence=False` | `mcmc` | — |
| `rs_fit` | `model_code`, `data`, `seed` | `string`, `raw_handle`, `string`, `integer`, `integer`, `integer`, `boolean` | `model_name='anon_model'`, `chains=2`, `iter=1000`, `allow_nonconvergence=False` | `mcmc` | — |

### Use when

an arbitrary generative model in the Stan DSL (custom likelihood/hierarchical/state-space); NUTS + a hard convergence gate

### Do not use when

a regression formula -> #69 brms; BUGS-style -> #70 nimble; a ready-made package (BVAR/SV); MAP/ADVI (optimizing/vb)

### Alternatives

| instead use | when |
| --- | --- |
| #69 brms | the model can be expressed as a formula (linear/GLM/hierarchical) |
| #70 nimble | BUGS syntax / discrete latent states / custom samplers |
| BVAR/bvarsv (cat. 03) | a ready-made Bayesian VAR — do not rewrite it in Stan |
| optimizing/vb | you want a fast MAP/ADVI instead of a full posterior (out of scope) |

### Output fields

- summary: data_frame per parameter (mean/se_mean/sd/quantiles/n_eff/Rhat)
- diagnostics.max_rhat: rank-normalized split-R-hat FROM monitor (the convergence decision)
- diagnostics.min_bulk_ess / min_tail_ess: Bulk/Tail ESS from monitor
- diagnostics.num_divergent: divergent transitions (>0 = a biased posterior)
- converged (lgl) + nonconvergence_reasons (chr); object=stanfit (stubbed)

### Pitfalls

- the Rhat/n_eff column of summary is the CLASSIC diagnostic, which UNDERSTATES non-convergence — read diagnostics.max_rhat (monitor)
- an empty/whitespace model_code compiles SILENTLY (stanc status==TRUE) -> pre-gate
- NA/NaN/Inf or a missing variable in data -> fit@mode==2 SILENTLY (universal post-gate)
- chains>=1 is not enough: a split-R-hat from one chain -> converged=TRUE on a bimodal model (chains>=2 is mandatory)
- the seed is MANDATORY: the conventional set.seed does NOT affect the Stan RNG; the default is RANDOM

### References

- Hoffman & Gelman 2014 (NUTS, JMLR 15)
- Carpenter et al 2017 (Stan, JSS 76(1))
- Vehtari et al 2021 (rank-normalized split-R-hat + Bulk/Tail ESS, Bayesian Analysis 16(2))
- Gelman et al 2013 (BDA3)

## #69 — Bayesian regression models

**Module:** `bayesian_regression.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `br_fit` | `formula`, `data`, `seed` | `formula`, `df_handle`, `enum`, `raw_handle`, `integer`, `integer`, `integer`, `number`, `number`, `boolean` | `chains=2`, `iter=1000`, `rhat_threshold=1.01`, `neff_ratio_threshold=0.1`, `allow_nonconvergence=False` | `mcmc` | — |
| `br_set_prior` | `prior` | `string`, `string` | `class='b'` | `light` | — |
| `br_make_formula` | `formula` | `formula` | — | `light` | — |

### Use when

Bayesian regression as a formula (gaussian/student/bernoulli/poisson/negbinomial/Gamma/lognormal) + informative priors; NUTS + a convergence gate

### Do not use when

a custom generative model -> #68 rstan; BUGS/discrete -> #70 nimble; frequentist estimation suffices (plm/OLS); multilevel/loo/splines/GP (outside v1)

### Alternatives

| instead use | when |
| --- | --- |
| #68 rstan | the model is not a regression (custom likelihood/state-space) |
| plm FE/RE (cat. 08) | panel regression, frequentist estimation + Hausman |
| quantreg GaR (cat. 12) | conditional quantiles (growth-at-risk), not a posterior mean |
| brms multilevel (1\|g) | hierarchical shrinkage — omitted in v1, re-scope |

### Output fields

- summary: posterior_summary data_frame (parameter/Estimate/Est.Error/Q2.5/Q97.5)
- fixed: fixef data_frame (population-level coefficients + credible intervals)
- diagnostics: max_rhat/min_neff_ratio/n_divergent/n_max_treedepth + echoed family/config
- converged (lgl) + nonconvergence_reasons (chr); prior=prior_summary df; object=brmsfit (stubbed)

### Pitfalls

- family AS A STRING: Gamma gives an INVERSE link whereas the brms canonical one is LOG (a silent change of model)
- data that is NOT a data_frame -> a SILENT as_matrix coercion; NA in model columns -> SILENT listwise deletion
- all-NA R-hat/neff (too few retained draws) -> -Inf/+Inf is caught as HARD non-convergence (otherwise it passes vacuously)
- Est.Error = the posterior SD (NOT a frequentist SE); the uncertainty is the credible interval Q2.5/Q97.5
- the accessors rhat/neff_ratio/fixef/prior_summary are masked (posterior/bayesplot/nlme) -> getS3method brmsfit

### References

- Bürkner 2017 (brms, JSS 80(1))
- Bürkner 2018 (brms multilevel, 10(1))
- Vehtari et al 2021 (rank-normalized R-hat/ESS)

## #70 — General BUGS-style Bayesian MCMC (injection-safe)

**Module:** `general_bugs_style.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `nim_bayes_mcmc` | `code`, `inits`, `monitors`, `seed` | `string`, `raw_handle`, `series_codes`, `raw_handle`, `raw_handle`, `integer`, `integer`, `integer`, `integer`, `integer`, `number`, `number`, `boolean` | `niter=2000`, `nburnin=1000`, `nchains=2`, `thin=1`, `rhat_threshold=1.1`, `ess_min=100`, `allow_nonconvergence=False` | `mcmc` | — |

### Use when

a model in BUGS/JAGS syntax (discrete latent variables/mixtures/custom nodes); injection-safe build + a Gelman R-hat/ESS gate

### Do not use when

pure Stan -> #68 rstan (NUTS is more efficient); a regression formula -> #69 brms; WAIC/HMC/SMC/custom samplers (out of scope)

### Alternatives

| instead use | when |
| --- | --- |
| #68 rstan | continuous parameters, you want efficient NUTS |
| #69 brms | a regression formula, you do not want BUGS |
| #72 coda | you ALREADY have draws, only diagnostics are needed |

### Output fields

- summary: run.summary.all.chains (Mean/Median/StDev/credible quantiles, pooled)
- convergence.rhat: gelman psrf matrix [Point est./Upper C.I.] + mpsrf + ess
- convergence.max_rhat/min_ess/converged; nonconvergence_reasons (chr)
- samples: list(chains=matrices, nodes); per_chain_summary; metadata (seed/set_seed/config)
- object: compiled model/mcmc/samples (stubbed)

### Pitfalls

- INJECTION-SAFE: NEVER eval(parse(paste0('nimbleCode({',code,'})'))) — a brace-break payload = RCE; parse ONLY
- an NA in data -> nimble SILENTLY treats it as a MISSING node to be imputed (a hidden parameter); clean the data first
- setSeed must be a VECTOR seed+0.(nchains-1); a FRESH compiled pipeline (reusing Cmcmc = non-reproducible)
- inits must cover ALL top-level stochastic parameters (otherwise an NA start -> NaN samples)
- the default rhat_threshold=1.1 is looser than the 1.01 of rstan/brms (a BUGS legacy)

### References

- de Valpine et al 2017 (nimble, JCGS 26(2))
- Lunn et al 2000 (BUGS language)
- Gelman & Rubin 1992 (R-hat, Stat. Science 7(4))

## #71 — Posterior R-hat / ESS diagnostics + summaries

**Module:** `posterior_hat_ess.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `post_summarise_draws` | `x` | `raw_handle`, `boolean` | `include_mcse=False` | `light` | — |

### Use when

for ANY MCMC draws: rank-normalized split-R-hat + Bulk/Tail ESS + mean/median/sd/mad/quantiles/MCSE per parameter

### Do not use when

you want Geweke/Raftery/Heidel/HPD/ACF -> #72 coda; chart data -> #73 bayesplot; the engine already produced the diagnostics

### Alternatives

| instead use | when |
| --- | --- |
| #72 coda | you want Geweke z / Raftery-Lewis / Heidel / HPD / autocorrelation |
| #73 bayesplot | you want rating tables / chart data for R-hat/neff |
| engine diagnostics (#68-70) | the fit object already contains R-hat/ESS |

### Output fields

- summary: draws_summary df per variable (mean/median/sd/mad/quantiles/rhat/ess_bulk/ess_tail[/mcse_mean])
- nchains/niterations/ndraws/nvariables; variables (chr); probs
- degenerate_variables: variables with an NA R-hat on finite draws (zero variance)
- draws: draws_array

### Pitfalls

- MASKING: rhat/ess_bulk/ess_tail/sd/mad are masked -> pass posterior::* BY VALUE (NEVER strings/default_*_measures -> R-hat=999 garbage)
- a 2D matrix/data_frame input is converted SILENTLY into 1 chain; nchains>=2 is required (a split-R-hat of ~1.0 is silent)
- ess_bulk = the reliability of the central estimates; ess_tail = the reliability of the credible-interval edges (a low tail ESS -> bad quantiles)
- R-hat>1.01 = non-convergence (Vehtari 2021); the wrapper does NOT gate on a threshold (a valid diagnostic, not an error)
- an NA R-hat ≠ an error — it is a constant parameter (degenerate_variables)

### References

- Vehtari et al 2021 (rank-normalized split-R-hat + Bulk/Tail ESS + MCSE, Bayesian Analysis 16(2))
- posterior package (Bürkner/Gabry/Kay/Vehtari)

## #72 — MCMC convergence diagnostics (Gelman/Geweke/Raftery/Heidel/ESS/HPD/ACF)

**Module:** `mcmc_convergence_diagnostics.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `coda_diagnostics` | `chains` | `raw_handle`, `number`, `number` | `confidence=0.95`, `prob=0.95` | `mcmc` | — |
| `coda_gelman` | `chains` | `raw_handle`, `number` | `confidence=0.95` | `mcmc` | — |
| `coda_geweke` | `chains` | `raw_handle`, `number`, `number` | `frac1=0.1`, `frac2=0.5` | `mcmc` | — |
| `coda_effective_size` | `chains` | `raw_handle` | — | `mcmc` | — |
| `coda_hpd_interval` | `chains` | `raw_handle`, `number` | `prob=0.95` | `mcmc` | — |
| `coda_raftery` | `chain` | `raw_handle`, `number`, `number`, `number` | `q=0.025`, `r=0.005`, `s=0.95` | `light` | — |
| `coda_heidel` | `chain` | `raw_handle`, `number`, `number` | `eps=0.1`, `pvalue=0.05` | `light` | — |
| `coda_autocorr` | `chains` | `raw_handle` | — | `mcmc` | — |

### Use when

the classical diagnostics set for draws: Gelman-Rubin PSRF/MPSRF, Geweke z, ESS, HPD, Raftery-Lewis, Heidel-Welch, autocorrelation

### Do not use when

you want a rank-normalized R-hat + Bulk/Tail ESS -> #71 posterior; chart data -> #73 bayesplot

### Alternatives

| instead use | when |
| --- | --- |
| #71 posterior | the modern rank-normalized R-hat + Bulk/Tail ESS (more reliable) |
| #73 bayesplot | rating tables / chart data for R-hat/neff |
| coda_raftery/coda_heidel | single-chain diagnostics (they do not need >=2 chains) |

### Output fields

- gelman.psrf: matrix [Point est./Upper C.I.] per parameter; mpsrf (NA if nvar==1)
- geweke.z: matrix (chain x var) + a derived pvalue (2*pnorm(-\|z\|))
- effective_size: named vector (POOLED = the sum over chains); hpd.interval: matrix [lower/upper] on the pooled draws
- raftery.resmatrix (M/N/Nmin/I); heidel (stationarity+halfwidth); autocorr (lags x vars); meta

### Pitfalls

- coda_effective_size on an mcmc.list SUMS (POOLED=sum) the ESS of the chains — NOT per chain (pooled=TRUE)
- coda_raftery with few draws returns a CHARACTER resmatrix c('Error',Nmin) WITHOUT an the reference error -> POST-GATE is_numeric + Nmin
- Gelman R-hat>1.1 (strictly 1.01) = non-convergence; Geweke \|z\|>1.96 = non-stationarity
- HPD is computed on the POOLED draws (all chains together), one matrix; prob must be strictly in (0,1) (0/1 -> degenerate/full range)
- gelman/bundle require nchain>=2; niter>=10 (the spectral measures are undefined below that); a constant parameter -> singular

### References

- Plummer, Best, Cowles, Vines 2006 (coda, the reference News 6(1))
- Gelman & Rubin 1992 (Stat. Science 7(4))
- Geweke 1992 (Bayesian Statistics 4)
- Raftery & Lewis 1992 (Stat. Science 7(4))
- Heidelberger & Welch 1983 (Operations Research 31(6))

## #73 — Bayesian visualization DATA extractors (data, not charts)

**Module:** `bayesian_visualization_extractors.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `bp_mcmc_intervals_data` | `x` | `raw_handle`, `series_codes`, `number`, `number`, `enum` | `prob=0.5`, `prob_outer=0.9` | `light` | — |
| `bp_mcmc_areas_data` | `x` | `raw_handle`, `series_codes`, `number`, `number`, `enum` | `prob=0.5`, `prob_outer=1` | `light` | — |
| `bp_mcmc_trace_data` | `x` | `raw_handle`, `series_codes` | — | `light` | — |
| `bp_mcmc_rhat_data` | `rhat` | `raw_handle` | — | `light` | — |
| `bp_mcmc_neff_data` | `ratio` | `raw_handle` | — | `light` | — |
| `bp_ppc_intervals_data` | `y`, `yrep` | `raw_handle`, `matrix_handle`, `raw_handle`, `raw_handle`, `number`, `number` | `prob=0.5`, `prob_outer=0.9` | `light` | — |
| `bp_ppc_ribbon_data` | `y`, `yrep` | `raw_handle`, `matrix_handle`, `raw_handle`, `raw_handle`, `number`, `number` | `prob=0.5`, `prob_outer=0.9` | `light` | — |
| `bp_ppc_stat_data` | `y`, `yrep`, `stat` | `raw_handle`, `matrix_handle`, `string`, `raw_handle` | — | `light` | — |

### Use when

extracting NUMERIC data for diagnostic/PPC charts (intervals/areas/trace/rhat/neff/ppc); the frontend draws them

### Do not use when

raw R-hat/ESS numbers -> #71 posterior; classical diagnostics -> #72 coda; ggplot-returning functions (excluded); ppc_loo_pit (non-deterministic)

### Alternatives

| instead use | when |
| --- | --- |
| #71 posterior | raw R-hat/ESS numbers (not rating tables) |
| #72 coda | HPD/autocorrelation/Gelman/Geweke diagnostics |
| #71 rhat | it produces the rhat VECTOR that feeds bp_mcmc_rhat_data |

### Output fields

- list(data=df with the EXACT bayesplot fields, n=nrow, + echoed params) per extractor -> to_mcp records
- mcmc_intervals: parameter/outer_width/inner_width/point_est/ll/l/m/h/hh
- mcmc_areas: parameter/interval/interval_width/x/density/scaled_density (default prob_outer=1)
- mcmc_rhat/mcmc_neff: diagnostic/parameter/value/rating/description (rating low/ok/high)
- ppc_intervals/ribbon: per-obs ll/l/m/h/hh; ppc_stat: per-draw value

### Pitfalls

- the B extractors take a precomputed numeric VECTOR (rhat/ess-ratio), NOT a fitted model
- the generics rhat/neff_ratio/pp_check are NEVER called bare (multi-way collisions with posterior/rstanarm/brms); pars AS character (NEVER vars(..))
- prob>prob_outer -> a SILENT swap; prob=0 is accepted SILENTLY; stat=c('mean','sd') keeps ONLY the first
- an NA in the diagnostic vector -> a SILENT drop of the parameter (fewer rows); ncol(yrep)==length(y) is a KEY GATE
- the output is tidy data FOR a chart, NOT a convergence diagnosis (that decision belongs to #71/#72)

### References

- Gabry, Simpson, Vehtari, Betancourt, Gelman 2019 (Visualization in Bayesian workflow, JRSS-A 182(2))
- Vehtari et al 2021 (R-hat/ESS rating thresholds)

## #204 — Bayesian Structural Time Series (state.specification: local/semilocal trend + seasonal + AR + spike-and-slab regression) with MCMC

**Module:** `bayesian_structural_time.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `bsts_fit` | `seed` | `series_handle`, `formula`, `df_handle`, `enum`, `boolean`, `boolean`, `integer`, `integer`, `integer`, `integer`, `integer`, `number`, `integer` | `local_linear_trend=True`, `semilocal_linear_trend=False`, `seasonal_nseasons=0`, `season_duration=1`, `ar_lags=0`, `niter=1000` | `mcmc` | `object` |
| `bsts_predict` | `object`, `seed` | `raw_handle`, `integer`, `df_handle`, `number`, `number`, `integer`, `integer` | `horizon=12`, `quantile_lower=0.025`, `quantile_upper=0.975` | `mcmc` | — |
| `bsts_components` | `object` | `raw_handle`, `integer`, `number`, `number` | `quantile_lower=0.025`, `quantile_upper=0.975` | `mcmc` | — |

### Use when

you want a Bayesian structural decomposition/forecast of a univariate series with explicitly interpretable state components (trend + seasonality + AR) and FULL posterior uncertainty (not a point estimate); or a Bayesian regression on a time series with variable SELECTION through spike-and-slab (expected_model_size) when you have many candidate regressors; you want the posterior mean contribution of each component (nowcasting/decomposition) + predictive quantile bands

### Do not use when

you want a point/frequentist state-space estimate without MCMC (go to KFAS/dlm, cat. 10); multivariate/cointegration dynamics (VAR/VECM/BVAR); a fully custom likelihood/hierarchical model (rstan/brms/nimble); a plain ARIMA/ETS forecast without a component decomposition; a very long series where the MCMC cost is not justified against a fast Kalman filter

### Prerequisites

- bsts_fit (the PRODUCER: it builds the state.specification from flags + the MCMC fit; it returns the object handle consumed by predict/components — the seed is MANDATORY)
- c00_data_utilities/reading_delimited_fixed.read_delimited (loading the data_frame for regression mode: response + regressors)
- c10_trend_cycle_statespace/kalman_filter_smoother.kf_local_linear_trend (a frequentist state-space baseline; compare before investing in MCMC)

### Alternatives

| instead use | when |
| --- | --- |
| 10-trend-cycle-statespace/bs_run_mcmc | you want a Bayesian state-space model with an explicit prior specification / custom observation models (SV/non-Gaussian) rather than the flag-driven bsts builder |
| 10-trend-cycle-statespace/kf_local_linear_trend | you want a point/frequentist MLE state-space model (a fast Kalman filter, no MCMC) — the same structural decomposition without posterior draws |
| 14-bayesian-toolkit/nim_bayes_mcmc | you need a fully custom hierarchical/state model that cannot be expressed with the bsts state components |
| bsts_fit (family='student') | outliers / heavy tails in the observation — a robust observation model instead of gaussian |
| bsts_fit (semilocal_linear_trend=TRUE) | long forecast horizons — a mean-reverting slope avoids the explosive trend of the local linear model |

### Output fields

- bsts_fit: state_components (the names trend/seasonal.N.k/Ar_k/regression); residual_sd (the posterior mean sigma.obs); sigma_obs_quantiles; coefficients {variable, inclusion_prob, posterior_mean, posterior_mean_incl} (regression only); burn; fitted_series + time; object (the handle)
- bsts_predict: mean/median (chart-data); lower/upper predictive bands at the quantiles; step; has_regression
- bsts_components: contributions (time x component posterior mean; a stacked decomposition); contributions_lower/upper bands; components; time; burn

### Pitfalls

- DETERMINISM: bsts is MCMC (the Boom C++ RNG) — ONLY the combination set.seed(seed)+bsts(seed=) gives reproducible results; the wrapper does both, in fit AND in predict; the seed is MANDATORY
- local_linear_trend vs semilocal: the local linear trend has a random-walk slope that can 'explode' at long horizons; the semilocal one (an AR(1) mean-reverting slope) is safer for forecasting — the two are mutually exclusive (gate)
- inclusion_prob (spike-and-slab): the posterior probability that the regressor is in the model; posterior_mean is the MEAN OVER ALL draws (it includes the zeros -> shrunk), posterior_mean_incl is conditional on inclusion — do NOT confuse them
- expected_model_size applies ONLY in regression mode; it sets the prior number of non-zero coefficients (smaller => a stronger sparsity prior); in a pure structural model it is an error (gate)
- regression forecast: newdata (the future regressors) is MANDATORY and must have nrow==horizon with the same predictor columns — otherwise a gate stop (the forecast needs future values of X)
- burn-in: the default SuggestBurn(0.1) discards 10% as warm-up; too few niter => unstable posterior means; keep niter large enough (>=500 in production; 100-250 only for smoke tests)
- seasonal.N.k naming: AddSeasonal with nseasons=12 gives the component 'seasonal.12.1'; season_duration>1 groups steps into a season (e.g. weekly seasonality in daily data)

### References

- Scott & Varian (2014) Predicting the present with Bayesian structural time series, Int. J. Mathematical Modelling and Numerical Optimisation 5:4-23
- Scott & Varian (2015) Bayesian Variable Selection for Nowcasting Economic Time Series, in Economic Analysis of the Digital Economy (NBER/Univ. Chicago Press)
- Brodersen, Gallusser, Koehler, Remy & Scott (2015) Inferring causal impact using Bayesian structural time-series models, Annals of Applied Statistics 9:247-274
- Durbin & Koopman (2012) Time Series Analysis by State Space Methods, 2nd ed., Oxford University Press (structural components + the Kalman filter foundation)
- George & McCulloch (1997) Approaches for Bayesian variable selection, Statistica Sinica 7:339 (the spike-and-slab prior)

## #205 — Sequential Monte Carlo / particle filters for non-linear/non-Gaussian state-space models (bootstrap / auxiliary / Liu-West / ensemble Kalman)

**Module:** `sequential_monte_carlo.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `smc_filter` | `code`, `inits`, `latentNodes`, `seed` | `string`, `raw_handle`, `series_codes`, `integer`, `raw_handle`, `raw_handle`, `enum`, `integer`, `series_codes`, `number`, `enum`, `number`, `num_array` | `nParticles=1000`, `thresh=1`, `d=0.99` | `light` | — |

### Use when

you have a BUGS-style state-space (hidden Markov) model with latent states x[t] and observations y[t]; you want (a) an estimate of the marginal log-likelihood (for model comparison / particle MCMC / likelihood-based inference) and/or (b) the filtered distribution of the latent states f(x[t]\|y[1:t]) per time point (mean/quantiles = chart-data). It handles NON-linear/NON-Gaussian transition & observation equations where the Kalman filter does not apply

### Do not use when

a linear-Gaussian state-space model (use the exact Kalman filter: 10-trend-cycle-statespace/kf_fit or MARSS/dlm — analytic, with no Monte Carlo noise); you want a FULL Bayesian posterior over the parameters with MCMC diagnostics (14-bayesian-toolkit/nim_bayes_mcmc — MCMC with an Rhat/ESS gate); structural-break/latent-regime work (06-volatility-regimes); simple smoothing without a latent-state model (mFilter/HP)

### Prerequisites

- smc_filter (the default method=bootstrap; only bootstrap/auxiliary return log_lik+ESS)
- c14_bayesian_toolkit/general_bugs_style.nim_bayes_mcmc (the same BUGS DSL; for a full parameter posterior rather than filtering)
- c00_data_utilities/reading_delimited_fixed.read_delimited (loading the observations y as a series)

### Alternatives

| instead use | when |
| --- | --- |
| 10-trend-cycle-statespace/kf_fit | a linear-Gaussian SSM -> an exact Kalman filter/smoother (no Monte Carlo variance), a closed-form likelihood |
| 14-bayesian-toolkit/nim_bayes_mcmc | you want a full Bayesian posterior over the parameters + convergence diagnostics (Rhat/ESS), not only latent-state filtering / a log_lik |
| smc_filter method='auxiliary' | a peaked/informative observation likelihood -> lookahead resampling reduces particle degeneracy relative to bootstrap |
| smc_filter method='liuWest' | you want joint state+parameter online estimation in ONE pass (caution: didactic, often poor; no log_lik) |
| smc_filter method='ensembleKF' | a high-dimensional latent state with additive normal observation error -> an EnKF Monte Carlo Kalman approximation (no log_lik) |

### Output fields

- method: the selected filter; latent_vars: the names of the latent variable(s)
- log_likelihood + log_likelihood_available: the estimated marginal log_lik (numeric for bootstrap/auxiliary; NA_real_ + FALSE for liuWest/ensembleKF — STRUCTURALLY, NEVER a fabricated value)
- state_summary: a data_frame {node, mean, sd, q..} PER latent node/time — the per-time filtered summaries (chart-data); state_mean: the per-time posterior mean
- filtered_samples: a named list of equally weighted samples (particles × latent nodes) per latent variable — for downstream reweighting/plots
- ess + ess_available: the per-time effective sample size (numeric for bootstrap/auxiliary; NULL + FALSE otherwise)
- param_summary + param_vars: (liuWest ONLY) the posterior summary of the top-level parameters; NULL for the rest
- n_particles / n_time / metadata (method/thresh/lookahead/d/seed/saveAll)

### Pitfalls

- METHOD HETEROGENEITY (live-verified): ONLY bootstrap & auxiliary return a log-likelihood estimate and a per-time ESS; for liuWest & ensembleKF run returns NULL and there is no returnESS. The node declares this explicitly (log_likelihood_available / ess_available) — do not read log_likelihood=NA as 'a bad model', it is a structural limit of the method
- particle depletion / collapse: too few nParticles or a model-data mismatch -> log_lik=-Inf or NaN samples; the node blocks it (a hard gate). Raise nParticles (default 1000); the log_lik estimate has Monte Carlo variance -> for model comparison use the SAME seed & nParticles
- the Liu-West filter: the package itself warns that it 'often performs poorly, provided primarily for didactic purposes'; the parameter posteriors can be over-concentrated (particle impoverishment). Prefer PMCMC (sampler_RW_PF, outside the surface) or nim_bayes_mcmc for reliable parameter inference
- filtered, NOT smoothed: what is returned is f(x[t]\|y[1:t]) (saveAll=TRUE, smoothing=FALSE); it is not the full smoothing distribution f(x[t]\|y[1:T])
- thresh MUST ==1 (gate): resampling at every step => mvEWSamples is equally weighted everywhere => correct per-time summaries; thresh<1 is blocked (silently wrong otherwise); this applies ONLY to bootstrap (auxiliary ignores thresh)
- latentNodes in TIME order: they must be stochastic nodes (e.g. 'x' or 'x[1:10]'); the data must contain NO NA (nimble treats an NA as a MISSING node to be imputed — a hidden parameter, gate)

### References

- Michaud, de Valpine, Turek, Paciorek, Nguyen (2021) 'Sequential Monte Carlo Methods in the nimble and nimbleSMC the reference Packages', J. Statistical Software 100(3)
- Gordon, Salmond & Smith (1993) 'Novel approach to nonlinear/non-Gaussian Bayesian state estimation', IEE Proc. F 140(2):107 (the bootstrap filter)
- Pitt & Shephard (1999) 'Filtering via simulation: Auxiliary particle filters', JASA 94(446):590 (the auxiliary filter)
- Liu & West (2001) 'Combined parameter and state estimation in simulation-based filtering', in Sequential Monte Carlo Methods in Practice, Springer, pp.197-223
- Houtekamer & Mitchell (1998) 'Data assimilation using an ensemble Kalman filter technique', Monthly Weather Review 126(3):796
- Doucet, de Freitas & Gordon (2001) Sequential Monte Carlo Methods in Practice, Springer
