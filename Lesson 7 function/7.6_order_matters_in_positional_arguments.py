def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# mixing up the order can cause unexpected results

describe_pet("wes", "dog")

# I have a wes.
# My wes's name is Dog.

# this is due to the order of arguments being wrong
