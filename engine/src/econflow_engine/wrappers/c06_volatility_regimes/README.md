<!-- SPDX-License-Identifier: AGPL-3.0-only -->
# 06-volatility-regimes

16 METHOD-SELECTION cards, 16 modules, 61 nodes.

Every card below governs one wrapper module in this package. The cards are the
reason a method exists here at all: they record when it applies, what to reach
for instead, and the traps that make its output easy to misread.

## #28 — Univariate GARCH family

**Module:** `univariate_garch_family.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `ga_spec` | — | `enum`, `int_array`, `int_array`, `string`, `enum`, `boolean`, `boolean`, `integer`, `boolean` | `include_mean=True`, `archm=False`, `archpow=1`, `variance_targeting=False` | `light` | `object` |
| `ga_fit` | `spec`, `data` | `raw_handle`, `series_handle`, `integer`, `enum` | `out_sample=0` | `light` | `object` |
| `ga_forecast` | `fit` | `raw_handle`, `integer`, `integer` | `n_ahead=10`, `n_roll=0` | `light` | — |
| `ga_sim` | `fit` | `raw_handle`, `integer`, `integer`, `integer` | `n_sim=1000`, `n_start=0`, `m_sim=1` | `light` | — |
| `ga_roll` | `spec`, `data` | `raw_handle`, `series_handle`, `integer`, `integer`, `enum`, `enum`, `boolean` | `forecast_length=500`, `refit_every=25`, `calculate_VaR=True` | `light` | — |
| `ga_diagnostics` | `fit` | `raw_handle`, `integer` | `gof_groups=20` | `light` | — |

### Use when

a univariate series of returns/errors with volatility clustering; modelling/forecasting sigma_t, VaR, persistence/asymmetry

### Do not use when

multivariate covariance (#29); switching volatility (#31); thresholds in the mean (#32); realized-vol/mcsGARCH/realGARCH (out of scope)

### Prerequisites

- c01_preparation_prechecks/unit_root_normality.run_adf_test
- c01_preparation_prechecks/unit_root_normality.run_kpss_test
- c15_model_evaluation/arch.run_arch_test

### Alternatives

| instead use | when |
| --- | --- |
| MSGARCH (#31) | when the GARCH dynamics themselves change regime (Nyblom instability) |
| stochastic-volatility state-space (10-* KFAS/bssm) | when you want latent volatility with Bayesian filtering instead of ML-GARCH |
| eGARCH/gjrGARCH against sGARCH | when signbias indicates asymmetry/leverage |

### Output fields

- coefficients: mean.model terms + variance terms (omega, alpha, beta, gamma leverage, shape/skew)
- sigma: vector of conditional standard deviations sigma_t (chart-data)
- persistence: alpha+beta (→1 = near-IGARCH, shocks almost permanent)
- uncvariance/halflife: long-run variance; half-life of decay
- infocriteria: AIC/BIC/SIC/HQ
- signbias: Engle-Ng sign-bias df, p<0.05 => asymmetry
- nyblom: parameter stability, teststat-vs-critical-value WITHOUT a p-value
- gof: adjusted Pearson goodness-of-fit, p<0.05 => the wrong distribution

### Pitfalls

- ga_fit blocks if convergence!=0 (a non-converged fit does not escape)
- gof_groups must be > params+1, otherwise the test degenerates silently
- persistence≈1 is often a non-stationary input, not genuine IGARCH
- nyblom: compare IndividualStat/JointStat with the critical values (no p-value, as with urca)
- ga_sim is always seeded (default seq_len(m.sim)+2024)

### References

- Bollerslev 1986 (GARCH)
- Nelson 1991 (EGARCH)
- Glosten-Jagannathan-Runkle 1993 (GJR)
- Engle-Ng 1993 (sign-bias)
- Nyblom 1989
- Enders 2015
- rugarch vignette (Galanos)

## #29 — DCC-MGARCH (multivariate)

**Module:** `dcc_mgarch.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `dcc_multispec` | `specs` | `raw_handle_array` | — | `light` | `object` |
| `dcc_spec` | `uspec` | `raw_handle`, `enum`, `enum`, `boolean`, `integer` | `VAR=False`, `lag=1` | `light` | `object` |
| `dcc_fit` | `spec`, `data` | `raw_handle`, `matrix_handle`, `integer`, `enum` | `out_sample=0` | `light` | `object` |
| `dcc_forecast` | `fit` | `raw_handle`, `integer`, `integer` | `n_ahead=1`, `n_roll=0` | `light` | — |
| `dcc_sim` | `fit` | `raw_handle`, `integer`, `integer`, `integer` | `n_sim=1000`, `n_start=0`, `m_sim=1` | `heavy` | — |
| `dcc_roll` | `spec`, `data` | `raw_handle`, `matrix_handle`, `integer`, `integer`, `enum`, `enum` | `forecast_length=50`, `refit_every=25` | `light` | — |

### Use when

>=2 return series with time-varying correlation/covariance; spillovers, dynamic hedge ratios, portfolio risk

### Do not use when

