w = "miChae232l jA3434cks4on"
print(w.title())

for c in w.lower():
    print(c)
    
print( len(w) )

print(w[4])

w = list(w.lower())
print(w)
#w[4] = 'c'
w = ''.join( x for x in w if x.isalpha() or x == ' ' ).title()
#w = ''.join(w)
print(w)