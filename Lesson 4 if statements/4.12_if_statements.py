# the simplest kind of if statement has one test and one action

#if conditional_test
#  do something

# you can put any conditional test in the first line and just about any action in the indented block following the test
# if the action is True python executes the code following the if statement
# if the test evaluates to False, python ignores the code following the statement

# lets say we have a variable representing someones age and we want to know if the person is old enough to vote

age = 19
if age >= 18: # python checks whether the value is equal or greater than 18
    print("You are old enough to vote!") # if True the following message is printed
    # you can have as many lines of code as necessary
    print("Have you registered to vote yet?")

# if the vlaue is less than 18 it comes up as false and would produce no output