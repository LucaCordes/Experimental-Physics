import matplotlib.pyplot as plt
from numpy import pi, sqrt, log
from astropy.constants import alpha
plt.rcParams.update({"xtick.top": True , "ytick.right": True,
"xtick.minor.visible": True, "ytick.minor.visible": True,
"xtick.direction": "in" , "ytick.direction": "in",
"axes.labelsize": "large", "text.usetex": False, "font.size": 11})

# Nr.4
c,hbar,epsilon0,kB = 1,1,1,1
m_e = 0.51 # MeV
K = 0.307 # MeV / g / cm^2
rho = 1.06 # g / cm^3
ZA = 0.53768
I = 68.7e-6 # MeV
L = 1 # cm

particles = ["muon", "pion", "kaon", "proton", "alpha"]
particle_masses = [105.7, 139.6, 493.7, 938.3, 3727.4] # MeV
particle_charges = [1,1,1,1,2] * sqrt(4*pi*alpha) # 1

gamma = lambda p,M: sqrt(1 + (p / M)**2)
beta = lambda p,M: sqrt(1 - 1 / (gamma(p,M))**2)
W_max = lambda p,M: 2 * m_e * c**2 * beta(p,M)**2 * gamma(p,M)**2 / (1 + 2*gamma(p,M)*m_e/M + (m_e/M)**2)

dEdx = lambda p,M,z: K * rho * z**2 * ZA / beta(p,M)**2 * gamma(p,M)**2 / (1/2 * np.log(2 * m_e * c**2 * beta(p,M)**2 * gamma(p,M)**2 * W_max(p,M) / I**2) - beta(p,M)**2) 

xlim = [1/2,8000]
p = np.linspace(*xlim,10000)
fig,ax = plt.subplots()
ax.set_xscale("log")
ax.set_yscale("log")
ax.set(xlabel="p in MeV",ylabel="(dE/dx in MeV/cm) bzw. ($\\approx \\Delta E$ in MeV)", xlim=xlim, title="Ionisierungsverluste")

for particle, mass, charge in zip(particles, particle_masses, particle_charges):
    DE = [dEdx(p, mass, charge) for p in p]
    ax.plot(p, np.divide(DE,mass), label=particle)
    argmin = np.argmin(DE[np.argmax(DE):])
    min = p[argmin]
    print(f"{particle:6}:    argmin        = {min:.5} MeV")
    print(f"{"":11}dE/dx(argmin) = {DE[argmin]:.5} MeV/cm")

ax.axvline(10**2.2, linestyle="--", label="158.5 MeV")
ax.legend()
fig.savefig("2.svg")