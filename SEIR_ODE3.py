import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the model
def model(y, t, beta, gamma, mu, alpha, delta, tau, lambda_):
    S1, Sg1, E1, I1, R1, S2, Sg2, E2, I2, R2 = y

    S1_prime = (-gamma * S1) + (tau * S2) - (tau * S1) + (lambda_ * Sg1)
    Sg1_prime = (gamma * S1) + (tau * Sg2) - (mu * E1) + (tau * Sg1) - (beta * Sg1) * (I1 / (S1 + Sg1 + E1 + I1 + R1)) - (lambda_ * Sg1)
    E1_prime = (beta * Sg1) * ((I1) / (S1 + Sg1 + E1 + I1 + R1)) + (tau * E2) - ((alpha + tau) * E1)
    I1_prime = (alpha * E1) + (tau * I2) - ((delta + tau) * I1)
    R1_prime = (delta * I1) + (tau * (R2 - R1))
    
    S2_prime = (-gamma * S2) + (tau * S1) - (tau * S2) + (lambda_ * Sg2)
    Sg2_prime = (gamma * S2) + (tau * Sg2) - (mu * E2) + (tau * Sg2) - (beta * Sg2) * ((I2) / (S2 + Sg2 + E2 + I2 + R2)) - (lambda_ * Sg2)
    E2_prime = (beta * Sg2) * ((I2) / (S2 + Sg2 + E2 + I2 + R2)) + (tau * E1) - ((alpha + tau) * E2)
    I2_prime = (alpha * E2) + (tau * I1) - ((delta + tau) * I2)
    R2_prime = (delta * I2) + (tau * (R1 - R2))

    return [S1_prime, Sg1_prime, E1_prime, I1_prime, R1_prime, S2_prime, Sg2_prime, E2_prime, I2_prime, R2_prime]

# Initial conditions based on the new values
population = 50  # population

Ei0 = 0.05 * population  # Set to 5% of the population
Ii0 = 0.25 * population  # Set to 25% of the population
Ri0 = 0  # Initial number of removed individuals in each city

Si0 = [population - Ei0 - Ii0 for _ in range(2)]  # Initial number of susceptible residents
Sgi0 = 0  # Initial number of susceptible residents that can move

# Initial conditions vector
y0 = [Si0[0], Sgi0, Ei0, Ii0, Ri0,  # City 1
      Si0[1], Sgi0, Ei0, Ii0, Ri0]  # City 2

# Parameters with non-zero values
gamma = 0.25  # Adjusted go-out rate
beta = 2 / 14  # Exposure rate
mu = 0.25  # 1 - Rate at which an exposed individual becomes susceptible again
lambda_ = 0.5  # Rate at which mobile susceptible individuals will be immobile
alpha = 0.75  # Adjusted rate at which exposed individuals become infected
tau = 0.25  # Adjusted rate at which individuals travel to another city
delta = 1 / 14  # Rate at which infected individuals become non-infectious

# Time vector
t = np.linspace(0, 50, 50)  # Simulate for 100 time units

# Solve the ODEs
solution = odeint(model, y0, t, args=(beta, gamma, mu, alpha, delta, tau, lambda_))

# Extract the final values of Infected for both cities
I1_final, I2_final = solution[-1, 3], solution[-1, 8]

# Print final values of Infected
print(f"Final number of Infected in City 1: {I1_final}")
print(f"Final number of Infected in City 2: {I2_final}")

# Plot the results for Infected individuals
plt.plot(t, solution[:, 3], label='City 1')
plt.plot(t, solution[:, 8], label='City 2')
plt.xlabel('Time')
plt.ylabel('Infected Individuals')
plt.legend()
plt.show()