import os
import shutil
import kagglehub

# Step 1: Download dataset
path = kagglehub.dataset_download("kazanova/sentiment140")

# Step 2: Set target folder to current script directory
target_folder = os.path.dirname(os.path.abspath(__file__))

# Step 3: Copy dataset files to the current folder
for filename in os.listdir(path):
    src_file = os.path.join(path, filename)
    dest_file = os.path.join(target_folder, filename)
    if os.path.isfile(src_file):
        shutil.copy(src_file, dest_file)

print("✅ Dataset copied to:", target_folder)
