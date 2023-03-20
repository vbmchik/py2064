class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        pass

    def describe_restaurant(self):

        name_type = f"Ресторан:{self.restaurant_name}, Кухня:{self.cuisine_type}"
        return name_type.title()

    def describe_restaurant_name(self):

        name_rest = f"Название ресторана: {self.restaurant_name}"
        return name_rest.title()

    def describe_restaurant_cuisine(self):

        cuisine_rest = f"Кухня в ресторане: {self.cuisine_type}"
        return cuisine_rest.title()
    
    def __str__(self) -> str:
        return f"Название ресторана: {self.restaurant_name} Кухня в ресторане: {self.cuisine_type}"

    def open_restaurant(self):
        return "Ресторан открыт"
