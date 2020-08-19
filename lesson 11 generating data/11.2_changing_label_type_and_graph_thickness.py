# here is how to change the label type and graph thickness

import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
# set linewidth
plt.plot(squares, linewidth = 5)

# set title and label axes
plt.title("Square Numbers", fontsize=24) # .title() to gives a title
plt.xlabel("Value", fontsize =14) # .xlabel() gives title for x axis
plt.ylabel("Square of Value", fontsize=14) # /ylabel() gives title for y axis

# set size of tick labels
plt.tick_params(axis="both", labelsize=14) # .tick_params() styles the tick marks, effect tick marks
# on both tick marks on x and y axis
plt.show()

