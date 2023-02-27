a = True
b = False
c = True
# and -> True and True = True ; True and False = False ; False and False = False
# or  -> True or True = True ; True or False = True ; False or False = False

print( a and b )  # False
print( a and c )  # True
print( a or b )   # True
print( (a and c ) or b ) # True
print( a or b or c) # True
print( a and b and c ) # False


    