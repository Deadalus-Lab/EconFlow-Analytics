<!-- SPDX-License-Identifier: AGPL-3.0-only -->
# 09-cross-section-networks

15 METHOD-SELECTION cards, 15 modules, 90 nodes.

Every card below governs one wrapper module in this package. The cards are the
reason a method exists here at all: they record when it applies, what to reach
for instead, and the traps that make its output easy to misread.

## #48 — Input-Output / Leontief analysis (full)

**Module:** `input_output_leontief.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `io_build` | `Z`, `RS_label`, `X` | `matrix_handle`, `matrix_handle`, `matrix_handle`, `matrix_handle`, `matrix_handle`, `matrix_handle`, `matrix_handle` | — | `light` | `object` |
| `io_leontief_inverse` | `Z` | `raw_handle` | — | `light` | — |
| `io_ghosh_inverse` | `Z` | `raw_handle` | — | `light` | — |
| `io_multipliers` | `io`, `multipliers` | `raw_handle`, `series_codes` | — | `light` | — |
| `io_linkages` | `io` | `raw_handle`, `series_codes`, `boolean` | — | `light` | — |
| `io_key_sector` | `io` | `raw_handle`, `number`, `series_codes` | `crit=1` | `light` | — |
| `io_field_of_influence` | `io`, `i`, `j` | `raw_handle`, `integer`, `integer` | — | `light` | — |
| `io_field_of_influence_total` | `io` | `raw_handle` | — | `light` | — |
| `io_extraction` | `io` | `raw_handle`, `series_codes` | — | `light` | — |

### Use when

a transactions matrix Z + X (+f/V): full IO analysis — Leontief/Ghosh inverse, multipliers, Rasmussen-Hirschman linkages, key sectors, field of influence, hypothetical extraction

### Do not use when

bare A/L/multiplier arithmetic only -> #49 leontief; RAS/location-quotient/aggregation (data prep, not exposed)

### Alternatives

| instead use | when |
| --- | --- |
| #49 leontief | you want only A/B/L/multipliers/linkages/dispersion, not Ghosh/key-sector/extraction |
| io_ghosh_inverse (supply-side) | downstream effect of a supply change rather than demand-side |
| io_extraction | a full 'what is lost if the sector disappears' rather than a plain multiplier |

### Output fields

- object$L: Leontief inverse (I-A)^-1 — total output of i per unit of final demand j
- multipliers: matrix [sectors x type] or a list per region (output=colSum(L))
- linkages: BL (backward, colSum) / FL (forward, rowSum) linkages
- key_sectors: Rasmussen-Hirschman quadrants (I = high BL&FL = a key sector)
- extraction/field_of_influence: inconsistent shape (a matrix or a nested list per region/type)

### Pitfalls

- linkages/key.sector: with normalize=FALSE (default), type='direct' == type='total' (a quirk, live-verified) — a message, not a block; use normalize=TRUE
- key.sector does NOT expose normalize -> the quirk is always active there
- extraction ALWAYS needs io$V regardless of type (otherwise 'invalid times argument')
- crit must be numeric; non-numeric -> a silently wrong classification through string coercion
- f.influence with i/j outside [1,n] -> 'subscript out of bounds' (gated)

### References

- Miller & Blair 2009 Input-Output Analysis 2nd ed.
- Rasmussen 1956 & Hirschman 1958 (linkages)
- Sonis & Hewings 1992 (field of influence)
- Dietzenbacher, van der Linden & Steenge 1993 (hypothetical extraction)

## #49 — Input-Output / Leontief (simple)

**Module:** `input_output_leontief_2.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `lt_input_requirement` | `X`, `d` | `matrix_handle`, `raw_handle` | — | `light` | — |
| `lt_augmented_input_requirement` | `X`, `w`, `c`, `d` | `matrix_handle`, `raw_handle`, `raw_handle`, `raw_handle` | — | `light` | — |
| `lt_output_allocation` | `X`, `d` | `matrix_handle`, `raw_handle` | — | `light` | — |
| `lt_leontief_inverse` | `A` | `matrix_handle` | — | `light` | — |
| `lt_equilibrium_output` | `L`, `d` | `matrix_handle`, `raw_handle` | — | `light` | — |
| `lt_output_multiplier` | `L` | `matrix_handle` | — | `light` | — |
| `lt_income_multiplier` | `L`, `w` | `matrix_handle`, `raw_handle` | — | `light` | — |
| `lt_employment_multiplier` | `L`, `e` | `matrix_handle`, `raw_handle` | — | `light` | — |
| `lt_backward_linkage` | `A` | `matrix_handle` | — | `light` | — |
| `lt_forward_linkage` | `A` | `matrix_handle` | — | `light` | — |
| `lt_power_dispersion` | `L` | `matrix_handle` | — | `light` | — |
| `lt_power_dispersion_cv` | `L` | `matrix_handle` | — | `light` | — |
| `lt_sensitivity_dispersion` | `L` | `matrix_handle` | — | `light` | — |
| `lt_sensitivity_dispersion_cv` | `L` | `matrix_handle` | — | `light` | — |
| `lt_multiplier_product_matrix` | `L` | `matrix_handle` | — | `light` | — |
| `lt_employment_number` | `L`, `e`, `c` | `matrix_handle`, `raw_handle`, `raw_handle` | — | `light` | — |

### Use when

a transactions matrix X + vectors (d/w/e): the classic Leontief operations, fast — A/B/L, equilibrium, multipliers, linkages, dispersion (+CV), MPM

### Do not use when

you need Ghosh/key-sector/field-of-influence/extraction/multiregional labels -> #48 ioanalysis

### Alternatives

| instead use | when |
| --- | --- |
| #48 ioanalysis | you want completeness (Ghosh/key-sector/extraction/multiregional) — they give bit-identical L/A/multipliers |

### Output fields

- A/B/L: technical input/output coefficients + the Leontief inverse
- output: L*d (output equilibrium)
- output_multiplier: named vector = colSum(L)
- backward_linkage/forward_linkage: normalized (>1 = above average)
- power/sensitivity_dispersion (+_cv): dispersion indices + CV

### Pitfalls

- income/employment_multiplier: pass an ALREADY normalised w/d or e/d (vignette), NOT a raw wage — it does not divide internally
- the C++ layer strips dimnames -> the wrapper puts them back (otherwise anonymous vectors)
- NA/NaN/Inf in the input propagate silently (gated with a finite check)
- a zero in d -> silent Inf in A/B/augmented (gated); d=0 is OK in equilibrium_output
- augmented -> (n+1)x(n+1) (a wage_over_demand row, a consumption_over_demand column)

### References

- Miller & Blair 2009
- vignette data: the Chilean economy 2013 (Central Bank of Chile)

## #50 — Global VAR (GVAR)

