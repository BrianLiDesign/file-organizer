# main.py
# Author: Brian Li
# Description: Organizes files into folders based on their extensions.

import os
import shutil


path = input("Enter the path to the folder you want to organize: ")
files = os.listdir(path)

DESTINATIONS = {
    "Photos": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp", ".heic"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx", ".odt"],
    "Audios": [".mp3", ".wav", ".aac", ".flac", ".m4a"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".wmv"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c"],
    "Miscellaneous": []
}

for file in files:
    file_path = os.path.join(path, file)
    
    if os.path.isfile(file_path):
        ext = file.split('.')[-1] if '.' in file else 'no_extension'
        
        # Create a directory for the extension if it doesn't exist
        ext_dir = os.path.join(path, ext)
        if not os.path.exists(ext_dir):
            os.makedirs(ext_dir)
        
        # Move the file to the corresponding directory
        shutil.move(file_path, os.path.join(ext_dir, file))
        print(f"Moved {file} to {ext_dir}")

print("Files have been organized by their extensions.")