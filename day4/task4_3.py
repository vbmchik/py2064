from functools import reduce


def clearword(word):
    cleanword = ''.join([x for x in word if x.isalpha()])
    return cleanword


with open('beasts.txt', "r") as f:
    words = [clearword(word.lower()) for line in f for word in line.split()]
print(words)
redwords = set(reduce(lambda x, y: set(x) | {y}, words))
redwords = set(filter(lambda x: x != '', words))
print(redwords)
cwords = set(filter(lambda x: x != "", words))
print(cwords)

print({1,2}|{4,3})