**Module:** `global_var.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `gv_fit` | `data`, `weight_matrix`, `ic` | `df_handle`, `matrix_handle`, `integer`, `enum`, `enum` | `p=2` | `light` | `object` |
| `gv_foreign_variables` | `data`, `weight_matrix` | `df_handle`, `matrix_handle` | — | `light` | — |
| `gv_structural` | `data`, `weight_matrix` | `df_handle`, `matrix_handle`, `integer`, `enum`, `enum` | `p=2` | `light` | — |
| `gv_residual_correlation` | `out` | `raw_handle` | — | `light` | — |
| `gv_coef` | `out`, `sheet` | `raw_handle`, `integer` | — | `light` | — |
| `gv_coef_nw` | `out`, `sheet` | `raw_handle`, `integer` | — | `light` | — |
| `gv_coef_white` | `out`, `sheet` | `raw_handle`, `integer` | — | `light` | — |
| `gv_coef_exo` | `out` | `raw_handle` | — | `light` | — |
| `gv_coef_exo_nw` | `out` | `raw_handle` | — | `light` | — |
| `gv_coef_exo_white` | `out` | `raw_handle` | — | `light` | — |

### Use when

a panel of many countries (the same variables) + bilateral trade weights: country-specific VAR with weighted foreign variables — cross-border spillovers

### Do not use when

one country -> VAR (vars/03); cointegration -> Global VECM (not exposed); IRF (not implemented in the package)

### Prerequisites

- c01_preparation_prechecks/unit_root_normality.run_adf_test (+ KPSS confirmatory) — stationarity per variable

### Alternatives

| instead use | when |
| --- | --- |
| VAR (vars/03) | one country, or the weighting structure does not matter to you |
| #51 ConnectednessApproach | you want spillover matrices instead of structural coefficients; no external weight matrix |
| Global VECM | cointegration dominates (out of scope) |

### Output fields

- country_var_models: a list of varest objects (one per country, via country_names)
- coef_white/coef_nw: coefficients with White/Newey-West HAC SE; gv_coef*(sheet=k) the coefficient table of country k
- foreign_variables: weighted foreign variables per country (the heart of the GVAR)
- gv_residual_correlation: mean cross-sectional residual cor, VAR vs GVAR (a reduction is good)
- gv_structural: G0/G1/G2/F1/F2 structural matrices (for downstream IRF/forecast)

### Pitfalls

- weight_matrix is accessed POSITIONALLY -> the wrong column order = silently wrong (gated where the mis-order is detectable)
- the 'ID' column is EXACTLY upper case (the documentation says 'id' — stale); Time must be a character-parseable date (not an integer)
- weight_matrix is mandatory (NULL bug); a real N x N matrix (not a data_frame); a zero diagonal
- p is restricted to {1,2} (documented); >=2 variables; a strictly balanced panel
- GVAR_GF returns only G0/G1/F1 when the minimum lag=1 (data-driven shape)

### References

- Pesaran, Schuermann & Weiner 2004 (JBES 22:129)
- Dees, di Mauro, Pesaran & Smith 2007 (J. Applied Econometrics 22:1)
- di Mauro & Pesaran 2013 The GVAR Handbook

## #51 — Connectedness (Diebold-Yılmaz, full)

**Module:** `connectedness.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `dy_fit` | `x` | `irregular_series_handle`, `integer`, `integer`, `integer`, `boolean`, `enum` | `nlag=1`, `nfore=10` | `light` | — |
| `dy_var` | `x` | `irregular_series_handle`, `integer` | `nlag=1` | `light` | — |
| `dy_time_connectedness` | — | `matrix_handle`, `matrix_handle`, `integer`, `boolean`, `boolean`, `matrix_handle` | `nfore=10` | `light` | — |
| `dy_table` | `FEVD` | `matrix_handle`, `integer` | `digit=2` | `light` | — |

### Use when

a multivariate series (markets/returns/macro): a spillover matrix from the VAR FEVD (Diebold-Yılmaz) — static/rolling/TVP-VAR; TCI/TO/FROM/NET

### Do not use when

you want a decomposition per frequency band -> #52; a structural GVAR of countries -> #50; univariate (meaningless)

### Prerequisites

- c01_preparation_prechecks/unit_root_normality.run_adf_test (+ KPSS) — stationarity (the VAR requires it)

### Alternatives

| instead use | when |
| --- | --- |
| #52 frequencyConnectedness | the distribution of spillovers per frequency band (short/long run) |
| generalized=TRUE vs FALSE | generalized (Pesaran-Shin, order-invariant) with no Cholesky ordering; orthogonalized with a structural ordering |
| model=TVP-VAR vs rolling VAR | TVP = smooth variation over time; rolling = discrete windows |

### Output fields

- TCI: Total Connectedness Index (%) — systemic interconnection
- TO/FROM: transmits to / receives from; NET=TO-FROM (positive=net transmitter)
- NPT/NPDC: net pairwise directional connectedness
- TABLE/CT: the full spillover matrix (row=origin, column=recipient)

### Pitfalls

