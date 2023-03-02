def mx(x, y):
    return x - y if x > y else x + y

l = [ x**3 if x < 5 else x**2 for x in range (1, 10) ]

q = lambda x,y : (x+y,x-y,x*y,x**y)

print(q(3,2))

print(l)