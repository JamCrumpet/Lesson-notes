# a colourmap is a series of colours in a gradient that moves from starting to ending colour
# coloursmaps are used in visualisation to emphasise a pattern in data
# e.g. you may want to make low values alight and high colours darker
# pyplot has built in clourmaps

import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor ="none", s=40)

# set title and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize =14)
plt.ylabel("Square of Value", fontsize=14)

# set size of tick labels
plt.tick_params(axis="both", which = "major", labelsize=14)

# set the range for each axis
plt.axis([0,1100,0,1100000]) # use axis to specify the range of each axis

plt.show()