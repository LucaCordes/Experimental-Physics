import scipy.constants as c

def J2eV(J): 
    # $1\u{eV} = q\sub{elektron} \cdot 1\u{V} = 1.602\E{-19}\u{J} \implies 1\u{J} = \frac1{1.602\E{-19}}\u{eV} $ 
    return J / c.elementary_charge

def m2angstrom(m): 
    # $1\, \A = 10^{-10}\u{m} \implies 1\u{m} = 10^{10}\,\A$
    return m * 1e10

def kg2MolH2O(kg): 
    # $m / n = M_{\schemie{H2O}} \implies n = \frac{m}{M_{\schemie{H2O}}}$
    return kg / 18.01528e-3

def eV2lambda(eV): 
    # $E=hf=\frac{hc}{\lambda} \implies \lambda = \frac{hc}{E}$
    return c.h * c.c / c.elementary_charge / eV  

def eV2f(eV): 
    # $E=hf \implies f = \frac{E}{h}$
    return eV * c.elementary_charge / c.h

def i(x):
    return float(x)

for f in [i, J2eV, m2angstrom, kg2MolH2O, eV2lambda, eV2f]:
    print(f"{f.__name__+('' if f is i else '(i)'):13}" , end="")
    for n in range(1,11):
        print(f"{f(n):10.3}", end="")
    print("")

# returns:
# i                   1.0       2.0       3.0       4.0       5.0       6.0       7.0       8.0       9.0      10.0
# J2eV(i)        6.24e+18  1.25e+19  1.87e+19   2.5e+19  3.12e+19  3.74e+19  4.37e+19  4.99e+19  5.62e+19  6.24e+19
# m2angstrom(i)     1e+10     2e+10     3e+10     4e+10     5e+10     6e+10     7e+10     8e+10     9e+10     1e+11
# kg2MolH2O(i)       55.5  1.11e+02  1.67e+02  2.22e+02  2.78e+02  3.33e+02  3.89e+02  4.44e+02     5e+02  5.55e+02
# eV2lambda(i)   1.24e-06   6.2e-07  4.13e-07   3.1e-07  2.48e-07  2.07e-07  1.77e-07  1.55e-07  1.38e-07  1.24e-07
# eV2f(i)        2.42e+14  4.84e+14  7.25e+14  9.67e+14  1.21e+15  1.45e+15  1.69e+15  1.93e+15  2.18e+15  2.42e+15