class Dog():
    
    def __init__(self, name:str, age:str) -> None:
        self.name = name
        self.age = age
    
    def bark(self)->None:
       print(f"{self.name} barks - bow, bow, bow") 
         
    def __str__(self)->str:
        return f"Dog name {self.name}, age {self.age}" 