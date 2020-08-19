# you can also import an entire module
# you access a module from a class you use the dot notation

import car

my_tesla = car.ElectricCar("tesla", "model s", 2016) # dot notation used a access ElectricCar
print(my_tesla.get_descriptive_name())

my_new_car = car.Car("Audi", "A4", 2016)
print(my_new_car.get_descriptive_name())

my_new_car = car.Car("Land Rover", "Defender", 1969)
print(my_new_car.get_descriptive_name())
