# break statement can be used to exit a while loop immediately without running remaining code in the loop ...
# ... regardless of any conditional test

# the break statement statement directs the flow of a program and can be used to control which lines are ...
# ... executed and which aren't os the program only executes the code that you want, when you want it

# for example consider we have a piece of code which repeats an input
# we cab stop the while loop in the program by calling break as soon the user enters the quit value

prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.)"

while True: # while true the loop will run forever until it reaches the break statement
    city = input(prompt)

    if city == "quit":
        break
    else:
        print("I'd love to go to " + city.title() + "!")