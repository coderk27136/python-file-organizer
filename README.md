# Bulk File Renamer & Organizer

Python script to batch rename files (add prefix/date) and organize them into subfolders by type. Perfect for freelance gigs like "Rename 1000 photos", "Sort my downloads folder", "Add date prefix to invoices".

## Features
- Add custom prefix (e.g., "project_")
- Add current date (YYYYMMDD)
- Move files to subfolders by extension (Images, Documents, etc.)
- Safe: skips non-files, handles errors

## How to Run
1. Clone repo: git clone http://github.com/coderk27136/python-file-organizer.git
2. Put files in a folder (e.g. "test_files")
3. Edit config in script (folder_path, prefix, etc.)
4. Run: python file_organizer.py

## Screenshots

![Before Running](before.png)  
![Terminal Output](terminal-output.png)  
![After Running – Organized](after.png)

No external libraries needed – uses built-in os & shutil.

Great for automation, file management, and batch processing tasks on Upwork/Fiverr.