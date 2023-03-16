from day6_3 import Dog

# team contains trainer and a list (pride) of dogs
class Team():
    
    def __init__(self, trainer: str) -> None:
        self.trainer = trainer
        self.dogs = []
        
    def changeTrainer(self, trainer: str):
        self.trainer = trainer
        
    def addDog(self, dog: Dog) -> None:
        self.dogs.append(dog)
    
    def transferTeam(self, team):
        self.dogs.extend(team.dogs)
        team.dogs.clear()
        
    def mixTeam(self, team, n):
        for _ in range(n):
            self.dogs.append(team.dogs.pop(0))
    
    def sortTeam(self, name: bool):
        # True - name, False - age
        self.dogs.sort(key=lambda x: x.name if name  else x.age )
    
    def printTeam(self):
        print(self.trainer)
        for dog in self.dogs:
            print(dog)