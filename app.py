import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("Building Temperature Visualization")

# Instructions
st.write("""
This app visualizes temperature readings in a building over a 24-hour period, 
with two conditions: Air Conditioning (AC) and Fan.
""")

# Load the dataset from GitHub
url = "https://raw.githubusercontent.com/<your-username>/<your-repo>/main/building_temperature_readings.csv"
try:
    data = pd.read_csv(url, parse_dates=["Timestamp"])
    st.success("Dataset loaded successfully.")
except Exception as e:
    st.error(f"Failed to load dataset: {e}")
    st.stop()

# Display the dataset
st.write("### Dataset Preview")
st.dataframe(data)

# Visualization: Line chart for temperature readings
st.write("### Temperature Over Time")
fig, ax = plt.subplots(figsize=(10, 6))
for condition in data["Condition"].unique():
    subset = data[data["Condition"] == condition]
    ax.plot(subset["Timestamp"], subset["Temperature (°C)"], label=condition)

ax.set_title("Temperature Readings Over 24 Hours")
ax.set_xlabel("Time")
ax.set_ylabel("Temperature (°C)")
ax.legend()
ax.grid(True)
st.pyplot(fig)

# Additional insights
st.write("### Insights")
avg_temp = data.groupby("Condition")["Temperature (°C)"].mean()
st.write("#### Average Temperatures by Condition:")
for condition, avg in avg_temp.items():
    st.write(f"- **{condition}**: {avg:.2f} °C")
