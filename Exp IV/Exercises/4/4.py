from sympy import *
from sympy.plotting import *

a = 5.291e-11

Z, a0, r, theta, phi = symbols("Z a0 r theta phi")
x, y, z = symbols("x y z")

phi1 = 1/sqrt(pi) * (Z/a0)**(3/2) * exp(-Z*r/a0)
phi2 = -1/(8*sqrt(pi)) * (Z/a0)**(3/2) * (Z*r)/a0 * exp(-Z*r/(2*a0))* sin(theta) * exp(1j * phi)
phi3 = sqrt(2)/(81*sqrt(pi)) * (Z/a0)**(3/2) * (6-Z*r/a0) * (Z*r)/a0 * exp(-Z*r/(3*a0))* cos(theta) 

cartesian = lambda f: f.subs({r: sqrt(x**2 + y**2 + z**2),
                              theta: acos(z / sqrt(x**2 + y**2 + z**2)),
                              phi: atan2(y,x),
                              Z:1,
                              a0:a}) 

cart_phi = [(abs(cartesian(phi)))**2 for phi in [phi1,phi2,phi3]]

for phi, name in zip(cart_phi, ("phi_1,0,0", 
                                "phi_2,1,+1", 
                                "phi_3,1,0")):
    try: 
        m = 10
        plot3d(phi.subs(x, 0), (z,-m*a,m*a),(y,-m*a,m*a), size=(8,8), title=name+", z-y")
        plot3d(phi.subs(y, 0), (x,-m*a,m*a),(z,-m*a,m*a), size=(8,8), title=name+", x-z")
        plot3d(phi.subs(z, 0), (x,-m*a,m*a),(y,-m*a,m*a), size=(8,8), title=name+", x-y")
    except:
        pass