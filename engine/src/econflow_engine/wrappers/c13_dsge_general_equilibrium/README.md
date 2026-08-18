<!-- SPDX-License-Identifier: AGPL-3.0-only -->
# 13-dsge-general-equilibrium

4 METHOD-SELECTION cards, 4 modules, 12 nodes.

Every card below governs one wrapper module in this package. The cards are the
reason a method exists here at all: they record when it applies, what to reach
for instead, and the traps that make its output easy to misread.

## #200 — Small linear(ized) DSGE: Klein (2000) solution + Kalman-filter ML estimation, structural IRFs, forecasts and historical shock decomposition

**Module:** `small_linear_dsge.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `dsge_solve` | `obs_eqs`, `state_eqs`, `params` | `series_codes`, `series_codes`, `series_codes`, `raw`, `raw`, `raw`, `number` | `tol=1e-06` | `light` | `object` |
| `dsge_estimate` | `obs_eqs`, `state_eqs`, `data` | `series_codes`, `series_codes`, `series_codes`, `raw`, `raw`, `df_handle`, `enum`, `boolean`, `integer` | `demean=True`, `maxit=500` | `light` | `object` |
| `dsge_irf` | `object` | `raw_handle`, `integer`, `series_codes`, `series_codes`, `boolean`, `number` | `periods=20`, `se=True`, `level=0.95` | `light` | — |
| `dsge_forecast` | `object` | `raw_handle`, `integer` | `horizon=12` | `light` | — |
| `dsge_shock_decomposition` | `object` | `raw_handle` | — | `light` | — |

### Use when

you have a SMALL linearized DSGE (log-linear equilibrium conditions with rational-expectations leads; e.g. a 3-equation New Keynesian or a linearized RBC model) and you want (a) to solve it at given parameters -> policy/transition matrices + saddle-path stability (dsge_solve), (b) to estimate the structural parameters on real observed macro data by ML through the Kalman filter (dsge_estimate), (c) structural IRFs to fundamental shocks (dsge_irf), (d) model-consistent forecasts (dsge_forecast), (e) a historical shock decomposition + smoothed structural shocks (dsge_shock_decomposition)

### Do not use when

a large/nonlinear DSGE with substantive nonlinearities or occasionally binding constraints (you need Dynare/higher-order perturbation — outside this linear formula node); undocumented atheoretical multivariate forecasting -> #10-13 VAR/BVAR/factor models; a plain state-space model without RE cross-equation restrictions -> #56-61 KFAS/dlm/MARSS/bssm; a Bayesian DSGE (RWMH posterior) -> a separate Bayesian node (bayes_dsge, not exposed here); #shocks != #observed (the Klein solver requires equality)

### Prerequisites

- dsge_solve (solve at calibrated parameters FIRST; stable==TRUE == saddle path -> the model is solvable before you attempt estimation)
- dsge_estimate (the ML fit; check convergence==0 & identification.identified before interpreting IRFs/forecasts)
- c00_data_utilities/reading_delimited_fixed.read_delimited (loading the observed macro series as a data_frame; the column names == the observed controls)
- c01_preparation_prechecks/unit_root_normality.run_adf_test (the observables must be stationary deviations — demean=TRUE removes the mean, NOT a trend/unit root)

### Alternatives

| instead use | when |
| --- | --- |
| 56-61 KFAS/dlm/MARSS/bssm (state space) | you want a general linear state-space model (local level/trend, unobserved components) WITHOUT rational-expectations cross-equation restrictions; the DSGE imposes theoretical restrictions that KFAS does not |
| 03 VAR/BVAR (Vars/bvartools) | atheoretical reduced-form dynamics/forecasting without structural microfoundations; you do not want to impose equilibrium conditions |
| 04 svars/VARsignR (structural VAR) | structural shocks + IRFs but with identification through restrictions on a VAR, not through the full DSGE cross-equation structure |
| bayes_dsge (dsge, not exposed) | you want posterior distributions/credible bands with priors (adaptive RWMH) rather than ML point estimates + delta-method SE |

### Output fields

- dsge_solve: policy_matrix (G, controls×states); transition_matrix (H); shock_matrix (M); obs_matrix (D); eigenvalue_moduli + eigen_classification; stable (saddle path); n_stable/n_states; object=dsge_solution (register -> dsge_irf)
- dsge_estimate: coefficients + se (the structural parameters + the log shock SD, delta method); loglik (Kalman); nobs; convergence (0=OK); stable; identification{identified,rank,condition_number,strength,summary}; the policy/transition matrices; object=dsge_fit (register)
- dsge_irf: irf, a data_frame {period,impulse,response,value[,se,lower,upper]}; has_se (TRUE only for a fit); impulses/responses; source_class
- dsge_forecast: forecasts {period,variable,value}; horizon; states (h×n_states); obs_matrix (h×n_obs); variables
- dsge_shock_decomposition: decomposition_by_obs (per observable: T×{shocks..,initial}); obs_names; shock_names; observed (T×n_obs deviations); smoothed_shocks ((T-1)×n_shocks) + smoothed_shock_names

### Pitfalls

- saddle-path stability is a PREREQUISITE: stable==FALSE => the solution is not unique/stable (a Blanchard-Kahn violation) — do NOT interpret IRFs/forecasts; change the parameters or the spec
- the number of exogenous state shocks MUST equal the number of observed controls (the Klein solver): the wrapper gates it explicitly (#state_eqs == #obs_eqs); fewer shocks -> stochastic singularity
- lead(x)/E(x) in the formula = the rational-expectations forward term (E_t[x_{t+1}]); NOT a real future value; state is always an exogenous AR with a shock (shock=TRUE)
- SE on the IRFs (dsge_irf) exist ONLY when the object is a dsge_fit (the delta method on an estimated vcov); on a dsge_solution (calibrated) se is ignored (has_se=FALSE) — there is no sampling uncertainty at fixed parameters
- dsge_forecast/dsge_shock_decomposition require a dsge_fit (they need Kalman-filtered/smoothed states from an estimation on data); a bare dsge_solve is not enough -> a hard gate
- estimate: convergence!=0 or identification.identified==FALSE => the coefficients/SE are not reliable (a flat likelihood / weak identification); check condition_number & the per-parameter strength before interpreting
- demean=TRUE removes only the mean — the observables must already be stationary (log deviations); trending/unit-root data give a wrong likelihood
- ML point estimates + delta-method SE (NOT Bayesian): for posterior uncertainty with priors you need the Bayesian node (bayes_dsge)

### References

- the dsge vignette 'Introduction to the dsge Package' + help: dsge_model/obs/unobs/state, solve_dsge, estimate, irf, forecast, shock_decomposition, smooth_shocks, stability, check_identification (live introspection) <
- Klein (2000) Using the generalized Schur form to solve a multivariate linear rational expectations model, J. Economic Dynamics & Control 24:1405
- Sims (2002) Solving linear rational expectations models, Computational Economics 20:1
- Herbst & Schorfheide (2016) Bayesian Estimation of DSGE Models, Princeton University Press (the Kalman-filter likelihood, identification)
- Galí (2015) Monetary Policy, Inflation, and the Business Cycle, 2nd ed. (the three-equation New Keynesian model)

## #201 — Structural simultaneous-equation macro-econometric model (FRB/US-style): MDL definition → estimate → deterministic/stochastic simulation → policy multipliers

**Module:** `structural_simultaneous_equation.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `bimets_estimate` | `model`, `data` | `string`, `multiseries_handle`, `raw`, `enum`, `raw`, `series_codes` | — | `light` | `object` |
| `bimets_simulate` | `object`, `tsrange` | `raw_handle`, `raw`, `enum`, `enum`, `boolean`, `integer`, `integer`, `number`, `integer` | `stochastic=False`, `stoch_replica=100`, `seed=2025`, `simConvergence=1e-05`, `simIterLimit=100` | `light` | — |
| `bimets_multipliers` | `object`, `tsrange`, `target`, `instrument` | `raw_handle`, `raw`, `series_codes`, `series_codes`, `number`, `enum`, `enum` | `mm_shock=1e-05` | `light` | — |

