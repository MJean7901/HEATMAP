import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

N = 50. 
Sg0 = 0 # Total number of individuals, N
I0, R0, E0 = 20., 0, 0  # Initial number of infected and recovered individuals
S0 = N - I0 - E0- R0  # Susceptible individuals to infection initially is deduced
beta, gamma = 2./14, 0.25
lambda_ = 0.5
mu = 0.25
delta = 1./14
alpha = 0.50 #infection rate
# Contact rate and mean recovery rate
tmax = 50  # A grid of time points (in days)
Nt = 50
t = np.linspace(0, tmax, Nt+1)

def derivative(X, t):
    S, Sg, E, I, R = X
    dotS = -gamma * S + lambda_ *Sg
    dotSg = gamma * S -((beta * Sg * I )/ N) + mu * E
    dotE = beta * Sg *( I/N) - alpha*E
    dotI = alpha * E - delta*I
    dotR = delta * I
    return np.array([dotS,dotSg,dotE, dotI, dotR])

X0 = Sg0, S0, E0, I0, R0  # Initial conditions vector
res = integrate.odeint(derivative, X0, t)
S, Sg,  E, I, R = res.T

# Print the maximum number of infected individuals
max_infected = np.max(I)
print(f"Maximum number of infected individuals: {max_infected}")

plt.figure()
plt.grid()
plt.title("odeint method")
plt.plot(t, S, 'blue', label='Susceptible')
plt.plot(t, Sg, 'black', label='immobile')
plt.plot(t, E, 'yellow', label='Exposed')
plt.plot(t, I, 'r', label='Infected')
plt.plot(t, R, 'g', label='Recovered with immunity')
plt.xlabel('Time t, [days]')
plt.ylabel('Numbers of individuals')
plt.ylim([0, N])
plt.legend()
plt.show()


