import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the model
def model(y, t, beta, gamma, mu, alpha, delta, tau, lambda_):
    S1, Sg1, E1, I1, R1, S2, Sg2, E2, I2, R2 = y

    S1_prime = -gamma * S1 + tau * S2 - tau * S1 + lambda_ * Sg1
    Sg1_prime = gamma * S1 + tau * Sg2 - mu * E1 + tau * Sg1 - beta * Sg1 * I1 / (S1 + Sg1 + E1 + I1 + R1) - lambda_ * Sg1
    E1_prime = beta * Sg1 * I1 / (S1 + Sg1 + E1 + I1 + R1) + tau * E2 - (alpha + tau) * E1
    I1_prime = alpha * E1 + tau * I2 - (delta + tau) * I1
    R1_prime = delta * I1 + tau * (R2 - R1)
    
    S2_prime = -gamma * S2 + tau * (S1 - S2) + lambda_ * Sg2
    Sg2_prime = gamma * S2 + tau * Sg2 - mu * E2 + tau * Sg2 - beta * Sg2 * I2 / (S2 + Sg2 + E2 + I2 + R2) - lambda_ * Sg2
    E2_prime = beta * Sg2 * I2 / (S2 + Sg2 + E2 + I2 + R2) + tau * E1 - (alpha + tau) * E2
    I2_prime = alpha * E2 + tau * I1 - (delta + tau) * I2
    R2_prime = delta * I2 + tau * (R1 - R2)

    return [S1_prime, Sg1_prime, E1_prime, I1_prime, R1_prime, S2_prime, Sg2_prime, E2_prime, I2_prime, R2_prime]

# Initial number of individuals in each compartment
# (You need to adjust these numbers)
S1_0, Sg1_0, E1_0, I1_0, R1_0 = 50, 0, 13, 0, 0
S2_0, Sg2_0, E2_0, I2_0, R2_0 = 50, 0, 13, 0, 0

# Total population, N
N1 = S1_0 + Sg1_0 + E1_0 + I1_0 + R1_0
N2 = S2_0 + Sg2_0 + E2_0 + I2_0 + R2_0

# Parameters (can be adjusted)
beta = 2/14
gamma = 0.75 #go-out rate
mu = 1 - 0.75; #protection rate
alpha = 0.5 
delta = 1/14
tau = 0.25
lambda_ = 0.5 #social distancing

# A grid of time points (in days)
t = np.linspace(0, 360, 360)

# Initial conditions vector
y0 = [S1_0, Sg1_0, E1_0, I1_0, R1_0, S2_0, Sg2_0, E2_0, I2_0, R2_0]

# Integrate the ODEs over the time grid, t
result = odeint(model, y0, t, args=(beta, gamma, mu, alpha, delta, tau, lambda_))

final_infected_city1 = result[-1, 3]
final_infected_city2 = result[-1, 8]
print(f"Final number of infected individuals in City 1: {final_infected_city1}")
print(f"Final number of infected individuals in City 2: {final_infected_city2}")


# Plotting
plt.figure(figsize=[12, 12])

# Plot for City 1
plt.subplot(2, 1, 1)  # 2 rows, 1 column, 1st subplot
plt.plot(t, result[:, 0], label='Susceptible in City 1')
plt.plot(t, result[:, 2], label='Exposed in City 1')
plt.plot(t, result[:, 3], label='Infected in City 1')
plt.plot(t, result[:, 4], label='Recovered in City 1')
plt.xlabel('Time / days')
plt.ylabel('Number of Individuals')
plt.title('Disease Spread Over Time in City 1')
plt.legend()

# Plot for City 2
plt.subplot(2, 1, 2)  # 2 rows, 1 column, 2nd subplot
plt.plot(t, result[:, 5], label='Susceptible in City 2')
plt.plot(t, result[:, 7], label='Exposed in City 2')
plt.plot(t, result[:, 8], label='Infected in City 2')
plt.plot(t, result[:, 9], label='Recovered in City 2')
plt.xlabel('Time / days')
plt.ylabel('Number of Individuals')
plt.title('Disease Spread Over Time in City 2')
plt.legend()

plt.tight_layout()
plt.show()


