from sympy import *
init_printing()

A,A2,B,C,D,k1,k2,a = symbols("A,A2,B,C,D,k1,k2,a")

eq = [A+B-C-D, 
      C*exp(1j*k2*a) + D*exp(-1j*k2*a) - A2*exp(1j*k1*a), 
      k1*(A-B) - k2*(C-D), 
      k2*(C*exp(1j*k2*a) - D*exp(-1j*k2*a)) - k1*A2*exp(1j*k1*a)]

sol = solve(eq)[0]
print(f"A = {sol[A]}\nB = {sol[B]}")

# returns:
# 
# A = 0.25*A2*(-k1**2*exp(2.0*I*a*k2) + k1**2 + 2.0*k1*k2*exp(2.0*I*a*k2) + 2.0*k1*k2 - k2**2*exp(2.0*I*a*k2) + k2**2)*exp(I*a*(k1 - k2))/(k1*k2)
# B = 0.25*A2*(-k1**2*exp(2.0*I*a*k2) + k1**2 + k2**2*exp(2.0*I*a*k2) - k2**2)*exp(I*a*(k1 - k2))/(k1*k2)