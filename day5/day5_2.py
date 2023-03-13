from itertools import groupby
import random


def getDictsByKeyValue(dicts, key, value):
    dictsres = list(filter(lambda dict: dict[key] == value, dicts))
    return dictsres


d = [{"name": "Michael", "age": 29}, {"name": "Lisa", "age": 9},
     {"name": "Naomi", "age": 19}, {"name": "Michael", "age": 23}, {"name": "Lisa", "age": 33}]

# groupby  -  обязательная сортировка
#  [1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 5, 6]
#  [(1,[1,1]), (2,[2,2,2])] ...


#print( list(map(lambda x : (x[0], list(x[1])), list(groupby(l, key=lambda x: x))) ))
d.sort(key=lambda x: x["name"])

result = []
for x, y in groupby(d, key=lambda x: x["name"]):
    result.append({x:list(y)})
    
    
res = []

key = "name"
value = d[0][key]
res = {value:[d[0]]}
for x in range(1, len(d)):
    if value == d[x][key]:
        res[value].append(d[x])
    else:
        value = d[x][key]
        res[value] = [d[x]]
print(res)

res1 = list( map(lambda x : (x, res[x]), res) )
print(res1)

m = sum(map(lambda x: x["age"], d))
print(m)

result = []
for x, y in groupby(d, key=lambda x: x["name"]):
    result.append({x:  sum(map(lambda x: x["age"], y))})
   
print(result)

result = []
for x, y in groupby(d, key=lambda x: x["name"]):
    result.append({x:  len(list(y))})

print(result)
