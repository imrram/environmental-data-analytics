import pandas as pd
import folium
from geopy.geocoders import Nominatim
import time

stations = pd.read_csv("data/air-quality-data-in-india/stations.csv")
daily = pd.read_csv("data/air-quality-data-in-india/station_day.csv")
delhi_stations = stations[stations["City"].str.lower() == "delhi"]
delhi_data = daily[daily["StationId"].isin(delhi_stations["StationId"])]

latest = delhi_data.sort_values("Date").groupby("StationId").last().reset_index()
merged = pd.merge(latest, delhi_stations, on="StationId")

geolocator = Nominatim(user_agent="geoapi")
coords = []

for name in merged["StationName"]:
    try:
        loc = geolocator.geocode(name + ", Delhi")
        coords.append((loc.latitude, loc.longitude) if loc else (None, None))
    except:
        coords.append((None, None))
    time.sleep(1)

merged["lat"] = [c[0] for c in coords]
merged["lon"] = [c[1] for c in coords]
merged = merged.dropna(subset=["lat", "lon"])

m = folium.Map(location=[28.61, 77.20], zoom_start=11)
for _, row in merged.iterrows():
    folium.CircleMarker(
        location=[row["lat"], row["lon"]],
        radius=6,
        popup=f"{row['StationName']}<br>AQI: {row['AQI']}",
        color="green" if row["AQI_Bucket"] == "Good" else "red",
        fill=True
    ).add_to(m)

m.save("output/delhi_station_pollution_map.html")
