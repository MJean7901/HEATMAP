import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

N = 50
E0 ,I0 , R0= 0.25*N, 0.25*N, 0
Sg0 = 0
S0 = N - I0 - E0 - R0

gamma = 0.25 #go out rate
beta = 2./14 #exposure rate
mu = 0.25 #protection rate
lambda_ = 0.5
alpha = 0.5
tau = 0.25 #travel rate
delta = 1./14

tmax = 160
Nt= 160
t = np.linspace(0, tmax, Nt+1)

def derivative(X, t):
    S, Sg, E, I, R = X
    dotS = -gamma * S0 + lambda_ * Sg0
    dotSg = gamma*S0 + mu*E0  - beta*Sg*(I0/N) - lambda_*Sg0
    dotE = beta*Sg0 *(1/N) - alpha* E0
    dotI = alpha*E0 - delta*I0
    dotR = delta * I0 
    return np.array([dotS, dotSg, dotE, dotI, dotR])

X0 = S0, Sg0, E0, I0, R0
res = integrate.odeint(derivative, X0, t)
S ,Sg, E , I, R =res.T

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








