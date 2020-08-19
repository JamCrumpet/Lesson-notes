# writing out lists by hand can be inefficient
# here we will have python do the calculations for us

import matplotlib.pyplot as plt

x_values = list(range(1,1001)) # list containing numbers 1 through 1000
y_values = [x**2 for x in x_values] # generates y-values by looping through x_values squaring each number

plt.scatter(x_values, y_values, s=40) # x and y values passed through scatter

# set title and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize =14)
plt.ylabel("Square of Value", fontsize=14)

# set size of tick labels
plt.tick_params(axis="both", which = "major", labelsize=14)

# set the range for each axis
plt.axis([0,1100,0,1100000]) # use axis to specify the range of each axis

plt.show()