# one way to to have a method that updates certain attributes for you
# instead if changing the attribute directly here is a way of updating an attribute internally

class Car():
    """Represents a car"""

    def __init__(self, make, model, year):
        """Attributes to describe car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a nearly formatted descriptive name"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        """Shows car mileage"""
        print("This car has " + str(self.odometer_reading) + " miles on it.\n")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cant roll back an odometer")

    def increment_odometer(self,miles):
        self.odormeter_reading += miles

my_new_car = Car("Audi", "A4", 2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(21) # call update_odometer() and give it value of 23
my_new_car.read_odometer()

my_new_car = Car("Land Rover", "Defender", 1969)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(3403)
my_new_car.read_odometer()