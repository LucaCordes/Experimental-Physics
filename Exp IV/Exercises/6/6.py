import numpy as np
import scipy.constants as c
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
plt.style.use("seaborn-v0_8-poster")

df = pd.read_csv("dataLines.csv")
nu = np.array(df).T * 1e2 # in $\ufrac{1}{m}$

# $E = h f = \frac{hc}{\lambda} = h c \bar{\nu}$
E = c.h * c.c * nu / c.e # in $\u{eV}$

E_mean = E.mean(axis=1)
E_std = E.std(axis=1, ddof=1)

fig, axes = plt.subplots(2,3,)
for n,ax in enumerate(axes.flatten()[:-1]):
    ax.set_title(f"Messreihe {n+1}")
    ax.hist(E[n], bins=20)
    ax.errorbar(E_mean[n], 1,xerr=E_std[n], c="r", fmt="o")

fig.supxlabel(r"$\Delta E$ in eV")
fig.supylabel(r"$n$ in 1")
fig.tight_layout()

# Fit 
X = np.arange(2,7)
fit, cov = curve_fit(lambda x,a,b: a*x+b, X, E_mean, sigma=E_std)
f = lambda x: fit[0] * x + fit[1]

print(f"A = {fit[0]:.3} +/- {np.sqrt(cov[0,0]):.3} eV")
print(f"b = {fit[1]:.3} +/- {np.sqrt(cov[1,1]):.3} eV")

# output:
# A = 9.72e-06 +/- 6.87e-08 eV
# b = 9.72e-06 +/- 2.57e-07 eV

# Fit-/ und Residuenplot
fig, [ax1,ax2] = plt.subplots(2,1,sharex=True)
fig.suptitle("Fit und Residuenplot")

X_ = np.arange(1,8)
Y_ = f(X_)
ax1.errorbar(X, E_mean, E_std, fmt="o")
ax1.plot(X_,Y_)
ax1.set_xlim(X_[0], X_[-1])
ax1.set_ylim(min(Y_),max(Y_)) 
ax1.set_ylabel(r"$\Delta E$ in eV")
ax1.grid()

res = (E_mean - f(X)) / E_std
ax2.errorbar(X, res, np.ones_like(X), fmt="o")
ax2.axhline(0, ls="--",c="r")
ax2.set_ylabel(r"$\Delta$ in $\sigma$")

plt.tight_layout()
plt.savefig("2.svg")
plt.show()