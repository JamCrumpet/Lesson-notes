class Restaurant():
    """ About restaurants or whatever"""

    def __init__(self, restaurant_name, restaurant_type):
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type
        self.number_served = 0


    def open_restaurant(self):
        print(self.restaurant_name + " which serves " +
              self.restaurant_type + " is open for business.")

    def set_number_served(self):
        print("This restaurant has served " + str(self.number_served) + " customers.\n")