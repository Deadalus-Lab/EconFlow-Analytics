# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 13-heterogeneous-agent-ge: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'sem_estimate': {
        'fn': 'sem_estimate',
        'description': 'sem_estimate -- category 13-heterogeneous-agent-ge, method card #201.',
        'args': {'model': 'MDL model-string (MODEL... END· behaviorals with EQ>/COEFF>, identities with EQ>).', 'data': 'Handle to an panel (one column per variable)· covers ALL the vendog ∪ vexog of the model.', 'tsrange': 'Optional estimation period [startYear,startPeriod,endYear,endPeriod] (default = the TSRANGE of the MDL).', 'estTech': 'Estimation technique· OLS (default) or IV (Instrumental Variables).', 'iv': "Character vector of instrumental-variables expressions (when estTech='IV' & they are not defined in the MDL).", 'eqList': 'Names of behavioral equations to estimate (default = all).'},
        'input_example': {'model': '...', 'data': '<multiseries_handle>'},
    },
    'sem_multipliers': {
        'fn': 'sem_multipliers',
        'description': 'sem_multipliers -- category 13-heterogeneous-agent-ge, method card #201.',
        'args': {'object': 'Handle to an estimated BIMETS_MODEL (from sem_estimate).', 'tsrange': 'Period [startYear,startPeriod,endYear,endPeriod]· single-period=>impact, multi-period=>interim/dynamic.', 'target': 'Endogenous target variables (⊆ vendog) for the multipliers.', 'instrument': 'Exogenous instrument variables (⊆ vexog) that are perturbed.', 'mm_shock': 'Relative perturbation of the instruments for the numerical computation (default 1e-5).', 'simType': 'Simulation type behind the multiplier matrix (default DYNAMIC).', 'simAlgo': 'Solution algorithm (default GAUSS-SEIDEL).'},
        'input_example': {'object': '<raw_handle>', 'tsrange': '...', 'target': ['PROVIDER/DATASET/SERIES'], 'instrument': ['PROVIDER/DATASET/SERIES'], 'mm_shock': 1e-05},
    },
    'sem_simulate': {
        'fn': 'sem_simulate',
        'description': 'sem_simulate -- category 13-heterogeneous-agent-ge, method card #201.',
        'args': {'object': 'Handle to an estimated BIMETS_MODEL (from sem_estimate).', 'tsrange': 'Simulation period [startYear,startPeriod,endYear,endPeriod] (within the data).', 'simType': 'Simulation type· DYNAMIC (default), FORECAST, STATIC.', 'simAlgo': 'Solution algorithm of the system (default GAUSS-SEIDEL).', 'stochastic': 'False=deterministic SIMULATE· True=STOCHSIMULATE (auto NORM(0,SER) perturbation per behavioral -> mean/sd).', 'stoch_replica': 'Number of stochastic replications when stochastic=True (>=2).', 'seed': 'Reproducibility seed for the stochastic path (StochSeed).', 'simConvergence': 'Convergence tolerance of the simulation (positive number· default 1e-5).', 'simIterLimit': 'Maximum iterations per period (default 100).'},
        'input_example': {'object': '<raw_handle>', 'tsrange': '...', 'stochastic': False, 'stoch_replica': 100, 'seed': 2025, 'simConvergence': 1e-05, 'simIterLimit': 100},
    },
    'cge_solve': {
        'fn': 'cge_solve',
        'description': 'cge_solve -- category 13-heterogeneous-agent-ge, method card #202.',
        'args': {'dstype': 'Demand structure: constant (Leontief/Sraffa constant A) | CD (Cobb-Douglas) | CES (default constant).', 'A': 'Handle to a demand-coefficient n-by-m matrix (non-negative)· ONLY for dstype=constant.', 'Beta': 'Handle to a share n-by-m matrix (non-negative)· required for CD/CES· CD => each column sums to 1.', 'alpha': 'Efficiency m-vector (CD/CES)· of length 1 (recycle) or m· default rep(1,m).', 'sigma': 'CES elasticity m-vector· of length 1 or m· required for dstype=CES.', 'Theta': 'Handle to a positive n-by-m matrix (CES scale params)· optional.', 'B': 'Handle to a supply-coefficient n-by-m matrix· default diag(n) (requires m==n).', 'S0Exg': 'Handle to an exogenous supply n-by-m (NA=endogenous, NOT 0)· default all NA.', 'p0': 'Initial prices n-vector (>0)· default rep(1,n).', 'z0': 'Initial activity levels m-vector (>0)· default rep(100,m).', 'GRExg': 'Exogenous growth rate of the S0Exg· NA -> 0 if exogenous supply exists.', 'tolCond': 'Convergence tolerance (>0).', 'maxIteration': 'Maximum number of iterations (>=1)· =1 => pure simulation.', 'numberOfPeriods': 'Number of periods per iteration (>=1).', 'priceAdjustmentMethod': 'Price adjustment method (default variable).', 'priceAdjustmentVelocity': 'Price adjustment speed ∈ (0,1].', 'ts': 'If True it also returns the adjustment time series (ts_p/ts_z/ts_S/ts_q).'},
        'input_example': {'tolCond': 1e-05, 'maxIteration': 200, 'numberOfPeriods': 300, 'priceAdjustmentVelocity': 0.15, 'ts': False},
    },
    'dsge_estimate': {
        'fn': 'dsge_estimate',
        'description': 'dsge_estimate -- category 13-heterogeneous-agent-ge, method card #200.',
        'args': {'obs_eqs': "Observed control equations 'lhs ~ rhs' (names = data columns).", 'state_eqs': 'Exogenous AR state equations with shock (#state_eqs == #obs_eqs).', 'unobs_eqs': 'Unobserved control equations (optional).', 'fixed': 'Named-numeric map of fixed parameters.', 'start': 'Named-numeric map of initial values for the free params.', 'data': 'Handle to a DataFrame/matrix/ts· columns = names of the observed controls.', 'method': 'Optimizer optim (default BFGS).', 'demean': 'Removal of the mean from the observed before estimation (default True).', 'maxit': 'Maximum optimizer iterations (default 500).'},
        'input_example': {'obs_eqs': ['PROVIDER/DATASET/SERIES'], 'state_eqs': ['PROVIDER/DATASET/SERIES'], 'data': '<df_handle>', 'demean': True, 'maxit': 500},
    },
    'dsge_forecast': {
        'fn': 'dsge_forecast',
        'description': 'dsge_forecast -- category 13-heterogeneous-agent-ge, method card #200.',
        'args': {'object': 'Handle to a dsge_fit (dsge_estimate)· requires filtered states.', 'horizon': 'Forecast horizon in periods (default 12).'},
        'input_example': {'object': '<raw_handle>', 'horizon': 12},
    },
    'dsge_irf': {
        'fn': 'dsge_irf',
        'description': 'dsge_irf -- category 13-heterogeneous-agent-ge, method card #200.',
        'args': {'object': 'Handle to a dsge_solution (dsge_solve) or a dsge_fit (dsge_estimate).', 'periods': 'IRF horizon in periods (default 20).', 'impulse': 'Names of shocks for the impulse (default all).', 'response': 'Names of response variables (default all).', 'se': 'Delta-method SE + CI bands (applies ONLY to dsge_fit· default True).', 'level': 'Confidence level for the bands ∈ (0,1) (default 0.95).'},
        'input_example': {'object': '<raw_handle>', 'periods': 20, 'se': True, 'level': 0.95},
    },
    'dsge_shock_decomposition': {
        'fn': 'dsge_shock_decomposition',
        'description': 'dsge_shock_decomposition -- category 13-heterogeneous-agent-ge, method card #200.',
        'args': {'object': 'Handle to a dsge_fit (dsge_estimate)· Kalman smoother.'},
        'input_example': {'object': '<raw_handle>'},
    },
    'dsge_solve': {
        'fn': 'dsge_solve',
        'description': 'dsge_solve -- category 13-heterogeneous-agent-ge, method card #200.',
        'args': {'obs_eqs': "Observed control equations 'lhs ~ rhs' (lead/E for forward expectations).", 'state_eqs': 'Exogenous AR state equations with shock (#state_eqs == #obs_eqs).', 'unobs_eqs': 'Unobserved control equations (optional).', 'fixed': 'Named-numeric map of fixed parameters (e.g. {beta:0.96}).', 'params': 'Named-numeric map of parameter values for the solution.', 'shock_sd': 'Named-numeric map of shock SD (>0)· default 1 per shock.', 'tol': 'Tolerance for classifying an eigenvalue as stable (default 1e-6).'},
        'input_example': {'obs_eqs': ['PROVIDER/DATASET/SERIES'], 'state_eqs': ['PROVIDER/DATASET/SERIES'], 'params': '...', 'tol': 1e-06},
    },
    'sfc_balance_check': {
        'fn': 'sfc_balance_check',
        'description': 'sfc_balance_check -- category 13-heterogeneous-agent-ge, method card #203.',
        'args': {'baseline': 'Handle to a solved sfcr_tbl (baseline OR scenario $object).', 'matrix_type': 'tfm=transactions-flow· bs=balance-sheet (default tfm).', 'columns': 'Sector column names of the matrix.', 'codes': 'Column abbreviations (same length & order as columns· unique).', 'rows': "List of rows· each row {name, <code>:formula-string,...} (e.g. {'name':'Consumption','h':'-Cd','f':'+Cs'}).", 'tol': 'Absolute validation tolerance (default 1).', 'rtol': 'Relative discrepancy for growth models (default False).'},
        'input_example': {'baseline': '<raw_handle>', 'columns': ['PROVIDER/DATASET/SERIES'], 'codes': ['PROVIDER/DATASET/SERIES'], 'rows': '...', 'tol': 1, 'rtol': False},
    },
    'sfc_scenario_run': {
        'fn': 'sfc_scenario_run',
        'description': 'sfc_scenario_run -- category 13-heterogeneous-agent-ge, method card #203.',
        'args': {'baseline': 'Handle to a baseline sfcr_tbl (sfc_simulate.object)· the scenario REQUIRES a baseline.', 'shock_variables': "Shock variables as formula-strings ('Gd ~ 30'· or a series of length end-start).", 'shock_start': 'Shock start period (>=1).', 'shock_end': 'Shock end period (shock_start<=shock_end<=periods).', 'periods': 'Total scenario periods (>=2).', 'method': 'Solution algorithm (default Broyden).', 'max_iter': 'Maximum iterations per period (default 350).', 'tol': 'Scenario convergence tolerance (default 1e-10).'},
        'input_example': {'baseline': '<raw_handle>', 'shock_variables': ['PROVIDER/DATASET/SERIES'], 'shock_start': 1, 'shock_end': 1, 'periods': 1, 'max_iter': 350, 'tol': 1e-10},
    },
    'sfc_simulate': {
        'fn': 'sfc_simulate',
        'description': 'sfc_simulate -- category 13-heterogeneous-agent-ge, method card #203.',
        'args': {'equations': "Model equations as a list of strings in Wilkinson formula syntax ('Y ~ Cs + Gs'· lag=x[-1]· difference=d(x)).", 'external': "Exogenous variables/parameters as formula-strings ('Gd ~ 20').", 'periods': 'Number of simulation periods (>=2· steady-state needs ~50+).', 'initial': 'Optional initial values as formula-strings.', 'hidden': "Named 1-pair mapping of the hidden/redundant identity (e.g. {'Hh':'Hs'})· if given, accounting consistency is checked.", 'method': 'Solution algorithm (default Broyden· Gauss=Gauss-Seidel· Newton=Newton-Raphson).', 'max_iter': 'Maximum iterations per period (default 350).', 'tol': 'Convergence tolerance (default 1e-8).', 'rhtol': 'Relative-hidden tolerance for growth models (default False=absolute).', 'hidden_tol': 'Tolerance of the hidden-equation check (default 0.1).'},
        'input_example': {'equations': ['PROVIDER/DATASET/SERIES'], 'external': ['PROVIDER/DATASET/SERIES'], 'periods': 1, 'max_iter': 350, 'tol': 1e-08, 'rhtol': False, 'hidden_tol': 0.1},
    },
    'ge_ssj_steady_state': {
        'fn': 'ge_ssj_steady_state',
        'description': 'ge_ssj_steady_state -- category 13-heterogeneous-agent-ge, method card #499.',
        'args': {'model': 'Model block specification.', 'calibration': 'Parameter calibration.', 'targets': 'Steady-state targets to hit.', 'tol': 'Convergence tolerance.'},
        'input_example': {'model': '...', 'calibration': '<df_handle>', 'tol': 1e-09},
    },
    'ge_ssj_jacobians': {
        'fn': 'ge_ssj_jacobians',
        'description': 'ge_ssj_jacobians -- category 13-heterogeneous-agent-ge, method card #499.',
        'args': {'steady_state': 'Handle to a solved steady state.', 'horizon': 'Truncation horizon.', 'inputs': 'Input variables to differentiate with respect to.'},
        'input_example': {'steady_state': '<raw_handle>', 'horizon': 300, 'inputs': ['a', 'b']},
    },
    'ge_ssj_irf': {
        'fn': 'ge_ssj_irf',
        'description': 'ge_ssj_irf -- category 13-heterogeneous-agent-ge, method card #499.',
        'args': {'jacobians': 'Handle to computed Jacobians.', 'shock': 'Shocked variable.', 'persistence': 'Shock persistence.', 'horizon': 'Response horizon.'},
        'input_example': {'jacobians': '<raw_handle>', 'shock': '...', 'persistence': 0.9, 'horizon': 50},
    },
    'ge_lifecycle_solve': {
        'fn': 'ge_lifecycle_solve',
        'description': 'ge_lifecycle_solve -- category 13-heterogeneous-agent-ge, method card #500.',
        'args': {'calibration': 'Model parameters.', 'model': 'Model variant.', 'n_grid': 'Grid points for the wealth state.', 'horizon': 'Life-cycle horizon; 0 = infinite.'},
        'input_example': {'calibration': '<df_handle>', 'model': 'buffer_stock', 'n_grid': 100, 'horizon': 0},
    },
    'ge_lifecycle_simulate': {
        'fn': 'ge_lifecycle_simulate',
        'description': 'ge_lifecycle_simulate -- category 13-heterogeneous-agent-ge, method card #500.',
        'args': {'solution': 'Handle to a solved model.', 'n_agents': 'Simulated agents.', 'n_periods': 'Simulation periods.', 'seed': 'Seed for the random number generator; required for reproducibility.'},
        'input_example': {'solution': '<raw_handle>', 'n_agents': 10000, 'n_periods': 1000, 'seed': 1},
    },
    'ge_discretise_ar1': {
        'fn': 'ge_discretise_ar1',
        'description': 'ge_discretise_ar1 -- category 13-heterogeneous-agent-ge, method card #501.',
        'args': {'rho': 'Autoregressive coefficient.', 'sigma': 'Innovation standard deviation.', 'n_states': 'Number of states.', 'method': 'Discretisation method.', 'n_std': 'Grid width in standard deviations for Tauchen.'},
        'input_example': {'rho': 1.0, 'sigma': 1.0, 'n_states': 7, 'method': 'rouwenhorst', 'n_std': 3.0},
    },
    'ge_linear_quadratic': {
        'fn': 'ge_linear_quadratic',
        'description': 'ge_linear_quadratic -- category 13-heterogeneous-agent-ge, method card #501.',
        'args': {'transition': 'State transition matrix.', 'control': 'Control matrix.', 'control_cost': 'Control cost matrix.', 'state_cost': 'State cost matrix.', 'beta': 'Discount factor.'},
        'input_example': {'transition': '<matrix_handle>', 'control': '<matrix_handle>', 'control_cost': '<matrix_handle>', 'state_cost': '<matrix_handle>', 'beta': 0.95},
    },
    'ge_discrete_dp': {
        'fn': 'ge_discrete_dp',
        'description': 'ge_discrete_dp -- category 13-heterogeneous-agent-ge, method card #501.',
        'args': {'rewards': 'Reward matrix over states and actions.', 'transitions': 'Transition probabilities.', 'beta': 'Discount factor.', 'method': 'Solution method.'},
        'input_example': {'rewards': '<matrix_handle>', 'transitions': '<matrix_handle>', 'beta': 0.95, 'method': 'policy_iteration'},
    },
    'ge_nonlinear_path': {
        'fn': 'ge_nonlinear_path',
        'description': 'ge_nonlinear_path -- category 13-heterogeneous-agent-ge, method card #502.',
        'args': {'model': 'Model specification.', 'shock': 'Shock path.', 'horizon': 'Transition horizon.', 'constraints': 'Occasionally binding constraints.', 'tol': 'Convergence tolerance.', 'max_iter': 'Maximum Newton iterations.'},
        'input_example': {'model': '...', 'shock': '<df_handle>', 'horizon': 100, 'tol': 1e-08, 'max_iter': 100},
    },
    'ge_dsge_solve': {
        'fn': 'ge_dsge_solve',
        'description': 'ge_dsge_solve -- category 13-heterogeneous-agent-ge, method card #503.',
        'args': {'model': 'Model specification.', 'calibration': 'Parameter values.', 'order': 'Perturbation order.', 'check_determinacy': 'Verify the Blanchard-Kahn conditions.'},
        'input_example': {'model': '...', 'calibration': '<df_handle>', 'order': 1, 'check_determinacy': True},
    },
    'ge_dsge_estimate': {
        'fn': 'ge_dsge_estimate',
        'description': 'ge_dsge_estimate -- category 13-heterogeneous-agent-ge, method card #503.',
        'args': {'solution': 'Handle to a solved model.', 'data': 'Observed series.', 'priors': 'Prior specification.', 'draws': 'Posterior draws.', 'warmup': 'Warm-up draws.', 'seed': 'Seed for the random number generator; required for reproducibility.'},
        'input_example': {'solution': '<raw_handle>', 'data': '<df_handle>', 'priors': '<df_handle>', 'draws': 10000, 'warmup': 5000, 'seed': 1},
    },
    'ge_identification_check': {
        'fn': 'ge_identification_check',
        'description': 'ge_identification_check -- category 13-heterogeneous-agent-ge, method card #503.',
        'args': {'solution': 'Handle to a solved model.', 'method': 'Identification diagnostic.'},
        'input_example': {'solution': '<raw_handle>', 'method': 'rank'},
    },
    'ge_linear_re_solve': {
        'fn': 'ge_linear_re_solve',
        'description': 'ge_linear_re_solve -- category 13-heterogeneous-agent-ge, method card #504.',
        'args': {'A': 'Coefficient matrix on future variables.', 'B': 'Coefficient matrix on current variables.', 'C': 'Coefficient matrix on shocks.', 'n_forward': 'Number of forward-looking variables.', 'method': 'Solution method.'},
        'input_example': {'A': '<matrix_handle>', 'B': '<matrix_handle>', 'n_forward': 1, 'method': 'klein'},
    },
    'ge_simulate_re': {
        'fn': 'ge_simulate_re',
        'description': 'ge_simulate_re -- category 13-heterogeneous-agent-ge, method card #504.',
        'args': {'solution': 'Handle to a solved system.', 'n_periods': 'Simulation length.', 'shock_cov': 'Shock covariance matrix.', 'seed': 'Seed for the random number generator; required for reproducibility.'},
        'input_example': {'solution': '<raw_handle>', 'n_periods': 1000, 'seed': 1},
    },
    'ge_sfc_solve': {
        'fn': 'ge_sfc_solve',
        'description': 'ge_sfc_solve -- category 13-heterogeneous-agent-ge, method card #505.',
        'args': {'model': 'Model specification.', 'parameters': 'Parameter values.', 'initial': 'Initial stocks.', 'n_periods': 'Simulation periods.', 'tol': 'Within-period convergence tolerance.'},
        'input_example': {'model': '...', 'parameters': '<df_handle>', 'n_periods': 100, 'tol': 1e-10},
    },
    'ge_accounting_check': {
        'fn': 'ge_accounting_check',
        'description': 'ge_accounting_check -- category 13-heterogeneous-agent-ge, method card #505.',
        'args': {'solution': 'Handle to a solved model.', 'tolerance': 'Tolerance for the accounting residual.'},
        'input_example': {'solution': '<raw_handle>', 'tolerance': 1e-08},
    },
    'ge_abm_simulate': {
        'fn': 'ge_abm_simulate',
        'description': 'ge_abm_simulate -- category 13-heterogeneous-agent-ge, method card #506.',
        'args': {'model': 'Model specification.', 'parameters': 'Parameter values.', 'n_agents': 'Number of agents.', 'n_periods': 'Simulation periods.', 'n_seeds': 'Ensemble size.', 'seed': 'Seed for the random number generator; required for reproducibility.'},
        'input_example': {'model': '...', 'parameters': '<df_handle>', 'n_agents': 1000, 'n_periods': 500, 'n_seeds': 30, 'seed': 1},
    },
    'ge_abm_calibrate': {
        'fn': 'ge_abm_calibrate',
        'description': 'ge_abm_calibrate -- category 13-heterogeneous-agent-ge, method card #506.',
        'args': {'model': 'Model specification.', 'targets': 'Target moments.', 'bounds': 'Parameter bounds.', 'n_seeds': 'Ensemble size per evaluation.', 'method': 'Search method.', 'seed': 'Seed for the random number generator; required for reproducibility.'},
        'input_example': {'model': '...', 'targets': '<df_handle>', 'bounds': '<df_handle>', 'n_seeds': 10, 'method': 'surrogate', 'seed': 1},
    },
}
