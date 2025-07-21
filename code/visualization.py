import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_pm25_vs_temp(df, output_dir="output"):
    os.makedirs(output_dir, exist_ok=True)
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x="Month", y="PM2.5", label="PM2.5")
    sns.lineplot(data=df, x="Month", y="GlobalTemp", label="Global Temp")
    plt.title("Delhi PM2.5 vs Global Temperature")
    plt.savefig(f"{output_dir}/pm25_temp_trend.png")
    plt.close()

def plot_forecast(forecast, output_dir="output"):
    plt.figure(figsize=(10, 5))
    forecast.plot(title="Forecasted PM2.5")
    plt.savefig(f"{output_dir}/pm25_forecast.png")
    plt.close()
