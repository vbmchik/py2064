from pprint import pprint


def mygroup(listobject, key):
    pkey = key(listobject[0])
    result = [(pkey, [listobject[0]])]
    for i in range(1, len(listobject)):
        if pkey == key(listobject[i]):
            result[-1][1].append(listobject[i])
        else:
            pkey = key(listobject[i])
            result.append((pkey,[listobject[i]]) )
    return result
            
            
test = [('5238761', 'ETH'), ('5349618', 'ETH'), ('962142', 'ETH'), ('7795297', 'ETH'), ('7341464', 'ETH'), ('5594916',
                                                                                                            'ETH'), ('1550003', 'ETH'), ('11013331', 'KAT'), ('9843236', 'KAT'), ('9085267', 'NOT'), ('11788544', 'NOT')]
result = {}
#l = mygroup(test, lambda x: x[1])
for k, g in mygroup(test, lambda x: x[1]):
    result[k] = list(v[0] for v in g)
pprint(result)

