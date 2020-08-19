# you don't have to start from scratch when writing a class. If the class your writing is a specialised version ...
# ... of another class you're writing you can use inheritance. when one class inherits from another it ...
# ... automatically takes on all the attributes and methods from the first class. the original class is ...
# ... called the parent class the the new class is call the child class
# the child class can use every attribute and free to define new attributes


# the first task python has when creating an instance from a child class is to assign value to ...
# ... all attributes in the parent class
# to do this the init method for a class class needs help from its parent class
# as an example lets model an electric car. an electric car is a specific type of car so we can base ...
# ... the new ElectricCar class on the Car class

# first we started with the copied class Car. the parent class must appear before the child class
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

class ElectricCar(Car): # define child class, parent class must be included in parentheses
    """Represents aspects of a car, specifgic to eletric vehicles"""

    def __init__(self,make,model,year): # init takes info required to make a Car instance
        """Initialise attributes of the parent class."""
        super().__init__(make,model,year) # # super() is a function that help make connection between parent and ...
        # ... child class, the following line tells python to call the init method from parent class which ...
        # ... gives ElectricCar instance all attributes from its parent class

my_tesla = ElectricCar("Tesla", "model s", 2016) # instance mades of ElectricCar class and store it in my_tesla
# above line class init() defined in ElectricCar which calls init() from Car
print(my_tesla.get_descriptive_name())

