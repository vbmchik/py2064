from datetime import datetime
from time import perf_counter
def clearword(word):
    cleanword = ''.join([x for x in word if x.isalpha() or x == ' '])
    return cleanword


def mapfunc( word ):
    return [word, 1]

with open('advs.txt', 'r') as shfile:
    text = shfile.read().lower()
text = clearword(text)
text = list(filter( lambda x : x != '', text.split(" ")))

start_time = perf_counter()
print(datetime.now())
wordcount = {}
for word in text:
    if not word in wordcount:
        s = 0
        for sword in text:
            if word == sword:
                s +=1
        wordcount[word] = s

print(wordcount)
end_time = perf_counter()

print(f'Time taken: {end_time-start_time: 0.2f} seconds')
print(datetime.now())