### Use when

you have a structural system of simultaneous macro-model equations (behavioral equations with coefficients to estimate + accounting identities) defined in an MDL string; you want (a) coefficient estimation (OLS/IV) per equation, (b) deterministic/stochastic simulation or a forecast/scenario for the endogenous variables, (c) a table of policy multipliers (impact/interim/dynamic) of the endogenous variables with respect to exogenous instruments

### Do not use when

a single-equation model (single-equation OLS/IV -> cat. 07); a reduced-form VAR/VECM without theoretical identities (-> cat. 03/05); a micro-founded DSGE with rational expectations/Bellman equations & structural shocks (bimets solves a backward-looking structural form, NOT a general RE-DSGE); you do not have data covering ALL the variables over the estimation/simulation period

### Prerequisites

- c00_data_utilities/reading_delimited_fixed.read_delimited (loading the series from CSV/TSV)
- c00_data_utilities/time_series_class.ts_convert (a long data_frame -> a wide mts; one column per model variable)
- bimets_estimate (the PRODUCER: the estimated BIMETS_MODEL handle -> bimets_simulate/bimets_multipliers)

### Alternatives

| instead use | when |
| --- | --- |
| bimets_simulate | you want a projection/scenario (DYNAMIC/FORECAST) or a stochastic simulation of the endogenous variables after estimation |
| bimets_multipliers | you want impact/interim/dynamic policy multipliers (endogenous targets with respect to exogenous instruments) |
| 07-causality-policy/iv_fit | a single-equation causal estimate with an endogenous regressor (not a whole system) |
| 03-multivariate-nowcasting/Vars-vr_var | reduced-form dynamics without theoretical identities/behavioral restrictions |
| 13-dsge-general-equilibrium/dsge_solve | a micro-founded rational-expectations DSGE (structural shocks, IRFs) rather than a backward-looking structural form |

