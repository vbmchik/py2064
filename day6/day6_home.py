from day6_5 import Team
from day6_3 import Dog
from day6_7 import MyTeam

m = MyTeam("Mike Waldberg", "Louise Mitchell")
m.addDog(Dog("Charlie", 6))
m.addDog(Dog("Marlie", 9))
m.removeDogWithAgeFromTeam("Marlie", 19)
print(m)
l = sorted(m.dogs, key=lambda x: x.name)
m.removeDogFromTeam("Marlie")
print(l)
print(m.dogs)
print(l[0])
