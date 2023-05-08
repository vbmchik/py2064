# Пятая задача реальное собеседовение (высокий уровень)

# У вас есть девять цифр: 1, 2, …, 9.
# Именно в таком порядке.
# Вы можете вставлять между ними знаки «+», «-» или ничего.
# У вас будут получаться выражения вида 123+45-6+7+89.
# Найдите все из них, которые равны 100.

# 123456789
from pprint import pprint
from solver import solve

def insert_signs(digits, index, output):
    signs = ["+", "-", '*', '/', ""]
    if index == len(digits):
        if output[-1] not in signs:
            if solve(output) == 200:
                l.append(output)
        return
    for s in signs:
        insert_signs(digits, index + 1, output + digits[index] + s)


l = []
insert_signs("123456789", 0, "")

pprint(l)
