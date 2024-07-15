# (a)
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd

data = pd.read_csv('Rutherford.csv', delimiter=';', decimal=',')
data = data.query("Counts>0")

data.plot.scatter(x="Winkel [deg]", y="Rate [1/s]")
plt.savefig("1.svg")

#(b)
theta, rate = np.array(data.get(["Winkel [deg]", "Rate [1/s]"])).T
f = lambda theta, a, b: a * np.sin(theta * 2*np.pi/360 /2)**b
fit, _ = curve_fit(f, theta, rate)

# (c)
plt.scatter(theta,rate, label="data", marker="+")
plt.scatter(theta,f(theta, *fit), label=f"fit, $a={fit[0]:.3}$, $b={fit[1]:.3}$", marker="+")
plt.legend()
plt.yscale("log")
plt.xlabel("Winkel [deg]")
plt.ylabel("Zählrate [1/s]")
plt.savefig("2.svg")

# Theoretisch ist b=-4 zu erwarten -> relative Abweichung: ~2.75 % 