### Output fields

- bimets_estimate: coefficients (a named list per behavioral equation: named numeric); statistics (RSquared/AdjustedRSquared/DurbinWatson/Fstatistics/SER/AIC/BIC/LogLikelihood per behavioral equation); residuals (a ts per behavioral equation); endogenous/exogenous/behaviorals/identities; estTech; object (the registry handle)
- bimets_simulate (deterministic): mode='deterministic'; simulation (a named list of ts per endogenous variable); simType; simAlgo; tsrange
- bimets_simulate (stochastic): mode='stochastic'; sim_mean & sim_sd (a named list of ts per endogenous variable); stoch_replica; seed
- bimets_multipliers: multiplier_matrix (a TARGET×INSTRUMENT matrix with var_period dimnames); target_labels (rownames); instrument_labels (colnames); tsrange

### Pitfalls

- the data must extend AT LEAST one period before the start of the estimation/simulation when the equations contain TSLAG (otherwise a clean stop; the package gives a cryptic error)
- SIMULATE/STOCHSIMULATE/MULTMATRIX require an estimated model (coefficients without NA); the node gates them (an unestimated model -> blocked)
- in the multipliers: when the INSTRUMENT period is later than the TARGET period the cell is 0 (causality does not run backwards); a single-period TSRANGE => impact multipliers, a multi-period one => interim/dynamic multipliers
- stochastic=TRUE => an automatic NORM(0, StandardErrorRegression) disturbance ONLY in the behavioral equations (not in the identities); the seed is mandatory for reproducibility (default 2025)
- FORECAST vs DYNAMIC: FORECAST uses simulated values for the lagged endogenous variables AND beyond the historical data; STATIC uses the actual lagged values — do not confuse them
- estTech='IV' requires IV expressions inside the MDL or in the iv argument; otherwise the package errors (blocked); CHOWTEST/PDL/RESTRICT/ERROR(AUTO) are declared INSIDE the MDL string

### References

