<!-- SPDX-License-Identifier: AGPL-3.0-only -->
# 05-cointegration

8 METHOD-SELECTION cards, 8 modules, 29 nodes.

Every card below governs one wrapper module in this package. The cards are the
reason a method exists here at all: they record when it applies, what to reach
for instead, and the traps that make its output easy to misread.

## #23 — Johansen (ca.jo) + restricted VECM (cajorls) + Phillips-Ouliaris/Engle-Granger family (ca.po)

**Module:** `johansen_restricted_vecm.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `wrap_ca_jo` | `x` | `matrix_handle`, `enum`, `enum`, `integer`, `enum` | `K=2` | `light` | `object` |
| `wrap_cajorls` | `z` | `raw_handle`, `integer` | `r=1` | `light` | — |
| `wrap_ca_po` | `z` | `matrix_handle`, `enum`, `enum`, `enum` | — | `light` | — |

### Use when

A system of >=2 I(1) series; testing the cointegration rank + extracting beta/alpha, or a residual-based test (ca.po Pu/Pz).

### Do not use when

You need p-values for the rank (go to tsDyn); mixed order I(0)/I(1) (go to ARDL/bounds).

### Prerequisites

- c01_preparation_prechecks/unit_root_normality.run_adf_test
- c01_preparation_prechecks/unit_root_normality.run_kpss_test
- c01_preparation_prechecks/seasonal_unit_roots

### Alternatives

| instead use | when |
| --- | --- |
| #24 rank_test | You want p-values for the rank + 5 deterministic specs. |
| #25 ARDL / #26 dynamac | Single equation with a mixed order of integration I(0)/I(1). |
| #27 cointReg | The rank is known (=1) and you want an unbiased estimate of beta. |

### Output fields

- teststat: statistics per rank hypothesis (compare with cval)
- cval: critical values 10/5/1% (NOT a p-value)
- lambda: eigenvalues
- V: normalised cointegrating vectors (beta)
- W: loading weights (alpha, speed of adjustment)
- PI: Pi = alpha beta'
- ca.po teststat/cval: Pu or Pz; res = residuals of the cointegrating regression
- cajorls beta/rlm_coef: restricted VECM at rank r

### Pitfalls

- ca.jo gives ONLY critical values, NOT a p-value — compare teststat>cval (confirmed by the tsDyn docs).
- wrap_ca_jo(type=..) returns ONLY the selected test type per call: teststat/cval hold trace OR max-eigen, not both — to compare trace vs eigen call it TWICE (type='trace' & type='eigen'); by contrast rank_test gives trace AND eigen p-values together in one call.
- The K of ca.jo (lag in levels) = lag+1 of rank_test (off-by-one).
- KPSS has the opposite polarity among the preconditions: reject H0 ⇒ non-stationary.
- Pz is invariant to the normalisation; prefer it when there is no natural dependent variable.
- S4 object → to_mcp compact stub (rely on the atomic fields).

### References

- Johansen 1988/1991
- Phillips-Ouliaris 1990 (Econometrica 58:165-193)
- Enders 2015
- Lutkepohl 2005
- KPSS 1992
- urca reference manual (ca.jo/ca.po/cajorls)

## #24 — VECM estimate + Johansen rank_test (ML-only) + rank.select + predict

**Module:** `vecm_estimate_johansen.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `vecm_estimate` | `data`, `lag` | `matrix_handle`, `integer`, `integer`, `enum`, `enum`, `enum` | `r=1` | `light` | `object` |
| `vecm_rank_test` | `vecm` | `raw_handle`, `enum`, `number` | `cval=0.05` | `light` | — |
| `vecm_rank_select` | `data`, `lag_max` | `matrix_handle`, `integer`, `enum` | — | `light` | — |
| `vecm_predict` | `vecm` | `raw_handle`, `integer` | `n_ahead=5` | `light` | — |

### Use when

A system VECM with a Johansen rank test WITH p-values, 5 deterministic specs, 2OLS/ML estimation, rank selection by IC, forecasting.

### Do not use when

You need seasonal/exogenous regressors in the Johansen test (ca.jo only); a single equation of mixed order.

### Prerequisites

- c01_preparation_prechecks/unit_root_normality.run_adf_test
- c01_preparation_prechecks/unit_root_normality.run_kpss_test

### Alternatives

