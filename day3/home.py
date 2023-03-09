import json
import itertools
with open("beasts.json", "r") as f:
    beasts = json.loads(f.read())
print(beasts)


l = [1,2,3,4,5]

print(list(itertools.combinations(l,2)))