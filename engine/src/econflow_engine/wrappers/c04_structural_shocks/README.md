<!-- SPDX-License-Identifier: AGPL-3.0-only -->
# 04-structural-shocks

10 METHOD-SELECTION cards, 10 modules, 47 nodes.

Every card below governs one wrapper module in this package. The cards are the
reason a method exists here at all: they record when it applies, what to reach
for instead, and the traps that make its output easy to misread.

## #19 — SVAR / IRF / FEVD / Blanchard-Quah (theory-based identification)

**Module:** `svar_irf_fevd.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `vr_svar` | `model` | `raw_handle`, `enum`, `matrix_handle`, `matrix_handle`, `boolean` | `lrtest=True` | `light` | `model` |
| `vr_bq` | `model` | `raw_handle` | — | `light` | `model` |
| `vr_irf` | `model` | `raw_handle`, `string`, `string`, `integer`, `boolean`, `boolean`, `boolean`, `number`, `integer` | `n_ahead=10`, `ortho=True`, `cumulative=False`, `boot=True`, `ci=0.95`, `runs=100` | `heavy` | — |
| `vr_fevd` | `model` | `raw_handle`, `integer` | `n_ahead=10` | `light` | — |

### Use when

a reduced-form varest exists + credible theoretical restrictions (A/B contemporaneous or Blanchard-Quah long-run) for a full IRF/FEVD system.

### Do not use when

no credible restriction -> svars/VARsignR; you want robustness to misspecification/non-linearity -> lpirfs.

### Prerequisites

- c01_preparation_prechecks/unit_root_normality.run_adf_test
- c01_preparation_prechecks/unit_root_normality.run_kpss_test
- c03_multivariate_nowcasting/reduced_form_var.vr_var

### Alternatives

| instead use | when |
| --- | --- |
| svars (#20) | there is no theory for A/B -> statistical/data-driven identification. |
| VARsignR (#21) | only qualitative sign priors -> set-identification. |
| lpirfs (#22) | robustness to non-linearity/misspecification or an externally identified shock (LP-IV). |

### Output fields

- irf: 3D array {values,dim,dimnames} — the response to an impulse per horizon
- Lower/Upper: bootstrap CI bands at ci (0 inside => not significant)
- fevd: named list per variable — shares of forecast variance per shock
- A/B/Ase/Bse: structural matrices + SE; Sigma.U: residual covariance
- LRIM: long-run impact matrix (BQ/SVAR)
- LR: LR test of overidentifying restrictions (small p => the restrictions are rejected)

### Pitfalls

- Cholesky is ordering-dependent: the variable order is a theoretical assumption, not a given.
- bootstrap bands measure only sampling uncertainty given the ID — they do not correct a wrong identification.
- an unstable VAR (roots>=1) => explosive IRF, invalid CI; a stability post-check is required (roots).
- Blanchard-Quah: the long-run restriction holds in first differences — the wrong order of integration invalidates the LRIM.
- the IRF sign/normalization is a convention (a unit positive shock).

### References

- Blanchard-Quah 1989 AER
- Sims 1980
- Lütkepohl 2005 New Introduction to Multiple Time Series Analysis
- Enders 2015 Applied Econometric Time Series ch.5
- Pfaff 2008 JSS vars
- vars 1.6-1

## #20 — Data-driven SVAR identification (Cholesky / changes-in-vol / distance-cov / non-Gaussian ML) + HD + counterfactual + wild/mb bootstrap

**Module:** `driven_svar_identification.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `svar_id_chol` | `model` | `raw_handle` | — | `light` | `model` |
| `svar_id_cv` | `model`, `SB` | `raw_handle`, `integer`, `integer`, `number` | `max_iter=50`, `crit=0.001` | `light` | `model` |
| `svar_id_dc` | `model` | `raw_handle`, `boolean`, `integer` | `PIT=False`, `seed=2025` | `light` | `model` |
| `svar_id_ngml` | `model` | `raw_handle`, `boolean`, `integer` | `stage3=False`, `seed=2025` | `light` | `model` |
| `svar_irf` | `x` | `raw_handle`, `integer` | `n_ahead=10` | `light` | — |
| `svar_fevd` | `x` | `raw_handle`, `integer` | `n_ahead=10` | `light` | — |
| `svar_hd` | `x` | `raw_handle`, `integer`, `number` | `series=1`, `transition=0` | `light` | — |
| `svar_cf` | `x` | `raw_handle`, `integer`, `number` | `series=1`, `transition=0` | `light` | — |
| `svar_wild_boot` | `x` | `raw_handle`, `integer`, `integer`, `enum`, `enum`, `number`, `number` | `n_ahead=20`, `nboot=500`, `lower_q=0.16`, `upper_q=0.84` | `heavy` | — |
| `svar_mb_boot` | `x` | `raw_handle`, `integer`, `integer`, `integer`, `enum`, `number`, `number` | `n_ahead=20`, `nboot=500`, `b_length=15`, `lower_q=0.16`, `upper_q=0.84` | `heavy` | — |

### Use when

a reduced-form varest without credible theory -> statistical identification through heteroskedasticity (id.cv), independence (id.dc) or non-Gaussianity (id.ngml); + historical decomposition & counterfactual.

### Do not use when

exact theoretical restrictions -> SVAR; only sign priors -> VARsignR; Gaussian and homoskedastic shocks -> statistical ID fails.

### Prerequisites

- c01_preparation_prechecks/unit_root_normality.run_adf_test
- c01_preparation_prechecks/unit_root_normality.run_kpss_test
- c03_multivariate_nowcasting/reduced_form_var.vr_var

### Alternatives

