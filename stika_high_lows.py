from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path(__file__).parent / "data" / "sitka_weather_2021_simple.csv"
lines = path.read_text(encoding="utf-8").splitlines()

reader = csv.reader(lines)
header_row = next(reader)
# Print the header row.
for index, column_header in enumerate(header_row):
    print(index, column_header)

# Extract high temperature and dates from the file.
dates, highs, lows = [], [], []
for row in reader:
    try:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")  # Parse the date.
        high = int(row[4])  # Extract high temperature.
        low = int(row[5])  # Extract low temperature.
    except (ValueError, IndexError):
        print(f"Skipping row due to invalid data: {row}")
        continue
    dates.append(current_date)
    highs.append(high)
    lows.append(low)  # Append low temperature to the list.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots(figsize=(15, 9), dpi=100)  # Set the figure size and resolution.
ax.plot(highs, c='red', alpha=0.5)  # Plot the high temperatures with a red line.
ax.plot(lows, c='blue', alpha=0.5)  # Plot the low temperatures with a blue line.

# Set chart title and label axes.
ax.set_title("Daily high and low temperatures, 2021", fontsize=24)
ax.set_xlabel("Day", fontsize=14)
fig.autofmt_xdate()  # Automatically format the x-axis dates.
ax.set_ylabel("Temperature (F)", fontsize=14)

# Set the size of tick labels.
ax.set_xlabel("Day of the Year", fontsize=14)

plt.show()