- Diebold-Yılmaz = predictive/forecast-error connectedness, NOT structural causality
- minimum sample n>=nlag*(k+1)+2 (VAR); otherwise silent NaN se/a wrong dimension (gated)
- x MUST be a zoo (Date index) & have >=2 columns
- connectedness is fixed to 'Time' (frequency = #52); model is restricted to VAR/TVP-VAR
- the package message ('Estimating model') goes to stderr — not a violation of the no-print rule

### References

- Diebold & Yılmaz 2009 (Economic Journal 119:158) & 2012 (Int. J. Forecasting 28:57)
- Diebold & Yılmaz 2014 (J. Econometrics 182:119)
- Pesaran & Shin 1998 (Economics Letters 58:17, generalized FEVD)

## #52 — Frequency connectedness (Baruník-Křehlík)

**Module:** `frequency_connectedness.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `fq_spillover_bk12` | `est` | `raw_handle`, `integer`, `boolean`, `raw_handle` | `n_ahead=100` | `light` | `spillover_table` |
| `fq_spillover_bk09` | `est` | `raw_handle`, `integer`, `boolean`, `raw_handle` | `n_ahead=100` | `light` | `spillover_table` |
| `fq_spillover_rolling_bk12` | `data` | `multiseries_handle`, `integer`, `boolean`, `raw_handle`, `integer` | `n_ahead=100` | `light` | `list_of_spills` |
| `fq_spillover_rolling_bk09` | `data` | `multiseries_handle`, `integer`, `boolean`, `raw_handle`, `integer` | `n_ahead=100` | `light` | `list_of_spills` |
| `fq_fevd` | `est` | `raw_handle`, `integer`, `boolean` | `n_ahead=100` | `light` | — |
| `fq_gen_fevd` | `est` | `raw_handle`, `integer`, `boolean` | `n_ahead=100` | `light` | — |
| `fq_get_partition` | `partition`, `n_ahead` | `raw_handle`, `integer` | — | `light` | — |
| `fq_from` | `spillover_table` | `raw_handle`, `boolean` | — | `light` | — |
| `fq_to` | `spillover_table` | `raw_handle`, `boolean` | — | `light` | — |
| `fq_net` | `spillover_table` | `raw_handle`, `boolean` | — | `light` | — |
| `fq_overall` | `spillover_table` | `raw_handle`, `boolean` | — | `light` | — |
| `fq_pairwise` | `spillover_table` | `raw_handle`, `boolean` | — | `light` | — |
| `fq_collapse_bounds` | `spillover_table`, `which` | `raw_handle`, `raw_handle` | — | `light` | — |

### Use when

spillovers between variables PER frequency band (short/business-cycle vs long/trend) — Baruník-Křehlík 2018 frequency-decomposed DY

### Do not use when

the frequency decomposition does not matter to you -> #51 (the static DY is deliberately omitted here)

### Prerequisites

- c03_multivariate_nowcasting/reduced_form_var.vr_var (chaining: est = vr_var(y,..).model, class varest)
- c01_preparation_prechecks/unit_root_normality.run_adf_test — stationarity for the upstream VAR

### Alternatives

| instead use | when |
| --- | --- |
| #51 ConnectednessApproach | the total spillover suffices, or you want TVP/QVAR built in |
| spilloverBK12 (generalized) vs BK09 (recursive/Cholesky) | BK12 is order-invariant (the dominant choice); BK09 uses a Cholesky ordering |
| within=TRUE vs FALSE | within = % inside the band; FALSE = the absolute contribution to the total |

### Output fields

- tables: a list of spillover matrices, one per frequency band; bounds: the band boundaries
- fq_overall.overall: total connectedness per band (where the interconnection sits: short/long)
- fq_from/to/net/pairwise: FROM/TO/NET per band

### Pitfalls

- SECURITY: spilloverRolling calls get(func_est) (eval-by-name) -> func_est=match.arg('VAR') is a mandatory check
- partition is mandatory & must be in DESCENDING order; no.corr is a mandatory logical
- fq_collapse_bounds(which) must be a CONTIGUOUS increasing sequence (e.g. 1:2); otherwise silently wrong
- est MUST be varest/vec2var (chained from VAR)

### References

- Baruník & Křehlík 2018 (J. Financial Econometrics 16:271)
- Diebold & Yılmaz 2012 (the non-frequency basis)

## #53 — Spatial regression (lag/error)

**Module:** `spatial_regression.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `spr_fit_lag` | `formula`, `data`, `listw` | `formula`, `df_handle`, `raw_handle`, `boolean`, `enum`, `boolean` | — | `light` | `object` |
| `spr_fit_error` | `formula`, `data`, `listw` | `formula`, `df_handle`, `raw_handle`, `boolean`, `enum`, `boolean` | — | `light` | `object` |
| `spr_fit_sac` | `formula`, `data`, `listw` | `formula`, `df_handle`, `raw_handle`, `raw_handle`, `boolean`, `enum`, `boolean` | — | `light` | `object` |
| `spr_impacts` | `obj` | `raw_handle`, `raw_handle`, `integer` | — | `heavy` | — |
| `spr_summary` | `object` | `raw_handle`, `boolean`, `boolean`, `boolean` | — | `light` | — |
| `spr_lr_test` | `x`, `y` | `raw_handle`, `raw_handle` | — | `light` | — |
| `spr_hausman_test` | `object` | `raw_handle`, `number` | — | `light` | — |
| `spr_bptest` | `object` | `raw_handle`, `boolean` | — | `light` | — |

### Use when

cross-sectional data with spatial dependence: ML estimation of spatial lag (SAR, rho)/error (SEM, lambda)/SAC-SARAR + impacts (direct/indirect/total)

### Do not use when

only building weights / testing autocorrelation -> #54; GMM/2SLS/Bayesian/SLX (not exposed); no spatial structure -> lm

### Prerequisites

- c09_cross_section_networks/spatial_weights_diagnostics.spw_listw (building listw — a mandatory input)
- c09_cross_section_networks/spatial_weights_diagnostics.spw_moran_test (is there any spatial autocorrelation at all? otherwise this is pointless)

### Alternatives

| instead use | when |
| --- | --- |
| SAR (spr_fit_lag) | the neighbouring dependent variable has a substantive effect (spillover) |
| SEM (spr_fit_error) | the spatial dependence is a nuisance in the errors |
| SAC/SARAR (spr_fit_sac) or Durbin=TRUE (SDM/SDEM) | both, or + spatial lags of the regressors |

### Output fields

- coefficients/coef_table: Estimate/SE/z/p; rho (SAR)/lambda (SEM) spatial parameters + SE
- spr_impacts: direct/indirect/total effects — REQUIRED to interpret lag/Durbin (the raw coefficients are misleading)
- lr_test_vs_ols/wald_test_rho/lm_test: spatial dependence diagnostics (htest atomic)
- hausman_test: error models ONLY; bp_test: Breusch-Pagan heteroskedasticity

### Pitfalls

- spr_impacts is MANDATORY for lag/Durbin/SAC: the raw coefficients are misleading because of the feedback through W
- method='moments' was excluded (it fails on ML fits); Hausman is for error models ONLY (gated)
- listw MUST be of class 'listw' (a plain matrix -> 'No neighbourhood list')
- an invalid Durbin value (a non-formula string) -> silently ignored (fallback FALSE, gated)
- quiet=TRUE is always hardcoded (otherwise cat/print during the optimisation)

### References

- Anselin 1988 Spatial Econometrics
- LeSage & Pace 2009 Introduction to Spatial Econometrics (direct/indirect/total impacts)
- Bivand & Piras 2015 (JSS, spatialreg/spdep)

## #54 — Spatial weights / diagnostics

**Module:** `spatial_weights_diagnostics.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `spw_knn_nb` | `coords` | `matrix_handle`, `integer` | `k=1` | `light` | `neighbours` |
| `spw_dnearneigh_nb` | `coords`, `d1`, `d2` | `matrix_handle`, `number`, `number` | — | `light` | `neighbours` |
| `spw_cell2nb` | `nrow`, `ncol` | `integer`, `integer`, `enum`, `boolean` | — | `light` | `neighbours` |
| `spw_listw` | `neighbours` | `raw_handle`, `enum` | — | `light` | `listw` |
| `spw_nb_diagnostics` | `neighbours` | `raw_handle` | — | `light` | — |
| `spw_listw_constants` | `listw` | `raw_handle`, `boolean` | — | `light` | — |
| `spw_moran_test` | `x`, `listw` | `raw_handle`, `raw_handle`, `enum`, `boolean` | — | `light` | — |
| `spw_geary_test` | `x`, `listw` | `raw_handle`, `raw_handle`, `enum`, `boolean` | — | `light` | — |
| `spw_local_moran` | `x`, `listw` | `raw_handle`, `raw_handle`, `enum`, `boolean` | — | `light` | — |
| `spw_joincount_test` | `fx`, `listw` | `raw_handle`, `raw_handle`, `enum`, `enum` | — | `light` | — |

### Use when

preliminary work: building spatial weights from coordinates (kNN/distance/grid) + testing spatial autocorrelation (Moran/Geary/join-count/local Moran)

### Do not use when

estimating a spatial model -> #53; polygon GIS/shapefiles (poly2nb/sf not exposed); EB smoothing/MC tests (out of scope)

### Alternatives

| instead use | when |
| --- | --- |
| spw_knn_nb (k-NN) | a fixed number of neighbours per unit |
| spw_dnearneigh_nb (distance band) | adjacency by distance (a variable number) |
| spw_cell2nb (grid) | a regular grid of cells (rook/queen) |
| Moran vs Geary vs join-count vs local Moran | Moran is general; Geary captures local differences; join-count is for factors; local/LISA answers WHERE |

### Output fields

- neighbours (nb) / listw: spatial weights (style='W' row-standardized is the classic choice)
- spw_nb_diagnostics: cardinalities, no_neighbour_count, n_components (islands)
- moran_test/geary_test/joincount_test: htest atomic {statistic,p_value,estimate,alternative}
- local_moran: data_frame Ii/E.Ii/Var.Ii/Z.Ii/Pr + quadrant (HH/LL clusters, HL/LH outliers)

### Pitfalls

- Moran I: +1=positive autocorrelation (clusters), rejecting H0=structure is present
- Geary C has the INVERSE scale: C<1=positive autocorrelation, C=1 random, C>1 negative (do not read it like Moran)
- dnearneigh with d1>=d2 does NOT error -> silently an nb with zero neighbours everywhere (gated)
- na.action is NSE: it does not pass through do.call (deparse(substitute)) -> a literal switch
- geary_test does NOT allow na.action='pass' (structurally excluded)

### References

- Cliff & Ord 1981 Spatial Processes
- Moran 1950 (Biometrika 37:17); Geary 1954 (Incorporated Statistician 5:115)
- Anselin 1995 (Geographical Analysis 27:93, LISA)

## #55 — Network analysis

**Module:** `network.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `ig_from_edgelist` | `edges` | `df_handle`, `boolean` | — | `light` | `object` |
| `ig_from_adjacency` | `adjmatrix` | `matrix_handle`, `enum`, `boolean` | — | `light` | `object` |
| `ig_centrality` | `graph` | `raw_handle`, `enum` | — | `light` | — |
| `ig_community_louvain` | `graph` | `raw_handle`, `number` | `resolution=1` | `light` | — |
| `ig_connectivity` | `graph` | `raw_handle`, `boolean`, `enum` | — | `light` | — |

### Use when

a network of nodes and edges (bank exposures/trade/sectors): building the graph + centrality + Louvain communities + connectivity/robustness

### Do not use when

a 'network' derived from time-series spillovers -> #51/#52; spatial adjacency from coordinates -> #54; plotting/IO/motifs/other community algorithms (not exposed)

### Alternatives

| instead use | when |
| --- | --- |
| #51/#52 connectedness | the network arises endogenously from the covariance of time series |
| centrality: degree/betweenness/closeness/eigenvector/page_rank | degree=direct links; betweenness=bridge/flow; eigenvector=connection to important nodes; page_rank=directed influence |

### Output fields

- ig_from_*: vcount/ecount, is_directed/is_weighted + object
- ig_centrality: named vectors per node (degree/betweenness/closeness/eigenvector/page_rank) + vertex_names
- ig_community_louvain: membership, modularity (>0.3 = good structure), n_communities
- ig_connectivity: density/transitivity_global/diameter/mean_distance/components/assortativity_degree

### Pitfalls

- cluster_louvain works on an undirected graph ONLY (gated)
- degree does NOT use weights (for a weighted degree -> strength, out of scope)
- weighted=c(TRUE,TRUE) (length>1) -> silently wrong (an unweighted graph, gated)
- mode='undirected'+weighted+an asymmetric adjmatrix: the docs say 'error if not' but live 2.3.3 only warns -> the wrapper enforces a hard error
- closeness on a disconnected graph -> NaN; assortativity with a uniform degree -> NaN (both documented)

### References

- Csárdi & Nepusz 2006 (InterJournal Complex Systems 1695)
- Freeman 1978 (Social Networks 1:215, centrality)
- Blondel et al. 2008 (J. Stat. Mechanics P10008, Louvain)
- Newman 2010 Networks: An Introduction

## #176 — Bayesian Global VAR (multi-country shrinkage + SV): estimation + generalized-FEVD spillovers/GIRF + a posterior-predictive forecast

**Module:** `bayesian_global_var.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `bgvar_fit` | `Data`, `W` | `raw`, `matrix_handle`, `integer`, `integer`, `integer`, `enum`, `boolean`, `integer`, `integer`, `boolean`, `boolean`, `integer` | `plag=1`, `draws=200`, `burnin=200`, `prior='MN'`, `SV=False`, `hold_out=0`, `thin=1`, `eigen=True`, `trend=False`, `seed=2025` | `mcmc` | `object` |
| `bgvar_spillover` | `object` | `raw_handle`, `integer`, `enum`, `string`, `integer` | `n_ahead=8`, `type='gfevd'`, `seed=2025` | `light` | — |
| `bgvar_predict` | `object` | `raw_handle`, `integer`, `num_array`, `integer` | `n_ahead=4`, `quantiles=[0.16, 0.5, 0.84]`, `seed=2025` | `light` | — |

### Use when

a multi-country (N>=2) system with cross-country spillovers; you want a Bayesian GVAR with shrinkage (MN/SSVS/NG), optional stochastic volatility, generalized spillover matrices (Diebold-Yilmaz) and density forecasts tied to a weight matrix W (trade/spatial)

### Do not use when

one country/equation (use VAR/BVAR, cat. 03); pure spillover connectedness without a global-VAR structure (#51 ConnectednessApproach); a frequentist GVAR without Bayesian shrinkage (#50 GVARX); a single-equation spatial regression with W (#53 spatialreg)

### Prerequisites

- bgvar_fit (read max_eigenvalue<1 = a stable VAR & geweke_perc/geweke_exceed_share = MCMC convergence before interpreting spillovers/forecasts)
- c00_data_utilities/reading_delimited_fixed.read_csv_data (load the country data before building the named list; names must contain NO dot)

### Alternatives

| instead use | when |
| --- | --- |
| #50 GVARX gv_fit (09-cross-section-networks/gv_fit) | a frequentist GVAR (OLS country VARs) — a small model, you want point estimates without Bayesian shrinkage/SV |
| #51 ConnectednessApproach dy_time_connectedness | you want only spillover/connectedness matrices (Diebold-Yilmaz) without a full global-VAR structural model & W |
| prior='NG' or 'SSVS' | many countries·variables -> stronger/adaptive shrinkage (MN = the fast baseline) |

### Output fields

- bgvar_fit: object (the register handle for spillover/predict); max_eigenvalue/stable_draw_share/trim_info (eigen-trimming of unstable draws); geweke_perc/geweke_exceed_share (Geweke convergence); K/variables/country_names; xglobal (the stacked data)
- bgvar_spillover type=gfevd: spillover_matrix K x K (GFEVD[i,j]=the contribution of j to the variance of i, rows sum to 1); from_others/to_others/net (Diebold-Yilmaz %); total_spillover_index
- bgvar_spillover type=girf: irf_median K x (n.ahead+1), the posterior median responses to the shock; quantiles
- bgvar_predict: forecast K x n.ahead x quantiles + forecast_median (chart-data); has_holdout; lps/rmse (non-NULL ONLY if hold_out>0 at fit time)

### Pitfalls

- GFEVD orientation (Lanne-Nyberg 2016 corrected): the ROWS sum to 1; spillover_matrix[i,j] = the contribution OF j TO the variance of i; from_i=sum over {j≠i}, to_j=sum over {i≠j} — do not confuse them
- max_eigenvalue>=1 or a low stable_draw_share -> the VAR has unstable draws; a high geweke_exceed_share -> the MCMC did not converge (raise draws/burnin) — do NOT interpret spillovers/forecasts before checking these (a stateless node: they are returned in the list, NOT to the console)
- lps/rmse are NULL when the fit used hold_out=0; for an out-of-sample evaluation you MUST set hold_out>0 in bgvar_fit (the has_holdout flag records it)
- naming convention: country AND variable names must NOT contain a dot '.' (it is the Country.Variable separator); W must have diag=0 & row sums=1 (row-standardized) with the countries as names
- the prior default here = 'MN' (the 1st match.arg value, fast) WHEREAS the package's native default is 'NG'; 'HS' (Horseshoe) was deliberately left out

### References

- Boeck, Feldkircher & Huber (2022), 'BGVAR: Bayesian Global Vector Autoregressions with Shrinkage Priors in the reference', JSS <
- Pesaran, Schuermann & Weiner 2004 (the GVAR framework); Lanne & Nyberg 2016 (the corrected GFEVD, J. Time Ser. Econom.)
- Diebold & Yilmaz 2012/2014 (the spillover/connectedness index from generalized variance decompositions)
- Koop, Pesaran & Potter 1996 (generalized impulse response functions)

## #177 — Spatial panel models (SAR/SEM/SDM · FE/RE/pooling) — ML & GM + spatial LM tests

**Module:** `spatial_panel_spatial.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `sp_panel_ml` | `formula`, `data`, `W` | `formula`, `df_handle`, `matrix_handle`, `enum`, `enum`, `boolean`, `enum`, `enum`, `series_codes` | `lag=True` | `light` | `object` |
| `sp_panel_gm` | `formula`, `data`, `W` | `formula`, `df_handle`, `matrix_handle`, `enum`, `boolean`, `boolean`, `enum`, `enum`, `enum`, `series_codes` | `lag=True`, `spatial_error=True` | `light` | `object` |
| `sp_panel_lmtest` | `formula`, `data`, `W` | `formula`, `df_handle`, `matrix_handle`, `enum`, `string`, `enum`, `series_codes` | `model='pooling'` | `light` | — |

### Use when

a panel (i,t) with SPATIAL dependence between units (geographic/network neighbours); you want a spatial lag (Wy) and/or a spatial error with an FE/RE test; you have an n x n weight matrix W

### Do not use when

no spatial structure (lag=FALSE & error=none -> a plain panel, #46 plm); a dynamic panel (a lagged dependent variable -> #47 GMM); a pure cross-section without a panel (-> #53 spatialreg); an unbalanced panel (splm ML/GM does not support it)

### Prerequisites

- c09_cross_section_networks/spatial_weights_diagnostics.spw_moran_test (is there any spatial autocorrelation at all before a spatial panel?)
- sp_panel_lmtest (lml=lag vs lme=error; the robust rlml/rlme -> which spatial form)
- c08_panel_data/static_panel_estimators.pd_hausman_test (the FE vs RE dimension, on the non-spatial baseline)
- c01_preparation_prechecks/panel_unit_root.run_purtest (macro/large-T only: a panel unit-root test first)

### Alternatives

| instead use | when |
| --- | --- |
| #53 spatialreg (spr_fit_lag/error/sac) | a pure cross-section (not a panel) spatial regression |
| #46 plm pd_fit | a panel with no spatial dependence (the LM tests do not reject) |
| sp_panel_gm (spgm) | endogeneity/robust GM/IV instead of ML, or when the ML optimisation does not converge |
| model=random | the spatial-specific effects are uncorrelated with the regressors (Hausman does not reject) |

### Output fields

- coefficients: a named vector (the regressors + the spatial parameters rho/lambda; the names depend on lag/error/model)
- coef_table: terms/estimate/std_error/statistic/p_value (the summary CoefTable)
- ar_table / errcomp_table: ARCoefTable / ErrCompTable (random only; NULL in the within case, where they are merged into coef_table)
- errcomp: the variance components (phi=the idiosyncratic share, rho=the spatial error); random only
- rho (spgm): the spatial autoregressive (lag) coefficient; sigma2: the idiosyncratic variance
- sp_panel_lmtest: statistic/p_value/method/alternative (htest; lml->lag, lme->error)

### Pitfalls

- splm naming: 'rho'/'lambda' swap roles between ML and GM — in the ML CoefTable lambda=the spatial error & rho=the spatial lag; in spgm the spatial-lag coefficient sits in the .rho field (coefficients.lambda = the error); read the labels, do not assume
- within (FE): the spatial parameters go into coef_table, NOT into a separate ar_table/errcomp_table (those are NULL) — the random model separates them
- an unbalanced panel fails (a clean 'balanced' gate); NA in the data fail cryptically in the listw subsetting -> an NA gate
- the number of spatial units MUST == nrow(W); the order of the units in W must match the order of the index (a silent misalignment otherwise)
- LM tests: lml tests the spatial LAG, lme the spatial ERROR; the robust ones (rlml/rlme) are robust to the presence of the other form — prefer them when both plain LM tests reject

### References

- Millo & Piras, 'splm: Spatial Panel Data Models in the reference', JSS 2012 47(1) (the splm vignette)
- help('spml','splm'), help('spgm','splm'), help('slmtest','splm')
- Baltagi, Song, Koh 2003; Kapoor, Kelejian, Prucha 2007 (KKP error components)
- Anselin 1988 Spatial Econometrics; Elhorst 2014 Spatial Econometrics: From Cross-Sectional Data to Spatial Panels

## #178 — Spatial GMM / GS2SLS (SARAR/lag/error) with heteroskedasticity-robust SEs

**Module:** `spatial_gmm_gs2sls.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `sp_gmm_reg` | `formula`, `data`, `W` | `formula`, `df_handle`, `matrix_handle`, `enum`, `boolean`, `enum`, `number`, `integer` | `model='sarar'`, `het=True`, `style='W'`, `initial_value=0.2`, `q=2` | `light` | `object` |

### Use when

a cross-sectional spatial regression with possible heteroskedasticity; you want GMM/GS2SLS (not ML) estimation of a spatial lag (Wy) and/or a spatial error (Wu) with het-robust standard errors (Kelejian-Prucha/Arraiz); you have a square spatial weight matrix W

### Do not use when

homoskedastic errors + you want ML efficiency/impacts (-> spatialreg #53); panel data (spml/another category); you need direct/indirect/total spillover effects (impacts — pass the fit to spatialreg); time series/non-spatial data

### Prerequisites

- c09_cross_section_networks/spatial_weights_diagnostics.spw_moran_test (Moran's I: is there any spatial autocorrelation to model?)
- c09_cross_section_networks/spatial_weights_diagnostics.spw_listw (building/checking a 'listw' from adjacency; here W is supplied as a matrix)
- c00_data_utilities/reading_delimited_fixed.read_delimited (loading cross-section data)

### Alternatives

| instead use | when |
| --- | --- |
| #53 spatialreg spr_fit_lag/spr_fit_error/spr_fit_sac (ML) | homoskedastic errors; you want maximum-likelihood efficiency + impacts spillover effects |
| sp_gmm_reg model=error | spatial dependence only in the errors (a nuisance), not a substantive Wy |
| sp_gmm_reg model=lag | a substantive spatial spillover in Wy, clean errors |
| sp_gmm_reg model=ols | a non-spatial baseline/benchmark |

### Output fields

- coefficients: a named vector — the beta regressors + lambda (the spatial LAG, Wy) + rho (the spatial ERROR, Wu)
- coef_table: Estimate/Std. Error/t-value/Pr(>\|t\|); the SE are ALREADY het-robust when het=TRUE
- spatial_lag: the Wy coefficient (sphet 'lambda'); spatial_error: the Wu coefficient (sphet 'rho'); NA if the model does not include them
- vcov: the coefficient covariance; s2: the residual variance; residuals/nobs
- nonstationary: TRUE if \|spatial coef\| >= 1 (non-stationary); se_na: TRUE if a robust SE came back NA

### Pitfalls

- the OPPOSITE convention to spatialreg: in sphet lambda=the spatial LAG (Wy), rho=the spatial ERROR (Wu); in #53 rho=lag, lambda=error. ALWAYS read spatial_lag/spatial_error (the explicit names), not raw lambda/rho
- het=TRUE => the SE in coef_table are ALREADY heteroskedasticity-robust; do NOT apply a robust vcov again
- GMM/GS2SLS does not produce direct/indirect/total impacts; to interpret the spillovers of a spatial lag model you need impacts (spatialreg)
- nonstationary=TRUE (\|coef\|>=1) => the spatial process is not invertible; the results are suspect (check the row standardization of W)
- a very large q (spatial instruments) with a small n => singular/'Hin not found' — keep q small (2)

### References

- Piras 2010, 'sphet: Spatial Models with Heteroskedastic Innovations in the reference', JSS 35(1) (the sphet vignette)
- args(spreg), summary.sphet (sphet 2.1.1) — live introspection
- Kelejian & Prucha 1998 (JREE 17:99), 1999 (Int. Econ. Rev. 40:509) — the GM/GS2SLS spatial estimator
- Arraiz, Drukker, Kelejian & Prucha 2010 (J. Regional Sci. 50:592) — het-robust GMM

## #179 — Spatial dynamic panel data model (Lee-Yu QML, fixed effects) + direct/indirect/total effects

**Module:** `spatial_dynamic_panel.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `sp_dynpanel` | `formula`, `data`, `W`, `index` | `formula`, `df_handle`, `matrix_handle`, `series_codes`, `enum`, `enum`, `boolean`, `boolean`, `boolean`, `integer`, `boolean`, `boolean` | `LYtrans=True`, `rowstand=True` | `light` | `object` |
| `sp_dynpanel_impacts` | `object` | `raw_handle`, `integer`, `integer` | `NSIM=200`, `seed=2025` | `light` | — |

### Use when

a balanced spatial panel (i,t) with spatial dependence; estimating a SAR/SDM with fixed effects, static or dynamic (a time and space-time lag of the dependent variable), and interpreting it through direct/indirect/total spatial spillovers

### Do not use when

a non-spatial panel (-> #46 plm / #47 pgmm); a spatial CROSS-SECTION of one period (-> #53 spatialreg); an unbalanced panel (SDPDm blocks it); a pure spatial error without a lag ('sem' is not supported here); a very small N or an N without a reliable W

### Prerequisites

- sp_dynpanel (the estimation itself: balanced-panel + square-W gates; it returns a converged flag)
- c09_cross_section_networks/spatial_weights_diagnostics.spw_listw (building/checking the spatial neighbourhoods before you build W)
- c00_data_utilities/reading_delimited_fixed.read_delimited (loading the long-format panel from a file)

### Alternatives

| instead use | when |
| --- | --- |
| #53 spatialreg (spr_fit_lag/spr_fit_error) | a spatial cross-section of one period (not a panel) |
| splm (spatial panel GM/ML, splm) | a static spatial panel without dynamics/Lee-Yu bias correction, or a spatial error (SEM) component |
| #46 plm / #47 pgmm | there is no spatial dependence; a plain static/dynamic panel |
| model='sdm' instead of 'sar' | the spillovers of the regressors (W*X) are substantive — otherwise direct≈total |

### Output fields

- coefficients: a named vector of regressor coefficients (in an SDM & in the dynamic case it includes the W*X and time-lag terms)
- coef_table: Estimate/Std. Error/t-value/Pr(>\|t\|) per regressor
- rho / rho_se / rho_tstat / rho_pval: the spatial autoregressive coefficient (spatial dependence)
- sige, log_likelihood, r_squared, adj_r_squared: fit diagnostics; model/effect/dynamic: the configuration that was estimated
- n_units/n_times: the panel dimensions; converged: TRUE if rho & the log-likelihood are finite
- impacts: direct/indirect/total (matrices Estimate/SE/t/p) + estimates/std_errors/t_stats/p_values

### Pitfalls

- The beta coefficient is NOT the marginal effect when rho!=0 — read the impacts (direct=own unit, indirect=spillover, total=direct+indirect); the same feedback loop as in #178
- 'sem' is not supported (match.arg allows only sar/sdm); for a spatial-error component go to splm
- impactsSDPDm is STOCHASTIC (an NSIM simulation) — the SE/p depend on the seed; always keep the seed fixed
- A BALANCED panel is required; NA or an unbalanced panel are blocked (SDPDm does not handle unbalanced data)
- W should ideally be row-standardized (rowstand=TRUE by default); a zero row (an isolated unit) is blocked during the row standardization
- dynamic=TRUE: tlaginfo(tl/stl) controls y_{t-1} and W*y_{t-1}; at least one of the two is needed
- converged=FALSE or all-NA coefficients -> do not trust the fit (a stateless node: we catch it in the output, not in stderr)

### References

- Yu, De Jong & Lee 2008 (J. Econometrics 146:118-134) — QML spatial dynamic panel, n & T large
- Lee & Yu 2010 (J. Econometrics 154:165-185) — SAR panel fixed-effects estimation/bias correction
- Lee & Yu 2010 (Econometric Theory 26:564-597) — a spatial dynamic panel with time + individual FE
- LeSage & Pace 2009, Introduction to Spatial Econometrics — the direct/indirect/total effects interpretation

## #180 — Moran eigenvector spatial regression — eigenvector spatial filtering (ESF) & random-effects ESF (RE-ESF, an approximate Gaussian process)

**Module:** `moran_eigenvector_spatial.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `sp_meigen` | `W` | `matrix_handle`, `enum`, `number`, `integer` | `threshold=0` | `light` | `object` |
| `sp_esf` | `object`, `y` | `raw_handle`, `num_array`, `matrix_handle`, `enum`, `number` | — | `light` | — |
| `sp_resf` | `object`, `y` | `raw_handle`, `num_array`, `matrix_handle`, `enum` | — | `light` | — |

### Use when

a cross-section with spatial dependence; you want to clean the spatial autocorrelation out of the residuals with Moran eigenvectors (ESF fixed effects) or to model it as a spatial random effect (RE-ESF ~ a Gaussian process), without imposing a SAR/SEM structure

### Do not use when

you want an explicit SAR/SEM/SDM with spatial-lag/error parameters & impacts (-> #53 spatialreg); panel data with i/t (-> splm); a pure autocorrelation diagnostic without a model (-> #54 spdep Moran/Geary); no valid W matrix

### Prerequisites

- sp_meigen (the PRODUCER: it extracts Moran eigenvectors from W; run it FIRST; its .object feeds sp_esf/sp_resf)
- c09_cross_section_networks/spatial_weights_diagnostics.spw_moran_test (confirm that spatial autocorrelation EXISTS before the ESF)
- c00_data_utilities/reading_delimited_fixed.read_delimited (load y/x/coords from a file)

### Alternatives

| instead use | when |
| --- | --- |
| #53 spatialreg spr_fit_lag/error/sac | you want an explicit SAR/SEM/SDM parameter (rho/lambda) + impacts (direct/indirect/total) |
| sp_resf (RE-ESF) instead of sp_esf (ESF) | you want a spatial random effect (an approximate GP) & variance components rather than stepwise fixed eigenvectors; better for a large N / a smooth surface |
| #54 spdep spw_moran_test/spw_local_moran | only an autocorrelation diagnostic, not a regression |

### Output fields

- coefficients: a data_frame Estimate/SE/t_value/p_value per regressor (intercept + x); x=NULL -> a named intercept-only vector
- moran_i: the scaled Moran's I in [0,1] of the estimated spatial component (0.25-0.50 weak, 0.50-0.70 moderate, 0.70-0.90 strong, 0.90-1.00 very strong — Griffith 2003)
- spatial_sd / random_sd: the standard deviation of the spatial (ESF) / spatial-random (RE-ESF) component
- gof: resid_SE/adjR2/log_lik/AIC/BIC (esf) · resid_SE/adjR2(cond)/rlog_lik/AIC/BIC (resf)
- spatial_effect: the N x 1 estimated spatial component/random effect (chart-data); fitted/residuals
- n_eigenvectors / eigenvalues / eigenvectors: (sp_meigen) the count & the scaled eigenvalues (max=1) & the N x L matrix (chart-data)

### Pitfalls

- sp_esf/sp_resf CONSUME the sp_meigen .object (the raw_handle 'object'); they do not rebuild the eigenvectors — if you changed W, re-run sp_meigen
- moran_i is SCALED to [0,1] (Moran.I/max(Moran.I)), NOT the raw Moran's I — do not compare it with the spw_moran_test statistic
- ESF (sp_esf) = fixed eigenvectors chosen stepwise (fn=r2/aic/bic); RE-ESF (sp_resf) = a spatial random effect (an approximate GP) — a different interpretation of the spatial term
- x=NULL -> intercept only; the esf coefficients are then a named numeric vector (not a data_frame) — handle both types
- W is symmetrised internally ((W+t(W))/2); an asymmetric input does not error but loses the directionality

### References

- Griffith 2003 Spatial Autocorrelation and Spatial Filtering (Springer) — the scaled Moran's I bands
- Tiefelsdorf & Griffith 2007 (Environment and Planning A 39:1193) — eigenvector ESF
- Murakami & Griffith 2015 (J Geographical Systems 17:311) — random-effects ESF
- Murakami & Griffith 2019 (Geographical Analysis 51:23) — ESF for large data sets (fixed & random)
- Dray, Legendre & Peres-Neto 2006 (Ecological Modelling 196:483) — the PCNM/MEM basis

## #181 — Network estimation for time series — a sparse VAR (Granger network) + a concentration/partial-correlation network via the NETS LASSO

**Module:** `network_estimation_time.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `nets_fit` | `y` | `matrix_handle`, `integer`, `num_array`, `num_array`, `enum`, `boolean`, `boolean`, `enum`, `enum`, `integer`, `integer`, `integer` | `p=1`, `GN=True`, `CN=True`, `iter_in=100`, `iter_out=2`, `seed=2025` | `light` | `object` |

### Use when

a multivariate system (a small N ~4-6); you want SIMULTANEOUSLY (a) a Granger/directed network from a sparse VAR and (b) the contemporaneous partial-correlation network of the innovations, with LASSO sparsity instead of a dense VAR

### Do not use when

a large N without a sparsity assumption (a dense VAR -> vars); you want spillover/variance-decomposition connectedness (Diebold-Yilmaz -> #51); a single-equation spatial regression with a known W (#53/#54); you want point forecasts (this is a network node, not a forecaster)

### Prerequisites

- nets_fit (GN=TRUE for the Granger network; CN=TRUE for the partial-correlation network; lambda or lambda_grid+ic)
- c01_preparation_prechecks/unit_root_normality.run_adf_test (the NETS VAR assumes stationary series; check/difference first)
- c01_preparation_prechecks/unit_root_normality.run_kpss_test (a complementary stationarity check before the network)
- c00_data_utilities/reading_delimited_fixed.read_delimited (loading the T x N matrix of series)

### Alternatives

| instead use | when |
| --- | --- |
| #51 dy_fit (ConnectednessApproach) | you want FEVD-based spillover/connectedness (Diebold-Yilmaz) rather than a LASSO Granger/partial-correlation network |
| #52 fq_net (frequencyConnectedness) | connectedness per frequency (short/long-run bands) |
| vr_var (c03_multivariate_nowcasting/reduced_form_var) | a small N, you want a full dense VAR + IRF/FEVD with no sparsity penalty |
| CN=FALSE (LASSO VAR only) | you want only the directed Granger network |
| GN=FALSE (the space algorithm) | you want only the partial-correlation network without the autoregressive structure (p->0) |

### Output fields

- granger_network: g.adj, an N x N 0/1 directed adjacency (the Granger network from A.hat); NULL if GN=FALSE
- concentration_network: c.adj, an N x N 0/1 undirected adjacency (the partial-correlation network); NULL if CN=FALSE
- partial_correlation: an N x N matrix of partial correlations -C_ij/sqrt(C_ii C_jj), diag=1 (chart-data); NULL if CN=FALSE or degenerate
- concentration_matrix: C.hat (the precision matrix of the innovations); longrun_network: lr.adj; ar_matrices: A.hat, an N x N x P array
- lambda_used/selected_lambda/ic_table: the penalty that was used; (grid) the selection + a table {lambda,rss,npar,ic}
- rss/npar/p_used/N/T/degenerate_concentration: fit diagnostics + a degeneracy flag for C.hat

### Pitfalls

- g.adj is DIRECTED (Granger, from A.hat); c.adj/partial_correlation are UNDIRECTED (contemporaneous) — do not confuse them
- lambda controls the sparsity: a large lambda -> a sparser network; the graph structure DEPENDS on lambda (use lambda_grid+ic for a data-driven choice)
- a length-2 lambda = [the AR penalty, the concentration penalty] separately; it is allowed ONLY with GN&CN; length-3 values and negatives are accepted silently by nets -> blocked by a gate
- GN=FALSE -> the Granger fields are NULL & p is ignored (space, p=0); CN=FALSE -> the concentration/partial-correlation fields are NULL
- NETS assumes stationary series; non-stationary ones -> a spurious network structure; difference them first
- degenerate_concentration=TRUE => diag(C.hat)<=0 and the partial_correlation was not computed (do not read a network out of a degenerate fit)

### References

- Barigozzi, M. & Brownlees, C. (2019) 'NETS: Network Estimation for Time Series', Journal of Applied Econometrics 34(3):347-364
- Peng, J., Wang, P., Zhou, N. & Zhu, J. (2009) 'Partial Correlation Estimation by Joint Sparse Regression Models' (the space algorithm), JASA 104(486):735-746
- help('nets','nets') — nets 0.9.1 (Christian Brownlees), <

## #182 — Factor-adjusted network estimation (high-dimensional TS): a common factor + an idiosyncratic VAR + Granger/partial-correlation networks

**Module:** `factor_adjusted_network.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `fnets_fit` | `x` | `matrix_handle`, `raw`, `integer`, `enum`, `boolean`, `boolean`, `boolean`, `boolean`, `enum`, `integer`, `integer`, `integer` | `q='ic'`, `var_order=1`, `var_method='lasso'`, `fm_restricted=False`, `center=True`, `do_threshold=False`, `do_lrpc=True`, `tuning='cv'`, `n_folds=1`, `path_length=10`, `seed=2025` | `light` | `object` |
| `fnets_factor` | `x` | `matrix_handle`, `raw`, `boolean`, `boolean`, `integer` | `q='ic'`, `fm_restricted=False`, `center=True`, `seed=2025` | `light` | `object` |

### Use when

many (high-dimensional) time series, T x N, with a strong common (factor) structure; you want to SEPARATE the common from the idiosyncratic part and estimate the idiosyncratic network (Granger + partial correlation) free of pervasive co-movement

### Do not use when

few series without pervasive factors (go straight to a sparse VAR network -> #181 nets); a single-equation panel (i,t) (#46 plm); a spatial cross-section with a known W (#53 spatialreg); pure forecasting with no interest in the network

### Prerequisites

- fnets_factor (estimate the number of factors q first; degenerate=TRUE or q=0 -> there is no common structure, consider #181 nets directly)
- c00_data_utilities/reading_delimited_fixed.read_csv_data (load the T x N matrix of series)

### Alternatives

| instead use | when |
| --- | --- |
| #181 nets_fit | no pervasive factors -> a sparse VAR network directly, without factor adjustment |
| #53 spr_fit_lag/error (spatialreg) | a cross-section with a known spatial weight matrix W rather than an estimated network |
| BVAR/a large VAR (category 04) | few series, the interest is in forecasting/IRF and not in a sparse network |
| fm.restricted=TRUE | a static approximate factor model (PCA) suffices; no dynamic (spectral) factors |

### Output fields

- q: the estimated number of factors (or the input if a number was supplied)
- granger_network: an N x N directed matrix (the sum of the VAR transition matrices over all lags, with a zero diagonal) — chart-data
- pc_network: the N x N contemporaneous partial correlation of the VAR innovations (only with do.lrpc=TRUE)
- lrpc_network: the N x N long-run partial correlation (only with do.lrpc=TRUE)
- beta: the (N*var.order) x N VAR parameters (column j = the regression of variable j); Gamma: the innovation covariance; lambda: the regularisation
- fnets_factor: loadings (2D if restricted; a 3D IRF array (p,q,trunc.lags+2) if unrestricted); factors (the factor series/common shocks); the degenerate flag

### Pitfalls

- the edge weights CAN be negative (entries of the VAR parameters/partial correlations) — they are not \|weights\|
- granger_network[i,j] = the effect i -> j (the orientation of network(type=granger)); the diagonal is zeroed (self-lags are removed)
- pc/lrpc exist ONLY when do.lrpc=TRUE; otherwise out.lrpc is NA and the fields are missing
- q=0 is accepted silently by fnets (only a warning) -> a gate blocks a numeric q<1; fnets_factor sets degenerate=TRUE
- unrestricted loadings are NOT classical factor loadings but impulse response functions (a 3D array); the classical 2D loadings appear only with fm.restricted=TRUE
- input orientation: columns = variables (T x N); a single column or NA/Inf fails with a cryptic C error -> explicit gates

### References

- Barigozzi, Cho & Owens (2024+) FNETS: Factor-adjusted network estimation and forecasting for high-dimensional time series, JBES
- Owens, Cho & Barigozzi (2024+) fnets: An the reference Package for Network Estimation and Forecasting via Factor-Adjusted VAR Modelling,
- help('fnets','fnets'), help('fnets.factor.model'), help('network.fnets') ( fnets 0.1.6)
- Hallin & Liska (2007) JASA 102:603 (the number of dynamic factors); Avarucci et al. (2022); Ahn & Horenstein (2013) Econometrica 81:1203 (the eigenvalue ratio)
