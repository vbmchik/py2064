from day6_5 import Team
from day6_3 import Dog

team1 = Team("John Wick")
team2 = Team("Ada Lovelise")

team1.addDog(Dog("Snoop", 5))
team1.addDog(Dog("Rinha", 2))
team1.addDog(Dog("Jackson", 3))

team2.addDog(Dog("Cook", 6))
team2.addDog(Dog("Laila", 1))
team2.addDog(Dog("Cooper", 13))

team1.printTeam()
team2.printTeam()

team1.mixTeam(team2,2)
team1.printTeam()
team2.printTeam()

team1.sortTeam(False)
team1.printTeam()
