# when using the inout function python interprets the user inout as a string
# consider the following in a python interpreter , where we ask for the users age

# >>> age = input("How old are you? ")
# >>> How old are you? 21
# age
# >>> 21

# when we age for the value age it returns '21' which is the string representation of the numerial value
# we know this is represented as a string since it enclosed in quotes


# >>> age = input("How old are you? ")
# How old are you? 21
# >>> age >= 18 # when using a numerical comparison python produces an error because it cannot compair a string ...
# ... to an interger
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# TypeError: '>=' not supported between instances of 'str' and 'int'# string "21" cannot be compaired to value 18

# this is resolved by using the int() function

# >>> age = input("How old are you? ")
# How old are you? 21 # we enter 21 into hte prompt and python interprets the number as a string
# >>> age = int(age) # value is then converted to a numerical representation by int() and python can ...
# ... run conditional tests
# >>> age >=18
# True

# to use int() in an actual program:

height = input("How tall are you? ")
height = int(height)

if height >= 36:
    print("\nYou are tall enough to ride!")
else:
    print("\n You'll be abke ti rude when you're a little older.")

# the program can compare height to 36 becuase height has been converted to an interget using int()