import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    
    # Make a random walk.
    rw = RandomWalk(50_000)
    rw.fill_walk()
    
    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9), dpi=100) # Set the figure size and resolution.
    point_numbers =  range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap = 'Blues', edgecolors='none' , s=1)
    ax.set_aspect('equal')
    
    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100, label='Start')
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    
    # Removes the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    plt.show()
    
    keep_running = input("Make another walk? (y/n): ")
    if keep_running.lower() != 'y':
        break