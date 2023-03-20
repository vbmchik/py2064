from day6_home1 import Restaurant

class IceCreamStand( Restaurant ):
    
    def __init__(self, restaurant_name):
        super().__init__(restaurant_name, "Ice Cream")
        self.flavors = []
    
    def __str__(self) -> str:
        return super().__str__() + f" flavors {self.flavors}"

        
stand = IceCreamStand("Stand1")
stand.flavors.append("Choco")
stand.flavors.append("Vanilla")
stand.flavors.append("Fruitty")
stand.flavors.append("Beer")

print(stand)