from statsmodels.tsa.arima.model import ARIMA

def forecast_pm25(df, periods=12):
    df = df.set_index("Month")
    model = ARIMA(df["PM2.5"], order=(2, 1, 2))
    fit = model.fit()
    forecast = fit.forecast(steps=periods)
    return forecast
