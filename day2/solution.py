import copy
from home import getDictsByKeyValue, getBeastByName, deleteBeastByName, addSerie, delSerie

def combunit(ar):    # [ [], [], [] ]
    p = set(ar[0]) 
    for x in range(1, len(ar)):
        p = p & set(ar[x])
    if (len(p) > 0):
        print(p, ar)

def changeColor(beasts, name, color):
    getBeastByName(beasts, name)["Цвет"] = color


def addBeast(beasts: list, name: str, color: str, series: list):
    d = {}
    d["Имя"] = name
    d["Цвет"] = color
    d["Серии"] = series
    beasts.append(d)
# ([2, 4, 6, 3, 4, 1, 3, 4], [1, 3, 14, 15, 16, 17], [1, 2, 3, 4, 5, 6, 7])
#              0                      1                      2
#      p&set(ar[i])
#
def compareSeries(beasts, name1, name2):
    b1 = getBeastByName(beasts, name1)
    b2 = getBeastByName(beasts, name2)
    combunit([b1["Серии"], b2["Серии"]])

beasts = list()

beasts.append({
    "Имя": "Лосяш",
    "Цвет": "Шафрановый",
    "Серии": ["Герой Плутона", "Бабочка", "Долгая рыбалка"]
})

beasts.append({
    "Имя": "Копатыч",
    "Цвет": "Коричневый",
    "Серии": ["Долгая рыбалка", "Кулинария", "Танцор Диско"]
})

addBeast(beasts, "Хрюндель", "Серый", [
         "Кулинария", "Долгая рыбалка",  "Бабочка"])

compareSeries(beasts, "Копатыч", "Хрюндель")
changeColor(beasts, "Копатыч", "Зеленый")
print(len(beasts))
beasts2 = copy.deepcopy(beasts)
delSerie(beasts2, "Хрюндель", "Кулинария")
print(beasts)
print(beasts2)
