import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Clustering
df = pd.read_csv("data/air-quality-data-in-india/city_day.csv")
df = df.dropna(subset=["PM2.5", "NO2", "CO", "SO2", "O3"])
avg = df.groupby("City")[["PM2.5", "NO2", "CO", "SO2", "O3"]].mean()
scaled = StandardScaler().fit_transform(avg)
avg["Cluster"] = KMeans(n_clusters=4, random_state=42, n_init='auto').fit_predict(scaled)
avg.to_csv("output/city_clusters.csv")
sns.scatterplot(data=avg, x="PM2.5", y="NO2", hue="Cluster")
plt.savefig("output/city_cluster_plot.png")
plt.close()

# Anomaly Detection
df2 = pd.read_csv("data/air-quality-data-in-india/station_day.csv", parse_dates=["Date"])
df2 = df2.dropna(subset=["PM2.5", "NO2", "CO", "SO2", "O3"])
recent = df2[df2["Date"] > "2019-01-01"]
features = recent[["PM2.5", "NO2", "CO", "SO2", "O3"]]
recent["anomaly"] = IsolationForest(contamination=0.02).fit_predict(features)
recent.to_csv("output/station_anomalies.csv", index=False)
sns.scatterplot(x=recent["Date"], y=recent["PM2.5"], hue=recent["anomaly"])
plt.savefig("output/station_pm25_anomalies.png")
plt.close()
