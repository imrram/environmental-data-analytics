import subprocess
import sys
# from .code.cloud_storage import upload_folder_to_supabase
# from .code.forecast_model import forecast_pm25
import pandas as pd

def run_script(script_name):
    print(f"Running {script_name} ...")
    result = subprocess.run(["python3.10", script_name])
    if result.returncode != 0:
        print(f"{script_name} failed. Stopping execution.")
        sys.exit(1)

print("\nStarting Full Capstone Pipeline...\n")

run_script("code/dataset_download.py")
run_script("code/main_pipeline.py")
run_script("code/map_station_pollution.py")
run_script("code/clustering_anomaly.py")
# upload_folder_to_supabase("data")


# data = pd.read_csv("data/air-quality-data-in-india/city_day.csv")
# forecast = forecast_pm25(data, city="Delhi", periods=12)


print("\nAll scripts completed successfully.")
print("To launch the dashboard: streamlit run code/dashboard.py\n")
