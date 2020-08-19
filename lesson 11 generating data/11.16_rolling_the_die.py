# here we will roll the D6

from die import Die

# create D6
die = Die()

# make some rolls and store results in a list
results = []
for roll_num in range(10000): # increase number of simulated rolls to 1000
    ans = die.roll()
    results.append(ans)

# analyse the results
frequencies = []
for value in range(1,die.num_sides+1): # loop through possible values
    frequency = results.count(value) # count how many times each value appears
    frequencies.append(frequency) # append values to frequencies


print("Dice rolls:")
print(results)
print("\nDice roll frequencies:")
print(frequencies)