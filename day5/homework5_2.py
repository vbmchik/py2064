"""создать длинный список отсортировтаь его вручную как сможете в циклах и методом sort сравнить время
сравнить время алгоритма урока по подсчету количества слов и вашего ДЗ
"""


import random
import time

my_list = [random.randint(0, 999) for _ in range(10000)]
#my_list = [random.randint(0, 999) for _ in range(10)]


def manualSort(list):
    num = len(list)
    for x in range(num):
        for y in range(num-x-1):
            if list[y] > list[y+1]:
                list[y], list[y+1]  = list[y+1],list[y]
                pass
            pass
        pass
    pass

start_time = time.time()
manualSort(my_list)
end_time = time.time()
print(f'Time taken: {end_time-start_time: 0.2f} seconds')
    

start_time = time.time()
my_list.sort()
end_time = time.time()
print(f'Time taken: {end_time-start_time: 0.2f} seconds')
