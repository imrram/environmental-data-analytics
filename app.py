import subprocess
import sys

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
run_script("code/dashboard.py")

print("\nAll scripts completed successfully.")
print("To launch the dashboard: streamlit run dashboard.py\n")
