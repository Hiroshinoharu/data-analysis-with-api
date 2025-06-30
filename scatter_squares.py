import matplotlib.pyplot as plt

# This program plots a simple scatter plot with a single point.

x_values = range(1, 1001)  # x values from 1 to 1000
y_values = [x**2 for x in x_values]

plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap='Blues', s=10)  # s is the size of the point

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set the size of tick labels.
ax.tick_params(labelsize=14)

# Set the range for the x and y axes.
ax.axis([0,1100,0,1_100_000])

# Set a tick style for the y-axis.
ax.ticklabel_format(style='plain')

# Show the plot.
plt.show()

# Save the plot to a file.
fig.savefig('scatter_squares.png', bbox_inches='tight')