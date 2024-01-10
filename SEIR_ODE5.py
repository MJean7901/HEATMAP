import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

N = 50.  # Total number of individuals, N
I0, R0, E0 = 20., 0, 0  # Initial number of infected and recovered individuals
S0 = N - I0 - E0- R0  # Susceptible individuals to infection initially is deduced
beta, gamma = 0.90, 1./14
alpha = 0.50 #infection rate
# Contact rate and mean recovery rate
tmax = 360  # A grid of time points (in days)
Nt = 160
t = np.linspace(0, tmax, Nt+1)

def derivative(X, t):
    S, E, I, R = X
    dotS = -beta * S * I / N
    dotE = beta * S * I/N - alpha*E
    dotI = alpha * E - gamma*I
    dotR = gamma * I
    return np.array([dotS,dotE, dotI, dotR])

X0 = S0, E0, I0, R0  # Initial conditions vector
res = integrate.odeint(derivative, X0, t)
S, E, I, R = res.T

# Print the maximum number of infected individuals
max_infected = np.max(I)
print(f"Maximum number of infected individuals: {max_infected}")

plt.figure()
plt.grid()
plt.title("odeint method")
plt.plot(t, S, 'orange', label='Susceptible')
plt.plot(t, I, 'r', label='Infected')
plt.plot(t, R, 'g', label='Recovered with immunity')
plt.xlabel('Time t, [days]')
plt.ylabel('Numbers of individuals')
plt.ylim([0, N])
plt.legend()
plt.show()

