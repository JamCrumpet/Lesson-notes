import pygal
from die import Die

die = Die()

# make some rolls and store results in a list
results = []
for roll_num in range(1000): # increase number of simulated rolls to 1000
    ans = die.roll()
    results.append(ans)

# analyse the results
frequencies = []
for value in range(1,die.num_sides+1): # loop through possible values
    frequency = results.count(value) # count how many times each value appears
    frequencies.append(frequency) # append values to frequencies

# Visualise the results
hist = pygal.Bar() # create instance of pygal.Bar() abd store in hist # .bar() represents bar graph

hist.title = "Results of rolling one D6 n times"
hist.x_labels = ["1","2","3","4","5","6"]
hist.x_title = "Results"
hist.y_labels = "Frequency of Results"

hist.add("D6", frequencies) # add series of values to chart
hist.render_to_file("die_visual.svg")
