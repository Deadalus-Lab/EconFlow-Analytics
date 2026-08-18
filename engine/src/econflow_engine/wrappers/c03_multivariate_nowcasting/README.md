<!-- SPDX-License-Identifier: AGPL-3.0-only -->
# 03-multivariate-nowcasting

14 METHOD-SELECTION cards, 14 modules, 55 nodes.

Every card below governs one wrapper module in this package. The cards are the
reason a method exists here at all: they record when it applies, what to reach
for instead, and the traps that make its output easy to misread.

## #11 — Reduced-form VAR (lag select + Granger + diagnostics + vec2var)

**Module:** `reduced_form_var.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `vr_varselect` | `y` | `multiseries_handle`, `integer`, `enum` | `lag_max=10` | `light` | — |
| `vr_var` | `y` | `multiseries_handle`, `integer`, `enum` | `p=1` | `light` | `model` |
| `vr_predict` | `model` | `raw_handle`, `integer`, `number` | `n_ahead=10`, `ci=0.95` | `light` | — |
| `vr_causality` | `model`, `cause` | `raw_handle`, `string`, `boolean`, `integer` | `boot=False`, `boot_runs=100` | `heavy` | — |
| `vr_serial_test` | `model` | `raw_handle`, `integer`, `integer`, `enum` | `lags_pt=16`, `lags_bg=5` | `light` | — |
| `vr_arch_test` | `model` | `raw_handle`, `integer`, `integer`, `boolean` | `lags_single=16`, `lags_multi=5`, `multivariate_only=True` | `light` | — |
| `vr_normality_test` | `model` | `raw_handle`, `boolean` | `multivariate_only=True` | `light` | — |
| `vr_vec2var` | `z` | `raw_handle`, `integer` | `r=1` | `light` | `model` |

### Use when

2-6 stationary series, frequentist VAR: IC lag selection, forecasting, Granger, residual diagnostics; vec2var bridges VECM->level VAR

### Do not use when

many series (dfms/BVAR); a short sample that needs shrinkage; mixed-frequency (mfbvar/midasr); structural shocks IRF/FEVD (c04_structural_shocks/svar_irf_fevd)

### Prerequisites

- c01_preparation_prechecks/unit_root_normality.run_adf_test
- c01_preparation_prechecks/unit_root_normality.run_kpss_test

### Alternatives

| instead use | when |
| --- | --- |
| BVAR/bvartools (#12/#13) | medium n or a short sample -> Minnesota shrinkage |
| dfms (#15) | large n -> factor structure |
| bvarsv (#14) | time-varying parameters/volatility |
| c04_structural_shocks/svar_irf_fevd (#19) | you want identified shocks (IRF/FEVD) |

### Output fields

- selection/criteria: the suggested p per AIC/HQ/SC/FPE
- stable: all(moduli(roots)<1) -- a critical post-check for reliable IRF/FEVD
- fcst: list per variable fcst/lower/upper/CI (fan-chart data)
- Granger/Instant: htest {statistic,p_value,parameter,method}
- serial/arch/jb: htest residual diagnostics

### Pitfalls

- Granger = predictive causality, NOT structural; H0='does not cause', p<0.05 -> predictive causality
- the vars stability post-check (stable=TRUE) is required for reliable IRF/FEVD
- diagnostics have H0='clean residuals': p<0.05 -> mis-specification (increase p)
- the Granger test is problematic if the series are non-stationary (vars ref)

### References

- Enders 2015
- vars 1.6-1 ref (Pfaff)
- Granger 1969
- Lutkepohl 2006
- Hamilton 1994

## #12 — Bayesian VAR (Minnesota prior)

**Module:** `bayesian_var.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `bvar_estimate` | `data` | `multiseries_handle`, `integer`, `integer`, `integer`, `integer`, `number`, `integer` | `lags=1`, `n_draw=10000`, `n_burn=5000`, `n_thin=1`, `lambda=0.2` | `mcmc` | `model` |
| `bvar_predict` | `model` | `raw_handle`, `integer`, `number` | `horizon=12`, `conf_bands=0.16` | `light` | — |
| `bvar_irf` | `model` | `raw_handle`, `integer`, `boolean`, `boolean` | `horizon=12`, `identification=True`, `fevd=False` | `light` | — |
| `bvar_fevd` | `model` | `raw_handle`, `integer` | `horizon=12` | `light` | — |
| `bvar_companion` | `model` | `raw_handle` | — | `light` | — |
| `bvar_summary` | `model` | `raw_handle` | — | `light` | — |

### Use when

a multivariate VAR on a short/medium sample; hierarchical Minnesota shrinkage (GLP 2015); IRF by Cholesky or sign restrictions; posterior fan charts

### Do not use when

mixed-frequency (mfbvar); TVP/SV (bvarsv); very large n (dfms); you want frequentist p-values (vars)

### Prerequisites

- c01_preparation_prechecks/unit_root_normality.run_adf_test
- c01_preparation_prechecks/unit_root_normality.run_kpss_test

### Alternatives

