# to make a list if numbers, insead of a column, you would convert the results of range()
# this is done using list()

numbers = list(range(1,6))
print(numbers)

# we can use range() to tell python to skip numbers
# here is the code used to list the even numbers from 1 to 10
even_numbers = list(range(2,11,2))
print(even_numbers)
# in this code range() starts with the number 2 and then adds 2 to the value until it counts to 11
odd_numbers = list(range(1,10,2))
print(odd_numbers)
# in this code range() starts with the number 1 and then adds 2 to the value until it reaches 10
test = list(range(1,30,4))
print(test)
# in this code range(starts with the number 1 and then adds 4 until it reaches 30

# in this example we make a list of the first 10 square numbers
# in python two asterisks (**) represent exponents

squares = [] # we start with an empty list named square
for value in range(1,11): # python loops through each value from 1 to 10. inside the loop the current value is raised
    # to the second power and stored in the variable square
    square = value**2 # this is where the current value is stored
    squares.append(square) # append adds an item to the end of a list. all the values from square to squares
print(squares)

a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)