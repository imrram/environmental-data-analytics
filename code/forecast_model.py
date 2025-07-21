import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import os

def forecast_pm25(df, city, periods=12):
    df = df[df["City"] == city]
    df["Date"] = pd.to_datetime(df["Date"])
    df = df[["Date", "PM2.5"]].dropna()

    # Monthly aggregation
    df["Month"] = df["Date"].dt.to_period("M")
    df_monthly = df.groupby("Month").mean().reset_index()
    df_monthly["Month"] = df_monthly["Month"].dt.to_timestamp()

    df_monthly = df_monthly.set_index("Month")
    
    model = ARIMA(df_monthly["PM2.5"], order=(2, 1, 2))
    fit = model.fit()
    forecast = fit.forecast(steps=periods)
    
    forecast_index = pd.date_range(start=df_monthly.index[-1] + pd.offsets.MonthBegin(),
                                   periods=periods, freq='MS')
    forecast_df = pd.DataFrame({"Forecast_PM2.5": forecast.values}, index=forecast_index)
    forecast_df.index.name = "Month"

    # Save forecast to CSV
    os.makedirs("data/forecasts", exist_ok=True)
    forecast_df.to_csv(f"data/forecasts/{city.lower()}_pm25_forecast.csv")
    
    return forecast_df
