<!-- SPDX-License-Identifier: AGPL-3.0-only -->
# 19-business-cycle-dating

4 METHOD-SELECTION cards, 4 modules, 7 nodes.

Every card below governs one wrapper module in this package. The cards are the
reason a method exists here at all: they record when it applies, what to reach
for instead, and the traps that make its output easy to misread.

## #88 — Harding-Pagan BBQ (Quarterly Bry-Boschan turning points)

**Module:** `harding_pagan_bbq.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `date_business_cycles` | `y` | `series_handle`, `integer`, `integer`, `string` | `mincycle=5`, `minphase=2` | `light` | `bcdating` |
| `average_over_phases` | `series`, `dates` | `series_handle`, `raw_handle` | — | `light` | — |

### Use when

a quarterly univariate series; dating peaks/troughs & phases (expansion/recession), NBER-style, without a model

### Do not use when

a non-quarterly frequency; you want probabilistic regimes (MSwM) or a cyclical gap (filters) or a multivariate cycle

### Alternatives

| instead use | when |
| --- | --- |
| Markov-switching (MSwM, regime) | you want regime probabilities + endogenous transitions instead of deterministic dates; gaussian/lm only |
| HP/band-pass/Hamilton filter (mFilter/hpfilter, 10) | you want a continuous cyclical gap instead of discrete turning points |
| State-space/DFA (KFAS/MARSS, 10) | a latent common cycle from several series |
| Monthly Bry-Boschan | monthly data (outside the surface of this package) |

### Output fields

- states: ts of the regime, +1=expansion / -1=recession per quarter
- peaks_index/troughs_index: index positions inside the series (not dates)
- peaks_date/troughs_date: peaks/troughs as 'YYYYQn' labels
- phases: data_frame type/start/end/duration/state/complete
- avg_expansion_duration/avg_recession_duration: the mean duration over complete phases only
- n_complete_phases: complete (non-censored) phases
- bcdating: raw S4 BCDating fit (to_mcp -> stub)

### Pitfalls

- sign convention: +1=expansion, -1=recession — not the reverse, not a z-score
- peaks/troughs are position indices, NOT dates; a peak = the end of an expansion/the start of a recession
- the edge phases are censored (complete=FALSE); they are excluded from the means — do not compare them with complete ones
- an interior NA in avgts -> an error (not a silent omission); an all-NA input is rejected
- mincycle/minphase determine the number of turning points; the dating is not unique; mincycle>minphase (gate)
- deterministic (v0.9.8, legacy/archived); no RNG

### References

- Harding-Pagan 2002 'Dissecting the Cycle' JME 49(2) 365-381
- Bry-Boschan 1971 (the ancestor of algorithmic dating)
- BCDating v0.9.8 ref manual (BBQ, avgts help pages)
- wrapper footer IMPLEMENTATION NOTE (c19_business_cycle_dating/harding_pagan_bbq)

## #213 — Change-point detection in mean / variance / mean+variance (PELT/BinSeg/SegNeigh/AMOC)

**Module:** `change_point_detection.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `detect_changepoints` | `x` | `series_handle`, `enum`, `enum`, `number`, `enum`, `integer`, `string`, `integer`, `boolean`, `number`, `number` | `pen_value=0`, `Q=5`, `know_mean=False`, `shape=1` | `light` | `fit` |
| `changepoint_segments` | `fit` | `raw_handle` | — | `light` | — |

### Use when

a univariate series; locating the POSITIONS of structural changes in the mean, the variance, or both (meanvar) with penalized exact/approximate segmentation; any frequency (not only quarterly)

### Do not use when

