import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parameters
gamma = 0.75 # Go-out rate
beta = 2./14  # Exposure rate
mu = 0  # Rate of becoming susceptible again
lambda_ = 0.5  # Rate of becoming immobile
alpha = 0.5  # Infection rate
tau = 0.25  # Travel rate between cities
delta = 1./14  # Recovery rate

# Total population in each city
N1 = 50
N2 = 50

# Initial number of infected and exposed individuals
I1_0 = 25
I2_0 =10
E1_0 =0
E2_0 = 0

# Initial conditions
S1_0 = N1 - I1_0 - E1_0
Sg1_0 = 0
R1_0 = 0
S2_0 = N2 - I2_0 - E2_0
Sg2_0 = 0
R2_0 = 0

# Time points
t = np.linspace(0, 160, 160)

# The model equations
def model(y, t, N1, N2, gamma, beta, mu, lambda_, alpha, tau, delta):

    S1, Sg1, E1, I1, R1, S2, Sg2, E2, I2, R2 = y
    N1_total = S1 + Sg1 + E1 + I1 + R1
    N2_total = S2 + Sg2 + E2 + I2 + R2
    
    dS1dt = -gamma * S1 + tau * S2 - tau * S1 + lambda_ * Sg1
    dSg1dt = gamma * S1 - mu * E1 - beta * Sg1 * I1 / N1_total - lambda_ * Sg1 + tau * Sg2 - tau * Sg1
    dE1dt = beta * Sg1 * I1 / N1_total - (alpha + tau) * E1 + tau * E2
    dI1dt = alpha * E1 - (delta + tau) * I1 + tau * I2
    dR1dt = delta * I1 + tau * R2 - tau * R1
    
    dS2dt = -gamma * S2 + tau * S1 - tau * S2 + lambda_ * Sg2
    dSg2dt = gamma * S2 - mu * E2 - beta * Sg2 * I2 / N2_total - lambda_ * Sg2 + tau * Sg1 - tau * Sg2
    dE2dt = beta * Sg2 * I2 / N2_total - (alpha + tau) * E2 + tau * E1
    dI2dt = alpha * E2 - (delta + tau) * I2 + tau * I1
    dR2dt = delta * I2 + tau * R1 - tau * R2

    return [dS1dt, dSg1dt, dE1dt, dI1dt, dR1dt, dS2dt, dSg2dt, dE2dt, dI2dt, dR2dt]

# Initial conditions vector
y0 = [S1_0, Sg1_0, E1_0, I1_0, R1_0, S2_0, Sg2_0, E2_0, I2_0, R2_0]

# Integrate the ODEs
solution = odeint(model, y0, t, args=(N1, N2, gamma, beta, mu, lambda_, alpha, tau, delta))
S1, Sg1, E1, I1, R1, S2, Sg2, E2, I2, R2 = solution.T

max_infections_city1 = np.max(I1)
max_infections_city2 = np.max(I2)

print("Maximum number of infections in City 1:", max_infections_city1)
print("Maximum number of infections in City 2:", max_infections_city2)
plt.figure(figsize=(12, 8))

# City 1
plt.subplot(2, 1, 1)  # 2 rows, 1 column, first subplot
plt.plot(t, S1, 'b-', label='Susceptible in City 1')
plt.plot(t, Sg1, 'c-', label='Mobile Susceptible in City 1')
plt.plot(t, E1, 'y-', label='Exposed in City 1')
plt.plot(t, I1, 'r-', label='Infected in City 1')
plt.plot(t, R1, 'g-', label='Recovered in City 1')
plt.title('Simulation of Disease Spread in City 1')
plt.xlabel('Time / days')
plt.ylabel('Number of individuals')
plt.legend()
plt.grid()
plt.ylim(0, 50)

# City 2
plt.subplot(2, 1, 2)  # 2 rows, 1 column, second subplot
plt.plot(t, S2, 'b-', label='Susceptible in City 2')
plt.plot(t, Sg2, 'c-', label='Mobile Susceptible in City 2')
plt.plot(t, E2, 'y-', label='Exposed in City 2')
plt.plot(t, I2, 'r-', label='Infected in City 2')
plt.plot(t, R2, 'g-', label='Recovered in City 2')
plt.title('Simulation of Disease Spread in City 2')
plt.xlabel('Time / days')
plt.ylabel('Number of individuals')
plt.legend()
plt.grid()
plt.ylim(0, 50)

plt.tight_layout()
plt.show()