| instead use | when |
| --- | --- |
| #23 ca.jo | You want seasonal/exogenous regressors or a plain critical-value comparison. |
| #25 ARDL / #26 dynamac | Single equation, mixed order of integration. |
| #27 cointReg | Known rank=1, you want an unbiased beta with t-tests. |

### Output fields

- beta: cointegrating vectors
- alpha: loadings (negative & significant ⇒ valid error correction)
- PI: Pi = alpha beta'
- rank_test table: trace/eigen stats AND p-values
- r: selected rank (the first H0 not rejected at cval)
- best_ranks: AIC/BIC/HQ selection
- forecast: matrix n.ahead × k (chart-data)

### Pitfalls

- rank_test REQUIRES estim='ML' — with 2OLS it is blocked (hard gate).
- Lag convention: the K of ca.jo = lag+1 of tsDyn.
- predict is inherited from class VAR (getS3method namespace); S3 collision risk with vars/svars → run the WHOLE suite.
- p-values = gamma approximation (Doornik); the effective sample size differs from gretl.

### References

- Johansen 1996 (OUP)
- Doornik 1998/1999
- Doornik-Hendry-Nielsen 1998
- Enders 2015
- Lutkepohl 2005
- tsDyn reference manual (VECM/rank_test 'Comparison with urca')

## #25 — ARDL / UECM estimation + PSS bounds F/t-test + RECM + multipliers + coint_eq

**Module:** `ardl_uecm_estimation.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `ardl_fit` | `formula`, `data`, `order` | `formula`, `df_handle`, `integer` | — | `light` | `object` |
| `ardl_auto` | `formula`, `data`, `max_order` | `formula`, `df_handle`, `integer`, `string`, `enum`, `boolean` | `selection='AIC'`, `grid=False` | `light` | `object` |
| `ardl_bounds_f` | `object`, `case` | `raw_handle`, `integer`, `enum`, `integer` | `n_replications=40000` | `light` | — |
| `ardl_bounds_t` | `object`, `case` | `raw_handle`, `integer`, `integer` | `n_replications=40000` | `light` | — |
| `ardl_recm` | `object`, `case` | `raw_handle`, `integer` | — | `light` | — |
| `ardl_multipliers` | `object` | `raw_handle`, `string`, `boolean` | `type='lr'`, `se=False` | `light` | — |
| `ardl_coint_eq` | `object`, `case` | `raw_handle`, `integer` | — | `light` | — |

### Use when

Single-equation cointegration with regressors of mixed order I(0)/I(1); a bounds test without pre-classification; multipliers/ECM/cointegrating equation.

### Do not use when

Any I(2) series (the bounds test breaks down); multiple cointegrating relations (go to the system Johansen).

### Prerequisites

- c01_preparation_prechecks/unit_root_normality.run_adf_test
- c01_preparation_prechecks/unit_root_normality.run_kpss_test

### Alternatives

| instead use | when |
| --- | --- |
| #26 dynamac | You want stochastic counterfactual simulation + residual diagnostics. |
| #23 / #24 (Johansen/VECM) | System / multiple cointegrating relations. |
| #27 cointReg | The level relationship is confirmed, you want an unbiased beta. |

### Output fields

- bounds statistic/p_value: htest atomic fields
- tab: statistic + critical bounds I(0)/I(1) + alpha + p-value
- parameters/PSS2001parameters: critical value bounds
- coefficients/best_order/AIC/BIC/log_lik/nobs
- multipliers: lr (default)/sr/interim
- recm: restricted ECM (the ECT loading is negative & significant)
- coint_eq: fitted cointegrating series (chart-data)

### Pitfalls

- Inconclusive region: a statistic between the I(0)/I(1) bounds ⇒ NO conclusion about cointegration.
- The default p-value is asymptotic (T=1000, exact=FALSE, deterministic); ONLY exact=TRUE runs a simulation (the reference iterations, wrapper seed=2025).
- The wrong case (1-5) ⇒ the wrong H0; you do not restrict a deterministic term that is not there.
- case=5 requires a trend; case=1 requires a model without a constant.

### References

- Pesaran-Shin-Smith 2001 (JAE 16(3):289-326)
- Pesaran-Shin 1999
- Enders 2015
- ARDL reference manual (bounds_f_test/bounds_t_test cases)

## #26 — dynardl ARDL/ECM + stochastic simulation + PSS bounds + residual diagnostics

**Module:** `dynardl_ardl_ecm.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `dmac_ardl` | `formula`, `data` | `formula`, `df_handle`, `series_codes`, `series_codes`, `boolean`, `boolean`, `boolean`, `boolean`, `string`, `integer`, `integer` | `ec=False`, `trend=False`, `constant=True`, `simulate=False`, `sims=1000`, `range=20` | `heavy` | `object` |
| `dmac_pssbounds` | `object` | `raw_handle` | — | `light` | — |
| `dmac_autocorr` | `object` | `raw_handle`, `enum`, `integer` | `order=1` | `light` | — |

