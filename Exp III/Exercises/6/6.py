import numpy as np
import matplotlib.pyplot as plt

# Konstanten
n0 = 1 # Luft
n1 = 2.35 # TiO2
n2 = 1.52 # Kronglas
d = 40 # [nm]

# Koeffizienten
r = lambda n1,n2: (n1-n2) / (n1+n2)
t = lambda n1,n2: -2*n1 / (n1+n2)

# Reflektivität
def R(l, max_depth=10):
    total_R = r(n0,n1)
    curr_A = t(n0,n1)
    curr_phase = 0
    for _ in range(max_depth):
        curr_A *= r(n1,n2)
        curr_phase = (curr_phase + 4*np.pi*d/l*n1) % (2*np.pi)
        total_R += curr_A*t(n1,n0) * np.cos(curr_phase)
        curr_A *= r(n1,n0)
    return total_R**2

# Plot
X = np.linspace(200,800,100)
Y = [R(x) for x in X]

plt.plot(X,Y)
plt.grid()
plt.xlim(200,800)
plt.xlabel("Wellenlänge $\\lambda$ in nm")
plt.ylabel("Reflektivität $R$")


# Erklärung für das Maximum:

# Trifft ein Lichtstrahl auf die Trennfläche zwischen Luft und Beschichtung 
# mit einer Phasenverschiebung von null, und ist die Dicke der Trennfläche 
# gerade $\frac\lambda4$ so ist die Reflektion bei Austritt aus der Beschichtung 
# aufgrund der zurückgelegten Strecke bei um $\pi$ Phasenverschoben, auch die 
# Transmission von $n_1$ nach $n_0$ führt zu einer Phasenverschiebung von $\pi$, 
# sodass bei dieser Konfiguration die Reflektion insgesammt um $2\pi$
# phasenverschoben ist und konstruktiv interferiert. Die $n$-te Reflektion 
# ist nach dem gleichem Schema um $n\cdot 2\pi$ phasenverschoben, es kommt 
# somit immer zur konstruktiven Interferenz und es handelt sich um ein Maximum.

# Damit die Dicke der Beschichtung tatsächlich $\frac\lambda4$ beträgt, müsste man 
# sie als $\frac\lambda{4n_1}$ wählen $(\approx 42.6 \mathrm{nm})$.
