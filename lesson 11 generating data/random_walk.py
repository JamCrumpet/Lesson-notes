from random import choice

class RandomWalk():
    """A Class to generate random walks"""

    def __init__(self, num_points = 5000): # sets number of points walked
        self.num_points = num_points

        # All walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calcualte all the points in the walk"""

        # keep taking steps until the walk reaches the desired length
        while len(self.x_values) < self.num_points: # loop that runs until the walk is filled with the correct num of points

            x_direction = choice([1,-1]) # 1 for right movement or -1 for left movement
            x_distance = choice([0,1,2,3,4]) # how far to move in that direction
            x_step = x_direction * x_distance # length and direction of each step combined

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Rejects moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # calculate the next x and y values
            next_x = self.x_values[-1] + x_step # get new value we add value in x_step to last value of x_value
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)