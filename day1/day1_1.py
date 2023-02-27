# 2064 start 19:00

l = [1,2,3,4,5,6,7,8,9,10]
l = []
n = 1
while n < 11:
   l.append(n)
   n = n+1
   
l = []
for i in range(1,11):
    if not i%2:    # 0 если кратно 2 
        l.append(i)
print(l)    

l = [ x for x in range(1,11) ]


l = [ x for x in range(1,11) if not x%2 ]

print(l) 

if not 5%2:
    print('Bububu')
    
# and or
    
l = [ x for x in range(1,101) if not x%2 and x%3 and not x%5 ]
print(l)
# четное число и одновременно не делится на три и одновременно делится на 5

for x in range(1,31):
    if not x%3:
        print(f'{x} делится на 3')