- the bimets vignettes 'Getting started with bimets' & 'US Federal Reserve quarterly model (FRB/US) in the reference with bimets' + help(LOAD_MODEL/ESTIMATE/SIMULATE/STOCHSIMULATE/MULTMATRIX) — Luciani & Stok <
- Klein, L. (1950) 'Economic Fluctuations in the United States 1921–1941', Cowles Commission Monograph 11 (Klein Model I, the reference model)
- Pindyck, R.S. & Rubinfeld, D.L. (1998) 'Econometric Models and Economic Forecasts', 4th ed., McGraw-Hill (structural simultaneous-equation estimation & simulation, multipliers)
- Fair, R.C. (1984) 'Specification, Estimation, and Analysis of Macroeconometric Models', Harvard University Press (FRB/US-style structural macro modelling)

## #202 — Computable/Applied General Equilibrium — a structural dynamic model (sdm) with a Leontief/Cobb-Douglas/CES demand structure; equilibrium prices, activity levels, growth rate

**Module:** `computable_applied_general.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `cge_solve` | — | `enum`, `matrix_handle`, `matrix_handle`, `num_array`, `num_array`, `matrix_handle`, `matrix_handle`, `matrix_handle`, `num_array`, `num_array`, `number`, `number`, `integer`, `integer`, `enum`, `number`, `boolean` | `tolCond=1e-05`, `maxIteration=200`, `numberOfPeriods=300`, `priceAdjustmentVelocity=0.15`, `ts=False` | `heavy` | — |

### Use when

you have a technology/demand structure in IO/SAM form (a demand-coefficient matrix A, or Cobb-Douglas/CES shares Beta+alpha[+sigma]) + a supply matrix B + exogenous supplies S0Exg (labour/capital/off-network); you want to COMPUTE the general equilibrium — relative prices p (a numeraire), activity/output levels z, the demand matrix A·diag(z), the growth rate (in a purely productive economy); a fixed point (the Li structural dynamic model / a Sraffa system); optionally the time paths of the price adjustment towards equilibrium (ts=TRUE)

### Do not use when

you want a linearized DSGE with rational expectations / IRFs / Bayesian estimation on data (go to dsge_solve/dsge_estimate); stock-flow-consistent macro accounting with behavioral equations (sfcr); econometric structural macro-model estimation+simulation (bimets); you have time series and want a regression/forecast (not a calibrated GE); you need the multi-money / policy-experiment / intertemporal-path features of sdm (outside the curated surface)

### Prerequisites

- cge_solve (constant demand first as a Leontief/Sraffa baseline; then CD/CES for price-responsive demand)
- c00_data_utilities/canonical_disk_format.arw_read_parquet (loading the IO/SAM demand/supply matrices A/B/S0Exg from Parquet)
- c00_data_utilities/reading_delimited_fixed.read_delimited (alternatively: loading the coefficient matrices from CSV)

### Alternatives

| instead use | when |
| --- | --- |
| 13-dsge-general-equilibrium/dsge_solve | you want a linearized rational-expectations DSGE (policy functions, IRFs, forecast, shock decomposition) rather than a calibrated Walrasian GE on an IO/SAM structure |
| 13-dsge-general-equilibrium/sfcr_simulate | stock-flow-consistent macro accounting with behavioral equations & balance-sheet consistency rather than market-clearing GE |
| 13-dsge-general-equilibrium/bimets_simulate | an econometric structural macro model (estimated equations + multipliers) rather than a calibrated GE |
| cge_solve (dstype='CES') | you want price-responsive demand with a tunable elasticity of substitution (sigma) — CD is the special limit sigma->0 |

### Output fields

- p / p_normalized: the equilibrium prices (an n-vector) & the same normalised to the commodity-1 numeraire (p/p[1]; ONLY relative prices are meaningful)
- z: the equilibrium levels of activity/output/utility (an m-vector)
- demand_matrix: A_eq %*% diag(z) — the demand matrix at equilibrium (chart-data); S: the supply matrix of the initial period
- A_eq: the equilibrium demand-coefficient matrix (for CD/CES it differs from the inputs — it is computed at the equilibrium prices)
- growth_rate: the endogenous equilibrium growth rate (a purely productive economy without S0Exg; NA otherwise)
- tolerance / tolCond / converged: the convergence error vs the threshold; converged=TRUE <=> tolerance<=tolCond
- ts_p/ts_z/ts_S/ts_q (only with ts=TRUE): the adjustment paths of prices/levels/supply/sales-rate in the last iteration

### Pitfalls

- ONLY relative prices: a GE determines prices up to scale; ALWAYS use p_normalized (numeraire=commodity 1); the absolute p values are arbitrary
- converged=FALSE => the solution is NOT an equilibrium (tolerance>tolCond); raise maxIteration or check the structure; a stateless node — there is no silent retry
- CD requires every column of Beta to sum to 1 (Cobb-Douglas shares); CES does NOT (non-negative shares suffice); the wrapper gates it
- CES sigma: the elasticity parameter (sigma<0 is usual; sigma->0 => the Cobb-Douglas limit, sigma->-inf => Leontief); it is NOT the elasticity of substitution 1/(1-sigma) — do not confuse them
- S0Exg: NA=an endogenous commodity, a non-zero value=an exogenous supply (labour/land); 0 is FORBIDDEN (the sdm documentation); the wrapper blocks it
- dstype='constant' = price-INDEPENDENT demand (Leontief/Sraffa); CD/CES = price-responsive (A is recomputed at every iteration); a different economic interpretation
- maxIteration=1 => a pure dynamic simulation (not an equilibrium computation); combine it with ts=TRUE for the adjustment paths

### References

- LI Wu (2019, ISBN 9787521804225) General Equilibrium and Structural Dynamics: Perspectives of New Structural Economics; LI Wu (2010) A Structural Growth Model and its Applications to Sraffa's System (IIOA 18th conf.)
- Torres, Jose L. (2016, ISBN 9781622730452) Introduction to Dynamic Macroeconomic General Equilibrium Models (2nd ed.), Vernon Press
- Varian, Hal R. (1992, ISBN 0393957357) Microeconomic Analysis, W. W. Norton — general equilibrium, p.352

## #203 — Stock-Flow-Consistent (Godley-Lavoie) macro simulation — a baseline steady-state solve, policy scenarios (shocks), balance-sheet/transactions-flow accounting validation

**Module:** `stock_flow_consistent.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `sfcr_simulate` | `equations`, `external`, `periods` | `series_codes`, `series_codes`, `integer`, `series_codes`, `raw`, `enum`, `integer`, `number`, `boolean`, `number` | `max_iter=350`, `tol=1e-08`, `rhtol=False`, `hidden_tol=0.1` | `light` | `object` |
| `sfcr_scenario_run` | `baseline`, `shock_variables`, `shock_start`, `shock_end`, `periods` | `raw_handle`, `series_codes`, `integer`, `integer`, `integer`, `enum`, `integer`, `number` | `max_iter=350`, `tol=1e-10` | `light` | `object` |
| `sfcr_balance_check` | `baseline`, `columns`, `codes`, `rows` | `raw_handle`, `enum`, `series_codes`, `series_codes`, `raw`, `number`, `boolean` | `tol=1`, `rtol=False` | `light` | — |

