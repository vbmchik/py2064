import pprint


class First():
    x = 5
    y = 9
    z = 19

class Student():
    
    def __init__(self, name: str, age: int, sex: str, faculty: str ) -> None:
        self.name = name
        self.age = age
        self.sex = sex
        self.faculty = faculty
        
    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return f"Student: {self.name}, Age: {self.age}, Sex: {self.sex}, Faculty: {self.faculty}"
        
class Phrase():
    x = 2

    def __init__(self, line: str) -> None:
        line = ''.join([x for x in line.lower() if x.isalpha() or x == ' '])
        self.x -= 1
        self.phrase = list(filter(lambda x: x != '', line.split(' ')))


    def __repr__(self) -> str:
        res = ''
        for w in self.phrase:
            res += w+" "
        return res

    def __str__(self) -> str:
        res = ''
        for w in self.phrase:
            res += w
        return res


p = First()  # Создание этого объекта
print(p.x)
print(p.y+p.z)
c = First()
p.x = 4

print(p.x, c.x)

ph = Phrase("I love this world!")

print(ph.phrase)
pprint.pprint(ph.phrase)

print(ph)
pprint.pprint(ph)

student = Student("Manny Krawitz", 21, "male", "maths")
print(student)
pprint.pprint(student)

l = [1,2,3,5,6]

manny = Student("Manny Krawitz", 21, "male", "maths")