"""
Filename: process_model_dynamics.py
Purpose: Process model function describing the dynamics of the systems
            (thermal tank or boiler).
Author: Cameron L. Nolen
Created: 2026-01-07
"""


# A first-order, lumped-parameter thermal process used as a surrogate for
# boiler operation and efficiency analysis.
def thermal_tank_dynamics(
    T: float,
    Q_in: float,
    T_amb: float,
    T_in: float,
    m: float,
    m_dot: float,
    c_p: float,
    hA: float
) -> float:
    """
    Computes dT/dt for a well-mixed thermal tank.

    Parameters
    ----------
    T : float
        Current tank temperature (°C)
    Q_in : float
        Heat input (kW)
    T_amb : float
        Ambient temperature (°C)
    T_in : float
        Inlet temperature (°C)
    m : float
        Mass of fluid (kg)
    m_dot : float
        Mass flow rate (kg/s)
    c_p : float
        Specific heat capacity (kJ/kg·°C)
    hA : float
        Heat loss coefficient (kW/°C)

    Returns
    -------
    dTdt : float
        Time derivative of temperature (°C/s)
    """

    heat_loss = hA * (T - T_amb)
    E_flow_loss = m_dot * c_p * (T - T_in)
    dT_dt = (Q_in - heat_loss - E_flow_loss) / (m * c_p)

    return dT_dt
