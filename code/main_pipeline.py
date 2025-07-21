from ingest_pipeline import load_pm25_data, load_global_temp
from feature_engineering import aggregate_monthly_pm25, preprocess_global_temp
from forecast_model import forecast_pm25
from visualization import plot_pm25_vs_temp, plot_forecast
import pandas as pd
import os

pm25_raw = load_pm25_data()
temp_raw = load_global_temp()

pm25_monthly = aggregate_monthly_pm25(pm25_raw)
temp_processed = preprocess_global_temp(temp_raw)

merged = pd.merge(pm25_monthly, temp_processed, on="Month", how="inner")
os.makedirs("output", exist_ok=True)
merged.to_csv("output/merged_pm25_temp.csv", index=False)

plot_pm25_vs_temp(merged)
forecast = forecast_pm25(pm25_monthly)
plot_forecast(forecast)
