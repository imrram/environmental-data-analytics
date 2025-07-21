import pandas as pd

def load_pm25_data(filepath="data/air-quality-data-in-india/city_day.csv"):
    df = pd.read_csv(filepath, parse_dates=["Date"])
    df = df[df["City"] == "Delhi"]
    df = df[["Date", "PM2.5"]].dropna()
    return df

def load_global_temp(filepath="data/gistemp-global-temp/monthly.csv"):
    df = pd.read_csv(filepath)

    if "Year" in df.columns:
        try:
            df["Month"] = pd.to_datetime(df["Year"], format="%Y-%m")
        except:
            raise ValueError("Could not convert 'Year' to Month format (expected YYYY-MM)")
    else:
        raise ValueError("'Year' column not found in global temp data")

    df = df.rename(columns={"Mean": "GlobalTemp"})
    return df[["Month", "GlobalTemp"]]

def load_annual_temp(filepath="data/gistemp-global-temp/annual.csv"):
    df = pd.read_csv(filepath)
    df["Year"] = pd.to_datetime(df["Year"], format="%Y")
    df = df.rename(columns={"Mean": "GlobalTemp"})
    return df[["Year", "GlobalTemp"]]
