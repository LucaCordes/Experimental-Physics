import numpy as np
import matplotlib.pyplot as plt

L = 9
# $1\peq\int_0^L \dx \abs\psi^2 \implies A = \sqrt{\frac2L}$
psi = lambda x, n: np.sqrt(2/L) * np.sin(n * np.pi / L * x)

X = np.linspace(*(lim:=[-.2*L, 1.2*L]), N:=1000)
Y = np.array([psi(X,n) for n in (1,2,3)]) **2
Y[:, (0>X) | (X>L)] = 0

fig, axes = plt.subplots(3,1,sharex=True)
axes[0].set_xlim(*lim)
fig.supxlabel(r"$x$ in $[cm]$")
fig.supylabel(r"Wahrscheinlichkeitsdichte in $[1/\mathrm{cm}]$ für n=1,2,3")

for n,ax in enumerate(axes):
    ax.plot(X,Y[n])

fig.savefig("2.svg")