| instead use | when |
| --- | --- |
| SVAR/BQ (#19) | exact contemporaneous/long-run restrictions exist. |
| VARsignR (#21) | only qualitative sign priors -> set-identification. |
| lpirfs LP-IV (#22) | an external instrument/proxy for one shock (full-system ID is not needed). |

### Output fields

- B: structural impact matrix (column j = the immediate response to the j-th shock)
- model: identified 'svars' object (feeds irf/fevd/hd/cf/bootstrap)
- id.cv: Lambda (post-break heteroskedasticity), Lambda_SE, wald_statistic (test of equal eigenvalues)
- id.ngml: df (t-df of the shocks), sigma, B_stand
- svar_hd: hd — the contribution of each shock to the historical path; svar_cf: actual vs counter
- wild/mb boot: point/mean/lower/upper bands (default 0.16/0.84), SE, nboot, design, distr

### Pitfalls

- id.cv wald_statistic: the ID is valid ONLY if the test REJECTS equal eigenvalues of Lambda — otherwise the shocks are not identified (spurious B).
- statistical ID identifies the columns of B only up to sign & permutation — you must label which column = which economic shock.
- id.dc/id.ngml break down if the shocks are Gaussian (at most one Gaussian shock is allowed).
- stochastic routines (id.dc/id.ngml/bootstrap) -> set.seed (default 2025) for reproducibility.
- wild.boot design fixed vs recursive; mb.boot for dependent residuals.

### References

- Rigobon 2003 RESTAT
- Lanne-Meitz-Saikkonen 2017
- Herwartz-Plödt 2016 OBES
- Lütkepohl-Meitz-Netšunajev-Saikkonen 2021 Econometrics Journal
- Gonçalves-Kilian 2004
- Brüggemann-Jentsch-Trenkler 2016
- Lange-Dalheimer-Herwartz-Maxand 2021 JSS svars
- svars

## #21 — Sign-restriction SVAR (Uhlig rejection & penalty, Rubio-Ramirez/Waggoner/Zha)

**Module:** `sign_restriction_svar.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `vsr_uhlig_reject` | `Y`, `constrained` | `multiseries_handle`, `int_array`, `integer`, `integer`, `integer`, `integer`, `integer`, `integer`, `integer`, `enum` | `nlags=4`, `draws=200`, `subdraws=200`, `nkeep=1000`, `KMIN=1`, `KMAX=4`, `steps=24` | `mcmc` | — |
| `vsr_uhlig_penalty` | `Y`, `constrained` | `multiseries_handle`, `int_array`, `integer`, `integer`, `integer`, `integer`, `integer`, `integer`, `integer`, `number`, `enum` | `nlags=4`, `draws=1000`, `subdraws=1000`, `nkeep=1000`, `KMIN=1`, `KMAX=4`, `steps=24`, `penalty=100` | `mcmc` | — |
| `vsr_rwz_reject` | `Y`, `constrained` | `multiseries_handle`, `int_array`, `integer`, `integer`, `integer`, `integer`, `integer`, `integer`, `integer`, `enum` | `nlags=4`, `draws=200`, `subdraws=200`, `nkeep=1000`, `KMIN=1`, `KMAX=4`, `steps=24` | `mcmc` | — |

### Use when

only qualitative expectations about the direction of the responses (sign restrictions) -> Bayesian set-identification (sampling rotations).

### Do not use when

exact restrictions -> SVAR; point-identified statistical ID -> svars; you need a maintained package (VARsignR is archived/fragile).

### Prerequisites

- c01_preparation_prechecks/unit_root_normality.run_adf_test
- c01_preparation_prechecks/unit_root_normality.run_kpss_test

### Alternatives

| instead use | when |
| --- | --- |
| SVAR (#19) | exact contemporaneous/long-run restrictions. |
| svars (#20) | statistical/data-driven point identification (without subjective sign priors). |
| lpirfs + external shock (#22) | you already have an identified shock/proxy. |

### Output fields

- irf_median/irf_lower/irf_upper: posterior summary bands (steps x nvar) at lower_q/upper_q
- fevd_median/_lower/_upper: FEVD bands
- n_keep: accepted draws; steps; nvar; type (median/mean); constrained; variables

### Pitfalls

- set-identification, not point: the bands are the range of many admissible models (identification uncertainty), not the sampling uncertainty of a single model.
- the pointwise median IRF does NOT correspond to a single structural model (Fry-Pagan 2011 critique).
- constrained polarity/sign convention: the 1st element = the shock of interest, the sign = the direction; the wrong sign -> the inverted shock.
- too few accepted rotations -> cryptic errors (ldraw/SDraws) which the wrapper translates into a gate (increase draws, relax the restrictions).
- MCMC -> set.seed (default 12345); fp.target was omitted (plot output, not data).

### References

- Uhlig 2005 JME
- Rubio-Ramírez-Waggoner-Zha 2010 RES
- Fry-Pagan 2011 JEL critique
- Danne 2015 VARsignR
- archive VARsignR

## #22 — Local projections (Jordà) + LP-IV / non-linear state-dependent / panel

**Module:** `local_projections_lp.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `lp_linear` | `endog_data` | `df_handle`, `integer`, `integer`, `integer`, `number`, `integer` | `lags_endog_lin=2`, `trend=0`, `shock_type=1`, `confint=1.96`, `hor=10` | `light` | — |
| `lp_linear_iv` | `endog_data`, `shock` | `df_handle`, `series_handle`, `integer`, `integer`, `number`, `integer`, `boolean`, `boolean` | `lags_endog_lin=2`, `trend=0`, `confint=1.96`, `hor=10`, `cumul_mult=False`, `use_twosls=False` | `light` | — |
| `lp_nonlinear` | `endog_data`, `switching` | `df_handle`, `series_handle`, `integer`, `integer`, `integer`, `integer`, `number`, `integer`, `boolean`, `boolean`, `number`, `number` | `lags_endog_lin=2`, `lags_endog_nl=2`, `trend=0`, `shock_type=1`, `confint=1.96`, `hor=10`, `use_logistic=True`, `use_hp=False`, `gamma=3` | `light` | — |
| `lp_nonlinear_iv` | `endog_data`, `shock`, `switching` | `df_handle`, `series_handle`, `series_handle`, `integer`, `integer`, `number`, `integer`, `boolean`, `boolean`, `boolean`, `number`, `number` | `lags_endog_nl=2`, `trend=0`, `confint=1.96`, `hor=10`, `cumul_mult=False`, `use_logistic=True`, `use_hp=False`, `gamma=3` | `light` | — |
| `lp_panel` | `data_set`, `endog_data`, `shock` | `df_handle`, `string`, `string`, `integer`, `number`, `string`, `string`, `boolean`, `boolean`, `boolean` | `hor=10`, `confint=1.96`, `panel_model='within'`, `panel_effect='individual'`, `iv_reg=False`, `cumul_mult=True`, `diff_shock=True` | `light` | — |
| `lp_panel_nl` | `data_set`, `endog_data`, `shock`, `switching` | `df_handle`, `string`, `string`, `string`, `integer`, `number`, `string`, `string`, `boolean`, `boolean`, `boolean`, `boolean`, `number`, `number` | `hor=10`, `confint=1.96`, `panel_model='within'`, `panel_effect='individual'`, `cumul_mult=True`, `diff_shock=True`, `use_logistic=True`, `use_hp=False`, `gamma=3` | `light` | — |

### Use when

IRF without a full VAR (one regression per horizon), robust to misspecification; state dependence (two regimes), external instrument/proxy (LP-IV + 2SLS), panel FE/IV/GMM; fiscal multipliers (cumul_mult).

### Do not use when

you want full-system FEVD/HD & efficiency -> vars/svars; very long horizons with little data (the LP variance explodes).

### Prerequisites

- c01_preparation_prechecks/unit_root_normality.run_adf_test
- c01_preparation_prechecks/unit_root_normality.run_kpss_test

### Alternatives

| instead use | when |
| --- | --- |
| vars/svars (#19/#20) | full-system FEVD/HD, efficiency, lower variance at long horizons. |
| VARsignR (#21) | identification exclusively through sign priors (LP needs an already-identified shock). |
| plm panel (§08) | a static/dynamic panel without an IRF horizon. |

### Output fields

- irf_lin_mean/low/up: matrices — row = response variable, column = horizon (transposed vs the vars array)
- irf_s1_*/irf_s2_*: regime 1/2 responses (non-linear); fz: logistic switching function values
- variables, hor, lags, shock_type (0=sd,1=unit), trend, confint, cumul_mult, use_twosls

### Pitfalls

- confint is a MULTIPLIER, not a probability: 1=68%, 1.65=90%, 1.96=95% (Newey-West band width).
- orientation: in irf_lin_mean rows=variables, columns=horizons — do not confuse it with the vars 3D array.
- the LP variance grows with the horizon -> wide bands at large h; do not over-interpret long-horizon significance.
- cumul_mult=TRUE = cumulative multipliers, only for lags_criterion=NaN; shock_type 0=1sd,1=unit.
- LP-IV: validity depends entirely on the instrument (relevance+exogeneity); there is no built-in weak-IV test; endog_data MUST be a data_frame, not a ts.

### References

- Jordà 2005 AER
- Jordà-Schularick-Taylor 2015
- Ramey-Zubairy 2018 JPE
- Auerbach-Gorodnichenko 2012
- Newey-West 1987 Econometrica
- Adämmer 2019 lpirfs
- lpirfs

## #148 — Bayesian Structural VAR identified through heteroskedasticity/non-normality (SV / Markov-switching heteroskedasticity / Student-t) + IRF/FEVD/HD/structural shocks + a Savage-Dickey (SDDR) identification check — bsvars

**Module:** `bayesian_structural_var_identified_through.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `bsv_estimate` | `data`, `seed` | `matrix_handle`, `enum`, `integer`, `integer`, `integer`, `integer`, `integer`, `boolean`, `integer`, `boolean` | `p=1`, `S=100`, `burnin=50`, `thin=1`, `M=2`, `stationary=False`, `allow_nonconvergence=False` | `mcmc` | `model` |
| `bsv_irf` | `model` | `raw_handle`, `integer`, `boolean`, `num_array` | `horizon=12`, `standardise=False` | `light` | — |
| `bsv_fevd` | `model` | `raw_handle`, `integer`, `num_array` | `horizon=12` | `light` | — |
| `bsv_hd` | `model` | `raw_handle`, `num_array` | — | `light` | — |
| `bsv_shocks` | `model` | `raw_handle`, `num_array` | — | `light` | — |
| `bsv_verify` | `model` | `raw_handle`, `boolean` | `allow_nonconvergence=False` | `light` | — |

### Use when

A multivariate series (K>=2) where you want a BAYESIAN structural VAR with shock identification through STATISTICAL STRUCTURE (not theoretical restrictions): sv=stochastic volatility, msh=Markov-switching heteroskedasticity (M regimes), t=Student-t non-normality. Posterior IRF/FEVD/HD/structural shocks with credible bands + an SDDR identification check (bsv_verify).

### Do not use when

Reduced-form/forecasting suffices -> vars #11; FREQUENTIST data-driven identification (Rigobon changes-in-volatility, distance covariance, non-Gaussian ML) -> svars #20; theoretical A/B or Blanchard-Quah restrictions -> SVAR/vr_bq #19; sign-restriction set-ID -> VARsignR #21; regime-dependent DYNAMICS (not just the variance) -> sstvars #150.

### Prerequisites

- c01_preparation_prechecks/unit_root_normality.run_adf_test
- c01_preparation_prechecks/unit_root_normality.run_kpss_test
- bsv_verify

### Alternatives

| instead use | when |
| --- | --- |
| 04-structural-shocks/svar_id_cv | Frequentist changes-in-volatility (Rigobon) identification instead of Bayesian; a point estimate + wild/MB bootstrap bands. |
| 04-structural-shocks/svar_id_chol | Plain recursive (Cholesky) identification without the Bayesian machinery. |
| 03-multivariate-nowcasting/Vars-vr_var | Reduced-form dynamics/forecasting suffice (no structural identification). |
| bsv_verify | Before interpreting IRF/FEVD: confirm that the statistical structure identifies the shocks (a negative logSDDR). |

### Output fields

- bsv_estimate: model (the producer posterior 'PosteriorBSVAR*' handle) + B_mean/A_mean (posterior-mean structural/AR matrices) + model_type/p/K/S/burnin/thin/n_draws/seed/converged
- bsv_irf/bsv_fevd: a long df (response\|variable x shock x horizon + mean/lower/upper) — the posterior mean + quantile bands (default 16%/84%); horizon 0 = the impact
- bsv_hd: a long df (variable x shock x time + mean/lower/upper) — the historical contribution of each shock per period (time = real ts time)
- bsv_shocks: a long df (shock x time + mean/lower/upper) — the estimated structural disturbances
- bsv_verify: logSDDR (a vector of length K per shock for SV/MSH; a scalar for t) + logSDDR_se (SV/MSH) or the SDDR ratio (t) + identified (per-shock logSDDR<0) + type/degenerate

### Pitfalls

- SDDR sign: a NEGATIVE logSDDR is evidence AGAINST non-identification (the shock IS identified through heteroskedasticity/non-normality); a positive one means it adds no identification beyond the default lower-triangular structure. -Inf is VALID (strong evidence, t model); NaN/NA = degenerate -> block.
- The default identification is a lower-triangular B (recursive; the variable ORDER matters); the heteroskedasticity allows the exclusion restrictions to be TESTED/relaxed, it does not replace the recursive structure by default.
- Degenerate diagnostics = non-convergence (the Bayesian lesson): non-finite posterior draws (bsv_estimate) or an NaN/NA logSDDR (bsv_verify) -> a hard stop unless allow_nonconvergence=TRUE.
- TINY defaults (S=100, burnin=50): production runs raise the draw counts; the seed is MANDATORY (set.seed covers the burn-in + retained draws across two sequential estimate calls; without a seed the run is not reproducible).
- bsv_hd time axis: as_numeric of the labels (NOT as.integer, which would TRUNCATE 1.25->1 and destroy the axis); model='msh' => M>=2.

### References

- Lütkepohl H., Woźniak T. 2020. Bayesian Inference for Structural Vector Autoregressions Identified by Markov-Switching Heteroskedasticity. Journal of Economic Dynamics and Control, 113, 103862.
- Lütkepohl H., Shang F., Uzeda L., Woźniak T. 2024. Partial Identification of Heteroskedastic Structural VARs: Theory and Bayesian Inference. University of Melbourne Working Paper, arXiv:2404.11057.
- Woźniak T. 2024. bsvars: Bayesian Estimation of Structural Vector Autoregressive Models. the reference package.
- bsvars v3.2 (specify_bsvar_sv/_msh/_t, estimate, compute_impulse_responses/_variance_decompositions/_historical_decompositions/_structural_shocks, verify_identification — reference + live introspection the engine)

## #149 — Bayesian Structural VAR with SIGN + ZERO + NARRATIVE restrictions (set-identified, importance sampling; a Waggoner-Zha Gibbs sampler + a uniform rotation Q) — bsvarSIGNs

**Module:** `bayesian_structural_var_sign_zero.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `bss_estimate` | `data`, `seed` | `multiseries_handle`, `integer`, `matrix_handle`, `matrix_handle`, `integer`, `integer`, `integer`, `number`, `boolean`, `integer` | `p=1`, `S=100`, `thin=1`, `max_tries=10000`, `ess_min_ratio=0.01`, `allow_nonconvergence=False` | `mcmc` | `model` |
| `bss_irf` | `model` | `raw_handle`, `integer`, `boolean`, `number`, `number` | `horizon=8`, `standardise=False`, `lower_q=0.16`, `upper_q=0.84` | `light` | — |
| `bss_fevd` | `model` | `raw_handle`, `integer`, `number`, `number` | `horizon=8`, `lower_q=0.16`, `upper_q=0.84` | `light` | — |
| `bss_forecast` | `model`, `seed` | `raw_handle`, `integer`, `matrix_handle`, `matrix_handle`, `number`, `number`, `integer` | `horizon=4`, `lower_q=0.16`, `upper_q=0.84` | `light` | — |

### Use when

A multivariate series (N>=2) with structural shocks identified through THEORETICAL restrictions: sign restrictions (IRF signs), zero restrictions (0 entries in sign_irf; importance sampling), narrative sign restrictions (historical episodes). Set-identified Bayesian work -> posterior credible bands on IRF/FEVD + a predictive/conditional forecast.

### Do not use when

Exclusion/recursive identification (a known order) or statistical ID from heteroskedasticity/non-Gaussianity -> svars #20 / SVAR #19; purely reduced-form forecasting/nowcasting -> vars #11 / BVAR #12; regime-dependent (nonlinear) structural dynamics -> sstvars #150.

### Prerequisites

- c01_preparation_prechecks/unit_root_normality.run_adf_test
- c01_preparation_prechecks/unit_root_normality.run_kpss_test

### Alternatives

| instead use | when |
| --- | --- |
| 04-structural-shocks/svar_id_chol | Frequentist data-driven ID (heteroskedasticity/non-Gaussianity) or a recursive Cholesky — there are no theoretical sign/zero restrictions. |
| 03-multivariate-nowcasting/Vars-vr_var | Purely reduced-form work (forecasting/Granger) without structural shock identification. |
| 04-structural-shocks/sst_girf | Regime-dependent (nonlinear/smooth-transition) structural dynamics. |
| bss_forecast | You want predictive/conditional forecast bands rather than structural IRF/FEVD bands (bss_irf). |

### Output fields

- bss_estimate: model (the 'PosteriorBSVARSIGN' producer handle) + B_median (the posterior median of the contemporaneous B) + ess (the importance-sampling ESS) + n_draws + ess_ratio + converged + restrictions (the active restrictions) + K/p/S/seed
- bss_irf: irf = a tidy long data_frame (response, shock, horizon, median, lower, upper) — the set-identified band per (response,shock,horizon), chart-data
- bss_fevd: fevd = tidy long (variable, shock, horizon, median share + lower/upper)
- bss_forecast: forecast = tidy long (variable, horizon, median, lower, upper) + conditional (TRUE when a conditional_forecast was supplied)

### Pitfalls

- SET identification, NOT point: the IRF is a posterior DISTRIBUTION -> read the median + the credible band, NEVER a single 'true' response; the band reflects identification AND estimation uncertainty.
- ESS is a degeneracy diagnostic (mirroring rstan/MARSS): sign-only -> ess==n_draws (uniform); zero/narrative -> ess<n_draws (importance reweighting); a very low ess/n_draws means very few valid rotations -> an UNRELIABLE posterior -> STOP (ess_min_ratio, overridable with allow_nonconvergence).
- Zero restrictions are written as 0 in the SAME sign_irf array (NOT a separate argument); they trigger importance sampling (Arias et al. 2018).
- Impossible/excessive restrictions -> the sampler spends an enormous time searching for a valid rotation Q (the L1 default max_tries=Inf can hang; the node uses a finite default).
- Stochasticity: bss_estimate (Gibbs) & bss_forecast (predictive sampling) require a seed (identical draws were verified); bss_irf/bss_fevd are deterministic transformations of the draws.
- S3 collision: the generics estimate/compute_impulse_responses/compute_variance_decompositions/forecast -> NO library(bsvarSIGNs); getS3method(.., asNamespace('bsvarSIGNs')) + bsvarSIGNs:: (conflicts(detail=TRUE) is empty).

### References

- Wang X., Woźniak T. bsvarSIGNs: Bayesian SVARs with sign, zero and narrative restrictions. v2.0.
- Rubio-Ramírez J., Waggoner D., Zha T. 2010. Structural Vector Autoregressions: Theory of Identification and Algorithms for Inference. Review of Economic Studies, 77:2, 665-696.
- Arias J., Rubio-Ramírez J., Waggoner D. 2018. Inference Based on SVARs Identified with Sign and Zero Restrictions. Econometrica, 86:2, 685-720.
- Antolín-Díaz J., Rubio-Ramírez J. 2018. Narrative Sign Restrictions for SVARs. American Economic Review, 108:10, 2802-2829.
- Waggoner D., Zha T. 2003. A Gibbs sampler for structural vector autoregressions. Journal of Economic Dynamics and Control, 28:2, 349-366.
- Giannone D., Lenza M., Primiceri G. 2015. Prior Selection for Vector Autoregressions. Review of Economics and Statistics, 97:2, 436-451.
- bsvarSIGNs v2.0 (specify_bsvarSIGN/estimate/compute_impulse_responses/compute_variance_decompositions/forecast/specify_narrative reference + live introspection)

## #150 — Smooth-transition / threshold / (m)logistic STRUCTURAL VAR (nonlinear, regime-dependent dynamics) + GIRF/GFEVD/linear IRF — sstvars

**Module:** `smooth_transition_threshold.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `sst_fit` | `data`, `seed` | `multiseries_handle`, `integer`, `integer`, `enum`, `enum`, `enum`, `num_array`, `integer`, `integer`, `integer`, `integer` | `p=1`, `M=2`, `nrounds=2`, `ngen=30`, `maxit=300` | `light` | `model` |
| `sst_girf` | `model`, `seed` | `raw_handle`, `num_array`, `integer`, `number`, `integer`, `integer`, `integer`, `num_array`, `integer`, `integer` | `N=16`, `shock_size=1`, `n_iterations=50`, `n_initial_values=50`, `init_regime=1`, `burn_in=200` | `light` | — |
| `sst_gfevd` | `model`, `seed` | `raw_handle`, `integer`, `number`, `enum`, `integer`, `integer`, `integer`, `integer`, `integer` | `N=16`, `shock_size=1`, `n_iterations=50`, `n_initial_values=50`, `init_regime=1`, `burn_in=200` | `light` | — |
| `sst_linear_irf` | `model` | `raw_handle`, `integer`, `integer`, `number`, `integer`, `integer` | `N=16`, `regime=1`, `bootstrap_reps=100` | `light` | — |

### Use when

A multivariate series (d>=2) whose dynamics CHANGE by regime (recession vs expansion, high vs low volatility, monetary regime) — a smooth-transition or threshold switch between M regimes. You want regime-/state-dependent generalized impulse responses (GIRF), a generalized FEVD, or the linear IRF of one regime. weight_function: relative_dens/logistic/mlogit/exponential/threshold/exogenous.

### Do not use when

Linear/time-invariant dynamics suffice -> vars #11 / BVAR #12; SMOOTH continuous variation of the coefficients WITHOUT discrete regimes -> shrinkTVPVAR #146 / bvarsv #14; linear structural shock identification -> svars #20 / SVAR #19; fully structural non-Gaussian ID -> fitSSTVAR (outside the surface).

### Prerequisites

- c01_preparation_prechecks/unit_root_normality.run_adf_test
- c01_preparation_prechecks/unit_root_normality.run_kpss_test
- c01_preparation_prechecks/linearity_battery_linearity.nlt_nonlinearity

### Alternatives

| instead use | when |
| --- | --- |
| 03-multivariate-nowcasting/Vars-vr_var | Linear/time-invariant dynamics suffice — there are no regimes (cheaper, IRF/FEVD ready). |
| 03-multivariate-nowcasting/stv_estimate | Smooth CONTINUOUS variation of the coefficients (NOT discrete regimes) + stochastic volatility. |
| 04-structural-shocks/svar_id_chol | A linear structural VAR — data-driven shock identification within one regime (heteroskedasticity/non-Gaussianity). |
| sst_linear_irf | You want the linear IRF of one fixed regime rather than a regime-/state-dependent GIRF (sst_girf). |

### Output fields

- sst_fit: model (the 'stvar' producer handle) + loglik/IC (AIC/HQIC/BIC) + params + transition_weights ((T-p)xM regime probabilities, chart-data) + identification (reduced_form)/p/M/d
- sst_girf: girf (a named list per shock: point_est [(N+1) x (d+M-1)] + conf_ints; row 1 = the impact at n=0) + which_shocks/N/ci — regime-dependent generalized responses
- sst_gfevd: gfevd (a 3D array [horizon x variable x shock]) + initval_type/N — the generalized variance decomposition
- sst_linear_irf: point_est (a 3D array [variables x shock x horizon], slice 1 = the impact) + conf_ints (wild-bootstrap bands or NULL) + regime/N

### Pitfalls

- The GIRF is NON-LINEAR & NON-SYMMETRIC: the response depends on the size/sign of the shock AND on the initial state (init_regime) — NOT like a linear IRF.
- linear_IRF/GIRF on a reduced-form model -> an automatic lower-triangular recursive (Cholesky) ID (the variable ORDER matters); structural without an order -> the non-Gaussian fitSSTVAR.
- linear_IRF bootstrap ci: the bands exist ONLY for models with linear AR dynamics; a genuinely regime-dependent STVAR -> conf_ints=NULL (use the GIRF).
- The stochastic GA log-likelihood is multimodal: small nrounds/ngen (the defaults are TINY) -> a local maximum; production runs raise nrounds/ngen. The seed is MANDATORY (without it the run is not reproducible).
- sst_fit filters out unsuitable solutions (near-singular Sigma with eig<0.002, companion modulus>0.9985); if no appropriate solution is found -> rescale the series to a similar magnitude or run more rounds.
- relative_dens => a Gaussian cond_dist ONLY; logistic/exponential => M=2; a non-relative_dens weight function => weightfun_pars is mandatory (e.g. c(switch_var, lag)).

### References

- Lanne M., Virolainen S. 2025. A Gaussian smooth transition vector autoregressive model. Journal of Economic Dynamics and Control, 178, 105162.
- Virolainen S. (in press). Identification by non-Gaussianity in structural smooth transition VAR models. Econometric Reviews.
- Hubrich K., Teräsvirta T. 2013. Thresholds and Smooth Transitions in VAR Models. CREATES Research Paper 2013-18, Aarhus University.
- Tsay R. 1998. Testing and Modeling Multivariate Threshold Models. JASA, 93:443, 1188-1202.
- Lanne M., Nyberg H. 2016. Generalized Forecast Error Variance Decomposition for Linear and Nonlinear Multivariate Models. Oxford Bulletin of Economics and Statistics, 78:4, 595-603.
- Kilian L., Lütkepohl H. 2017. Structural Vector Autoregressive Analysis. Cambridge University Press.
- sstvars v1.2.4 (fitSTVAR/GIRF/GFEVD/linear_IRF reference + live introspection)

## #151 — Gaussian / Student's-t Mixture VAR (regime switching through mixture-density weights) + GIRF/GFEVD/linear IRF — gmvarkit

**Module:** `gaussian_student_mixture.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `gmv_fit` | `data`, `seed` | `multiseries_handle`, `integer`, `int_array`, `enum`, `boolean`, `enum`, `matrix_handle`, `integer`, `integer`, `integer`, `integer`, `boolean` | `p=1`, `M=2`, `conditional=True`, `ncalls=2`, `ncores=1`, `maxit=100`, `allow_nonconvergence=False` | `light` | `model` |
| `gmv_girf` | `model`, `seed` | `raw_handle`, `int_array`, `integer`, `integer`, `integer`, `number`, `num_array`, `boolean`, `integer`, `integer` | `which_shocks=1`, `N=10`, `n_iterations=50`, `n_initial_values=50`, `shock_size=1`, `include_mixweights=False`, `ncores=1` | `light` | — |
| `gmv_gfevd` | `model`, `seed` | `raw_handle`, `integer`, `integer`, `integer`, `enum`, `number`, `boolean`, `integer`, `integer` | `N=10`, `n_iterations=50`, `n_initial_values=50`, `shock_size=1`, `include_mixweights=False`, `ncores=1` | `light` | — |
| `gmv_linear_irf` | `model`, `seed` | `raw_handle`, `integer`, `integer`, `number`, `integer`, `integer`, `integer` | `N=10`, `regime=1`, `bootstrap_reps=100`, `ncores=1` | `light` | — |

### Use when

A multivariate series (d>=2) whose dynamics SWITCH between M regimes with mixture-density weights that depend on the past (recession vs expansion, high vs low volatility, monetary regime). The regimes are Gaussian (GMVAR), Student's-t (StMVAR) or mixed (G-StMVAR). You want regime-/state-dependent GIRF, a generalized FEVD, or the linear IRF of one regime, with optional structural ID through conditional heteroskedasticity (W).

### Do not use when

Linear/time-invariant dynamics suffice -> vars #11 / BVAR #12; a smooth-transition/threshold/(m)logistic switch (not mixture-density weights) -> sstvars #150; smooth CONTINUOUS variation of the coefficients (NOT discrete regimes) -> shrinkTVPVAR #146 / bvarsv #14; linear data-driven structural ID -> svars #20; univariate (d=1) -> uGMAR.

### Prerequisites

- c01_preparation_prechecks/unit_root_normality.run_adf_test
- c01_preparation_prechecks/unit_root_normality.run_kpss_test

### Alternatives

| instead use | when |
| --- | --- |
| 04-structural-shocks/sst_fit | The switch is smooth-transition/threshold/(m)logistic/exogenous — NOT mixture-density weights (the closest successor). |
| 03-multivariate-nowcasting/Vars-vr_var | Linear/time-invariant dynamics suffice — there are no regimes (cheaper, IRF/FEVD ready). |
| 04-structural-shocks/svar_id_chol | A linear structural VAR — data-driven shock identification within one regime. |
| gmv_linear_irf | You want the linear IRF of one fixed regime rather than a regime-/state-dependent GIRF (gmv_girf). |

### Output fields

- gmv_fit: model (the 'gsmvar' producer handle) + loglik/IC (AIC/HQIC/BIC) + params/std_errors + mixing_weights (a T x M regime-probability path, chart-data) + M/d/p/model_type/structural/converged/n_converged
- gmv_girf: girf (a named list per shock: point_est [(N+1) x vars] + conf_ints; row 1 = the impact at n=0) + which_shocks/N/ci — non-linear generalized responses
- gmv_gfevd: gfevd (a 3D array [(N+1) x variable x shock]) + initval_type/N — the generalized variance decomposition
- gmv_linear_irf: point_est (a 3D array [variables x shock x (N+1)], slice 1 = the impact) + conf_ints (4D wild-bootstrap bands or NULL) + regime/N

### Pitfalls

- The GIRF is NON-LINEAR & NON-SYMMETRIC: the response depends on the size/sign of the shock AND on the initial state (init_regimes) — NOT like a linear IRF
- linear_IRF/GIRF on a reduced-form model -> an automatic lower-triangular recursive (Cholesky) ID (the variable ORDER matters); genuine structural ID -> structural_W (which requires M>=2)
- linear_IRF bootstrap ci: the bands exist ONLY for models with linear AR dynamics (M==1 or constrained identical); genuine regime switching -> conf_ints=NULL (use the GIRF)
- The GFEVD seeds length DEPENDS on initval_type (live-verified): nrow(data)-p+1 for 'data', R2 for 'random'; the wrapper computes it automatically
- A stochastic GA with a multimodal log-likelihood: a small ncalls (default TINY=2) -> a local maximum; production uses ncalls=(M+1)^5. The seed is MANDATORY. Convergence post-gate: degenerate (no round converged or a non-finite loglik) => stop unless allow_nonconvergence=TRUE
- G-StMVAR requires M=c(M1,M2) (M1 Gaussian + M2 Student's-t regimes); Student's-t df near the boundary => effectively Gaussian

### References

- Kalliovirta L., Meitz M., Saikkonen P. 2016. Gaussian mixture vector autoregression. Journal of Econometrics, 192:2, 485-498.
- Virolainen S. 2022. A mixture autoregressive model based on Gaussian and Student's t-distributions. Studies in Nonlinear Dynamics & Econometrics, 26:4, 559-580.
- Virolainen S. 2025. A statistically identified structural vector autoregression with endogenously switching volatility regime. Journal of Business & Economic Statistics, 43:1, 44-54.
- Lanne M., Nyberg H. 2016. Generalized Forecast Error Variance Decomposition for Linear and Nonlinear Multivariate Models. Oxford Bulletin of Economics and Statistics, 78:4, 595-603.
- gmvarkit v2.2.1 (fitGSMVAR/GIRF/GFEVD/linear_IRF reference + live introspection)

## #152 — Desparsified/debiased LASSO inference (high-dimensional time series) + high-dimensional local projections (HDLP) with valid CIs — Adamek-Smeekes-Wilms

**Module:** `desparsified_debiased_lasso.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `dsl_desla` | `X`, `y`, `H`, `seed` | `matrix_handle`, `num_array`, `int_array`, `integer`, `num_array`, `boolean`, `matrix_handle`, `num_array`, `boolean`, `boolean` | `penalize_H=True`, `demean=True`, `scale=True` | `light` | — |
| `dsl_hdlp` | `x`, `y`, `seed` | `num_array`, `num_array`, `integer`, `matrix_handle`, `matrix_handle`, `matrix_handle`, `boolean`, `boolean`, `integer`, `integer`, `num_array`, `boolean`, `boolean` | `y_predetermined=False`, `cumulate_y=False`, `hmax=10`, `lags=4`, `penalize_x=False`, `OLS=False` | `light` | — |

### Use when

High-dimensional inference: a point estimate + honest CIs + a z/Wald test for the target coefficient(s) when N (regressors) is large/≈T (dsl_desla); or an IRF via local projection with MANY controls & valid asymptotic CIs (HAC/LRV variance) when a plain LP would be over-parameterised (dsl_hdlp); optionally a state-dependent IRF (Ramey-Zubairy). The shock must already be identified/exogenous.

### Do not use when

A low-dimensional LP (few controls) -> lpirfs #22 (OLS + Newey-West, no penalty); full-system FEVD/HD/efficiency -> vars/svars #19/#20; shock identification from sign priors -> VARsignR #21 (desla does NOT identify shocks, it takes them as given); pure forecasting (not inference) -> shrinkage/ML forecasters.

### Prerequisites

- c01_preparation_prechecks/unit_root_normality.run_adf_test
- c01_preparation_prechecks/unit_root_normality.run_kpss_test (confirmatory)

### Alternatives

| instead use | when |
| --- | --- |
| #22 lpirfs (04-structural-shocks/lp_linear_iv) | A low-dimensional LP/LP-IV: few controls, standard OLS + Newey-West bands suffice (no high-dimensional penalty/debiasing). |
| #19 vars/svars (04-structural-shocks/vr_irf) | A full-system IRF/FEVD/HD with efficiency & lower variance at long horizons (not high-dimensional). |
| #21 VARsignR | The shock is identified ONLY through sign restrictions (desla/HDLP presupposes an already identified shock). |

### Output fields

- dsl_desla.coefficients: data_frame variable/bhat/se (debiased estimates, on the original scale)
- dsl_desla.intervals: data_frame variable + lower/upper per alpha (honest CIs)
- dsl_desla.joint_test: H0 the reference*beta=q (default: all H jointly zero) -> statistic/p_value
- dsl_desla.row_tests: per-row z_stats + intervals (ONLY when the reference or q is supplied); n_selected: the number of non-zeros in the initial lasso
- dsl_hdlp.irf: a named list per state, each a data_frame horizon + lower/bhat/upper per alpha (CI bands — chart-data)
- dsl_hdlp.states/n_states/hmax/lags/cumulate_y/OLS/seed

### Pitfalls

- STOCHASTICITY (live-verified): although the debiasing is convex+analytic, the lambda selection uses RANDOM CV folds -> WITHOUT a seed two calls give different bhat. The seed is MANDATORY in both tools.
- alphas is the significance level (0.05 -> a 95% CI); the column 'lower 0.05'/'upper 0.05' corresponds to alpha=0.05 (NOT the 5% quantile).
- dsl_hdlp: a hard gate requires hmax + lags < T. If you exceed it, the package itself SILENTLY truncates hmax (to 0.8*eff-lags); the wrapper surfaces this as a message instead of losing it.
- desla/HDLP does NOT identify a structural shock — x (the shock) must already be exogenous/identified (a proxy/instrument/orthogonalised series). The validity of the inference depends on that.
- q in dsl_hdlp = the 'fast' controls (the high-dimensional space); q in dsl_desla = the RHS of H0 the reference*beta=q. The SAME NAME but a DIFFERENT meaning.
- OLS=TRUE only for the low-dimensional case (otherwise singular); state_variables: each column must be categorical OR a binary indicator of one regime.

### References

- Adamek, Smeekes & Wilms 2021 'LASSO inference for high-dimensional time series' (arXiv:2007.10952)
- van de Geer, Buhlmann, Ritov & Dezeure 2014 'On asymptotically optimal confidence regions and tests for high-dimensional models' (Annals of Statistics 42(3):1166-1202)
- Plagborg-Moller & Wolf 2021 'Local projections and VARs estimate the same impulse responses' (Econometrica 89(2):955-980)
- Ramey & Zubairy 2018 'Government spending multipliers in good times and in bad' (JPE 126(2):850-901); Andrews 1991 (Econometrica 59(3):817-858)
- desla reference manual (desla, HDLP)

## #153 — Residual diagnostics for a reduced-form VAR: a multivariate LM autocorrelation test (+HC-robust/univariate) + a combined bootstrap ARCH test (CA/ET/MARCH) + a wild-bootstrap AC test

**Module:** `residual_diagnostics_reduced.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `vtt_fit` | `y` | `multiseries_handle`, `integer`, `boolean`, `boolean`, `exog_handle` | `p=1`, `const=True`, `trend=False` | `light` | `model` |
| `vtt_portmanteau` | `fit` | `raw_handle`, `integer`, `raw`, `boolean`, `number` | `h=4`, `univariate=False`, `alpha=0.05` | `light` | — |
| `vtt_arch` | `fit`, `seed` | `raw_handle`, `integer`, `integer`, `integer`, `boolean`, `boolean`, `enum`, `num_array`, `number` | `h=2`, `B=499`, `ET=True`, `MARCH=True`, `alpha=0.05` | `heavy` | — |
| `vtt_wildboot` | `fit`, `seed` | `raw_handle`, `integer`, `raw`, `enum`, `integer`, `enum`, `boolean`, `integer`, `number` | `h=4`, `B=199`, `univariate=False`, `alpha=0.05` | `heavy` | — |

### Use when

After estimating a reduced-form VAR (vr_var #11 -> varest, or the native vtt_fit -> VARfit): checking the adequacy of the residuals before structural ID/IRF. Autocorrelation (the Ahlgren-Catani multivariate LM + HC0-HC3 + per equation), ARCH/volatility clustering (the combined CA + Eklund-Terasvirta CCC-ARCH + multivariate MARCH, bootstrapped), wild-bootstrap AC p-values for a small/heteroskedastic sample.

### Do not use when

Estimating/selecting the lags of the VAR -> #11 (vr_var); a cointegration bootstrap (cointBootTest) -> category 05; residual normality (VARtests has NO normality test); producing IRF/FEVD (this is purely diagnostics); a bare residual matrix as input (the LM auxiliary regressions need the whole fitted model).

### Prerequisites

- c03_multivariate_nowcasting/reduced_form_var.vr_var
- vtt_fit

### Alternatives

| instead use | when |
| --- | --- |
| vtt_wildboot | A small sample or heteroskedastic errors: wild-bootstrap p-values (Ahlgren-Catani Algorithm 1/2) instead of the asymptotic chi^2 of vtt_portmanteau. |
| vtt_arch | The test concerns ARCH/volatility clustering in the residuals (not autocorrelation). |
| #11 vr_var | Autocorrelation is rejected -> increase the lags of the reduced-form VAR and re-test. |

### Output fields

- vtt_portmanteau: a multivariate data_frame (HCtype, statistic Q, p_value, df=K^2*h, decision) + h/K/alpha/inputType; univariate=TRUE -> an additional per-equation data_frame (df=h)
- vtt_arch: a list per test -> CA {statistic=1-min_i p(LM_i), boot.p, uni.stat, uni.boot.p, decision}; MARCH {statistic, asymp.p, boot.p, df=K^2(K+1)^2 h/4, decision}; ET {statistic, asymp.p, boot.p, df=K*h, decision} + B/dist/seed
- vtt_wildboot: a wild data_frame (HCtype, the statistic from ACtest, WB.p, df, decision) + WBtype/WBdist/numberOfErrors/numberOfNA/seed
- vtt_fit: the model handle (a 'VARfit' producer) + K/p/N/variables/residuals (chart-data)

### Pitfalls

- Polarity: H0 = CLEAN residuals (no AC / no ARCH). p<alpha => reject => misspecification is present (autocorrelation/ARCH) => the VAR FAILS the test (not the other way round).
- vtt_arch & vtt_wildboot are bootstrap-based => the seed is MANDATORY; the same seed => the same bootstrap p-values (cache key); without a seed they are uncacheable.
- The CA (Catani-Ahlgren) test ALWAYS runs inside vtt_arch: the package errors with 'CA_LMi not found' when CA=FALSE. The CA statistic is bootstrap-only (no asymptotic p/df); only the ET/MARCH toggles are exposed.
- Input = a fitted VAR (VARfit or varest), NOT a bare residual matrix: residuals alone give silently wrong LM auxiliary regressions (the gate.vtt_check_fit blocks it).
- univariate: only FALSE/TRUE — the package's 'only' value errors (blocked). MARCH df=K^2(K+1)^2 h/4 grows rapidly with K => a small sample => low power. The wildBoot p-values are in WBr.pv (recursive) or WBf.pv (fixed).

### References

- Ahlgren, N. & Catani, P. (2016), 'Wild bootstrap tests for autocorrelation in vector autoregressive models', Statistical Papers, doi:10.1007/s00362-016-0744-0
- Catani & Ahlgren 2016 (the combined bootstrap LM ARCH test); Eklund & Teräsvirta 2007 (CCC-ARCH LM); Lütkepohl 2006, New Introduction to Multiple Time Series Analysis, sect. 16.5 (multivariate ARCH-LM); MacKinnon & White 1985 (HCCME)
