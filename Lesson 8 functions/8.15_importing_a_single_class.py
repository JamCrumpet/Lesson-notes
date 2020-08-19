from car import Car

my_new_car = Car("Audi", "A4", 2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(21) # call update_odometer() and give it value of 23
my_new_car.read_odometer()

my_new_car = Car("Land Rover", "Defender", 1969)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(3403)
my_new_car.read_odometer()