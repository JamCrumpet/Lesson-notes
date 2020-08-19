def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# you can call the function as many times as needed
# describing a second different pet requires one more call to describe_pet()

describe_pet("Dog", "Wes")
describe_pet("Turtle", "Terry The Turtle")