univariate (#28); GO-GARCH (deliberately out); structural spillover networks (09-* Connectedness/frequencyConnectedness)

### Prerequisites

- c01_preparation_prechecks/unit_root_normality.run_adf_test
- c01_preparation_prechecks/unit_root_normality.run_kpss_test
- c15_model_evaluation/arch.run_arch_test
- c06_volatility_regimes/univariate_garch_family.ga_diagnostics

### Alternatives

| instead use | when |
| --- | --- |
| GO-GARCH / BEKK | when you want the full covariance without the DCC decomposition |
| static unconditional correlation | when ARCH-LM shows no time variation |
| frequencyConnectedness (09-*) | when the objective is directional spillovers rather than a correlation matrix |

### Output fields

- coefficients: univariate GARCH per asset + DCC params (dcca1=a, dccb1=b; a+b<1)
- rcov: TxNxN array of time-varying covariance H_t
- rcor: TxNxN array of time-varying correlation R_t (chart-data)
- rcov_forecast/rcor_forecast: the 1st element of the forecast list (n.roll=0)
- infocriteria: AIC/BIC of the whole model

### Pitfalls

- dcc_fit blocks if fit@mfit.convergence!=0 (the slot is read; no exported generic exists)
- multispec belongs to rugarch, not to rmgarch
- groups must have length == #assets, otherwise it is silently wrong (gate)
- DCC imposes a common correlation dynamic on all pairs (under-fitting under heterogeneity)
- two-stage: a wrong univariate stage is inherited by the DCC
- dcc_sim is always seeded

### References

- Engle 2002 (DCC)
- Cappiello-Engle-Sheppard 2006 (aDCC)
- Bollerslev 1990 (CCC baseline)
- rmgarch vignette (Galanos)

## #30 — Markov switching (gaussian/lm)

**Module:** `markov_switching.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `msw_fit` | `formula`, `data` | `formula`, `df_handle`, `integer`, `integer` | `k=2`, `p=0` | `heavy` | `object` |
| `msw_intervals` | `fit` | `raw_handle`, `number` | `level=0.95` | `light` | — |
| `msw_residuals` | `fit` | `raw_handle`, `integer` | — | `light` | — |

### Use when

endogenous regime switching in the mean/regression dynamics with a latent Markov chain (recession/expansion); EM estimation

### Do not use when

switching in GARCH volatility (#31); observable-threshold regimes (#32); glm/poisson/binomial/Gamma (NOT exposed — glm dispatch breaks from inside a wrapper). gaussian/lm only

### Prerequisites

- c01_preparation_prechecks/structural_change

### Alternatives

| instead use | when |
| --- | --- |
| SETAR/LSTAR (#32) | when the transition variable is observable rather than latent |
| MSGARCH (#31) | when the switching concerns volatility |
| linear ARMA/VAR | when no break/nonlinearity test justifies regimes |

### Output fields

- coefficients (matrix kxp): coefficients per regime (column/regime)
- std_errors: SE per regime
- pMat: transition probability matrix; the diagonal ≈ regime persistence
- prob (filtProb Txk): filtered P(regime\|info<=t)
- smoProb (Txk): smoothed P(regime\|the whole sample)
- regime: argmax filtProb per t (chart-data)
- log_lik/AIC: for comparing k

### Pitfalls

- filtered vs smoothed: for ex-post dating use smoProb, not the filtered-based regime
- label switching: the numbering of regimes is arbitrary — identify them from the coefficients
- AIC(fit) bare (NOT AIC — S4 masking); BIC does not exist for MSM
- there is no formal LR test for the number of regimes — compare AIC/log_lik across k
- set.seed before msw_fit (EM init uses sample with no seed argument); k=1 fails opaquely (gate k>=2)

### References

- Hamilton 1989 (Markov-switching)
- Krolzig 1997 (MS-VAR)
- Perlin 2012 (doi:10.2139/ssrn.1714016)
- MSwM reference manual

## #31 — Markov-switching GARCH

**Module:** `markov_switching_garch.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `msg_spec` | — | `enum`, `enum`, `integer`, `boolean` | `K=2`, `do_mix=False` | `light` | `object` |
| `msg_fit_ml` | `spec`, `data` | `raw_handle`, `series_handle` | — | `light` | `object` |
| `msg_fit_mcmc` | `spec`, `data` | `raw_handle`, `series_handle` | — | `heavy` | `object` |
| `msg_predict` | `fit` | `raw_handle`, `integer`, `boolean` | `nahead=1`, `do_cumulative=False` | `light` | — |
| `msg_state` | `fit` | `raw_handle` | — | `light` | — |
| `msg_sim` | `fit` | `raw_handle`, `integer`, `integer`, `integer` | `nsim=1`, `nahead=1`, `nburn=500` | `heavy` | — |
| `msg_risk` | `fit` | `raw_handle`, `boolean`, `integer` | `do_es=True`, `nahead=1` | `light` | — |

### Use when

univariate volatility where the GARCH dynamics themselves alternate between regimes (calm/turbulent) under a latent Markov chain; ML or MCMC, VaR/ES

### Do not use when

single-regime volatility (#28); switching in the mean only (#30); multivariate (#29)

### Prerequisites

- c01_preparation_prechecks/unit_root_normality.run_adf_test
- c01_preparation_prechecks/unit_root_normality.run_kpss_test
- c15_model_evaluation/arch.run_arch_test

### Alternatives

| instead use | when |
| --- | --- |
| rugarch single-regime GARCH (#28) | when the single regime passes ga_diagnostics (Nyblom shows no break) |
| MSwM (#30) | when the switching concerns the mean |
| PerformanceAnalytics VaR/ES (12-*) | when you want historical/Cornish-Fisher risk without a parametric MSGARCH |

### Output fields

- par (ML) / posterior (MCMC): parameters per regime + transition probabilities
- loglik: log-likelihood (ML)
- vol: predicted conditional volatility n-ahead
- FiltProb/PredProb/SmoothProb: regime probabilities (Txdrawsxk arrays)
- Viterbi: most probable regime path (integer vector, global MAP path)
- VaR/ES: Value-at-Risk / Expected Shortfall per alpha

### Pitfalls

- Viterbi != argmax(SmoothProb): the optimal sequence, not the per-t marginal MAP
- label switching in MCMC (do.sort); identify regimes from the volatility params
- an alpha for VaR/ES outside (0,1) is silently accepted & yields garbage (gate)
- VaR sign convention: a negative value = a loss (the lower quantile of the return)
- msg_sim only on an estimated fit (not a bare spec), always seeded (default 2025)
- simulate is taken as simulate (avoiding masking by simulate)

### References

- Haas-Mittnik-Paolella 2004 (MSGARCH)
- Ardia-Bluteau-Boudt-Catania-Trottier 2019 JSS 91(4) (doi:10.18637/jss.v091.i04)

## #32 — Threshold models (SETAR/LSTAR/STAR)

**Module:** `threshold.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `setar_fit` | `x`, `m` | `series_handle`, `integer`, `integer`, `integer`, `enum`, `enum`, `enum`, `integer`, `number` | `d=1`, `thDelay=0`, `nthresh=1`, `trim=0.15` | `light` | `object` |
| `lstar_fit` | `x`, `m` | `series_handle`, `integer`, `integer`, `integer`, `number`, `enum` | `d=1` | `light` | `object` |
| `star_fit` | `x`, `noRegimes` | `series_handle`, `integer`, `integer`, `integer`, `number` | `m=2`, `d=1`, `sig=0.05` | `light` | `object` |
| `setar_select` | `x`, `m` | `series_handle`, `integer`, `integer`, `integer`, `number`, `enum`, `enum`, `enum` | `thDelay=0`, `nthresh=1`, `trim=0.15` | `light` | — |
| `setar_test` | `x`, `m` | `series_handle`, `integer`, `integer`, `number`, `enum`, `integer`, `enum`, `enum` | `thDelay=0`, `trim=0.1`, `nboot=100` | `heavy` | — |
| `thr_predict` | `object` | `raw_handle`, `integer`, `enum`, `integer`, `number` | `n_ahead=1`, `nboot=100`, `ci=0.95` | `heavy` | — |
| `thr_regime` | `object` | `raw_handle` | — | `light` | — |

### Use when

non-linear dynamics in the mean with an observable transition variable; SETAR (abrupt threshold) / LSTAR-STAR (smooth transition); business-cycle asymmetry, band-TAR

### Do not use when

latent regime switching (#30/#31); threshold cointegration TVECM (c05_cointegration/vecm_estimate_johansen #24); pure volatility (#28/#31)

### Prerequisites

- c01_preparation_prechecks/unit_root_normality.run_adf_test
- c01_preparation_prechecks/unit_root_normality.run_kpss_test
- c06_volatility_regimes/threshold.setar_test

### Alternatives

| instead use | when |
| --- | --- |
| MSwM (#30) | when the transition variable is latent rather than observable |
| linear AR/ARIMA (02-*) | when setar_test.pval does not reject linearity |
| LSTAR against SETAR | when the transition is smooth/gradual (a large gamma -> SETAR as the limit) |

### Output fields

- coefficients: AR coefficients per regime (low/high) + threshold/gamma
- th: estimated threshold (SETAR) or transition centre (LSTAR); nthresh=2 -> 2 thresholds
- gamma (LSTAR): speed of the smooth transition (large -> nearly SETAR)
- regime (thr_regime): integer regime indicator per t (chart-data)
- AIC/BIC: selection of m/nthresh/model
- Ftests/pval/cval (setar_test): Hansen F-stat, bootstrapped p-value & critical values
- bests/res (setar_select): the best delay/lags/threshold & the criterion grid

### Pitfalls

- setar_test.pval is bootstrapped (seeded, default 2025); p<0.05 => linearity is rejected
- thr_regime only for setar/lstar — not star (regime_default on star = silently NULL, gate)
- star_fit requires a mandatory noRegimes>=2
- regime numbering is arbitrary (identify from th & the signs)
- thr_predict with type!=naive is stochastic (MC/bootstrap) -> seeded
- trace/plot are always FALSE (no chart/console spam)

### References

- Tong 1990 (SETAR/threshold AR)
- Teräsvirta 1994 (LSTAR/STAR)
- Hansen 1999 (threshold linearity test)
- Enders 2015
- tsDyn vignette (Di Narzo-Aznarte-Stigler)

## #154 — Univariate GARCH family (vanilla/egarch/gjr/aparch/component)

**Module:** `univariate_garch_family_2.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `tg_estimate` | `y` | `num_array`, `enum`, `boolean`, `int_array`, `enum`, `boolean`, `string`, `integer` | `constant=True`, `variance_targeting=False`, `solver='nloptr'`, `seed=2025` | `light` | `object` |
| `tg_predict` | `object` | `raw_handle`, `integer`, `integer`, `enum`, `integer` | `h=1`, `nsim=0`, `seed=2025` | `heavy` | — |
| `tg_backtest` | `y` | `num_array`, `enum`, `boolean`, `int_array`, `enum`, `integer`, `integer`, `integer`, `integer`, `boolean`, `integer` | `constant=True`, `h=1`, `estimate_every=1`, `rolling=False`, `seed=2025` | `light` | — |

### Use when

modelling conditional volatility in univariate returns (volatility clustering); ML estimation of a GARCH + an h-step forecast of sigma_t + a rolling backtest; a modern tidy API (nloptr, TMB, autodiff SE)

### Do not use when

multivariate volatility/correlation (-> #29 rmgarch/tsmarch); regime-switching volatility (-> #31 MSGARCH); return levels with no ARCH effects (a non-significant run_arch_test); realized/intraday volatility (highfrequency)

### Prerequisites

- c15_model_evaluation/arch.run_arch_test (ARCH effects: H0=no ARCH; rejection -> GARCH is justified)
- c00_data_utilities/reading_delimited_fixed.read_delimited (loading the returns from a file)

### Alternatives

| instead use | when |
| --- | --- |
| #28 rugarch (ga_spec/ga_fit) | you need the fGARCH/csGARCH submodels, a VaR rolling backtest with coverage tests, or the mature rugarch API |
| #29 rmgarch/tsmarch (dcc_fit) | multivariate conditional covariance/correlation (>=2 assets) |
| #31 MSGARCH (msg_fit_ml) | the volatility switches between regimes (Markov switching) |
| variance_targeting=TRUE | a large sample + you want a fixed unconditional variance without estimating omega |

### Output fields

- coefficients: named (mu/omega/alpha*/beta*/gamma*/shape/skew..) depending on the model/distribution
- persistence: sum(alpha+beta) ~ the persistence; ~1 => near-integrated (IGARCH-like), see near_nonstationary
- sigma: the conditional sd series (chart-data); tg_predict.sigma_forecast: the h-step sigma_t
- converged/kkt1/kkt2: the optimisation KKT conditions (converged=KKT1, first order); a stateless capture
- aic/bic/loglik: for comparing model/distribution; tg_backtest.table: sigma/actual/convergence per forecast

### Pitfalls

- y MUST be returns (log/simple), NOT price levels — the wrapper does not difference
- persistence>=0.999 (near_nonstationary=TRUE) => the unconditional variance explodes; the long-horizon sigma_t forecast is unreliable
- egarch persistence is measured on the log-variance (a different scale from the vanilla alpha+beta)
- converged=FALSE (KKT1) => the solution is not an optimum; do not interpret the coefficients/SE
- std_errors are NULL/NaN when the Hessian is not positive definite (common at boundary persistence)
- tg_estimate/tg_backtest are deterministic (ML); only tg_predict with nsim>0 is stochastic (seeded 2025)

### References

- Galanos A. (2024) tsgarch: Univariate GARCH Models, the reference package (tsmodels)
- Bollerslev 1986 (J. Econometrics 31:307, GARCH); Nelson 1991 (Econometrica 59:347, EGARCH)
- Glosten Jagannathan Runkle 1993 (J. Finance 48:1779, GJR); Ding Granger Engle 1993 (APARCH)

## #155 — Multivariate GARCH — Dynamic Conditional Correlation (DCC/aDCC/CCC)

**Module:** `multivariate_garch_dynamic.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `tm_dcc_estimate` | `y` | `matrix_handle`, `enum`, `enum`, `enum`, `int_array`, `enum`, `int_array`, `enum`, `integer` | `garch_model='garch'`, `garch_distribution='norm'`, `seed=2025` | `light` | `object` |
| `tm_predict` | `object` | `raw_handle`, `integer`, `integer`, `enum`, `integer` | `h=1`, `nsim=1000`, `seed=2025` | `heavy` | — |
| `tm_cov` | `object` | `raw_handle`, `boolean` | `correlation=False` | `light` | — |

### Use when

time-varying covariance/correlation of >=2 return series; volatility spillovers, time-varying correlation, dynamic hedge ratios, portfolio risk (the tidy )

### Do not use when

univariate volatility (-> #28 rugarch/tsgarch); many assets (N>~10; the DCC parameter/estimation burden -> GO-GARCH/factor models); level/non-stationary series (take returns first); regime-switching volatility (-> #31 MSGARCH)

### Prerequisites

- c00_data_utilities/reading_delimited_fixed.read_delimited (load the T×N matrix of returns)
- c15_model_evaluation/arch.run_arch_test (ARCH-LM: there must be ARCH effects in each series, otherwise GARCH is pointless)
- tm_cov (post: check whether the dynamic correlation really varies — if not, a constant/CCC suffices)

### Alternatives

| instead use | when |
| --- | --- |
| #29 rmgarch dcc_fit | the legacy rugarch/rmgarch pipeline, or copula/GO-GARCH variants that are not exposed here |
| dynamics=constant (CCC) | the correlation does not vary appreciably (the Engle-Sheppard test / a ~constant tm_cov) — fewer parameters |
| distribution=mvt | heavy tails/joint tail dependence in the standardized returns |
| cgarch/gogarch (tsmarch, not exposed) | copula dependence or orthogonalisation for a larger N |

### Output fields

- coefficients: the DCC dynamic parameters (alpha_1/beta_1; gamma_1 for adcc; shape for mvt); constant -> empty (no dynamics)
- coef_table: term/Estimate/Std. Error/t value/Pr(>\|t\|) of the DCC parameters
- correlation_last / covariance_last: the N×N last in-sample conditional matrix (chart-data)
- loglik/AIC/BIC/nobs/n_series/n_pars; converged: convergence of the second stage (a stateless capture)
- tm_cov.covariance/.correlation: an N×N×T array; tm_predict.forecast_covariance/.forecast_correlation: N×N×h (the mean)

### Pitfalls

- alpha+beta ~ 1 -> high persistence of the correlation; alpha ~ 0 -> ~constant (the DCC adds nothing)
- with constant dynamics tm_cov.correlation is N×N×1 (time-invariant); only the covariance varies (through the garch variances)
- keep_tmb=TRUE internally is MANDATORY: without it the dynamic dcc/adcc fails (tsgarch>=1.0.4 removes the second-stage .tmb)
- converged=FALSE or enormous/NaN Std.Error in coef_table -> a degenerate solution, do not interpret the DCC parameters
- the mean forecast (tscov/tscor with distribution=FALSE) is the centre; the uncertainty lives in the nsim paths (it is not exposed flat)

### References

- help('dcc_modelspec','tsmarch'), help('estimate','tsmarch'), the tsmarch DCC vignette ( tsmarch 1.0.0)
- Engle 2002 'Dynamic Conditional Correlation' (JBES 20:339)
- Cappiello, Engle & Sheppard 2006 asymmetric DCC (J. Financial Econometrics 4:537)
- Ghalanos tsmarch/tsgarch documentation (keep_tmb two-stage estimation)

## #156 — Realized (co)variance & intraday spot volatility from high-frequency data

**Module:** `realized_variance_intraday.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `hf_realized_var` | `data` | `num_array`, `enum`, `boolean`, `enum`, `integer`, `integer`, `integer` | `makeReturns=True`, `kernelParam=1`, `J=1` | `light` | — |
| `hf_realized_cov` | `data` | `matrix_handle`, `enum`, `boolean`, `boolean`, `integer`, `integer` | `makeReturns=True`, `cor=False`, `J=1` | `light` | — |
| `hf_spot_vol` | `data` | `df_handle`, `enum`, `enum`, `integer`, `string`, `string`, `string` | `alignPeriod=5`, `marketOpen='09:30:00'`, `marketClose='16:00:00'`, `tz='GMT'` | `light` | — |

### Use when

you have intraday data and you want the ex-post realized volatility/covariance of ONE day (rCov=the sum of r², the jump-robust rBPCov/medRV, the noise-robust rKernelCov/rTSCov), a semivariance decomposition, or an intraday spot-volatility pattern

### Do not use when

daily/low-frequency series -> a parametric GARCH (#28 rugarch/tsgarch); conditional/forecast volatility -> GARCH; a multi-day dynamic covariance -> DCC (#29); you have no intraday observations

### Prerequisites

- hf_realized_var (a univariate realized measure; choose the measure according to the microstructure noise / jumps)
- hf_realized_cov (a multivariate realized covariance/semicovariance; >=2 assets)
- c00_data_utilities/reading_delimited_fixed.read_delimited (loading an intraday CSV: spotVol needs DT+price columns)

### Alternatives

| instead use | when |
| --- | --- |
| #28 rugarch/tsgarch (ga_fit) | conditional/forecast volatility from daily returns rather than an ex-post realized measure |
| #29 rmgarch DCC (dcc_fit) | a dynamic multi-day correlation/covariance rather than a per-day realized covariance |
| measure=rBPCov/medRV | suspected jumps in the intraday series (a jump-robust integrated variance) |
| measure=rKernelCov/rTSCov | market microstructure noise (bid-ask bounce) -> noise-robust estimators |
| measure=rSemiCov | you want downside/upside (negative/positive/mixed/concordant) semicovariance |

### Output fields

- hf_realized_var: realized_variance (the scalar sum or a robust version) + realized_vol=sqrt; K (rTSCov only); n_obs/n_returns
- hf_realized_cov: rcov (the N×N covariance, or the correlation if cor=TRUE); correlation (cov2cor when cor=FALSE); asset_names; n_assets
- hf_realized_cov with measure=rSemiCov: semicov=list{mixed,negative,positive,concordant} N×N + rcov (=the sum)
- hf_spot_vol: spot_vol (the numeric intraday series); timestamps; daily (per day); periodic (the intraday pattern); n_na

### Pitfalls

- multivariate rTSCov: the package requires a LIST of per-asset xts; a single multi-column input collapses SILENTLY to a scalar — the wrapper handles this, but do not call rTSCov directly
- measure='medRV' -> rMedRVar (rMedRV is deprecated in 1.0.3)
- rTSCov/rKernelCov require PRICES (makeReturns=TRUE); rTSCov needs n>=10*K, otherwise a gate stop
- alignBy is NOT exposed for the realized measures: the data must ALREADY be sampled (e.g. 5-min) intraday data for ONE day; the value is timestamp-invariant without alignBy
- spotVol with method='detPer' ideally wants >=50 days; fewer -> a warning (unstable periodicity), not an error; read n_na
- realized variance ≠ conditional/forecast variance: it is an ex-post estimate of one day's integrated variance, not a forecast

### References

- Boudt, Cornelissen, Payseur et al., the highfrequency vignette + help (help('rCov'/'rBPCov'/'rKernelCov'/'rTSCov'/'rSemiCov'/'spotVol','highfrequency')) <
- Andersen, Bollerslev, Diebold & Labys 2003 (Econometrica 71:579) — realized volatility
- Barndorff-Nielsen & Shephard 2004 (J. Financial Econometrics) — bipower variation (rBPCov)
- Andersen, Dobrev & Schaumburg 2012 (J. Econometrics 169:75) — MedRV, jump-robust
- Zhang, Mykland & Aït-Sahalia 2005 (JASA 100:1394); Zhang 2011 — two-time-scale (rTSCov)
- Barndorff-Nielsen, Hansen, Lunde & Shephard 2008 (Econometrica 76:1481) — realized kernels (rKernelCov)
- Bollerslev, Li, Patton & Quaedvlieg 2020 (J. Econometrics 217:411) — realized semicovariance (rSemiCov)
- Boudt, Croux & Laurent 2011 (J. Empirical Finance 18:353) — deterministic periodicity spot vol (spotVol detPer)

## #157 — HAR realized-volatility models (HAR/HARJ/HARQ/HARQ-J) — estimation, rolling OOS forecasting, simulation

**Module:** `har_realized_volatility.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `har_estimate` | `RM` | `num_array`, `int_array`, `enum`, `num_array`, `num_array`, `int_array`, `int_array`, `boolean`, `integer` | `periods=[1, 5, 22]`, `type='HAR'`, `insanityFilter=True`, `h=1` | `light` | `object` |
| `har_forecast` | `RM` | `num_array`, `int_array`, `integer`, `integer`, `enum`, `enum`, `num_array`, `num_array`, `int_array`, `int_array`, `boolean`, `integer` | `periods=[1, 5, 22]`, `nRoll=10`, `nAhead=1`, `type='HAR'`, `windowType='rolling'`, `insanityFilter=True`, `h=1` | `light` | — |
| `har_simulate` | — | `integer`, `int_array`, `num_array`, `number`, `integer` | `len=1500`, `periods=[1, 5, 22]`, `coef=[0.01, 0.36, 0.28, 0.28]`, `errorTermSD=0.001`, `seed=2025` | `light` | — |

### Use when

you have a daily realized measure (realized variance/RV) of an integrated volatility and you want to model its long-memory dynamics with the heterogeneous autoregressive (HAR) model of Corsi (2009); a daily/weekly/monthly cascade (c(1,5,22)); jump-robust (HARJ) or measurement-error-corrected (HARQ)

### Do not use when

you only have daily returns without a realized measure (go to GARCH — rugarch/tsgarch #28); you want multivariate/conditional-correlation volatility (rmgarch/tsmarch); regime-switching volatility (MSGARCH); the intraday realized measure must be computed FIRST (hf_realized_var)

### Prerequisites

- c06_volatility_regimes/realized_variance_intraday.hf_realized_var (computing the realized variance from intraday data -> it becomes the RM input)
- har_simulate (generating a controlled HAR series for validation/benchmarking)
- c00_data_utilities/reading_delimited_fixed.read_delimited (loading the realized-measure series from a file)

### Alternatives

| instead use | when |
| --- | --- |
| #28 ga_fit (rugarch) / tsgarch | only daily returns are available (no realized measure); a parametric conditional variance |
| type='HARJ' | significant jumps -> separate the continuous (BPV) from the jump component |
| type='HARQ' | measurement error in the RV -> a correction with the realized quarticity (BPQ 2016) |
| mfGARCH (#31) | you want to link the volatility to a low-frequency macro variable (GARCH-MIDAS) |

### Output fields

- coefficients: a named vector (beta0 the intercept + one beta per period); coef_table: Estimate/Std.Error/t/p (from summary.lm)
- r_squared/adj_r_squared/sigma/log_lik: fit diagnostics; qlike_mean: the QLIKE loss (the main volatility-forecast loss); qlike: the per-observation vector
- uncond_mean: the unconditional mean volatility (type='HAR' ONLY; NA elsewhere — the package does not implement it)
- fitted/residuals: chart-data; nobs/type/periods: metadata
- har_forecast: forecast (the getForc vector); forecast_matrix (step×roll); actual (forecastComparison); forecast_residuals; rmse/mae; an object of class HARForecast
- har_simulate: simulation (a numeric vector); an object of class HARSim (object@simulation)

### Pitfalls

- RM is a realized VARIANCE (not returns, not a standard deviation); it must be a positive series; NA are accepted silently by the package -> an explicit gate blocks them
- an invalid type returns NULL SILENTLY in the package (it prints a message); the wrapper fences it with match.arg{HAR,HARJ,HARQ,HARQ-J}
- HARJ/HARQ-J require BPV; HARQ/HARQ-J require RQ (of the same length as RM); without them -> a cryptic armadillo error, the wrapper gives a clean gate
- QLIKE (qlike_mean) is the appropriate robust volatility-forecast loss (Patton 2011); NOT an MSE on the levels — prefer it for model comparison
- uncond_mean is returned ONLY for HAR (NA for HARJ/HARQ/HARQ-J); the @model is a plain lm (an OLS estimate of the HAR components)
- length(RM) must be >= max(periods)+2, otherwise an armadillo error; the wrapper fences it

### References

- Corsi F. 2009, 'A Simple Approximate Long-Memory Model of Realized Volatility', Journal of Financial Econometrics 7(2):174-196
- Bollerslev, Patton & Quaedvlieg 2016, 'Exploiting the errors: A simple approach for improved volatility forecasting', Journal of Econometrics 192(1):1-18 (HARQ/HARQ-J)
- Patton A. 2011, 'Volatility forecast comparison using imperfect volatility proxies', Journal of Econometrics 160(1):246-256 (QLIKE)
- help('HAREstimate','HARModel'), help('HARForecast','HARModel'), help('HARSimulate','HARModel') + live introspection (HARModel 1.0)

## #158 — Generalized Autoregressive Score / Dynamic Conditional Score (GAS/DCS) — a time-varying volatility/location/tails

**Module:** `generalized_autoregressive_score.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `gas_fit` | `y` | `num_array`, `enum`, `enum`, `string`, `integer`, `integer`, `int_array`, `integer` | `distr='norm'`, `scaling='unit'`, `p=1`, `q=1`, `maxeval=10000` | `light` | `object` |
| `gas_forecast` | `object` | `raw_handle`, `enum`, `integer`, `integer`, `num_array` | `method='mean_path'`, `t_ahead=10`, `rep_ahead=1000`, `quant=[0.025, 0.975]` | `light` | — |
| `gas_simulate` | `object` | `raw_handle`, `integer` | `t_sim=10` | `light` | — |

### Use when

one univariate series with score-driven dynamics in a parameter (variance/mean/tails); an explicit distribution (norm/t/ged/gamma..); an alternative to GARCH with a full distributional likelihood

### Do not use when

multivariate volatility/correlation (-> rmgarch/tsmarch DCC/BEKK); pure variance-only dynamics with the standard GARCH interface (-> rugarch/tsgarch); regime switching (-> MSGARCH/MSwM); realized/intraday volatility (-> highfrequency)

### Prerequisites

- gas_fit (ML estimation; check converged==TRUE + status_optim before moving on to forecast/simulate)
- c01_preparation_prechecks/unit_root_normality.run_jarque_bera_test (normality of the innovations: rejection -> distr='t'/'ged' instead of 'norm')
- c00_data_utilities/reading_delimited_fixed.read_delimited (loading the return series from a file)

### Alternatives

| instead use | when |
| --- | --- |
| #28 ga_fit (rugarch) | you want a classic GARCH-family variance model with the standard interface/rolling backtest |
| tsgarch/tsmarch | a modern (m)GARCH; multivariate DCC/copula volatility |
| #31 msg_fit (MSGARCH) | regime-switching volatility (Markov states) |
| quantreg (category 12) | static conditional quantiles without score dynamics |

### Output fields

- coef_table: a matrix Estimate/Std. Error/z value/Pr(>\|z\|) of the coefficients (omega/alpha/phi per parameter)
- par_tv / mean_tv / var_tv: the time-varying parameters / mean / VARIANCE (chart-data; var_tv = the volatility path when par_static drives the variance)
- resid_tv / score_tv / loglik_tv: standardized residuals, the score path, the per-observation log-likelihood
- loglik_sum / aic / bic: fit criteria; converged + status_optim/status_hessian: convergence (a stateless node — do not ignore them)
- gas_forecast: y_ahead_mean (+ y_ahead_sd/y_ahead_quant with simulated_paths = a fan chart); gas_simulate: y_sim/par_tv_sim

### Pitfalls

- the DEFAULT drives the MEAN (par_static=[FALSE,TRUE] for the normal); for a volatility model you MUST set par_static=[1,0] so that the VARIANCE is the dynamic parameter
- converged=FALSE (e.g. status_optim='iteration_limit_reached') => the estimates are NOT reliable; the bounded maxeval yields converged=FALSE instead of a hang
- the fisher_* scaling options are MUCH heavier (a numerical Fisher matrix); unit is the safe default; for orthogonal distributions the scaling variants coincide
- quant under simulated_paths are quantiles of the PREDICTIVE distribution (a fan chart); mean_path gives only a point forecast (no y_ahead_quant)
- gas_forecast(simulated_paths)/gas_simulate are stochastic -> seeded internally (default 2025) for determinism; positive distributions require y>0 (a hard gate)

### References

- the gasmodel vignette + help('gas','gasmodel') (Holý, package 0.6.2)
- Creal, Koopman & Lucas 2013, 'Generalized Autoregressive Score Models with Applications', J. Applied Econometrics 28(5):777-795
- Harvey 2013, 'Dynamic Models for Volatility and Heavy Tails' (DCS), Cambridge University Press
- the distr table of distributions/parameterisations (gasmodel)

## #159 — GARCH-MIDAS (a short-run GARCH × a long-run MIDAS macro component)

**Module:** `garch_midas.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `mfg_fit` | `data`, `y`, `x`, `K` | `df_handle`, `string`, `string`, `integer`, `string`, `enum`, `boolean`, `string` | `low_freq='date'`, `gamma=True` | `light` | `object` |
| `mfg_predict` | `object` | `raw_handle`, `int_array` | — | `light` | — |
| `mfg_simulate` | `n_days`, `mu`, `alpha`, `beta`, `gamma`, `m`, `theta`, `w2`, `K`, `psi`, `sigma_psi` | `integer`, `number`, `number`, `number`, `number`, `number`, `number`, `number`, `integer`, `number`, `number`, `number`, `integer`, `integer`, `number` | `w1=1`, `low_freq=1`, `n_intraday=288`, `corr=0` | `light` | — |

### Use when

you want to link the volatility of high-frequency returns (y) to a slow macro variable (x; e.g. industrial production, the NFCI) through MIDAS; the volatility = tau_t (long run, macro-driven) × g_t (short-run GARCH). mfg_fit -> mfg_predict; mfg_simulate = a standalone DGP

### Do not use when

a purely univariate GARCH with no exogenous macro driver (-> #28 rugarch / #154 tsgarch); regime-switching volatility (-> #31 MSGARCH); multivariate work (-> #29 rmgarch / #155 tsmarch); you have no low-frequency variable that is constant within each period

### Prerequisites

- c15_model_evaluation/arch.run_arch_test (ARCH-LM: is there volatility clustering in y to model?)
- c00_data_utilities/reading_delimited_fixed.read_delimited (loading the long-format df with date/y/x/low.freq columns)
- mfg_fit (check convergence==0 before interpreting the parameters)

### Alternatives

| instead use | when |
| --- | --- |
| #28 rugarch / #154 tsgarch | there is no macro long-run driver; a plain univariate GARCH |
| #31 MSGARCH | a regime change (not a slow macro trend) drives the volatility |
| beta.unrestricted weighting | you want free (non-monotone) MIDAS weighting -> an extra w1 parameter |

### Output fields

- par: a named vector of estimates (mu/alpha/beta/gamma/m/theta/w2[+w1 in the unrestricted case])
- coefficients: a broom.mgarch data_frame (estimate/rob.std.err/p_value/opg.std.err/opg.p_value)
- tau: the long-run component (chart); g: the short-run component (chart); tau×g = the total variance
- variance.ratio: the share of variance explained by the long-run component; tau.forecast: the 1-step long-run value
- llh/bic; convergence (the integer optim code); converged (logical)

### Pitfalls

- silent non-convergence: optim RETURNS a fit even when convergence!=0 — CHECK the converged field before interpreting
- x MUST be constant within each low.freq period; mixed values -> the gate 'a SINGLE unique value' (not a silent error)
- a column literally NAMED 'date' of class Date is mandatory AND the low.freq column must be of class Date; otherwise it is blocked
- K must be < the number of low.freq periods (otherwise negative-length vectors in the MIDAS lag)
- beta.restricted -> w1=1 (a monotonically decreasing weighting); beta.unrestricted -> an extra w1 parameter
- mfg_predict returns the total conditional variance per horizon (not tau or g separately)

### References

- Engle, Ghysels & Sohn 2013 'Stock Market Volatility and Macroeconomic Fundamentals' (REStat 95:776)
- Conrad & Kleen 2020 'Two are better than one: Volatility forecasting using multiplicative component GARCH-MIDAS' (J. Applied Econometrics 35:19)
- Ghysels, Santa-Clara & Valkanov 2004/2006 (MIDAS regressions)

## #160 — BEKK-family multivariate GARCH (BEKK/diagonal/scalar) + multivariate VaR + Volatility IRF

**Module:** `bekk_family_multivariate.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `bekk_estimate` | `y` | `matrix_handle`, `enum`, `boolean`, `num_array`, `boolean`, `integer`, `number`, `integer` | `asymmetric=False`, `QML_t_ratios=False`, `max_iter=50`, `crit=1e-09`, `seed=2025` | `light` | `object` |
| `bekk_var` | `object` | `raw_handle`, `number`, `num_array`, `enum` | `p=0.99` | `light` | — |
| `bekk_virf` | `object` | `raw_handle`, `integer`, `number`, `integer`, `integer`, `number`, `boolean` | `time=1`, `q=0.05`, `index_series=1`, `n_ahead=10`, `ci=0.9`, `time_shock=False` | `light` | — |

### Use when

N-dimensional returns; you want the full BEKK dynamic conditional covariance (spillovers/co-volatility) + risk (a portfolio VaR) or volatility impulse responses

### Do not use when

a large N (BEKK has ~O(N²) parameters -> the curse of dimensionality; go to DCC #155/#29); a univariate series (rugarch #28); you need an asymmetric VIRF (not implemented)

### Prerequisites

- c01_preparation_prechecks/unit_root_suite.wrap_ur_df (stationarity of the returns before the GARCH)
- bekk_estimate (bekk_valid=TRUE declares a stationary/valid BEKK process before VaR/VIRF)
- c00_data_utilities/reading_delimited_fixed.read_delimited (loading the T×N matrix of returns if it comes from a file)

### Alternatives

| instead use | when |
| --- | --- |
| #155 tm_dcc_estimate (tsmarch) or #29 dcc_fit (rmgarch) | a large N / you want a scalable conditional correlation rather than a full BEKK |
| type='dbekk' / 'sbekk' | fewer parameters (diagonal/scalar) when the full BEKK is not identified |
| 12-distribution-risk/pa_var | a non-model-based (historical/gaussian/modified) VaR without MGARCH dynamics |

### Output fields

- bekk_valid: logical — TRUE=a stationary/valid BEKK; FALSE=degenerate (the VaR/VIRF are unreliable)
- log_likelihood/AIC/BIC: fit criteria; theta: the estimated parameters (vech)
- C0/A/G: the BEKK parameter matrices (C0 the lower-triangular intercept, A the ARCH matrix, G the GARCH matrix)
- sigma_t: the T×N(N+1)/2 conditional st.dev/covariance path (chart-data)
- var_values (bekk_var): the T×1 (portfolio) or T×N (per-series) VaR path
- virf/virf_upper/virf_lower (bekk_virf): n_ahead × N(N+1)/2 responses + bands

### Pitfalls

- bekk_valid=FALSE is NOT blocked (a valid output with a flag; a stateless node): always read it before using the VaR/VIRF
- VaR with distribution='empirical' requires >=1000 observations (gated); the default is 'normal' — switch to 't' for fat tails
- the VIRF exists only for a SYMMETRIC BEKK (asymmetric=FALSE); an asymmetric object is blocked by a gate
- portfolio_weights=NULL -> a per-series VaR (N columns); a vector of length N -> a portfolio VaR (1 column)
- the BEKK curse of dimensionality: ~O(N²) parameters; for N>~4 prefer DCC (#155/#29)

### References

- Engle & Kroner 1995 (Econometric Theory 11:122) — the BEKK parameterisation
- Hafner & Herwartz 2006 (J. Int. Money & Finance 25:719) — Volatility Impulse Responses
- Basel Committee — VaR at 99% confidence (the default p)

## #161 — (Hierarchical) Hidden Markov Models + Viterbi global decoding + forecasting

**Module:** `hidden_markov_viterbi.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `hmm_fit` | `data` | `num_array`, `integer`, `enum`, `integer`, `integer`, `integer` | `nstates=2`, `runs=5`, `iterlim=100`, `seed=2025` | `heavy` | `object` |
| `hmm_decode` | `object` | `raw_handle` | — | `light` | — |
| `hmm_predict` | `object` | `raw_handle`, `integer`, `number` | `ahead=5`, `alpha=0.05` | `light` | — |

### Use when

a univariate series (returns/observations) with latent discrete regimes; you want a full HMM with probabilistic state-dependent distributions (normal/t/gamma/..) + decoding of the most likely state sequence

### Do not use when

regime-conditional GARCH volatility (-> #31 MSGARCH msg_fit_*); a linear Markov-switching model with regressors (-> #30 MSwM msw_fit); threshold (self-exciting) non-Markovian regimes (-> #32 tsDyn setar_fit); hierarchical/multi-scale two-level data (hierarchy=TRUE is not exposed)

### Prerequisites

- hmm_fit (the PRODUCER; check converged/n_accepted_runs before decode/predict)
- hmm_decode (the degenerate flag: did it collapse to <k states?)
- c00_data_utilities/reading_delimited_fixed.read_delimited (loading the series from a file, if needed)

### Alternatives

| instead use | when |
| --- | --- |
| #31 msg_fit_ml/msg_fit_mcmc (MSGARCH) | the regimes concern volatility clustering (the conditional variance), not the level/mean |
| #30 msw_fit (MSwM) | a Markov-switching linear model with exogenous regressors |
| #32 setar_fit/lstar_fit (tsDyn) | the regimes are determined by an observable threshold variable, not by a latent Markov chain |
| sdd='t' | fat tails in the returns within a regime |

### Output fields

- hmm_fit: log_lik/AIC/BIC/npar/nobs; estimates (a data_frame parameter/lb/estimate/ub — the Gamma_ij transitions + mu/sigma/df per state); nstates/sdd
- hmm_fit convergence: nlm_code (1/2=OK); converged (bool); n_accepted_runs — check them BEFORE interpreting (a stateless node: stderr is lost)
- hmm_decode: states (an integer sequence of length T); state_counts/state_labels; n_states_used; degenerate (TRUE => fewer than nstates were used)
- hmm_predict: state_probs (ahead × nstates probabilities); forecast (ahead × {lb,estimate,ub} observations); it decodes internally (predict requires it)

### Pitfalls

- state labelling is not inherently ordered (label switching); identify the states through the mu/sigma in estimates, not through the index 1/2
- degenerate=TRUE or converged=FALSE => the solution collapsed/did not converge — do NOT interpret the regimes; increase runs or change sdd
- AIC/BIC are comparable ONLY on the same data & sdd family (a different nstates is nested; a different sdd is non-nested)
- gamma/lognormal require strictly positive values, poisson non-negative integers — for raw returns use normal/t
- the artificial Date column is a placeholder (fHMM requires dates); it does not affect the estimation, do not read it as a real calendar

### References

- Oelschläger, Adam & Michels, the fHMM JSS/ vignette 'fHMM' <
- help('set_controls','fHMM'), help('fit_model','fHMM'), help('decode_states','fHMM'), help('predict.fHMM_model','fHMM')
- Zucchini, MacDonald & Langrock 2016, 'Hidden Markov Models for Time Series' 2nd ed. (Viterbi global decoding §5)
- Hamilton 1989 (Econometrica 57:357) Markov-switching regimes

## #162 — Bayesian univariate Stochastic Volatility (vanilla / Student-t / leverage) via MCMC

**Module:** `bayesian_univariate_stochastic.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `sv_sample` | `y` | `num_array`, `enum`, `integer`, `integer`, `num_array`, `num_array`, `number`, `number`, `num_array`, `enum`, `integer`, `number` | `draws=500`, `burnin=200`, `priorsigma=1`, `thin=1`, `ess_min=20` | `mcmc` | `object` |
| `sv_predict` | `object` | `raw_handle`, `integer` | `steps=1` | `light` | — |
| `sv_simulate` | `len` | `integer`, `number`, `number`, `number`, `number`, `number` | `mu=-10`, `phi=0.98`, `sigma=0.2`, `rho=0` | `light` | — |

### Use when

a univariate return series; you want the latent (unobserved) volatility as a stochastic process with a full Bayesian posterior (uncertainty bands on the volatility), not a deterministic GARCH-type recursion

### Do not use when

you want point/ML volatility or closed-form forecasting (-> GARCH #28 rugarch/tsgarch); multivariate volatility/correlation (-> DCC #29 rmgarch/tsmarch); regime-switching volatility (-> #31 MSGARCH); very large samples with a tight latency budget (the MCMC is expensive)

### Prerequisites

- sv_sample (read converged/min_ess before trusting the posteriors — a low ESS ⇒ raise the number of draws)
- c00_data_utilities/reading_delimited_fixed.read_delimited (load the return series; NOT price levels)
- sv_simulate (a data-generating check / prior predictive check before fitting real data)

### Alternatives

| instead use | when |
| --- | --- |
| #28 ga_fit (rugarch) / tsgarch | you want a deterministic ML GARCH with closed-form forecasts rather than latent-SV MCMC |
| #31 msg_fit_mcmc (MSGARCH) | the volatility changes regime (Markov switching) rather than following a continuous AR(1) log-volatility |
| #29 dcc_fit (rmgarch) | multivariate volatility + a time-varying correlation |
| model='t' | fat tails in the returns beyond what the stochastic volatility delivers |
| model='leverage' | asymmetry: negative returns raise the volatility more (the leverage effect) |

### Output fields

- para_summary: a matrix mean/sd/5%/50%/95%/ESS per parameter (mu=the level, phi=persistence, sigma=vol-of-vol, [nu],[rho])
- ess / min_ess / converged: the convergence capture — converged=FALSE ⇒ insufficient mixing, do not interpret the posteriors
- vol_mean (+ vol_time): the posterior mean of exp(h_t/2) per time point (chart-data; NULL when keeptime='last')
- sv_predict: vol_mean/vol_median + vol_lower(5%)/vol_upper(95%) per step — posterior predictive bands of the future volatility
- sv_simulate: y (returns) + vol (the true latent volatility) + para — chart-data for a synthetic path

### Pitfalls

- check the converged flag first: SV MCMC can silently suffer monstrous autocorrelation (a very low phi ESS); 500 draws is a smoke test — for production raise draws/burnin
- phi≈1 ⇒ an almost non-stationary log-volatility (high persistence); phi near 0 ⇒ the volatility is nearly white noise
- y is returns (roughly mean-zero), NOT price levels; otherwise the log(y^2) offset produces nonsense
- vol_mean refers to exp(h_t/2) (a standard deviation), not a variance; do not compare it directly with a GARCH conditional variance
- predict/simulate are stochastic -> seed=2025 by default; the same seed ⇒ the same draws (a reproducible node)
- keeptime='last' discards the latent path (vol_mean=NULL) — use it only when you do not need the volatility chart

### References

- Kastner (2016) 'Dealing with Stochastic Volatility in Time Series Using the reference Package stochvol', JSS 69(5)
- Kastner & Frühwirth-Schnatter (2014) ASIS interweaving (CSDA 76:408) — the sampler behind svsample
- help('svsample','stochvol'), svtsample, svlsample, svsim, predict.svdraws ( stochvol)
- Jacquier, Polson & Rossi (1994, JBES 12:371) — the foundations of Bayesian SV

## #163 — Multivariate factor stochastic volatility (Bayesian MCMC) + model-implied & predictive covariance/correlation

**Module:** `multivariate_factor_stochastic.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `fsv_sample` | `y` | `matrix_handle`, `integer`, `integer`, `integer`, `enum`, `integer` | `factors=1`, `draws=300`, `burnin=100`, `seed=2025` | `mcmc` | `object` |
| `fsv_cov` | `object` | `raw_handle` | — | `light` | — |
| `fsv_predict` | `object` | `raw_handle`, `int_array`, `integer` | `ahead=1`, `each=1` | `light` | — |

### Use when

multivariate returns (a small to medium N); you want a time-varying covariance/correlation through a few latent factors with stochastic-volatility dynamics + Bayesian posterior uncertainty

### Do not use when

a univariate series (-> stochvol sv_sample); you want a parametric MGARCH point estimate (DCC/GO-GARCH -> rmgarch/tsmarch); a very large N with no factor structure; too few observations (<~50) for reliable MCMC

### Prerequisites

- fsv_cov (the posterior-mean model-implied cov/cor at the last t — a check on plausible magnitudes)
- fsv_predict (the posterior predictive h-step cov/cor)
- c00_data_utilities/reading_delimited_fixed.read_delimited (loading the T×N returns if they come from a file)

### Alternatives

| instead use | when |
| --- | --- |
| rmgarch dcc_fit / tsmarch tm_dcc_estimate | you want a parametric DCC/GO-GARCH point-estimate MGARCH rather than a Bayesian factor structure |
| stochvol sv_sample | a univariate series — you do not need a multivariate covariance |
| restrict='upper' | you need identification/interpretation of the factor loadings (not only the covariance) — it stabilises the MCMC |

### Output fields

- fsv_sample.facload_mean: the posterior-mean matrix of factor loadings (N × factors); it shows which series load on the common factors
- fsv_sample.communalities / communality_total: the share of variance per series (and in total) explained by the factors
- fsv_sample.para_mean: the posterior-mean mu/phi/sigma per idiosyncratic & factor log-volatility process (phi->1 = high persistence)
- fsv_sample.ledermann_bound / exceeds_ledermann: the static bound on identifiable factors; TRUE = take care with the identification of the loadings
- fsv_cov.cov_mean/cor_mean (+ _sd): the posterior mean & posterior sd of the conditional covariance/correlation at the last t
- fsv_predict.pred_cov_mean/pred_cor_mean: a list of posterior-mean matrices per horizon (the key = ahead)

### Pitfalls

- restrict='none' is preferable for ESTIMATING the covariance/forecast; 'upper' only when you want identifiable/interpretable loadings (a strong a-priori assumption)
- exceeds_ledermann=TRUE is NOT an error: the package deliberately allows more factors than the static Ledermann bound (identification comes from the time-varying volatilities); it is merely a caveat for interpreting the loadings
- the signs of the factor loadings & factors are not identified by the likelihood (sign switching); interpret magnitudes/patterns, not absolute signs
- fsv_cov returns ONLY the last time point (keeptime='last') = the current conditional covariance, not the whole path
- MCMC: few draws/burnin -> noise in the posterior; the posterior_sd fields show the uncertainty, do not read only the means

### References

- the factorstochvol vignette & help (help('fsvsample','factorstochvol'), covmat, cormat, predcov, predcor, ledermann) — factorstochvol 1.1.2 <
- Kastner, Frühwirth-Schnatter & Lopes 2017, 'Efficient Bayesian Inference for Multivariate Factor Stochastic Volatility Models', JCGS 26(4):905-917
- Kastner 2019, 'Sparse Bayesian time-varying covariance estimation in many dimensions', J. Econometrics 210(1):98-115 (the Normal-Gamma shrinkage prior)

## #164 — Discrete-time Markov chain: estimating the transition matrix (MLE/Laplace/bootstrap CI) + long-run analytics (the stationary distribution, mean first passage times, irreducibility, period)

**Module:** `discrete_time_markov.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `mc_fit` | `data` | `series_codes`, `enum`, `number`, `number`, `integer`, `boolean`, `integer` | `method='mle'`, `laplacian=0`, `confidencelevel=0.95`, `nboot=10`, `sanitize=False`, `seed=2025` | `heavy` | `object` |
| `mc_analytics` | `object` | `raw_handle` | — | `light` | — |

### Use when

a discrete sequence of states (regimes/ratings/states); you want the estimated transition matrix, the long-run (stationary) distribution, expected first passage times, or an irreducibility/period check

### Do not use when

continuous return/volatility series (-> GARCH #28/#33/#34); latent regime switching on continuous observations (-> MSwM #30/MSGARCH #31); a continuous-time Markov chain (CTMC); higher-order/order-selection dependence

### Prerequisites

- mc_fit (it produces the 'markovchain' object -> the input to mc_analytics)
- c00_data_utilities/reading_delimited_fixed.read_delimited (loading the state sequence from a file)

### Alternatives

| instead use | when |
| --- | --- |
| MSwM msw_fit (#30) | the regimes are latent on a continuous observed series, not directly observed states |
| MSGARCH msg_spec/msg_fit_* (#31) | Markov switching in the variance of continuous returns |
| fHMM (#32) | a hidden Markov model with emission distributions rather than observed states |

### Output fields

- transitionMatrix: the estimated transition matrix (rows=from, they sum to 1)
- standardError / lowerEndpointMatrix / upperEndpointMatrix: the SE + CI per element (confidenceLevel)
- log_likelihood: the log-likelihood of the fit
- steadyStates: the stationary distribution (a matrix; >1 row if there are several recurrent classes)
- meanFirstPassageTime: the expected number of steps i->j (the diagonal=0); NULL + mfpt_note if the chain is not ergodic
- is_irreducible / period: the irreducibility bool + the period (NA + period_note if it is not irreducible)

### Pitfalls

- markovchainFit does NOT fail on NA (it treats them as a separate state) & it accepts a single state — the wrapper's gates block both explicitly
- steadyStates returns a MATRIX: >1 row means several closed recurrent classes (a non-unique stationary distribution)
- period emits a WARNING (not an error) on a non-irreducible chain -> the wrapper returns NA+a note, do not interpret an invalid value
- meanFirstPassageTime requires an ergodic (irreducible) chain -> NULL+a note otherwise, not an error that would crash the node
- method='bootstrap' is STOCHASTIC (resampling CI) -> use the same seed for reproducibility; mle/laplace are deterministic

### References

- Spedicato, 'Discrete Time Markov Chains with the reference', 2017 (the markovchain vignette)
- help('markovchainFit','markovchain'), steadyStates, meanFirstPassageTime, period, is.irreducible
- Norris 1997, Markov Chains (CUP) — the stationary distribution, first passage, periodicity
