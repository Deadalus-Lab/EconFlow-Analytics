<!-- SPDX-License-Identifier: AGPL-3.0-only -->
# 10-trend-cycle-statespace

14 METHOD-SELECTION cards, 14 modules, 40 nodes.

Every card below governs one wrapper module in this package. The cards are the
reason a method exists here at all: they record when it applies, what to reach
for instead, and the traps that make its output easy to misread.

## #56 — HP / Baxter-King / Christiano-Fitzgerald filters

**Module:** `hp_baxter_king.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `mfl_hp_filter` | `y` | `series_handle`, `number`, `enum`, `boolean` | `drift=False` | `light` | — |
| `mfl_bk_filter` | `y` | `series_handle`, `number`, `number`, `integer`, `enum`, `boolean` | `drift=False` | `light` | — |
| `mfl_cf_filter` | `y` | `series_handle`, `number`, `number`, `boolean`, `boolean`, `enum`, `integer` | `root=False`, `drift=False` | `light` | — |
| `mfl_bw_filter` | `y` | `series_handle`, `integer`, `integer`, `boolean` | `drift=False` | `light` | — |
| `mfl_tr_filter` | `y` | `series_handle`, `number`, `number`, `boolean` | `drift=False` | `light` | — |

### Use when

a fast trend/cycle decomposition (output gap) without estimating a model; CF-asymmetric fills the end (end-of-sample gap, no NA) but is internally full-sample time-varying/revisable — real-time only at the endpoint; a non-revisable real-time gap -> #92 one-sided HP

### Do not use when

you want SE/credible bands (KFAS/dlm/bssm), a common trend across several series (MARSS), or a non-revisable Basel gap (hpfilter)

### Alternatives

| instead use | when |
| --- | --- |
| #92 hpfilter one-sided HP | real-time / Basel III credit gap (non-revisable) |
| #57 Hamilton filter | avoiding the spurious cycles of the HP filter |
| #58/#59 UC state-space | you want SE bands + a model-based forecast |

### Output fields

- trend: potential output (ts)
- cycle: output gap in % of 100*log(GDP) (ts)
- lambda: the effective smoothing parameter
- na_each_end: NA at the edges (BK/CF-symmetric endpoint problem)

### Pitfalls

- an interior NA -> silently the WHOLE cycle becomes NA (silently wrong, hard gate)
- BK & CF-symmetric/fixed leave nfix NA at EACH edge -> the most recent gap is missing
- the two-sided HP is revised at the edge (endpoint bias) -> NOT for real-time policy
- the choice of lambda (1600 quarterly / Ravn-Uhlig) changes the gap dramatically
- CF-asymmetric fills the end BUT the values are revised just as with the two-sided HP: interior points use future data (time-varying weights, Christiano-Fitzgerald 2003) — only the last observation is genuinely one-sided

### References

- Hodrick & Prescott 1997 (JMCB)
- Baxter & King 1999 (REStat)
- Christiano & Fitzgerald 2003 (Int. Econ. Review)
- Ravn & Uhlig 2002 (REStat)
- Enders 2015

## #57 — Hamilton regression filter

**Module:** `hamilton_regression_filter.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `hf_xts_from_long` | `df`, `series_name` | `df_handle`, `string`, `enum`, `integer` | — | `light` | `x` |
| `hf_filter` | `x` | `raw_handle`, `integer`, `integer` | — | `light` | — |
| `hf_glm` | `x` | `raw_handle`, `integer`, `integer` | — | `light` | — |

### Use when

an output gap without the spurious dynamics of the HP filter (the Hamilton critique); OLS projection of y_{t+h} on p lags; residual=gap

### Do not use when

you want a smooth potential output, a forecast/state uncertainty (state space), or band-pass isolation (BK/CF)

### Alternatives

| instead use | when |
| --- | --- |
| #56 HP filter | you accept two-sided smoothing |
| #92 one-sided HP | a real-time Basel gap |
| #58 KFAS trend-cycle | a model-based gap with SE |

### Output fields

- cycle: output gap (residual y_{t+h}-fitted)
- trend: fitted (the predictable component)
- n_lost_trend: h+p-1 leading NA; n_lost_random: h
- coefficients/glance (hf_glm): OLS diagnostics (term/estimate/p_value, aic, r_squared)

### Pitfalls

- p>=2 is MANDATORY (p=1 does not capture seasonality)
- xts lags POSITIONALLY -> calendar gaps silently desynchronise h/p
- the default is h=2*ppy/p=ppy (frequency-aware); the package hardcodes 8/4 even for monthly data (silently wrong)
- leading NA in trend/cycle are expected (date alignment), not an error

### References

- Hamilton 2018 'Why You Should Never Use the Hodrick-Prescott Filter' (REStat 100(5))
- Enders 2015

## #58 — Kalman filter/smoother + unobserved-components models

