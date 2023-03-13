from datetime import datetime
from itertools import groupby
from time import perf_counter


def clearword(word):
    cleanword = ''.join([x for x in word if x.isalpha() or x == ' '])
    return cleanword


def mapfunc(word):
    return [word, 1]

def reducefunc(key, values):
    return [key, len(values)]


with open('advs.txt', 'r') as shfile:
    text = shfile.read().lower()
text = clearword(text)
text = list(filter(lambda x: x != '', text.split(" ")))
print(len(text))
start_time = perf_counter()
print(datetime.now())

mapwords = map(mapfunc, text)
mapwords_sorted = sorted(mapwords, key=lambda x: x[0])
reduce_result = []
for x, y in groupby(mapwords_sorted,lambda x: x[0]):
    reduce_result.append(reducefunc(x,list(y)))
d = dict(sorted(reduce_result, key=lambda x: x[1], reverse=True))    
end_time = perf_counter()

print(f'Time taken: {end_time-start_time: 0.2f} seconds')
print(datetime.now())

n = 10
for x in d:
    print(x, d[x])
    n -=1
    if n == 0:
        break
