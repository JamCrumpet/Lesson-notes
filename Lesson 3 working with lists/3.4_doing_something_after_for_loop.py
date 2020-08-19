# after a for loop a summary massage of the block may be left afterwards

magicians = ["alice", "david", "carolina"]

for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

# any lines after the for loop are not executed without repetition
print("Thank you, everyone. That was a great magic show!") # This is not part of the loop
# so it is not repeated after each pass through
