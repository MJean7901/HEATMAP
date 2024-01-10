import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

N= 50

E0 = 0 *N
I0 = 0.25 *N
R0 = 0
S0 = N - (E0 - I0 - R0)



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

