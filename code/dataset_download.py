import kagglehub
import shutil
import os

path = kagglehub.dataset_download("rohanrao/air-quality-data-in-india")

target_dir = os.path.join("data", "air-quality-data-in-india")
os.makedirs(target_dir, exist_ok=True)

for root, _, files in os.walk(path):
    for file in files:
        src = os.path.join(root, file)
        dst = os.path.join(target_dir, file)
        shutil.move(src, dst)

print(f"All files moved into {target_dir}")
