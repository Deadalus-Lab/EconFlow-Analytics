# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.v1.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 13-dsge-general-equilibrium: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'bimets_estimate': {
        'fn': 'bimets_estimate',
        'description': 'bimets_estimate -- category 13-dsge-general-equilibrium, METHOD-SELECTION card #201.',
        'args': {'model': 'MDL model-string (MODEL... END· behaviorals with EQ>/COEFF>, identities with EQ>).', 'data': 'Handle to an mts (one column per variable)· covers ALL the vendog ∪ vexog of the model.', 'tsrange': 'Optional estimation period [startYear,startPeriod,endYear,endPeriod] (default = the TSRANGE of the MDL).', 'estTech': 'Estimation technique· OLS (default) or IV (Instrumental Variables).', 'iv': "Character vector of instrumental-variables expressions (when estTech='IV' & they are not defined in the MDL).", 'eqList': 'Names of behavioral equations to estimate (default = all).'},
        'input_example': {'model': '...', 'data': '<multiseries_handle>'},
    },
    'bimets_multipliers': {
        'fn': 'bimets_multipliers',
        'description': 'bimets_multipliers -- category 13-dsge-general-equilibrium, METHOD-SELECTION card #201.',
        'args': {'object': 'Handle to an estimated BIMETS_MODEL (from bimets_estimate).', 'tsrange': 'Period [startYear,startPeriod,endYear,endPeriod]· single-period=>impact, multi-period=>interim/dynamic.', 'target': 'Endogenous target variables (⊆ vendog) for the multipliers.', 'instrument': 'Exogenous instrument variables (⊆ vexog) that are perturbed.', 'mm_shock': 'Relative perturbation of the instruments for the numerical computation (default 1e-5).', 'simType': 'Simulation type behind the multiplier matrix (default DYNAMIC).', 'simAlgo': 'Solution algorithm (default GAUSS-SEIDEL).'},
        'input_example': {'object': '<raw_handle>', 'tsrange': '...', 'target': ['PROVIDER/DATASET/SERIES'], 'instrument': ['PROVIDER/DATASET/SERIES'], 'mm_shock': 1e-05},
    },
    'bimets_simulate': {
        'fn': 'bimets_simulate',
        'description': 'bimets_simulate -- category 13-dsge-general-equilibrium, METHOD-SELECTION card #201.',
        'args': {'object': 'Handle to an estimated BIMETS_MODEL (from bimets_estimate).', 'tsrange': 'Simulation period [startYear,startPeriod,endYear,endPeriod] (within the data).', 'simType': 'Simulation type· DYNAMIC (default), FORECAST, STATIC.', 'simAlgo': 'Solution algorithm of the system (default GAUSS-SEIDEL).', 'stochastic': 'False=deterministic SIMULATE· True=STOCHSIMULATE (auto NORM(0,SER) perturbation per behavioral -> mean/sd).', 'stoch_replica': 'Number of stochastic replications when stochastic=True (>=2).', 'seed': 'Reproducibility seed for the stochastic path (StochSeed).', 'simConvergence': 'Convergence tolerance of the simulation (positive number· default 1e-5).', 'simIterLimit': 'Maximum iterations per period (default 100).'},
        'input_example': {'object': '<raw_handle>', 'tsrange': '...', 'stochastic': False, 'stoch_replica': 100, 'seed': 2025, 'simConvergence': 1e-05, 'simIterLimit': 100},
    },
    'cge_solve': {
        'fn': 'cge_solve',
        'description': 'cge_solve -- category 13-dsge-general-equilibrium, METHOD-SELECTION card #202.',
        'args': {'dstype': 'Demand structure: constant (Leontief/Sraffa constant A) | CD (Cobb-Douglas) | CES (default constant).', 'A': 'Handle to a demand-coefficient n-by-m matrix (non-negative)· ONLY for dstype=constant.', 'Beta': 'Handle to a share n-by-m matrix (non-negative)· required for CD/CES· CD => each column sums to 1.', 'alpha': 'Efficiency m-vector (CD/CES)· of length 1 (recycle) or m· default rep(1,m).', 'sigma': 'CES elasticity m-vector· of length 1 or m· required for dstype=CES.', 'Theta': 'Handle to a positive n-by-m matrix (CES scale params)· optional.', 'B': 'Handle to a supply-coefficient n-by-m matrix· default diag(n) (requires m==n).', 'S0Exg': 'Handle to an exogenous supply n-by-m (NA=endogenous, NOT 0)· default all NA.', 'p0': 'Initial prices n-vector (>0)· default rep(1,n).', 'z0': 'Initial activity levels m-vector (>0)· default rep(100,m).', 'GRExg': 'Exogenous growth rate of the S0Exg· NA -> 0 if exogenous supply exists.', 'tolCond': 'Convergence tolerance (>0).', 'maxIteration': 'Maximum number of iterations (>=1)· =1 => pure simulation.', 'numberOfPeriods': 'Number of periods per iteration (>=1).', 'priceAdjustmentMethod': 'Price adjustment method (default variable).', 'priceAdjustmentVelocity': 'Price adjustment speed ∈ (0,1].', 'ts': 'If True it also returns the adjustment time series (ts_p/ts_z/ts_S/ts_q).'},
        'input_example': {'tolCond': 1e-05, 'maxIteration': 200, 'numberOfPeriods': 300, 'priceAdjustmentVelocity': 0.15, 'ts': False},
    },
    'dsge_estimate': {
        'fn': 'dsge_estimate',
        'description': 'dsge_estimate -- category 13-dsge-general-equilibrium, METHOD-SELECTION card #200.',
        'args': {'obs_eqs': "Observed control equations 'lhs ~ rhs' (names = data columns).", 'state_eqs': 'Exogenous AR state equations with shock (#state_eqs == #obs_eqs).', 'unobs_eqs': 'Unobserved control equations (optional).', 'fixed': 'Named-numeric map of fixed parameters.', 'start': 'Named-numeric map of initial values for the free params.', 'data': 'Handle to a DataFrame/matrix/ts· columns = names of the observed controls.', 'method': 'Optimizer optim (default BFGS).', 'demean': 'Removal of the mean from the observed before estimation (default True).', 'maxit': 'Maximum optimizer iterations (default 500).'},
        'input_example': {'obs_eqs': ['PROVIDER/DATASET/SERIES'], 'state_eqs': ['PROVIDER/DATASET/SERIES'], 'data': '<df_handle>', 'demean': True, 'maxit': 500},
    },
    'dsge_forecast': {
        'fn': 'dsge_forecast',
        'description': 'dsge_forecast -- category 13-dsge-general-equilibrium, METHOD-SELECTION card #200.',
        'args': {'object': 'Handle to a dsge_fit (dsge_estimate)· requires filtered states.', 'horizon': 'Forecast horizon in periods (default 12).'},
        'input_example': {'object': '<raw_handle>', 'horizon': 12},
    },
    'dsge_irf': {
        'fn': 'dsge_irf',
        'description': 'dsge_irf -- category 13-dsge-general-equilibrium, METHOD-SELECTION card #200.',
        'args': {'object': 'Handle to a dsge_solution (dsge_solve) or a dsge_fit (dsge_estimate).', 'periods': 'IRF horizon in periods (default 20).', 'impulse': 'Names of shocks for the impulse (default all).', 'response': 'Names of response variables (default all).', 'se': 'Delta-method SE + CI bands (applies ONLY to dsge_fit· default True).', 'level': 'Confidence level for the bands ∈ (0,1) (default 0.95).'},
        'input_example': {'object': '<raw_handle>', 'periods': 20, 'se': True, 'level': 0.95},
    },
    'dsge_shock_decomposition': {
        'fn': 'dsge_shock_decomposition',
        'description': 'dsge_shock_decomposition -- category 13-dsge-general-equilibrium, METHOD-SELECTION card #200.',
        'args': {'object': 'Handle to a dsge_fit (dsge_estimate)· Kalman smoother.'},
        'input_example': {'object': '<raw_handle>'},
    },
    'dsge_solve': {
        'fn': 'dsge_solve',
        'description': 'dsge_solve -- category 13-dsge-general-equilibrium, METHOD-SELECTION card #200.',
        'args': {'obs_eqs': "Observed control equations 'lhs ~ rhs' (lead/E for forward expectations).", 'state_eqs': 'Exogenous AR state equations with shock (#state_eqs == #obs_eqs).', 'unobs_eqs': 'Unobserved control equations (optional).', 'fixed': 'Named-numeric map of fixed parameters (e.g. {beta:0.96}).', 'params': 'Named-numeric map of parameter values for the solution.', 'shock_sd': 'Named-numeric map of shock SD (>0)· default 1 per shock.', 'tol': 'Tolerance for classifying an eigenvalue as stable (default 1e-6).'},
        'input_example': {'obs_eqs': ['PROVIDER/DATASET/SERIES'], 'state_eqs': ['PROVIDER/DATASET/SERIES'], 'params': '...', 'tol': 1e-06},
    },
    'sfcr_balance_check': {
        'fn': 'sfcr_balance_check',
        'description': 'sfcr_balance_check -- category 13-dsge-general-equilibrium, METHOD-SELECTION card #203.',
        'args': {'baseline': 'Handle to a solved sfcr_tbl (baseline OR scenario $object).', 'matrix_type': 'tfm=transactions-flow· bs=balance-sheet (default tfm).', 'columns': 'Sector column names of the matrix.', 'codes': 'Column abbreviations (same length & order as columns· unique).', 'rows': "List of rows· each row {name, <code>:formula-string,...} (e.g. {'name':'Consumption','h':'-Cd','f':'+Cs'}).", 'tol': 'Absolute validation tolerance (default 1).', 'rtol': 'Relative discrepancy for growth models (default False).'},
        'input_example': {'baseline': '<raw_handle>', 'columns': ['PROVIDER/DATASET/SERIES'], 'codes': ['PROVIDER/DATASET/SERIES'], 'rows': '...', 'tol': 1, 'rtol': False},
    },
    'sfcr_scenario_run': {
        'fn': 'sfcr_scenario_run',
        'description': 'sfcr_scenario_run -- category 13-dsge-general-equilibrium, METHOD-SELECTION card #203.',
        'args': {'baseline': 'Handle to a baseline sfcr_tbl (sfcr_simulate$object)· the scenario REQUIRES a baseline.', 'shock_variables': "Shock variables as formula-strings ('Gd ~ 30'· or a series of length end-start).", 'shock_start': 'Shock start period (>=1).', 'shock_end': 'Shock end period (shock_start<=shock_end<=periods).', 'periods': 'Total scenario periods (>=2).', 'method': 'Solution algorithm (default Broyden).', 'max_iter': 'Maximum iterations per period (default 350).', 'tol': 'Scenario convergence tolerance (default 1e-10).'},
        'input_example': {'baseline': '<raw_handle>', 'shock_variables': ['PROVIDER/DATASET/SERIES'], 'shock_start': 1, 'shock_end': 1, 'periods': 1, 'max_iter': 350, 'tol': 1e-10},
    },
    'sfcr_simulate': {
        'fn': 'sfcr_simulate',
        'description': 'sfcr_simulate -- category 13-dsge-general-equilibrium, METHOD-SELECTION card #203.',
        'args': {'equations': "Model equations as a list of strings in Wilkinson formula syntax ('Y ~ Cs + Gs'· lag=x[-1]· difference=d(x)).", 'external': "Exogenous variables/parameters as formula-strings ('Gd ~ 20').", 'periods': 'Number of simulation periods (>=2· steady-state needs ~50+).', 'initial': 'Optional initial values as formula-strings.', 'hidden': "Named 1-pair mapping of the hidden/redundant identity (e.g. {'Hh':'Hs'})· if given, accounting consistency is checked.", 'method': 'Solution algorithm (default Broyden· Gauss=Gauss-Seidel· Newton=Newton-Raphson).', 'max_iter': 'Maximum iterations per period (default 350).', 'tol': 'Convergence tolerance (default 1e-8).', 'rhtol': 'Relative-hidden tolerance for growth models (default False=absolute).', 'hidden_tol': 'Tolerance of the hidden-equation check (default 0.1).'},
        'input_example': {'equations': ['PROVIDER/DATASET/SERIES'], 'external': ['PROVIDER/DATASET/SERIES'], 'periods': 1, 'max_iter': 350, 'tol': 1e-08, 'rhtol': False, 'hidden_tol': 0.1},
    },
}
