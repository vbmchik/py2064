from day6_5 import Team
from day6_3 import Dog

class MyTeam(Team):
    
    def __init__(self, trainer: str, second_trainer: str) -> None:
        super().__init__(trainer)
        self.second_trainer = second_trainer
    
    def printTeam(self):
        print(self.trainer)
        print(self.second_trainer)
        for dog in self.dogs:
            print(dog)

    def changeTrainer(self, trainer: str, second_trainer: str):
        super().changeTrainer(trainer)
        self.second_trainer = second_trainer
        
    def removeDogFromTeam(self, dogName: str):
        poordog = list(filter(lambda x: x.name == dogName, self.dogs))
        if len(poordog) == 0 :
            return
        for dog in poordog:
            self.dogs.remove(dog)

    def removeDogWithAgeFromTeam(self, dogName: str, dogAge: int):
        poordog = list(filter(lambda x: x.name == dogName and x.age == dogAge, self.dogs))
        if len(poordog) == 0:
            return
        for dog in poordog:
            self.dogs.remove(dog)
            

        
