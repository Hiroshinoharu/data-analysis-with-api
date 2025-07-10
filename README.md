# 📊 Data Analysis with APIs & Visualizations

A hands-on project combining **data analysis**, **API integration**, and **data visualization** using Python. This repo includes a series of mini-projects ranging from earthquake mapping and temperature analysis to die simulations and random walks.

---

## 🎯 Project Goals

- Practice fetching real-world data from APIs
- Explore and visualize datasets using Python libraries
- Gain hands-on experience with matplotlib, JSON handling, and custom classes
- Build a modular and extensible codebase for learning and experimentation

---

## 📁 Project Structure

```
data-analysis-with-api/
├── apiRequests/                 # Scripts for working with web APIs (e.g. GitHub, USGS)
├── die.py                       # Simulates rolling a die
├── die_visual.py               # Visualizes die rolls
├── dice_visual_d6d10.html      # HTML output of D6 vs D10 simulation
├── random_walk.py              # RandomWalk class for 2D visualizations
├── rw_visuals.py               # Plots random walk paths
├── mpl_squares.py              # Simple matplotlib square visual
├── scatter_squares.py          # Scatter plot for squares
├── eq_explore_data.py          # Earthquake API data exploration
├── eq_world_map.py             # Visualizes earthquakes on a world map
├── death_valley_highs_low.py   # Temperature plotting using CSV data
├── stika_highs.py              # Alaska temperature plotting
├── stika_high_lows.py          # Alaska highs/lows plotting
├── README.md                   # Project overview
└── requirements.txt            # Python dependencies (optional)
```

---

## 🧪 Key Projects

### 🌍 Earthquake Data Visualization
- Pulls earthquake data from the USGS API
- Plots magnitude and location using Plotly or matplotlib
- Great for exploring geospatial data

### 🎲 Die Simulation
- Custom `Die` class to simulate multiple rolls
- Plots frequency using matplotlib
- Includes D6 and D10 comparisons in HTML format

### 🌀 Random Walks
- Simulates 2D random movements
- Useful for learning about probabilistic simulations
- Plots using scatter or line charts

### 🌡️ Temperature Analysis
- Reads CSV files of historical weather data
- Plots high/low temperatures over time
- Fixes included to handle date parsing and formatting

---

## 🔧 Setup Instructions

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/data-analysis-with-api.git
   cd data-analysis-with-api
   ```

2. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run any script with:
   ```bash
   python script_name.py
   ```

---

## 📊 Libraries Used

- `requests`
- `matplotlib`
- `plotly`
- `json`, `csv`, `datetime`
- `random`

---

## 📌 Notes

- All scripts are organized for individual testing and exploration.
- Ideal for beginners learning Python through real-world data.
- Can be extended with new datasets, APIs, and visualization tools.

---

## 📜 License

MIT License – use, share, and modify freely!
