import numpy as np 
import matplotlib.pyplot as plt
import scipy.stats as stats
import scipy.constants as c
from scipy.optimize import curve_fit
import pandas as pd
plt.rcParams.update({"xtick.top": True          , "ytick.right": True,
                     "xtick.minor.visible": True, "ytick.minor.visible": True,
                     'xtick.direction': "in"    , "ytick.direction": "in"})

df = pd.read_csv('DopplerfreieSpektroskopieRubidium.csv', skiprows=3)
[X,CH1,CH2,CH3] = np.array(df).T
X *= 0.016

plt.plot(X,CH1,linewidth=0.3)
plt.xlabel("Frequenz [GHz]")
plt.ylabel("Amplitude [a.u.]")
plt.savefig("a.svg")

# (c)
def f(x,p0,p1,A1,A2,A3,A4,mu1,mu2,mu3,mu4,std1,std2,std3,std4):
    return p0 + p1*x + A1*stats.norm.pdf(x,mu1,std1) + A2*stats.norm.pdf(x,mu2,std2) + A3*stats.norm.pdf(x,mu3,std3) + A4*stats.norm.pdf(x,mu4,std4) 

p0 = [1.3,-1/10, 
      -.8,-1,-.7,-.3,
      5.5,6.8,10,12.7,
      .4, .4, .4, .4]

fit, cov = curve_fit(f, X, CH1, p0=p0)
mu, std = fit[6:10], fit[10:]

plt.plot(X,CH1,linewidth=0.3)
plt.plot(X, f(X, *fit))
plt.xlabel("Frequenz [GHz]")
plt.ylabel("Amplitude [a.u.]")
plt.savefig("c.svg")

print(f"{"="*28}\n{"n":<3}{"mu_n [GHz]":12}{"sigma_n [GHz]":10}\n{"-"*28}")
for n, [mu_, std_] in enumerate(zip(mu,std)):
    print(f"{n:<3}{mu_:<12.3}{std_:<10.3}")
print("="*28)

"""
outputs:
============================
n  mu_n [GHz]  sigma_n [GHz]
----------------------------
0  5.67        0.362     
1  6.82        0.356     
2  10.1        0.337     
3  12.5        0.664     
============================
"""

# (e)
df = pd.read_csv('DopplerfreieSpektroskopieHyperfineStruktur.csv', skiprows=3)
[X,CH1,CH2] = np.array(df).T
X *= 0.0016

plt.plot(X_,CH1_,linewidth=0.6)
plt.xlim(1,1.5)
plt.xlabel("Frequenz [GHz]")
plt.ylabel("Amplitude [a.u.]")
plt.savefig("e.svg")

# %%
# (f)

# %%
# (g)


