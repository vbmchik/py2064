import random
import time


def mySort(something: list, descend=False, key=None):
    # [ 4, 3, 6, 1 ]
    l = len(something)
    if key != None:
        for i in range(l - 1):
            marginal = i
            for j in range(i + 1, l):
                if (descend and key(something[j]) > key(something[marginal])) or (not descend and key(something[j]) < key(something[marginal])):
                    marginal = j
            p = something[marginal]
            something[marginal] = something[i]
            something[i] = p
    for i in range(l - 1):
        marginal = i
        for j in range(i + 1, l):
            if (descend and something[j] > something[marginal]) or (not descend and something[j] < something[marginal]):
                marginal = j
        if i != marginal:        
            p = something[marginal]
            something[marginal] = something[i]
            something[i] = p

def takeElement(x):
    return x[1]

l = [4, 3, 6, 1]
l1 = [(5, "Masha"), (3, "Leo"), (6, "Sigismund"), (1, "Ameli")]
mySort(l, False)
mySort(l1, False, takeElement)
print(l1)

my_list = [random.randint(0, 999) for _ in range(10000)]
start_time = time.time()
mySort(my_list,False)
end_time = time.time()
print(f'Time taken: {end_time-start_time: 0.2f} seconds')
