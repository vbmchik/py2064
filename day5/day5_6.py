from datetime import datetime
from time import perf_counter


def clearword(word):
    cleanword = ''.join([x for x in word if x.isalpha() or x == ' '])
    return cleanword


def mapfunc(word):
    return [word, 1]


with open('advs.txt', 'r') as shfile:
    text = shfile.read().lower()
text = clearword(text)
text = list(filter(lambda x: x != '', text.split(" ")))

start_time = perf_counter()
print(datetime.now())
wordcount = {}
for word in text:
    if not word in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] = wordcount[word] + 1
       

#print(wordcount)
end_time = perf_counter()
result = [ (x,y) for x,y in wordcount.items() ]
result.sort(key=lambda x: x[1])
print(f'Time taken: {end_time-start_time: 0.2f} seconds')
print(datetime.now())
#print(result)
