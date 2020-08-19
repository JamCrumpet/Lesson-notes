# object oriented programming is one of the most effective approaches to writing software
# object oriented programming involves classes the represent real world things and situation and you ...
# ... create objects based on these classes
# when you write a class you define the general behavior that whole category of objects can have

# when you create individual objects from that class each object is automatically equipped with the general behavior
# making a object from a class is called instantiation and you work with instances of a class

# you can model almost anything using a class
# the following class is called dog and represents the name and age of a dog and that the dog can sit and roll over

class Dog: # defined a class name dog, convention states we capitalise names in functions
    """A simple attempt to model a dog""" # docstring describing class

    # the function part of a class is called a method. everything learnt about functions apply to methods as well

    def __init__(self, name, age): # three parameters, self required as every class must pass self argument
        """Initialise name and age attributes"""
        self.name = name # name.self=name takes value stored in parameter name and stores it in variable name
        self.age = age


    def sit(self): # contains method sit and roll over, doesn't need any other info so one parameter is needed, self
        """Simulate a dog sitting in response to a command"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(self.name.title() + " rolled over!")