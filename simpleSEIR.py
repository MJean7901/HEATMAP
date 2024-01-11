import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

N= 50

E0 = 0 *N
I0 = 0.25 *N
R0 = 0
S0 = N - (E0 - I0 - R0)

gamma = 0.25 #go-out rate
alpha = 0.25 #infection rate
delta = 1./14 #recovery rate

tmax = 360
Nt = 160
t= np.linspace(0,tmax, Nt+1)

def derivative(X,t):
        S, E, I, R =X
        S_prime = (-gamma *S * I)/N
        E_prime = ((gamma * S * I)/N) - alpha*E
        I_prime = alpha*E - delta * I
        R_prime = delta * I
        return np.array([S_prime, E_prime, I_prime, R_prime])

X0 = S0, E0, I0, R0
res = integrate.odeint(derivative, X0, t)
S, E, I, R = res.T

max_infected = np.max(I)
print (print(f"Maximum number of infected individuals: {max_infected}"))

plt.figure()
plt.grid()
plt.title("odeint method")
plt.plot(t, S, 'blue', label='Susceptible')
plt.plot(t, E, 'orange', label='exposed')
plt.plot(t, I, 'r', label='Infected')
plt.plot(t, R, 'g', label='Recovered with immunity')
plt.xlabel('Time t, [days]')
plt.ylabel('Numbers of individuals')
plt.ylim([0, N])
plt.legend()
plt.show()

