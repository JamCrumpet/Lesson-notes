# plot the first five cubic numbers and the first 5000 numbers
print("\t\t\t- Cubes -")

import matplotlib.pyplot as plt

x_values = list(range(1,6))
y_values = [x**3 for x in x_values]

plt.scatter(x_values,y_values,s=40)

# set title and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize =14)
plt.ylabel("Square of Value", fontsize=14)

# set size of tick labels
plt.tick_params(axis="both", which = "major", labelsize=14)

# set the range for each axis
plt.axis([0,5.5,0,135])

plt.show()

# same thing for for 5000 instead of 5

x_values = list(range(1,5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values,y_values,s=40)

# set title and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize =14)
plt.ylabel("Square of Value", fontsize=14)

# set size of tick labels
plt.tick_params(axis="both", which = "major", labelsize=14)

plt.axis([0, 5100, 0, 5100**3])

plt.show()