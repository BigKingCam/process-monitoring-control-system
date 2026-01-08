### simulate.py
## this file will:
# step the ODE (process_model_dynamics.py function thermal_tank_dynamics) forward in time
# generate tagged outputs
# add noise
# compute efficiency

import numpy as np
import matplotlib.pyplot as plt

from src.process_model.process_model_dynamics import thermal_tank_dynamics
from src.process_model.example_parameters_1 import DEFAULT_PARAMS

# time definition - since PLCs and SCADA work in discrete time; and since 1-second resolution is realistic
dt = 1.0        # seconds
t_end = 3600    # 1 hour
time = np.arange(0, t_end, dt)      # outputs an array with values between <0> and <t_end> with step value <dt>

# inputs (fuel / heater power) definitions
Q_in = np.zeros_like(time)
    # step input (simulating fuel valve change)
Q_in[time >= 600] = 120.0     # kW
# this simulates system startup (0's), operator change, control action

# initialize state variables
T = np.zeros_like(time)     # temperature (°C)
T[0] = 20.0     # initial temperature (°C)


## Time-Stepped Simulation
params = DEFAULT_PARAMS

for k in range(len(time) - 1):
    dT_dt = thermal_tank_dynamics(        
        T = T[k],
        Q_in = Q_in[k],
        T_amb = params["T_amb"],
        T_in = params["T_in"],
        m = params["m"],
        m_dot = params["m_dot"],
        c_p = params["c_p"],
        hA = params["hA"]
    )
T[k + 1] = T[k] + dT_dt * dt    # Euler integration (PLC-like)


# sensor noise
np.random.seed(0)   # ?TODO: make more/true random
sensor_noise_std = 0.3 # (°C)

Temp_Out = T + np.random.normal(0, sensor_noise_std, size = len(T))
# result: true process temperature, measured sensor value


# KPI2 Efficiency Deviation computation
Efficiency = np.zeros_like(time)

for k in range(len(time)):
    if (Q_in[k] > 0):
        Efficiency[k] = (params["m_dot"] * params["c_p"] * (Temp_Out[k] - params["T_in"])) / Q_in[k]
    else:
        Efficiency[k] = 0.0

# SCADA-style tags (Ignition-esque)
tags = {
    "Temp_Out" : Temp_Out,
    "Fuel_Input" : Q_in,
    "Efficiency" : Efficiency
}


## Example Plot Generation
plt.figure()
plt.plot(time / 60, Temp_Out)
plt.xlabel("Time (minutes)")
plt.ylabel("Temperature (°C)")
plt.title("Process Temperature")
plt.grid()

plt.figure()
plt.plot(time / 60, Efficiency)
plt.xlabel("Time (minutes)")
plt.ylabel("Efficiency")
plt.title("Thermal Efficiency")
plt.grid()

plt.show()