### Use when

A single-equation ARDL/ECM when you want counterfactual shock simulation (response path chart-data) + native PSS bounds + BG/SW residual diagnostics.

### Do not use when

You do not need simulation/diagnostics (go to ARDL); system/multiple relations; I(2) series.

### Prerequisites

- c01_preparation_prechecks/unit_root_normality.run_adf_test
- c01_preparation_prechecks/unit_root_normality.run_kpss_test

### Alternatives

| instead use | when |
| --- | --- |
| #25 ARDL | The same PSS bounds, richer multipliers/auto-order, without simulation. |
| #23 / #24 (Johansen/VECM) | System VECM. |
| #27 cointReg | Unbiased estimation of beta. |

### Output fields

- coefficients/AIC/BIC/log_lik/nobs/residuals
- simulation: data_frame central + ll95/ul95 response path (chart-data, only with simulate=TRUE)
- fstat/tstat: PSS statistics (NOT a p-value)
- f_bounds/t_bounds: named vectors of critical I(0)/I(1) × 10/5/1%
- bg_statistic/bg_pvalue: Breusch-Godfrey autocorrelation
- sw_statistic/sw_pvalue: Shapiro-Wilk normality

### Pitfalls

- pssbounds does NOT give a p-value — compare fstat/tstat with the I(0)/I(1) bounds (as with urca).
- An inconclusive region between the bounds ⇒ NO conclusion.
- data MUST be a plain data_frame, NOT a ts (hard gate).
- pssbounds REQUIRES ec=TRUE (error-correction form).
- simulate=TRUE is Monte Carlo (stochastic) → wrapper seed=2025; a different seed ⇒ different CI bands.
- A Breusch-Godfrey rejection ⇒ autocorrelation undermines the validity of the bounds test.

### References

- Pesaran-Shin-Smith 2001
- Jordan-Philips 2018 (The dynamac)
- Enders 2015
- dynamac reference manual (dynardl/pssbounds/dynardl.auto.correlated)

## #27 — Modified-OLS cointegrating regressions: FM-OLS / D-OLS / IM-OLS

