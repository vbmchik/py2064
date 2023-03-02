
l1 = [2,4,3,5,1,7,2,8]
l2 = [3,1,6,5,4,4,8,9]
#l3 = [[3,2],[4,1],[6,3]..[9,8]] 

def p(x):
    return x**2

def p(x,y):
    return [x,y] if x > y else [y,x]

#q = list(map(p,l1))
q = list(map(lambda x: x%2==0, l1))
print(q)

m = []
for c in l1:
    m.append(c**2)
    
print(m)

t = list(map(p,l1,l2))
t1 = list(map( lambda x,y: [x,y] if x > y else [y,x] , l1, l2))
print(t)
print(t1)

q = []
for i in range(0, len(l1)):
    if l1[i] > l2[i]:
        q.append([l1[i],l2[i]])
    else:
        q.append([l2[i],l1[i]])
print(q)

q1 = []
for x,y in zip(l1,l2):
    if x > y :
        q1.append([x,y])
    else:
        q1.append([y,x])
print(q1)

q2 = []
for x,y in zip(l1,l2):
    q2.append([max(x,y),min(x,y)])
print(q2)

t2 = list(map( lambda x,y: [max(x,y),min(x,y)], l1, l2))
print(t2)