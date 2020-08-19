# often you'll want to take one action when a conditional test passes and different one action in all other cases
# an if-else allows you to define an action or set of actions that are executed when the conditional test fails

# here is the same code from 4.12 but will a message for anyone who is not old enough to vote

age = 17
if age >= 18: # if the conditional test passes the indented print statement below is executed
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else: # if the test evaluates False the else block is executed
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")