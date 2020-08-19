# when writing a function you can define a default value
# if an argument for a parameter is provided in the functional call python uses the argument value

def describe_pet( pet_name, animal_type = "dog"):
    """Display information about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name= "wes")
describe_pet(animal_type= "turtle", pet_name= "terry the turtle") # in order to change animal_type it first must ...
# ... be defined