# think of a class as a set of instructions for how to make an instance
# the class Dog is a set of instructions that tells python how to make individual instance representing specific dogs

# here is an example an instance representing a specific dog


class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """Initialise name and age attributes"""
        self.name = name
        self.age = age


    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(self.name.title() + " rolled over!")

my_dog = Dog("willie", 6)

print("My dog's name is " + my_dog.name.title() + ".") #[1]
print("My dog is " + str(my_dog.age) + " years old.")

# [1] to access the value my dog you use the following notation
my_dog.name

# new exercise
# 8.X calling methods
# after creating an instance from the class dog we can use dot notation to call any other defined in dog
# here is the notation to sit and roll over

my_dog.sit()
my_dog.roll_over()