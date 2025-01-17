import streamlit as st
import pandas as pd
import altair as alt

# Title and description
st.title("Building Temperature Visualization")
st.write("This app visualizes temperature readings in a building based on two air conditions: 'AC' and 'Fan'.")

# Load the dataset from GitHub
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/<your-github-username>/<your-repository>/main/building_temperature_readings.csv"
    return pd.read_csv(url)

# Load data
try:
    data = load_data()
    data['Timestamp'] = pd.to_datetime(data['Timestamp'])
except Exception as e:
    st.error("Error loading the data. Please ensure the file path is correct.")
    st.stop()

# Sidebar filters
st.sidebar.header("Filters")
condition_filter = st.sidebar.multiselect(
    "Select Air Condition:",
    options=data['Condition'].unique(),
    default=data['Condition'].unique()
)

# Filter data
filtered_data = data[data['Condition'].isin(condition_filter)]

# Display filtered data
st.subheader("Filtered Data")
st.dataframe(filtered_data)

# Visualization
st.subheader("Temperature Over Time")
chart = alt.Chart(filtered_data).mark_line().encode(
    x=alt.X("Timestamp:T", title="Time"),
    y=alt.Y("Temperature (°C):Q", title="Temperature (°C)"),
    color=alt.Color("Condition:N", legend=alt.Legend(title="Air Condition"))
).properties(
    width=800,
    height=400
)
st.altair_chart(chart, use_container_width=True)

# Additional Statistics
st.subheader("Summary Statistics")
st.write(filtered_data.groupby('Condition')['Temperature (°C)'].describe())

st.write("\n**GitHub Repository:** [Your Repository](https://github.com/<your-github-username>/<your-repository>)")
