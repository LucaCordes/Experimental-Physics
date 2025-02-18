from scipy.optimize import fsolve
import numpy as np
from scipy.constants import e, epsilon_0 
alpha, r0, kappa, z =  1.7476, 2.820e-10, 4.17e-11, 6

def scaled_eq1(params):
    B, rho = params
    left = (B / rho) * np.exp(-r0 / rho)
    right = (e**2 * alpha) / (4 * np.pi * epsilon_0 * z * r0**2)
    return (left - right) / right

def scaled_eq2(params):
    B, rho = params
    term1 = -2 * (e**2 * alpha) / (4 * np.pi * epsilon_0 * r0**3)
    term2 = (z * B / rho**2) * np.exp(-r0 / rho)
    d2U_dr2 = term1 + term2
    kappa_term = 18 * r0 / kappa
    return (d2U_dr2 - kappa_term) / kappa_term 

def scaled_equations(params):
    return [scaled_eq1(params), scaled_eq2(params)]

B, rho  = fsolve(scaled_equations, [1e-16, 3e-11])

print(f"{B = :.3} J\n{rho = :.3} m")

# returns:
# >>> B = 1.75e-16 J
# >>> rho = 3.22e-11 m