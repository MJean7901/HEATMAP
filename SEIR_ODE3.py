import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parameters
beta = 2/14     # Exposure rate
gamma = 0.75    # Go-out rate of susceptible individuals
mu = 0.5        # Rate at which an exposed individual becomes susceptible
lambda_ = 0.5   # Rate at which mobile susceptible individuals will be immobile
alpha = 0.5     # Rate at which exposed individuals become infected
tau = 0.5       # Rate at which individuals travel to another city
delta = 1/14    # Rate at which infected individuals become non-infectious

# Initial conditions
S10, Sg10, E10, I10, R10 = 100, 0, 25, 25, 0  # City 1
S20, Sg20, E20, I20, R20 = 100, 0, 25, 25, 0  # City 2

# ODE system
def model(y, t):
    S1, Sg1, E1, I1, R1, S2, Sg2, E2, I2, R2 = y

    dS1dt = -gamma * S1 + tau * S2 - tau * S1 + lambda_ * Sg1
    dSg1dt = gamma * S1 + tau * Sg2 - mu * E1 + tau * Sg1 - beta * Sg1 * I1 / (S1 + Sg1 + E1 + I1 + R1) - lambda_ * Sg1
    dE1dt = beta * Sg1 * I1 / (S1 + Sg1 + E1 + I1 + R1) + tau * E2 - (alpha + tau) * E1
    dI1dt = alpha * E1 + tau * I2 - (delta + tau) * I1
    dR1dt = delta * I1 + tau * (R2 - R1)

    dS2dt = -gamma * S2 + tau * (S1 - S2) + lambda_ * Sg2
    dSg2dt = gamma * S2 + tau * Sg2 - mu * E2 + tau * Sg2 - beta * Sg2 * I2 / (S2 + Sg2 + E2 + I2 + R2) - lambda_ * Sg2
    dE2dt = beta * Sg2 * I2 / (S2 + Sg2 + E2 + I2 + R2) + tau * E1 - (alpha + tau) * E2
    dI2dt = alpha * E2 + tau * I1 - (delta + tau) * I2
    dR2dt = delta * I2 + tau * (R1 - R2)

    return [dS1dt, dSg1dt, dE1dt, dI1dt, dR1dt, dS2dt, dSg2dt, dE2dt, dI2dt, dR2dt]

# Time points
t = np.linspace(0, 360, 360)

# Initial conditions vector
y0 = [S10, Sg10, E10, I10, R10, S20, Sg20, E20, I20, R20]

# Integrate the ODEs
solution = odeint(model, y0, t)

# Plotting
plt.figure(figsize=(12, 8))
plt.plot(t, solution[:, 0], label='S1')
plt.plot(t, solution[:, 1], label='Sg1')
plt.plot(t, solution[:, 2], label='E1')
plt.plot(t, solution[:, 3], label='I1')
plt.plot(t, solution[:, 4], label='R1')
plt.plot(t, solution[:, 5], label='S2')
plt.plot(t, solution[:, 6], label='Sg2')
plt.plot(t, solution[:, 7], label='E2')
plt.plot(t, solution[:, 8], label='I2')
plt.plot(t, solution[:, 9], label='R2')
plt.xlabel('Time / days')
plt.ylabel('Number of people')
plt.title('Disease spread dynamics in two cities')
plt.legend()
plt.grid(True)
plt.show()
