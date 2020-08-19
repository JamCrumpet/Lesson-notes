import matplotlib.pyplot as plt
from random_walk import RandomWalk

# make a random walk and plot RandomWalk points

while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    # increase intensity of colour as plot progresses
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
        edgecolors="none", s=15)
    plt.show()

    # emphasise the first and last point
    plt.scatter(0,0, c="green", edgecolors="none", s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break
