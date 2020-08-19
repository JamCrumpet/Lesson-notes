# you can store multiple classes in a single module although each class in a module should be related somehow
# the classes Battery and ElectricCar both help represent cars, so both are added to car.py

# we can now make a new class from the imported ElectricCar class

from car import ElectricCar

my_tesla = ElectricCar("tesla", "model s", 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

