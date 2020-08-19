# often you'll need to test more than two possible situations, this can be done using if-elif-else chain

# python executes only one block in an if-elif-else chain
# it runs each test in order until one passes
# when a test passes, the code following that test is executed and python skips the rest of the tests

# an example of this, consider an amusement park that charges different rates for different age groups
# admission for anyone under 4 is free
# admission for anyone between the ages 4 and 18 is £5
# admission for anyone age 18 or older is £10

age = 12

if age <4: # the if tests whether is a person is under 4 years, if True it prints the message, if False print is skipped
    print("Your admission cost £0")
elif age <18: # the elif is another if test
    print("Your admission cost £5")
else:
    print("Your admission cost £10")

# it would work better to test a price within an if-elif-else chain and have a simple print statement

age_2 = 19

if age_2 <4:
    price = 0
elif age_2 <18:
    price = 5
else:
    price = 10 # one the if statement is True it sets the price

print("Your admission cost is £" + str(price) + ".")