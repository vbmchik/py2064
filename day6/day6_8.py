from day6_5 import Team
from day6_3 import Dog
from day6_7 import MyTeam

m = MyTeam("Mike Waldberg", "Louise Mitchell")
m.addDog(Dog("Charlie", 6))
m.addDog(Dog("Marlie", 9))

m.changeTrainer("Rene Decart", "Albert Einstein")

m.printTeam()
a = Dog("Charlie", 6)
b = Dog("Charlie", 6)
print(a)
print(b)