**Module:** `modified_ols_cointegrating.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `creg_fmols` | `x`, `y` | `matrix_handle`, `series_handle`, `enum`, `enum`, `enum`, `boolean` | `demeaning=False` | `light` | — |
| `creg_dols` | `x`, `y` | `matrix_handle`, `series_handle`, `enum`, `enum`, `enum`, `enum`, `enum`, `boolean` | `demeaning=False` | `light` | — |
| `creg_imols` | `x`, `y` | `matrix_handle`, `series_handle`, `enum`, `enum`, `enum` | — | `light` | — |

### Use when

ONE known/assumed cointegrating relation; unbiased, asymptotically efficient estimation of beta with valid t-tests (correcting endogeneity/serial correlation).

### Do not use when

You have not confirmed cointegration (these are estimators, NOT tests); multiple cointegrating vectors (go to a system VECM).

### Prerequisites

- c01_preparation_prechecks/unit_root_normality.run_adf_test
- c01_preparation_prechecks/unit_root_normality.run_kpss_test

### Alternatives

| instead use | when |
| --- | --- |
| FM-OLS (creg_fmols) | Default; semiparametric long-run variance correction (Phillips-Hansen). |
| D-OLS (creg_dols) | Parametric correction with leads/lags of the differenced regressors, no kernel choice. |
| IM-OLS (creg_imols) | Robust without bandwidth tuning; it REPLACES CCR (which the package does not provide). |
| #23-#26 (Johansen/ARDL/bounds) | You want a TEST for the existence of cointegration, not an estimate. |

### Output fields

- beta: cointegrating vector (the main objective)
- delta: coefficients of the deterministic terms
- theta: combined (delta, beta)
- sd.theta/t.theta/p.theta: SE/t/p (only when y is one-dimensional)
- residuals: FM residuals[1] is always NA (structural)
- omega.u.v: conditional long-run variance; Omega: full LRV matrix
- bandwidth/kernel: the choices; D-OLS lead.lag

### Pitfalls

- Estimators, NOT tests — they do not decide whether cointegration exists (run #23-#26 first).
- FM residuals[1] = NA by design (not a bug).
- t/p-values only for one-dimensional y.
- IM-OLS has NO demeaning argument (unlike FM/D).
- Align deter (const/trend) with the deterministic spec of the test that confirmed the relation.
- IM replaces CCR — do not ask for CCR.

### References

- Phillips-Hansen 1990 (RES 57:99-125)
- Stock-Watson 1993 (Econometrica, D-OLS)
- Vogelsang-Wagner 2014 (J.Econometrics, IM-OLS)
- Andrews 1991
- Newey-West 1994
- Enders 2015
- cointReg reference manual (cointRegFM/D/IM)

## #139 — Fractionally Cointegrated VAR (Johansen-Nielsen): fractional cointegration with estimated d/b + rank tests (asymptotic + wild bootstrap) + lag selection

**Module:** `fractionally_cointegrated_var.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `fcv_estimate` | `x` | `matrix_handle`, `integer`, `integer`, `num_array`, `num_array`, `boolean`, `boolean`, `boolean`, `boolean`, `boolean`, `boolean` | `k=1`, `r=1`, `restrict_db=True`, `constrained=False`, `level_param=True`, `r_constant=False`, `unr_constant=False`, `grid_search=False` | `light` | `object` |
| `fcv_rank_test` | `x` | `matrix_handle`, `integer`, `boolean`, `boolean`, `boolean` | `k=1`, `restrict_db=True`, `constrained=False`, `grid_search=False` | `light` | — |
| `fcv_lag_select` | `x` | `matrix_handle`, `integer`, `integer`, `integer`, `boolean` | `kmax=2`, `order=2`, `grid_search=False` | `light` | — |
| `fcv_boot_rank` | `x`, `seed` | `matrix_handle`, `integer`, `integer`, `integer`, `integer`, `integer`, `boolean` | `k=1`, `r1=0`, `r2=1`, `B=99`, `grid_search=False` | `heavy` | — |

### Use when

a system of >=2 series with fractional integration (long memory, non-integer I(d)) -> fractional cointegration; estimating d/b + the cointegrating beta + the adjustment alpha; lag_select -> rank_test -> boot_rank -> estimate (the PRODUCER)

### Do not use when

purely integer I(1) without long memory -> the integer Johansen #23 urca/#24 tsDyn; a single equation of mixed order -> ARDL #25/dynamac #26; hypothesis restrictions/forecasting (FCVARhypoTest/FCVARforecast are omitted)

### Prerequisites

- c02_univariate_forecasting/long_memory_fractional.fdf_gph (estimate the fractional order d — FCVAR vs integer Johansen)
- c02_univariate_forecasting/long_memory_fractional.fdf_sperio (the Sperio estimate of d)
- c01_preparation_prechecks/unit_root_normality.run_adf_test (non-stationarity)
- c01_preparation_prechecks/unit_root_normality.run_kpss_test (confirmatory; rejection=non-stationary)

### Alternatives

| instead use | when |
| --- | --- |
| 05-cointegration/wrap_ca_jo | the integer Johansen VECM when d~=1 (standard critical values, simpler) |
| 05-cointegration/vecm_rank_test | the integer Johansen WITH p-values |
| fcv_boot_rank | a small sample -> the asymptotic LR rank test is unreliable, you need the wild bootstrap |

### Output fields

- fcv_estimate: d/b (fractional params), beta (p x r cointegrating), alpha (p x r adjustment), Pi=alpha*beta', Gamma/Omega/mu, log_lik/fp/SE, roots (re/im/mod), object (the FCVAR_model PRODUCER)
- fcv_rank_test: LRstat/pv vectors of length p+1 (the i-th -> rank=i-1); the rank is read bottom-up (the first non-rejected H0); pv=999/NA if unavailable
- fcv_lag_select: aic/bic (+ i_aic/i_bic, the selected lag), pvWNQ/pvWNLM white-noise tests per lag
- fcv_boot_rank: LRbs (B simulated LR — chart-data), LRstat (the observed one), pv_bs (the bootstrap p-value = H.pvBS)

### Pitfalls

