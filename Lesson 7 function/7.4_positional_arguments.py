# when calling a function python will match each argument in the function call with a parameter ...
# ... in the function definition
# the simplest way to do this is bases on the order of the argument provided
# values match up this way are called positional argument

# for example consider a function that displays info about pets
# the function tell use what kind of animal each pet is the the pets name

def describe_pet(animal_type, pet_name):  # two types of argument the pet name and type
    """Display information about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet("Dog", "Wes")