### Use when

you have a THEORETICALLY SPECIFIED SFC model (a system of accounting identities + behavioral equations in the Godley-Lavoie tradition) and you want to SOLVE it to a steady state (sfcr_simulate), to run policy scenarios with shocks to exogenous variables/parameters (sfcr_scenario_run), and to VERIFY that the balance-sheet/transactions-flow matrix is water-tight (sfcr_balance_check). A deterministic simulation with block-ordered Gauss-Seidel/Broyden/Newton root solving.

### Do not use when

you want to ESTIMATE parameters from data (SFC is calibrated/theory-driven, not estimated — go to an econometric structural model); you want a micro-founded DSGE with rational expectations/optimisation & log-linearization (a different paradigm); you have a single behavioral equation (run a regression, cat. 07/08); you want a stochastic/Monte Carlo ensemble or a sensitivity sweep (sfcr_multis/sfcr_random — deliberately outside the deterministic node)

### Prerequisites

- sfcr_simulate (solve the baseline FIRST; sfcr_scenario_run & sfcr_balance_check REQUIRE a solved sfcr_tbl handle)
- sfcr_scenario_run (a scenario = baseline + shock; it needs the baseline object)
- sfcr_balance_check (run it AFTER simulate/scenario to certify accounting consistency — a water-tight check)

