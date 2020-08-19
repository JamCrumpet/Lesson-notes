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