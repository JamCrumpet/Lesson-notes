# once you have a child class inhert from the parent class you can add new attributes

# in this example we will had battery life to the child class of Cars, ElectricCar

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

class ElectricCar(Car):
    """Represents aspects of a car, specifgic to eletric vehicles"""

    def __init__(self,make,model,year):
        """
        Initalised attributes of parent class.
        Then initialised attributes specific to eclectic car
         """
        super().__init__(make,model,year)
        self.battery_size = 70 # new attribute is added, value is accociated with instances ElectricCar

    def describe_battery(self):
        """Statement describing battery size"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.") # prints related info

my_tesla = ElectricCar("Tesla", "model s", 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
