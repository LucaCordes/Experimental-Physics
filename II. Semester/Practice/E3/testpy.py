from sympy import *

a,b,c,d = symbols("a b c d")
f = Matrix([[a,b],[c,d]])

print(latex(f))