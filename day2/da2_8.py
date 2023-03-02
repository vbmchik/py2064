# range(1,10,1), [1,3,2,5,4,3,7,9,8], [5,3,4,5,6,3,1,3,5]

newone = list(map( lambda x,y,z: max(x,y,z), range(1,10,1), [1,3,2,5,4,3,7,9,8], [5,3,4,5,6,3,1,3,5]))
print(newone)

l = [1,4,2,6,3]
l1 = [2,4,2,67,5,3,1]
l2 = [1,5,3,6]

l3 = [l,l1,l2]
print(l3)
print(max(l3))

inp = ["miller","mullum","bayley", "kook", "100101", "10101", "010010"]

newinp = list(filter(lambda x: x[::-1] == x, inp))
print(newinp)

print(l[::-1])