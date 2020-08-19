# the modulo operator is used for working with numerical information which divides on number by antother ...
# ... and returns the remainder

# >>> 4 % 3
# 1
# >>> 5 % 3
# 2
# >>> 6 % 3
# 0
# >>> 7 % 3
# 1

# modulo operator doesnt tell you how many time one number fits into another, just what the remainder is
# when the number is divisible by another the remainder is 0
# this can be used to determine whether a number is odd or even

number = input("Enter a number, and i'll tell you if its odd or even: ")
number = int(number)

if number % 2 == 0: # even number are divisible by two the modoulo of a even number is always 0
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")
