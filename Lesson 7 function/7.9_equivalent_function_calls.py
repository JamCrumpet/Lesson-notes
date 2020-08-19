# because of positional arguments, keyword arguments and default values can all be used together
# consider the following definitions for describe pets with one default value provided

# def describe_pet( pet_name, animal_type = "dog"):
# with this defnition an arguement always need to be provided for pet_name ...
# ... this value can be provided using the positional or keyword format
# if the animal described is not a dog an argument for animal_type must be included in the cell ...
# ... and this argument can also be specified using the positional or keyword format.

def describe_pet( pet_name, animal_type = "dog"):
    """Display information about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


# a dog named willie
describe_pet('willie')
describe_pet(pet_name = 'willie')

# a hamster named harry
describe_pet('harry', 'hamster')
describe_pet(pet_name = 'harry', animal_type = 'hamster')
describe_pet(animal_type = 'hamster', pet_name = 'harry')

# each of these functions calls would have the same output as the previous examples