### Alternatives

| instead use | when |
| --- | --- |
| sfcr_scenario_run | you want a counterfactual/policy shock (e.g. higher government spending, a higher tax rate) on an already solved baseline |
| sfcr_balance_check | you want to certify that the accounting identities close (every column/row of the TFM/BS sums correctly; locating a leak) |
| #204 bimets (an econometric structural macro model) | you want an ESTIMATED structural macro-econometric model (Klein type) with simulation/multiplier analysis rather than a calibrated SFC model |
| 04-structural-shocks SVAR/BVAR nodes | you want empirically identified shocks & IRFs from data rather than a theory-driven counterfactual |

### Output fields

- sfcr_simulate: paths (a data_frame period × all the variables; chart-data); steady_state (the values of the last period); variables/n_variables; method; converged; object (the baseline sfcr_tbl handle -> scenario/balance)
- sfcr_scenario_run: paths (the scenario data_frame; chart-data); final_values; shocked_vars; shock_start/shock_end; object (the scenario sfcr_tbl handle)
- sfcr_balance_check: consistent (bool; TRUE=water-tight); leaking_rows/leaking_cols (the names that leak); max_row_residual/max_col_residual (the maximum absolute accounting residual); row_residual_by_period/col_residual_by_period (chart-data); message

### Pitfalls

- sfcr_validate (the package function) returns NO value — it either cats 'Water tight!' or aborts; the wrapper traps that into a consistent flag + leaking rows/cols AND computes explicit numeric residuals per period (otherwise they would not surface)
- SFC is calibrated/theory-driven, NOT estimated; the parameters (alpha1, theta,..) are given exogenously — do not 'estimate' them; the steady state depends on them (e.g. SIM: Y* = G/theta)
- in growth models (perpetually increasing stocks) the hidden equation & the validation must use rhtol=TRUE (relative), not absolute — otherwise a spurious failure from computational buildup
- the hidden equation (a redundant identity, e.g. Hh=Hs in SIM): if supplied, it is checked; its failure = a mis-specified model (a leak in the logic)
- the scenario INHERITS the block structure & the final state from the baseline; a shock applied BEFORE the baseline has converged produces a transient that is not a policy effect; run the baseline for enough periods (~50+) first
- sfcr_matrix rows: the first element = the row name, the rest are name-value pairs per code; do NOT add a manual 'sum' column to a TFM (it is generated automatically); in a BS the non-zero rows need an explicit 'Sum' column
- a large max_col_residual/max_row_residual while consistent=TRUE is impossible within tol; consistent=FALSE with small residuals => raise tol (stationary vs growth models)

### References

- the sfcr package + vignettes ('sfcr', 'sfcr_multis') — João Macalós, sfcr_set/sfcr_baseline/sfcr_shock/sfcr_scenario/sfcr_matrix/sfcr_validate (live introspection + Rd help pages) <
- Godley W. & Lavoie M. (2007) Monetary Economics: An Integrated Approach to Credit, Money, Income, Production and Wealth, Palgrave Macmillan (the SIM/PC/.. models, transactions-flow & balance-sheet matrices, water-tight accounting)
- Kinsella S. & OShea T. (2010) Solution and Simulation of Large Stock Flow Consistent Monetary Production Models via the Gauss Seidel Algorithm, SSRN, doi:10.2139/ssrn.1729205 (the Gauss-Seidel method, cited in the sfcr_baseline help)
- Peressini A.L., Sullivan F.E., Uhl J.J. (1988) The Mathematics of Nonlinear Programming, Springer (the Broyden & Newton-Raphson algorithms, cited in the sfcr_baseline help)
