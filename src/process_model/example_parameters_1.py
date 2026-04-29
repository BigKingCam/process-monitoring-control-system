"""
Filename: example_parameters_1.py
Purpose: Default process parameters to use in process_model_dynamics.py.
Author: Cameron L. Nolen
Created: 2026-01-07
"""


DEFAULT_PARAMS: dict[str, float] = {
    "T_amb": 25.0,       # °C
    "T_in": 20.0,        # °C
    "m": 100.0,          # kg
    "m_dot": 1.0,        # kg/s
    "c_p": 4.18,         # kJ/kg·°C (water)
    "hA": 0.5            # kW/°C
}
