import matplotlib.pyplot as plt

# This program plots a simple line graph of square numbers.
input_values = [1, 2, 3, 4, 5]

# This is a simple example of using matplotlib to plot a list of squares.
squares = [1,4,9,16,25]

# Applying a style to the plot.
plt.style.use('fivethirtyeight')

# Create a figure and an axes.
fig, ax = plt.subplots()

# Plot the squares on the axes.
ax.plot(input_values,squares, linewidth = 3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize = 14)

# Set the size of tick labels.
ax.tick_params(labelsize=14)

# Show the plot.
plt.show()