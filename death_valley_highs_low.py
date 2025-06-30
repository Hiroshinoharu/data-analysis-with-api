from pathlib import Path
import csv
from datetime import datetime
from matplotlib import pyplot as plt

path = Path(__file__).parent / "data" / "death_valley_2021_simple.csv"
lines = path.read_text(encoding="utf-8").splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Print the header row.
for index, column_header in enumerate(header_row):
    print(index, column_header)

# Extract high, low temperatures and dates from the file.
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    try:
        high = int(row[3])
        low = int(row[4])
    except (ValueError, IndexError):
        print(f"Skipping row due to invalid data: {row}")
        continue
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots(figsize=(15, 9), dpi=100)  # Set the figure size and resolution.
ax.plot(dates, highs, c='red', alpha=0.5)  # Plot the high temperatures with a red line.
ax.plot(dates, lows, c='blue', alpha=0.5)  # Plot the low temperatures with a blue line.

# Set chart title and label axes.
ax.set_title("Daily high and low temperatures, 2021", fontsize=24)
ax.set_xlabel("Date", fontsize=14)
fig.autofmt_xdate()  # Automatically format the x-axis dates.
ax.set_ylabel("Temperature (F)", fontsize=14)

plt.show()