**Module:** `kalman_filter_smoother.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `kf_local_level` | `y` | `series_handle`, `boolean`, `integer` | `seasonal=False` | `light` | `model` |
| `kf_local_linear_trend` | `y` | `series_handle`, `boolean`, `integer` | `seasonal=False` | `light` | `model` |
| `kf_trend_cycle` | `y` | `series_handle`, `number`, `boolean`, `integer` | `seasonal=False` | `light` | `model` |
| `kf_forecast` | `object` | `raw_handle`, `integer`, `enum`, `number` | `n_ahead=8`, `level=0.95` | `light` | — |

### Use when

linear-Gaussian UC with ML estimation + an exact Kalman filter (real-time) & smoother (two-sided); trend+SSMcycle -> output gap with SE bands

### Do not use when

non-Gaussian data, you want a full Bayesian posterior (bssm), a common trend across several series (MARSS), or a time-varying exog_handle

### Alternatives

| instead use | when |
| --- | --- |
| #59 dlm | SVD Kalman; equivalent; KFAS has better diffuse handling |
| #60 bssm | you want credible bands instead of asymptotic SE |
| #56 HP | a fast filter without estimation |

### Output fields

- filtered_states (att): real-time/one-sided
- smoothed_states (alphahat): two-sided/historical
- trend: potential output; cycle: output gap (+_se bands)
- log_lik, variances H/Q, convergence, diffuse_d

### Pitfalls

- signal is masked by signal -> ALWAYS use signal
- non-convergence of fitSSM -> silently junk variances (post-gate convergence==0)
- diffuse_d: the first d filtered values have ~infinite variance (unreliable)
- the filtered gap != the smoothed gap (the real-time gap is revised)

### References

- Durbin & Koopman 2012 (State Space Methods, 2nd ed.)
- Harvey 1989 (Structural Time Series & Kalman Filter)
- Helske 2017 JSS 78(10) 'KFAS'

## #59 — Dynamic linear models (state space)

**Module:** `dynamic_linear.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `dl_local_level` | `y` | `series_handle`, `boolean`, `integer` | `seasonal=False` | `light` | `filtered_obj` |
| `dl_local_linear_trend` | `y` | `series_handle`, `boolean`, `integer` | `seasonal=False` | `light` | `filtered_obj` |
| `dl_trend_cycle` | `y` | `series_handle`, `number`, `boolean`, `integer` | `seasonal=False` | `light` | `filtered_obj` |
| `dl_forecast` | `object` | `raw_handle`, `integer`, `number` | `n_ahead=8`, `level=0.95` | `light` | — |

### Use when

linear-Gaussian state space with an SVD Kalman filter (numerically stable); trend + a rotation-form stochastic cycle -> output gap

### Do not use when

you want diffuse initialisation/non-Gaussian (KFAS), Gibbs/Bayesian (bssm), time-varying regression, or multivariate (MARSS)

### Alternatives

| instead use | when |
| --- | --- |
| #58 KFAS | an equivalent UC model; better diffuse handling |
| #60 bssm | a full posterior |
| #56 HP | no model |

### Output fields

- smoothed_states/filtered_states + _se (two-sided vs real-time)
- trend (smoothed level), slope, cycle (output gap)
- one_step_forecast, log_lik, par, convergence

### Pitfalls

- CRITICAL: a free AR(2) cycle -> a DEGENERATE decomposition (level & cycle cancel each other out); the wrapper builds a rotation form at a FIXED frequency
- dlmMLE non-convergence -> junk variances (post-gate)
- dlmFilter/dlmSmooth carry a time-0 prior row (n+1) -> dropFirst
- dlmForecast works on constant models ONLY

### References

- West & Harrison 1997 (Bayesian Forecasting & Dynamic Models)
- Petris, Petrone & Campagnoli 2009 (Dynamic Linear Models with the reference, Springer UseR!)
- Petris 2010 JSS 36(12)

## #60 — Bayesian state space

