# the following class represents are car

class Car():
    """Represents a car"""

    def __init__(self, make, model, year): # create three parameters: make, model, year
        """Attributes to describe car""" # init take parameters and stores them in attributes associated ...
        self.make = make # ... with instances made from class
        self.model = model
        self.year = year

    def get_descriptive_name(self): #  put make, model and year in desriptive string
        """Return a nearly formatted descriptive name"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

my_new_car = Car("Audi", "A4", 2016)
print(my_new_car.get_descriptive_name())

my_new_car = Car("Land Rover", "Defender", 1969)
print(my_new_car.get_descriptive_name())