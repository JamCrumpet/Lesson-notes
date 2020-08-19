# here we will create the random walk graph, a graph representing if every step you took was in a random direction

# to generate the graph first we need to generate the RandomWalk class which will make the decisions ...
# ... about which directions the walk will take
# the class will have three attributes: one to store the number of points in the walk and ...
# ... two to list the x and y cooridinates of each point the in the walk
# RandomWalk will use two methods: init and fill_walk which will calculate the points in the walk

from random import choice # to store possible choices in a list and use choice() to decide which choice to use

class RandomWalk():
    """A Class to generate random walks"""

    def __init__(self, num_points = 5000):
        self.num_points = num_points

        # All walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]