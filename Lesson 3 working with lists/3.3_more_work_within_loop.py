# a message can be automated for each magician

magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician.title() + ", that was a great trick!")  # a message is composed for each person in the list

print("")  # new line

# as many lines are you want can be written in the for loop
# every line following the line "for magician in magicians" is considered inside the loop
# when in the loop each indent line is executed once for each value in the list

for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
    # both print statements have been indented each line will be executed for every magician in the list
    # \n creates a new line in the second print statement creating a new line after each pass through
    # this way each message is neatly grouped
