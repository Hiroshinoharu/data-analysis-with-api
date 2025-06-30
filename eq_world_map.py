import json

import plotly.express as px

# Read data as a string and convert to a python object.
with open('eq_data/eq_data.geojson', encoding='utf-8') as f:
    data = json.load(f)

# Extract the magnitudes, longitudes, and latitudes.
mags, lons, lats = [], [], []
for feature in data['features']:
    mag = feature['properties']['mag']
    lon = feature['geometry']['coordinates'][0]
    lat = feature['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

# Create a scatter plot of the earthquake data.
fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    size=mags,
    projection='natural earth',
    title='Global Earthquakes',
    labels={'lat': 'Latitude', 'lon': 'Longitude', 'size': 'Magnitude'},
    hover_name=[f"Mag: {mag}" for mag in mags],
)

# Save the figure as a PNG file.
fig.write_image("eq_data/eq_data.png")

# Show the figure.
fig.show()