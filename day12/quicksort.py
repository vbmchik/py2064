# быстрая сортировка
import random
from time import perf_counter


def quicksort(arr):
    if len(arr) < 2:
        return arr
    # берем PIVOT (опорный элемент) как первый элемент массива
    pivot = arr[0]
    # делим массив на два один с элементами меньше или равными pivot другой c элементами больше PIVOT
    smaller = [x for x in arr[1:] if x <= pivot]
    larger = [x for x in arr[1:] if x > pivot]
    return quicksort(smaller)+[pivot]+quicksort(larger)


def quicksortplanar(array):
    stack = [(0, len(array)-1)]
    # пока stack не пустой
 
    while stack:
        low, high = stack.pop()
        # Ищем индекс опорного элемента
        pivot = partition(array, low, high)
        # левый массив загоняем в стек
        if low < pivot - 1:
            stack.append((low, pivot-1))
        if high >= pivot + 1:
            stack.append((pivot+1, high))
# 2 4 3 5 1  
# 2 1 3 5 4
# уже поменяли
# нам нужно все элементы меньше чем pivot переместить в начало нашего списка
def partition(array, low, high):
    pivot = random.randint(low, high)
    array[pivot], array[high] = array[high], array[pivot]
    i = low - 1
    for j in range(low, high):
        # если текущий элемент меньше или равен опорному
        if array[j] <= array[high]:
            i += 1
            array[i], array[j] = array[j], array[i]
    #  первый элемент больше pivot меняем с ним местами
    array[i+1], array[high] = array[high], array[i+1]
    return i+1


def ordinarysort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if (arr[i] > arr[j]):
                arr[i], arr[j] = arr[j], arr[i]



l = [random.randint(1, 45000) for _ in range(1000000)]
#l = [3, 5, 4, 7, 12, 34, 2, 1]
print("ordinary")
start = perf_counter()
#ordinarysort(l)
quicksort(l)
end = perf_counter()-start
print(f"finished in {end}")
print("quick")
start = perf_counter()
quicksortplanar(l)
end = perf_counter()-start
print(f"finished in {end}")
