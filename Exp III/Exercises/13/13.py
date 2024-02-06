import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import scipy.constants as pcs
from scipy.optimize import fsolve

me = 9.109383e-31 # kg
f = 2*me/(pcs.hbar**2)

V0 = -4*pcs.e # J (-4 eV)
L = 6e-10 # m (6 Angstrom)

E_n = [np.pi**2 / L**2 / f * n**2 - np.abs(V0) for n in range(1,5)]

def func(E, *args):
    symmetric = args[0]
    if E>=0 or E<=V0:
        return 1e10
    k_E = np.sqrt(f * (E - V0))
    kappa_E = np.sqrt(-f * E)
    kappa_k = (1 if symmetric else -1)*k_E*np.tan(L/2*k_E)**(1 if symmetric else -1)
    return (kappa_E - kappa_k)

roots =  [fsolve(func, V0*0.8, True),
          fsolve(func, V0*0.5, False)]

print(f"Energieniveaus des unendlichen Potenzialkasten: \n\t{E_n = }\n ")
print(f"Energieniveaus des endlichen Potenzialkasten: \n\tE_n = {roots}")
print("""\nEs fällt auf, dass es im endlichen Potenzialkasten nur endlich viele 
erlaubte Energieniveaus gibt, anders als im unendlichen Potenzialkasten. 
Außerdem ist das niedrigste Energieniveau im endlichen Potenzialkasten niedriger.""")

# Ausgabe des Programms:

# Energieniveaus des unendlichen Potenzialkasten: 
# 	E_n = [-4.735187684281048e-19, 2.8536887087580535e-20, 8.652963129470561e-19, 2.036759509150322e-18]
#
# Energieniveaus des endlichen Potenzialkasten: 
# 	E_n = [array([-5.4680873e-19]), array([-2.82871858e-19])]
#
# Es fällt auf, dass es im endlichen Potenzialkasten nur endlich viele 
# erlaubte Energieniveaus gibt, anders als im unendlichen Potenzialkasten. 
# Außerdem ist das niedrigste Energieniveau im endlichen Potenzialkasten niedriger.