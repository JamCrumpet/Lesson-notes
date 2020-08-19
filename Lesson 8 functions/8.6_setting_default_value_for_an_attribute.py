# every attribute in a class needs an initial value, even if that value is 0 or an empty string
# in some cases, such as when setting a default value, it makes since to specify this initial in the ...
# ... body of the init method
# if you do this you do this for an attribute you don't have to include a parameter for that attribute

# in this example we will add odometer_reading that starts with a value of 0
# and we will add a method to read each cars odometer

class Car():
    """Represents a car"""

    def __init__(self, make, model, year):
        """Attributes to describe car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # new attribute added, default is 0

    def get_descriptive_name(self):
        """Return a nearly formatted descriptive name"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self): # function makes it easier to read odometer
        """Shows car mileage"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

my_new_car = Car("Audi", "A4", 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car = Car("Land Rover", "Defender", 1969)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()