import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# Baro Formel
p0 = 101325 # Pa
rho0 = 1.292 # kg m^-3
g = 9.81 # m s^-2
H = (p0)/(rho0*g) * 1e-3 # km

# Brechungsindex Meereshöhe
n0 = 1.00029

# Höhe
h0 = 0.0 # km

# Stützstellen
L = 100.0 # km
N = 100 + 1

p = lambda h: p0 * np.exp(-h/H)
n = lambda h: (n0 - 1) / p0 * p(h) + 1

def optischeWeglaenge(H, start=0, end=0, dx=1):
    H = [start, *H, end] 
    dL = np.sqrt(np.diff(H)**2 + dx**2)
    N = [n(h) for h in H[:-1]]
    l_optisch = np.sum(N * dL)
    return l_optisch

print("%.6f km" % optischeWeglaenge([0]*(N-2)))

res = minimize(optischeWeglaenge, [0]*(N-2))

print(res.message)
print("%.6f km" % res.fun)
h_stuetz = res.x

plt.plot(np.linspace(0,100,101), [0, *res.x, 0])
plt.xlabel("l in [km]")
plt.ylabel("h in [km]")
plt.grid()
plt.show()