# a keyword argument is a name value pair that you pass to a function
# you directly associate the name and the value within the argument
# e.g so when you pass the argument to the function there is no confusion like the harry the hamster example
# keyword arguments free you from having to worry about correctly ordering the arguments

def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type= "turtle", pet_name= "terry the turtle")

# from this previously used piece of code we name each parameter the argument should be matched with