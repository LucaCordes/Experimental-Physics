import numpy as np

tests = [["Argon", 18], 
         ["Sauerstoff", 8], 
         ["Kupfer", 29], 
         ["Krpyton", 36], 
         ["Uran", 92]]

def next_shell():
    n,l = 0,0
    yield n+1,l
    while True:
        if l==0:
            n += 1
            while l+1 <= n-1:
                n, l = n-1, l+1
        else: 
            n,l = n+1, l-1
        yield n+1,l

def orbital(Z):
    spd = "spdfghijklmno"
    nl = next_shell()
    max_e = lambda l: 2*(2*l+1)

    while Z>0:
        n,l = next(nl)
        electrons_used = min(Z, max_e(l))
        Z -= electrons_used
        print(f"{n}{spd[l]}{electrons_used}", end=" ")

for element, Z in tests:
    print(f"\n{element:10}, {Z=:2}: ", end="")
    orbital(Z) 

# outputs:
# Argon      (Z=18): 1s2 2s2 2p6 3s2 3p6 
# Sauerstoff (Z= 8): 1s2 2s2 2p4 
# Kupfer     (Z=29): 1s2 2s2 2p6 3s2 3p6 4s2 3d9 
# Krpyton    (Z=36): 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 
# Uran       (Z=92): 1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f4