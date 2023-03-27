from itertools import groupby
from pprint import pprint
data = []
with open('input.txt', "r") as file:
    for line in file.readlines():
        l = []
        for word in line.split():
            l.append(''.join(filter(lambda x: x.isalnum(), word)))
        data.append(tuple(l))

data.sort(key=lambda x: x[2])
pprint(data)

result = {}
for y in groupby(data, key=lambda x: x[2]):
    l = list(y[1])
    print(l)
    result[y[0]] = {t[1]: t[0] for t in l}

# (0,1), (3,4) -> {"0":1, "3":4}

resulttest = dict(
    map(
        lambda y: (y[0], {t[1]: t[0] for t in y[1]}),
        groupby(data, key=lambda x: x[2])
    )
)


trt = { y[0]: {t[1]: t[0] for t in y[1] } for y in groupby(data, key=lambda x: x[2])}
pprint(trt)