- the raw opt object (~40 fields) is NOT exposed; it is built internally from a curated surface (bounds/restrict_db/constrained/level_param/constants/grid_search)
- grid_search defaults to FALSE (a deviation from the package default gridSearch=1); the switching optimizer converges; the grid search is an expensive accuracy refinement for local maxima in d/b
- the bootstrap p-value is in br$H.pvBS; br.pv comes back empty (length 0)
- FCVAR does NOT enforce r1<r2 (a silently wrong negative LR) -> the wrapper gates it
- full rank r=p -> a singular Hessian in the SE (silenced); it means no rank reduction (stationary fractional differences); r>p -> a cryptic non-conformable arguments error

### References

- Johansen & Nielsen 2012 (Econometrica 80:2667-2732, Likelihood inference for a fractionally cointegrated VAR)
- Cavaliere, Rahbek & Taylor 2010 (J. Econometrics 158:7-24, wild-bootstrap rank test)
- Doornik 2018 (Scand. J. Statist. 45(2), accelerated switching algorithm)
- FCVAR 0.1.4 reference manual (FCVARoptions/FCVARestn/FCVARrankTests/FCVARlagSelect/FCVARbootRank) — live-verified via Rd + votingJNP2014 probes

## #140 — Nonlinear (asymmetric) ARDL — NARDL (Shin-Yu-Greenwood-Nimmo) + PSS bounds + CUSUM/CUSUMQ stability

**Module:** `nonlinear_ardl_nardl.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `nar_fit` | `data`, `y`, `x` | `df_handle`, `string`, `string`, `enum`, `integer`, `integer` | `maxlag=4`, `case=3` | `light` | `object` |
| `nar_bounds` | `object` | `raw_handle` | — | `light` | — |
| `nar_stability` | `object` | `raw_handle` | — | `light` | — |

### Use when

Single-equation cointegration with an ASYMMETRIC relation: the regressor acts differently on increases vs decreases (positive/negative partial sums); regressors of mixed order I(0)/I(1); EXACTLY one decomposed regressor; long-run beta+/beta- + a Wald test of asymmetry + PSS bounds + CUSUM/CUSUMQ.

### Do not use when

A symmetric relation (a linear ARDL suffices) -> #25; any I(2) series (the bounds test breaks down); multiple cointegrating relations / a system -> Johansen #23/#24; >1 decomposed regressor (nardl accepts EXACTLY one).

### Prerequisites

- c01_preparation_prechecks/unit_root_normality.run_adf_test
- c01_preparation_prechecks/unit_root_normality.run_kpss_test (confirmatory)

### Alternatives

| instead use | when |
| --- | --- |
| #25 ARDL | The relation is SYMMETRIC (a linear ARDL/UECM + bounds suffices). |
| #26 dynamac | You want stochastic counterfactual simulation + residual diagnostics. |
| #23 / #24 (Johansen/VECM) | A system / multiple cointegrating relations. |

### Output fields

- long_run: a table of long-run coefficients x_p (positive) / x_n (negative) + SE/t/p
- asym_lr / asym_sr: the Wald test of asymmetry (statistic, p_value); H0 of asym_lr: beta+ = beta- (long-run symmetry)
- ect_coef: the coefficient on the lagged DV (error correction; it must be negative)
- fstat / orders / case / k / Nobs; normality (Shapiro) & arch (Engle) htests
- nar_bounds: statistic + bounds (a data_frame level/I0/I1 10/5/1%) + decision + report (the raw pssbounds display)
- nar_stability: cusum & cusumq -> x/process/lower/upper/breach (chart-data, NOT a plot)

### Pitfalls

- Decision (bounds): F > the upper I(1) 5% bound ⇒ cointegration; F < the lower I(0) bound ⇒ none; BETWEEN ⇒ inconclusive (no conclusion).
- case: ONLY 3 (unrestricted intercept, no trend) or 5 (+trend) are supported; 1/2/4 -> a cryptic error in nardl (the gate blocks it).
- a NON-significant asym_lr ⇒ the asymmetry is NOT justified -> go back to the linear ARDL #25.
- nardl accepts EXACTLY one decomposed regressor; pssbounds k follows the documented usage k=fit.k (the nardl convention).
- CUSUM/CUSUMQ take k/n from object.sels/selresidu (NOT object.k/object.n, which stay 1/nrow(dx) when graph=FALSE — silently wrong bounds).

### References

- Shin, Yu & Greenwood-Nimmo 2014 (Festschrift in Honor of Peter Schmidt, Ch.9: Modelling Asymmetric Cointegration and Dynamic Multipliers in a NARDL Framework)
- Pesaran-Shin-Smith 2001 (JAE 16(3):289-326); Narayan 2005 (small-sample bounds critical values)
- nardl reference manual + source (nardl, pssbounds, cusum, cumsq)

## #141 — Consistent monitoring of stationarity & cointegration (Wagner-Wied): calibration-period estimation + a sequential detector (FM/D/IM-OLS)

**Module:** `consistent_monitoring_stationarity.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `cmo_stationarity` | `x` | `series_handle`, `number`, `boolean`, `enum`, `enum`, `number` | `m=0.25`, `trend=False`, `signif_level=0.05` | `light` | — |
| `cmo_cointegration` | `x`, `y` | `matrix_handle`, `series_handle`, `number`, `enum`, `boolean`, `enum`, `enum`, `number`, `raw` | `m=0.25`, `trend=False`, `signif_level=0.05` | `light` | — |

