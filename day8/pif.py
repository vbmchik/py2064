def Pythagoras(a, b, c):
    l = [a,b,c]
    l.sort()
    a = l[0]
    b=l[1]
    c=l[2]
    return a**2 + b**2 == c**2
