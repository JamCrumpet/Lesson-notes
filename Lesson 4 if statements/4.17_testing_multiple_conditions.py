# the if elif chain is useful but only appropriate to use when you need one test to pass
# once it finds the test it stops and skips the rest of the tests
# this is useful because it is efficient and allows you to test for one specific condition

# however sometimes it is important to check all the conditions of interest
# in this case you should use a series of if statements with no elif or else blocks
# this makes sence when one or more conditions could be True

requested_topping =["mushrooms", "extra cheese"] # a list containing requested toppings

if "mushrooms" in requested_topping: # the if statement checks if mushrooms are True or False and ...
    # continues to the next statement and continues despite the outcome
    print("Adding Mushrooms.")
if "pepperoni" in requested_topping: # the if statement is still considered despite the last statement being True
    print("Adding Pepperoni.")
if "extra cheese" in requested_topping:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

# every condition is evaluated both mushrooms and extra cheese is added to the pizza

# the code would not work properly if a if-elif-else were used
# this is because one a statement is Ture in an if-elif-else statement python will stop running the test
