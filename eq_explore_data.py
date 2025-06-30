from pathlib import Path
import json

# Read data as a string and convert to a python object.
path = Path(__file__).parent / "eq_data" / "eq_data.geojson"
contents = path.read_text(encoding="utf-8")
data = json.loads(contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = data["features"]

# Print the number of earthquakes in the dataset.
print(f"Number of earthquakes: {len(all_eq_dicts)}")

# Extract the magintudes
mags, lons, lats = [],[], []
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    lon = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])  # Print the first 10 magnitudes.
print(lons[:10])  # Print the first 10 longitudes.
print(lats[:10])   # Print the first 10 latitudes.

# Create a more readable version of the data.
path = Path(__file__).parent / "eq_data" / "eq_explore_data.geojson"
readable_contents = json.dumps(data, indent=4)
path.write_text(readable_contents, encoding="utf-8")