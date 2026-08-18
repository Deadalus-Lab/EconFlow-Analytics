<!-- SPDX-License-Identifier: AGPL-3.0-only -->
# 21-systemic-risk

3 METHOD-SELECTION cards, 3 modules, 8 nodes.

Every card below governs one wrapper module in this package. The cards are the
reason a method exists here at all: they record when it applies, what to reach
for instead, and the traps that make its output easy to misread.

## #221 — Market-based systemic risk: CoVaR / Delta-CoVaR (Adrian-Brunnermeier) + correlation-network measures

**Module:** `market_systemic_risk.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `syr_covar_delta_covar` | `returns` | `matrix_handle` | — | `light` | — |
| `syr_covar_delta_covar_t` | `returns`, `state_variables` | `matrix_handle`, `matrix_handle` | — | `light` | — |
| `syr_correlation_network_measures` | `returns` | `matrix_handle`, `integer` | — | `light` | — |
| `syr_scale` | `x` | `matrix_handle` | — | `light` | — |

### Use when

a matrix of market returns (column 1 = the market/system index, columns 2. = the institutions); you want the contribution of each institution to systemic risk (CoVaR/Delta-CoVaR in the sense of Adrian-Brunnermeier, static or time-varying with state variables) or monthly correlation-network measures (degree/closeness/eigenvector centrality) + a system-wide index

### Do not use when

there is no market index in column 1; fewer than 2 institutions; you want the VaR/ES of a portfolio (→#65 PerformanceAnalytics) or a conditional-on-X GaR (→#64 quantreg); you want Diebold-Yilmaz spillover/FEVD connectedness (→ ConnectednessApproach/frequencyConnectedness, cat. 09); a quantile level != 95% (it is hardcoded in the package)

### Alternatives

| instead use | when |
| --- | --- |
| syr_covar_delta_covar (static) | you want an unconditional CoVaR/Delta-CoVaR per institution — a single cross-sectional picture, without state variables |
| syr_covar_delta_covar_t (time-varying) | you want a conditional CoVaR/Delta-CoVaR that evolves with lagged macro-financial state variables (VIX/spreads) + the system-wide index Delta_CoVaR_t |
| syr_correlation_network_measures | you want the topology of the correlation network (centrality) + a systemic risk index (SR) per month, not a tail CoVaR |
| Diebold-Yilmaz connectedness (ConnectednessApproach/frequencyConnectedness, cat. 09) | you want directional spillovers from an FEVD (to/from/net) rather than correlation-network centrality or a quantile CoVaR |
| PerformanceAnalytics VaR/ES (#65) | you want the tail risk of ONE portfolio/series, not a cross-system contribution |

### Output fields

- CoVaR_95 / CoVaR_50: the VaR of the system when institution i is at its VaR@95 / median (per institution)
- Delta_CoVaR: the systemic contribution of institution i = CoVaR_95 - CoVaR_50 (an identity); loss-signed
- CoVaR_i_q_t / Delta_CoVaR_i_q_t: time-varying matrices, (n-1) × institutions + dates
- Delta_CoVaR_t: the system-wide index (the cross-sectional mean Delta-CoVaR ×100, positive=higher risk); the 1st element is NA (an off-by-one)
- Degree/Closeness_Centrality/Eigenvector_Centrality: monthly network measures, min-max scaled to [0,1]
- SR: the systemic risk index (a correlation-corrected realized portfolio volatility), min-max scaled to [0,1]
- q=0.95 (a constant, hardcoded in the package); n_institutions/n_state_variables/n_months/seed (an audit trail)
- network: it requires n_months>=3 (a post-gate, blocked-by-gate); ~>=100 daily rows — 90 rows give only 2 months, where the monthly min-max degenerates every measure to {0,1}

### Pitfalls

- q=0.95 & q_50=0.5 ARE HARDCODED in the package — the quantile level is NOT parameterisable (tau=0.05)
- Delta_CoVaR = CoVaR_95 - CoVaR_50 EXACTLY; its sign follows the slope of the quantile regression (a positive co-movement with the market ⇒ Delta-CoVaR<0, a loss)
- column 1 = the market/system index (the LHS), columns 2. = the institutions (the RHS) — NOT the other way round; the wrong order ⇒ a wrong CoVaR
- Delta_CoVaR_t[1] is structurally NA (an off-by-one in the package, m_D_CoVaR_iqt[cpt_time-1,] at cpt_time=1) — do not interpret it as 0
- the network is fragile with few months (seq by 'months' → NA in the xts order.by); the gate requires >=90 observations
- network Eigenvector_Centrality: eigen_centrality (ARPACK) is non-deterministic (~1e-18); the wrapper stabilises it with set.seed(seed)
- a degenerate input (a constant column) ⇒ a quantreg 'Singular design matrix' — a hard error, not a silent result
- the VaR is computed parametrically (qnorm, assuming normality of the institution) — not as a historical/empirical quantile

### References

- Adrian & Brunnermeier 2016 'CoVaR' American Economic Review 106(7) 1705-1741 (the definition of CoVaR/Delta-CoVaR)
- Billio, Getmansky, Lo, Pelizzon 2012 'Econometric measures of connectedness and systemic risk' JFE 104(3) 535-559 (the correlation-network measures)
- SystemicR v0.1.0 (J.-B. Hasse) ref manual + vignette — f_CoVaR_Delta_CoVaR_i_q / f_CoVaR_Delta_CoVaR_i_q_t / f_correlation_network_measures / f_scale (
- live introspection the engine (the printed source + an independent quantreg recomputation) — wrapper footer IMPLEMENTATION NOTE (c21_systemic_risk/market_systemic_risk)

## #222 — Financial-network contagion: DebtRank + Furfine cascades + interbank exposure-matrix reconstruction (Maximum Entropy / Minimum Density)

**Module:** `financial_network_contagion.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `nrm_reconstruct_matrix` | `rowsums`, `colsums` | `matrix_handle`, `matrix_handle`, `enum`, `integer`, `integer`, `number`, `number`, `number`, `integer`, `number`, `number` | — | `light` | `exposure_matrix` |
| `nrm_contagion` | `exposures`, `buffer` | `matrix_handle`, `matrix_handle`, `matrix_handle`, `raw`, `enum`, `enum`, `integer`, `boolean` | — | `light` | — |

