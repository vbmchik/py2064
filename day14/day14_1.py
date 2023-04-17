def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n - 1)
    
s = 0
n = 4
while n > 0:
    s = s + n
    n -= 1 

print(sum(4), s)

# (4)->4+(3)->3+(2)->2+(1)->{1}