you want NBER-style expansion/recession phase dating (BBQ #88); probabilistic regimes (MSwM); breaks in regression coefficients with dates (strucchange/Bai-Perron); a continuous cyclical gap (filters)

### Alternatives

| instead use | when |
| --- | --- |
| Harding-Pagan BBQ (BCDating, #88) | you want cycle dating (peaks/troughs/phases) on a QUARTERLY series, not the positions of a structural break in the mean/variance |
| Bai-Perron / CUSUM (strucchange) | breaks in regression COEFFICIENTS (structural stability), not in the level's mean/variance |
| Markov switching (MSwM) | you want regime probabilities + endogenous transitions rather than deterministic break positions |
| statistic=mean vs variance vs meanvar | mean: a level change; variance: a change in volatility (volatility regimes); meanvar: a simultaneous change in level & volatility |
| method PELT vs BinSeg vs SegNeigh vs AMOC | PELT: exact, linear cost, an unknown number of breaks (default); BinSeg: approximate and fast up to Q; SegNeigh: exact but slow up to Q; AMOC: at most ONE break |

### Output fields

- changepoints: 1-based SEGMENT-END INDICES (NOT the final n, NOT dates)
- n_changepoints/n_segments: the number of breaks and of segments (=breaks+1)
- segments: a data_frame segment/start/end/length + per-segment parameter columns (mean/variance/scale/rate/lambda depending on test.stat)
- segment_params/global_params: per-segment vs global (e.g. the Gamma shape, the assumed mean for a variance model) parameter estimates
- penalty/method/test_stat/minseglen/Q/pen_value_used: the rules that produced the segmentation (an audit trail)
- fit: the raw S4 'cpt' fit (to_mcp -> a stub; a register field for the changepoint_segments accessor node)

### Pitfalls

- changepoints are SEGMENT-END INDICES (the last observation of a segment), 1-based; they do NOT include the final n; they are not dates
- the param.est field names CHANGE with test.stat: mean/variance(Normal); scale+shape(Gamma); rate(Exponential); lambda(Poisson) — do not always assume mean/variance
- cpt.var: the mean is handled separately (estimated by MLE or supplied via know_mean/mu); it is a GLOBAL parameter (the assumed mean), not per segment
- the placement is STABLE even in the degenerate nseg==1 case (no change): the assumed common mean (variance/know_mean) and the Gamma 'shape' are ALWAYS in global_params, NEVER in segment_params/segments; per segment: mean(mean/meanvar)/variance/scale/rate/lambda
- penalty='Manual' requires pen_value>0 (0 => no penalty => over-segmentation); 'None' segments at every point; 'Asymptotic' needs pen_value ∈ (0,1]
- CSS/CUSUM (non-parametric) do NOT work with PELT — they require AMOC/BinSeg/SegNeigh (a hard gate)
- BinSeg/SegNeigh: Q (the maximum number of breaks/segments) must satisfy Q < n/minseglen; AMOC finds at most 1 break
- a matrix input means MANY datasets to the package (a silent list, not a cpt object); the node accepts univariate input only (gate); an interior NA -> an error (the regularly-spaced requirement)
- deterministic — no RNG in AMOC/PELT/BinSeg/SegNeigh (verified with identical); no seed is needed

### References

- Killick, Fearnhead & Eckley 2012 'Optimal detection of changepoints with a linear computational cost' (PELT) JASA 107(500) 1590-1598
- Killick & Eckley 2014 'changepoint: An the reference Package for Changepoint Analysis' JSS 58(3) 1-19
- Scott & Knott 1974 (Binary Segmentation) Biometrics 30(3) 507-512; Auger & Lawrence 1989 (Segment Neighbourhoods) Bull. Math. Biol. 51(1) 39-54
- Zhang & Siegmund 2007 (MBIC) Biometrics 63 22-32; Hinkley 1970 (a change in mean) Biometrika 57 1-17
- changepoint v2.3 ref manual — the cpt.mean/cpt.var/cpt.meanvar/cpts/param.est help pages (args/values confirmed live)
- wrapper footer IMPLEMENTATION NOTE (c19_business_cycle_dating/change_point_detection)

## #214 — Bayesian change point (the Barry-Hartigan Product-Partition Model, MCMC)

**Module:** `bayesian_change_point.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `detect_change_points` | `y` | `series_handle`, `number`, `number`, `integer`, `integer`, `number`, `integer` | `p0=0.2`, `w0=0.2`, `burnin=50`, `mcmc=500`, `threshold=0.5`, `seed=20240719` | `mcmc` | — |

### Use when

a univariate sequential series; Bayesian detection of change points in the MEAN with a posterior probability of change at EVERY position (the Barry-Hartigan PPM, MCMC); you want soft/posterior probabilities & Bayesian model averaging rather than deterministic dates or a MAP segmentation

### Do not use when

you want NBER-style peaks/troughs & dated expansion/recession phases (→#88 BCDating); a change in variance/the whole distribution, or multivariate data (→ecp/changepoint); a regression/panel/graph change point (scoped out: x/id/adj); a length < 4 (a segfault gate)

### Alternatives

| instead use | when |
| --- | --- |
| Harding-Pagan BBQ (BCDating, #88) | you want NBER-style peaks/troughs & dated phases (deterministic dates) rather than a posterior probability of a change in the mean |
| Frequentist PELT/BinSeg (the changepoint package) | you want an exact MAP segmentation with a penalty (mean/var/meanvar), not Bayesian posterior averaging |
| E-Divisive / ECP (ecp) | a non-parametric change in the WHOLE distribution (not only the mean), multivariate |
| Markov switching (MSwM) | probabilistic regimes with endogenous transition probabilities rather than a partition/change point |

### Output fields

- posterior_prob: an array of length n; the posterior probability of a change AT each position; the LAST element = NA (the last position cannot host a change) → JSON null
- posterior_mean: the smoothed posterior level per position (model-averaged, NOT constant within a block)
- posterior_var: the posterior variance per position (finiteness/non-negativity gated; roundoff negatives ~-1e-14 → 0; genuine negatives < -1e-8 → a hard stop)
- changepoint_index: the 1-based positions where posterior_prob > threshold (the final NA is excluded automatically)
- changepoint_prob: the posterior probabilities at the detected positions; n_changepoints: the count
- posterior_expected_blocks: the POST-BURN-IN mean(blocks[(burnin+1):(burnin+mcmc)]) — the expected number of segments (consistent with the other post-burn-in summaries; NOT the all-iteration mean)
- threshold/p0/w0/burnin/mcmc/seed: the audit trail of the rules/parameters
- bcp_fit: the raw S3 'bcp' fit (to_mcp -> a stub)

### Pitfalls

- the LAST posterior_prob is NA by construction (the last position cannot host a change — there is no following block); do not read it as 0
- a change AT position i ⇒ a block boundary AFTER i (the new segment starts at i+1); it is a position index, NOT a date
- posterior_mean is NOT constant within a segment (it is a Bayesian average over partitions); no single 'best' partition is returned — that is deliberate (Barry-Hartigan)
- STOCHASTIC (MCMC): the seed is mandatory for reproducibility; the same seed ⇒ an identical result, without reseeding two calls differ
- bcp accepts NA/Inf SILENTLY and produces garbage (live-verified) → a hard gate here (no NA/Inf)
- length(y) < 4 causes a SEGFAULT in the C core rcpp_bcpM (live-verified: n=2,3 crash) → a hard gate (>= 4)
- p0 = the prior probability of a change (larger ⇒ more changes); w0 = the signal-to-noise prior; the detection depends on p0/w0 + the threshold — it is not unique
- the p0 domain is (0,1] (a hard gate): p0=0 is REJECTED as a degenerate prior that structurally forbids any change (it would silently return zero change points for ANY series)
- the regression/multivariate/graph case (x/id/adj/d/nreg/return.mcmc) is scoped out — univariate mean change only

### References

- Barry & Hartigan 1993 'A Bayesian Analysis for Change Point Problems' JASA 88(421) 309-319 [the Product-Partition Model]
- Erdman & Emerson 2007 'bcp: An the reference Package for Performing a Bayesian Analysis of Change Point Problems' J. Stat. Software 23(3)
- Wang & Emerson 2015 'Bayesian change point analysis of linear models on graphs' (the bcp >= 4.0 methods)
- bcp v4.0.4 ref manual — the bcp help page (live-verified)
- wrapper footer IMPLEMENTATION NOTE (c19_business_cycle_dating/bayesian_change_point)

## #215 — Energy-statistics nonparametric multivariate change-point detection (E-divisive / E-agglomerative)

**Module:** `energy_statistics_nonparametric.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `detect_changepoints_divisive` | `X` | `matrix_handle`, `number`, `integer`, `integer`, `number`, `integer`, `integer` | `sig_lvl=0.05`, `n_permutations=199`, `min_size=30`, `alpha=1`, `seed=20240101` | `light` | — |
| `detect_changepoints_agglo` | `X` | `matrix_handle`, `int_array`, `number`, `enum` | `alpha=1` | `light` | — |

### Use when

a multivariate (n×d) series; detecting MULTIPLE change points in the distribution (mean/variance/higher moments) without a parametric assumption, based on the energy distance; divisive = permutation-test significance, agglo = penalized bottom-up merging

### Do not use when

univariate turning-point dating of peaks/troughs (→BCDating #88); you want probabilistic regimes (MSwM); you want a cyclical gap (filters, cat. 10); you want a structural break in regression coefficients (strucchange/CUSUM); a very small n (< 2*min.size)

### Alternatives

| instead use | when |
| --- | --- |
| detect_changepoints_divisive (E-divisive) | you want a data-driven number of change points with formal permutation-test significance (p-values per split); stochastic → seeded; the default choice |
| detect_changepoints_agglo (E-agglomerative) | you have an initial segmentation (member) or you want a deterministic bottom-up procedure with a penalized goodness of fit; no permutation test; faster with initial groups |
| Harding-Pagan BBQ (BCDating, #88) | univariate quarterly data; you want peaks/troughs & expansion/recession phases (turning points), not distributional change points |
| Markov switching (MSwM, regime) | you want regime probabilities + endogenous transitions rather than discrete change points; gaussian/lm only |
| strucchange/CUSUM (structural break tests) | a break in the coefficients of a linear model/regression, not in the distribution of the data |

### Output fields

- changepoints: the interior change points (sorted; position p = a change BEFORE observation p, 2<=p<=n); WITHOUT the boundaries 1 & n+1
- n_changepoints / n_segments: the number of changes and of segments (divisive: n_segments==k_hat, n_changepoints==k_hat-1); agglo: n_segments == n_changepoints+1 (CONTIGUOUS temporal segments, NOT length(unique(cluster)) — the cyclic clustering reuses labels)
- cluster: an integer vector assigning a segment to each observation (of length n)
- estimates_raw: the raw ecp .estimates WITH the boundaries (an audit trail)
- p_values (divisive): the p-value per split in order.found order; the LAST one = the terminating non-significant split; n_significant = the number with p<=sig.lvl (boundary-inclusive, matching the stopping rule 'if(pval>sig.lvl) break'); WHEN a fixed k is supplied → p_values are all NA + n_significant NA (no permutation)
- significance_tested (divisive): TRUE only when k=NULL (a permutation test was run); FALSE when a fixed k is supplied (e.divisive forces the reference=0 internally — the p_values are placeholders, NOT evidence)
- gof_progression/gof_final (agglo): the penalized goodness of fit per merging step
- alpha/sig_lvl/the reference/min_size/k/penalty: the rules that produced the result (an audit trail)
- seed (divisive): the seed that was used (reproducibility)

### Pitfalls

- the ecp .estimates INCLUDE the boundaries 1 and n+1 (divisive) / a cyclic wrap (agglo) — those are NOT change points; the wrapper removes them, report ONLY the changepoints field
- e.divisive is STOCHASTIC (the reference permutations); WITHOUT a seed the p-values (and borderline splits) change from call to call — the wrapper calls set.seed INSIDE (default 20240101)
- silently wrong: NA/Inf in X → ecp silently returns NO change point (not an error); the wrapper fences it
- silently wrong: 2*min.size > nrow(X) → silently no change point; the wrapper requires nrow(X) >= 2*min.size
- silently wrong: the reference=0 (or non-positive) → it RUNS but the p-values are meaningless; the wrapper requires a positive integer the reference
- p_values are NOT aligned with the sorted changepoints; they are in order.found order with one extra terminating (non-significant) split — use n_significant for the number of significant ones
- silently wrong: divisive with a fixed k forces the reference=0 → the placeholder p_values are all 0; do NOT read them as significance (significance_tested=FALSE, p_values/n_significant=NA); only the data-driven k=NULL gives tested significance
- silently wrong: the agglo clustering is CYCLIC → length(unique(cluster)) counts distinct distributions, NOT contiguous regimes (e.g. a symmetric mean 0→5→0 gives 2 clusters but 3 segments); use n_segments (=changepoints+1)
- alpha is the moment index of the energy distance in (0,2] (default 1), NOT a significance level — do not confuse it with sig.lvl
- e.agglo with penalty='none' can over-segment noisy data; 'num_cp' penalizes the count; the dating is NOT unique (it depends on alpha/member/penalty)

### References

- Matteson D.S., James N.A. (2014) 'A Nonparametric Approach for Multiple Change Point Analysis of Multivariate Data' JASA 109(505) 334-345 [e.divisive]
- James N.A., Matteson D.S. (2014) 'ecp: An the reference Package for Nonparametric Multiple Change Point Analysis of Multivariate Data' JSS 62(7) 1-25 [e.divisive & e.agglo]
- Székely G.J., Rizzo M.L. (2005) 'Hierarchical clustering via joint between-within distances' J. Classification 22 151-183 [the energy distance basis]
- ecp v3.1.6 ref manual (the e.divisive, e.agglo help pages, live-verified)
- wrapper footer IMPLEMENTATION NOTE (c19_business_cycle_dating/energy_statistics_nonparametric)
