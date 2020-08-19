# to import every class from a module you use the following

from car import *
my_tesla = ElectricCar("tesla", "model s", 2016) # dot notation used a access ElectricCar
print(my_tesla.get_descriptive_name())

my_new_car = Car("Audi", "A4", 2016)
print(my_new_car.get_descriptive_name())

my_new_car = Car("Land Rover", "Defender", 1969)
print(my_new_car.get_descriptive_name())

# this method is not recommended because its helpful to read import statements and can lead to confusing names