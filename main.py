# main.py
# Author: Brian Li
# Description: Organizes files into folders based on their extensions.

import os
import shutil


path = input("Enter the path to the folder you want to organize: ")
files = os.listdir(path)

for file in files:
    file_path = os.path.join(path, file)
    
    if os.path.isfile(file_path):
        # Get the file extension
        ext = file.split('.')[-1] if '.' in file else 'no_extension'
        
        # Create a directory for the extension if it doesn't exist
        ext_dir = os.path.join(path, ext)
        if not os.path.exists(ext_dir):
            os.makedirs(ext_dir)
        
        # Move the file to the corresponding directory
        shutil.move(file_path, os.path.join(ext_dir, file))
        print(f"Moved {file} to {ext_dir}")
        
print("Files have been organized by their extensions.")