| instead use | when |
| --- | --- |
| bvartools (#13) | you want an explicit Gibbs sampler + gir/sir IRF types |
| vars (#11) | frequentist Granger/diagnostics, sample large enough |
| bvarsv (#14) | changing volatility/parameters |

### Output fields

- acceptance_rate: MH tuning diagnostic (~0.20-0.40)
- predict.quants: array [quantiles x horizon x variables] chart-ready
- irf.quants: array [quantiles x horizon x impulse x response]
- companion.stable: modulus<1
- summary.coef: posterior median (not MLE)

### Pitfalls

- bvar_irf post-gate: all-NA quants -> sign/zero identification failed (stop); sign_restr MxM in {1,-1,0,NA}
- coef is the posterior median, not a point MLE
- S3 collision with bvartools: predict/irf/summary.bvar are called namespaced (asNamespace BVAR)
- the seed is mandatory (bvar has no seed argument -> set.seed in the wrapper)
- stationarity is methodological, NOT a hard gate: the Minnesota prior centres the 1st own lag at 1 (RW; bv_minnesota(b=1), fixed; the wrapper does not expose b) -> apply it to LEVELS/log-levels (typically I(1)), do NOT difference beforehand (differencing I(1) with b=1 = a de facto I(2) prior, over-shrinkage); the I(d) check is for cointegration awareness (I(1)&cointegrated -> consider a VECM ca.jo), not for differencing

### References

- BVAR 1.0.5 (Kuschnig & Vashold 2021 JSS)
- Giannone-Lenza-Primiceri 2015
- BVAR vignette introduction

## #13 — Bayesian VAR (Gibbs sampler)

**Module:** `bayesian_var_2.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `bt_var` | `data` | `multiseries_handle`, `integer`, `enum`, `integer`, `integer`, `integer` | `p=2`, `iterations=10000`, `burnin=5000` | `mcmc` | `model` |
| `bt_predict` | `model` | `raw_handle`, `integer`, `number`, `integer` | `n_ahead=10`, `ci=0.95` | `heavy` | — |
| `bt_irf` | `model`, `impulse`, `response` | `raw_handle`, `string`, `string`, `integer`, `number`, `enum`, `boolean` | `n_ahead=5`, `ci=0.95`, `cumulative=False` | `light` | — |
| `bt_fevd` | `model`, `response` | `raw_handle`, `string`, `integer`, `enum` | `n_ahead=5` | `light` | — |
| `bt_summary` | `model` | `raw_handle`, `number` | `ci=0.95` | `light` | — |

### Use when

a Bayesian VAR with an explicit, transparent Gibbs pipeline (gen_var->add_priors->draw_posterior); flexible IRF/FEVD types feir/oir/gir/sir/sgir

### Do not use when

you want a ready-made hierarchical Minnesota, auto-tuned (BVAR); mixed-frequency (mfbvar); TVP/SV (bvarsv)

### Prerequisites

- c01_preparation_prechecks/unit_root_normality.run_adf_test
- c01_preparation_prechecks/unit_root_normality.run_kpss_test

### Alternatives

| instead use | when |
| --- | --- |
| BVAR (#12) | hierarchical Minnesota + sign restrictions with minimal tuning |
| vars (#11) | frequentist workflow + Granger |

### Output fields

- predict.fcst: list of ts per variable [n.ahead x 3] lower/median/upper
- irf: bvarirf ts [0.n.ahead x 3] median+CI
- fevd: ts [0.n.ahead x n_vars], rows sum to ~1
- summary.coefficients/sigma: posterior stats

### Pitfalls

- type: feir=non-orthogonalised; oir=Cholesky (order-dependent); gir=generalized (order-independent); sir/sgir=structural
- data MUST be of class ts/mts (not a matrix)
- two MCMC seeds: draw_posterior AND predict.bvar
- S3 collision: bvartools methods are namespaced (asNamespace bvartools); also summary.dfm collides with dfms

### References

- bvartools 0.2.4
- bvartools vignette bvar (Mohr)
- Pesaran & Shin 1998 (generalized IRF)
- Lutkepohl 2006

## #14 — TVP-VAR with Stochastic Volatility

**Module:** `tvp_var_stochastic.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `sv_estimate` | `Y` | `multiseries_handle`, `integer`, `integer`, `integer`, `integer`, `integer`, `integer`, `integer` | `p=1`, `tau=40`, `nf=10`, `nrep=50000`, `nburn=5000`, `thinfac=10` | `heavy` | `model` |
| `sv_predict_density` | `model` | `raw_handle`, `integer`, `integer`, `integer`, `boolean` | `variable=1`, `horizon=1`, `n_grid=101`, `cdf=False` | `heavy` | — |
| `sv_predict_draws` | `model` | `raw_handle`, `integer`, `integer` | `variable=1`, `horizon=1` | `heavy` | — |
| `sv_irf` | `model` | `raw_handle`, `integer`, `integer`, `integer`, `integer` | `impulse=1`, `response=2`, `horizon=20`, `scenario=2` | `light` | — |
| `sv_parameter_draws` | `model` | `raw_handle`, `string`, `integer`, `integer` | `type='lag1'`, `row=1`, `col=1` | `light` | — |

### Use when

relationships/volatility change over time (TVP + stochastic volatility); posterior predictive distributions; IRF at each point in time t

### Do not use when

a small sample (heavily parameterized); constant coefficients (BVAR/vars); many series (2-4 variables in practice)

### Prerequisites

- c01_preparation_prechecks/unit_root_normality.run_adf_test
- c01_preparation_prechecks/unit_root_normality.run_kpss_test

### Alternatives

| instead use | when |
| --- | --- |
| BVAR/bvartools (#12/#13) | constant coefficients suffice -> far cheaper |
| 10-trend-cycle-statespace (KFAS/dlm/bssm) | a general custom state-space TVP |
| MSwM (Markov-switching, outside the category) | discrete regimes -- CAUTION, MSwM is gaussian/lm only |

### Output fields

- predict_density: {grid,value} -- the closure f(z) evaluated on a grid (cdf optional)
- predict_draws: draws + quantiles (fan chart) + mean
- irf: [draws x nhor] + bands [probs x nhor]; contemporaneous
- parameter_draws: [draws x time] coefficient path (drift inspection)

### Pitfalls

- predictive.density returns a FUNCTION -> it is NEVER returned; it is evaluated on a grid
- scenario: 1=no orthogonalization, 2=Cholesky(t) default, 3=DNP variant
- requires save.parameters=TRUE (always ON) for irf/parameter.draws
- tau is the LS-prior training split: ncol*p+1 <= tau < nrow

### References

- bvarsv 1.1 (Krueger)
- Primiceri 2005 ReStud
- Del Negro & Primiceri 2015 corrigendum

## #15 — Dynamic Factor Model / nowcasting (routes #16)

**Module:** `dynamic_factor_nowcasting.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `df_icr` | `X` | `multiseries_handle`, `integer` | — | `light` | — |
| `df_dfm` | `X` | `multiseries_handle`, `integer`, `integer`, `boolean`, `enum`, `enum` | `p=1`, `idio_ar1=False` | `light` | `model` |
| `df_predict` | `model` | `raw_handle`, `integer`, `boolean` | `h=10`, `standardized=False` | `light` | — |
| `df_summary` | `model` | `raw_handle` | — | `light` | — |

### Use when

many series with few common factors; nowcast with ragged edges/missing data (BM EM) and mixed frequency (quarterly.vars); rule-based r from Bai-Ng ICr

### Do not use when

few series (a VAR is more natural); you want a Bayesian mixed-freq VAR with latent monthly states (mfbvar); one low-freq y from one regressor (midasr)

### Prerequisites

- c01_preparation_prechecks/unit_root_normality.run_adf_test
- c01_preparation_prechecks/unit_root_normality.run_kpss_test

### Alternatives

| instead use | when |
| --- | --- |
| mfbvar (#17) | you want a full Bayesian posterior + steady-state prior in mixed frequency |
| BVAR (#12) | medium n, full VAR dynamics instead of a factor summary |
| midasr (#18) | one dependent variable, few high-freq regressors |

### Output fields

- df_icr.r_star: vector of length 3 (IC1/IC2/IC3 Bai-Ng); IC table; eigenvalues
- df_dfm.factors: T x r factors (QML/2S/PCA); loadings C; transition A; Q/the reference
- df_dfm.converged: EM post-check (does not block)
- df_predict$X_fcst: h x n nowcast/forecast (original units); F_fcst factors
- df_summary$R2: share of variance from the common component per series

### Pitfalls

- the 3 ICs often disagree; IC2 has the largest penalty -> the most parsimonious r (auto default)
- factors/loadings are identified only up to rotation/sign (the factor sign has no absolute interpretation)
- standardization happens INTERNALLY -> NO pre-scaling of the input
- df_icr & auto-r require X without NA (PCA); an explicit r allows NA (BM EM)
- S3 collision: summary.dfm is namespaced (asNamespace dfms) -- bvartools defines the same name

### References

- dfms 1.0.1 (rOpenSci)
- Bai & Ng 2002 Econometrica
- Doz-Giannone-Reichlin 2011/2012
- Banbura & Modugno 2014
- Stock & Watson 2016

## #17 — Mixed-Frequency Bayesian VAR

**Module:** `mixed_frequency_bayesian.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `mf_estimate` | `Y`, `n_lags` | `raw_handle`, `integer`, `integer`, `integer`, `integer`, `enum`, `enum`, `enum`, `integer` | `n_reps=10000`, `n_fcst=0` | `heavy` | `model` |
| `mf_predict` | `model` | `raw_handle`, `number`, `boolean` | `pred_bands=0.8`, `aggregate_fcst=True` | `light` | — |
| `mf_mdd` | `model` | `raw_handle`, `number`, `integer` | `p_trunc=0.5`, `method=1` | `light` | — |

### Use when

a Bayesian VAR with series of different frequencies (monthly indicators + quarterly GDP); nowcast with latent monthly states + a steady-state prior (Schorfheide-Song)

### Do not use when

all series at the same frequency (BVAR/bvartools); very large n (dfms); one dependent variable driven by high-freq regressors (midasr)

### Prerequisites

- c01_preparation_prechecks/unit_root_normality.run_adf_test
- c01_preparation_prechecks/unit_root_normality.run_kpss_test

### Alternatives

| instead use | when |
| --- | --- |
| dfms (#15) | many indicators, factor nowcast (frequentist EM, faster) |
| midasr (#18) | you target one low-freq variable with few regressors |
| BVAR (#12) | same frequency, no latent states |

### Output fields

- mf_predict.forecast: data_frame variable/time/fcst_date/lower/median/upper (list of records)
- mf_mdd.log_mdd: log marginal data density (higher=better) for model comparison
- mf_estimate: prior/variance/aggregation echo; model (mfbvar) stub

### Pitfalls

- Y = a list of ts, monthly FIRST, quarterly last; NA only at the end (ragged edge)
- aggregation='average' -> n_lags>=3
- mf_mdd ONLY for variance='iw' (class _iw gate); ss->method{1,2}, minn->p_trunc(0,1)
- the ss/ssng prior requires prior_psi_mean&Omega (or prior_psi_int); fsv->n_fac
- masking: set_prior explicitly (set_prior masks it in the suite env)

### References

- mfbvar 0.5.6 ( archive)
- Schorfheide & Song 2015 JBES
- Ankargren et al. (steady-state/FSV)
- mfbvar vignette

## #18 — MIDAS regression (mixed data sampling)

**Module:** `midas_regression.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `md_midas` | `y`, `x`, `m` | `raw_handle`, `raw_handle`, `integer`, `integer`, `enum`, `integer`, `boolean` | `k=7`, `poly_degree=2`, `trend=False` | `light` | `model` |
| `md_haht` | `model` | `raw_handle`, `boolean` | `robust=False` | `light` | — |
| `md_forecast` | `model`, `newx`, `m` | `raw_handle`, `raw_handle`, `integer` | — | `light` | — |
| `md_select` | `y`, `x`, `m` | `raw_handle`, `raw_handle`, `integer`, `integer`, `enum`, `integer`, `boolean` | `k=7`, `poly_degree=2`, `trend=False` | `light` | — |

### Use when

forecasting one low-freq variable (quarterly GDP) from high-freq regressor(s) (monthly/daily) through a parametric weight scheme (nealmon/nbeta/almonp)

### Do not use when

many interacting series/a system (the VAR family); nowcast from many indicators (mfbvar/dfms); same frequency (ARDL)

### Prerequisites

- c01_preparation_prechecks/unit_root_normality.run_adf_test

### Alternatives

| instead use | when |
| --- | --- |
| mfbvar (#17) | you want a mixed-freq VAR system + posterior + latent states |
| dfms (#15) | many high-freq indicators -> factor summary |
| ARDL (category 05) | same frequency, no weight scheme |

### Output fields

- md_midas.midas_coefficients: implied weights theta (the shape over high-freq lags -- the interpretable part)
- md_midas.converged: NLS post-check (non-convergence is flagged, it does not block)
- md_haht: htest {statistic,df,p_value,method}; H0=the weight scheme is adequate
- md_forecast: mean/lower/upper/level (newx of length h*m)
- md_select.best: rule-based weight selection by AIC/BIC (not by the LLM)

### Pitfalls

- md_haht H0='the restriction is adequate': p<0.05 -> REJECTION -> the scheme is wrong (Kvedaras-Zemlys)
- the determining condition is length(x)==m*length(y); formula/data/start are built INTERNALLY (LLM safety)
- start must have the right length per scheme: nealmon=3, nbeta=4, almonp=deg+1
- NLS is deterministic for given start values -> no seed

### References

- midasr 0.9
- Kvedaras & Zemlys 2012 Economics Letters
- Ghysels-Santa-Clara-Valkanov (MIDAS)
- midasr vignette (JSS 2016)

## #142 — High-dimensional penalized VAR (structured penalties + rolling-CV lambda)

**Module:** `high_dimensional_penalized.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `bvr_fit` | `Y` | `multiseries_handle`, `integer`, `enum`, `int_array`, `integer`, `enum`, `integer`, `integer`, `boolean`, `boolean` | `p=1`, `h=1`, `IC=True`, `ONESE=False` | `light` | `model` |
| `bvr_predict` | `model` | `raw_handle`, `integer`, `boolean` | `n_ahead=1`, `confint=False` | `light` | — |
| `bvr_coef` | `model` | `raw_handle` | — | `light` | — |

### Use when

a multivariate VAR with a large k·p relative to T (an OLS VAR over-fits); a structured VARX-L/HLAG penalty + rolling-OOS selection of lambda; a data-driven lag order (HLAG)

### Do not use when

a short sample with Minnesota shrinkage in levels + fan charts (BVAR #12); frequentist Granger/p-values (vars #11); a very large n with factor structure (dfms #15); mixed frequency (mfbvar)

### Prerequisites

- c01_preparation_prechecks/unit_root_normality.run_adf_test
- c01_preparation_prechecks/unit_root_normality.run_kpss_test

### Alternatives

| instead use | when |
| --- | --- |
| BVAR (#12) | a short sample, Bayesian shrinkage in LEVELS + posterior fan charts |
| vars (#11) | a small k·p, you want frequentist Granger/IRF/diagnostics |
| dfms (#15) | a very large n with few common factors |

### Output fields

- optimal_lambda: the best lambda (minimum in-sample MSFE); oos_msfe = the OOS MSFE on the test set (vs mean/RW/AIC/BIC)
- coefficients: a k x (kp+1) sparse matrix (intercept + Y{i}L{l}); sparsity = the share of zeros
- predict.forecast: an n.ahead x k path (built step by step); confint=TRUE -> lower/upper 95% CI
- model: the BigVAR.results producer handle -> bvr_predict/bvr_coef

### Pitfalls

- stationarity: BigVAR shrinks towards ZERO (MN=FALSE by default, NOT an RW prior) -> apply it to STATIONARY data, difference I(1) series FIRST (the opposite of BVAR #12, which wants levels); I(1)&cointegrated -> consider a VECM ca.jo
- BigVAR DISCARDS colnames(Y): the variables are Y1.Yk (position=column order), consistently across fit/predict/coef -> map positions in the frontend
- struct: EFX is VARX ONLY (a pure VAR -> stop); HLAG*/Tapered are VAR-only; the non-convex MCP/SCAD are out of scope
- predict.BigVAR.results by itself returns only the final horizon (k x 1); the wrapper builds the full n.ahead x k path step by step
- gran = c(penalty_grid_depth, number_of_lambda), two positive integers; too few rows for the rolling-CV window -> a clean stop (too few rows)
- S4 collision: BigVAR calls setGeneric on predict/coef; the wrapper calls selectMethod(g,'BigVAR.results') explicitly; conflicts(detail=TRUE) is empty, with no effect on the sibling S3 predict/coef
- determinism: penalized (convex) + rolling/LOO CV = deterministic, no seed

### References

- BigVAR 1.1.5 reference/vignette
- Nicholson-Wilms-Bien-Matteson 2020 JMLR 21(166) High-dim forecasting via interpretable VAR
- Nicholson-Matteson-Bien 2017 IJF 33(3):627-651 VARX-L
- Banbura-Giannone-Reichlin 2010 (BGR)

## #143 — Hierarchical global-local shrinkage Bayesian VAR + stochastic volatility (HS/DL/R2D2/NG/SSVS priors, posterior fan charts + LPL)

**Module:** `hierarchical_global_local.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `bvs_estimate` | `data`, `seed` | `matrix_handle`, `integer`, `enum`, `integer`, `integer`, `integer`, `enum`, `integer`, `integer`, `number`, `boolean` | `lags=1`, `draws=200`, `burnin=100`, `thin=1`, `min_draws=100`, `ess_min=1`, `allow_nonconvergence=False` | `mcmc` | `model` |
| `bvs_predict` | `model`, `seed` | `raw_handle`, `integer`, `boolean`, `num_array`, `boolean`, `matrix_handle`, `integer` | `ahead=4`, `stable=True`, `LPL=False` | `light` | — |
| `bvs_irf` | `model` | `raw_handle`, `integer`, `num_array` | `ahead=8` | `light` | — |

### Use when

a multivariate BVAR (small to medium k) with global-local shrinkage that adapts sparse-vs-dense in a data-driven way (HS/DL/R2D2/NG/SSVS/normal on Phi) + stochastic volatility; posterior median/quantiles, predictive fan charts, LPL density forecasts

### Do not use when

a Minnesota RW prior in LEVELS + an IRF/FEVD toolkit (BVAR #12); frequentist penalized rolling-CV (BigVAR #142); TVP coefficients (bvarsv); mixed frequency (mfbvar #17); a large-n factor model (dfms #15 / sparseDFM #144); structural identification (04-structural-shocks; bvs_irf is reduced-form)

### Prerequisites

- c01_preparation_prechecks/unit_root_normality.run_adf_test
- c01_preparation_prechecks/unit_root_normality.run_kpss_test

### Alternatives

| instead use | when |
| --- | --- |
| 03-multivariate-nowcasting/bvar_estimate | a Minnesota RW prior in LEVELS + a ready-made IRF/FEVD/companion/sign-restrictions toolkit |
| 03-multivariate-nowcasting/bvr_fit | a frequentist penalized VAR-L, rolling-OOS lambda, deterministic (no posterior) |
| 03-multivariate-nowcasting/sv_estimate | time-varying coefficients (TVP-VAR) + SV |
| bvs_irf | reduced-form posterior impulse responses from the same fit |

### Output fields

- phi_median: the posterior median Phi (K x M); phi_quantiles: an nq x K x M grid (2.5/25/50/75/97.5%)
- convergence: n_retained/min_ess/n_stable/phi_finite/min_draws/ess_min/seed; converged + nonconvergence_reasons
- model: the bayesianVARs_bvar producer handle -> bvs_predict/bvs_irf (register field=model, bucket=rds)
- bvs_predict.quants: an nq x horizon x M predictive fan grid; mean: horizon x M; LPL/LPL_univariate when LPL=TRUE (density forecast)
- bvs_irf.irf_median: M x shocks x horizon; irf_quantiles: nq x M x shocks x horizon (reduced-form bands)

### Pitfalls

- stationarity: specify_prior_phi with priormean=0 shrinks towards ZERO (like BigVAR #142, NOT an RW prior in levels like BVAR #12) -> use STATIONARY/growth data, difference I(1) series FIRST; ADF/KPSS precheck
- single-chain convergence: there is NO split-Rhat -> the gate is on retained/stable draws + DEGENERATE cases (all-NA ESS when the sampler is stuck, non-finite Phi, 0 stable draws) count as non-convergence; allow_nonconvergence overrides (mirroring rstan/MARSS); a low ESS with TINY draw counts is NOT an error -> raise the number of draws
- masking: library(bayesianVARs) is NOT used — it exports the generics bvar/irf, which mask the BVAR/vars siblings; every call is bayesianVARs::*; the class 'bayesianVARs_bvar' is unique (≠ 'bvar') -> the S3 dispatch does not clash
- determinism: bvar/predict are stochastic with NO seed argument -> the seed is MANDATORY, set.seed before the sampling (live-verified: seed=42 gives an identical PHI, predict with seed=7 is identical); irf is deterministic
- LPL: Y_obs must be the [ahead x M] realised values (a wrong dimension -> an upstream recycling warning; the wrapper blocks it); bvs_irf is reduced-form (shocks=1, no orthogonalization) -> structural shocks live in 04-structural-shocks

### References

- bayesianVARs 0.1.8 reference (specify_prior_phi, bvar, predict.bayesianVARs_bvar, irf, stable_bvar, summary)
- Gruber & Kastner 2023 Forecasting macroeconomic data with Bayesian VARs: Sparse or dense? It depends! (arXiv:2206.04902)
- Kastner & Fruhwirth-Schnatter 2014 ASIS/interweaving SV
- Vehtari et al. 2021 Bayesian Analysis 16(2):667-718 rank-normalized ESS

## #144 — Sparse Dynamic Factor Model (EM with LASSO sparse loadings; arbitrary missing data / ragged-edge nowcasting; PCA/2Stage/EM/EM-sparse)

**Module:** `sparse_dynamic_factor.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `sdf_fit` | `X`, `r` | `multiseries_handle`, `integer`, `enum`, `enum`, `integer`, `num_array`, `boolean`, `integer`, `number` | `q=0`, `standardize=True`, `max_iter=100`, `threshold=0.0001` | `light` | `model` |
| `sdf_predict` | `model` | `raw_handle`, `integer`, `boolean` | `h=1`, `standardize=False` | `light` | — |
| `sdf_factors` | `model` | `raw_handle` | — | `light` | — |

### Use when

large-panel nowcasting with interpretable sparse (LASSO) loadings + handling of arbitrary missing data; sdf_fit=a (sparse) DFM + imputation, sdf_predict=an h-step nowcast, sdf_factors=factor paths+covariances

### Do not use when

a dense DFM + Bai&Ng r + explicit mixed frequency -> dfms #15; a Bayesian mixed-frequency nowcast with bands -> mfbvar #17; non-stationary data (difference it first); charts (frontend); forecasting with err='AR1' (the upstream predict breaks)

### Prerequisites

- c01_preparation_prechecks/unit_root_normality.run_adf_test
- c01_preparation_prechecks/unit_root_normality.run_kpss_test (confirmatory)

### Alternatives

| instead use | when |
| --- | --- |
| 03-multivariate-nowcasting/df_dfm | you want DENSE loadings + automatic Bai&Ng factor selection + explicit quarterly.vars mixed frequency |
| 03-multivariate-nowcasting/mf_estimate | a Bayesian mixed-frequency nowcast with posterior uncertainty/credible bands |
| sdf_predict | an h-step nowcast/forecast (X_hat + F_hat) from the already estimated model |

### Output fields

- factors: n x r factor paths; loadings: the p x r Lambda (zeros = a series that is irrelevant under EM-sparse)
- var_explained/var_explained_cum: the share of variance (eigen-decomposition); eigenvalues
- fitted: the n x p common component (original scale); imputed (X.bal): the panel with interpolated NA (the nowcast input)
- transition(A)/Sigma_u/Sigma_epsilon; converged/loglik/num_iter/alpha_opt(BIC-optimal); na_count
- sdf_predict: X_hat (an h x p nowcast, columns=varnames) + F_hat (h x r); sdf_factors: factors + factors_cov (r x r x n)

### Pitfalls

- err='AR1': the fit is valid BUT prediction is impossible (a package limitation, non-conformable) — sdf_predict blocks it cleanly; use err='IID' for a nowcast
- method='PCA'/'2Stage': no EM is run -> converged/loglik/num_iter/alpha_opt = NA (NOT an error, it is a static/two-step estimate)
- gate 1 <= r < ncol(X); the data MUST be stationary; standardization happens INTERNALLY (no pre-scaling); deterministic EM (no seed)
- COLLISION: sparseDFM exports VAR, which masks VAR — the wrapper uses requireNamespace + sparseDFM:: (NOT library)

### References

- Mosley, Chan & Gibberd 2023, sparseDFM: An the reference Package to Estimate DFMs with Sparse Loadings (arXiv:2303.14125)
- Banbura & Modugno 2014 (J. Appl. Econometrics 29:133-160, EM with arbitrary missing data)
- Doz, Giannone & Reichlin 2011 (J. Econometrics 164:188-205, two-step); Bai & Ng 2002 (Econometrica 70:191-221, IC for r)
- sparseDFM 1.0 reference manual (sparseDFM, predict.sparseDFM, tuneFactors)

## #145 — High-dimensional mixed-frequency regression via MIDAS-ML sparse-group LASSO (Legendre/Gegenbauer weighted high-frequency blocks -> a low-frequency target, sg-LASSO lambda + mixing gamma, CV-tuned)

**Module:** `high_dimensional_mixed.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `mml_fit` | `y`, `X`, `group` | `num_array`, `matrix_handle`, `int_array`, `integer`, `enum`, `number`, `number`, `num_array`, `integer`, `boolean`, `boolean` | `degree=3`, `gb_alpha=1`, `gamma=0.5`, `nlambda=100`, `intercept=True`, `standardize=False` | `light` | `model` |
| `mml_cv` | `y`, `X`, `group` | `num_array`, `matrix_handle`, `int_array`, `integer`, `enum`, `number`, `number`, `num_array`, `integer`, `boolean`, `boolean`, `integer` | `degree=3`, `gb_alpha=1`, `gamma=0.5`, `nfolds=10`, `intercept=True`, `standardize=False` | `light` | `model` |
| `mml_predict` | `model`, `newx` | `raw_handle`, `matrix_handle`, `enum` | — | `light` | — |

### Use when

Forecasting/nowcasting one low-frequency variable from MANY high-frequency indicators with many lags; each predictor (group) -> an orthonormal Legendre/Gegenbauer basis (degree+1) & a sparse-group LASSO for simultaneous group selection + within-group sparsity; gamma=the mixing weight (0 group-LASSO, 1 LASSO), lambda=the penalty (tuned with mml_cv).

### Do not use when

Few high-frequency regressors with an interpretable weight shape -> midasr #18; factor structure/a large n -> dfms #15 / sparseDFM; a Bayesian mixed-frequency VAR with latent states -> mfbvar #17; a same-frequency high-dimensional VAR -> BigVAR; it is not multi-equation/IRF (a single low-frequency target).

### Prerequisites

- c01_preparation_prechecks/unit_root_normality.run_adf_test
- c01_preparation_prechecks/unit_root_normality.run_kpss_test

### Alternatives

| instead use | when |
| --- | --- |
| midasr (#18) | Few high-frequency regressors + an interpretable parametric weight shape theta (not sparse selection). |
| dfms (#15) | A large n; a latent factor structure summarises better than sparse selection. |
| mml_cv | A principled choice of lambda (lam.min/lam.1se) instead of the mml_fit path default (the smallest lambda). |

### Output fields

- mml_fit: model (an 'mml_model' producer -> register field=model, bucket=rds); beta = (n_basis x nlambda) BASIS coefficients per lambda; the lambda/df/intercept path; n_groups/n_basis/gamma/degree/weight/s_default
- mml_cv: lambda_min (minimising the CV error) & lambda_1se (the 1-SE, more parsimonious one); cvm/cvsd/cvupper/cvlower (the CV curve, chart-data); nzero; beta_min/beta_1se + intercept_min/intercept_1se; seed (NA if empty)
- mml_predict: fitted (length==nrow(newx)) + s + kind

### Pitfalls

- mml_predict newx = the RAW high-frequency block (the same group/ncol as at fit time); the wrapper applies the SAME MIDAS transform internally — do NOT pass a pre-transformed design.
- beta is in BASIS coefficients (Legendre/Gegenbauer functions), NOT per-lag weights; the per-lag shape = Psi %*% beta_group.
- mml_fit (convex coordinate descent) is DETERMINISTIC (no seed); mml_cv partitions the folds RANDOMLY -> it REQUIRES a seed for reproducibility/caching (otherwise lambda_min fluctuates).
- s: for a cv model -> lam.min/lam.1se; for a path model -> a numeric lambda (the default is the smallest lambda = the richest/least regularized model).
- weighted basis: every group MUST have jmax >= degree+1 (a well-posed orthonormal basis); gamma ∈ [0,1] (the package enforces it, the gate gives a clean message).

### References

- Babii, Ghysels & Striaukas 2022 'Machine Learning Time Series Regressions With an Application to Nowcasting' JBES 40(3):1094-1106 (doi:10.1080/07350015.2021.1899933)
- midasml 0.1.11 reference manual (sglfit, cv.sglfit, lb, gb, predict.sglpath, predict.cv.sglfit)
- Babii, Ghysels & Striaukas 2021 (sparse-group LASSO with dependent/heteroskedastic data)

## #146 — Time-Varying-Parameter VAR with stochastic volatility + dynamic global-local shrinkage (triple/double gamma or ridge) — shrinkTVPVAR

**Module:** `time_varying_parameter.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `stv_estimate` | `y`, `seed` | `multiseries_handle`, `integer`, `enum`, `boolean`, `integer`, `integer`, `integer`, `integer`, `number`, `integer`, `boolean` | `p=1`, `const=True`, `niter=200`, `nburn=100`, `nthin=1`, `ess_min=10`, `min_draws=20`, `allow_nonconvergence=False` | `mcmc` | `model` |
| `stv_forecast` | `model` | `raw_handle`, `integer`, `num_array` | `n_ahead=1` | `light` | — |
| `stv_tvp` | `model` | `raw_handle`, `integer`, `num_array`, `boolean` | `equation=1`, `include_intercept=True` | `light` | — |

### Use when

A multivariate VAR (k>=2) where the relations EVOLVE smoothly over time (time-varying coefficients) AND the volatility changes (stochastic volatility), while MANY coefficients are in practice 0/constant -> dynamic shrinkage (triple/double gamma) automatically picks which ones are genuinely time-varying. The classic macro case: changing monetary transmission, structural breaks without explicit breakpoints.

### Do not use when

Constant (time-invariant) coefficients suffice -> Bayesian VAR #12 (BVAR) / vars #11; TVP WITHOUT shrinkage and with explicit identification/IRF -> bvarsv #14 (Primiceri); a single-equation TVP regression (not a VAR) -> shrinkTVP; a high-dimensional penalized point estimate -> BigVAR #142; nowcasting with a missing panel -> sparseDFM #144.

### Prerequisites

- c01_preparation_prechecks/unit_root_normality.run_adf_test
- c01_preparation_prechecks/unit_root_normality.run_kpss_test

### Alternatives

| instead use | when |
| --- | --- |
| #14 bvarsv | You want a TVP-VAR-SV with explicit Cholesky identification + structural IRFs (Primiceri), WITHOUT automatic variable selection. |
| #12 BVAR | The coefficients are plausibly constant -> a hierarchical Minnesota BVAR (cheaper, IRF/FEVD ready). |
| mod_type=triple | You want more aggressive shrinkage/sparsity (triple gamma) than the default double gamma; ridge = no selection. |

### Output fields

- stv_estimate: model (the producer handle), converged/min_ess/retained_draws/n_varying_params (the convergence gate), variables/n_vars/p/mod_type/const
- stv_forecast: quants (a named list per variable: [probs x horizon] posterior predictive fan) + mean [vars x horizon] + probs/horizon
- stv_tvp: paths (a named list per coefficient L<lag>.<var> & intercept: [probs x time] posterior bands) + coefficients/time/variable — the time-varying paths

### Pitfalls

- Convergence: a single-chain sampler -> NO split-Rhat; the gate is the minimum ESS (coda) over the beta_mean draws, IGNORING coefficients shrunk to constants (legitimate shrinkage, NOT poor convergence). A DEGENERATE all-NA ESS (every parameter constant) = NON-CONVERGENCE; it passes ONLY with allow_nonconvergence=TRUE.
- the seed is MANDATORY: without it the MCMC is not reproducible (the reference RNG; set.seed before the sampling).
- SV is INHERENT (it is always a TVP-VAR-SV); there is NO sv toggle — the only shrinkage knob is mod_type. ONLY the VAR-coefficient draws are returned (not those of the variance-covariance).
- the min_ess default (10) is a FLOOR for tiny-draw development; production runs (niter>=5000) must raise ess_min (>=200).
- stv_tvp equation = the index of the TARGET equation (the response); the paths are the time-varying loadings of the lagged variables in it.

### References

- Cadonna, Frühwirth-Schnatter & Knaus (2020), 'Triple the Gamma—A Unifying Shrinkage Prior..', Econometrics 8(2):20 (doi:10.3390/econometrics8020020)
- Knaus, Bitto-Nemling, Cadonna & Frühwirth-Schnatter (2021), 'Shrinkage in the TVP Model Framework Using shrinkTVP', JSS 100(13) (doi:10.18637/jss.v100.i13)
- shrinkTVPVAR reference (shrinkTVPVAR, forecast_shrinkTVPVAR) + live introspection

## #147 — Bayesian VAR & VHAR (Vector Heterogeneous AR; day/week/month long memory) with a Minnesota conjugate (analytic) / SSVS / Horseshoe prior + a posterior forecast fan

**Module:** `bayesian_var_vhar.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `bvh_var` | `y` | `multiseries_handle`, `integer`, `enum`, `number`, `integer`, `integer`, `integer`, `integer`, `boolean`, `integer`, `number`, `number`, `boolean` | `p=1`, `prior='minnesota'`, `lambda=0.1`, `num_chains=2`, `num_iter=200`, `num_burn=100`, `thinning=1`, `include_mean=True`, `rhat_max=1.1`, `ess_min=100`, `allow_nonconvergence=False` | `light` | `model` |
| `bvh_vhar` | `y` | `multiseries_handle`, `int_array`, `enum`, `number`, `integer`, `integer`, `integer`, `integer`, `boolean`, `integer`, `number`, `number`, `boolean` | `har=[5, 22]`, `prior='minnesota'`, `lambda=0.1`, `num_chains=2`, `num_iter=200`, `num_burn=100`, `thinning=1`, `include_mean=True`, `rhat_max=1.1`, `ess_min=100`, `allow_nonconvergence=False` | `light` | `model` |
| `bvh_predict` | `model` | `raw_handle`, `integer`, `number`, `boolean` | `n_ahead=8`, `level=0.05`, `sparse=False` | `light` | — |

### Use when

multivariate Bayesian dynamics with shrinkage when the VAR is over-parameterized; bvh_var=a Bayesian VAR; bvh_vhar=a Corsi VHAR (day/week/month, multi-scale persistence); priors minnesota(conjugate/analytic)/ssvs/horseshoe(MCMC sparsity)

### Do not use when

the frequentist route with a sufficient sample -> #11 vars; hierarchical GLP without SSVS/HS/VHAR -> #12 BVAR; gir/sir Gibbs -> #13 bvartools; TVP+SV -> #14 bvarsv; mixed frequency/nowcasting -> #15/#16; structural IRF/FEVD -> 04-structural-shocks (irf/fevd are omitted here)

### Prerequisites

- c01_preparation_prechecks/unit_root_normality.run_adf_test
- c01_preparation_prechecks/unit_root_normality.run_kpss_test

### Alternatives

| instead use | when |
| --- | --- |
| #12 BVAR | a hierarchical GLP Minnesota without SSVS/HS/VHAR suffices |
| #13 bvartools | you want an explicit Gibbs sampler + gir/sir IRF types |
| #14 bvarsv | time-varying parameters + stochastic volatility |
| #11 vars | frequentist Granger/diagnostics, the sample is sufficient |

### Output fields

- model: the fit (a producer; register field=model bucket=rds); class bvarmn/bvharmn (analytic) or bvarldlt/bvharldlt (MCMC)
- coefficients: the posterior mean, K x m (VHAR rownames a_day/a_week/a_month/const); pip: the inclusion probability (ssvs/horseshoe only)
- converged/max_rhat/min_ess/nonconvergence_reasons: the convergence gate (MCMC); analytic -> converged=TRUE, Rhat NA
- bvh_predict: forecast [n_ahead x m] point + lower/upper/se credible bands; draws + lower_joint/upper_joint (MCMC)

### Pitfalls

- minnesota = an ANALYTIC conjugate NIW (closed form, no MCMC/convergence, the seed is optional); ssvs/horseshoe = MCMC (the seed is MANDATORY + a convergence gate + tiny draw counts)
- convergence gate (mirroring rstan #68): num_chains<2 or ALL Rhat NA = DEGENERATE -> non-convergence; max(Rhat)>rhat_max or min(Bulk_ESS)<ess_min -> stop unless allow_nonconvergence=TRUE
- the tiny defaults (num_iter=200) often do NOT meet strict thresholds -> the gate blocks conservatively (correctly); raise num_iter or override
- nrow <= order_max+1 (VHAR: >23) -> a cryptic Eigen C++ assertion; gated explicitly
- the predict level is a significance level (0.05 -> a 95% interval), NOT a confidence level; sparse=TRUE -> SAVS coefficients (MCMC only)
- S3 collision: bvhar exports irf/predict.bvarsv/coef.* -> it masks irf in the shared env; no function masking occurs (conflicts=NULL); predict goes through getS3method(asNamespace('bvhar')); we do not expose irf/fevd here

### References

- Corsi 2009 (HAR-RV, JFE); George-Sun-Ni 2008 (SSVS for VAR); Carvalho-Polson-Scott 2010 (horseshoe)
- Vehtari et al. 2021 (rank-normalized split-Rhat + Bulk/Tail-ESS, Bayesian Analysis)

## #256 — PCA for MIXED I(0)/I(1) variables: an h-step-ahead OLS regression per series (a constant + p own lags) -> PCA on the RESIDUALS (Hamilton-Ma-Xi)

**Module:** `pca_mixed_variables.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `pn_cyclical_components` | `x` | `matrix_handle`, `integer`, `integer` | `h=24`, `p=12` | `light` | — |
| `pn_pca_nonstationary` | `x` | `matrix_handle`, `integer`, `integer`, `enum`, `integer` | `h=24`, `p=12`, `r_max=10` | `light` | — |

### Use when

common CYCLICAL factors behind many macro series whose stationarity is UNKNOWN or MIXED (I(1) levels + I(0) rates in the SAME panel); the method does NOT require the user to classify the series or to choose a per-series transformation — THE SAME regression on ALL of them; the defaults h=24/p=12 (monthly), h=8/p=4 (quarterly)

### Do not use when

ALL the series are demonstrably stationary and on a common scale -> classical PCA #117; a latent factor with DYNAMICS/mixed frequency/a ragged-edge nowcast -> dfms #15 or sparseDFM #144; charts (the frontend, §5); ONE series (N>=2 is required); an unbalanced panel with NA (a balanced sample is required); isolating the cycle of ONE series -> the Hamilton regression filter / neverhpfilter (cat 10)

### Prerequisites

- pn_cyclical_components # run step (7) alone FIRST and look at r_squared/residual_sd/short_sample before the PCA
- c00_data_utilities/composite_index_dimensionality.pca_stationarity_precheck # KPSS per column; if it flags non-stationarity, THIS is the right node (NOT #117)

### Alternatives

| instead use | when |
| --- | --- |
| #117 pca_composite (prcomp on levels) | ONLY when ALL the series are stationary; on non-stationary levels the standardization is undefined and the Bai-Ng criteria are corrupted (>1 factor at T=100 when the truth is 0) |
| #15 dfms / #144 sparseDFM | you need a state-space DFM with factor dynamics, mixed frequency or ragged-edge missing data instead of a static PCA on the cyclical components |
| pn_pca_nonstationary(h = 12) or (h = 1) | T_eff < 600 (< 50 years of monthly data) -> short_sample=TRUE: a large h raises the risk of a spurious factor (Onatski & Wang 2021); the paper recommends h=12 or h=1 in small samples |
| scale_residuals = 'none' | the series are ALREADY on a common scale and you want a COVARIANCE matrix; otherwise keep the default 'unit_variance' (= the paper's procedure) |

### Output fields

- factor1/scores: the estimated common CYCLICAL factors per time point (T_eff x k) — the main chart-data; the x-axis = time
- loadings: N x k sign-normalized (which series loads on which factor); loadings_hmx/factors_hmx = the paper's normalization (lambda'lambda/N = 1, f = N^-1 lambda'C, eq. 9-12)
- sdev/var_explained/cum_var/pc1_var + pca_matrix ('correlation' under the default, 'covariance' under 'none')
- residuals (T_eff x N) = the CYCLICAL COMPONENTS c-hat_it of eq. (7) + residual_sd/r_squared/sigma/rss/rank per series
- coefficients (N x (p+1)) + lag_terms + residual_center/residual_scale: ALL the fitted params as NUMBERS (fit/apply externalization, §3b gate 6)
- cor_residuals/eigenvalues/r2_eigen (eq. 18) + ic_p2/n_factors_icp2 (Bai-Ng IC_p2, eq. 19) + r_max_effective
- h/p/n_obs/n_eff/df_residual/obs_index/time/frequency/recommended_h/recommended_p/short_sample/short_sample_threshold/short_sample_advice

### Pitfalls

- DO NOT difference and DO NOT de-trend before the node: eq. (7) on LEVELS IS the transformation; pre-differencing transforms twice and destroys the cycle
- NEVER standardize the raw series (the invalid step: under I(1) the population mean does not exist and the sample sd diverges with T); the scaling is applied ONLY to the (stationary) residuals and is an explicit gated option
- scale_residuals='none' => var_explained (covariance) does NOT coincide with r2_eigen (eq. 18, ALWAYS the correlation matrix); read the pca_matrix field before comparing the two
- a hard size gate: T >= h + 2p + 1 (T_eff = T-h-p+1 >= p+2); with fewer, lm.fit does NOT error — it returns residuals EXACTLY 0 (silently wrong) and the PCA would run on zeros
- A DETERMINISTIC series (y_t = a + b*t, a running number, an index) => the p lags are collinear: lm.fit returns SILENTLY rank<p+1 with NA coefficients — a hard gate here
- a constant/zero-variance column => cor -> NA with ONLY the warning «the standard deviation is zero» (silently wrong) and prcomp(scale.) -> «cannot rescale a constant/zero column» — a hard gate here
- p is ALSO the maximum order of integration/polynomial trend d_i <= p that is annihilated; the paper recommends p = the number of observations per year (persistent seasonality)
- the signs of the PCs are arbitrary (the prcomp help Note) -> an explicit sign-normalization (the max-\|loading\| is positive); read the direction from the loadings
- T_eff < 600 (= 50 years of monthly data) => short_sample=TRUE: an increased risk of a spurious factor; a DIAGNOSTIC, NOT a gate (every h>=1 produces a stationary cyclical component)
- logs vs levels: the paper takes logs of whatever is described in rates of change (output/prices) and leaves rates/unemployment as they are — an UPSTREAM decision (cat 00), NEVER implicit here
- outliers: the paper EXPLICITLY «make no corrections for outliers» for h=24 (h itself reduces the kurtosis); for extreme values see #246

### References

- Hamilton, J. D., Ma, X. & Xi, J., «Principal Component Analysis for a Mix of Stationary and Nonstationary Variables», NBER WP 32068 (rev. 2026-04-08; econweb.ucsd.edu/~jhamilto/HX.pdf) — eq. (7) the regression, «Our procedure is to perform PCA on the regression residuals», «h=8/p=4 quarterly, h=24/p=12 monthly», §6.3 «Since c-hat_it is normalized to have unit variance», eq. (18)-(19) on the CORRELATION matrix, §5 «600 or larger»
- Hamilton, J. D. (2018), «Why You Should Never Use the Hodrick-Prescott Filter», REStat 100(5) — the h-step-ahead regression as a trend/cycle decomposition; c_it is stationary for a polynomial trend d_i or I(d_i) with d_i <= p
- Bai, J. & Ng, S. (2002), «Determining the Number of Factors in Approximate Factor Models», Econometrica 70(1) — IC_p2; Stock & Watson (2016, Handbook of Macroeconomics, p. 436) recommend it
- Onatski, A. & Wang, C. (2021), «Spurious Factor Analysis», Econometrica 89(2), pp. 591-614 — why PCA on non-stationary levels produces spurious factors
