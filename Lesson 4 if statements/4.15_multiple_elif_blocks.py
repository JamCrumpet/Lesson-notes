# you can use as many elif blocks are you like

age = 44

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65: # the elif block now check to make sure a person is less than 65 before assigning a price of 10
    price = 10
else: #
    price = 6

print("Your admission cost is £" + str(price) + ".")
