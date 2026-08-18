<!-- SPDX-License-Identifier: AGPL-3.0-only -->
# 01-preparation-prechecks

24 METHOD-SELECTION cards, 24 modules, 76 nodes.

Every card below governs one wrapper module in this package. The cards are the
reason a method exists here at all: they record when it applies, what to reach
for instead, and the traps that make its output easy to misread.

## #1 — Unit-root & normality prechecks (ADF/KPSS/PP/Jarque-Bera)

**Module:** `unit_root_normality.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `run_adf_test` | `x` | `series_handle`, `enum`, `integer`, `number` | `alpha=0.05` | `light` | — |
| `run_kpss_test` | `x` | `series_handle`, `enum`, `boolean`, `number` | `lshort=True`, `alpha=0.05` | `light` | — |
| `run_pp_test` | `x` | `series_handle`, `enum`, `enum`, `boolean`, `number` | `lshort=True`, `alpha=0.05` | `light` | — |
| `run_jarque_bera_test` | `x` | `series_handle`, `number` | `alpha=0.05` | `light` | — |

### Use when

a fast standardised first look at the stationarity of a univariate series + residual normality; ready-made p-values

### Do not use when

you need the test regression/DF-GLS/break-aware (-> #2 urca); seasonal (-> #89); structural break; panel (-> #6)

### Alternatives

| instead use | when |
| --- | --- |
| #2 urca | DF-GLS/explicit critical values/Zivot-Andrews break-aware |
| ADF+KPSS confirmatory (same package) | established practice: opposite H0, cross-check for I(1) |
| #89 hegy_test | the non-stationarity may be seasonal |

### Output fields

- statistic: value of the statistic; p_value: ready-made p-value (the main decision)
- lag_order/truncation_lag: lag k (ADF) or truncation lag; df: 2 (JB)
- decision: pre-computed interpretation at alpha
- warnings: 'p-value smaller/greater than printed' -> p-value clamped (0.01/0.10), not exact

### Pitfalls

- KPSS polarity: H0=stationarity -> rejection=NON-stationarity (the opposite of ADF/PP)
- non-rejection by ADF does not prove a unit root (low power) -> confirmatory KPSS
- the p-value is clamped when the statistic falls outside the critical-value table
- class tseries_wrapper (not htest) -> to_mcp recurses into atomic fields

### References

- Said & Dickey 1984 (Biometrika 71:599); Dickey & Fuller 1979 (JASA 74:427)
- Kwiatkowski Phillips Schmidt Shin 1992 (J.Econometrics 54:159)
- Phillips & Perron 1988 (Biometrika 75:335); Jarque & Bera 1987
- Enders 2015 Applied Econometric Time Series 4th ed. ch.4

## #2 — Unit-root suite (ADF/KPSS/PP/ERS-DFGLS/Zivot-Andrews)

**Module:** `unit_root_suite.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `wrap_ur_df` | `y` | `series_handle`, `enum`, `integer`, `enum` | `lags=1` | `light` | — |
| `wrap_ur_kpss` | `y` | `series_handle`, `enum`, `enum` | — | `light` | — |
| `wrap_ur_pp` | `x` | `series_handle`, `enum`, `enum`, `enum` | — | `light` | — |
| `wrap_ur_ers` | `y` | `series_handle`, `enum`, `enum`, `integer` | `lag_max=4` | `light` | — |
| `wrap_ur_za` | `y` | `series_handle`, `enum`, `integer` | — | `light` | — |

### Use when

heavy unit-root work with an explicit choice of deterministic model, DF-GLS (greater power), or Zivot-Andrews (ONE endogenous break)

### Do not use when

