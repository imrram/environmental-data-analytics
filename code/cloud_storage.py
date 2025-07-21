import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
SUPABASE_BUCKET = os.getenv("SUPABASE_BUCKET")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def upload_folder_to_supabase(local_folder, supabase_folder=""):
    for root, _, files in os.walk(local_folder):
        for file in files:
            local_path = os.path.join(root, file)
            relative_path = os.path.relpath(local_path, local_folder)
            supabase_path = os.path.join(supabase_folder, relative_path).replace("\\", "/")
            with open(local_path, "rb") as f:
                res = supabase.storage.from_(SUPABASE_BUCKET).upload(supabase_path, f, {"upsert": True})
                print(f"Uploaded: {supabase_path} -> {res}")

if __name__ == "__main__":
    upload_folder_to_supabase("data")