### Use when

You have an established cointegration relation (or a stationary series) and you monitor whether it BREAKS DOWN in a later period; estimation only on a break-free calibration sample [1.floor(m*N)] -> detector -> break point.

### Do not use when

A full-sample one-shot test for the existence of cointegration (#23/#25/#26); estimating beta (#27); you cannot assume a break-free calibration period.

### Prerequisites

- c01_preparation_prechecks/unit_root_normality.run_adf_test
- c01_preparation_prechecks/unit_root_normality.run_kpss_test
- c05_cointegration/johansen_restricted_vecm.wrap_ca_jo (cointegration in the calibration period, cmo_cointegration only)

### Alternatives

| instead use | when |
| --- | --- |
| cmo_stationarity | A univariate series (level/trend stationarity) rather than a relation. |
| cmo_cointegration model=FM | The default; semiparametric long-run variance correction (Phillips-Hansen). |
| cmo_cointegration model=D | D-OLS (=DOLS); leads/lags of the differenced regressors. |
| cmo_cointegration model=IM | IM-OLS; integrated-modified, robust without bandwidth tuning at the estimation point. |
| 05-cointegration/wrap_ca_jo | A full-sample TEST for the existence of cointegration (rank), not sequential monitoring. |
| 05-cointegration/creg_fmols | ESTIMATING the cointegrating vector beta, not monitoring. |

### Output fields

- statistic: the detector value (H_sm)
- critical_value: the critical value at signif_level
- detected: the DECISION — a break/deviation was detected (boolean)
- detection_time: the detection index (NA if none; the raw time=Inf is not exposed)
- statistics_path: the detector path, NA over the calibration period (chart-data)
- p_value: bounded to ∈ [0.01, 0.1] (not an exact p)
- residuals: modified-OLS residuals (cmo_cointegration only)
- calibration: the fraction (m.frac) + the index (floor(m*N))
- kernel/bandwidth/trend/model: the options that were used
- object: cointmonitoR (not a producer; a stub in to_mcp)

### Pitfalls

- m = the CALIBRATION fraction ∈ [0.1,0.9]; the last observation = floor(m*N); a bad calibration (containing a break) invalidates the procedure.
- p_value is bounded to [0.01,0.1] (0.1=far from rejection, 0.01=strong) — NOT an exact p-value.
- detected=FALSE / detection_time=NA (raw time=Inf) means no break, not an error.
- model='D'=DOLS, 'IM'=Integrated-Modified; there is NO 'DOLS'/'CCR' token.
- Silently wrong: a multi-column y / NA / nrow(x)!=length(y) -> the raw package only WARNS and returns garbage; hard-gated here.
- Fully deterministic (no RNG/bootstrap) -> reproducible without a seed; computational (no register).

### References

- Wagner & Wied 2015 (SSRN DOI:10.2139/ssrn.2624657, Monitoring Stationarity and Cointegration)
- Chu-Stinchcombe-White 1996 (Econometrica 64:1045-1065)
- Phillips-Hansen 1990 (RES 57:99-125, FM-OLS)
- Stock-Watson 1993 (Econometrica, D-OLS)
- Vogelsang-Wagner 2014 (J.Econometrics, IM-OLS)
- Andrews 1991
- Newey-West 1994
- cointmonitoR reference manual (monitorStationarity/monitorCointegration) — args/value/floor(m*N)/p∈[0.01,0.1] confirmed via the help page + live introspection
