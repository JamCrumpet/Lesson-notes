# here we will plot a single point based on certain characteristics

# to plot a single point use the scatter() function and pass the single (x,y) values of the point of interest
# here is an example of how to do so

import matplotlib.pyplot as plt

# plt.scatter(2,4)
# plt.show()

# here we will style the output

plt.scatter(2,4, s=200) # call scatter() and s argument and use the argument to set size of dots used to draw the graph

# set title and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize =14)
plt.ylabel("Square of Value", fontsize=14)

# set size of tick labels
plt.tick_params(axis="both", which = "major", labelsize=14)
plt.show()