# a*x**2 + b*x + c = 0
# d = b**2 - 4*a*c
# x1 = ( -b + d ) / (2*a)
# x2 = ( -b - d ) / (2*a)

import math


def Meq( a: float, b: float, c: float):
    if a == 0 and b == 0 :
        if c == 0:
            return (0, 0, 0)
        else:
            return (0,0,-1)
    if a == 0:
        return (-c/b)
    d = b**2 - 4*a*c
    if d < 0 :
        return (0,0,-1)
    else:
        d = math.sqrt(d)
    x1 = ( -b + d ) / (2*a)
    x2 = ( -b - d ) / (2*a)
    if x2 > x1 :
        return (x1, x2)
    else :
        return (x2, x1)
    
