import os
import shutil
import kagglehub

# Define dataset slugs
DATASETS = {
    "air-quality-data-in-india": "ram0007/air-quality-data-in-india",
    "gistemp-global-temp": "ram0007/gistemp-global-temp"
}

# Define destination folder
DEST_FOLDER = "data"

def is_data_empty():
    return not os.path.exists(DEST_FOLDER) or not any(os.scandir(DEST_FOLDER))

def safe_move(src_folder, dataset_name):
    dst_folder = os.path.join(DEST_FOLDER, dataset_name)
    os.makedirs(dst_folder, exist_ok=True)

    for filename in os.listdir(src_folder):
        src_file = os.path.join(src_folder, filename)
        dst_file = os.path.join(dst_folder, filename)
        shutil.move(src_file, dst_file)
        print(f"Moved {filename} to {dst_folder}")

def download_datasets():
    os.makedirs(DEST_FOLDER, exist_ok=True)

    for name, kaggle_id in DATASETS.items():
        print(f"Downloading: {name}...")
        dataset_path = kagglehub.dataset_download(kaggle_id)
        safe_move(dataset_path, name)
        print(f"Downloaded and moved: {name}\n")

if is_data_empty():
    print("Data folder is empty. Fetching datasets...")
    download_datasets()
else:
    print("Data already exists. Skipping download.")