**Module:** `bayesian_state_space.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `bs_prior_spec` | `init` | `enum`, `number`, `number`, `number`, `number`, `number`, `number`, `number` | — | `light` | — |
| `bs_bsm_lg` | `y`, `sd_y`, `sd_level` | `series_handle`, `raw_handle`, `raw_handle`, `raw_handle`, `raw_handle`, `integer` | — | `light` | `object` |
| `bs_ar1_lg` | `y`, `rho`, `sigma`, `mu`, `sd_y` | `series_handle`, `raw_handle`, `raw_handle`, `raw_handle`, `raw_handle` | — | `light` | `object` |
| `bs_run_mcmc` | `model`, `iter`, `seed` | `raw_handle`, `integer`, `integer`, `integer`, `integer`, `enum` | `thin=1` | `mcmc` | — |

### Use when

a full posterior + credible bands via MCMC; bsm_lg (level+slope+seasonal) -> a stochastic trend; ar1_lg -> a Bayesian output-gap factor

### Do not use when

you want a fast point estimate (KFAS/dlm), non-Gaussian data, forecasting (v1), or multivariate (MARSS)

### Alternatives

| instead use | when |
| --- | --- |
| #58 KFAS / #59 dlm | an ML point estimate + asymptotic SE, fast |
| #14 bayesian-toolkit (BVAR/brms) | more general Bayesian models |

### Output fields

- theta_summary: posterior of the variances/parameters
- trend (state level), cycle (state signal ar1_lg), seasonal: {time,mean,sd,lower,upper} credible band
- states_summary: per-time records (variable/time/Mean/SD/probs%)
- acceptance_rate

### Pitfalls

- gamma MASKS gamma -> use qualified bssm:: constructors
- the seed is MANDATORY (the bssm default is random, determinism)
- the MCMC output is a jump chain (counts=weights) -> use summary.mcmc_output ONLY (weighted), NOT the raw array
- a low acceptance_rate -> poor mixing, check it before trusting the bands

### References

- Helske & Vihola 2021 (bssm, The 13(2))
- Durbin & Koopman 2012

## #61 — Multivariate state space (output gap / NAIRU / DFA)

**Module:** `multivariate_state_space.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `marss_prepare_data` | `df` | `df_handle`, `string`, `boolean` | `standardize=False` | `light` | — |
| `marss_dfa` | `data` | `raw_handle`, `integer`, `enum`, `integer`, `boolean` | `m=1`, `maxit=5000`, `allow_nonconvergence=False` | `light` | `object` |
| `marss_param_cis` | `object` | `raw_handle`, `enum`, `number`, `integer`, `integer` | `alpha=0.05`, `nboot=1000` | `heavy` | — |
| `marss_forecast` | `object` | `raw_handle`, `integer`, `number`, `enum`, `enum` | `n_ahead=0`, `level=0.95` | `light` | — |
| `marss_glance` | `object` | `raw_handle`, `boolean` | `tidy=False` | `light` | — |

### Use when

Dynamic Factor Analysis: m common latent trends from n macro indicators; a common labour-market trend = a robust NAIRU proxy; y-fitted = output-gap-style

### Do not use when

a univariate series (KFAS/dlm), an explicit structural NAIRU/Phillips model (EXCLUDED: weakly identified), or TMB paths (marssTMB)

### Alternatives

| instead use | when |
| --- | --- |
| #07 dfms factor models | nowcasting factors |
| #58/#59 univariate SS | one series |
| #56 filters | no model |

### Output fields

- factors: m x T COMMON smoothed trends (+factors_se, filtered_factors)
- loadings: Z n x m factor loadings
- gaps: y - fitted (output-gap-style)
- log_lik/AIC/AICc, convergence

### Pitfalls

