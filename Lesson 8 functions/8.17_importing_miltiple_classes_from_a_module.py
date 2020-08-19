#you can import as many classes as you need into a program file if we want o make a regular car and electric car ...
# ... we need to import both classes

from car import Car, ElectricCar # you import multiple cars from a class by separating each class with a comma

my_tesla = ElectricCar("tesla", "model s", 2016)
print(my_tesla.get_descriptive_name())

my_new_car = Car("Audi", "A4", 2016)
print(my_new_car.get_descriptive_name())

my_new_car = Car("Land Rover", "Defender", 1969)
print(my_new_car.get_descriptive_name())

