<!-- SPDX-License-Identifier: AGPL-3.0-only -->
# 28-trade-gravity

3 METHOD-SELECTION cards, 3 modules, 11 nodes.

Every card below governs one wrapper module in this package. The cards are the
reason a method exists here at all: they record when it applies, what to reach
for instead, and the traps that make its output easy to misread.

## #237 — Gravity models of bilateral trade (OLS / PPML / importer-exporter fixed effects / Bonus vetus OLS / Head-Mayer-Ries tetrads)

**Module:** `gravity_bilateral_trade.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `gr_ppml` | `df`, `dependent_variable`, `distance` | `df_handle`, `string`, `string`, `series_codes`, `boolean` | `robust=False` | `light` | — |
| `gr_ols` | `df`, `dependent_variable`, `distance`, `income_origin`, `income_destination`, `code_origin`, `code_destination` | `df_handle`, `string`, `string`, `string`, `string`, `string`, `string`, `series_codes`, `boolean`, `boolean` | `uie=False`, `robust=False` | `light` | — |
| `gr_fixed_effects` | `df`, `dependent_variable`, `distance`, `code_origin`, `code_destination` | `df_handle`, `string`, `string`, `string`, `string`, `series_codes`, `boolean` | `robust=False` | `light` | — |
| `gr_bvu` | `df`, `dependent_variable`, `distance`, `income_origin`, `income_destination`, `code_origin`, `code_destination` | `df_handle`, `string`, `string`, `string`, `string`, `string`, `string`, `series_codes`, `boolean` | `robust=False` | `light` | — |
| `gr_tetrads` | `df`, `dependent_variable`, `distance`, `code_origin`, `code_destination`, `filter_origin`, `filter_destination`, `additional_regressors` | `df_handle`, `string`, `string`, `string`, `string`, `string`, `string`, `series_codes`, `boolean` | `multiway=False` | `light` | — |

### Use when

a bilateral (dyadic) trade panel/cross-section {origin, destination, flow, distance, (GDPs), (dummies)} and you want to estimate the elasticity of trade with respect to distance/income/trade-cost proxies -> choose the estimator according to how you handle the Multilateral Resistance (MR) terms and the zero flows

### Do not use when

a univariate/time series with no dyadic structure; input-output/networks (#48-55); a plain panel OLS/FE with no gravity structure (#46-47 plm); censored/tobit trade (gpml/tobit — separate cards); data ingestion (a file upload — a frontend route, not a node)

### Alternatives

| instead use | when |
| --- | --- |
| gr_ppml (Poisson PML, Santos Silva & Tenreyro 2006) | the flow contains ZEROS and/or heteroskedasticity; you want consistent estimates in the multiplicative form (the log-of-gravity critique) — the default-safe estimator; supply the incomes ALREADY logged as additional_regressors |
| gr_ols (log-log OLS, no MR terms) | you want the traditional log-log gravity with explicit income regressors; ONLY if flow>0 everywhere (no zeros) and you do not care about the MR bias (Anderson-van Wincoop) — a baseline/comparison |
| gr_fixed_effects (importer + exporter FE, Feenstra 2002) | you want to absorb ALL the monadic/MR terms with country dummies (theoretically consistent in a cross-section); the unilateral GDPs are no longer estimated — for a clean estimate of dyadic trade-cost elasticities |
| gr_bvu (Bonus vetus OLS, Baier & Bergstrand 2009/2010) | you want MR-consistent estimates WITH comparative statics preserved (a first-order log-linear Taylor MR approximation through simple averages) — when you need counterfactuals that FE do not allow |
| gr_tetrads (Head-Mayer-Ries 2010, the ratio of ratios) | you want to eliminate the monadic effects without dummies through a reference exporter+importer (a ratio of ratios); it requires >=1 dyadic regressor; multiway=TRUE for multi-way clustered SEs (Cameron-Gelbach-Miller 2011) |

### Output fields

- coefficients: a tidy data_frame {term, estimate, std_error, statistic, p_value} (rlm robust => p_value=NA; a multiway coeftest => 4 columns with p_value)
- distance_term / distance_coef: the name and value of the elasticity with respect to (logged) distance — the central gravity result
- fitstats: named numeric {n_obs, r_squared, adj_r_squared, sigma, log_lik, aic, bic, deviance, null_deviance, pseudo_r2, df_residual} (NA where undefined; pseudo_r2=1-dev/null.dev only for glm/ppml)
- method / fit_class / robust + method-specific flags (family, accepts_zeros, uie, mr_terms, fixed_effects, method_family, multiway, filter_origin, filter_destination)
- fit: the raw fitted object (glm/lm/rlm/coeftest; to_mcp -> a stub)

### Pitfalls

- distance & (for OLS/FE/BVU/tetrads) the dependent variable and the incomes are logged AUTOMATICALLY -> they must be STRICTLY POSITIVE; non-positive values are dropped SILENTLY (log=NaN/-Inf, verified: gravity_zeros 500->355 observations with no warning) -> hard gates; for zero flows use gr_ppml (>=0)
- gr_ols with uie=TRUE (unitary income elasticities) is BROKEN in gravity 1.1 (a package bug: the formula refers to inc_o_log/inc_d_log, which the uie path does not create -> 'object inc_o_log not found', verified live) -> HARD-GATED; the only working value is uie=FALSE (explicit income regressors)
- robust=TRUE => rlm: its summary gives 3 columns (Value/Std.Error/t) with NO p-value -> p_value=NA in coefficients (expected, not an error)
- gr_tetrads requires >=1 additional_regressor (dyadic, e.g. rta/contig); NULL -> a cryptic dplyr join error (verified) -> a gate; filter_origin/filter_destination must EXIST as codes in the code columns
- gr_ppml: quasipoisson/a log link => AIC/log_lik are NA (quasi-likelihood); use pseudo_r2 (1-deviance/null.deviance), not r_squared
- gr_fixed_effects: the unilateral GDPs are absorbed by the country FE and are NOT estimated -> do not ask for them as coefficients; only the dyadic terms (distance + additional_regressors) are interpretable
- the estimators are DETERMINISTIC given the data (OLS/IRLS/rlm/cluster.vcov) -> NO seed; identical across two runs confirmed
- nls masks nls in the shared source env -> the wrapper does NOT call library(gravity); requireNamespace + gravity:: everywhere

### References

- gravity v1.1 (Wölwer, Burgard, Kunst) ref manual — the ppml/ols/fixed_effects/bvu/tetrads help pages + References
- Silva JMCS & Tenreyro S (2006) 'The Log of Gravity' Review of Economics and Statistics 88(4) 641-658 doi:10.1162/rest.88.4.641 (PPML)
- Feenstra RC (2002) 'Border effects and the gravity equation: consistent methods for estimation' Scottish Journal of Political Economy 49(5) 491-506 (fixed effects)
- Baier SL & Bergstrand JH (2009) 'Bonus vetus OLS: a simple method for approximating international trade-cost effects using the gravity equation' Journal of International Economics 77(1) 77-85 doi:10.1016/j.jinteco.2008.10.004; Baier & Bergstrand (2010) Cambridge University Press ch.4 (BVU)
- Head K, Mayer T & Ries J (2010) 'The erosion of colonial trade linkages after independence' Journal of International Economics 81(1) 1-14 doi:10.1016/j.jinteco.2010.01.002 (tetrads)
- Head K & Mayer T (2014) 'Gravity Equations: Workhorse, Toolkit, and Cookbook' Handbook of International Economics vol 4, 131-195 (a survey); Anderson JE & van Wincoop E (2003) 'Gravity with Gravitas' (the MR terms)
- wrapper footer IMPLEMENTATION NOTE (c28_trade_gravity/gravity_bilateral_trade) — live-verified traps (the uie bug, the silent row drop, the tetrads join, the nls masking)

## #238 — Penalized Poisson PML gravity with high-dimensional fixed effects (an HDFE PPML baseline; a single-lambda lasso/ridge/plugin; a lasso/ridge path + a BIC-selected lambda)

**Module:** `penalized_poisson_pml.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `pp_hdfeppml` | `data`, `dep`, `indep`, `fixed` | `df_handle`, `string`, `series_codes`, `raw`, `series_codes`, `number`, `number` | `tol=1e-08`, `hdfetol=0.0001` | `light` | — |
| `pp_penhdfeppml` | `data`, `dep`, `indep`, `fixed`, `lambda` | `df_handle`, `string`, `series_codes`, `raw`, `number`, `enum`, `boolean`, `series_codes`, `number` | `plugin=False`, `hdfetol=0.0001` | `light` | — |
| `pp_mlfitppml` | `data`, `dep`, `indep`, `fixed` | `df_handle`, `string`, `series_codes`, `raw`, `num_array`, `enum`, `boolean`, `boolean`, `series_codes`, `integer`, `number` | `plugin=False`, `post=False`, `seed=1`, `hdfetol=0.0001` | `light` | — |

