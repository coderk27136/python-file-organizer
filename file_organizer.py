# Bulk File Renamer & Organizer
# Renames files with prefix/date + organizes by file type into subfolders
# Great for freelance gigs: rename photos, sort downloads, batch file tasks

import os
import shutil
from datetime import datetime

# === CONFIG ===
folder_path = "test_files"          # Change to your target folder
prefix = "renamed_"                 # e.g. "project_", "2026_"
add_date = True                     # Add YYYYMMDD prefix?
organize_by_type = True             # Create subfolders like Images, Documents?

# File type categories (add more as needed)
type_folders = {
    '.jpg':  'Images',
    '.jpeg': 'Images',
    '.png':  'Images',
    '.gif':  'Images',
    '.pdf':  'Documents',
    '.docx': 'Documents',
    '.txt':  'Text',
    '.csv':  'Data',
    '.xlsx': 'Data',
    # Add your own: '.mp4': 'Videos', etc.
}

print(f"Processing folder: {os.path.abspath(folder_path)}\n")

if not os.path.exists(folder_path):
    print("Error: Folder not found!")
    exit()

processed = 0
moved = 0

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    # Skip directories and hidden files
    if not os.path.isfile(file_path) or filename.startswith('.'):
        continue

    name, ext = os.path.splitext(filename)
    ext = ext.lower()

    # Build new filename
    new_name = filename
    if add_date:
        date_str = datetime.now().strftime("%Y%m%d")
        new_name = f"{date_str}_{new_name}"
    if prefix:
        new_name = f"{prefix}{new_name}"

    new_file_path = os.path.join(folder_path, new_name)

    # Rename if needed
    if new_file_path != file_path:
        try:
            os.rename(file_path, new_file_path)
            print(f"Renamed: {filename} → {new_name}")
            processed += 1
            file_path = new_file_path  # update path for moving
        except Exception as e:
            print(f"Rename failed for {filename}: {e}")
            continue

    # Organize into subfolder by type
    if organize_by_type and ext in type_folders:
        subfolder_name = type_folders[ext]
        subfolder_path = os.path.join(folder_path, subfolder_name)

        os.makedirs(subfolder_path, exist_ok=True)

        dest_path = os.path.join(subfolder_path, new_name)

        try:
            shutil.move(file_path, dest_path)
            print(f"Moved: {new_name} → {subfolder_name}/")
            moved += 1
        except Exception as e:
            print(f"Move failed for {new_name}: {e}")

print(f"\nDone!")
print(f"Renamed files: {processed}")
print(f"Moved to subfolders: {moved}")
print("Check your folder for results!")