- ORIENTATION TRAP (silently wrong #1): a T x n matrix is accepted SILENTLY -> garbage; VARIABLES GO IN ROWS (transpose)
- non-convergence (conv=1/2/10=maxit) -> a post-gate blocker
- DFA factors: the sign/scale/rotation is undetermined -> interpret loadings+factor together
- parametric/innovations CIs = a seeded bootstrap (seed gate)

### References

- Holmes, Ward & Wills 2012 (MARSS, The 4(1))
- Zuur et al. 2003 (Dynamic factor analysis, Environmetrics)
- Harvey 1989

## #92 — One-sided HP filter (Basel III credit gap)

**Module:** `sided_hp_filter.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `hp_one_sided` | `x` | `series_handle`, `number` | `lambda=1600` | `light` | — |

### Use when

a ONE-SIDED (real-time/recursive) HP trend; the OFFICIAL Basel III methodology for the credit-to-GDP gap / CCyB (lambda=400000 quarterly)

### Do not use when

historical analysis where revision is acceptable (two-sided HP), band-pass (BK/CF), or model-based uncertainty (KFAS/dlm/bssm)

### Alternatives

| instead use | when |
| --- | --- |
| #56 mfl_hp_filter (two-sided) | the same lambda but revisable |
| #56 mfl_cf_filter asymmetric | end-of-sample band-pass (no NA at the end); real-time only at the endpoint — internally revisable |
| #57 Hamilton | a real-time OLS gap |

### Output fields

- trend: one-sided HP trend (data_frame)
- cycle: x - trend = credit gap / output gap (data_frame -> records)
- lambda (400000 for the Basel credit gap), n, series

### Pitfalls

- the one-sided trend DIFFERS from the two-sided one at the same lambda -> do not compare them as equals
- lambda=400000 is the Basel-mandated value for quarterly credit data (NOT 1600)
- an interior NA/Inf -> a silently NA trend (hard gate)
- lambda<0 runs WITHOUT an error but gives a wrong result (hard gate); lambda=0 -> almost everything NA

### References

- BCBS 2010 'Guidance for national authorities operating the countercyclical capital buffer' (Basel III)
- Drehmann, Borio & Tsatsaronis 2011 (BIS Working Papers, credit-to-GDP gap)
- Hodrick & Prescott 1997
- Stock & Watson 1999 (one-sided HP)

## #183 — Bayesian time-varying-parameter (TVP) regression with global-local shrinkage (triple/double/ridge) + SV

**Module:** `bayesian_time_varying.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `stvp_fit` | `formula`, `data` | `formula`, `df_handle`, `enum`, `boolean`, `integer`, `integer`, `integer`, `integer` | `sv=False`, `niter=2000`, `nthin=1`, `seed=2025` | `mcmc` | `object` |
| `stvp_forecast` | `object`, `newdata` | `raw_handle`, `df_handle`, `integer` | `n_ahead=1` | `light` | — |
| `stvp_lpds` | `object`, `data_test` | `raw_handle`, `df_handle` | — | `light` | — |

### Use when

a single equation y ~ x; you suspect the coefficients CHANGE over time (structural change, changing elasticities); you want a full posterior + automatic shrinkage towards a constant coefficient wherever no variation is needed

### Do not use when

constant coefficients suffice (OLS/#46); multivariate joint dynamics (a VAR, cat. 03); a pure trend/cycle decomposition of one series (#56-61 filters/state space); very large samples (MCMC cost)

### Prerequisites

- c00_data_utilities/reading_delimited_fixed.read_delimited (load the panel/time series as a numeric data_frame)
- stvp_lpds (the out-of-sample log predictive density: compare mod_type / TVP vs constant on a hold-out sample)
- stvp_forecast (a predictive forecast with future regressor values)

### Alternatives

| instead use | when |
| --- | --- |
| dlm/KFAS/bssm (#58-60) state space | you want a structural trend/cycle/seasonal decomposition or Kalman filtering, not a TVP regression with shrinkage |
| #46 plm/OLS with constant coefficients | theta_sr ~0 for ALL coefficients — there is no time variation, the constant model suffices |
| mod_type='ridge' | you want TVP without global-local shrinkage (a baseline; it does not shrink towards a constant) |
| brms/rstan (category 14) | a non-gaussian likelihood or a hierarchical structure beyond TVP+SV |

### Output fields

- beta_paths: per covariate, the posterior median + 95% CI of the time-varying coefficient (chart-data, of length n_obs+1: the states t=0.T)
- theta_sr_median: sqrt(theta), the state standard deviation per covariate; ~0 => the coefficient is CONSTANT (shrinkage collapsed it), a large value => substantive time variation
- beta_mean_median: the constant (mean) level of each coefficient
- sigma2_median: the observation variance — a scalar if sv=FALSE, a path (of length n_obs) if sv=TRUE
- shrinkage: a_xi/a_tau (double/triple only)/kappa2_B/lambda2_B — the global shrinkage hyperparameters
- stvp_forecast: pred_median/pred_lower/pred_upper per horizon; stvp_lpds: lpds (larger=a better forecast)

### Pitfalls

- theta_sr is the sqrt of the variance AND non-centered (it can come out negative in the posterior sample; the ABSOLUTE value/distance from 0 is what matters) — \|theta_sr\|~0 means a constant coefficient, NOT a zero coefficient (see beta_mean)
- beta_paths have n_obs+1 points (the initial state t=0 is included); beta_time runs 0.T
- stvp_forecast REQUIRES future values of the regressors (newdata); it does not forecast the x itself — nrow(newdata) >= n.ahead, otherwise it fails
- stvp_lpds accepts EXACTLY 1 hold-out row (the package fails otherwise); compare mod_type through the sum of LPDS over a rolling hold-out
- ridge has NO a_xi/a_tau (it performs no shrinkage selection); do not look for the shrinkage fields there
- the MCMC is stochastic: the seed is mandatory; a different seed => different (but compatible) posterior summaries

### References

- Knaus, Bitto-Nemling, Cadonna & Frühwirth-Schnatter, 'Shrinkage in the Time-Varying Parameter Model Framework Using the reference Package shrinkTVP', JSS 2021 (the shrinkTVP vignette)
- help('shrinkTVP','shrinkTVP'), help('forecast_shrinkTVP'), help('LPDS'), help('simTVP')
- Bitto & Frühwirth-Schnatter 2019 (J. Econometrics 210:75, the Normal-Gamma / double shrinkage prior)
- Cadonna, Frühwirth-Schnatter & Knaus 2020 (Econometrics 8:20, the triple gamma prior)
- Frühwirth-Schnatter & Wagner 2010 (J. Econometrics 154:85, the non-centered parameterization / theta_sr)

## #184 — Bayesian regression with time-varying (random-walk) coefficients — HMC (Stan)

**Module:** `bayesian_regression_time.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `walker_fit` | `formula`, `data` | `formula`, `df_handle`, `enum`, `enum`, `num_array`, `num_array`, `num_array`, `num_array`, `num_array`, `integer`, `integer`, `integer` | `family='gaussian'`, `rw_order='rw1'`, `beta_prior=[0, 10]`, `sigma_prior=[2, 0.01]`, `nu_prior=[0, 10]`, `sigma_y_prior=[2, 0.01]`, `chains=1`, `iter=400`, `seed=2025` | `mcmc` | `object` |
| `walker_coef` | `object` | `raw_handle`, `boolean` | `exponentiate=False` | `light` | — |

### Use when

you want a regression whose coefficients EVOLVE over time (structural change / time-varying elasticities / a changing NAIRU slope), gaussian or counts (poisson/binomial), with a full posterior + CI

### Do not use when

constant coefficients (a classic lm/GLM); pure trend-cycle extraction without regressors (#56-61); you need a formal forecast (predict; outside the surface here); a very large n/many covariates (HMC is expensive)

### Prerequisites

- c00_data_utilities/reading_delimited_fixed.read_delimited (loading a TIME-ordered data_frame; one row = one time point)
- walker_fit (max_rhat/n_divergent/converged: check the HMC convergence BEFORE interpreting the coefficients)

### Alternatives

| instead use | when |
| --- | --- |
| 14-bayesian-toolkit/br_fit | you want a hierarchical/multilevel or non-gaussian GLM WITHOUT a time-varying structure (constant or group-varying coefficients) |
| 10-trend-cycle-statespace/bs_run_mcmc | a general (non-linear/non-gaussian) state-space model with particle MCMC rather than the HMC-marginalised approach |
| 10-trend-cycle-statespace/kf_local_linear_trend | a purely frequentist state-space trend/level WITHOUT time-varying regression coefficients |

### Output fields

- walker_fit.converged / max_rhat / n_divergent: the convergence gate (converged=TRUE only if max_rhat<1.1 & there are 0 divergences)
- walker_fit.coef_names / n_time_varying: the names of the time-varying coefficients (including the time-varying (Intercept)/level)
- walker_fit.sigma_summary: the posterior of the standard deviations (sigma_y = the observation sd; sigma_rw* = the rate of change of each coefficient)
- walker_fit.fitted: the posterior mean fitted values (y_fit) — chart-data
- walker_coef.coef_table: long records {beta,time,median,lower,upper,mean,sd} — the time-varying posterior median + 95% CI (chart-data)

### Pitfalls

- convergence FIRST: if converged=FALSE (max_rhat>=1.1 or n_divergent>0) the estimates are unreliable — raise iter/tighten the priors, do NOT interpret
- a small iter=400 -> low-ESS warnings; it is deliberately SMALL for a node — raise iter for a final analysis
- poisson/binomial: the coefficients are on the LINK scale; use walker_coef(exponentiate=TRUE) for a multiplicative interpretation
- sigma_rw*->0 ⇒ the coefficient is PRACTICALLY constant (negligible time variation); a large sigma_rw ⇒ strong variation
- double intercept: the rw term adds its own time-varying level; the wrapper prepends '-1 +' so that only ONE remains (identifiability)
- counts, silently wrong: walker_glm accepts non-integer y SILENTLY — the gate blocks it (non-negative integers; binomial requires y<=u)

### References

- Helske J. (2022), walker: Bayesian Generalized Linear Models with Time-Varying Coefficients, the vignette 'walker'
- help('walker','walker'), help('walker_glm','walker'), coef.walker_fit
- Vihola, Helske & Franks (2020), Importance sampling type estimators based on approximate marginal MCMC, Scandinavian J. of Statistics 47(4):1339-1376 (the walker_glm exact-approximate weighting)
- Durbin & Koopman (2012), Time Series Analysis by State Space Methods 2nd ed. (the random-walk coefficient state-space representation)

## #185 — Particle-filter (bootstrap) log-likelihood + iterated filtering (IF2) MLE for non-linear non-Gaussian state-space models

**Module:** `particle_filter_log.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `pomp_pfilter` | — | `enum`, `raw`, `integer`, `integer` | `model='gompertz'`, `Np=500`, `seed=2025` | `light` | — |
| `pomp_mif2` | — | `enum`, `raw`, `raw`, `integer`, `integer`, `number`, `number`, `integer` | `model='gompertz'`, `Nmif=10`, `Np=500`, `cooling_fraction_50=0.5`, `rw_sd_value=0.02`, `seed=2025` | `light` | — |

### Use when

a non-linear / non-Gaussian state-space model where the Kalman filter does not apply; you want a particle-filter log-likelihood (pomp_pfilter) or a simulation-based MLE (pomp_mif2) on one of the built-in templates gompertz/ricker/ou2

### Do not use when

a linear-Gaussian model (use KFAS/dlm/MARSS/bssm — the exact Kalman filter); you want custom dynamics beyond the three templates (that requires C code, blocked for security reasons); a full Bayesian posterior over the parameters (pmcmc/bssm)

### Prerequisites

- pomp_pfilter (run the particle filter first: check for a finite loglik & min_ess before IF2)
- pomp_mif2 (the IF2 MLE; check the converged field & the loglik_trace for convergence)

### Alternatives

| instead use | when |
| --- | --- |
| KFAS/dlm/MARSS/bssm (category 10) | the model is linear-Gaussian -> an exact Kalman filter, not a particle approximation |
| the bssm bootstrap/psi particle filter | you want Bayesian inference (MCMC) with a particle filter rather than a point MLE |
| a larger Np / more Nmif | a low min_ess (particle depletion) or a non-converging loglik_trace |

### Output fields

- loglik: the particle-filter log-likelihood (pomp_pfilter) or the final IF2 loglik (pomp_mif2); a Monte Carlo estimate, it varies with Np/the seed
- eff_sample_size / min_ess (pomp_pfilter): the ESS per time point; a low min_ess -> particle depletion, raise Np
- cond_log_lik (pomp_pfilter): the conditional log-likelihood per time point (chart-data)
- estimates / estimated (pomp_mif2): the final values of ALL the parameters + which names were estimated
- loglik_trace / traces (pomp_mif2): the loglik & the parameter path per IF2 iteration — a convergence diagnostic (chart-data)
- converged: a finite loglik (& estimates); a stateless-node flag instead of stderr

### Pitfalls

- the loglik is a STOCHASTIC Monte Carlo estimate — two runs with a different seed/Np give different values; compare only with the same seed/Np
- a low min_ess (e.g. << Np) means particle depletion -> the loglik is unreliable, NOT that the model is bad; raise Np
- IF2 (pomp_mif2) has NO hard convergence test — judge convergence from the loglik_trace (it must stabilise) & the converged flag, not from a single run
- the initial-value parameters (…_0, e.g. X_0/N_0/x1_0) are NOT perturbed by default; to estimate them pass them explicitly in estimate
- SECURITY: ONLY the built-in templates are exposed; there is no way to supply custom C dynamics (the compile/eval surface is blocked)

### References

- King, Nguyen & Ionides, 'Statistical Inference for Partially Observed Markov Processes via the reference Package pomp', JSS 2016 <
- help('pfilter','pomp'), help('mif2','pomp'), help('gompertz','pomp'), help('ricker','pomp'), help('ou2','pomp')
- Ionides, Nguyen, Atchadé, Stoev & King 2015, 'Inference for dynamic and latent variable models via iterated, perturbed Bayes maps', PNAS 112(3):719 (the IF2 algorithm)
- Arulampalam et al. 2002, IEEE Trans. Signal Processing 50(2):174 (the bootstrap particle filter)

## #186 — BEAST — a Bayesian decomposition into trend + seasonality + change points with posterior change probabilities

**Module:** `beast_bayesian_decomposition.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `beast_decompose` | `y` | `num_array`, `enum`, `integer`, `int_array`, `int_array`, `integer`, `integer`, `integer`, `integer` | `season='harmonic'`, `tcp_minmax=[0, 10]`, `scp_minmax=[0, 10]`, `mcmc_samples=2000`, `mcmc_burnin=200`, `mcmc_chains=1`, `seed=2025` | `light` | `object` |
| `beast_changepoints` | `object` | `raw_handle`, `enum`, `number` | `component='trend'`, `threshold=0` | `light` | — |

### Use when

you want to decompose a regular series into trend + seasonality AND simultaneously locate structural breaks / change points with PROBABILITIES (a posterior), not a point decision; ideal when the number/location of the breaks is unknown and you want uncertainty per time point

### Do not use when

irregular/unevenly sampled data (that needs beast.irreg, outside the node scope); a pure output-gap/potential-output estimate (#56 mFilter / #92 hpfilter); one KNOWN break at a known date (#4 Chow/strucchange); a state-space model with an explicit UC structure (#58 KFAS / #59 dlm)

### Prerequisites

- beast_decompose (the PRODUCER: run it first to obtain the fitted beast handle)
- beast_changepoints (the CONSUMER: extracting change-point positions + probabilities with a threshold)
- c00_data_utilities/reading_delimited_fixed.read_delimited (loading the series from a file -> num_array)

### Alternatives

| instead use | when |
| --- | --- |
| #56 mFilter (mfl_hp_filter/mfl_bk_filter) | you only want a trend/cycle gap without change-point uncertainty |
| strucchange / Bai-Perron (#4 structural) | a frequentist multiple-break test with explicit break dates + SC/BIC |
| #58 KFAS / #59 dlm | an explicit linear-Gaussian state-space UC model (level+slope+seasonal) with smoothing |
| prophet-style models | outside the engine — only a point forecast without posterior break probabilities |

### Output fields

- trend$Y / trend$SD: the fitted trend + the posterior SD per time point (a chart-data band)
- trend.cpOccPr: the per-time posterior change-probability curve (of length n, ∈[0,1]) — the MAIN chart-data
- trend.cp / trend.cpPr / trend.cpCI: the change-point positions (in decreasing Pr), the probability of each, the credible interval of the position
- trend.ncp / ncp_median / ncp_mode: the posterior distribution of the number of change points
- season_component$Y + .cpOccPr + .amp: the seasonal component + the seasonal change probability (NULL if season='none')
- R2 / RMSE / marg_lik / sig2: goodness of fit + the marginal likelihood + the noise
- beast_changepoints: n_cp/cp/cpPr filtered by a threshold (with no NaN padding)

### Pitfalls

- ncp is a posterior MEAN (non-integer, e.g. 0.14) — NOT a fixed number of breaks; read ncp_median/ncp_mode + cpPr for a decision
- cp is returned with NaN padding at the end (the maximum slots); the wrapper already filters it — do not read the raw slots
- an NA in y does not fail in BEAST — it INTERPOLATES silently; the wrapper blocks it (a hard gate) for determinism
- harmonic/dummy seasonality WITHOUT a period -> BEAST silently guesses the periodicity (non-deterministic); the wrapper requires it explicitly
- cpOccPr (the per-time curve) ≠ cpPr (per detected cp): the former is the chart-data, the latter is the probability of the top change points
- stochastic MCMC: the same seed ⇒ an identical result; the default seed=2025

### References

- help('beast', 'Rbeast') — Rbeast 1.0.2 (season/period/tcp.minmax/scp.minmax/mcmc.*)
- Zhao, Wulder et al. 2019, 'Detecting change-point, trend, and seasonality in satellite time series data..', Remote Sensing of Environment 232:111181 (the BEAST algorithm)
- live introspection: the beast output .trend/.season fields (cpOccPr/cp/cpPr/cpCI/ncp), reproducibility through mcmc.seed

## #187 — Seasonal-Trend decomposition using Regression (AutoSTR) — trend + multiple/complex seasonality + remainder with CIs per component

**Module:** `seasonal_trend_decomposition.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `str_decompose` | `y` | `series_handle`, `integer`, `boolean`, `integer`, `number`, `num_array`, `integer` | `robust=False`, `confidence=0.95`, `seed=2025` | `light` | `object` |
| `str_seasadj` | `object` | `raw_handle`, `raw` | — | `light` | — |

### Use when

a univariate seasonal series (ts/msts); you want a trend + (possibly multiple) seasonal components with confidence intervals, and/or the seasonally adjusted series; robust to outliers (robust=TRUE)

### Do not use when

a non-seasonal series (frequency<2 -> the mFilter trend filters); forecasting (STR does not forecast — state space #58-60/ARIMA); latent common factors across several series (#61 MARSS DFA); manual custom predictors/covariates (that needs the low-level STR, outside the node)

### Prerequisites

- str_decompose (it produces the STR object; NA/non-seasonality/length are hard gates)
- str_seasadj (the seasonally adjusted series; include must be a subset of the component names)
- c00_data_utilities/reading_delimited_fixed.read_delimited (loading the series from a file before building the ts)

### Alternatives

| instead use | when |
| --- | --- |
| #56 mFilter (mfl_hp_filter) | a non-seasonal series — only a trend/cycle decomposition (the output gap) |
| #61 MARSS DFA (marss_dfa) | common latent trends across MANY series, not one |
| #59 dlm (dl_local_linear_trend, seasonal=TRUE) | a state-space trend+seasonal model with forecasting/filtering |
| confidence=NULL | you do not need CIs — a faster decomposition |

### Output fields

- components: a named list of numeric vectors (Data/Trend/Seasonality <period>../Random) — chart-data
- component_names: the column order; n_seasonal: the number of seasonal components (>1 for msts)
- confidence_intervals: per predictor component {lower,upper} (NULL when confidence=NULL)
- fitted: {fitted,lower,upper}, the overall fit CI (NULL when confidence=NULL)
- cvMSE: the CV MSE of the lambda selection (NA on the robust path); the robust/confidence flags
- seasadj (str_seasadj): the seasonally adjusted series = the sum of the included components (default Trend+Random)

### Pitfalls

- seasadj.STR SILENTLY ignores unknown include names (a warning + skip) -> the node blocks them with a hard gate
- AutoSTR silently accepts NA -> the node requires a complete series (an NA gate)
- the seasonal component names are 'Seasonality <period>' (e.g. 'Seasonality 12'); msts -> several of them
- cvMSE = NA on the robust path (the package does not return a CV MSE) — do not read it as a perfect fit
- STR is a decomposition, NOT a forecast; to forecast, apply state space/ARIMA to the seasadj series

### References

- Dokumentov & Hyndman, 'STR: Seasonal-Trend decomposition using Regression', INFORMS J. Data Science 2022
- the stR vignette + help('AutoSTR','stR'), help('components','stR'), help('seasadj','stR') (stR 0.7.1)
- Hyndman & Athanasopoulos, Forecasting: Principles and Practice 3rd ed. §3.7 (STL/STR decomposition)

## #188 — STL decomposition (seasonal-trend-loess) tolerant of NA + short series

**Module:** `stl_decomposition_tolerant.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `stlplus_decompose` | `x` | `series_handle`, `integer`, `string`, `integer`, `integer`, `integer`, `integer`, `integer` | `s_window='periodic'`, `s_degree=1`, `t_degree=1`, `inner=2`, `outer=1` | `light` | — |

### Use when

a univariate seasonal series; you want a seasonal/trend/remainder decomposition when there are NA (gaps) or the series is short/does not contain a whole number of periods

### Do not use when

multiple/changing seasonality (-> seasonal X-13 or STL with multiple s.window); a structural state-space model with uncertainty (#58 KFAS/#59 dlm); a pure trend/cycle output gap (#56 mFilter/#92 hpfilter)

### Prerequisites

- c00_data_utilities/reading_delimited_fixed.read_delimited (loading the series when it is not already a ts handle)
- stlplus_decompose (the decomposition itself; the robustness weights reveal outliers)

### Alternatives

| instead use | when |
| --- | --- |
| stl (base) | no NA + complete whole periods; then base stl suffices |
| #56 mFilter (HP/BK/CF) | you want only trend/cycle (the output gap), not a seasonal term |
| seasonal X-13-ARIMA-SEATS | an official seasonal adjustment with calendar/outlier regressors |

### Output fields

- seasonal/trend/remainder: numeric vectors of length n (raw = seasonal+trend+remainder at the non-NA points)
- raw: the original series (with NA at the gaps); weights: the outer-loop robustness weights (0.1, low = outliers)
- time: the numeric time index; n_obs/n_missing: the number of observations / NA
- n.p/periodic/s.window/t.window/l.window/s.degree/t.degree: the final parameters that were used

### Pitfalls

- an even s.window/t.window is SILENTLY rounded to the next odd value by stlplus; the wrapper blocks it (an explicit odd-number gate) so you do not think that what you passed was used
- s.window='periodic' -> it forces s.degree=0 & an enormous internal span (the seasonality is fixed); for an evolving seasonality supply a finite odd s.window
- trend/seasonal contain NO NA even when raw does (block interpolation); the remainder is NA at the original gaps
- low weights (~0) mark points that the robust loop down-weighted as outliers, not an error
- s.degree=1/2 requires enough points per subseries; for very short series prefer s.window='periodic'

### References

- Cleveland, Cleveland, McRae & Terpenning 1990 (STL), J. Official Statistics 6:3-73
- live introspection (btw): args(stlplus), the .data/.pars.win structure, edge-case probes

## #189 — Nonparametric detrending & output gap (loess / smoothing spline / Friedman super-smoother)

**Module:** `nonparametric_detrending_output.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `np_detrend` | `y` | `num_array`, `num_array`, `enum`, `number`, `integer`, `number`, `boolean` | `span=0.75`, `degree=2`, `cv=False` | `light` | — |
| `np_output_gap` | `y` | `num_array`, `num_array`, `enum`, `enum`, `number`, `integer`, `number`, `boolean` | `span=0.75`, `degree=2`, `cv=False` | `light` | — |

### Use when

you want a trend/cycle or output gap without a parametric trend form; a smooth, data-driven detrending of a series (loess/smooth.spline/supsmu); a fast atheoretical benchmark for the gap

### Do not use when

you want economic structure/potential output with shocks (KFAS/dlm/MARSS #58-61); a band-pass cycle at a specific frequency (mFilter BK/CF #56); a real-time/one-sided gap with no end-point revision (one-sided hpfilter #92, Hamilton #57); very short series (n<4)

### Prerequisites

- np_detrend (get the trend+cycle; check that the cycle looks mean-≈0 and stationary)
- c00_data_utilities/reading_delimited_fixed.read_delimited (load the series from a file before detrending)

### Alternatives

| instead use | when |
| --- | --- |
| #56 mfl_hp_filter / mfl_bk_filter / mfl_cf_filter | you want an HP or band-pass cycle at a defined frequency rather than a free non-parametric trend |
| #92 hp_one_sided | you need a real-time (one-sided) gap with no revision of the end points |
| #57 hf_filter (Hamilton) | you want a regression-based filter without the HP spurious-cycle problem |
| #58-61 KFAS/dlm/bssm/MARSS | you want a structural unobserved-components/state-space potential output with shocks & credible bands |
| method='smooth.spline' (GCV) | you want automatic smoothing selection instead of a manual span |

### Output fields

- trend: numeric, of the same length as y (the non-parametric trend; chart-data)
- cycle: y - trend (np_detrend; the cyclical component / gap in levels)
- gap: the output gap by mode (np_output_gap; pct=% deviation, log=100*the log difference, level=y-trend)
- smoother: the parameters per method — loess {span,degree,equivalent_df}; smooth.spline {spar,lambda,df,crit,cv}; supsmu {span}
- x/y/n: the index, the original series, the number of observations

### Pitfalls

- atheoretical: the gap is statistical, NOT economic potential output — do not interpret it as structural
- end-point instability: loess/smooth.spline are two-sided -> the ends of the trend/gap are revised as new data arrive (as with the HP filter); for real-time work use #92/#57
- a higher smooth.spline spar => a less flexible trend (a larger gap); a higher span in loess/supsmu => a smoother trend; the smoothing choice determines the amplitude of the gap
- mode='pct' requires trend != 0; mode='log' requires y>0 & trend>0 (explicit gates; for rates/growth around 0 use mode='level')
- supsmu sorts x internally; the trend is realigned back to the original order (approx) so that cycle = y - trend is correct

### References

- help('loess','stats'), help('smooth.spline','stats'), help('supsmu','stats') (the reference stats reference)
- Cleveland, Grosse & Shyu 1992 (loess, local regression); Friedman 1984 SLAC PUB-3477 (the super smoother)
- Hastie, Tibshirani & Friedman 2009 ESL §5 (smoothing splines, GCV)
- Hamilton 2018 REStat 100:831 (the HP critique -> the motivation for atheoretical benchmarks)
