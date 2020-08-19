# python doe not require an else block at the end of an if-elif chain
# sometimes an else block is useful
# or sometime times it is clearer to use an additional elif statement that catches a specific condition of interest

age = 24

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65: # the elif block now check to make sure a person is less than 65 before assigning a price of 10
    price = 10
elif age >= 65: #
    price = 6

print("Your admission cost is $" + str(price)+ ".")