from functools import reduce
from datetime import datetime

print("start ", datetime.now())
li = [x for x in range(1, 9000)]
print(datetime.now(), "array ready, loop reduce start ")
r = li[0]
for i in range(1, len(li)):
    r = sum([r,li[i]])
print(datetime.now(), "loop reduce finish")
# print(r)
print(datetime.now(), "start internal reduce ")
red = reduce(lambda x, y: sum([x,y]), li)
print(datetime.now(), "finished internal rediuce ")
# print(red)

l = [[2, 8, 9, 3, 1, 11, 12], [2, 4, 6, 3, 4, 1, 3, 4], [
    1, 3, 14, 15, 16, 17], [1, 2, 3, 4], [3, 1, 4, 5], [1, 2, 3, 4, 5, 6, 7]]
redo = reduce(lambda x, y: set(x)&set(y), l)
print(redo)
l = [[2, 8, 9, 3, 1, 11, 12], [2, 4, 6, 3, 4, 1, 3, 4], [
    1, 3, 14, 15, 16, 17], [1, 2, 3, 4], [3, 1, 4, 5], [1, 2, 3, 4, 5, 6, 7], [3,9,8,7,0], [7,2,3,4]]
p = set(l[0])
print(f"шаг 1 предыдущий результат {p} текущий элемент {p} результат операции {p}")
for i in range(1, len(l)):
    print(
        f"шаг {i+1} предыдущий результат {p} текущий элемент {l[i]} результат операции {p&set(l[i])}")
    p = p&set(l[i])
print(p)

l = [{"c":1,"l":4}, {"c":3,"l":7},{"c":4,"l":4},{"c":7,"l":4},{"c":4,"l":4}]
l1 = [{"c":2,"l":4}, {"c":5,"l":7},{"c":4,"l":4},{"c":8,"l":4},{"c":5,"l":4}]

l11 = list(map(lambda x: x["c"], l))
l12 = list(map(lambda x: x["c"], l1))

print(l11, l12)
