import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

d1, d2 = 2.13e-10, 1.23e-10

U = np.array([3.0, 3.5, 4.0, 4.5, 5.0]) * 1e3

D1 = np.array([2.8, 2.7, 2.6, 2.5, 2.4]) * 1e-2
D2 = np.array([5.0, 4.7, 4.4, 4.1, 3.9]) * 1e-2

R1, R2 = D1/2, D2/2
sqrt_U_inv = U**(-1/2)

fit_R1 = linregress(sqrt_U_inv, R1)
fit_R2 = linregress(sqrt_U_inv, R2)

def create_plot(X, Y, fit, filename=None, ylabel = "Y"):
    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(7,4), sharex=True)
    ax1.scatter(X, Y,  c="r")
    
    lin_X = np.array([min(X)-(max(X)-min(X))/6 , max(X)+(max(X)-min(X))/6])
    ax1.plot(lin_X, fit[0] * lin_X + fit[1], c="g", label="Fit: T")

    ax2.axhline(y=0, c="black", linestyle="--")
    ax2.scatter(X, Y - (fit[0] * X + fit[1]))
    
    ax1.set_title(f"a = {fit[0]:.3}+/-{fit[4]:.3} , b = {fit[1]:.3}+/-{fit.intercept_stderr:.3} , R-Wert = {fit[2]:.3}, $R^2$-Wert = {fit[2]**2:.3}")
    ax1.grid()
    ax1.set_xlim(lin_X)
    ax2.set_xlabel(r"$\frac{1}{\sqrt{U}}$ in $\left[\mathrm{V}^{-1/2}\right]$")
    ax1.set_ylabel(ylabel + r"in [m]")
    ax2.set_ylabel("Residuum in [m]")
    fig.subplots_adjust(hspace=0)
    plt.tight_layout()

    if filename:
        plt.savefig(filename + ".svg")

create_plot(sqrt_U_inv, R1, fit_R1, "fit_R1", "$R_1$")
create_plot(sqrt_U_inv, R2, fit_R2, "fit_R2", "$R_2$")