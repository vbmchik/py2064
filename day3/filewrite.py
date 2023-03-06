from jsonmy import printJson

coding="utf-8"
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

with open("beasts.json", "w+t", encoding="utf-8") as somefile:
    somefile.write(printJson(beasts))
    

