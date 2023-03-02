#new day
import random 

def createrandomlist():
    l = [ random.randint(1,6) for x in range(1,10) ]
    return l

def squareoflist( x: list ) -> list:
    for i in range(0, len(x), 1):
        if( x[i]%2 ):
          x[i] = x[i]**2
        else:
           x[i] += 1
5+1



l = [0,2,4,7,5,4,2]
m = l
l[2] = 12
m[4] = 222
print(m)
squareoflist(l)
print(l)
print(createrandomlist())


b = lambda x: x**2
y = lambda x,y,z: x+y+z
print(y(3,4,5))