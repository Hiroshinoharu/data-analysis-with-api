from die import Die

import plotly.express as px

# Create a D6 die.
die_1 = Die()
die_2 = Die(10)  # Create a D10 die.

# Make some rolls, and store results in a list.
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()  # Sum the results of two dice.
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides  # Maximum result is the sum of the sides of both dice.
poss_results = range(2, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
fig = px.bar(x=poss_results, y=frequencies, labels={'x': 'Result', 'y': 'Frequency'}, title='Results of rolling one D6 and one D10 50,000 times.')

# More customization.
fig.update_layout(xaxis_dtick=1) # Set x-axis ticks to show every integer.

fig.show()

fig.write_html("dice_visual_d6d10.html")  # Save the figure as a HTML file.