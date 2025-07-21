import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Environmental Data Dashboard 🌱")

merged = pd.read_csv("output/merged_pm25_temp.csv", parse_dates=["Month"])
clusters = pd.read_csv("output/city_clusters.csv")

st.subheader("PM2.5 vs Global Temp")
fig1, ax1 = plt.subplots(figsize=(10,4))
sns.lineplot(data=merged, x="Month", y="PM2.5", ax=ax1, label="PM2.5")
sns.lineplot(data=merged, x="Month", y="GlobalTemp", ax=ax1, label="Temp")
st.pyplot(fig1)

st.subheader("City Clusters")
fig2, ax2 = plt.subplots()
sns.scatterplot(data=clusters, x="PM2.5", y="NO2", hue="Cluster", ax=ax2)
st.pyplot(fig2)

st.subheader("PM2.5 Forecast")
st.image("output/pm25_forecast.png")

st.subheader("Delhi AQI Map")
with open("output/delhi_station_pollution_map.html", 'r') as f:
    st.components.v1.html(f.read(), height=500)
