from random import choice

class RandomWalk:
    """A class to simulate a random walk."""
    
    def __init__(self, num_points=5000) -> None:
        """Initialize attributes of a random walk."""
        self.num_points = num_points
        
        # All random walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]
        
    def fill_walk(self):
        """Calculate all points in the walk."""
        
        # Keep taking steps until the walk reaches the desired number of points.
        while len(self.x_values) < self.num_points:
            
            # Decide which direction to go and how far to go in that direction.
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance
            
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance
            
            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue
            
            # Calculate the new position.
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            
            # Append the new position to the lists of x and y values.
            self.x_values.append(next_x)
            self.y_values.append(next_y)