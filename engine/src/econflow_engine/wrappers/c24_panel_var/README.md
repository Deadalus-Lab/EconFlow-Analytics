<!-- SPDX-License-Identifier: AGPL-3.0-only -->
# 24-panel-var

1 METHOD-SELECTION card, 1 module, 4 nodes.

Every card below governs one wrapper module in this package. The cards are the
reason a method exists here at all: they record when it applies, what to reach
for instead, and the traps that make its output easy to misread.

## #230 — Heterogeneous-panel VAR/SVAR: (P)MG estimation, panel cointegration rank tests, structural identification (+MG-IRF/MG-FEVD), bootstrap IRF confidence bands

**Module:** `heterogeneous_panel_var.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `pv_estimate` | `df`, `variables`, `lags` | `df_handle`, `series_codes`, `integer`, `string`, `enum`, `string`, `integer`, `integer`, `integer` | `id_col='id'` | `light` | `fit` |
| `pv_cointegration` | `df`, `variables`, `lags` | `df_handle`, `series_codes`, `integer`, `enum`, `string`, `enum`, `integer` | `id_col='id'` | `light` | — |
| `pv_identify` | `fit` | `raw_handle`, `enum`, `integer`, `integer`, `raw`, `string`, `df_handle`, `enum`, `enum`, `raw`, `raw`, `integer`, `integer` | `n_ahead=20`, `fevd_ahead=10`, `seed=1` | `light` | `fit` |
| `pv_bootstrap` | `fit` | `raw_handle`, `enum`, `integer`, `integer`, `integer`, `int_array`, `string`, `number`, `integer` | `n_ahead=20`, `n_boot=100`, `b_length=1`, `b_dim=[1, 1]`, `level=0.9`, `seed=1` | `heavy` | — |

### Use when

a panel of N individuals × K macro variables (heterogeneous, a common lag p) -> a (pooled) mean-group panel VAR or a rank-restricted VECM; testing the panel cointegration rank (combining the K×N individual statistics); structural identification (recursive/ICA/proxy/long-run) with an MG-IRF & MG-FEVD; confidence bands through a panel/individual moving-block bootstrap or mean-group inference

### Do not use when

a single time series/individual (a single-country VAR/SVAR -> cat 03/04); a micro-panel regression without VAR dynamics (plm #46-47); a pure cross-section with no time dimension; data ingestion (a file upload — a frontend route, not a node)

### Alternatives

| instead use | when |
| --- | --- |
| pv_estimate (model=VAR) | a stationary/level panel -> a mean-group VAR in levels (Canova-Ciccarelli 2013; Pesaran-Smith 1995 MG) |
| pv_estimate (model=VEC, dim_r) | a cointegrated panel of known rank r -> a (pooled) mean-group rank-restricted VECM (Pesaran-Shin-Smith 1999 PMG; Breitung 2005) |
| pv_cointegration (test=JO/BR/SL/CAIN) | an unknown cointegration rank -> a panel rank test (JO=the Johansen trace panel test; BR=Breitung pooled; SL=Saikkonen-Luetkepohl; CAIN=Arsova-Oersal); RUN IT BEFORE model=VEC in order to choose r |
| pv_identify (method=chol/cvm/dc/iv/grt) | structural shocks: chol=recursive (a known causal ordering); cvm/dc=statistical ICA (non-gaussian shocks); iv=external instruments/a proxy; grt=long/short-run restrictions on an SVEC; -> an MG-IRF (Gambacorta et al. 2014) + an MG-FEVD |
| pv_bootstrap (method=pmb/mg/mb) | IRF confidence bands: pmb=a panel moving-block bootstrap (full inference); mg=the mean-group spread over the N individuals (fast, no bootstrap); mb=an individual moving-block bootstrap for one selected individual |

### Output fields

- pv_estimate: A (the lined-up MG coefficient matrices), beta (the cointegrating matrix; VEC), dim_K/dim_N/dim_r, individuals, variables, estimator; fit=pvarx (register -> a raw_handle, a to_mcp stub)
- pv_cointegration: panel_stats & panel_pvals (matrices: rows=the combination methods LRbar/Choi_P/Choi_Pm/Choi_Z, columns=r_H0=0.K-1), individual_stats/pvals, ranks_tested, combination_tests, csd_present
- pv_identify: B (the (K×S) structural impact matrix, MG), irf (a data_frame V1=horizon + impulse->response columns), fevd_mg (a named list per response variable; the matrices sum to ~100 per row under full identification), shock_names; fit=pid (register -> a raw_handle)
- pv_bootstrap: irf_point/irf_lower/irf_upper (data.frames V1 + impulse->response columns; the quantiles (1-level)/2 and 1-(1-level)/2), n_boot (actual), level, horizon, impulse_response, individual (mb)

### Pitfalls

- pcoint.BR FAILS with the default VECTOR type ('condition has length > 1'); the wrapper enforces a scalar type through match.arg; SL/CAIN ignore det_case and use 'SL_trend'
- a panel-level fevd(pid) is NOT defined (fevd.id works per individual only); fevd_mg is the mean group of the individual FEVDs; under partial identification (iv, S!=K) the rows do NOT necessarily sum to 100
- the MG-IRF (irf.pvarx, MG_IRF=TRUE by default) = the average of the INDIVIDUAL IRFs (Gambacorta et al. 2014); NOT the IRF of the mean-group VAR — a different quantity
- recursive-design bootstrap bands (pmb/mb) do NOT necessarily contain the point estimate (a small-sample bias); mg gives the spread across the N individuals, NOT a genuine bootstrap
- cvm/dc identification is STOCHASTIC (DEoptim/steadyICA); the pmb/mb bootstraps are too; determinism comes from seeding (identical confirmed); chol/mg use no RNG
- chaining: pv_estimate.fit (pvarx) -> pv_identify.fit (pid) -> pv_bootstrap; pv_identify requires an UNIDENTIFIED pvarx (it blocks an already-identified pid); pv_bootstrap requires a pid; grt requires a VEC fit
- MASKING: pvars Depends on svars->vars; use requireNamespace + pvars::/vars:: (NOT library) so that the shared global search path is not polluted (irf/fevd/plot/summary/as.Date/kronecker)

### References

- pvars v1.1.1 ref manual (the pvarx.VAR/VEC, pcoint.JO/BR/SL/CAIN, pid.chol/cvm/dc/iv/grt, irf.pvarx, fevd.id, sboot.mg/pmb/mb help pages)
- Canova & Ciccarelli 2013 'Panel Vector Autoregressive Models: A Survey' Advances in Econometrics 32, 205-246
- Pesaran & Smith 1995 'Estimating Long-Run Relationships from Dynamic Heterogeneous Panels' J. Econometrics 68, 79-113 (mean group)
- Pesaran, Shin & Smith 1999 'Pooled Mean Group Estimation of Dynamic Heterogeneous Panels' JASA 94, 621-634 (PMG); Breitung 2005 Econometric Reviews 24, 151-173 (two-step panel cointegration)
- Gambacorta, Hofmann & Peersman 2014 JMCB 46, 615-642 (the mean-group IRF); Herwartz & Wang 2024 J. Applied Econometrics 39(4), 620-639 (panel ICA identification)
- Mertens & Ravn 2013 AER 103, 1212-1247 & Jentsch & Lunsford 2021 JBES 40, 1876-1891 (the proxy SVAR); Empting et al. 2025 (the panel proxy SVAR); Kilian 1998 REStat 80, 218-230 (bootstrap-after-bootstrap)
- wrapper footer IMPLEMENTATION NOTE (c24_panel_var/heterogeneous_panel_var)
