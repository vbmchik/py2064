from itertools import groupby
from pprint import pprint

# [1,2,4,1,2,1,6,4,2,1]

input = [
    ('11013331', 'KAT'),
    ('9085267',  'NOT'),
    ('5238761',  'ETH'),
    ('5349618',  'ETH'),
    ('11788544', 'NOT'),
    ('962142',   'ETH'),
    ('7795297',  'ETH'),
    ('7341464',  'ETH'),
    ('9843236',  'KAT'),
    ('5594916',  'ETH'),
    ('1550003',  'ETH')
]

input.sort(key=lambda x: x[1])
print(input)
result = {}
for k, g in groupby(input, lambda x: x[1]):
    result[k] = list( v[0] for v in g )
    
test = { k: list(v[0] for v in g) for k, g in groupby(input, key=lambda x: x[1]) }    
pprint(test)