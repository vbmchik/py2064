import copy
from pprint import pprint

def route(a, b):
    if a == b :
        return
    for i in range(le):
        if i == a or i == b :
            continue
        if not links[a][i]:
            continue
        if themap[a][i] + themap[i][b] == themap[a][b]:
            routes.append(i+1)
            route(i,b)
            break
    

themap = [
    [0, 4, 0, 0, 0, 0, 0, 0, 0, 0],
    [4, 0, 5, 0, 0, 1, 0, 0, 0, 0],
    [0, 5, 0, 6, 0, 0, 0, 0, 0, 0],
    [0, 0, 6, 0, 3, 0, 0, 0, 0, 0],
    [0, 0, 0, 3, 0, 0, 0, 1, 0, 7],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 5, 0, 0],
    [0, 0, 0, 0, 7, 0, 0, 0, 0, 0]
]

links = copy.deepcopy(themap)

""" themap = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
] """

le = len(themap)

routes = []

    
pprint(routes)
for a in range(le):
    for b in range(le):
        if a == b or not themap[a][b]:
            continue
        for c in range(le):
            if c == b or c == a:
                continue
            if themap[a][b] and themap[b][c]:
                d = themap[a][b] + themap[b][c]
                if themap[a][c] > d or not themap[a][c]:
                    themap[a][c] = d
                    themap[c][a] = d



pprint(themap) 
route(2,7)
pprint(routes)
