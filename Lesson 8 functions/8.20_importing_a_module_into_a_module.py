# sometimes you'll want o spread out your classes over several classes over several modules to keep any one ...
# .. file from growing to large and to avoid storing unrelated classes in the same module

# when you store you classes in several modules you may find that a class in one module depends on a class in ...
# ... another module

from car2 import Car

class Battery():
    """Simple model for battery for electric car"""

    def __init__(self, battery_size = 70):
        """Initialise battery attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print statement describe battery size"""
        print("This car has a " + str(self.battery_size) + "kWh Battery")

    def get_range(self):
        """Print statement about range battery provides"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

class ElectricCar(Car):
    """Represents aspects of a car, specifgic to eletric vehicles"""

    def __init__(self,make,model,year):
        """Initialise attributes of parent class"""
        super().__init__(make,model,year)
        self.battery = Battery()

# the class ElectricCar needs access to its parent class Car so Car is imported from car2

my_tesla = ElectricCar("tesla", "model s", 2016) # dot notation used a access ElectricCar
print(my_tesla.get_descriptive_name())

my_new_car = Car("Audi", "A4", 2016)
print(my_new_car.get_descriptive_name())

my_new_car = Car("Land Rover", "Defender", 1969)
print(my_new_car.get_descriptive_name())