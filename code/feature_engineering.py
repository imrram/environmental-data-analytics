def aggregate_monthly_pm25(df):
    df["Month"] = df["Date"].dt.to_period("M").dt.to_timestamp()
    return df.groupby("Month")["PM2.5"].mean().reset_index()

def preprocess_global_temp(df):
    df["Month"] = df["Month"].dt.to_period("M").dt.to_timestamp()
    return df