### Use when

a bilateral network of financial exposures (interbank/counterparty): (a) only the MARGINS are KNOWN (assets per node + liabilities per node) → reconstruct the n×n exposure matrix with Maximum Entropy (dense) or Minimum Density (sparse, realistic); (b) the exposure matrix + capital buffers are KNOWN → measure systemic risk/contagion with DebtRank (continuous stress) or traditional default cascades (a Furfine threshold), identifying the most systemic nodes (too-central-to-fail)

### Do not use when

non-financial networks or general centrality/community work (→ igraph #55); spillover/connectedness from a VAR/FEVD of returns (→ ConnectednessApproach/frequencyConnectedness #52-53); you want the tail risk of one series (VaR/ES #65, GaR #64); you have only indicators and no network; Bayesian ER sampling of a network from its margins (→ systemicrisk #223)

### Alternatives

| instead use | when |
| --- | --- |
| method='me' (Maximum Entropy) | you want a fully connected (dense) matrix that maximises entropy subject to the margins; deterministic; it understates concentration/contagion (a known issue: much denser than real interbank networks) |
| method='md' (Minimum Density) | you want a SPARSE, more realistic matrix (few large exposures, Anand et al. 2015); STOCHASTIC → a seed is mandatory for reproducibility |
| method='debtrank' (contagion) | you want a CONTINUOUS measure of systemic importance (how much stress the failure of each node transmits) — Bardoscia et al. 2015; single_hit=TRUE for the old Battiston 2012 variant |
| method='threshold' (contagion / Furfine) | you want discrete default cascades (which nodes default in a chain when the losses exceed the buffer), not continuous stress |
| systemicrisk (#223) | you want a Bayesian posterior distribution of networks consistent with the margins (ER/Gibbs), not a single ME/MD point estimate |
| igraph network analysis (#55) | you want general centrality/community/connectivity, not contagion-specific DebtRank/cascade dynamics |

### Output fields

- nrm_reconstruct_matrix.exposure_matrix: the reconstructed n×n exposure matrix (rows=lenders/assets, cols=borrowers/liabilities; a registered handle for chaining into nrm_contagion)
- nrm_reconstruct_matrix.density/n_links: the sparsity of the network (MD << ME); total_exposure: the total volume
- nrm_reconstruct_matrix.max_rowsum_resid/max_colsum_resid: how well the requested margins were honoured (the fit quality)
- nrm_reconstruct_matrix.seed: the seed that was used (critical for md)
- nrm_contagion.results: a data_frame per scenario — scenario/original_stress/additional_stress/original_losses/additional_losses/additional_defaults
- nrm_contagion.additional_stress: the (unweighted) DebtRank of each node (shock='all'); most_systemic_scenario: the most systemic node
- nrm_contagion.total_additional_defaults: the total number of chain defaults beyond the initial shock
- nrm_contagion.weights_defaulted: TRUE when equal weights were used (the weights=NULL fallback)
- nrm_contagion user weights: a hard gate sum(weights)>0 (not merely >=0); a zero sum → the package computes weights/sum=NaN → a NaN systemic stress (blocked as blocked-by-gate)

### Pitfalls

- MATRIX ORIENTATION: rowsums=ASSETS (the creditor/lender per row), colsums=LIABILITIES (the debtor/borrower per column); M[i,j]>0 means an «assets network»: i holds a claim/asset on j (i lent to j). exposure_type='liabilities' REVERSES the convention — state correctly which one describes your matrix
- BALANCE is mandatory: sum(rowsums)==sum(colsums) (total assets = total liabilities in a closed system); otherwise ME silently rescales the rowsums → a hard gate
- MD (min_dens) is STOCHASTIC: a different seed → a different matrix/results; always record/pin the seed; ME/DebtRank/threshold are deterministic
- additional_stress is NON-NEGATIVE additional stress (systemic amplification), NOT a z-score; ME understates transmission (too dense a network) — prefer MD for realistic exposures
- shock: 'all' = one default scenario per node (a per-node DebtRank); a numeric vector = ONE scenario of a uniform proportional shock in [0,1]; values outside [0,1] are rejected (otherwise contagion silently returns a meaningless 0)
- weights=NULL triggers a package bug ('object v not found'); the wrapper works around it with equal weights (weights_defaulted=TRUE) — supply total assets as weights for an economic weighting
- single_hit=TRUE (the old Battiston 2012 single-hit DebtRank) applies ONLY to method='debtrank'; with 'threshold' it is rejected

### References

- Battiston, Puliga, Kaushik, Tasca & Caldarelli 2012 'DebtRank: Too Central to Fail?' Scientific Reports 2:541
- Bardoscia, Battiston, Caccioli & Caldarelli 2015 'DebtRank: A Microscopic Foundation for Shock Propagation' PLoS ONE 10(6)
- Upper & Worm 2004 'Estimating bilateral exposures in the German interbank market' European Economic Review 48, 827-849 (Maximum Entropy)
- Anand, Craig & von Peter 2015 'Filling in the blanks: network structure and interbank contagion' Quantitative Finance 15(4), 625-636 (Minimum Density)
- Furfine 2003 'Interbank Exposures: Quantifying the Risk of Contagion' JMCB 35(1) (threshold default cascades)
- NetworkRiskMeasures v0.1.7 ref manual — the matrix_estimation/max_ent/min_dens/contagion help pages (
- wrapper footer IMPLEMENTATION NOTE (c21_systemic_risk/financial_network_contagion)

## #223 — Bayesian interbank-network reconstruction (the Gandy-Veraart Gibbs sampler, an Erdős-Rényi hierarchical model)

**Module:** `bayesian_interbank_network.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `build_er_model` | `l`, `a` | `matrix_handle`, `matrix_handle`, `number`, `integer`, `integer`, `integer`, `number` | — | `light` | `model` |
| `sample_interbank_network` | `l`, `a`, `model` | `matrix_handle`, `matrix_handle`, `raw_handle`, `integer`, `integer`, `integer`, `integer`, `integer`, `num_array`, `number` | — | `mcmc` | `samples` |

### Use when

you know only the MARGINS of an interbank network — the row sums l (the total liabilities of each bank) & the column sums a (the total claims) — and you want to reconstruct the UNKNOWN n×n matrix of bilateral exposures L; Bayesian sampling of all the matrices consistent with the margins -> a posterior mean matrix, the probability of an edge per cell, the network density (an input for contagion/stress tests)

### Do not use when

you ALREADY have the full exposure matrix (then go straight to contagion/centrality, cat 09 igraph/ConnectednessApproach); you want network centrality/connectedness rather than reconstruction; non-square margins or known cells L_fixed (scoped out); a deterministic max-entropy/RAS reconstruction rather than a Bayesian posterior; sum(l) != sum(a) (unbalanced margins -> a gate)

### Alternatives

| instead use | when |
| --- | --- |
| build_er_model (calibrate_ER) | you need a valid calibrated model BEFORE the sampler; you tune targetdensity (the expected share of existing edges) |
| a larger targetdensity | you believe in a dense/interconnected network (a fully connected core); a smaller one -> a sparse network (few large exposures) |
| a deterministic max-entropy / RAS reconstruction | you want ONE point estimate (no posterior/uncertainty); it typically overstates interconnection (a fully connected bias) — Gandy-Veraart corrects that with sparsity |
| network connectedness/centrality (igraph/ConnectednessApproach, cat 09) | the exposure matrix is KNOWN and you want diffusion/centrality metrics, not a reconstruction |

### Output fields

- mean_matrix: the n×n posterior MEAN exposure matrix (rowSums==l, colSums==a, a zero diagonal — guaranteed)
- prob_link: the n×n posterior probability that an edge EXISTS, P(L[i,j]>0) ∈ [0,1]
- sd_matrix / lower_matrix / upper_matrix: the uncertainty per cell (the standard deviation + the quantiles probs)
- density: the mean network density (the share of positive off-diagonal edges)
- out_degree / in_degree: the expected degree per bank (the sums of prob_link)
- row_sum_max_dev / col_sum_max_dev: the maximum deviation from the margins (~0 = a sound reconstruction)
- n_moving_cells: the cells that moved in the MCMC (the rest are deterministic/forced)
- achieved_density (build_er_model): the REALIZED margin-conditional density (the mean off-diagonal link proportion over seeded sample_HierarchicalModel draws; the same quantity as the density of sample_interbank_network) — NOT the unconditional prior density of genL; directly comparable with targetdensity
- model / samples: the raw handles (systemicrisk_er_model / systemicrisk_gv_samples) -> a to_mcp stub, registered for chaining
- seed: the reproducibility seed (every stochastic path is seeded)

### Pitfalls

- ORIENTATION: l = the row sums = the LIABILITIES (what bank i owes, row i), a = the column sums = the CLAIMS (what is owed to it, column j); L[i,j] = the exposure of i to j — do not transpose l/a; the post-gate rowSums==l & colSums==a catches it
- sum(l) MUST equal sum(a) (total liabilities == total claims); a mismatch -> a hard gate 'they do not balance', NOT a silent adjustment
- achieved_density can EXCEED targetdensity when the margins force a minimum number of edges (forced links); too LOW a targetdensity -> calibrate_ER ERRORS with 'Could not find feasible matrix', not a warning
- both functions are STOCHASTIC (the calibration samples; the Gibbs sampler is MCMC); ALWAYS pass a seed for reproducibility — the same seed -> an identical posterior
- the diagonal is always zero (no self-exposure); the diagonal of prob_link == 0
- a small nsamples/thin -> a noisy estimate (the MCMC has not converged); raise them for production; the defaults (100/100) are conservative for small networks
- mean_matrix is NOT the 'true' matrix — it is the posterior mean; the uncertainty lives in sd_matrix/lower/upper; use prob_link for the structure, not only the mean

### References

- Gandy & Veraart 2017 'A Bayesian Methodology for Systemic Risk Assessment in Financial Networks' Management Science 63(12) 4428-4446
- Gandy & Veraart 2019 'Adjustable Network Reconstruction with Applications to CDS Exposures' J. Multivariate Analysis 172 193-209
- systemicrisk v0.4.3 ref manual — the calibrate_ER, sample_HierarchicalModel, Model.Indep.p.lambda, genL help pages (
- wrapper footer IMPLEMENTATION NOTE (c21_systemic_risk/market_systemic_riskisk)
