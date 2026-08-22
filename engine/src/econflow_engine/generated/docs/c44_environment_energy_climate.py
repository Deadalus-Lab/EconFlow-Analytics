# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 44-environment-energy-climate: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'env_footprint': {
        'fn': 'env_footprint',
        'description': 'env_footprint -- category 44-environment-energy-climate, method card #367.',
        'args': {'io_table': 'Handle to a loaded multi-regional table.', 'extension': 'Environmental extension to attribute.', 'final_demand': 'Final-demand categories; omitted = all.'},
        'input_example': {'io_table': '<raw_handle>', 'extension': '...'},
    },
    'env_multipliers': {
        'fn': 'env_multipliers',
        'description': 'env_multipliers -- category 44-environment-energy-climate, method card #367.',
        'args': {'io_table': 'Handle to a loaded multi-regional table.', 'extension': 'Environmental extension.'},
        'input_example': {'io_table': '<raw_handle>', 'extension': '...'},
    },
    'env_embodied_trade': {
        'fn': 'env_embodied_trade',
        'description': 'env_embodied_trade -- category 44-environment-energy-climate, method card #367.',
        'args': {'io_table': 'Handle to a loaded multi-regional table.', 'extension': 'Environmental extension.', 'region': 'Region to report for; omitted = all.'},
        'input_example': {'io_table': '<raw_handle>', 'extension': '...'},
    },
    'env_decompose_index': {
        'fn': 'env_decompose_index',
        'description': 'env_decompose_index -- category 44-environment-energy-climate, method card #368.',
        'args': {'data': 'Factors by period, one column per driver.', 'total': 'Column holding the aggregate being decomposed.', 'factors': 'Driver columns.', 'method': 'Index form.', 'form': 'Additive or multiplicative decomposition.'},
        'input_example': {'data': '<df_handle>', 'total': '...', 'method': 'lmdi_i', 'form': 'additive'},
    },
    'env_scenario_filter': {
        'fn': 'env_scenario_filter',
        'description': 'env_scenario_filter -- category 44-environment-energy-climate, method card #369.',
        'args': {'data': 'Scenario data in the standard long format.', 'model': 'Models to keep.', 'scenario': 'Scenarios to keep.', 'variable': 'Variables to keep.', 'region': 'Regions to keep.', 'year': 'Years to keep.'},
        'input_example': {'data': '<df_handle>'},
    },
    'env_scenario_harmonise': {
        'fn': 'env_scenario_harmonise',
        'description': 'env_scenario_harmonise -- category 44-environment-energy-climate, method card #369.',
        'args': {'data': 'Scenario data.', 'history': 'Historical values to harmonise to.', 'base_year': 'Year to harmonise on.', 'method': 'Harmonisation method.', 'convergence_year': 'Year the adjustment converges to zero.'},
        'input_example': {'data': '<df_handle>', 'history': '<df_handle>', 'base_year': 1, 'method': 'ratio', 'convergence_year': 2050},
    },
    'env_scenario_aggregate': {
        'fn': 'env_scenario_aggregate',
        'description': 'env_scenario_aggregate -- category 44-environment-energy-climate, method card #369.',
        'args': {'data': 'Scenario data.', 'mapping': 'Aggregation mapping.', 'dimension': 'Dimension to aggregate.', 'method': 'Aggregation function.'},
        'input_example': {'data': '<df_handle>', 'mapping': '<df_handle>', 'dimension': 'region', 'method': 'sum'},
    },
    'env_ekc': {
        'fn': 'env_ekc',
        'description': 'env_ekc -- category 44-environment-energy-climate, method card #370.',
        'args': {'data': 'Country-year panel.', 'emissions': 'Emissions column.', 'income': 'Income column.', 'controls': 'Control columns.', 'unit': 'Column identifying the country.', 'time': 'Column identifying the period.', 'form': 'Functional form.', 'cluster': 'Clustering variable for standard errors.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'data': '<df_handle>', 'emissions': '...', 'income': '...', 'unit': '...', 'time': '...', 'form': 'quadratic', 'conf_level': 0.95},
    },
    'env_degree_days': {
        'fn': 'env_degree_days',
        'description': 'env_degree_days -- category 44-environment-energy-climate, method card #371.',
        'args': {'temperature': 'Temperature series.', 'base_heating': 'Heating base temperature.', 'base_cooling': 'Cooling base temperature.', 'frequency': 'Aggregation frequency.'},
        'input_example': {'temperature': '<series_handle>', 'base_heating': 15.5, 'base_cooling': 22.0, 'frequency': 'monthly'},
    },
    'env_weather_normalise': {
        'fn': 'env_weather_normalise',
        'description': 'env_weather_normalise -- category 44-environment-energy-climate, method card #371.',
        'args': {'demand': 'Energy demand series.', 'hdd': 'Heating degree days.', 'cdd': 'Cooling degree days.', 'controls': 'Additional control columns.', 'estimate_base': 'Estimate the balance point instead of assuming it.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'demand': '<series_handle>', 'hdd': '<series_handle>', 'cdd': '<series_handle>', 'estimate_base': False, 'conf_level': 0.95},
    },
    'env_climate_macro_map': {
        'fn': 'env_climate_macro_map',
        'description': 'env_climate_macro_map -- category 44-environment-energy-climate, method card #372.',
        'args': {'scenario': 'Climate scenario variables.', 'elasticities': 'Mapping elasticities from scenario to macro variables.', 'horizon': 'Horizon in years.', 'component': 'Risk component to map.'},
        'input_example': {'scenario': '<df_handle>', 'elasticities': '<df_handle>', 'horizon': 30, 'component': 'both'},
    },
    'env_damage_function': {
        'fn': 'env_damage_function',
        'description': 'env_damage_function -- category 44-environment-energy-climate, method card #372.',
        'args': {'temperature': 'Warming path in degrees.', 'function': 'Damage-function family.', 'parameters': 'Override the default parameters.'},
        'input_example': {'temperature': '<series_handle>', 'function': 'nordhaus'},
    },
    'env_kaya': {
        'fn': 'env_kaya',
        'description': 'env_kaya -- category 44-environment-energy-climate, method card #373.',
        'args': {'emissions': 'Emissions.', 'population': 'Population.', 'output': 'Output.', 'energy': 'Primary energy.', 'method': 'Attribution method.'},
        'input_example': {'emissions': '<series_handle>', 'population': '<series_handle>', 'output': '<series_handle>', 'energy': '<series_handle>', 'method': 'lmdi'},
    },
    'env_energy_balance': {
        'fn': 'env_energy_balance',
        'description': 'env_energy_balance -- category 44-environment-energy-climate, method card #373.',
        'args': {'data': 'Energy flows by carrier and stage.', 'carrier': 'Column identifying the energy carrier.', 'stage': 'Column identifying the balance stage.', 'value': 'Column holding the flow.'},
        'input_example': {'data': '<df_handle>', 'carrier': '...', 'stage': '...', 'value': '...'},
    },
}
