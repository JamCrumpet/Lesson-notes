# in previous examples we had programs the performed certain tasks while a given condition is true
#  but there could be more complicated programs in which many different events could cause the program to stop running
# e.g. in a game, when a player runs out of ships, their time runs our, or the city they were supposed ...
# ... to protect gets destroyed, the game should end

# if many of these events were to occur trying to test all these conditions in one while statement becomes difficult
# you can define one variable that determines whether or not the entire program is active
# this variable is called a flag and acts as a signal to the program

# we can write our program so that they run while the flag is set to true and stop running when amy of ...
# ... several programs are set to false
# as a result, our while statement needs to check one one condition, whether or not the flag is true
# that way all other tests , to see if an event to see if the flag is false, can be organised into one program

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."