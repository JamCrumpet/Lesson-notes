# a tuple looks just like a list except you use parentheses instead of square brackets
# once you define a tuple you can access individual elements by each items index, just like you would for a list
# for example if we have a rectangle that should always be a certain size, we can ensure that the size doesn't ...
# ...  change by putting the dimensions into a tuple

dimensions = (200,50) # we define a tuple by using parentheses instead of square brackets
print(dimensions[0])
print(dimensions[1])

# dimensions[0]=250 # here we try to change the index[0] to 250
# Traceback (most recent call last):
#   File "C:/Users/f-dal/PycharmProjects/lesson_3_working_with_lists/3.16_defining_a_tuple.py", line 10, in <module>
#     dimensions[0]=250
# TypeError: 'tuple' object does not support item assignment

# trying to change the value of the first dimension causes an error because qw are trying to alter a tuple