### Use when

structural gravity on ONE long bilateral-trade panel (exporter x importer x [time]): PPML estimation with several HDFE (exporter-time, importer-time, pair) and MANY dummy regressors (e.g. trade-agreement provisions) -> baseline coefficients (pp_hdfeppml); penalized selection of a relevant subset (pp_penhdfeppml at a single lambda; pp_mlfitppml over a path + BIC, or a plugin lasso)

### Do not use when

log-OLS gravity on positive flows only (Santos Silva-Tenreyro: biased under heteroskedasticity/zeros); few regressors with no need for variable selection (use fepois/feglm, #33); economic complexity/ECI-PCI (#237); a non-count/negative dependent variable; time-series gravity without a dyadic panel; data ingestion (a file upload — a frontend route, not a node)

### Alternatives

| instead use | when |
| --- | --- |
| pp_hdfeppml | you want the (unpenalized) HDFE PPML gravity baseline: coefficients + robust/cluster SE + deviance/BIC, with no variable selection |
| pp_penhdfeppml (penalty=lasso/ridge, lambda) | you want a penalized fit at ONE known lambda: lasso (L1, it zeroes out/selects) or ridge (L2, shrinkage without zeroing) |
| pp_penhdfeppml (plugin=TRUE, cluster) | you want a plugin lasso with data-driven coefficient-specific penalty loadings (Breinlich et al. 2021); it REQUIRES a cluster |
| pp_mlfitppml (lambdas, penalty) | you want the WHOLE penalization path over a vector of lambdas and automatic selection of the lambda that MINIMISES the BIC (+ optional post-lasso de-biasing) |
| pp_mlfitppml (plugin=TRUE, cluster) | you want the plugin lasso through the path API (it ignores lambdas and returns the plugin-selected fit); it REQUIRES a cluster |

### Output fields

- pp_hdfeppml: coefficients (named per regressor) + se + deviance + bic + n_obs/n_coef + fixed_effects (the labels) + penalty='none'
- pp_penhdfeppml: coefficients (named) + deviance + bic + lambda + penalty + plugin + n_selected (the non-zero ones) + phi (the plugin penalty loadings, or NULL)
- pp_mlfitppml: beta_path (a matrix regressors x lambdas, with rownames) + lambdas + bic_path (a matrix [lambda,bic]) + selected_lambda + selected_bic + selected_coefficients (the column at the argmin BIC) + n_selected + deviance (NA on the path) + phi (plugin) + seed

### Pitfalls

- PPML models E[y]=exp(x*beta) in LEVELS (not logs) -> it handles zero flows & heteroskedasticity; the dependent variable MUST be non-negative (negatives/NA -> NaN -> a cryptic crash, blocked by a gate)
- fixed MUST be supplied in LIST form to penppml (a list of characters = an interaction FE); the wrapper normalises it, and a plain character vector (simple FE) is converted into a list — otherwise the package fails cryptically
- the lasso zeroes coefficients out (n_selected = the number of non-zero ones); ridge NEVER zeroes any (n_selected is usually all of them)
- the IC selection = the argmin of the finite BIC along bic_path (DETERMINISTIC); a degenerate/all-NA BIC (e.g. too large a lambda -> an all-zero fit) -> the 1st lambda is returned with bic=NA
- plugin=TRUE (penhdfeppml & mlfitppml) REQUIRES a cluster (cluster-robust penalty loadings) -> a gate; it returns phi (the per-coefficient loadings)
- a non-numeric indep regressor is coerced SILENTLY into a meaningless coefficient by the package -> a hard gate (indep must be all numeric, with no NA)
- IRLS/glmnet are deterministic (identical when seeded); the seed is exposed as defence in depth; the raw fit is NOT returned (heavy per-observation internals -> a to_mcp stub); the _int/xvalidate/selectobs/bootstrap/iceberg functions were omitted (outside the node estimator surface)

### References

- penppml v0.2.4 ref manual + vignette (the hdfeppml/penhdfeppml/mlfitppml help pages, signatures & output fields live-verified)
- Santos Silva & Tenreyro 2006 'The Log of Gravity' Review of Economics and Statistics 88(4) 641-658 (the PPML gravity estimator)
- Correia, Guimaraes & Zylkin 2020 'Fast Poisson estimation with high-dimensional fixed effects' The Stata Journal 20(1) 95-115 (ppmlhdfe / the fast HDFE PPML backbone)
- Breinlich, Corradi, Rocha, Ruta, Santos Silva & Zylkin 2021 'Machine Learning in International Trade Research: Evaluating the Impact of Trade Agreements' World Bank Policy Research WP 9629 (penalized/plugin PPML provision selection)
- Belloni, Chernozhukov, Hansen & Kozbur 2016 'Inference in High-Dimensional Panel Models With an Application to Gun Control' JBES 34(4) 590-605 (the plugin lasso penalty loadings)
- wrapper footer IMPLEMENTATION NOTE (c28_trade_gravity/penalized_poisson_pml)

## #239 — Economic complexity: RCA (the Balassa index), ECI/PCI (fitness/reflections/eigenvalues), product-space proximity

**Module:** `economic_complexity_rca.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `ec_balassa` | `df` | `df_handle`, `boolean`, `number`, `string`, `string`, `string` | `discrete=True`, `cutoff=1` | `light` | — |
| `ec_complexity` | `df` | `df_handle`, `enum`, `integer`, `number`, `boolean`, `number`, `string`, `string`, `string` | `iterations=20`, `extremality=1`, `discrete=True`, `cutoff=1` | `light` | — |
| `ec_proximity` | `df` | `df_handle`, `enum`, `boolean`, `number`, `string`, `string`, `string` | `discrete=True`, `cutoff=1` | `light` | — |

### Use when

a bipartite country×product export panel -> the Revealed Comparative Advantage (Balassa), the Economic/Product Complexity Index (ECI/PCI), and product-space proximity (country×country / product×product similarity) for analysing specialisation, diversification & productive capabilities

### Do not use when

gravity/PPML trade-flow models (#237/#238 in the same category); a time series of one variable (no bipartite structure); input-output/network centrality (#48-55); downstream product-space diffusion (outlook/density/distance/projections — a separate card); data ingestion (a file upload — a frontend route, not a node)

### Alternatives

| instead use | when |
| --- | --- |
| ec_balassa (discrete=TRUE => 0/1 specialization; FALSE => a continuous RCA) | you want the country×product Revealed Comparative Advantage matrix + diversification (rowSums) & ubiquity (colSums) |
| ec_complexity (method=fitness/reflections/eigenvalues) | you want the ECI per country + the PCI per product; fitness=non-linear iterative (Tacchella); reflections=iterated averaging (Hidalgo-Hausmann); eigenvalues=the 2nd eigenvector |
| ec_proximity (compute=both/country/product) | you want product-space similarity matrices: country×country AND/OR product×product (Hausmann-Hidalgo) |

### Output fields

- ec_balassa: balassa_index (a country×product matrix with dimnames; discrete => 0/1) + diversification (named numeric per country, rowSums) + ubiquity (per product, colSums) + n_countries/n_products/discrete/cutoff
- ec_complexity: eci (named numeric per country) + pci (named numeric per product) + method/iterations/extremality/discrete/cutoff + countries/products
- ec_proximity: proximity_country (a country×country matrix or NULL) + proximity_product (a product×product matrix or NULL) + compute + n_countries/n_products (NA if that side was not requested)

### Pitfalls

- MASKING: density masks density -> the wrapper uses requireNamespace + fn (NEVER library); conflicts(detail=TRUE) live-confirmed
- balassa_index silently ACCEPTS negative values & returns a plausible-but-wrong RCA -> a hard non-negativity gate (the Balassa index is defined only on non-negative exports)
- a single country OR a single product -> a degenerate all-1 RCA (silently wrong) -> a hard gate requiring >=2 countries AND >=2 products
- discrete=TRUE (a 0/1 RCA >= cutoff) is the classic input for ECI/proximity; a continuous RCA changes the meaning of the downstream metrics
- extremality affects ONLY method='fitness' (it is inert for reflections/eigenvalues but is still passed); eigenvalues prints a cosmetic sign-correction message (suppressMessages, not a warning)
- deterministic (linear algebra / iterated reflections); no RNG -> no seed; identical over 2 runs is pinned in the tests
- a TERMINAL node: no register/handle chaining; it returns chart-ready numbers (matrices + the ECI/PCI vectors), not a fitted model

### References

- economiccomplexity v2.1.0 ref manual (the balassa_index/complexity_measures/proximity help pages)
- Balassa 1965 'Trade Liberalisation and Revealed Comparative Advantage' The Manchester School 33(2) 99-123 (the Balassa/RCA index)
- Hidalgo & Hausmann 2009 'The building blocks of economic complexity' PNAS 106(26) 10570-10575 (ECI/PCI, the method of reflections)
- Hausmann, Hidalgo et al. 2014 'The Atlas of Economic Complexity' MIT Press (ECI/PCI, the product space, proximity)
- Hidalgo, Klinger, Barabasi, Hausmann 2007 'The Product Space Conditions the Development of Nations' Science 317(5837) 482-487 (proximity / the product space)
- Tacchella, Cristelli, Caldarelli, Gabrielli, Pietronero 2012 'A New Metrics for Countries Fitness and Products Complexity' Scientific Reports 2:723 (the fitness method)
- wrapper footer IMPLEMENTATION NOTE (c28_trade_gravity/economic_complexity_rca)
