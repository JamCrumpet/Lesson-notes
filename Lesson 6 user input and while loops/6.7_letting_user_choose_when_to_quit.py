# we can make a program that repeats inputted text until the user wants to stop using a while loop
# this can be done by defining a quit value that keeps the code running until the user has inputted the value quit


prompt = "\nTell me something, and I will repeat it back to you:" # define prompt that tells the user two options ...
prompt += "\nEnter 'quit' to end the program." # ... the option to input a message or quit

message = "" # variable is created to store user input, python compares the message in the while loop to "quit"
while message != "quit": # python runs the loop as long of the value of message is not quit
    message = input(prompt)

    if message != "quit": # if statement will check value of message, if user inputs quit we set active quit
        print(message)
    else: # if user prints anything other than quit, this prints message
        print(message)