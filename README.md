# Environmental Data Analytics Project

Capstone Project – EcoSphere Institute  

---

## Overview

This project addresses the challenges of climate change and urban air pollution by leveraging large-scale environmental datasets. The goal is to build a robust data analytics pipeline for:

- Forecasting air quality (PM2.5)
- Clustering polluted cities
- Detecting anomalies in AQI readings
- Visualizing pollution trends with a dashboard
- Correlating pollution with global temperature anomalies

---

## Datasets Used

### 1. Air Quality in India
- Source: Kaggle
- Dataset: https://www.kaggle.com/datasets/ram0007/air-quality-data-in-india
- Files: city_day.csv, city_hour.csv, station_day.csv, station_hour.csv, stations.csv

### 2. Global Temperature (GISTEMP)
- Source: Kaggle
- Dataset: https://www.kaggle.com/datasets/ram0007/gistemp-global-temp
- Files: monthly.csv, annual.csv

---

## Project Structure

```
├── data/                       # Automatically downloaded datasets
│   ├── air-quality-data-in-india/
│   └── gistemp-global-temp/
├── download_data.py           # Downloads data using kagglehub
├── ingest_pipeline.py         # Cleans and ingests datasets
├── feature_engineering.py     # Aggregates and transforms data
├── forecast_model.py          # PM2.5 forecasting with Prophet
├── clustering.py              # City clustering with KMeans
├── anomaly_detection.py       # Isolation Forest for outliers
├── visualization.py           # Plotting and mapping tools
├── app.py                     # Streamlit dashboard
├── run_all.py                 # Runs full pipeline
├── README.md                  # Project documentation
```

---

## Setup Instructions

### 1. Clone the Repository
```
git clone https://github.com/imrram/environmental-data-analytics.git
cd environmental-data-analytics
```

### 2. Install Required Packages
```
pip install -r requirements.txt
```

### 3. Run the Project
```
python run_all.py
```

This script will:
- Check if the `data/` folder is empty
- Automatically download both datasets using kagglehub
- Run ingestion, feature engineering, clustering, forecasting, and visualization steps

### 4. Launch Dashboard
```
streamlit run dashboard.py
```
Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## Dashboard Features

- PM2.5 vs Global Temperature trend analysis
- Monthly and daily forecasts of PM2.5
- KMeans clustering of cities based on pollutant composition
- Anomaly detection highlighting critical AQI spikes
- Geospatial map of Delhi station AQI levels

---

## Dependencies

- Python 3.10+
- pandas, numpy, scikit-learn
- prophet
- folium, geopy
- streamlit
- kagglehub

Install all via:
```
pip install -r requirements.txt
```

---

## Data Handling Note

To avoid GitHub file size limits, the `data/` folder is excluded via `.gitignore`. When you run the project, it will automatically pull the datasets from Kaggle using `kagglehub` if the folder is empty.

---