a fast yes/no with a p-value (-> #1); seasonal (-> #89); MULTIPLE breaks (-> #3); panel (-> #6)

### Alternatives

| instead use | when |
| --- | --- |
| #1 tseries | a fast ready-made p-value without the test regression |
| ur.ers (DF-GLS) | power is critical, series close to unity |
| ur.za | ONE break at an unknown date (bpoint = the estimate) |
| #3 strucchange | multiple breaks |

### Output fields

- teststat: numeric; cval: matrix of critical values 1/5/10% (-> nested rows+dim+dimnames)
- model/type/lag: deterministic spec & lags (documents the decision)
- bpoint (ur.za): estimated break position; tstats: rolling t-stat profile; yd (ur.ers): GLS-detrended
- testreg/model/res: heavy lm/text -> stubbed by to_mcp

### Pitfalls

- NO p-value: compare teststat with cval by hand
- tail polarity: ADF/PP/ERS/ZA reject when teststat < cval (left tail); KPSS when teststat > cval (right tail)
- urca objects are S4 slots (not htest); ur.za handles ONE break ONLY

### References

- Elliott Rothenberg Stock 1996 (Econometrica 64(4):813, DF-GLS; cval MacKinnon 1991)
- Zivot & Andrews 1992 (JBES 10(3):251)
- KPSS 1992; Phillips & Perron 1988; Enders 2015 ch.4

## #3 — Structural change (Bai-Perron multiple breaks / Chow-F / CUSUM)

**Module:** `structural_change.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `run_breakpoints` | `formula` | `formula`, `df_handle`, `number`, `integer`, `number`, `integer` | `h=0.15`, `ci_level=0.95` | `light` | — |
| `run_Fstats` | `formula` | `formula`, `df_handle`, `number` | `from=0.15` | `light` | `fstats_object` |
| `run_efp` | `formula` | `formula`, `df_handle`, `enum`, `number`, `boolean` | `h=0.15`, `dynamic=False` | `light` | `efp_object` |
| `run_sctest` | `x` | `raw_handle`, `enum`, `boolean` | `asymptotic=False` | `light` | — |

### Use when

testing & estimating the structural stability of a relationship; CUSUM (dating-free), sup-F (one break), Bai-Perron (multiple breaks + dates)

### Do not use when

only a unit-root yes/no (-> #1/#2); ONE break inside the unit-root framework (-> #2 ur.za); probabilistic regimes (Markov 10, MSwM gaussian/lm only); seasonality

### Alternatives

| instead use | when |
| --- | --- |
| #2 ur.za | the break is tied to a unit-root question (one, endogenous) |
| Markov-switching (10) | smooth/probabilistic regime changes; MSwM gaussian/lm only |
| CUSUM (run_efp) vs Bai-Perron | CUSUM=screening without dating; Bai-Perron=how many & where, with dates |

### Output fields

- breakpoints_minBIC: break index(es); breakdates: dates; confint: matrix lower/breakpoint/upper; confint_dates
- process (run_efp): ts/mts fluctuation process (chart-ready); type; par (bandwidth, meaningless for CUSUM)
- run_sctest: atomic statistic/p_value/method/data_name (htest) = the main decision
- breakpoints_full: heavy breakpointsfull -> stubbed

### Pitfalls

- run_efp.par is NOT a decision; the decision is the p-value of sctest
- run_sctest takes RAW Fstats/efp objects (not wrapper lists) — gate inherits
- min-BIC may select 0 breaks (breakpoints_minBIC=NA): no structural change, not an error

### References

- Bai & Perron 1998 (Econometrica 66:47) & 2003 (J.Applied Econometrics 18:1)
- Chow 1960 (Econometrica 28:591); Brown Durbin Evans 1975 (JRSS-B 37:149, CUSUM)
- Andrews 1993 (Econometrica 61:821, sup-F)

## #4 — Seasonal adjustment with X-13ARIMA-SEATS

**Module:** `seasonal_adjustment_13arima.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `run_seas` | `x` | `series_handle`, `exog_handle`, `boolean` | `out=False` | `light` | `seas_object` |
| `get_series` | `seas_object`, `series` | `raw_handle`, `string`, `boolean`, `boolean` | `reeval=True`, `verbose=True` | `light` | — |
| `check_x13` | — | `boolean`, `boolean`, `boolean` | `fail=False`, `fullcheck=True`, `htmlcheck=True` | `light` | — |

### Use when

seasonally adjusting a monthly/quarterly series + isolating trend/seasonal/irregular via regARIMA+SEATS/X-11

### Do not use when

TESTING a seasonal unit root (not adjustment -> #89); non-seasonal; no X-13 binaries (STL/10); structural breaks (-> #3)

### Prerequisites

- check_x13 (X-13 binaries installed/working before seas)

### Alternatives

| instead use | when |
| --- | --- |
| #89 hegy_test/ch_test | TESTING seasonal non-stationarity/stability (inference, not adjustment) |
| X-11 mode (x11='') | non-model-based decomposition, more robust than SEATS |
| trend/cycle filters (10) | trend extraction only (HP/Hamilton) without a seasonal model |

### Output fields

- final: seasonally adjusted series (the main output, ts); original/trend/seasonal/irregular: components
- seas_table: 'seats.seasonal'(s10) or 'x11.seasonal'(d10); NULL if no known spec
- qs: QS seasonality test (post-check, small p = seasonality remains); udg: diagnostics
- err/model/fivebestmdl: X-13 warnings, selected ARIMA, top-5

### Pitfalls

- there is no seasonal extractor — the spec is auto-detected; seasonal=NULL if seats=NULL
- final = original/(seasonal*trading-days); use get_series(obj,'seats.adjustfac') for the ratio
- final (adjusted) != trend (it has also removed the irregular)

### References

- U.S. Census Bureau X-13ARIMA-SEATS Reference Manual
- QS test: Maravall/Census diagnostics

## #5 — Automatic outlier detection (Chen-Liu)

**Module:** `automatic_outlier_detection.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `run_tso` | `y` | `series_handle`, `exog_handle`, `number`, `number`, `integer`, `enum` | `delta=0.7`, `maxit=1` | `light` | — |

### Use when

automatic detection & classification of outliers (AO/LS/TC/IO/SLS) in a univariate ts before modelling; a level shift mimics a unit root

### Do not use when

a break in a regression relationship (-> #3); ONE unit-root break (-> #2 ur.za); outliers inside seasonal adjustment (-> #4); non-ts

### Alternatives

| instead use | when |
| --- | --- |
| #3 strucchange | structural change in a relationship, not isolated anomalies |
| #4 seasonal (outlier spec) | outlier detection as part of seasonal adjustment |
| tsmethod='arima' | known ARIMA order, speed/stability |

### Output fields

- outliers (data_frame): type/ind/time/coefhat/tstat (-> records) = the main result
- yadj: series cleaned of outliers (ts); fit: final ARIMA; effects: contribution of the outliers
- tsoutliers_object: the whole object (the docs do not enumerate named elements)

### Pitfalls

- LS (level shift) != AO: a permanent level shift -> a possible structural break/pseudo unit root
- before concluding I(1), check whether a single LS explains the non-stationarity
- cval defaults from n (n<=50->3.0, n>=450->4.0); a larger n = a stricter threshold
- exog_handle: EXPLICIT requirement of a matrix + colnames + tsp(exog_handle)==tsp(y) (gate stop)

### References

- Chen & Liu 1993 (JASA 88(421):284)

## #6 — Panel unit-root (LLC/IPS/Fisher/Hadri + Pesaran CIPS)

**Module:** `panel_unit_root.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `run_purtest` | `object` | `df_handle`, `enum`, `enum`, `enum`, `integer` | `pmax=10` | `light` | — |
| `run_cipstest` | `x` | `raw_handle`, `integer`, `enum`, `enum`, `boolean` | `lags=2`, `truncated=False` | `light` | — |
| `make_pdata_frame` | `x` | `df_handle`, `series_codes`, `boolean` | `drop_index=False` | `light` | — |

### Use when

stationarity in a macro panel (i×t, large T); LLC/IPS/Fisher/Hadri (purtest) or CIPS (2nd generation, robust to cross-section dependence)

### Do not use when

univariate (-> #1/#2); ESTIMATING a panel equation FE/RE/GMM (-> category 08, same package, different file); panel cointegration; short-T micro panel

### Prerequisites

- make_pdata_frame (panel structure before cipstest: pseries gate)
- run_cipstest (model=cmg if cross-sectional dependence is present)

### Alternatives

| instead use | when |
| --- | --- |
| cipstest (CIPS) vs purtest (LLC/IPS) | CIPS under cross-sectional dependence; LLC/IPS when the units are independent |
| ips vs levinlin | IPS heterogeneous root per unit; LLC a common root (more powerful if it holds) |
| hadri | confirmatory (H0 stationarity), as KPSS is against ADF |

### Output fields

- run_purtest.statistic: htest -> to_mcp atomic {statistic,p_value,parameter,method,data.name,alternative}
- args/idres: arguments + per-individual ADF regressions (records); adjval/sigma2 only for levinlin/ips
- ips_tbar_crit: critical values only for ips.stat=tbar (lags=0)
- run_cipstest.cipstest: the whole htest

### Pitfalls

- polarity: LLC/IPS/Fisher/CIPS have H0=unit root; BUT hadri has H0=stationarity (the opposite, like KPSS)
- IPS non-rejection != all units I(1); it rejects if SOME units are stationary (heterogeneous alternative)
- gate: ips.stat='tbar' does not apply when lags>0 (stop); tbar/hadri/levinlin not available for unbalanced panels
- 1st-generation purtest is size-distorted under cross-section dependence -> CIPS

### References

- Levin Lin Chu 2002 (J.Econometrics 108:1); Im Pesaran Shin 2003 (115:53)
- Maddala & Wu 1999 (Oxford Bull.Econ.Stat. 61:631); Choi 2001 (JIMF 20:249)
- Hadri 2000 (Econometrics J. 3:148); Pesaran 2007 (J.Applied Econometrics 22:265, CIPS)

## #89 — Seasonal unit roots & seasonal stability (HEGY / Canova-Hansen)

**Module:** `seasonal_unit_roots.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `run_hegy_test` | `x` | `series_handle`, `enum`, `integer`, `enum`, `boolean`, `integer`, `integer` | `maxlag=0`, `bootstrap=False`, `boot_nb=1000`, `seed=123` | `heavy` | — |
| `run_ch_test` | `x` | `series_handle`, `enum`, `boolean`, `enum` | `lag1=False` | `light` | — |

### Use when

seasonal series (freq>1): stochastic/non-stationary seasonality (HEGY, H0 seasonal unit root) vs stable seasonality (Canova-Hansen, H0 stability)

### Do not use when

non-seasonal or level unit root only (-> #1/#2); REMOVING seasonality/adjustment (-> #4); panel (-> #6)

### Alternatives

| instead use | when |
| --- | --- |
| run_hegy_test + run_ch_test confirmatory | opposite H0, as ADF+KPSS in the non-seasonal case |
| #4 seasonal (X-13) | the final objective is the adjusted series |
| ADF on a seasonally-differenced series | rough; HEGY however identifies AT WHICH frequency the root sits |

### Output fields

- statistics: named numeric per root/frequency (t_1,t_2,F_3:4); pvalues; statistic_names
- pvalue.method: RS(default)/raw/bootstrap (CPU, deterministic through the seed)
- lag.method/lag.order/strdet/deterministic: regression spec
- test.object/fitted.model: stubbed by to_mcp

### Pitfalls

- polarity: HEGY H0=unit root (small p=NO root); Canova-Hansen H0=stability (small p=changing) — OPPOSITE
- HEGY = MANY verdicts (one per frequency); not one; a root may sit at a seasonal harmonic but not at zero frequency
- deterministic=c(0,0,0) is forbidden (it breaks the package); bootstrap+AICc is forbidden
- pvalue='bootstrap' of hegy_test was removed together with CUDA -> CPU hegy.boot.pval via bootstrap=TRUE

### References

- Hylleberg Engle Granger Yoo 1990 (J.Econometrics 44(1):215, HEGY)
- Beaulieu & Miron 1993 (J.Econometrics 55:305); Smith Taylor del Barrio Castro 2009 (Econometric Theory 25:527)
- Canova & Hansen 1995 (JBES 13(3):237); Burridge & Taylor 2004 (J.Econometrics 123:67, bootstrap)
- Diaz-Emparanza 2014 (CSDA 76:237, response-surface p-values)

## #122 — Bootstrap unit-root tests robust to heterogeneity/non-stationary volatility/missing data (boot ADF / union / panel GM / order of integration)

**Module:** `bootstrap_unit_root.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `bur_boot_adf` | `data`, `seed` | `series_handle`, `integer`, `enum`, `integer`, `enum`, `enum`, `integer`, `integer`, `enum`, `boolean`, `number` | `B=1999`, `min_lag=0`, `criterion_scale=True`, `alpha=0.05` | `heavy` | — |
| `bur_boot_union` | `data`, `seed` | `series_handle`, `integer`, `enum`, `integer`, `integer`, `integer`, `enum`, `boolean`, `number`, `number` | `B=1999`, `min_lag=0`, `criterion_scale=True`, `union_quantile=0.05`, `alpha=0.05` | `heavy` | — |
| `bur_boot_panel` | `data`, `seed` | `multiseries_handle`, `integer`, `enum`, `integer`, `boolean`, `number`, `enum`, `enum`, `integer`, `integer`, `enum`, `boolean`, `number` | `B=1999`, `union=True`, `union_quantile=0.05`, `min_lag=0`, `criterion_scale=True`, `alpha=0.05` | `heavy` | — |
| `bur_order_integration` | `data`, `seed` | `multiseries_handle`, `integer`, `enum`, `integer`, `number`, `enum`, `integer`, `integer`, `integer`, `enum` | `max_order=2`, `level=0.05`, `B=1999`, `min_lag=0` | `heavy` | `diff_data` |

### Use when

unit root/stationarity when the asymptotic critical values do not apply (heteroskedasticity/nonstationary volatility); a residual bootstrap instead of fixed tables; single series (boot_adf/boot_union), panel GM (boot_panel, H0=all have a UR), or the order of integration + stationarisation (order_integration -> diff_data feeder)

### Do not use when

fixed critical-value tables suffice -> urca #2 / tseries #1; KPSS (H0=stationarity); seasonal roots -> uroot HEGY #89; a fixed-N panel -> plm purtest/cips #6; charts (frontend); the raw joint/FDR boot_ur/boot_sqt/boot_fdr as direct nodes (only via order_integration method=)

### Prerequisites

- bur_boot_adf
- bur_boot_union

### Alternatives

| instead use | when |
| --- | --- |
| bur_boot_union (the univariate default) | robust to the arbitrary choice of deterministics/detrending (a union of 4 specs) |
| bur_boot_adf with detrend=QD | an a-priori specification; QD ⇒ DF-GLS, more powerful near unity |
| bootstrap=AWB (default) | general/robust; MBB/SB do NOT handle unbalanced/NA data; SB/SWB are not for panels |
| urca #2 / tseries #1 | the asymptotic critical values do apply — faster, no bootstrap |

### Output fields

- statistic/p_value/estimate(gamma; NA for union)/stationary/decision/selected_lag(s)/alpha/seed
- boot_panel: statistic(Group-Mean)/some_stationary + individual_statistics/pvalues/estimates/selected_lags (N×specs matrices) + series_names
- order_integration: order_int (named I(d) per series) + classification + diff_data (the stationarised TxN matrix — a PRODUCER, register->Parquet)

### Pitfalls

- POLARITY: H0=unit root ⇒ p<alpha ⇒ STATIONARY (the OPPOSITE of KPSS, where rejection ⇒ non-stationary)
- the panel H0 is that ALL series have a UR; rejection ⇒ SOME are stationary (NOT all) — run a per-series follow-up
- a union estimate=NA by definition (there is no single gamma across the 4 combinations) — NOT an error
- NA: a silent trim of leading/trailing values + an internal error -> a hard 'no NA' gate (run imputeTS #80 first)
- the seed is MANDATORY (a stochastic bootstrap); do_parallel=FALSE for determinism/caching

### References

- Smeekes & Wilms 2023, bootUR: An the reference Package for Bootstrap Unit Root Tests, JSS 106(12):1-39 (doi:10.18637/jss.v106.i12)
- Palm, Smeekes & Urbain 2011, J. Econometrics 163(1):85-104 (panel GM test)
- Ng & Perron 2001, Econometrica 69(6):1519-1554 (MAIC lag selection)
- Smeekes & Wijler 2020, Unit roots and cointegration (order of integration)

## #123 — Covariate-Augmented Dickey-Fuller (CADF) unit-root test — power gain from stationary covariates (Hansen 1995); a plain ADF when X=NULL

**Module:** `covariate_augmented_dickey.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `run_cadf` | `y` | `series_handle`, `multiseries_handle`, `enum`, `integer`, `integer`, `integer`, `enum`, `number` | `max_lag_y=1`, `min_lag_X=0`, `max_lag_X=0`, `alpha=0.05` | `light` | — |

### Use when

a unit root in a univariate series when stationary, correlated covariates are available (CADF is more powerful than ADF); or a plain ADF with full p-values + automatic lag selection when X=NULL

### Do not use when

no genuinely stationary covariate -> a plain ADF/PP #1 or urca #2; H0 stationarity (the reverse polarity) -> KPSS; a seasonal unit root -> uroot #89; a structural break -> ur.za; a non-stationary X invalidates the theory

### Prerequisites

- c01_preparation_prechecks/unit_root_normality.run_adf_test
- c01_preparation_prechecks/unit_root_normality.run_kpss_test

### Alternatives

| instead use | when |
| --- | --- |
| #2 urca (ur.df/ur.ers) | you want the classic critical-value tables without covariates |
| #1 tseries (adf_test/pp_test) | fast univariate screening without covariates |
| criterion=AIC/BIC | automatic lag selection within [min,max]; the default none = a fixed max.lag.y |

### Output fields

- method (ADF\|CADF)
- statistic (+statistic_label)
- p_value (Costantini-Lupi-Popp)
- rho2 (nuisance, CADF only, NULL for ADF)
- estimate
- null_value
- alternative=less
- max_lag_y/min_lag_X/max_lag_X (as selected)
- info_criteria {AIC,BIC,HQC,MAIC}
- decision
- warnings

### Pitfalls

- POLARITY: H0=unit root, rejection (p<alpha) => STATIONARITY (the OPPOSITE of KPSS)
- silently wrong (gated): a silent NA drop in y; silent acceptance of NA/misaligned X; a cryptic subscript-out-of-bounds on a constant y or min.lag.X>max.lag.X or excessive lags
- the «Specified sample size may be too small» notice is printed to stdout (it is NOT an the reference warning) -> it is exposed in warnings; the p-value is less reliable at small n
- min.lag.X<0 means leads of the covariates (a documented feature, not an error)
- the covariates X MUST be stationary; a non-stationary X invalidates the asymptotic theory (the package does not check it)

### References

- Hansen BE (1995) Rethinking the Univariate Approach to Unit Root Testing, Econometric Theory 11(5):1148-1171
- Costantini, Lupi, Popp (2007) A Panel-CADF Test for Unit Roots (asymptotic p-values)
- Lupi C (2009) Unit Root CADF Testing with the reference, JSS 32(2), http://www.jstatsoft.org/v32/i02

## #124 — General-to-Specific (GETS) model selection + Indicator Saturation (IIS/SIS/TIS) for outliers & structural breaks

**Module:** `general_specific_selection.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `gts_arx` | `y` | `series_handle`, `boolean`, `int_array`, `exog_handle`, `enum` | `mc=True` | `light` | `model` |
| `gts_getsm` | `object` | `raw_handle`, `number`, `number`, `enum`, `enum` | `t_pval=0.05` | `light` | — |
| `gts_isat` | `y` | `series_handle`, `boolean`, `int_array`, `exog_handle`, `boolean`, `boolean`, `boolean`, `number`, `enum` | `mc=True`, `iis=False`, `sis=True`, `tis=False`, `t_pval=0.001` | `light` | `model` |

### Use when

set up the GUM (gts_arx: intercept+AR lags+regressors) -> a parsimonious final model (gts_getsm, multi-path GETS+PET) or automatic detection of outliers/mean shifts/trend shifts (gts_isat, IIS/SIS/TIS); deterministic (no seed)

### Do not use when

testing for a break at a single point with sup-F/CUSUM -> strucchange #3; ARIMA-intervention outliers -> tsoutliers; log-variance GETS (getsv) is omitted; charts (frontend)

### Prerequisites

- c01_preparation_prechecks/unit_root_normality.run_adf_test (stationarity of y before the GUM)

### Alternatives

| instead use | when |
| --- | --- |
| #3 strucchange (breakpoints/Fstats/efp) | a hypothesis-driven break test at a known or unknown point rather than automatic multiple saturation |
| gts_isat with a tight t.pval | an unknown number/location of breaks -> data-driven saturation with a controlled gauge (~t.pval·n false positives) |

### Output fields

- coefficients + mean_results (term/coef/std_error/t_stat/p_value) + sigma/rss/logl/r_squared + fitted/residuals + n/k/df
- gts_arx/gts_isat: model = the fitted arx/isat object (a producer, register->RDS; a to_mcp stub @mcp_serialized=FALSE)
- gts_isat: is_names (e.g. sis41), n_indicators, isat_dates.iis/.sis/.tis (breaks/date/index/coef/coef.se/coef.t/coef.p)
- gts_getsm: specific_spec (the reg.no that were kept), terminals_results, n_estimations, empty_model flag

### Pitfalls

- sisNN=a step shift at observation NN (a permanent level change); iisNN=an impulse (a single outlier); tisNN=a trend shift — do not confuse them
- gauge: a tighter t.pval ⇒ fewer false detections/lower power; the isat default is t.pval=0.001 (NOT 0.05)
- gts_getsm empty model: it may end at the empty model -> empty_model=TRUE, coefficients of length 0 (NOT a silent NULL)
- SILENTLY WRONG (gated): an mxreg with NROW>length(y) is accepted silently; t.pval>=1 is accepted silently -> hard gates

### References

- Pretis, Reade & Sucarrat (2018), JSS 86(3), doi:10.18637/jss.v086.i03
- Sucarrat (2020), 12(2):388-401; Hendry & Doornik (2014), Empirical Model Discovery and Theory Evaluation (MIT Press)

## #125 — Seasonality tests (combined/QS/Friedman/Kruskal-Wallis/seasonal-dummies/Welch/OCSB)

**Module:** `seasonality.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `run_isseasonal` | `x` | `series_handle`, `enum`, `integer`, `number`, `integer` | `alpha=0.01`, `seed=123` | `light` | — |
| `qs_test` | `x` | `series_handle`, `integer`, `boolean`, `boolean`, `boolean`, `number` | `diff=True`, `residuals=False`, `autoarima=True`, `alpha=0.05` | `light` | — |
| `fried_test` | `x` | `series_handle`, `integer`, `boolean`, `boolean`, `boolean`, `number` | `diff=True`, `residuals=False`, `autoarima=True`, `alpha=0.05` | `light` | — |
| `kw_test` | `x` | `series_handle`, `integer`, `boolean`, `boolean`, `boolean`, `number` | `diff=True`, `residuals=False`, `autoarima=True`, `alpha=0.05` | `light` | — |
| `seasdum_test` | `x` | `series_handle`, `integer`, `boolean`, `number` | `autoarima=False`, `alpha=0.05` | `light` | — |
| `welch_test` | `x` | `series_handle`, `integer`, `boolean`, `boolean`, `boolean`, `boolean`, `number` | `diff=True`, `residuals=False`, `autoarima=True`, `rank=False`, `alpha=0.05` | `light` | — |
| `ocsb_test` | `x`, `seed` | `series_handle`, `integer`, `enum`, `int_array`, `integer`, `integer`, `number` | `augmentations=[3, 0]`, `nrun=1000`, `alpha=0.05` | `light` | — |

### Use when

the prechecks stage after stationarity (#1/#2), before seasonal adjustment (#3); the structural decision whether a monthly/quarterly/weekly series is seasonal; run_isseasonal=a boolean gate (WO); ocsb=a seasonal unit root (nsdiffs)

### Do not use when

non-seasonal stationarity -> tseries/urca (#1/#2); deseasonalization -> seasonal/X-13 (#3, seastests only DETECTS); frequency=1 (hard gate); charts (frontend)

### Alternatives

| instead use | when |
| --- | --- |
| #3 seas (X-13) | the objective is deseasonalization rather than detection |
| ocsb_test | a suspected seasonal UNIT ROOT (stochastic) rather than deterministic seasonality |
| combined (run_isseasonal) | a fast default boolean decision (the WO combination rule) |

### Output fields

- test/null_hypothesis/statistic/p_value/alpha/is_seasonal/decision/freq/n_obs (+ echoed args)
- run_isseasonal(combined): statistic=NA, p_values = the 3 named WO p-values (QS/QS-the reference/KW-the reference)
- ocsb: + method/augmentations/nrun/seed; the null is a seasonal unit root

### Pitfalls

- POLARITY: combined/qs/fried/kw/seasdum/welch have H0=no seasonality (a small p => seasonal); ocsb has H0=A SEASONAL UNIT ROOT, REVERSED (fail to reject, p>=alpha => seasonal, the nsdiffs convention) -> which is why null_hypothesis is always returned
- combined: .stat is a LOGICAL decision (QS p<0.01 OR KW p<0.002), NOT a statistic; alpha does not affect it
- NA: SILENTLY WRONG — seastests silently accepts NA and returns an incorrect decision -> hard gate
- isSeasonal does NOT support test='ocsb' (object 'seasonal' not found); run_isseasonal routes ocsb directly
- a pure deterministic sine is NOT detected by combined (it is residual-based); welch fails on a plain numeric ('intra' not found) -> normalise to a ts

### References

- Webel & Ollech (2019), An overall seasonality test, Deutsche Bundesbank Discussion Paper
- Osborn, Chui, Smith & Birchenhall (1988), Seasonality and the order of integration for consumption, Oxford Bull. Econ. Stat. 50(4):361-377 (OCSB)

## #126 — Time-series decomposition (STL / classical) + feature extraction (STL strength / ACF / spectral entropy)

**Module:** `time_series_decomposition.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `fst_stl` | `series` | `series_handle`, `raw`, `integer` | — | `light` | `decomp` |
| `fst_classical` | `series` | `series_handle`, `enum` | — | `light` | `decomp` |
| `fst_features` | `series` | `series_handle` | — | `light` | — |

### Use when

a preparatory check of the structure of a seasonal series — isolating trend/seasonal/remainder (STL preferred, robust; classical as a baseline) or summarising into numeric features (trend/seasonal strength, ACF, spectral entropy) for screening/comparing series; a ts input -> tsibble internally

### Do not use when

a non-seasonal series (frequency==1) -> the HP/BK/CF trend filters, cat.10 (gated); forecasting/ARIMA/ETS -> cat.02 fable; charts (frontend); Box-Cox/guerrero -> transforms; multiple seasonal periods (a univariate ts has one frequency)

### Prerequisites

- fst_stl
- fst_classical

### Alternatives

| instead use | when |
| --- | --- |
| fst_stl vs fst_classical | STL is robust/loess (default; s_window periodic or an odd number >=7); classical is only a baseline (fixed seasonality, NA at the edges) |
| #4 seasonal (X-13/SEATS) | you need the official X-13-ARIMA-SEATS seasonal adjustment rather than loess/MA |
| trend filters cat.10 (HP/Baxter-King/Christiano-Fitzgerald) | a non-seasonal trend/cycle rather than a seasonal decomposition |
| #81 descriptives (ACF/PACF) | you want the raw ACF/PACF rather than unified comparable feature metrics |

### Output fields

- components: data_frame {index, observed, trend, seasonal, remainder, season_adjust} (canonical, parquet-able)
- strength (fst_stl): {trend, seasonal} in [0,1]
- decomp (fst_stl/fst_classical): mable mdl_df [PRODUCER -> RDS bucket]
- features (fst_features): a named numeric list (one row) + feature_names + n_features

### Pitfalls

- STL on frequency==1 SILENTLY drops the seasonal component -> a frequency>1 gate (do not read it as 'no seasonality')
- STL/classical with NA -> <NULL model> -> the cryptic 'no applicable method for components applied to null_mdl' -> an anyNA gate + an is_null_model post-gate
- classical multiplicative on non-positive values -> a silently inconsistent decomposition -> a >0 gate
- the column naming differs (STL season_year/remainder vs classical seasonal/random) -> unified to seasonal/remainder
- classical trend: NA at the ~frequency/2 edges because of the centred MA (expected, not an error)
- a trend/seasonal strength ~1 => a strong component, ~0 => negligible

### References

- Cleveland, Cleveland, McRae & Terpenning 1990, STL: A Seasonal-Trend Decomposition Procedure Based on Loess, J. Official Statistics 6:3-73
- Hyndman & Athanasopoulos, Forecasting: Principles and Practice 3e, ch.3 (decomposition & feature strengths), https://otexts.com/fpp3

## #127 — Data-driven locally-weighted regression decomposition of seasonality/trend (IPI optimal bandwidth) under short memory

**Module:** `driven_locally_weighted.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `des_deseats` | `y` | `series_handle`, `enum`, `enum`, `enum`, `boolean` | `order_poly=3`, `kernel_fun='epanechnikov'`, `inflation_rate='optimal'`, `autocor=True` | `light` | `model` |

### Use when

an equidistant seasonal ts (frequency>1); a non-parametric decomposition into trend + (slowly varying) seasonality + remainder with a DETERMINISTICALLY selected bandwidth (IPI/AMISE); it also returns detrended + seasonally-adjusted series

### Do not use when

frequency<=1 (non-seasonal -> a trend filter); the official model-based seasonal adjustment -> seasonal X-13 #4; STL with explicit windows/robustness -> feasts #126; charts (frontend)

### Prerequisites

- c01_preparation_prechecks/seasonality.run_isseasonal (seasonality is present)

### Alternatives

| instead use | when |
| --- | --- |
| 01-preparation-prechecks/fst_stl | you want STL (loess) with explicit trend/seasonal windows or robustness to outliers rather than a data-driven optimal bandwidth |
| 01-preparation-prechecks/Seasonal-run_seas | you need the official model-based X-13ARIMA-SEATS adjustment (RegARIMA+SEATS) rather than non-parametric locally-weighted regression |

### Output fields

- trend/seasonal/remainder/observations: ts (from fit@decomp mts: Trend/Seasonality/Rest/Observations)
- detrended = observations - trend; adjusted = seasonally adjusted = observations - seasonality
- bwidth: the relative [0,1] data-driven IPI bandwidth (NOT a number of observations); sum_autocov: the estimated sum of autocovariances
- model: the S4 'deseats' fitted object (a producer -> RDS pointer)

### Pitfalls

- deseats accepts a matrix/mts SILENTLY (silently wrong) — the wrapper blocks it as multivariate
- bwidth is a RELATIVE bandwidth, not a number of observations
- NA -> the cryptic «Convergence of the bandwidth selection algorithm failed» (gated); the seasonality is assumed to vary SLOWLY

### References

- Feng, Gries & Fritz (2020), Data-driven local polynomial for the trend and its derivatives, J. Nonparametric Statistics 32(2):510-533
- Feng (2013), J. Applied Statistics 40(2):266-281; Bühlmann (1996), J. Time Series Analysis 17(3):247-270

## #128 — Detection of structural breaks in the trend & seasonality of seasonal time series (BFAST: iterative STL + breakpoints) + near-real-time disturbance monitoring

**Module:** `detection_structural_breaks.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `bf_bfast` | `Yt` | `series_handle`, `number`, `enum`, `integer`, `raw`, `num_array`, `enum` | `h=0.15`, `max_iter=10`, `level=0.05` | `light` | `model` |
| `bf_monitor` | `data`, `start` | `series_handle`, `num_array`, `enum`, `integer`, `number`, `num_array` | `order=3`, `h=0.25`, `level=[0.05, 0.05]` | `light` | — |

### Use when

a seasonal ts (frequency>1); locating WHEN the trend and/or the seasonality changed structurally (retrospective multiple breaks + dates, bf_bfast) or near-real-time detection of a new disturbance at the end (bf_monitor); separating trend/season before forecasting/regime work

### Do not use when

non-seasonal series (frequency=1); only a unit-root yes/no -> tseries #1 / urca #2; one break in the unit-root framework -> urca ur.za #2; probabilistic regimes (Markov switching); charts (frontend); NA without an explicit decomp='stlplus' (a gated silent fallback)

### Prerequisites

- c00_data_utilities/time_series_class.ts_fill_regular (a regular ts before bfast)
- c00_data_utilities/time_series_class.ts_convert (to ts, frequency>1)
- c00_data_utilities/replacement_missing_values.imputets_kalman (fill NA; otherwise decomp='stlplus')

### Alternatives

| instead use | when |
| --- | --- |
| 01-preparation-prechecks/strucchange-run_breakpoints | Bai-Perron dating of ONE relationship/trend (a regression) only, without a seasonal decomposition & seasonal breaks |
| 01-preparation-prechecks/des_deseats | a smooth (data-driven bandwidth) trend+seasonal decomposition WITHOUT break detection |
| bf_monitor | online detection of a new disturbance at the END, not a full retrospective break history |

### Output fields

- trend_breaks/seasonal_breaks: {n, indices, dates (decimal time), confint(lower/break/upper_date)}
- magnitude/time_of_change: the largest change & its timing, for the TREND ONLY (Vt)
- trend_component/seasonal_component/remainder_component: ts chart-data (the last iteration)
- model: the full 'bfast' fit (a producer -> register field='model', rds bucket; a stub in to_mcp)
- bf_monitor: breakpoint (a date or NA), disturbance (logical), magnitude=median(data-prediction), history_period/monitor_period

### Pitfalls

- breakpoints are index numbers of na.omit(as_numeric(component)), NOT raw positions — the node already returns them as dates
- no break: fit.nobp$Vt/Wt==TRUE -> bp.Vt/bp.Wt is an atomic NA (not a breakpoints object) -> n=0, empty fields
- magnitude/time_of_change concern the TREND ONLY, not the seasonality
- NA + decomp='stl' -> a silent fallback to stlplus (gated: set decomp='stlplus' explicitly)

### References

- Verbesselt et al. (2010) Detecting trend and seasonal changes, Remote Sensing of Environment 114(1):106-115
- Verbesselt et al. (2010) Phenological change detection, RSE 114(12):2970-2980
- Verbesselt, Zeileis, Herold (2012) Near real-time disturbance detection, RSE 123:98-108

## #129 — Regularisation/decomposition & analysis of space-time series (turning points + Kendall info; a full descriptive table including normality; diff/LOESS trend-seasonal decomposition)

**Module:** `regularisation_decomposition_space.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `ps_turnpoints` | `x` | `series_handle`, `boolean` | `calc_proba=True` | `light` | — |
| `ps_stat_desc` | `x` | `series_handle`, `boolean`, `boolean`, `boolean`, `number` | `basic=True`, `desc=True`, `norm=False`, `p=0.95` | `light` | — |
| `ps_decompose` | `x` | `series_handle`, `enum`, `enum`, `integer`, `integer`, `enum`, `raw`, `integer`, `integer`, `integer`, `boolean`, `boolean` | `lag=1`, `order=1`, `s_degree=0`, `t_degree=2`, `robust=False`, `trend=False` | `light` | — |

### Use when

a preparatory/diagnostic precheck BEFORE estimation: a full descriptive table (stat.desc) with normality criteria; locating peaks/pits + a randomness test (turnpoints/Kendall info); fast detrending (decdiff) or seasonal STL (decloess)

### Do not use when

charts (frontend); formal stationarity/unit root -> tseries/urca #1/#2; seasonal HEGY/CH tests -> uroot #89; multiplicative seasonal adjustment -> seasonal #4; irregular->regular resampling (regul) WAS OMITTED

### Prerequisites

- c00_data_utilities/replacement_missing_values.imputets_interpolation (fill NA before the decomposition/analysis)
- c00_data_utilities/time_series_class.ts_fill_regular (make the series a regular ts before decloess)

### Alternatives

| instead use | when |
| --- | --- |
| #81 descriptives | you want ACF/PACF/rolling/correlation rather than a static summary table per series |
| #1 tseries / #2 urca | you need a formal stationarity p-value rather than a turning-point/visual precheck |
| #4 seasonal | you want a full X-13 seasonal adjustment rather than a quick decdiff/decloess |

### Output fields

- ps_turnpoints: n_turns/n_peaks/n_pits/first_is_peak; tppos + peak_positions/pit_positions; proba/info (if calc_proba) — info=-log2(P), larger ⇒ more monotone/informative
- ps_stat_desc: stats_table records with a 'statistic' column (names preserved) + one column per variable; skew.2SE/kurt.2SE >1 ⇒ significantly ≠0; normtest.p = Shapiro-Wilk
- ps_decompose: components mts — diff: filtered/residuals; loess with trend=TRUE: trend/seasonal/residuals; trend=FALSE: deseasoned/seasonal

### Pitfalls

- stat.desc on a NON-numeric input -> silently ALL NA (hard gate: every column must be numeric)
- decdiff FILLS NA in the input silently (ends='fill') -> a single NA gate across the whole of ps_decompose
- turnpoints with <3 unique values -> a warning & a degenerate result (gate unique>=3); decloess is additive ONLY and requires frequency>1 + >=2 periods
- coef.var = std.dev/mean is unreliable when mean≈0; info is in bits (Kendall), not a p-value

### References

- Kendall 1976, Time-series 2nd ed., Griffin (turning-points test)
- Ibanez 1982, J. Exp. Mar. Biol. Ecol. 4:619-632 (turning-points information)
- Cleveland et al. 1990, STL: Seasonal-Trend decomposition based on Loess, J. Official Stat. 6:3-73

## #130 — Robust descriptives + correlation prechecks (describe / rcorr Pearson-Spearman + p-values / weighted mean-var-quantile)

**Module:** `robust_descriptives_correlation.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `hm_describe` | `data` | `df_handle`, `integer` | `digits=4` | `light` | — |
| `hm_rcorr` | `data` | `df_handle`, `enum` | — | `light` | — |
| `hm_wtd` | `x`, `weights` | `series_handle`, `num_array`, `num_array`, `enum`, `boolean` | `normwt=False` | `light` | — |

### Use when

the preparatory layer BEFORE modelling; robust per-variable stats (pMedian/Gmd/distinct/missing/quantiles), a correlation matrix WITH p-values + pairwise n, weighted statistics with survey/frequency weights

### Do not use when

charts (frontend); formal stationarity -> tseries/urca cat.01; causality/lead-lag -> CCF #81 / Granger; class-agnostic transformations -> tsbox #78

### Alternatives

| instead use | when |
| --- | --- |
| 00-data-utilities/desc_correlations | a correlation matrix WITHOUT p-values/significance; use hm_rcorr when you need asymptotic p-values + pairwise n |
| hm_rcorr (type=spearman) | rank-based, robust to outliers/non-linearity vs pearson (linear) |
| hm_wtd | observations with weights (survey/frequency) vs the unweighted hm_describe |
| hm_wtd (var_method=ML) | the MLE Gaussian variance vs the unbiased/Bessel one (default) |

### Output fields

- hm_describe.stats: a named list per variable -> named numeric (n/missing/distinct/Info/Mean/pMedian/Gmd + quantiles.05.-.95); rounded to digits (default 4)
- hm_rcorr.r/P/n: matrices (nested rows + dimnames); the diagonal of P = NA; pairwise deletion -> n per pair
- hm_wtd.weighted_mean/weighted_var/weighted_sd/weighted_quantiles (named) + probs/var_method/normwt/n/sum_weights

### Pitfalls

- describe: quantiles ONLY for continuous variables (>10 distinct); discrete ones get no quantiles; the values are rounded to digits significant figures (raise digits for precision); pMedian=Hodges-Lehmann robust location, Gmd=Gini robust dispersion
- rcorr.P: the diagonal = NA (no self-correlation p-value); pairwise deletion -> a strong correlation with a small n is fragile (read the n matrix); spearman = Pearson on the ranks
- wtd.var defaults to unbiased (Bessel); ML = the Gaussian MLE; n=1 effective observation -> var=NaN (the warning becomes a message); weights: a length mismatch gives silent NA and negatives are accepted silently -> the gates block both

### References

- Harrell, Regression Modeling Strategies 2nd ed. (describe/pseudomedian/Gini mean difference)
- Hollander & Wolfe, Nonparametric Statistical Methods 1973 (rcorr midrank Spearman)

## #131 — Non-parametric trend & change-point tests (Mann-Kendall / Theil-Sen slope / Pettitt / Seasonal MK)

**Module:** `non_parametric_trend.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `tr_mk` | `x` | `series_handle`, `enum`, `boolean`, `number` | `continuity=True`, `alpha=0.05` | `light` | — |
| `tr_sens` | `x` | `series_handle`, `number`, `number` | `conf_level=0.95`, `alpha=0.05` | `light` | — |
| `tr_pettitt` | `x` | `series_handle`, `number` | `alpha=0.05` | `light` | — |
| `tr_smk` | `x` | `series_handle`, `integer`, `enum`, `boolean`, `number` | `continuity=True`, `alpha=0.05` | `light` | — |

### Use when

detecting a monotone trend without a distributional assumption (rank-based, robust to outliers/non-normality); tr_mk=significance, tr_sens=magnitude (a robust slope+CI), tr_pettitt=a single change point at position K, tr_smk=seasonal series with frequency>1

### Do not use when

unit root/stationarity -> tseries #1 / urca #2 (MK is not a unit-root test); multiple/parametric breakpoints -> strucchange #3; charts (frontend); strong autocorrelation (the p-value is unreliable, over-rejection)

### Alternatives

| instead use | when |
| --- | --- |
| tr_sens | you need the MAGNITUDE of the trend (slope + CI), not only the significance from tr_mk |
| tr_smk | the series is seasonal (frequency>1) — a plain tr_mk confuses seasonality with trend |
| 01-preparation-prechecks/strucchange-run_breakpoints | multiple / parametric (regression-based) breakpoints rather than one non-parametric change point (Pettitt) |
| 01-preparation-prechecks/tseries-run_kpss_test | the question is trend stationarity (I(0) around a trend), not monotone direction |

### Output fields

- tr_mk: statistic (z), p_value, S, varS, tau (∈[-1,1], the sign = the direction), decision
- tr_sens: slope (the median of the pairwise slopes per unit of time), conf_low/conf_high at conf_level, p_value/statistic from MK
- tr_pettitt: change_point_index (an integer index 1.n, NOT a date), statistic (U*), Uk (the \|U[k]\| series, chart-data)
- tr_smk: overall statistic/p_value + season_S/season_varS/season_pvalue/season_z per-season vectors (length=frequency)

### Pitfalls

- MK/Sen test MONOTONICITY, not linearity — a U shape gives a non-significant MK despite a strong non-monotone change
- on autocorrelated data the p-value is understated (a spurious trend) — prewhiten or use a block bootstrap
- the tr_sens slope is per unit of time (NOT a %); tr_pettitt change_point_index is a position index (map it to a date); the Pettitt approximate p-value is valid only for p<=0.5
- a constant series (var=0) -> p_value=NaN (silently wrong) — hard gate; NA are not allowed (complete observations only)

### References

- trend 1.1.7 reference: help pages mk_test/sens.slope/pettitt_test/smk_test (r-btw docs lookup)
- Hipel & McLeod (1994) Time Series Modelling of Water Resources and Environmental Systems; Sen (1968) JASA 63:1379-1389; Pettitt (1979) Appl. Statist. 28:126-135; Hirsch, Slack & Smith (1982) Water Resources Research 18:107-121

## #132 — (Non-)linearity tests: a battery of linearity tests (Teraesvirta/White ANN, Keenan, McLeod-Li, Tsay, LR-threshold) + an FFT surrogate-data test

**Module:** `linearity_battery_linearity.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `nlt_nonlinearity` | `x`, `seed` | `series_handle`, `integer`, `number` | `alpha=0.05` | `light` | — |
| `nlt_surrogate` | `x`, `seed` | `series_handle`, `integer`, `enum`, `number`, `boolean`, `enum`, `integer`, `integer` | `statistic='timeAsymmetry'`, `significance=0.05`, `one_sided=False`, `alternative='smaller'`, `K=1`, `tau=1` | `light` | — |

### Use when

a precheck after stationarity; linear (ARIMA/VAR) vs nonlinear/threshold models; a parametric battery or a model-free surrogate test

### Do not use when

charts/attractor/fractal work (corrDim/maxLyapunov/rqa/dfa); before stationarity is established; < 50 observations; it is not an estimation tool

### Prerequisites

- c01_preparation_prechecks/unit_root_normality.run_adf_test (stationarity first)
- c01_preparation_prechecks/unit_root_normality.run_kpss_test (stationarity first)

### Alternatives

| instead use | when |
| --- | --- |
| nlt_surrogate | a single model-free surrogate test (H0: gaussian linear) instead of a battery of parametric tests |
| nlt_nonlinearity | a parametric battery with per-test statistics/p-values + an overall verdict |

### Output fields

- nlt_nonlinearity: tests (a named list per test: statistic/p_value/reject_linearity/decision) + a summary df + p_values (named numeric, chart-data)
- nlt_nonlinearity: n_reject/reject_tests/overall_nonlinear/verdict
- nlt_surrogate: data_statistic vs surrogates_statistics (a vector, chart-data) + n_surrogates + reject_linearity/direction/decision

### Pitfalls

- McLeod-Li: a VECTOR of p-values, one per lag; the decision uses the MINIMUM (statistic=NA); it tests ARCH (heteroscedasticity), NOT a nonlinear mean
- the White/Teraesvirta ANN test is STOCHASTIC (random weights): the p-value varies without a seed -> the seed is MANDATORY in nlt_nonlinearity too
- surrogateTest does NOT return a p-value; the decision is rank-based (K smallest/largest); H0=gaussian LINEAR (rejection => nonlinearity); one.sided=FALSE ignores the alternative

### References

- Keenan 1985 (Biometrika 72:39); Tsay 1986 (Biometrika 73:461); McLeod & Li 1983; Teraesvirta/Lee-White-Granger 1993 (ANN); Schreiber & Schmitz 2000, Surrogate time series, Physica D 142(3):346-382

## #246 — MULTIVARIATE outlier detection: CLASSICAL Mahalanobis distances vs the ROBUST MCD (Deterministic MCD) at the SAME chi-square(p) cutoff + a MASKING / SWAMPING diagnostic

**Module:** `multivariate_outlier_detection.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `mv_mahalanobis` | `x` | `matrix_handle`, `number`, `num_array`, `matrix_handle` | `quantile=0.975` | `light` | — |
| `mv_covmcd` | `x` | `matrix_handle`, `number`, `number`, `boolean`, `boolean`, `integer` | `alpha=0.5`, `quantile=0.975`, `use_correction=True`, `robust_cor=False`, `seed=1234` | `light` | — |
| `mv_outliers` | `x` | `matrix_handle`, `number`, `number`, `boolean`, `integer` | `alpha=0.5`, `quantile=0.975`, `use_correction=True`, `seed=1234` | `light` | — |

### Use when

a numeric observations×variables matrix (countries × macro indicators, periods × variables) and the question is WHICH ROWS are outlying in the JOINT (multivariate) space — a COMBINATION of values that no univariate check sees (each individual value «normal», the combination impossible); the flow: mv_outliers (classical AND robust SIDE BY SIDE + masked/swamped) -> mv_covmcd (only the robust center/cov/h/best subset) -> mv_mahalanobis (the classical distance, or OUT-OF-SAMPLE scoring with a GIVEN center/cov)

### Do not use when

ONE variable (p >= 2 is a hard gate; univariate tails/capping -> #114 dt_winsorize/dt_trim); TIME-SERIES outliers of type AO/LS/TC/IO in a univariate ts -> #5 run_tso; the LEVELS of non-stationary series (a Mahalanobis distance is UNINTERPRETABLE there: the population mean does not exist and the sample covariance diverges with T — supply differences EXPLICITLY, §3b gate 3); missing data (impute FIRST, cat. 00); CLUSTERING rather than outlier detection -> cat 29 (#241 kmeans/pam, #244 mclust); charts (the frontend, §5); robust REGRESSION (ltsReg/lmrob) — a different family (cat 06/07)

### Prerequisites

- c01_preparation_prechecks/profiling_quality_report.dp_quality_flags # the blockers 'constant' / 'p_ge_n' / 'infinite_values' are EXACTLY the hard gates of this node — run it FIRST
- c00_data_utilities/replacement_missing_values.imputets_interpolation # NA -> imputation BEFORE the node (covMcd SILENTLY drops the incomplete rows: live n.obs = 29 out of 30)
- mv_mahalanobis # a cheap algebraic pass: cov_rcond reveals collinearity BEFORE the MCD runs

### Alternatives

| instead use | when |
| --- | --- |
| mv_outliers (the MAIN function of the card) | you want THE DECISION: the classical AND robust distances at the same cutoff + masked/swamped counts + a ranking by decreasing robust D². It is the default path — the comparison of the two IS the result |
| mv_covmcd (alpha = 0.5) | you want ONLY the ROBUST center/cov (e.g. as fitted parameters for downstream scoring) with MAXIMUM robustness: h ~ n/2, a breakdown point of ~ (n-h+1)/n |
| mv_covmcd (alpha = 0.75) | you know the contamination is < 25% and you want HIGHER EFFICIENCY (a larger h) with less robustness — alpha controls EXACTLY that trade-off |
| mv_mahalanobis (without center/cov) | the sample is PROVABLY clean (or you want the baseline for the comparison): purely algebraic, with no randomness and no MCD |
| mv_mahalanobis(center =, cov = ) | an OUT-OF-SAMPLE APPLY (§3b gate 6): you pass back the center/cov of a previous mv_covmcd => robust scoring of NEW observations; with BOTH supplied, n >= 1 suffices |
| #114 dt_winsorize / dt_trim (c00_data_utilities/robust_outlier_handling) | the objective is UNIVARIATE tail cleaning per series (capping/trimming), not the detection of outlying COMBINATIONS |
| #5 run_tso (tsoutliers) | the input is a TIME SERIES and outliers are wanted BY TYPE (additive / level shift / transitory change), not by a multivariate distance |

### Output fields

- mv_mahalanobis: distance (the named D² per observation — the main chart-data) + distance_sqrt + outlier/outlier_index/outlier_labels + n_outliers/share_outliers + cutoff = qchisq(quantile, df = p) + df = p + center/cov/cov_rcond + center_source/cov_source ('sample' or 'supplied') + max_distance/n/p/observations/variables
- mv_covmcd: center/cov (ROBUST, fit/apply) + cov_rcond + cor (ONLY if robust_cor=TRUE, otherwise NULL) + distance/raw_distance (after/before the reweighting) + raw_center/raw_cov + outlier/n_outliers/share_outliers + h (= h.alpha.n(alpha,n,p)) / h_share / best_subset / in_best_subset + mcd_weight (BINARY 0/1) / n_zero_weight + crit (log(det)) + cnp2/raw_cnp2 (the consistency + finite-sample factors, of LENGTH 2) + method / nsamp='deterministic' / i_best (1.6) / n_csteps (PER initial subset) + small_sample (n < 2p) + alpha/use_correction/seed
- mv_outliers: distance_table (an n×2 «classical \| robust» table — THE CENTRAL chart-data) + classical/robust + outlier_classical/outlier_robust + masked / swamped / both (+ n_ and _labels for each) + order_robust / ranked_labels (by decreasing robust D², ties broken on the name) + classical_center/classical_cov/classical_rcond + robust_center/robust_cov/robust_rcond + h/h_share/best_subset/in_best_subset/mcd_weight/crit + cutoff/quantile/df/alpha/use_correction/small_sample/seed
- ALL of them: observations/variables (the row/column names; if they are missing, obs1.obsN / v1.vP are generated) — every flag/distance is named PER ROW

### Pitfalls

- MASKING / SWAMPING IS THE POINT OF THIS NODE: the classical mean/cov is computed FROM the outlying points themselves => an outlier «hides» itself by inflating the variance (masked) and clean points look outlying (swamped). The MCD estimates from the «cleanest» subset h => it is not corrupted. Do NOT read ONLY the classical column: read n_masked/n_swamped (live in the tests: the classical method found 2 of the 4 planted outliers, the MCD found all 4; and no univariate check would have seen any of them)
- alpha STRICTLY in [0.5, 1) — SILENTLY WRONG: covMcd(alpha = 0.2) does NOT error, it only warns «subsample size h < n/2 may be too small» and returns a fit with h = 9 out of 30 (a breakdown point > 50%: the «robust» subset can be ENTIRELY outlying). The help page states «Allowed values are between 0.5 and 1» => OUR OWN hard gate
- alpha = 1 DEGENERACY (a separate hard gate): «alpha = 1: The minimum covariance determinant estimates.. are equal to the classical estimates» and the returned object has NO mah / best / iBest fields AT ALL (LIVE-VERIFIED in robustbase 0.99.7: names = call,nsamp,method,cov,center,n.obs,alpha,quan,raw.cov,raw.center,crit,mcd.wt,X,raw.cnp2,cnp2) — zero robustness AND no distance
- DETERMINISM (§5): nsamp = 'deterministic' is PINNED (the Deterministic MCD; it starts from the h most central points of SIX deterministic estimators) — the default nsamp = 500 is SUBSAMPLING. The seed is a SAFETY NET for n > nmini*kmini (= 1500 with the defaults), where the help page states explicitly that «the initial search uses only a subsample of size nmini*kmini»; it runs inside set.seed + a RESTORATION of the caller's.Random.seed (L1 purity). covMcd(seed=) is NEVER passed (it requires a whole.Random.seed vector). Live: identical over 2 runs AND IDENTICAL distances with a DIFFERENT seed
- mcd_weight vs outlier: the mcd.wt values are binary and are tied to the FIXED 0.975 of wgtFUN = '01.original' — INDEPENDENT of our own 'quantile'. With quantile != 0.975 n_zero_weight does NOT equal n_outliers (that is not an error: it is a different cutoff)
- SILENTLY WRONG cases blocked by hard gates: p = 1 (covMcd does NOT error but returns an object WITHOUT mah/best — a univariate path); a character column in a data_frame (covMcd calls data_matrix and works on factor CODES, live crit = -2.300799); NA/NaN/Inf (a SILENT dropping of rows); n <= p or n == p+1 (the cryptic «n <= p -- you can't be serious!» / «n == p+1 is too small sample size for MCD»); a constant column or collinearity (mahalanobis: «Lapack routine dgesv: system is exactly singular» / «system is computationally singular: reciprocal condition number..» — pre-checked with rcond >=.Machine.double.eps and exposed as cov_rcond)
- NO STANDARDIZATION, NO transform ARGUMENT (§3b gate 2): the Mahalanobis distance is AFFINE EQUIVARIANT — D²(x) = D²(Ax+b) — so scale(X) gives IDENTICAL distances (classical AND MCD, live-verified). A transform argument would be a no-op that implied a choice which does not exist
- NON-STATIONARITY (§3b gate 3, Hamilton-Ma-Xi): this node is CROSS-SECTION / PANEL. On the LEVELS of I(1) series the population mean is undefined and the sample covariance diverges with T => the distances are uninterpretable. The user supplies differences EXPLICITLY — NEVER a silent correction here
- cnp2 / raw_cnp2 have LENGTH 2 (the consistency factor AND the finite-sample correction, Pison et al. 2002); with use_correction = FALSE the second element becomes 1. small_sample = TRUE (n < 2p) corresponds to the covMcd warning «n < 2 * p» — a DIAGNOSTIC, not a gate
- raw_distance vs distance: distance is AFTER the reweighting (typically considerably more efficient, Pison et al. 2002); raw_distance is before it. best_subset/h ALWAYS refer to the RAW step (length(best) == quan == h.alpha.n(alpha,n,p) — post-checked)
- a TERMINAL node (no register/handle chaining): it returns chart-ready numbers. The fit/apply split is EXPLICIT — the user passes center/cov back into mv_mahalanobis (modelled on the KNIME «Normalize Model»)
- PACKAGE MASKING: library(robustbase) is NOT used — it masks plot (live conflicts(detail=TRUE)); requireNamespace + fully qualified covMcd / h.alpha.n (the CLAUDE.md §3.a exception)

### References

- robustbase 0.99.7 the covMcd routine (live, the engine) — «Allowed values are between 0.5 and 1 and the default is 0.5»; nsamp = «deterministic» ⇒ «starts from the h most central observations of six (deterministic) estimators»; «When nmini*kmini < n, the initial search uses only a subsample of size nmini*kmini»; quan = h.alpha.n(alpha,n,p); length(best) == quan; iBest ∈ 1:6 / n.csteps per initial subset; cnp2 = the consistency + finite-sample factors; wgtFUN = «01.original» (Rousseeuw & Van Driessen 1999)
- Rousseeuw, P.J. & Van Driessen, K. (1999) «A fast algorithm for the minimum covariance determinant estimator», Technometrics 41, 212-223 (FastMCD; cited by the covMcd routine)
- Hubert, M., Rousseeuw, P.J. & Verdonck, T. (2012) «A deterministic algorithm for robust location and scatter», Journal of Computational and Graphical Statistics 21, 618-637 (DetMCD = the PINNED nsamp)
- Pison, G., Van Aelst, S. & Willems, G. (2002) «Small Sample Corrections for LTS and MCD», Metrika 55, 111-123 (use.correction / cnp2 / the efficiency of the reweighting)
- Rousseeuw, P.J. & Leroy, A.M. (1987) Robust Regression and Outlier Detection, Wiley (the breakdown point; why the classical mean/cov collapses in the presence of outliers — cited by the covMcd routine)
- Hamilton, J.D., Ma, X. & Xi, J., «Principal Component Analysis for a Mix of Stationary and Nonstationary Variables», NBER WP 32068 — §3b gate 3 (why this node is cross-section/panel and not for the levels of I(1) series)
- the normative gate spec §3b live-verified gates («covMcd: n == p+1 is too small sample size for MCD; alpha in [0.5,1]»; «covMcd(alpha=0.2) -> only a warning»; «mahalanobis with n<=p or collinear columns -> system is computationally singular»); DETERMINISM: «covMcd ⇒ nsamp="deterministic"»
- wrapper footer IMPLEMENTATION NOTE (c01_preparation_prechecks/multivariate_outlier_detection) — all the silently-wrong cases (p=1, a character column, the silent dropping of NA, alpha=1 without mah/best), the conflicts(detail=TRUE) baseline vs robustbase, and the affine-equivariance verification

## #247 — A battery of NORMALITY tests (the composite hypothesis): EDF omnibus tests (Anderson-Darling / Cramer-von Mises / Lilliefors) + the Pearson chi-square test on equiprobable classes + Shapiro-Francia, with a COMMON alpha and a tidy decision table

**Module:** `battery_normality_edf.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `nt_normality_battery` | `x` | `raw_handle`, `series_codes`, `number`, `integer`, `boolean`, `number`, `string` | `alpha=0.05`, `adjust=True`, `min_expected=5`, `series_name='x'` | `light` | — |
| `nt_ad_test` | `x` | `raw_handle`, `number`, `string` | `alpha=0.05`, `series_name='x'` | `light` | — |
| `nt_cvm_test` | `x` | `raw_handle`, `number`, `string` | `alpha=0.05`, `series_name='x'` | `light` | — |
| `nt_lillie_test` | `x` | `raw_handle`, `number`, `string` | `alpha=0.05`, `series_name='x'` | `light` | — |
| `nt_pearson_test` | `x` | `raw_handle`, `number`, `integer`, `boolean`, `number`, `string` | `alpha=0.05`, `adjust=True`, `min_expected=5`, `series_name='x'` | `light` | — |
| `nt_sf_test` | `x` | `raw_handle`, `number`, `string` | `alpha=0.05`, `series_name='x'` | `light` | — |

### Use when

ONE numeric univariate series (typically model RESIDUALS, returns, a macro series) and the question is whether its DISTRIBUTION is normal, with the parameters UNKNOWN (the composite hypothesis); nt_normality_battery = ALL the requested tests in ONE call -> a tidy table (statistic/p_value/decision) + a consensus summary; the 5 individual functions when you want ONE specific test (or when n rules some of them out)

### Do not use when

JARQUE-BERA (moment-based: skewness+kurtosis) -> it ALREADY EXISTS, #1 run_jarque_bera_test — it is NOT duplicated here (and BEWARE the incompatible NA policy, see the traps); a DESCRIPTIVE Shapiro-Wilk inside a descriptives table (normtest.W/normtest.p, with no gates/decision) -> #129 ps_stat_desc; DESCRIPTIVE moments (skewness/kurtosis per column) -> #248 dp_profile; SEVERAL columns at once (run the node PER COLUMN — a hard gate against a matrix/data_frame); missing values (impute FIRST, cat. 00 imputeTS — a hard stop here); testing STATIONARITY (#1/#2) or AUTOCORRELATION (Ljung-Box; #81 desc_acf) — a different hypothesis; qqnorm/plots (the frontend, §5); MULTIVARIATE normality -> #246 (Mahalanobis distances)

### Prerequisites

- c01_preparation_prechecks/profiling_quality_report.dp_quality_flags # the 'constant' blocker = EXACTLY the zero-variance gate; the 'infinite_values' blocker = the Inf gate; the 'few_rows' warning carries THE SAME min-n values per test
- c00_data_utilities/replacement_missing_values.imputets_interpolation # NA -> imputation BEFORE the node (PROJECT POLICY: a hard stop, NEVER a silent dropping of observations)
- nt_normality_battery # n / the min-n values are checked PER TEST: if one does not fit, the node BLOCKS and says WHICH one to remove

### Alternatives

| instead use | when |
| --- | --- |
| nt_normality_battery (the default: all 5) | you want THE DECISION with cross-checking: a tidy table + a consensus (reject_all / fail_to_reject_all / mixed) + a primary_test by a DOCUMENTED order of preference |
| nt_ad_test (Anderson-Darling) | ONE test, the RECOMMENDED EDF test after Stephens (1986); it gives MORE WEIGHT TO THE TAILS => the first choice when fat tails are the concern (returns, crises); it requires n > 7 |
| nt_sf_test (Shapiro-Francia) | a correlation-based test «known to perform well» (Royston 1993); the SECOND choice in the order of preference; it requires 5 <= n <= 5000 (it is RULED OUT for large samples) |
| nt_cvm_test (Cramer-von Mises) | an EDF omnibus test, the «second choice» after AD (the nortest the ad_test routine Note); less weight on the tails; it requires n > 7 |
| nt_lillie_test (Lilliefors) | the literature/reader asks for it explicitly (the best-known EDF test) — BUT it is «known to perform worse» than AD/CvM; it is the ONLY one that works for 5 <= n <= 7 |
| nt_pearson_test (adjust = TRUE AND FALSE) | you want the chi-square test on equiprobable classes; it is «usually not recommended» (inferior power) AND the correct p-value is NEITHER of the two — it lies BETWEEN them (Moore 1986) => run it BOTH ways |
| #1 run_jarque_bera_test (tseries) | you want a test of MOMENTS (skewness/kurtosis) rather than a deviation of the DISTRIBUTION FUNCTION — COMPLEMENTARY, not a substitute; CAUTION: a different NA policy |

### Output fields

- nt_normality_battery: table = tidy records (test/test_label/method/statistic/statistic_name/p_value/df/n_classes/expected_per_class/n/alpha/reject/decision) — THE MAIN chart-data; the row order is CANONICAL (ad,cvm,lillie,pearson,sf) regardless of the order the user supplied
- nt_normality_battery summary: statistic/p_value/reject (named PER TEST) + n_tests/n_reject/share_reject/reject_any/reject_all + consensus ('reject_all' \| 'fail_to_reject_all' \| 'mixed') + min/max/median_p_value + primary_test/primary_p_value/primary_reject + alpha/n/mean/sd/series/na_policy='error' + results (the complete per-test output, including the raw htest)
- the individual tests: test/test_label/method/statistic/statistic_name/p_value/alpha/reject/decision ('reject_normality' \| 'fail_to_reject') + interpretation (a ready-made sentence) + n/series/na_policy + htest
- pearson ONLY: df / n_classes / expected_per_class / adjust / min_expected (NA in the other tests — showing that they do NOT apply)

### Pitfalls

- MIN-N PER TEST, NEVER A GLOBAL n (the live-verified messages of nortest 1.0.4): ad/cvm need n > 7 («sample size must be greater than 7»); lillie needs n > 4 («.. greater than 4»); sf needs 5 <= n <= 5000 («sample size must be between 5 and 5000» — it RULES OUT LARGE samples too); pearson: NO gate in the package (see below). In the battery there is NO silent skip: if a requested test does not fit, the call STOPS and the user removes it EXPLICITLY from 'tests' (blocked-by-gate, §5)
- AN INCOMPATIBLE NA POLICY — AN EXPLICIT PROJECT DECISION: nortest declares «Missing values are allowed» and SILENTLY applies complete.cases (live: ad_test(c(rnorm(20), NA)) returns a normal result), whereas the EXISTING Jarque-Bera node (#1) ERRORS («NAs in x»). On the SAME input the two normality nodes would give one result and one error, and the reported n would NOT be the n of the input (=> a wrong reading of the min-n gates). THE CHOICE: ONE policy, the STRICTER one — a HARD STOP, with a message pointing at the imputation path (cat. 00); na_policy='error' is ALWAYS returned in the output
- THE SILENTLY-WRONG CASES OF pearson_test (THE PACKAGE HAS NO VALIDITY CHECK AT ALL): (a) n_classes = 3 & adjust = TRUE -> df = 0 -> p = 0 EXACTLY for ANY data (live: p_value == 0 on NORMAL data); (b) n_classes = 2 & adjust = TRUE -> df = -1 -> a warning «NaNs produced» + p = NA; (c) a non-integer n_classes (4.7) is accepted SILENTLY and tabulate truncates it; (d) an expected frequency n/k < 5: the chi-square approximation does not hold (Cochran 1954; Moore 1986) and the reference NEVER warns here; (e) an extreme value with pnorm == 1 -> num = k+1 -> tabulate DROPS the observation (live: sum(counts) = 199 for n = 200, WITH NO warning). EACH ONE is a hard gate here, with the PERMITTED RANGE of n_classes inside the message
- pearson adjust: NEITHER of the two p-values is the correct one — «this is not (!) the correct p-value, lying somewhere between the two» (the pearson_test routine); adjust=TRUE => df = k-3 (a correction for the 2 estimated parameters); FALSE => df = k-1. Run BOTH and read them as BOUNDS. The statistic is THE SAME, only the df/p change (live-verified)
- Lilliefors != ks_test: «Although the test statistic obtained from lillie_test(x) is the same as that obtained from ks_test(x, "pnorm", mean(x), sd(x)), it is not correct to use the p-value from the latter for the composite hypothesis of normality (mean and variance unknown), since the distribution of the test statistic is different when the parameters are estimated» (the lillie_test routine). NEVER compare the two p-values
- Shapiro-FRANCIA != Shapiro-WILK: nortest exposes the Shapiro-Francia test (the squared correlation with the expected normal quantiles, qnorm(ppoints(x, a = 3/8))); the Shapiro-Wilk test (shapiro_test) is NOT exposed as inference by any node — it appears ONLY descriptively in #129 ps_stat_desc (normtest.W/normtest.p, with no gates/decision)
- THE ORDER OF PREFERENCE (primary_test) IS DOCUMENTED, NOT ARBITRARY: ad > sf > cvm > lillie > pearson, taken from the Notes of the help pages themselves («the recommended EDF test by Stephens (1986)»; «known to perform well.. Royston (1993)»; «as second choice»; «known to perform worse»; «usually not recommended.. inferior power properties»). primary_test is the FIRST available one of that order inside the selected subset
- consensus = 'mixed' IS A NORMAL RESULT, not an error: the tests have DIFFERENT power against different departures (tails vs the centre vs moments). Live in the tests: with an alpha BETWEEN the p-values of ad (9.73e-05) and cvm (4.59e-04) ONLY ad rejects (n_reject = 1, share = 0.2). Read primary_test + the WHOLE table, never a single cell
- fail_to_reject DOES NOT PROVE NORMALITY (the interpretation field itself says so explicitly); it is the absence of EVIDENCE against normality at the given n. alpha changes ONLY the decision column — NEVER the p_value
- OTHER silently-wrong cases that are blocked: an Inf in the input -> ad/cvm/lillie fail cryptically («missing value where TRUE/FALSE needed») BUT sf -> W = NaN / p = NaN and pearson -> a NORMAL-LOOKING P = 21 / p = 0.00032, NEITHER OF THEM with an error or a warning; ZERO VARIANCE -> ad/cvm/lillie fail cryptically, sf gives a warning + NA, pearson gives a FALSELY «significant» result WITH NOTHING AT ALL (the worst of the family); a matrix/data_frame -> a hard stop (run it PER COLUMN)
- DETERMINISM (§5): no RNG in any of the 5 tests (closed-form formulas/tables from Stephens 1986, Dallal-Wilkinson 1986, Royston 1993, chi-square) => NO seed; identical over 2 runs AND identical output regardless of the order of 'tests'
- series_name is a LABEL, NOT data: it replaces the data.name of the htest (nortest fills it with deparse(substitute(x)), which on the node path — do.call(fn, coerced) — would serialize the WHOLE vector into the JSON). A TERMINAL node, no register/chaining. MASKING: library(nortest) is SAFE — conflicts(detail=TRUE) is identical before/after, with zero S3 registration

### References

- nortest 1.0.4 the ad_test routine (live, the engine) — «The Anderson-Darling test is the recommended EDF test by Stephens (1986). Compared to the Cramer-von Mises test (as second choice) it gives more weight to the tails of the distribution»
- nortest 1.0.4 the lillie_test routine — «The Lilliefors (Kolomorov-Smirnov) test is the most famous EDF omnibus test for normality. Compared to the Anderson-Darling test and the Cramer-von Mises test it is known to perform worse»; AND the explicit warning that the ks_test p-value does not apply to the composite hypothesis
- nortest 1.0.4 the sf_test routine — «The Shapiro-Francia test is known to perform well, see also the comments by Royston (1993)»; the expected quantiles are approximated with qnorm(ppoints(x, a = 3/8))
- nortest 1.0.4 the pearson_test routine — the usage pearson_test(x, n.classes = ceiling(2 * (n^(2/5))), adjust = TRUE) («The default is due to Moore (1986)»); «usually not recommended.. due to its inferior power properties»; «In both cases this is not (!) the correct p-value, lying somewhere between the two, see also Moore (1986)»
- Stephens, M.A. (1986) «Tests based on EDF statistics», in D'Agostino, R.B. & Stephens, M.A. (eds), Goodness-of-Fit Techniques, Marcel Dekker, New York (AD/CvM; cited by the ad_test routine / the cvm_test routine)
- Dallal, G.E. & Wilkinson, L. (1986) «An analytic approximation to the distribution of Lilliefors' test for normality», The American Statistician 40, 294-296 (cited by the lillie_test routine)
- Royston, P. (1993) «A pocket-calculator algorithm for the Shapiro-Francia test for non-normality: an application to medicine», Statistics in Medicine 12, 181-184 (cited by the sf_test routine)
- Moore, D.S. (1986) «Tests of the chi-squared type», in D'Agostino & Stephens (eds), Goodness-of-Fit Techniques, Marcel Dekker (the default n.classes; why the correct p-value lies BETWEEN the two)
- Cochran, W.G. (1954) «Some Methods for Strengthening the Common chi-square Tests», Biometrics 10(4), 417-451 — the minimum EXPECTED frequency rule (the default min_expected = 5)
- Thode Jr., H.C. (2002) Testing for Normality, Marcel Dekker, New York (a common reference in all 5 help pages; §5.2 for the Pearson chi-square test)
- the normative gate spec §3b live-verified gates — «the nortest min-n PER TEST: ad/cvm n>7 · lillie n>4 · sf 5<=n<=5000» AND «jarque.bera_test: NAs in x — an INCOMPATIBLE NA policy: nortest accepts NA, JB does not»
- wrapper footer IMPLEMENTATION NOTE (c01_preparation_prechecks/battery_normality_edf) — the boundary against #1/#129, the 5 live-verified silently-wrong cases of pearson_test, the identical conflicts(detail=TRUE) before/after library(nortest), and the justification of the NA policy

## #248 — Data profiling / a quality report: a PER-COLUMN profile (type/missing/uniqueness/Joanes-Gill moments) + a dataset-level summary + RULE-BASED quality flags (blocker/warning) with a rule and a source

**Module:** `profiling_quality_report.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `dp_profile` | `data` | `df_handle`, `integer`, `enum` | `quantile_type=7` | `light` | — |
| `dp_column_profile` | `data`, `column` | `df_handle`, `string`, `integer`, `enum`, `integer`, `integer` | `quantile_type=7`, `bins=10`, `top_n=10` | `light` | — |
| `dp_quality_flags` | `data` | `df_handle`, `number`, `number`, `integer`, `integer`, `enum` | `max_missing_pct=10`, `max_unique_ratio=0.95`, `min_rows=8`, `quantile_type=7` | `light` | — |

### Use when

THE FIRST node of every workflow, BEFORE any statistical method runs: «what is this data and what is wrong with it?» — dp_profile (a tidy per-column profile + a dataset summary) -> dp_column_profile (ONE column in depth: a quantile grid + a histogram or a top-N frequency table) -> dp_quality_flags (structured flags with a severity, a rule and a source, so that the user knows WHAT will block downstream and WHY). It works on MIXED column types (numeric/integer/logical/character/factor/Date/POSIXct) — the non-numeric columns are NOT lost and are NOT coerced

### Do not use when

TRANSFORMATION/imputation/standardization — the node DIAGNOSES, it does NOT alter (§3b gate 2; imputation -> cat. 00 imputeTS); CROSS-VARIABLE missingness patterns (which columns are missing TOGETHER) -> #249 missing-pattern (a separate node, «one wrapper = one node»); NORMALITY TESTS with a p-value/decision -> #247 nortest / #1 Jarque-Bera (here the moments are DESCRIPTIVE); CORRELATIONS + p-values -> #130 hm_rcorr; OUTLIERS (multivariate) -> #246; TIME-SERIES DESCRIPTIVES (ACF/PACF/rolling) -> #81 descriptives; a stat.desc table with normality criteria -> #129 pastecs; charts (the frontend, §5 — the node supplies ONLY breaks/counts/mids)

### Alternatives

| instead use | when |
| --- | --- |
| dp_profile | you want THE PICTURE OF THE WHOLE dataset in one tidy table (one row per column) + a dataset-level summary; the cheapest first pass |
| dp_column_profile | you have spotted ONE suspicious column and you want depth: a quantile grid p0.p100, a histogram (NUMERIC) or a top-N frequency table (CATEGORICAL/logical/date) + the factor levels |
| dp_quality_flags | you want a DECISION rather than numbers: structured blocker/warning flags with a rule, a detail and a value — what WILL BREAK downstream (constant/p>=n/duplicates/no complete rows) before it breaks |
| moment_type = 'type2' (SAS/SPSS) | you want the G1/G2 estimator that is unbiased under normality (it requires n >= 3 / n >= 4; otherwise NA) — e.g. to compare with SAS/SPSS output |
| moment_type = 'type3' (MINITAB/BMDP) | you want b1/b2 — e.g. to compare with MINITAB OR with e1071, whose OWN DEFAULT is type = 3 (our default is type1) |
| quantile_type != 7 | you need a specific quantile algorithm (Hyndman & Fan 1996, types 1.9); 7 is the reference/S default and is EXPLICITLY pinned for determinism |
| #249 mp_pattern (missing-pattern) | the question is not «how many are missing per column» but «WHICH columns are missing TOGETHER» (missingness patterns/pairs/runs) |

### Output fields

- dp_profile: profile = tidy records PER COLUMN {column, type, n, n_missing, pct_missing, n_infinite, n_valid, n_unique, is_constant, n_zeros, min, q1, median, mean, q3, max, iqr, sd, skewness, kurtosis} — the main chart-data
- dp_profile: dataset = {rows, cols, complete_rows, incomplete_rows, pct_complete_rows, duplicate_rows, distinct_rows, n_cells, n_missing_cells, pct_missing_cells, n_constant_cols, n_all_missing_cols, n_cols_with_missing, n_cols_with_infinite} + type_counts (a named integer over the 7 types) + columns
- dp_column_profile: all the above fields for the ONE column + quantiles (named p0/p1/p5/p10/p25/p50/p75/p90/p95/p99/p100) + quantile_probs + histogram {breaks, counts, mids, bins, degenerate} (NUMERIC only; otherwise NULL) + frequency (top-N records {value, count, pct}; non-numeric only) + n_levels/levels (factor only)
- dp_quality_flags: flags = tidy records {scope, column, issue, severity, detail, value} SORTED (blocker < warning < info, then issue, then column) + n_flags/n_blockers/n_warnings/has_blocker/blocked_columns + profile + dataset + thresholds
- ALL of them: quantile_type + moment_type + kurtosis_excess = TRUE (§3b gate 6 — TWO profiles are comparable ONLY under the SAME estimator)

### Pitfalls

- AN EXPLICIT DEFINITION OF THE MOMENTS (NEVER «just skewness»): Joanes & Gill (1998), the same typology as e1071. m_r = (1/n) sum (x_i - xbar)^r (the MOMENT estimator, with divisor n NOT n-1). type1 (THE DEFAULT): g1 = m3/m2^(3/2), g2 = m4/m2^2 - 3; type2 (SAS/SPSS): G1 = g1*sqrt(n(n-1))/(n-2) [n>=3], G2 = ((n+1)g2+6)(n-1)/((n-2)(n-3)) [n>=4]; type3 (MINITAB/BMDP): b1 = g1*((n-1)/n)^(3/2), b2 = (g2+3)(1-1/n)^2 - 3. THE KURTOSIS IS ALWAYS EXCESS (normal => 0) in ALL THREE types — it is declared explicitly as kurtosis_excess = TRUE
- COMPARABILITY: OUR default is type1, whereas e1071 defaults to type = 3 (the the skewness routine usage) — TWO «skewness» values on the same data can differ because the ESTIMATOR changed, not the data. That is why moment_type/quantile_type/kurtosis_excess are ALWAYS returned (§3b gate 6). The tests pin identity against an INDEPENDENT recomputation AND against e1071 for all 3 types
- NO SILENT COERCION (§3b gate 2): the non-numeric columns get the COUNT fields and NA for the moments — they are NEVER turned into numbers. An UNKNOWN S3 class (difftime/ts/units/labelled/AsIs) => a HARD STOP: it was LIVE-VERIFIED as silently wrong that a difftime is a double, so without the gate it would be profiled as «numeric» with moments in UNKNOWN UNITS (days/secs). Likewise a stop for: a list-column / a data_frame-column / a matrix-column / POSIXlt (internally a list of 9 fields) / complex
- NEVER NaN/Inf IN THE OUTPUT (the post-check.dp_postcheck_finite): the DOCUMENTED silently-wrong behaviours of the standard library that are neutralised — min/max on an ALL-NA column -> Inf/-Inf + the warning «no non-missing arguments to min; returning Inf» (here NA_real_); the moments of a constant column -> 0/0 = NaN (here NA_real_); NUMERIC OVERFLOW with c(1e308, -1e308) -> sd = Inf WITHOUT an error (here it BLOCKS: the profile would be numerically meaningless)
- NaN COUNTS AS MISSING (is.na(NaN) == TRUE), Inf does NOT — it is counted separately in n_infinite, excluded from the moments AND flagged as a blocker. n_valid = the non-missing AND finite values. n_unique counts the DISTINCT NON-missing values — for a factor the PRESENT levels, NOT nlevels (which is exposed separately as n_levels in dp_column_profile)
- EDGE-CASE BEHAVIOUR (documented + tested): an ALL-NA column => n_unique = 0, is_constant = NA (NOT FALSE), all the moments NA; n = 1 valid value => min=q1=median=mean=q3=max, iqr = 0, sd = NA (sd of one value), skew/kurt = NA; a constant column => sd = 0 BUT skew/kurt = NA (m2 == 0); n_zeros = NA for NON-numeric columns («zero» is undefined there)
- THE MOMENTS ARE DESCRIPTIVE, NOT INFERENCE: on an AUTOCORRELATED series they are NOT evidence of normality nor a basis for a test (compare §3b gate 4: autocorrelation inflates the Type I error). For a normality decision -> #247 nortest / #1 JB; for inference under autocorrelation -> the HAC path (sandwich, cat 07)
- THE HISTOGRAM IS NOT hist: the «Sturges» breaks there are pretty-adjusted (an UNPREDICTABLE number of bins); here they are EXACTLY equal-width seq(min, max, length.out = bins+1) => reproducible. A constant column (min == max) => ONE degenerate bin (degenerate = TRUE) instead of degenerate equal breaks. A post-check: sum(counts) == the number of values (no value is lost). NO DRAWING — only breaks/counts/mids (§5)
- dp_quality_flags: THE RULES ARE EXPLICIT AND SOURCED — all_missing (a blocker); high_missing > max_missing_pct (a warning; the default 10%, the Bennett 2001 rule as the detail itself cites it); constant (a blocker: cor -> NA with ONLY a warning; scale/a z-score divides by 0); infinite_values (a blocker); high_cardinality >= max_unique_ratio (a warning: it looks like an identifier, not a variable); duplicate_rows (a warning: it breaks kmeans with «more cluster centers than distinct data points» and isoMDS with «zero or negative distance»); few_rows < min_rows (a warning: the min-n values per normality test); p_ge_n (a blocker: a singular covariance -> mahalanobis «system is computationally singular»; Mclust does not even error); no_complete_rows (a blocker). all_missing EXCLUDES high_missing (an else-if): one flag per column for missingness
- dp_quality_flags DOES NOT STOP EXECUTION: it produces STRUCTURED flags that the frontend displays educationally (blocked-by-gate as a STATE, not an error); the hard stop calls are ONLY for STRUCTURALLY invalid input (duplicate/empty column names, a list-column, an unknown class, a quantile_type outside 1.9)
- DETERMINISM (§5): no RNG/seed, no sampling, no parallelism; ALL the orderings have an EXPLICIT tie-break — flags: severity -> issue -> column with method='radix' (locale-independent); frequency: DECREASING count with a LEXICOGRAPHIC tie-break on the value. identical over 2 runs is pinned in the tests (both the wrapper AND the node path)
- WHY the standard library AND NOT DataExplorer/skimr/naniar (the normative gate spec §3b REJECTED): we take the FEATURE, the PACKAGES are rejected — they drag in ggplot2/gridExtra/reshape2/rmarkdown/networkD3 and they DRAW (md.pattern(plot=TRUE) is the default) => a violation of §5; the naniar .order argument has an INCONSISTENT documented default => a determinism risk. Zero new dependencies here. df_handle (NOT matrix_handle):.mcp_to_matrix WOULD DROP the non-numeric columns — precisely what the profiling is obliged to REPORT

### References

- Joanes, D.N. & Gill, C.A. (1998) «Comparing measures of sample skewness and kurtosis», The Statistician (JRSS-D) 47, 183-189 — the type 1/2/3 typology of the skewness/kurtosis estimators
- e1071 the skewness routine / the kurtosis routine (live, the engine) — the EXACT formulas of type1/2/3 («g1 = m3/m2^(3/2)»; «G1 = g1*sqrt(n(n-1))/(n-2). Used in SAS and SPSS»; «b1 = m3/s^3 = g1((n-1)/n)^(3/2). Used in MINITAB and BMDP»; «G2 = ((n+1)g2+6)(n-1)/((n-2)(n-3))»; «Only G2 (type = 2) is unbiased under normality») AND the type = 3 default of e1071, citing Joanes & Gill (1998)
- Hyndman, R.J. & Fan, Y. (1996) «Sample Quantiles in Statistical Packages», The American Statistician 50(4), 361-365, doi:10.1080/00031305.1996.10473566 — the 9 types of quantile (cited by the quantile routine); type = 7 = the reference/S default, EXPLICITLY pinned and exposed
- Cochran-type rules do NOT apply here (this node is DESCRIPTIVE); the few_rows/p_ge_n/duplicate_rows flags reproduce the live-verified gates of the normative gate spec §3b: «the nortest min-n PER TEST: ad/cvm n>7 · lillie n>4 · sf 5<=n<=5000»; «mahalanobis with n<=p or collinear columns -> system is computationally singular»; «Mclust with p>n -> it does NOT error, it returns a fit»; «kmeans: more cluster centers than distinct data points»; «isoMDS: zero or negative distance»; «cor on a zero-variance column -> only a warning, it returns NA»
- the normative gate spec §3b REJECTED — «DataExplorer/skimr/naniar/mice/VIM as dependencies: we TAKE the feature (the standard library in data-profile/missing-pattern); the packages are rejected (they drag in ggplot2/..; md.pattern(plot=TRUE) DRAWS by default ⇒ a violation of §5; the naniar .order default is inconsistent ⇒ a determinism risk)»; AND §3b gates 2 (no silent conversion) / 6 (fit-apply externalization)
- Bennett, D.A. (2001) «How can I deal with missing data in my study?», Australian and New Zealand Journal of Public Health — the rule «>10% missing ⇒ possible bias», as the detail of the high_missing flag in the wrapper itself cites it
- wrapper footer IMPLEMENTATION NOTE (c01_preparation_prechecks/profiling_quality_report) — the explicit moment formulas, the live-verified silently-wrong cases (difftime as a double; min on an all-NA column -> Inf + a warning; sd = Inf on overflow), the justification of the histogram without hist, and the conflicts(detail=TRUE) baseline (no library => zero masking, but ALL the calls are base::/stats:: qualified because OTHER wrappers in the shared source env mask core generics)

## #249 — Analysis of MISSINGNESS PATTERNS (CROSS-VARIABLE): a pattern matrix 1=observed/0=missing + counts per pattern + an EXACT MONOTONICITY check (Van Buuren) · NA runs/spans per variable (a ragged edge / mixed frequency) · co-missingness per PAIR (rr/rm/mr/mm)

**Module:** `missingness_patterns_pattern.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `mp_pattern` | `data` | `df_handle`, `string`, `enum` | — | `light` | — |
| `mp_runs` | `data` | `df_handle`, `string` | — | `light` | — |
| `mp_pairs` | `data` | `df_handle`, `string` | — | `light` | — |

### Use when

the question is NOT «how many are missing PER COLUMN» (that is #248) but «WHICH COMBINATIONS of variables are missing TOGETHER»: 10% missing across 5 variables may be ONE common pattern (the same 10 countries) or 5 DISJOINT ones (=> 40% incomplete rows). The flow: mp_pattern (how many DISTINCT patterns, complete cases, MONOTONICITY) -> mp_runs (WHERE the gaps sit in time: leading/internal/trailing => mixed frequency vs a ragged edge from a publication lag) -> mp_pairs (which PAIRS are missing together). It works on MIXED column types — the criterion is ONLY is.na, with no coercion

### Do not use when

IMPUTATION / dropping rows or columns / any alteration — the node DIAGNOSES (§3b gate 2; filling NA in a time series -> imputeTS #80); a per-column profile/moments/types/quality flags -> #248 dp_profile («one wrapper = one node»); ESTIMATION with a ragged edge / mixed frequency rather than DIAGNOSIS -> dfms #15 / mfbvar #17 / midasr #18 / sparseDFM #144; an MCAR TEST (Little 1988) — NOT exposed (it requires normality + EM, and the autocorrelation of macro panels violates the assumptions — compare §3b gate 4); charts (the frontend, §5 — the node supplies ONLY 0/1 matrices, counts and spans); data WITHOUT names/with DUPLICATE column names (the patterns would be ambiguous)

### Prerequisites

- c01_preparation_prechecks/profiling_quality_report.dp_profile # FIRST the per-column profile (#248: how many are missing per column); HERE the question WHICH are missing TOGETHER is answered
- mp_pattern # run it FIRST: n_patterns / n_complete_cases / monotone.is_monotone decide whether mp_runs or mp_pairs are needed at all

### Alternatives

| instead use | when |
| --- | --- |
| mp_pattern | you want the STRUCTURE of the missingness: how many DISTINCT patterns exist, how many rows per pattern, how many complete cases, and whether the pattern is MONOTONE (critical for which imputation mechanism is admissible) |
| mp_runs | the data are TIME-ORDERED and you want to know WHERE the gaps are: trailing NA = a ragged edge (a publication lag), leading NA = a series that starts later, internal = mixed frequency or a silent gap. The pattern matrix does NOT distinguish the three cases |
| mp_pairs | you want the PER-PAIR view (the semantics of md.pairs): rr = both observed; rm = the row observed/the column missing; mr = the reverse; mm = both missing — which pairs NEVER have observations in common (rr = 0 ⇒ no pairwise correlation is defined) |
| sort_by = 'missingness' | you want the mice MEANING («increasing amounts of missing information») for the ROW ordering; the default 'count' = a DECREASING number of rows (the most frequent pattern first). BOTH are TOTAL orderings with a complete tie-break — mice does NOT define a tie-break |
| time = <a column name> | a STRICTLY INCREASING time column exists: it is excluded from the variables (it is the axis) and the spans get start_time/end_time LABELS; without it the positions are plain row indices |
| #248 dp_profile / #80 imputeTS | you need counts+moments PER COLUMN (#248) or the FILLING of the gaps (#80) — #249 NEVER alters the data |

### Output fields

- mp_pattern: pattern_matrix (an n_patterns x n_cols INTEGER 0/1 matrix, dimnames pattern_i x the column name — THE MAIN chart-data) + pattern_counts + pattern (tidy records {pattern_id, pattern_key, count, pct, n_missing_vars, n_observed_vars, missing_vars, is_complete_case}) + variables ({variable, n_missing, n_observed, pct_missing}) + row_missing_counts (chart-data per ROW)
- mp_pattern.monotone: {is_monotone, order (the names in the MONOTONE ordering), order_index, n_violating_rows, pct_violating_rows, first_violating_row} — an EXACT check, not a heuristic
- mp_pattern.summary: {n_rows, n_cols, n_patterns, n_complete_cases, n_incomplete_cases, pct_complete_cases, n_cells, n_missing_cells, pct_missing_cells, n_cols_with_missing, n_all_missing_cols, n_complete_cols, any_missing}
- mp_runs: runs = tidy records ONE PER NA SPAN {variable, run_id, start, end, length, position ∈ leading\|internal\|trailing\|all, start_time, end_time} + variables (+ n_runs, longest_run, leading_na, trailing_na, n_internal_runs, n_internal_missing, first_obs/last_obs (+ *_time), is_all_missing, is_complete) + na_counts_by_row
- mp_runs.summary: {n_runs, n_vars_with_missing, n_vars_ragged_start, n_vars_ragged_end, n_vars_internal_gaps, max_leading_na, max_trailing_na, balanced_start, balanced_end, ragged_edge, n_all_missing_cols} — ragged_edge is THE decision field for nowcasting workflows
- mp_pairs: rr / rm / mr / mm (FOUR p x p INTEGER matrices with dimnames — chart-data) + pairs (tidy records i<j {variable_1, variable_2, both_observed, both_missing, only_1_missing, only_2_missing, pct_both_missing}) + summary {n_pairs, n_pairs_co_missing, max_both_missing}
- ALL of them: columns (ALWAYS in the INPUT ORDER) + time_name (+ sort_by in mp_pattern, time_labels in mp_runs) — §3b gate 6: ALL the parameters that determine the output are returned, so that two runs are COMPARABLE

### Pitfalls

- WHY the standard library AND NOT mice (the normative gate spec §3b REJECTED — a DOCUMENTED DECISION): we take the SEMANTICS of md.pattern/md.pairs WITHOUT the dependency, because (a) mice MASKS both `filter` AND `complete` in the SHARED source env (CLAUDE.md §3.a) and (b) md.pattern has «plot = TRUE» AS ITS DEFAULT — that is, it DRAWS, violating charter §5 «charts ONLY in the frontend». Here: ZERO new dependencies, ZERO drawing, only numeric chart-data. The ENCODING (1 = observed, 0 = missing) and the rr/rm/mr/mm of md.pairs are preserved
- A DELIBERATE DIFFERENCE FROM mice: (i) the counts are NOT appended as the LAST ROW/COLUMN of the same matrix (they would pollute the chart-data with non-binary values) but are SEPARATE fields (pattern_counts / variables); (ii) the COLUMNS are NEVER reordered — mice «sorts rows and columns in increasing amounts of missing information», so the SAME schema with different data gives a DIFFERENT column order (incomparable runs)
- A DETERMINISTIC ORDERING — AN EXPLICIT RULE (no RNG anywhere): the COLUMNS are ALWAYS in the input order. The pattern ROWS use THREE keys: sort_by='count' (default) => DECREASING count -> INCREASING n_missing_vars -> INCREASING pattern key; sort_by='missingness' => INCREASING n_missing_vars -> DECREASING count -> INCREASING pattern key. The pattern key is UNIQUE per pattern ⇒ the ordering is TOTAL (no tie is left unresolved). RUNS: the input order of the variables, then INCREASING start. PAIRS: DECREASING both_missing -> INCREASING i -> INCREASING j. ALL with method='radix' = the C locale ⇒ locale-independent (live-verified: order(c('a','B'), method='radix') = 2,1 whereas the default en_US gives 1,2)
- MONOTONICITY — WHAT IT MEANS AND WHY THE CHECK IS EXACT: the Van Buuren definition (FIMD 2nd ed., §4.1.1) — «A missing data pattern is said to be monotone if the variables Y_j can be ordered such that if Y_j is missing then all variables Y_k with k>j are also missing». Equivalently: the sets M_j = {i : Y_ij is missing} are NESTED. The node does NOT search over p! orderings: it checks ONE (increasing \|M_j\|) and that SUFFICES, because nested sets have increasing cardinality and equinumerous nested sets are EQUAL. The tests verify this against a BRUTE-FORCE search over all p! orderings
- THE DEFINITION OF MISSING (explicit, NEVER «just missingness»): MISSING = is.na(x). So NaN COUNTS as missing (is.na(NaN) == TRUE, live-verified) while ±Inf does NOT (is.na(Inf) == FALSE — it is a VALUE). For Inf diagnostics -> #248 dp_profile (the n_infinite field)
- WHY THERE IS A GATE FOR A STRICTLY INCREASING TIME COLUMN: NA runs/spans are defined ONLY if «the row order = the time order». With an unsorted or DUPLICATED time column (= a panel, not a series) the spans are MEANINGLESS WITHOUT any error (silently wrong) ⇒ a hard stop; also NO NA in the axis. The check uses order(method='radix') + anyDuplicated, NOT is.unsorted on a character vector (which depends on the LOCALE)
- THE RUNS DEPEND ON THE ROW ORDER — the patterns/counts/monotonicity do NOT: the tests pin an UNCHANGED mp_pattern result under a RANDOM ROW PERMUTATION. THE ONLY field of mp_pattern that depends on the order is monotone.first_violating_row (it is a ROW INDEX by definition)
- COLUMN-TYPE GATES — AN ESSENTIAL DIFFERENCE FROM #248: here NO moment is computed and NO coercion happens, so «unknown» ATOMIC S3 classes (difftime/ts/units/labelled/AsIs) ARE ALLOWED (is.na is type-agnostic) — whereas #248 BLOCKS them (moments in unknown units). What is blocked is EXACTLY the structures where is.na does NOT give a vector of length nrow: a matrix-column / a data_frame-column (it returns a MATRIX) / POSIXlt (internally a LIST of 9 fields) / a list-column (it checks the CONTENT of each element, not the cell) / complex (not JSON-safe)
- POST-CHECKS AS MUTATION GUARDS (STRUCTURALLY impossible to trigger from a valid input; that is why they are SEPARATE functions that the tests call DIRECTLY): the sum of the pattern counts == nrow (the patterns PARTITION the rows); the complete cases derived from the patterns == a direct count; the sum of the run lengths per variable == its number of missing values (the completeness of the rle); rr+rm+mr+mm == nrow in EVERY cell
- EDGE-CASE BEHAVIOUR (documented + tested, NEVER an error): NO missing values => ONE pattern (all 1s), n_patterns = 1, any_missing = FALSE, monotone = TRUE (empty M_j are trivially nested), 0 runs, mm = 0 everywhere; an ALL-NA column => ONE run with position='all', first_obs/last_obs = NA, it does NOT break monotonicity; an ALL-NA dataset => ONE pattern (all 0s), n_complete_cases = 0; nrow == 1 => vapply(df, is.na) returns a VECTOR (live-verified) ⇒ an explicit matrix fallback; ncol == 1 => mp_pairs returns 0 pairs with the CORRECT shape, rr/mm being 1x1
- MASKING: NO library — only base/stats (always attached) ⇒ ZERO masking by construction (conflicts(detail=TRUE) is IDENTICAL BEFORE and AFTER the source, live-verified). CONVERSELY, ALL the calls are base::/stats:: qualified because OTHER wrappers in the SHARED source env mask core generics (proxy -> as_matrix/dist; sn -> sd; ARIMA -> ARIMA) ⇒ the behaviour does not depend on the LOAD ORDER
- df_handle AND NOT matrix_handle (the node layer):.mcp_to_matrix WOULD DROP the NON-NUMERIC columns — that is, it would HIDE exactly the missing values that the node is supposed to count (silent data loss). TERMINAL nodes: no register/chaining

### References

- van Buuren, S. «Flexible Imputation of Missing Data», 2nd ed., §4.1.1 — the definition of a MONOTONE pattern: «A missing data pattern is said to be monotone if the variables Y_j can be ordered such that if Y_j is missing then all variables Y_k with k>j are also missing»
- mice package documentation (the md.pattern / md.pairs help pages) — «1=observed, 0=missing»; «Rows and columns are sorted in increasing amounts of missing information»; «The last column and row contain row and column counts»; «Default is plot = TRUE»; md.pairs: rr = «both variables are observed», rm = «row observed, column missing», mr = «row missing, column observed», mm = «both variables are missing». NOTE: mice is NOT a dependency of the project and is NOT installed — the semantics are reproduced and recorded VERBATIM in the wrapper's footer
- the normative gate spec §3b REJECTED — «DataExplorer/skimr/naniar/mice/VIM as dependencies: we TAKE the feature (the standard library in data-profile/missing-pattern); the PACKAGES are rejected (md.pattern(plot=TRUE) DRAWS by default ⇒ a violation of §5)» + the masking table «mice: filter, complete ⇒ REJECTED» + §3b gates 2 (no imposed conversion) and 6 (fit/apply externalization)
- Little, R.J.A. (1988) «A Test of Missing Completely at Random for Multivariate Data with Missing Values», JASA 83(404), 1198-1202 — the MCAR test is NOT exposed by this node (it requires normality + EM; the autocorrelation of macro panels violates the assumptions, compare §3b gate 4)
- wrapper footer IMPLEMENTATION NOTE (c01_preparation_prechecks/missingness_patterns_pattern) — the explicit definitions (MISSING/PATTERN/MONOTONE/NA RUN), the proof that one candidate ordering suffices, the live-verified edge cases (vapply with nrow==1 -> a vector), the 4 post-checks and the conflicts(detail=TRUE) baseline

## #250 — Battery of PARAMETRIC MEAN tests on CROSS-SECTION data: t-test (one sample / two samples Welch or Student pooled / paired) · one-way ANOVA (equal variances, a full ANOVA table) · the one-way Welch (1951) test WITHOUT the equal-variance assumption

**Module:** `battery_parametric_mean.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `tp_t_test` | `x` | `raw_handle`, `raw_handle`, `number`, `boolean`, `boolean`, `enum`, `number`, `number`, `enum`, `string`, `string`, `integer`, `number`, `boolean` | `mu=0`, `paired=False`, `var_equal=False`, `conf_level=0.95`, `alpha=0.05`, `x_name='x'`, `y_name='y'`, `gate_alpha=0.05`, `ordered=True` | `light` | — |
| `tp_anova` | `data`, `response`, `group` | `df_handle`, `string`, `string`, `number`, `enum`, `integer`, `number`, `boolean` | `alpha=0.05`, `gate_alpha=0.05`, `ordered=True` | `light` | — |
| `tp_welch` | `data`, `response`, `group` | `df_handle`, `string`, `string`, `boolean`, `number`, `enum`, `integer`, `number`, `boolean` | `var_equal=False`, `alpha=0.05`, `gate_alpha=0.05`, `ordered=True` | `light` | — |

### Use when

a FAST MEAN test on CROSS-SECTION data — countries, firms, households, survey respondents — BEFORE a heavy model is thrown at it: «does the sample's mean growth rate differ from 2%?» (tp_t_test one-sample) · «do euro and non-euro differ?» (two-sample; Welch = THE DEFAULT) · «did something change before/after the reform in the SAME units?» (paired) · «do THREE+ regions differ?» (tp_anova for the ANOVA table/eta^2; tp_welch when the variances are NOT equal or the n_i are very unequal)

### Do not use when

TIME SERIES or time-dependent data — a HARD GATE (§3b normative gate 4); the HAC path: #35 sandwich (cat. 07-causality-policy — wrap_vcov_hac/wrap_vcov_cl/wrap_vcov_panel); NON-NORMAL or VERY SMALL samples -> #251 tests-nonparametric (rank-based); a normality DECISION -> #247 nortest / #1 Jarque-Bera; TWO CATEGORICAL variables -> #257 categorical-assoc (chi-squared/Fisher); MULTI-FACTOR / repeated-measures / Error strata / weights / contrasts -> ANOTHER family (not exposed here: ONLY one-way); POST-HOC comparisons (TukeyHSD) -> not exposed; charts (the frontend, §5 — the node supplies n/mean/sd per group and the ANOVA table as NUMBERS)

### Prerequisites

- c01_preparation_prechecks/battery_normality_edf.nt_normality_battery # (#247) a normality DECISION BEFORE you choose parametric vs #251
- c01_preparation_prechecks/profiling_quality_report.dp_quality_flags # (#248) constant columns / Inf / few_rows — EXACTLY the gates that will block here
- tp_welch # run BOTH: if tp_anova and tp_welch disagree, the EQUAL-VARIANCE assumption is the problem

### Alternatives

| instead use | when |
| --- | --- |
| tp_t_test(var_equal = FALSE) — DEFAULT | TWO independent samples: Welch/Satterthwaite is the SAFE default (separate variances); var_equal=TRUE (Student pooled, df = n1+n2-2) ONLY if the variances really are equal — and ONLY in the two-sample unpaired design (in one-sample/paired stats IGNORES it SILENTLY ⇒ a hard gate) |
| tp_t_test(paired = TRUE) | the SAME units measured TWICE (before/after); it requires EQUAL lengths. ⚠️ The Ljung-Box precheck runs ON THE DIFFERENCES d = x - y (that is where the test's real input lies) |
| tp_anova | k >= 2 groups AND you want the FULL ANOVA table (df/SS/MS/F/p per term) + eta_squared = SS_group/SS_total + grand_mean; it presupposes EQUAL variances |
| tp_welch (var_equal = FALSE) | k >= 2 groups with UNEQUAL variances and/or very unequal n_i: Welch (1951) generalises the 2-sample Welch test to arbitrarily many samples; it does NOT give an ANOVA table (it is an htest) |
| tp_welch(var_equal = TRUE) | you want the CLASSICAL F AS A TEST, without the ANOVA table — an identical statistic to tp_anova (pinned in the tests) |
| #251 tn_wilcox / tn_kruskal | normality does NOT hold (#247) or the sample is very small ⇒ the rank-based counterparts of the same designs |
| #35 sandwich (cat 07) | the data ARE time-dependent and inference MUST be done: HAC/Newey-West/clustered SE — NOT a bypass of the gate |

### Output fields

- tp_t_test: a tidy htest -> method/statistic/statistic_name/parameter(df)/p_value/estimate/conf_low/conf_high/conf_level/null_value/stderr/alternative + alpha/reject/decision ∈ {reject_H0, fail_to_reject_H0} + design ∈ {one_sample, two_sample_welch, two_sample_student_pooled, paired} + paired/var_equal/mu/n_used/n_na/na_action/sample_names
- tp_anova: anova_table = {term = c('group','Residuals'), df, sum_sq, mean_sq, f_value, p_value} AS NUMERIC COLUMNS (chart-data) + statistic(F)/parameter(num df, denom df)/p_value/alpha/reject/decision + eta_squared (= SS_group/SS_total) + ss_total/df_residual/grand_mean
- tp_welch: a tidy htest (statistic = F, parameter = num df + a NON-INTEGER Welch-Satterthwaite denom df) + test ∈ {oneway_welch, oneway_f} + var_equal
- tp_anova/tp_welch (shared): levels (CANONICALLY sorted) / k / n / n_na / n_by_group / mean_by_group / sd_by_group / grand_mean / response / group — the per-group chart-data
- ALL: cross_section_gate = {groups, lb_statistic, lb_p_value, lb_lag, n, n_na, gate_alpha, ordered, branch ∈ {ljung-box-tested, skipped-by-declaration}, tested, decision ∈ {pass, pass-untested, pass-unordered}} — the NUMERIC diagnostics of normative gate 4, ALWAYS in the output

### Pitfalls

- NORMATIVE GATE 4 (the normative gate spec §3b) — CROSS-SECTION ONLY: AUTOCORRELATION INFLATES THE TYPE I ERROR (it shrinks the variance estimator) ⇒ spuriously significant p-values. EVERY exported function calls the SHARED gate_cross_section_only (the shared gates module — written ONCE, shared with #251 and #257; NEVER copied). Two branches, BOTH a hard stop: (a) an explicit rejection of the classes ts/mts/msts/xts/zoo/zooreg/irts/timeSeries/tis/its/fts/tsibble/tbl_ts; (b) a Ljung-Box whiteness precheck with lag = min(10, n/5) (the DOCUMENTED default of checkresiduals; Hyndman & Athanasopoulos FPP 3rd ed. §5.4; fitdf = 0 because the input is DATA, not residuals) — a rejection at alpha ⇒ stop. The message points EXPLICITLY at the HAC path: #35 sandwich, cat. 07 (wrap_vcov_hac/wrap_vcov_cl/wrap_vcov_panel). A CONSEQUENCE: the minimum n rises to 3; for n < 5 the rule gives lag < 1 ⇒ an explicit tested = FALSE + decision = 'pass-untested' (NEVER a silent pass)
- gate_alpha (default 0.05) — DECOUPLED FROM THE TEST'S alpha: alpha determines ONLY the reject/decision of the output; the level of the cross-section gate is ITS OWN argument (gate_alpha). WHY: the Ljung-Box precheck is a TEST OF SIZE gate_alpha, so BY CONSTRUCTION it blocks a small share of VALID i.i.d. input (a false block). LIVE-MEASURED (the engine, rnorm, 5000 replications): n=200 -> 1.6%/5.7%/10.1% and n=60 -> 2.3%/6.7%/10.8% for gate_alpha = 0.01/0.05/0.10. With the level tied, a «t-test at 10%» would raise the gate's false-block rate to ~10% WITHOUT any statistical justification
- ordered (default TRUE) — AN EXPLICIT DECLARATION OF ROW ORDER: Ljung-Box is A FUNCTION OF THE ORDER — LIVE-VERIFIED that THE SAME 60 numbers pass unsorted and are BLOCKED sorted (sort), that is, exactly as a cross-section CSV arrives (countries alphabetically, firms by size); t_test/aov/oneway_test are PERMUTATION-INVARIANT. ordered = FALSE ⇒ the user DECLARES that the rows carry no order, the Ljung-Box branch is SKIPPED EXPLICITLY (branch = skipped-by-declaration, decision = pass-unordered, tested = FALSE everywhere) and ALL the structural checks (NaN/Inf, n>=3, zero variance) REMAIN. The time-series class rejection ALWAYS APPLIES (branch: class-rejected). lb_lag TOGETHER WITH ordered = FALSE ⇒ a hard stop (contradictory, it would be a silent no-op)
- WHERE EXACTLY THE GATE RUNS (statistically precise, not mechanical): one-sample -> on x; two-sample -> on x AND y SEPARATELY (each sample has its own mean and variance); paired -> ONLY on the DIFFERENCES d = x - y (autocorrelation that CANCELS in the difference does NOT inflate the paired test's Type I error — a gate on x/y would reject VALID analyses); anova/welch -> PER GROUP (a named list per level)
- ⚠️ A DOCUMENTED LIMIT OF THE GATE: in tp_anova/tp_welch the response column is split into groups BEFORE it reaches the gate, and `[` on a ts returns an UNCLASSED numeric ⇒ the «time-series class» branch does NOT see a ts column inside a data_frame. The SUBSTANTIVE branch (Ljung-Box PER GROUP) stays fully active. In tp_t_test the vector arrives AS IS ⇒ both branches are active (covered in the tests)
- SILENTLY WRONG (THE MOST SERIOUS, live-verified the engine): with a NUMERIC or LOGICAL grouping column aov does NOT do an ANOVA — it does a LINEAR REGRESSION (Df = 1 instead of k-1) WITHOUT any error/warning; oneway_test likewise accepts numeric groups ⇒ a HARD GATE: the column must be a factor or character (convert with factor EXPLICITLY)
- SILENTLY WRONG: t_test on NON-NUMERIC input does NOT error — it emits ONLY warnings («argument is not numeric or logical: returning NA», «NAs introduced by coercion») and returns NA; with muffled warnings (as.tp_call does) it would pass COMPLETELY silently ⇒ a hard input-type gate
- SILENTLY WRONG (INCONSISTENT BEHAVIOUR ACROSS TESTS): with Inf/-Inf/NaN both t_test AND oneway_test do NOT error — they return statistic = NaN / p = NaN (the t_test routine: «no longer errors and returns a still not very useful result»); aov DOES ERROR («NA/NaN/Inf in 'y'») ⇒ ONE uniform policy: a hard stop everywhere
- SILENTLY WRONG: t_test(c(1,2), 3, var.equal = TRUE) does NOT error — the pooled Student test accepts a sample with n = 1 (whose variance is not even defined) and returns a p-value ⇒ n >= 2 is checked PER SAMPLE explicitly; and n_i = 1 in an ANOVA ⇒ df_residual = 0 and the table comes back WITHOUT the «F value»/«Pr(>F)» columns WITHOUT an error (an explicit shape check, not a silent NULL)
- SILENTLY WRONG (ZERO VARIANCE — TWO DIFFERENT POLICIES): tp_welch (zero_var='any'): Welch weights by w_i = n_i/s_i^2 ⇒ ONE SINGLE constant group gives statistic = NaN / p = NaN, and with var_equal=TRUE F = Inf / p = 0; tp_anova (zero_var='all'): if ALL the groups are constant the residual SS is ~1e-31 and aov returns F ~ 1.83e+31, p ~ 4.4e-93 (numerical garbage), or F = NaN if the whole of y is constant. The gate runs BEFORE the shared cross-section gate so that the message is test-specific
- AN EXPLICIT NA POLICY: t_test/aov remove NA SILENTLY (the t_test routine: «Missing values are silently removed (in pairs if paired is TRUE)»; na.omit is the aov default) ⇒ the reported n is NOT the input n and the design's BALANCE is altered. Here: na_action='fail' (the DEFAULT, a hard stop) \| 'omit' (EXPLICIT removal WITH a count: n_na is always in the output; pairs in paired, ROWS in anova/welch)
- NO formula ON THE SURFACE (SECURITY,.claude/rules/security.md): the one-way design has EXACTLY one term, so a formula adds no expressiveness — only attack surface. The user supplies COLUMN NAMES (strings) that are validated with %in% names(data) and used ONLY as a `[[` index; the model's formula is LITERALLY written in the code (.tp_value ~.tp_group). ZERO user-string -> parse/eval path. The ANOVA table is returned with CANONICAL labels term = c('group','Residuals') (+ raw_rownames), so the frontend never sees the internal names
- DETERMINISM (charter §5): NO RNG (closed-form t/F + Welch-Satterthwaite df) ⇒ NO seed. The level order is CANONICAL — sort(unique(g)), NOT order of appearance — and the factor is built EXPLICITLY in that order, so that the ANOVA table, the mean_by_group/sd_by_group and the Welch statistic do NOT depend on the row sorting (pinned in the tests: identical over 2 runs AND over shuffled rows)
- POST-CHECKS (a DEFENSIVE «second net» — with the pre-gates active they are NOT triggered by any public call, which is why they are covered by a DIRECT call in the tests): class 'htest'/'aov'; a finite statistic of length 1; a finite p-value in [0,1]; df_residual >= 1; ALL 5 columns of the ANOVA table present AND EXACTLY 2 rows
- MASKING: NO library — only stats (the the standard library distribution, always attached) ⇒ ZERO new masking surface; conflicts(detail=TRUE) IDENTICAL before/after the source (live-verified) and NO S3 method is registered. Even so, ALL the calls are stats:: qualified (other wrappers in the shared env mask generics). Node layer: x/y as raw_handle (NOT series_handle — it would imply exactly the FORBIDDEN input, and resolve_handle(as='ts') rejects a numeric vector); data as df_handle; response/group/x_name/y_name = NAMES & LABELS, NEVER data. TERMINAL nodes: no register; the fitted aov is NOT returned (it carries terms/call/environment)

### References

- the t_test routine's documentation — «Missing values are silently removed (in pairs if 'paired' is TRUE)»; «if 'var.equal' is FALSE then the variance is estimated separately for both groups and the Welch modification to the degrees of freedom is used»; «'mu' must be a single number»; «'conf_level' must be a single number between 0 and 1»; «not enough 'x' observations»; «data are essentially constant»
- the oneway_test routine's documentation — «If TRUE, then a simple F test for the equality of means in a one-way analysis of variance is performed. If FALSE, an approximate method of Welch (1951) is used, which generalizes the commonly known 2-sample Welch test to the case of arbitrarily many samples»; the aov routine (the one-way design, na.action); summary.aov (Df \| Sum Sq \| Mean Sq \| F value \| Pr(>F))
- Welch, B.L. (1951) «On the Comparison of Several Mean Values: An Alternative Approach», Biometrika 38(3/4), 330, doi:10.2307/2332579 — the reference that the oneway_test routine ITSELF gives for the unequal-variance test
- Ljung, G.M. & Box, G.E.P. (1978) «On a Measure of Lack of Fit in Time Series Models», Biometrika 65(2), 297-303, doi:10.1093/biomet/65.2.297 — the whiteness precheck of the shared gate; the Box.test routine's documentation Note: «Missing values are not handled» (which is why the gate blocks NaN/Inf itself)
- Hyndman, R.J. & Athanasopoulos, G., «Forecasting: Principles and Practice», 3rd ed., §5.4 — the rule lag = min(10, n/5); IDENTICAL to the DOCUMENTED default of checkresiduals (live-verified help: «If missing, it is set to min(10, n/5) for non-seasonal data, and min(2m, n/5) for seasonal data»). Cross-section ⇒ there is no seasonal period m ⇒ the 2m branch never applies
- the normative gate spec §3b normative gate 4 (cross-section-only for t-test/ANOVA/Wilcoxon/KW/Friedman/chi-square; «to be written ONCE as a shared helper, not 3 times») + the live-verified gates «t_test: not enough 'x' observations · data are essentially constant»
- .claude/rules/security.md (the eval(parse) PROHIBITION — why no formula is exposed) + CLAUDE.md §5 (charts only in the frontend; blocked-by-gate as a first-class state)
- wrapper footers IMPLEMENTATION NOTE (c01_preparation_prechecks/battery_parametric_mean and the shared gates module) — EVERY silently-wrong case is live-verified on the engine with the EXACT messages/values (aov as a linear regression with numeric groups; F ~ 1.83e+31 / p ~ 4.4e-93 under zero variances; an ANOVA table without F/Pr(>F) when df_residual = 0)

## #251 — Battery of NON-PARAMETRIC (rank-based) tests on CROSS-SECTION data: Wilcoxon signed rank (one sample / paired) & rank sum = Mann-Whitney (two independent) with an optional non-parametric CI + Hodges-Lehmann · Kruskal-Wallis (k >= 2 independent groups) · Friedman (unreplicated complete block design)

**Module:** `battery_non_parametric.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `tn_wilcox` | `x` | `raw_handle`, `raw_handle`, `boolean`, `number`, `enum`, `boolean`, `boolean`, `boolean`, `number`, `number`, `enum`, `integer`, `number`, `boolean` | `paired=False`, `mu=0`, `correct=True`, `conf_int=False`, `conf_level=0.95`, `gate_alpha=0.05`, `ordered=True` | `light` | — |
| `tn_kruskal` | `x` | `raw_handle`, `enum`, `integer`, `number`, `boolean` | `gate_alpha=0.05`, `ordered=True` | `light` | — |
| `tn_friedman` | `y` | `raw_handle`, `series_codes`, `series_codes`, `enum`, `integer`, `number`, `boolean` | `gate_alpha=0.05`, `ordered=True` | `light` | — |

### Use when

the rank-based COUNTERPARTS of the parametric battery #250, when NORMALITY does NOT hold (#247 nortest) or the sample is very small: TWO independent groups of countries/firms -> tn_wilcox (rank sum / Mann-Whitney); BEFORE/AFTER on the SAME units -> tn_wilcox(paired=TRUE) (signed rank of the differences); k >= 2 INDEPENDENT groups -> tn_kruskal (non-parametric one-way ANOVA); k methods/treatments MEASURED ON THE SAME blocks (e.g. 3 forecasting methods x 6 countries) -> tn_friedman (non-parametric repeated measures)

### Do not use when

TIME SERIES or time-dependent data — a HARD GATE (§3b normative gate 4); the HAC path: #35 sandwich (cat. 07-causality-policy); normality DOES hold and you want MORE power / an ANOVA table / eta^2 -> #250 tests-parametric; TWO CATEGORICAL variables (a contingency table, chi-squared/Fisher/Cramer V) -> #257 categorical-assoc; a normality DECISION -> #247 nortest / #1 Jarque-Bera; a Friedman test WEIGHTED by the block range (quade_test) — NOT exposed (a DIFFERENT test, its own card if requested); an INCOMPLETE / REPLICATED block design (Friedman requires EXACTLY one observation per (block, group)); charts (the frontend, §5 — the node supplies rank_means/rank_sums/within_block_ranks as NUMBERS)

### Prerequisites

- c01_preparation_prechecks/battery_normality_edf.nt_normality_battery # (#247) you come HERE when normality was REJECTED or n is very small
- c01_preparation_prechecks/profiling_quality_report.dp_quality_flags # (#248) constant/infinite_values/few_rows — exactly the gates that will block here

### Alternatives

| instead use | when |
| --- | --- |
| tn_wilcox (y = NULL) | ONE sample: signed rank; H0 = the distribution of x is SYMMETRIC about mu |
| tn_wilcox (y given, paired = FALSE) | TWO INDEPENDENT samples: rank sum / Mann-Whitney; H0 = the distributions differ by a location shift equal to mu |
| tn_wilcox (paired = TRUE) | PAIRED measurements on the SAME units (EQUAL lengths); equivalent to the signed rank of the differences — the NA are removed PAIRWISE |
| tn_wilcox(conf_int = TRUE) | you want a MAGNITUDE, not only a p-value: a non-parametric CI + the Hodges-Lehmann estimator (pseudomedian or difference in location). ⚠️ At small n the ACHIEVED level differs from the requested one (conf_level_achieved) and the interval may come out infinite (conf_int_finite) |
| tn_kruskal | k >= 2 INDEPENDENT groups (list/matrix/data_frame): H0 = the same location parameter in every group; df = k-1 |
| tn_friedman | the k groups are NOT independent: they were ALL measured in EVERY block (country/unit); the ranks are computed WITHIN a block ⇒ the block effect is removed. WIDE (blocks x groups) or LONG (y + groups + blocks) |
| #250 tp_t_test / tp_anova / tp_welch | normality DOES hold: more power, an ANOVA table, eta^2 and confidence intervals for the means |
| #257 ca_chisq / ca_fisher | NEITHER of the two variables is continuous — two CATEGORICAL answers per unit ⇒ a contingency table, not a comparison of medians |
| #35 sandwich (cat 07) | the data ARE time-dependent and inference MUST be done: HAC/clustered SE — NOT a bypass of the gate |

### Output fields

- SHARED: tests = a ONE-row tidy record (test/method/statistic_name/statistic/(df)/p_value/alternative/n_*/n_omitted/exact_used/normal_approximation/ties_present…) + the same fields also as atomic scalars
- tn_wilcox: test ∈ {rank_sum, signed_rank_one_sample, signed_rank_paired} + statistic (W or V) + p_value + mu + rank_means/rank_sums/group_sizes (chart-data: groups 'x','y' in the rank sum; 'positive','negative','zero' in the signed rank) + n_x/n_y/n_omitted
- tn_wilcox (exact/asymptotic transparency): exact_requested / exact_used / normal_approximation / continuity_correction (READ FROM the stats method string ITSELF) + ties_present + zeroes_present
- tn_wilcox (conf_int = TRUE): conf_int + conf_level (REQUESTED) + conf_level_achieved (attr 'conf_level') + conf_int_finite + estimate/estimate_name (Hodges-Lehmann)
- tn_kruskal: statistic (Kruskal-Wallis chi-squared) + df (= k-1) + p_value + rank_means/rank_sums/group_sizes PER GROUP (chart-data) + groups/n_groups/n_total/n_omitted/ties_present
- tn_friedman: statistic (Friedman chi-squared) + df (= k-1) + p_value + rank_means/rank_sums (WITHIN-BLOCK ranks per group — chart-data) + within_block_ranks (a blocks x groups NUMERIC matrix) + groups/blocks/n_groups/n_blocks/n_blocks_dropped + input_form ∈ {wide, long}
- ALL: cross_section_gate = {groups, statistic, p_value, lag, n, n_na, gate_alpha, ordered, branch ∈ {ljung-box-tested, skipped-by-declaration}, tested, decision ∈ {pass, pass-untested, pass-unordered}} — the NUMERIC diagnostics of normative gate 4

### Pitfalls

- NORMATIVE GATE 4 (the normative gate spec §3b) — CROSS-SECTION ONLY: all three tests presuppose INDEPENDENT observations; autocorrelation INFLATES THE TYPE I ERROR ⇒ spuriously significant p-values. The rule is implemented ONCE in the SHARED gate_cross_section_only (the shared gates module; shared with #250 and #257) and is CALLED here — NEVER copied: (a) an explicit rejection of ts/mts/msts/xts/zoo/zooreg/tsibble/… and (b) a Ljung-Box whiteness precheck with lag = min(10, n/5) (the DOCUMENTED default of checkresiduals; Hyndman & Athanasopoulos FPP 3rd ed. §5.4). The message points EXPLICITLY at the HAC path: #35 sandwich, cat. 07 (wrap_vcov_hac/wrap_vcov_cl/wrap_vcov_panel). ⚠️ LIVE-VERIFIED: friedman_test accepts a matrix of class mts WITHOUT COMPLAINT — ONLY the gate stops it. A CONSEQUENCE: the minimum n PER GROUP rises to 3 (stricter than stats, DELIBERATELY)
- gate_alpha (default 0.05) — THE LEVEL BELONGS EXCLUSIVELY TO THE GATE: the three non-parametric tests have no alpha of their own (no decision column), which is why the argument is called gate_alpha and NOT alpha. The precheck is a TEST OF SIZE gate_alpha ⇒ by construction it blocks a small share of VALID i.i.d. input; LIVE-MEASURED (the engine, rnorm, 5000 replications): n=200 -> 1.6%/5.7%/10.1%, n=60 -> 2.3%/6.7%/10.8% for 0.01/0.05/0.10
- ordered (default TRUE) — AN EXPLICIT DECLARATION OF ROW ORDER: Ljung-Box depends on the ORDER (live-verified: the same 60 numbers pass unsorted and are blocked once sorted) whereas wilcox_test/kruskal_test/friedman_test are PERMUTATION-INVARIANT (Friedman with respect to the order of the BLOCKS). ordered = FALSE ⇒ an explicit omission of Ljung-Box (branch = skipped-by-declaration, decision = pass-unordered), with ALL the structural checks and the time-series class rejection (branch: class-rejected) ACTIVE. lb_lag together with ordered = FALSE ⇒ a hard stop
- WHY NO as_numeric BEFORE THE GATE: the CLASS of the input must survive INTACT up to the gate (it is the SOLE owner of the rule «reject ts/xts/zoo»); that is why the gate comes LAST before the test and the conversion happens AFTER. ⚠️ A KNOWN LIMITATION: when na_action='omit'/'drop_blocks' REMOVES values, the subset loses its class ⇒ a ts WITH NA + an explicit omit is checked only by the Ljung-Box branch; in the LONG form of tn_friedman the gate sees the RESHAPED wide matrix (correct: a stacked long vector is NOT a time series)
- AN INCONSISTENT documented policy FOR NON-FINITE VALUES (live-verified): the wilcox_test routine says of x/y «Non-finite (e.g., infinite or missing) values will be omitted» — but in the TWO-SAMPLE branch the Inf values are KEPT as «very large» (the release notes) ⇒ THE SAME Inf changes meaning depending on the branch. A hard gate: NO Inf/-Inf in any input
- AN EXPLICIT NA POLICY: wilcox_test/kruskal_test remove NA SILENTLY (live-verified: kruskal_test(list(c(x,NA), y)) runs normally) and friedman_test removes WHOLE BLOCKS (documentation: «if y contains NAs, corresponding blocks are removed») ⇒ silent data loss. Here: na_action='fail' (the DEFAULT hard stop) \| 'omit' (wilcox/kruskal — PAIRWISE in paired) \| 'drop_blocks' (friedman), ALWAYS with a count (n_omitted / n_blocks_dropped) and a check that >= 2 blocks remain
- A DOCUMENTED CHANGE IN the reference >= 4.6.0 (A DEPARTURE FROM OLD KNOWLEDGE, live-verified): there is no longer a silent fallback to the normal approximation with the warning «cannot compute exact p-value with ties» — «If there are ties, exact inference is performed using the conditional/permutation distribution given the observed ranks, using an implementation of the Streitberg-Röhmel shift algorithm» (the wilcox_test routine; the reference NEWS 4.6.0, contributed by Torsten Hothorn). The node EXPOSES IT anyway as FIELDS (exact_used/normal_approximation/continuity_correction read FROM the method string; the release notes: «If exact computations are used, the result now has 'exact' in the method element») ⇒ if a future version falls back again, IT IS VISIBLE in the JSON instead of hidden
- THE SAME SAMPLE, TWO V VALUES (a live finding, the engine): in the signed rank with ZERO differences stats builds the statistic in TWO WAYS — exact: r <- rank(abs(x)); V <- sum(r[x > 0]) (the zeros INSIDE the ranking); asymptotic: if (ZERO) x <- x[x != 0] FIRST (the zeros OUTSIDE). MEASURED: x = c(.6,1,1.4,.5,1.3,1.2,1.3,1.9), mu = 1 -> V = 22 (exact) vs 17 (exact=FALSE). The node exposes zeroes_present + exact_used TOGETHER AND builds rank_means/rank_sums BY THE PATH THAT ACTUALLY RAN
- A POST-CHECK OF THE IDENTITY chart-data <-> statistic (if it breaks, the frontend would draw NUMBERS OTHER than the p-value ⇒ a hard stop): tn_wilcox two-sample: rank_sums['x'] - n_x(n_x+1)/2 == W (the reference SUBTRACTS the m(m+1)/2 — the wilcox_test routine Note: «the engine subtracts»); tn_wilcox signed rank: rank_sums['positive'] == V; tn_kruskal: sum(rank_sums) == N(N+1)/2; tn_friedman: sum(rank_sums) == n_blocks*k(k+1)/2. The ranks are reproduced EXACTLY as stats builds them (the same signif(digits_rank); the same c(x - mu, y) in the two-sample case)
- SILENTLY WRONG DEGENERACIES (live-verified, all hard-gated): ALL differences from mu zero -> the signed rank degenerates to V = 0, p = 1 WITHOUT an error; a completely constant pooled sample -> rank sum p = 1 / kruskal_test chi-squared = NaN & p = NaN WITHOUT an error (a 0/0 division in the tie correction); EVERY block with identical values -> friedman_test NaN/NaN WITHOUT an error
- A SILENT DROP BY stats THAT IS AVOIDED STRUCTURALLY: kruskal_test documents «g is ignored with a warning if x is a list» ⇒ here the input is ALWAYS NORMALISED to a named list of groups (list/matrix/data_frame accepted), so that g can NEVER be ignored silently. Group names: NON-EMPTY and UNIQUE
- FRIEDMAN = AN UNREPLICATED COMPLETE BLOCK DESIGN (documentation: «exactly one observation in y for each combination of levels of groups and blocks») ⇒ our own gates in the LONG form: NO REPLICATION and NO EMPTY (block, group) combination; >= 2 columns AND >= 2 rows (otherwise stats throws the cryptic «dim(X) must have a positive length»); NA/empty labels are forbidden («NAs are not allowed in 'groups' or 'blocks'»). The ranks are WITHIN-BLOCK — they are NOT compared across blocks
- CONF.INT ONLY WHERE IT IS DOCUMENTED: conf_int/conf_level exist ONLY in tn_wilcox — kruskal_test/friedman_test do NOT document conf.int/estimate and nothing is invented. A live-verified trap: at small n the ACHIEVED level differs from the requested one (0.95 -> 0.9609375) and the interval may come out (-Inf, Inf) WITHOUT a warning ⇒ conf_level / conf_level_achieved / conf_int_finite are exposed EXPLICITLY
- digits_rank: if finite, the ranks are computed on signif(r, digits_rank) — it stabilises tie detection when differences of order 1e-16 hide them (the wilcox_test routine: «For stability reasons, it may be advisable to use rounded data or to set digits.rank = 7»). correct is exposed ONLY as a logical: the INTEGER form 0-3 (Edgeworth terms) is NOT recorded in the method string (live-verified: correct=2 gives THE SAME «with continuity correction») ⇒ the output would be UNVERIFIABLE, and the adapters kind 'number' would turn TRUE into 1 = «1 Edgeworth term» (a silent change of meaning)
- DETERMINISM (charter §5): NO RNG path — no seed, no Monte-Carlo/permutation simulation. The exact distributions are closed-form (psignrank/pwilcox) or, under ties, the DETERMINISTIC Streitberg-Röhmel shift algorithm; identical over 2 runs is pinned in the tests (the wrapper AND the node path)
- MASKING / HANDLES: NO library — only base+stats (always attached) ⇒ ZERO masking, but ALL the calls are stats::/base:: qualified (other wrappers in the shared source env mask generics: proxy -> as_matrix/dist; sn -> sd; ARIMA -> ARIMA). Node layer: ALL the data as raw_handle (NOT matrix_handle/num_array) — resolve_handle(as='raw') returns the object AS IS so that the CLASS reaches the gate INTACT (with matrix_handle the gate would be BLINDED); groups/blocks = LABELS (series_codes), not data. TERMINAL nodes: no register/chaining

### References

- the wilcox_test routine's documentation — «Non-finite (e.g., infinite or missing) values will be omitted»; «By default (if exact is not specified), an exact p-value is computed if the samples contain less than 50 finite values»; «If there are ties, exact inference is performed using the conditional/permutation distribution given the observed ranks, using an implementation of the Streitberg-Röhmel shift algorithm … contributed by Torsten Hothorn»; «For stability reasons, it may be advisable to … set digits.rank = 7»; Note «the sum of the ranks of the first sample with the minimum value (m(m+1)/2 …) subtracted or not: the engine subtracts»; «With small samples it may not be possible to achieve very high confidence interval coverages»
- the kruskal_test routine's documentation — «If x is a list, its elements are taken as the samples to be compared»; «g: … Ignored with a warning if x is a list»; the friedman_test routine — «friedman_test can be used for analyzing unreplicated complete block designs (i.e., there is exactly one observation in y for each combination of levels of groups and blocks)»; «If y is a matrix, groups and blocks are obtained from the column and row indices»; «NAs are not allowed in 'groups' or 'blocks'; if y contains NAs, corresponding blocks are removed»
- Streitberg, B. & Röhmel, J. (1986) «Exact Distributions for Permutation and Rank Tests», Statistical Software Newsletter 12(1), 10-17; (1987) «Exakte Verteilungen für Rang- und Randomisierungstests im allgemeinen c-Stichprobenfall», EDV in Medizin und Biologie 18(1), 12-19 — the DETERMINISTIC shift algorithm that stats uses under ties (Rs given by the wilcox_test routine)
- Hollander, M. & Wolfe, D.A. (1973) «Nonparametric Statistical Methods», Wiley, pp. 27-33 (one sample) / 68-75 (two samples) — the definition of the pseudomedian (p. 34) that conf_int = TRUE returns; Bauer, D.F. (1972) «Constructing Confidence Sets Using Rank Statistics», JASA 67(339), 687-690 — the exact CI algorithm (Rs given by the wilcox_test routine)
- Ljung, G.M. & Box, G.E.P. (1978) «On a Measure of Lack of Fit in Time Series Models», Biometrika 65(2), 297-303, doi:10.1093/biomet/65.2.297 — the whiteness precheck of the shared gate; the Box.test routine's documentation Note: «Missing values are not handled»
- Hyndman, R.J. & Athanasopoulos, G., «Forecasting: Principles and Practice», 3rd ed., §5.4 — the rule lag = min(10, n/5); IDENTICAL to the DOCUMENTED default of checkresiduals (live-verified help: «If missing, it is set to min(10, n/5) for non-seasonal data»); cross-section ⇒ never the 2m branch
- the normative gate spec §3b normative gate 4 (cross-section-only for t-test/ANOVA/Wilcoxon/KW/Friedman/chi-square; a shared helper ONCE) + «gate: friedman_test requires a matrix/blocks («argument "groups" is missing»)» (docs/catalog/merge-wrapper.md, the node's row)
- wrapper footers IMPLEMENTATION NOTE (c01_preparation_prechecks/battery_non_parametric and the shared gates module) — the live-verified findings on the engine: mts accepted by friedman_test; exact vs asymptotic V = 22 vs 17; NaN/NaN on constant data; conf_level 0.95 -> 0.9609375; correct=2 invisible in the method string
