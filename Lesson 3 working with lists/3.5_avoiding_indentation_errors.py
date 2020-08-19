# 3.5.1 forgetting to indent/tab
# always tab/indent a for loop to show that line belongs to the line above it
magicians = ["alice", "david", "carolina"]

# for magician in magicians
# print(magician) this will cause an error as there is no tab/indent to show belonging to a for loop

# 3.5.2 forgetting to indent additional lines
# forgetting to indent/tab additional lines can cause the code to run without errors but not as expected
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
print("I can't wait to see your next trick, " + magician.title() + ".\n")

# "I can wait..." was supposed to show after each persons line
# This didn't happen as as there was no tab/indent to show that this line belonged to the for a loop
